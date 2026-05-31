---
id: 859
url: https://georgeguimaraes.com/your-agent-orchestrator-is-just-a-bad-clone-of-elixir/
title: 'Your Agent Framework Is Just a Bad Clone of Elixir: Concurrency Lessons from
  Telecom to AI'
domain: georgeguimaraes.com
source_date: '2026-02-19'
tags:
- elixir
- distributed-systems
- ai
- python
summary: The article argues that modern AI agent frameworks are essentially reinventing
  the actor model that Erlang/Elixir's BEAM virtual machine has successfully implemented
  since 1986. AI agents require handling thousands of long-lived concurrent connections
  with isolated state and message passing—a problem the BEAM was originally designed
  to solve for telephone switches—whereas popular Python frameworks like LangGraph,
  Langroid, and AutoGen are building these abstractions on top of languages that don't
  natively support them. The author contends that using Elixir and the BEAM for agent
  orchestration isn't a stylistic choice but an architectural necessity, as the runtime
  already provides battle-tested solutions for concurrency, fault recovery, process
  supervision, and distributed communication that Python frameworks are struggling
  to recreate.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Your Agent Framework Is Just a Bad Clone of Elixir: Concurrency Lessons from Telecom to AI

**Follow-up:** This post got some fair pushback on [Hacker News](https://news.ycombinator.com/item?id=47067395&ref=georgeguimaraes.com). I wrote a follow-up addressing the three most valid criticisms: [Elixir/BEAM Doesn't Solve Everything for AI Agents](https://georgeguimaraes.com/what-the-critics-got-right-about-elixir-and-ai-agents/).

---

Recently, José Valim published ["Why Elixir is the Best Language for AI"](https://dashbit.co/blog/why-elixir-best-language-for-ai?ref=georgeguimaraes.com), citing a Tencent study showing Elixir achieved the highest LLM code completion rate across 20 languages. Claude Opus 4 scored 80.3% on Elixir problems versus 74.9% for C#, the next-best performer.

But there's a deeper argument than "LLMs write good Elixir." It's this: **the actor model that Erlang introduced in 1986 is the agent model that AI is rediscovering in 2026.** Every pattern the Python AI ecosystem is building (isolated state, message passing, supervision hierarchies, fault recovery) already exists in the BEAM virtual machine. And it's been running telecom switches, WhatsApp, and Discord at scale for decades.

I've been building agentic commerce infrastructure at New Generation. Before that, I shipped a full AI stack serving more than 3 million merchants at a unicorn Brazilian fintech. Both systems run on Elixir. Here's why that's not a hipster language choice. It's an architectural inevitability.

> **A note on terminology:** Throughout this post I refer to "the BEAM." BEAM is the virtual machine that runs both Erlang and Elixir code, similar to how the JVM runs both Java and Kotlin. Erlang (1986) created the VM and the concurrency model. Elixir (2012) is a modern language built on top of it with better ergonomics. When I say "BEAM," I mean the runtime and its properties. When I say "Elixir," I mean the language we write.

---

The 30-second request problem
-----------------------------

Traditional web frameworks were designed for a world where requests take milliseconds. A user clicks, the server queries a database, renders HTML, responds in under 100ms. Rails, Django, Laravel: all optimized for this pattern.

AI agents broke that model. When a user asks an agent a question, the response takes 5 to 30 seconds. The agent calls an LLM, waits for streaming tokens, maybe invokes a tool, calls the LLM again, streams more tokens. One "request" might involve three round-trips to an LLM API, two database lookups, and a web search. And the connection stays open the entire time.

Now multiply that by 10,000 concurrent users. Each one holding an open connection for 15+ seconds. Traditional thread-per-request frameworks choke. You need async, you need concurrency, you need to hold thousands of long-lived connections without burning through memory.

The BEAM was built for exactly this. Ericsson designed it for telephone calls: the original long-lived connections. Each call holds state, runs for minutes, and the system needs to handle millions of them concurrently. BEAM lightweight processes are ~2KB each. You can spawn millions of them. Each one has its own heap, its own garbage collector, and is preemptively scheduled so no single process can hog the CPU.

Node.js handles this reasonably well too, thanks to its event loop and async model. But there are key differences:

* **Single-threaded vs. preemptive scheduling.** Node.js runs on one thread (worker threads aside). If one agent does CPU-intensive work (tokenization, JSON parsing of a large response, embedding computation) it blocks every other agent on that process. BEAM preemptively switches between its lightweight processes every 4,000 reductions. No process can starve others.
* **Process isolation.** In Node.js, one unhandled exception in an async handler can crash the process, affecting all connections. On the BEAM, each agent is an isolated process with its own memory. One crash affects nothing else.
* **Garbage collection.** Node.js has stop-the-world GC pauses that affect all connections. BEAM garbage collects per process: tiny, incremental, unnoticeable. At 10,000 concurrent agent sessions, this matters a lot.
* **Native distribution.** Need to scale beyond one machine? BEAM processes can communicate across nodes transparently. In Node.js, you're setting up Redis pub/sub, message queues, or custom clustering.

Phoenix (Elixir's web framework) already handles this pattern for real-time apps. Phoenix Channels and LiveView routinely hold 100,000+ concurrent WebSocket connections on a single server. An AI agent chat session is just another long-lived connection. Nothing special from the runtime's perspective.

---

The pattern everyone is reinventing
-----------------------------------

Look at what the major Python agent frameworks are building and you'll see a pattern.

[Langroid](https://github.com/langroid/langroid?ref=georgeguimaraes.com) is the most explicit about it. Their README says the multi-agent paradigm is "inspired by the [Actor Framework](https://en.wikipedia.org/wiki/Actor_model?ref=georgeguimaraes.com)." Agents are "message transformers" that communicate through direct message passing. This is, almost literally, the actor model.

[LangGraph](https://github.com/langchain-ai/langgraph?ref=georgeguimaraes.com) takes a different approach: agents are nodes in a stateful graph with shared state flowing through reducers. They [internally refer to these as "state machines."](https://blog.langchain.com/langgraph/?ref=georgeguimaraes.com) The core abstraction is a `StateGraph` where nodes read from and write to shared state, with conditional edges controlling flow.

[CrewAI](https://github.com/crewAIInc/crewAI?ref=georgeguimaraes.com) organizes agents into "crews" that coordinate through task output passing and delegation. When one agent finishes a task, its output becomes context for the next. Agents can also delegate subtasks to each other. All agents in a crew share memory (short-term, long-term, entity) when enabled.

And then there's [AutoGen](https://github.com/microsoft/autogen?ref=georgeguimaraes.com). Microsoft's framework started in v0.2 as conversation-driven: agents exchanged messages in defined patterns (two-agent chat, group chat, sequential chat). But when they rebuilt it for v0.4, they went straight to what they call an "event-driven actor framework" with asynchronous message passing and runtime-managed agent lifecycles. The framing is telling: they arrived at the actor model independently, because the problem demands it.

How close did they get? AutoGen 0.4's agents communicate through messages, have runtime-managed lifecycles, and can run distributed across processes. That sounds like actors. But under the hood, it's single-threaded Python asyncio. There's no preemptive scheduling, no per-agent garbage collection, no supervision trees, no "let it crash" recovery. Their message layer is a hybrid of synchronous RPC (request/response) and async pub/sub (events), which is pragmatic but not the clean message-passing semantics of true actors. It's the actor model as aspiration, not as runtime. They're building the abstractions on top of a language that doesn't natively support them.

Each framework takes a different path, but they're all converging on the same set of problems:

* **How do agents communicate?** Message passing (Langroid, AutoGen 0.4), shared state (LangGraph), or task output chaining (CrewAI).
* **How do you orchestrate workflows?** State graphs (LangGraph), task sequences (CrewAI), conversation patterns (AutoGen), or task loops (Langroid).
* **How do you handle failure?** LangGraph has retry policies and checkpointing. The others rely on application-level try/except.
* **How do you manage agent lifecycles?** AutoGen 0.4's runtime creates and tracks agent instances. The others mostly leave this to the developer.

Now compare these to OTP, the Erlang Open Telecom Platform, formalized in 1998 for telephone switches that needed to handle millions of concurrent calls with zero downtime:

| Problem | BEAM/OTP Primitive | Battle-tested since |
| --- | --- | --- |
| Agent with isolated state | Erlang process | 1986 |
| Agent communication | Message passing (`send`/`receive`) | 1986 |
| Workflow orchestration | `Supervisor` trees | 1998 |
| Error recovery | `Supervisor` restart strategies | 1998 |
| Agent registry/discovery | `:global` process registry | 1998 |
| Event broadcasting | Process groups (`:pg`) | 1998 |
| State persistence | `ETS` (in-memory storage) | 1998 |
| Distributed agents | Built-in distribution | 1990 |

Every one of these is a solved problem on the BEAM. Not as a library. As the runtime. Isolated state, message passing, supervision, fault recovery, process registry, event broadcasting, distributed communication: all built into the runtime.

---

Let it crash (and why that's perfect for AI agents)
---------------------------------------------------

This is where the BEAM's philosophy pays off.

AI agents are inherently non-deterministic. LLM calls return different results every time. Tool calls fail unpredictably. Rate limits hit without warning. Context windows overflow. JSON parsing breaks because the model hallucinated invalid syntax. Timeouts happen because the API provider is having a bad day.

In Python, you deal with this through defensive coding. Every LLM call gets wrapped in try/except. Every tool invocation gets retry logic. You build error state management, fallback chains, exponential backoff. The happy path disappears under layers of error handling.

```
# The Python way: wrap everything defensively
try:
    response = await llm.chat(messages)
except (RateLimitError, TimeoutError, JSONDecodeError) as e:
    logger.error(f"LLM call failed: {e}")
    response = fallback_response()
# Repeat for every tool call, every API request, every parse step.
```

The BEAM's "let it crash" philosophy takes the opposite approach. Instead of anticipating every failure mode, you write the happy path and let processes crash. The supervisor detects the crash and restarts the process in a clean state. The rest of the system continues unaffected.

```
# The Elixir way: write the happy path, supervise the rest
defmodule AIAgent do
  use GenServer

  def handle_call({:ask, question}, _from, state) do
    response = LLM.chat(state.messages ++ [question])
    tool_result = Tools.execute(response.tool_call)
    final = LLM.chat(state.messages ++ [response, tool_result])
    {:reply, final, %{state | messages: state.messages ++ [question, final]}}
  end
  # No try/catch. If the LLM times out, returns garbage,
  # or the tool crashes: the process crashes.
  # The supervisor restarts it cleanly.
end

defmodule AgentSupervisor do
  use Supervisor

  def init(_) do
    children = [
      {AIAgent, name: :research_agent},
      {AIAgent, name: :coding_agent},
      {AIAgent, name: :review_agent}
    ]
    # One crashes? Restart just that one. Others keep working.
    Supervisor.init(children, strategy: :one_for_one)
  end
end
```

This matters for AI agents because **you cannot predict all failure modes of non-deterministic systems.** No amount of defensive coding will cover every way an LLM can surprise you. The model might return a response in a language you didn't expect. It might call a tool that doesn't exist. It might enter an infinite loop of self-correction.

With supervision trees, you don't need to predict these failures. You need to define recovery strategies: restart the agent, restart it with different parameters, restart the whole conversation, or give up after N attempts. The runtime handles the rest.

In LangGraph, you'd need external infrastructure to get equivalent reliability. In Elixir, it's a few lines of code and the runtime.

---

Hot code swapping: update agents without downtime
-------------------------------------------------

The BEAM supports hot code loading. You can deploy new code to a running system without stopping it. Running processes continue executing the old code until they're ready to switch, then seamlessly pick up the new version.

Think about what happens when you need to update an agent's behavior in production:

* You refined a system prompt after discovering edge cases
* You need to add a new tool to an agent's toolkit
* You want to change the decision logic for when agents escalate to humans
* You need to patch a bug in how agents parse LLM responses

In a Python deployment, you restart the process. Every in-flight conversation is dropped. Users get disconnected. Active conversations are lost. You either accept the disruption or build complex blue/green deployment infrastructure with state serialization and session draining.

On the BEAM, you deploy the new code and running agents pick it up on their next message. An agent in the middle of a negotiation finishes its current turn with the old code and processes the next message with the new code. No connections dropped. No state lost. No downtime.

Ericsson built this because you can't tell a million phone callers "please hold while we update the switch." The same principle applies to AI agents: you can't tell a thousand agents mid-task to stop and restart.

---

Why this matters now
--------------------

AI workloads are shifting from single-shot inference to long-running, multi-agent systems. Coding agents that spin up dozens of sub-agents in parallel. Customer support agents that hold conversations for minutes while calling internal APIs. Research agents that coordinate search, synthesis, and verification across multiple models. Commerce agents that negotiate prices and execute transactions autonomously. McKinsey projects AI agents could mediate $3-5 trillion of global commerce alone by 2030.

The common thread: you need infrastructure that can handle thousands of concurrent agents, each with its own state, communicating asynchronously, failing gracefully, and recovering automatically. This is not a hypothetical workload. It's what every serious agent deployment looks like today.

This is literally what the BEAM was built for. Ericsson needed to route millions of phone calls with five-nines uptime. Phone calls are conversations between parties, maintaining state, with strict latency requirements, where individual calls can fail without bringing down the switch. Swap "phone calls" for "agent sessions" and the requirements are identical.

---

The gaps (and how we're filling them)
-------------------------------------

My original ["hot take"](https://georgeguimaraes.com/ai-agentic-frameworks-are-building-their-own-erlang-elixir/) on this topic identified two gaps in the Elixir ecosystem for AI agents: **message exchange tooling** and **testability**.

The message exchange gap is mostly closed. [Elixir's LangChain library](https://github.com/brainlid/langchain?ref=georgeguimaraes.com) (which, despite the name, is well-designed and deserves its own reputation) provides step mode for controlled agent execution, while [ReqLLM](https://github.com/agentjido/req_llm?ref=georgeguimaraes.com) offers a nimbler alternative for LLM integration. [Jido](https://github.com/agentjido/jido?ref=georgeguimaraes.com) provides a full agentic framework. [Phoenix Channels](https://hexdocs.pm/phoenix/channels.html?ref=georgeguimaraes.com) and [PubSub](https://hexdocs.pm/phoenix_pubsub/Phoenix.PubSub.html?ref=georgeguimaraes.com) handle real-time agent communication at scale.

Testability is what I've been working on with [Tribunal](https://github.com/georgeguimaraes/tribunal?ref=georgeguimaraes.com), an LLM evaluation framework for Elixir that integrates with ExUnit:

```
test "agent response is faithful to context" do
  response = MyAgent.answer("What's our return policy?", context: @policy_doc)

  assert_faithful response, @policy_doc
  refute_hallucination response
  refute_bias response
end
```

The goal is making AI agent testing as natural as testing any other Elixir code. Because agents *are* just processes, and processes are testable.

---

Could you reinvent this in Python or TypeScript?
------------------------------------------------

The natural objection: "Sure, the BEAM has all this, but couldn't we just build it in Python or TypeScript?"

People have tried. Here's what you run into.

**Python**: The GIL prevents true parallel execution of lightweight processes. asyncio gives you concurrency but not isolation: all coroutines share the same memory space, and one bad coroutine can corrupt state for everyone else. There's no per-coroutine garbage collection, so a memory-hungry agent affects the whole process. And supervision? It's just try/except with extra steps. You can't restart a coroutine in a clean state without rebuilding it from scratch, and you can't do that transparently. Even with Python 3.13, which has no GIL, it'll take a long time for libraries and frameworks to adapt to it.

**TypeScript/Node.js**: Better concurrency story thanks to the event loop, but still fundamentally single-threaded. Worker threads exist but they're heavyweight OS threads, not 2KB processes. There's no preemptive scheduling: one CPU-bound operation blocks everything. No hot code swapping. No built-in distribution across nodes.

**Others have tried building actor runtimes on top of existing VMs.** Akka on the JVM got the closest, with proper supervision trees and location-transparent actors. Microsoft Orleans brought virtual actors to .NET. Both prove the point: you need deep runtime support to make actors work well, and both required massive engineering effort to approximate what the BEAM provides out of the box.

My honest answer is that you can get about 70% there with enough engineering. The remaining 30% (preemptive scheduling, per-process garbage collection, hot code swapping, true fault isolation between agents) requires runtime-level support. You can't bolt these onto a language that wasn't designed for them. That's not a criticism of Python or TypeScript. It's just not what they were built to do.

---

The uncomfortable truth
-----------------------

The uncomfortable truth: **you're not building something new. You're rebuilding telecom infrastructure in a language that wasn't designed for it.**

The industry is starting to notice. There's a growing trend of teams prototyping agents in Python, then rewriting in TypeScript for production. The reasoning is practical: Node.js handles concurrent connections better, the async story is more mature, and the deployment story for serverless and edge is simpler. Anecdotally, a significant share of recent YC agent startups chose TypeScript over Python for their production stack. But as we saw above, Node.js only solves half the problem. You get better concurrency, but you still don't get process isolation, supervision, or fault tolerance. You're trading one set of limitations for a slightly better set.

The BEAM was designed for exactly this problem. And Elixir makes it accessible.

I'm not saying everyone should rewrite their agent systems in Elixir. But if you're starting something new, especially if you're building infrastructure that needs to handle thousands of concurrent agents with production reliability, you might want to look at the technology that's been doing this for 40 years. And Elixir is easier to pick up than you'd expect: the syntax is clean, the tooling is excellent, and LLMs write it remarkably well.

---

Where to go from here
---------------------

If you're curious:

* José Valim's ["Why Elixir is the Best Language for AI"](https://dashbit.co/blog/why-elixir-best-language-for-ai?ref=georgeguimaraes.com) covers the LLM-friendliness angle
* [Elixir's LangChain](https://github.com/brainlid/langchain?ref=georgeguimaraes.com) is the best LLM integration library in the ecosystem
* [Jido](https://github.com/agentjido/jido?ref=georgeguimaraes.com) is a full agentic framework built on OTP principles
* [Bumblebee](https://github.com/elixir-nx/bumblebee?ref=georgeguimaraes.com) lets you run transformer models directly in your supervision tree
* My [awesome-ml-gen-ai-elixir](https://github.com/georgeguimaraes/awesome-ml-gen-ai-elixir?ref=georgeguimaraes.com) list covers the full ecosystem
