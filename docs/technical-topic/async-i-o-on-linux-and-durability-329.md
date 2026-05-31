---
id: 329
url: https://blog.canoozie.net/async-i-o-on-linux-and-durability/
title: Async I/O on Linux and durability
domain: blog.canoozie.net
source_date: '2025-07-20'
tags:
- database
- distributed-systems
- tutorial
summary: The author explores how Linux's **io_uring** can dramatically improve database
  performance by enabling truly asynchronous I/O operations, but discovers this creates
  durability challenges. To solve this, they implement a **dual write-ahead log (WAL)
  design** that separates intent records (what operations to perform) from completion
  records (confirmation of success), allowing async writes while maintaining consistency
  guarantees. This approach achieves a 10x throughput improvement through intelligent
  batching, demonstrating that modern async I/O tools could fundamentally reshape
  database architectures.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Async I/O on Linux and durability

I've been working on a complex multi-model database for a few weeks now, and recently I took time to simplify and test out an idea I had on a simple key-value database. I started with the basics: A hash table in memory, a simple append-only log for persistence and durability, and the classic fsync() call after every write to the log for durability.

It worked, but wasn't as fast as it could be.

In [Kevo](https://github.com/KevoDB/kevo?ref=blog.canoozie.net), that's the approach I use, but in Klay (not public yet, but will be open sourced when ready), I'm taking a different approach. What would a database look like if you treated the individual sectors on disk as unreliable, and how could you make it as fast as possible?

That's when I started reading about io\_uring on Linux [here (PDF)](https://kernel.dk/io_uring.pdf?ref=blog.canoozie.net) and [here](https://developers.mattermost.com/blog/hands-on-iouring-go/?ref=blog.canoozie.net).

io\_uring... what?
------------------

You can read [Wikipedia](https://en.wikipedia.org/wiki/Io_uring?ref=blog.canoozie.net) as good as the next person, so let's skip ahead.

The promises seem to good to be true: truly async I/O for all types of operations, not just network sockets. No more thread pools to work around blocking disk I/O, no more complex state machines built around `epoll`... What's the catch?

Well, after doing some reading, the core insight behind io\_uring clicked almost immediately. Traditional I/O interfaces force you to think synchronously--you make a system call, the kernel does work, you get a result. But modern storage hardware is inherently parallel. An NVMe SSD can handle thousands of operations simultaneously, and together, each with its own queue. The bottleneck isn't the hardware; it's the software abstraction.

io\_uring exposes this parallelism through a pair of ring buffers shared between your application and the kernel. You submit operations to the submission queue (SQ) and collect results from the completion queue (CQ). Instead of one system call per operation, you can submit dozens of operations with a single `io_uring_submit` call.

My first io\_uring experiment was simple: Replace my synchronous WAL writes with async ones. Instead of writing each log entry and waiting for completion, I would submit the write operation and continue processing. The results were dramatic--throughput increased by an order of magnitude almost immediately.

But then I started hitting consistency issues...

Durability
----------

The problem with naive async I/O in a database context at least, is that you lose the durability guarantee that makes databases useful. When a client receives a success response, their expectation is the data will survive a system crash. But with async I/O, by the time you send that response, the data might still be sitting in kernel buffers, not yet written to stable storage.

My initial solution was to track pending I/O operations and only return success after the corresponding completion arrived from io\_uring. This worked, but it defeated the purpose--I was back to waiting for disk I/O before completing transactions.

Clearly, I need a better approach.

Rethinking my WAL
-----------------

The traditional [write-ahead log](https://en.wikipedia.org/wiki/Write-ahead_logging?ref=blog.canoozie.net) (WAL) protocol is simple: log the change, force it to disk, then apply it. But what if we could separate the "intent to change" from the "confirmation of the change"? What if we could log our intentions quickly and asynchronously, then confirm completion separately?

That led me to a [TigerBeetle talk](https://www.youtube.com/watch?v=tRgvaqpQPwE&ref=blog.canoozie.net) being given by Joran Dirk Greef. Turns out, TigerBeetle uses the same sort of approach. The more I learned about TigerBeetle, the more I had confidence in the approach. (Note: TigerBeetle doesn't externalize commits asynchronously though, see clarification in [this X post](https://x.com/jorandirkgreef/status/1946200867163541708?ref=blog.canoozie.net).)

So I set out to experiment with a dual WAL design, in a simple in-memory key-value database, that used the dual WAL design:

1. **Intent WAL**: Records what operations I plan to perform
2. **Completion WAL**: Records successful completion of these operations

So the protocol ends up becoming:

1. Write intent record (async)
2. Perform operation in memory
3. Write completion record (async)
4. Wait for the completion record to be written to the WAL
5. Return success to client

During recovery, I only apply operations that have both intent and completion records. This ensures consistency while allowing much higher throughput.

**Update**: *It's critical to note that while both WAL writes are submitted asynchronously, we must wait for the completion record to be durably written before responding to the client. This is tracked through io\_uring's completion queue - we only send a success response after receiving confirmation that the completion record has been persisted to stable storage. Without this guarantee, we'd violate durability expectations and risk data loss if the system crashes between sending the response and the actual disk write.*

Building the Dual WAL System
----------------------------

Alright, I'm also using Zig for this, since Klay is being written in Zig, I kept [Poro (GitHub)](https://github.com/jeremytregunna/poro?ref=blog.canoozie.net) using Zig as well to reduce the things I needed to keep in my head at once. In case it's not obvious, and it may not be, Poro is the experimental key-value database with the dual WAL system implemented as a demo.

Implementing this approach requires attention to several details. First, I need to separate io\_uring instances--one for each WAL type. This prevents head-of-line blocking where completion writes might wait behind intent writes.

```
pub const WAL = struct {
    intent_ring: io_uring,              // Dedicated ring for intent ops
    completion_ring: io_uring,          // Dedicated ring for completions
    intent_file_fd: std.posix.fd_t,
    completion_file_fd: std.posix.fd_t,
    intent_buffer: []u8,                // Circular buffer
    completion_buffer: []u8,            // Circular buffer
};
```

The circular buffers are crucial for performance. Instead of writing individual entries to disk, I batch them into large buffers and flush only when they reach 75% capacity. This maximizes the benefits of io\_uring's batching capabilities.

Each completion entry includes a checksum and references back to the corresponding intent entry:

```
pub const CompletionEntry = struct {
    intent_offset: u32,  // Links back to intent entry
    timestamp: i64,      // Timestamp of completion record
    status: Status,      // Success, I/O error, or checksum error enum
    checksum: u32,       // CRC32 verification of key+value
};
```

### The Recovery Process

The recovery algorithm becomes more complex but much more robust:

1. Read the entire intent log to see what operations were attempted
2. Read the entire completion log to see what operations completed successfully
3. Build a hash map linking intent entries to completion entries
4. Replay only the operations that have successful completion entries
5. Verify the checksums to ensure data integrity.

This approach handles partial failures gracefully. If the system crashes between writing an intent record and its corresponding completion record, the operation is simply ignored during recovery--as if it never happened. In a networked database with replication, you can enhance this failure case by asking the cluster if any replica has the data, and if so, you can repair your version.

### Addressing latency vs batch performance

The dual WAL design does introduce a latency cost for individual operations - instead of one synchronous write, we now have two writes that must complete before responding to the client. For single operations, this could theoretically double the latency.

However, the real performance win comes from batch processing. When multiple clients are writing concurrently, we can:

* Submit dozens of intent records in a single io\_uring batch
* Process all operations in memory while those writes are in flight
* Submit all completion records as another batch
* Wait for all completions together

This batching transforms what would be 2N synchronous writes (for N operations) into just 2 io\_uring submissions plus waiting for completions. The amortized cost per operation drops dramatically as batch size increases. In practice, under load, the system achieves a throughput improvement when it's processing many operations in parallel rather than serializing them one by one.

### Performance Breakthrough

The results exceeded by expectations. Benchmarks showed a 10x improvement in transaction throughput compared to my original synchronous implementation. More importantly, the system now scales with the number of CPU cores rather than being bottlenecked by disk I/O serialization.

io\_uring's design aligns perfectly with the dual WAL approach. Each WAL can have its own ring buffer, preventing I/O contention. Operations can be batched and submitted together, reducing system call overhead. Finally, the completion queue provides precise information about which operations have finished, the result of that completion, enabling more sophisticated recovery logic than "uhh error, throw this and everything after away."

What I learned
--------------

Working through this implementation taught me several important lessons:

**Hardware parallelism matters**: Modern storage devices can handle thousands of concurrent operations. Traditional I/O interfaces hide this parallelism behind synchronous abstractions.

**Batching is critical**: The overhead of individual I/O operations is significant. Batching multiple operations together provides a major performance improvements.

**Consistency models are flexible**: By separating intent from completion, we can maintain strong consistency guarantees while achieving much higher performance.

**Recovery can be sophisticated**: More complex recovery algorithms enable simpler runtime protocols. So the effort invested in recovery logic pays dividends in operational performance.

The Broader Impact
------------------

This experiment changed how I think about database architecture. When I/O becomes cheap and parallel, many traditional design decisions need to be reconsidered. Buffer pool management, transaction scheduling, and concurrency control all benefit from rethinking around async I/O primitives.

Sometimes, the best optimizations come from questioning how we've done things in the past. In this case, the assumption that I/O must be synchronous to have durable database storage, turned out to be wrong. The hardware was always parallel--we just needed software architectures that could take advantage of it.
