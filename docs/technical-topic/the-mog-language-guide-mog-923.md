---
id: 923
url: https://moglang.org/#fft-on-tensors
title: The Mog Language Guide | Mog
domain: moglang.org
source_date: '2026-03-09'
tags:
- ai
- github-repo
- tutorial
summary: Mog is a programming language designed specifically for AI agents, featuring
  a comprehensive guide that covers fundamentals like variables, types, and control
  flow through advanced topics including async programming, error handling, and tensor
  operations. The language emphasizes safety through its capability system for controlled
  I/O access and supports embedding in host applications with clear resource limits
  and sandboxing. Key features include support for higher-order functions, structs,
  collections, and N-dimensional arrays, making it suitable for building secure, embeddable
  AI agent scripts.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# The Mog Language Guide | Mog

Contents
[Back to top](#guide)

1. [Mog: A Programming Language for AI Agents](#mog-a-programming-language-for-ai-agents)
2. [Overview](#overview)
3. [Examples](#examples)
4. [Agent hook](#agent-hook)
5. [Async HTTP with retry](#async-http-with-retry)
6. [FFT on tensors](#fft-on-tensors)
7. [Why Mog?](#why-mog)
8. [Alternatives](#alternatives)
9. [The Language](#the-language)
10. [Example](#example)
11. [The Capability System](#the-capability-system)
12. [The Compiler](#the-compiler)
13. [Current Status](#current-status)
14. [The Mog Language Guide](#the-mog-language-guide)
15. [Chapter 1: Your First Mog Program](#chapter-1-your-first-mog-program)
16. [Hello, World](#hello-world)
17. [How Mog Programs Are Compiled and Run](#how-mog-programs-are-compiled-and-run)
18. [Program Structure](#program-structure)
19. [Comments](#comments)
20. [Print Functions](#print-functions)
21. [A More Complete Example](#a-more-complete-example)
22. [What Mog Is Not](#what-mog-is-not)
23. [What's Next](#whats-next)
24. [Chapter 2: Variables and Bindings](#chapter-2-variables-and-bindings)
25. [Creating Bindings with `:=`](#creating-bindings-with)
26. [Reassignment with `=`](#reassignment-with)
27. [Type Annotations](#type-annotations)
28. [Shadowing](#shadowing)
29. [Practical Examples](#practical-examples)
30. [Swapping Two Values](#swapping-two-values)
31. [Fibonacci Sequence](#fibonacci-sequence)
32. [Processing a List](#processing-a-list)
33. [Counting Occurrences](#counting-occurrences)
34. [Summary](#summary)
35. [Chapter 3: Types and Operators](#chapter-3-types-and-operators)
36. [Scalar Types](#scalar-types)
37. [Integers](#integers)
38. [Explicit-Width Integers](#explicit-width-integers)
39. [Floats](#floats)
40. [Booleans](#booleans)
41. [Strings](#strings)
42. [Type Conversions](#type-conversions)
43. [The `as` Keyword](#the-as-keyword)
44. [String Conversions](#string-conversions)
45. [No Implicit Conversions](#no-implicit-conversions)
46. [Operators](#operators)
47. [Arithmetic Operators](#arithmetic-operators)
48. [Comparison Operators](#comparison-operators)
49. [Logical Operators](#logical-operators)
50. [Bitwise Operators](#bitwise-operators)
51. [String Concatenation](#string-concatenation)
52. [Flat Operators (No Precedence)](#flat-operators-no-precedence)
53. [Why no precedence?](#why-no-precedence)
54. [Common Patterns](#common-patterns)
55. [Clamping a Value](#clamping-a-value)
56. [Safe Division](#safe-division)
57. [Type-Aware Accumulation](#type-aware-accumulation)
58. [Bitflag Permissions](#bitflag-permissions)
59. [Building Results with Type Conversion](#building-results-with-type-conversion)
60. [Summary](#summary-2)
61. [Chapter 4: Control Flow](#chapter-4-control-flow)
62. [If/Else](#ifelse)
63. [Nested Conditions](#nested-conditions)
64. [If as Expression](#if-as-expression)
65. [While Loops](#while-loops)
66. [Accumulator Pattern](#accumulator-pattern)
67. [Convergence Loops](#convergence-loops)
68. [Infinite Loops](#infinite-loops)
69. [For Loops](#for-loops)
70. [For-To (Inclusive Range)](#for-to-inclusive-range)
71. [For-In Range (Exclusive End)](#for-in-range-exclusive-end)
72. [When to Use Which](#when-to-use-which)
73. [For-In Array](#for-in-array)
74. [For-In with Index](#for-in-with-index)
75. [For-In Map](#for-in-map)
76. [Break and Continue](#break-and-continue)
77. [Break](#break)
78. [Continue](#continue)
79. [Combined Break and Continue](#combined-break-and-continue)
80. [Break and Continue in Nested Loops](#break-and-continue-in-nested-loops)
81. [Match](#match)
82. [Matching Integers](#matching-integers)
83. [Matching Strings](#matching-strings)
84. [Multi-Statement Arms](#multi-statement-arms)
85. [Match as Expression](#match-as-expression)
86. [Matching on Result and Optional](#matching-on-result-and-optional)
87. [Practical Examples](#practical-examples-2)
88. [Fibonacci (Iterative)](#fibonacci-iterative)
89. [Sum of Squares](#sum-of-squares)
90. [Linear Search](#linear-search)
91. [Bubble Sort](#bubble-sort)
92. [FizzBuzz](#fizzbuzz)
93. [GCD (Euclidean Algorithm)](#gcd-euclidean-algorithm)
94. [Prime Checker](#prime-checker)
95. [Command Dispatcher with Match](#command-dispatcher-with-match)
96. [Summary](#summary-3)
97. [Chapter 5: Functions](#chapter-5-functions)
98. [Basic Function Declarations](#basic-function-declarations)
99. [Void Functions](#void-functions)
100. [Parameters and Return Types](#parameters-and-return-types)
101. [Named Arguments and Default Values](#named-arguments-and-default-values)
102. [Calling Conventions](#calling-conventions)
103. [Recursion](#recursion)
104. [Math Builtins](#math-builtins)
105. [Other Builtins](#other-builtins)
106. [Output Functions](#output-functions)
107. [Conversion Functions](#conversion-functions)
108. [A Complete Example](#a-complete-example)
109. [Summary](#summary-4)
110. [Chapter 6: Closures and Higher-Order Functions](#chapter-6-closures-and-higher-order-functions)
111. [Closure Syntax](#closure-syntax)
112. [Capturing Variables](#capturing-variables)
113. [Value Capture Semantics](#value-capture-semantics)
114. [Type Aliases for Function Types](#type-aliases-for-function-types)
115. [Passing Closures to Functions](#passing-closures-to-functions)
116. [Returning Closures from Functions](#returning-closures-from-functions)
117. [Closures with Array Methods](#closures-with-array-methods)
118. [filter](#filter)
119. [map](#map)
120. [sort](#sort)
121. [Chaining Methods](#chaining-methods)
122. [Summary](#summary-5)
123. [Chapter 7: Strings](#chapter-7-strings)
124. [String Basics](#string-basics)
125. [Escape Sequences](#escape-sequences)
126. [Immutability](#immutability)
127. [UTF-8 Encoding](#utf-8-encoding)
128. [String Interpolation](#string-interpolation)
129. [String Concatenation](#string-concatenation-2)
130. [String Methods](#string-methods)
131. [`.len`](#len)
132. [`.contains(substr)`](#containssubstr)
133. [`.starts\_with(prefix)` and `.ends\_with(suffix)`](#startswithprefix-and-endswithsuffix)
134. [`.upper()` and `.lower()`](#upper-and-lower)
135. [`.trim()`](#trim)
136. [`.replace(old, new)`](#replaceold-new)
137. [`.split(delimiter)`](#splitdelimiter)
138. [`.index\_of(substr)`](#indexofsubstr)
139. [Method Chaining](#method-chaining)
140. [String Slicing](#string-slicing)
141. [String Comparison](#string-comparison)
142. [Conversions](#conversions)
143. [To String: `str()`](#to-string-str)
144. [From String: Parsing](#from-string-parsing)
145. [Print Functions](#print-functions-2)
146. [Generic Printing](#generic-printing)
147. [Type-Specific Variants](#type-specific-variants)
148. [Building Strings](#building-strings)
149. [Concatenation in Loops](#concatenation-in-loops)
150. [Formatting Tables](#formatting-tables)
151. [Building Messages](#building-messages)
152. [Parsing with Validation](#parsing-with-validation)
153. [Summary](#summary-6)
154. [Chapter 8: Structs](#chapter-8-structs)
155. [Declaring Structs](#declaring-structs)
156. [Constructing Instances](#constructing-instances)
157. [Field Access](#field-access)
158. [Field Mutation](#field-mutation)
159. [Passing Structs to Functions](#passing-structs-to-functions)
160. [No Methods — Use Standalone Functions](#no-methods-use-standalone-functions)
161. [Constructor Functions](#constructor-functions)
162. [Nested Structs](#nested-structs)
163. [Structs with Arrays and Maps](#structs-with-arrays-and-maps)
164. [Practical Examples](#practical-examples-3)
165. [RGB Color Manipulation](#rgb-color-manipulation)
166. [Tree Structure](#tree-structure)
167. [Summary](#summary-7)
168. [Chapter 9: Collections](#chapter-9-collections)
169. [Arrays](#arrays)
170. [Array Literals](#array-literals)
171. [Repeat Syntax](#repeat-syntax)
172. [Type Annotations](#type-annotations-2)
173. [Indexing](#indexing)
174. [Iteration](#iteration)
175. [`.push()` and `.pop()`](#push-and-pop)
176. [`.slice()`](#slice)
177. [`.contains()`](#contains)
178. [`.reverse()`](#reverse)
179. [`.join()`](#join)
180. [`.filter()`](#filter-2)
181. [`.map()`](#map-2)
182. [`.sort()`](#sort-2)
183. [Chaining Array Methods](#chaining-array-methods)
184. [Maps](#maps)
185. [Creating Maps](#creating-maps)
186. [Access and Mutation](#access-and-mutation)
187. [`.has()` — Checking Key Existence](#has-checking-key-existence)
188. [`.len()`, `.keys()`, `.values()`](#len-keys-values)
189. [`.delete()` — Removing Entries](#delete-removing-entries)
190. [Iterating Maps](#iterating-maps)
191. [Practical Example: Word Counting](#practical-example-word-counting)
192. [Practical Example: Grouping Data](#practical-example-grouping-data)
193. [SoA (Struct of Arrays)](#soa-struct-of-arrays)
194. [When to Use SoA](#when-to-use-soa)
195. [Construction](#construction)
196. [Field Access](#field-access-2)
197. [Iteration Patterns](#iteration-patterns)
198. [Practical Example: Particle Simulation](#practical-example-particle-simulation)
199. [Practical Example: Column Operations](#practical-example-column-operations)
200. [Putting It All Together](#putting-it-all-together)
201. [Data Processing Pipeline](#data-processing-pipeline)
202. [Filter-Map-Sort Pipeline](#filter-map-sort-pipeline)
203. [Summary](#summary-8)
204. [Chapter 10: Error Handling](#chapter-10-error-handling)
205. [Result\<T\>](#resultt)
206. [Optional ?T](#optional-t)
207. [The ? Propagation Operator](#the-propagation-operator)
208. [try-catch Blocks](#try-catch-blocks)
209. [Match Patterns for Result and Optional](#match-patterns-for-result-and-optional)
210. [Practical Patterns](#practical-patterns)
211. [Validation Chains](#validation-chains)
212. [Safe Parsing](#safe-parsing)
213. [Converting Between Result and Optional](#converting-between-result-and-optional)
214. [Providing Defaults for Optionals](#providing-defaults-for-optionals)
215. [Error Message Formatting](#error-message-formatting)
216. [Collecting Results](#collecting-results)
217. [Nested Results](#nested-results)
218. [Summary](#summary-9)
219. [Chapter 11: Async Programming](#chapter-11-async-programming)
220. [Async Functions](#async-functions)
221. [Await](#await)
222. [Spawn](#spawn)
223. [all() — Wait for All](#all-wait-for-all)
224. [race() — Wait for First](#race-wait-for-first)
225. [Error Handling with Async](#error-handling-with-async)
226. [Retry Pattern](#retry-pattern)
227. [Fan-out / Fan-in](#fan-out-fan-in)
228. [Summary](#summary-10)
229. [Chapter 12: Modules and Packages](#chapter-12-modules-and-packages)
230. [Package Declaration](#package-declaration)
231. [Public vs Private — The `pub` Keyword](#public-vs-private-the-pub-keyword)
232. [Importing Packages](#importing-packages)
233. [Multi-Import Syntax](#multi-import-syntax)
234. [Qualified Access](#qualified-access)
235. [The Module File](#the-module-file)
236. [Circular Import Detection](#circular-import-detection)
237. [Practical Example: Splitting a Program into Packages](#practical-example-splitting-a-program-into-packages)
238. [Summary](#summary-11)
239. [Chapter 13: Capabilities — Safe I/O](#chapter-13-capabilities-safe-io)
240. [The Capability Model](#the-capability-model)
241. [Declaring Capabilities: `requires` and `optional`](#declaring-capabilities-requires-and-optional)
242. [Built-in Capabilities](#built-in-capabilities)
243. [`fs` — File System](#fs-file-system)
244. [`process` — Process and Environment](#process-process-and-environment)
245. [Practical Examples](#practical-examples-4)
246. [Copying a File](#copying-a-file)
247. [Reading Configuration](#reading-configuration)
248. [Timed Operations](#timed-operations)
249. [Simple Logger Using `fs`](#simple-logger-using-fs)
250. [Conventional Capabilities](#conventional-capabilities)
251. [Custom Host Capabilities](#custom-host-capabilities)
252. [`.mogdecl` Files](#mogdecl-files)
253. [Using a Custom Capability](#using-a-custom-capability)
254. [How the Pieces Fit Together](#how-the-pieces-fit-together)
255. [Capability Validation Example](#capability-validation-example)
256. [Summary](#summary-12)
257. [Chapter 14: Embedding Mog in a Host Application](#chapter-14-embedding-mog-in-a-host-application)
258. [The Embedding Lifecycle](#the-embedding-lifecycle)
259. [The Embedding API](#the-embedding-api)
260. [VM Lifecycle](#vm-lifecycle)
261. [Registering Capabilities](#registering-capabilities)
262. [Validating Script Requirements](#validating-script-requirements)
263. [Implementing a Custom Capability](#implementing-a-custom-capability)
264. [Step 1: Write the `.mogdecl` File](#step-1-write-the-mogdecl-file)
265. [Step 2: Implement the Host Functions](#step-2-implement-the-host-functions)
266. [Step 3: Build the Registration Table and Register](#step-3-build-the-registration-table-and-register)
267. [Step 4: Use It from Mog](#step-4-use-it-from-mog)
268. [MogValue: Data Exchange Between Host and Script](#mogvalue-data-exchange-between-host-and-script)
269. [Constructing Values](#constructing-values)
270. [Extracting Arguments](#extracting-arguments)
271. [Returning Errors](#returning-errors)
272. [Opaque Handles](#opaque-handles)
273. [Resource Limits and Timeouts](#resource-limits-and-timeouts)
274. [Memory Limits](#memory-limits)
275. [CPU Time Limits](#cpu-time-limits)
276. [Manual Timeout Arming](#manual-timeout-arming)
277. [Host-Initiated Interrupts](#host-initiated-interrupts)
278. [Stack Overflow Protection](#stack-overflow-protection)
279. [Complete Timeout Example](#complete-timeout-example)
280. [Safety Guarantees](#safety-guarantees)
281. [Practical Example: Embedding in a Game Server](#practical-example-embedding-in-a-game-server)
282. [The `.mogdecl` File](#the-mogdecl-file)
283. [The Host Implementation (C)](#the-host-implementation-c)
284. [The Player Script (Mog)](#the-player-script-mog)
285. [The Host Runner](#the-host-runner)
286. [Summary](#summary-13)
287. [Plugins — Dynamic Loading of Mog Code](#plugins-dynamic-loading-of-mog-code)
288. [Plugin Overview](#plugin-overview)
289. [Writing a Plugin](#writing-a-plugin)
290. [Compiling a Plugin](#compiling-a-plugin)
291. [Loading and Calling Plugins](#loading-and-calling-plugins)
292. [Plugin C API Reference](#plugin-c-api-reference)
293. [Capability Sandboxing](#capability-sandboxing)
294. [Plugin Protocol (Advanced)](#plugin-protocol-advanced)
295. [How Mog Compares to Other Embeddable Languages](#how-mog-compares-to-other-embeddable-languages)
296. [Chapter 15: Tensors — N-Dimensional Arrays](#chapter-15-tensors-n-dimensional-arrays)
297. [What Are Tensors?](#what-are-tensors)
298. [Creating Tensors](#creating-tensors)
299. [From a Literal](#from-a-literal)
300. [Static Constructors](#static-constructors)
301. [Supported Dtypes](#supported-dtypes)
302. [Tensor Properties](#tensor-properties)
303. [Element Access](#element-access)
304. [Reading Elements](#reading-elements)
305. [Writing Elements](#writing-elements)
306. [Computing Flat Indices](#computing-flat-indices)
307. [Shape Operations](#shape-operations)
308. [Reshape](#reshape)
309. [Transpose](#transpose)
310. [Tensors and Host Capabilities](#tensors-and-host-capabilities)
311. [Passing Tensors to Host Functions](#passing-tensors-to-host-functions)
312. [Composing Operations](#composing-operations)
313. [Why This Design?](#why-this-design)
314. [Practical Examples](#practical-examples-5)
315. [Creating a Data Batch](#creating-a-data-batch)
316. [Reading Model Output Elements](#reading-model-output-elements)
317. [Preparing Input Tensors](#preparing-input-tensors)
318. [End-to-End Inference Script](#end-to-end-inference-script)
319. [Summary](#summary-14)
320. [Chapter 16: Advanced Topics](#chapter-16-advanced-topics)
321. [Type Aliases](#type-aliases)
322. [With Blocks](#with-blocks)
323. [Struct-of-Arrays (SoA) Performance](#struct-of-arrays-soa-performance)
324. [Compilation Backend: rqbe](#compilation-backend-rqbe)
325. [The Interrupt System](#the-interrupt-system)
326. [Memory Management](#memory-management)
327. [What Mog Does NOT Have](#what-mog-does-not-have)
328. [Chapter 17: Cookbook — Practical Programs](#chapter-17-cookbook-practical-programs)
329. [1. FizzBuzz](#1-fizzbuzz)
330. [2. Fibonacci Sequence](#2-fibonacci-sequence)
331. [Recursive](#recursive)
332. [Iterative](#iterative)
333. [3. Word Frequency Counter](#3-word-frequency-counter)
334. [4. Simple Calculator with Error Handling](#4-simple-calculator-with-error-handling)
335. [5. Data Validation Chain](#5-data-validation-chain)
336. [6. Sorting and Filtering Pipeline](#6-sorting-and-filtering-pipeline)
337. [7. Matrix Operations](#7-matrix-operations)
338. [8. Agent Tool-Use Script](#8-agent-tool-use-script)
339. [9. Recursive Tree Traversal](#9-recursive-tree-traversal)
340. [10. Async Pipeline](#10-async-pipeline)
341. [Summary](#summary-15)

Mog: A Programming Language for AI Agents
=========================================

> What if an AI agent could modify itself quickly, easily, and safely? Mog is a
> programming language designed for exactly this.

---

Overview
--------

Mog is a statically typed, compiled, embedded language (think statically typed Lua) designed to be written by LLMs – the full spec fits in 3200 tokens.

* An AI agent writes a Mog program, compiles it, and dynamically loads it as a plugin, script, or hook.
* The host controls exactly which functions a Mog program can call (capability-based permissions), so permissions propagate from agent to agent-written code.
* Compiled to native code for low-latency plugin execution – no interpreter overhead, no JIT, no process startup cost.
* The compiler is written in safe Rust so the entire toolchain can be audited for security.
* Even without a full security audit, Mog is already useful for agents extending themselves with their own code.
* MIT licensed, contributions welcome. <https://github.com/voltropy/mog>

Examples
--------

### Agent hook

An agent hook that runs after context compaction. All I/O functions are provided by the host: `import` pulls in host-defined types, and `optional` capabilities degrade gracefully.

```
import agent;       // Agent, Message, Role types
optional log;       // silently ignored if not provided

// post-compaction hook: re-inject key context that may have been lost
pub fn on_post_compaction(session: agent.Session) {
  log.info("post-compaction hook: injecting reminder");

  session.messages.push(agent.Message {
    role: agent.Role.SYSTEM,
    content: "IMPORTANT: Always run tests before committing.",
  });
}
```

### Async HTTP with retry

An async HTTP fetcher with retry logic. Mog supports `async`/`await` that suspends without blocking the host’s agent loop, `match` for destructuring `Result` values, and f-strings for expression interpolation.

```
async fn fetch_with_retry(url: string, max_retries: int) -> Result<string> {
  attempts := 0;
  for attempts < max_retries {
    match await http.get(url) {
      ok(response) => return ok(response.body),
      err(e) => {
        attempts = attempts + 1;
        if attempts >= max_retries {
          return err(f"failed after {max_retries} attempts: {e}");
        }
        println(f"attempt {attempts} failed, retrying...");
        await sleep(1000 * attempts);  // exponential-ish backoff
      },
    }
  }
  return err(f"all {max_retries} attempts to fetch {url} failed");
}
```

### FFT on tensors

Mog compiles to machine code, with native support for multi-dimensional arrays (tensors). Here is a radix-2 FFT on `tensor<f32>` data. To minimize foot-guns, Mog has no operator precedence, so arithmetic involving non-associative operations requires explicit parentheses. Type conversions like `size as float` are always explicit – no implicit coercion.

```
// Fast Fourier Transform (Cooley-Tukey, radix-2, in-place)
// Returns a 2×n tensor: row 0 = real, row 1 = imaginary.

fn fft(re: tensor<f32>, im: tensor<f32>) -> tensor<f32> {
  n := re.shape[0];
  r := tensor<f32>.zeros([n]);
  im_out := tensor<f32>.zeros([n]);

  for i in 0..n {
    r[i] = re[i];
    im_out[i] = im[i];
  }

  // bit-reversal permutation
  j := 0;
  for i := 1 to (n - 1) {
    bit := n / 2;
    while j >= bit {
      j = j - bit;
      bit = bit / 2;
    }
    j = j + bit;
    if i < j {
      tmp := r[i]; r[i] = r[j]; r[j] = tmp;
      tmp = im_out[i]; im_out[i] = im_out[j]; im_out[j] = tmp;
    }
  }

  // Cooley-Tukey butterfly — mixed operators require explicit parens
  size := 2;
  while size <= n {
    half := size / 2;
    step := (0.0 - 6.283185307) / (size as float);  // -2π/size, explicit int->float cast
    k := 0;
    while k < n {
      angle := 0.0;
      for m := 0 to (half - 1) {
        cos_a := cos(angle) as f32;  // math builtins return f64; cast to match tensor
        sin_a := sin(angle) as f32;
        idx := (k + m) + half;

        tr := (r[idx] * cos_a) - (im_out[idx] * sin_a);
        ti := (r[idx] * sin_a) + (im_out[idx] * cos_a);

        r[idx] = r[(k + m)] - tr;
        im_out[idx] = im_out[(k + m)] - ti;
        r[(k + m)] = r[(k + m)] + tr;
        im_out[(k + m)] = im_out[(k + m)] + ti;

        angle = angle + step;
      }
      k = k + size;
    }
    size = size * 2;
  }

  // pack real and imaginary into 2×n result
  result := tensor<f32>.zeros([2, n]);
  for i in 0..n {
    result[i] = r[i];
    result[n + i] = im_out[i];
  }
  return result;
}
```

Why Mog?
--------

A general-purpose AI agent should be able to continuously extend and modify itself. Over time, an agent should grow into a personal server that manages tasks in all kinds of ways. To do that, the agent needs to write its own code – and that code needs to be safe.

The simplest kind of program an agent writes is a one-off script to achieve some task. Examples:

* Converting a markdown file to PDF.
* Analyzing a CSV with database results.
* Sending test requests to an application’s HTTP endpoint.
* Renaming all the files in a folder.
* Installing dependencies.

Coding agents typically use bash for this, and sometimes reach for an inline Python or TypeScript script. Mog is well-suited for this: it’s easy to write and it compiles fast. Notably, scripting is one of the main ways an agent escapes its sandbox, and Mog closes that loophole. Even if Mog is given a capability by its host agent to call bash commands, the host still has the ability to filter those commands according to its permissions, just as if the model had called its bash tool directly.

The second kind of program agents commonly write is a hook: a piece of code that runs repeatedly at a certain point in the agentic loop. Pre- and post-tool-use hooks are common, as well as pre-compaction hooks. For a hook, it’s not important for it to compile quickly, but it needs to start up quickly and execute quickly, since it can get called frequently enough that a slow implementation would meaningfully drag down the user experience. Mog compiles to native code, and it can then *load that machine code into the agent’s running binary*. The key property that makes this safe: native code compiled by the Mog compiler can’t do anything other than what the host explicitly lets it do – not even exceed limits on memory or time. The agent can incorporate a Mog program into itself at runtime and call into it without inter-process communication overhead or process startup latency.

The third category is writing or rewriting parts of the agent itself. This could mean adding a new tool that the agent exposes to the LLM, a status line for the user interface, settings about agent skills or session management – a potentially long list of agent internals that would benefit from extension or specialization.

One could imagine a microkernel agent, written as a small backbone of Rust code that calls into Mog code for almost all its features. The kernel would manage the event loops, multi-threading, root permissions, compiling and loading Mog programs, and maybe part of its upgrade functionality, but the rest of the system could be written in Mog – running with minimal, granular permissions and upgradeable on the fly without a restart, just by prompting the agent to modify itself.

Alternatives
------------

Without something like Mog, every option for AI-generated agent code has a downside. One major one is enforcing permissions: tools like Jeffrey Emanuel’s [`dcg`](https://github.com/Dicklesworthstone/destructive_command_guard) can interdict `rm -rf` and similarly destructive shell commands, but they can’t stop an agent from emitting Python that iterates through files in a folder and calls `os.remove()` on each one.

The next step is generally to run the agent in a sandbox, like a Docker container. But then the permissions tend to apply to the whole sandbox, so letting the agent use the host computer in nontrivial ways (e.g. pull in environment variables, access CLI tools, drive a browser, make HTTP requests) requires opening up the sandbox boundary. At that point the agent has regained essentially unfettered access to that capability.

What’s missing is a way to propagate the permissions granted to an agent to the programs that agent writes. Mog addresses this directly.

Another issue with external scripts is sharing them – receiving a script from an untrusted source is a security risk. With Mog, the receiving agent compiles the Mog source itself, rather than running a pre-compiled binary that could take over the machine.

There are other approaches to LLM-driven extension systems. Jeffrey Emanuel is building something similar using JavaScript containers with permissions, which is quite close to Mog in spirit, and has an impressive level of infrastructure behind it. Mog could complement such systems, especially for higher-performance plugins – Mog’s infrastructure is also in Rust, making integration straightforward. Emanuel’s [Rust version of the Pi agent](https://github.com/Dicklesworthstone/pi_agent_rust) would be a natural starting point for a Mog-based microkernel agent.

WASM is another natural option, since it’s a more standard sandboxing technique. Mog takes a different approach: a hot loop over an array runs at native speed, without the unpredictability of JIT compilation, the overhead of WASM interpretation, or the process startup time of an external binary.

The Language
------------

Mog is a minimal language designed to be written by LLMs. Its full specification, with examples, fits in a single [3200-token markdown file](https://github.com/voltropy/mog/blob/main/docs/context.md), which an LLM can pin in context when writing Mog programs. Everything about the language is designed to optimize the latency between asking an LLM to write a program for a task and having a performant program that implements that task.

The primary goal of Mog syntax is to be familiar to LLMs. It’s a mix of TypeScript, Rust, and Go, with a couple of Pythonisms. Its module system is modeled on Go modules. It’s a small but usable language with no foot-guns: no implicit type coercion, no operator precedence, and no uninitialized data.

Why statically typed and compiled? Because latency matters in this domain. Consider an agent plugin that runs before every tool call – it needs to be fast, or it’s not worth using. Jeffrey Emanuel rewrote every single one of his agent plugins in Rust to reduce startup time and Python overhead. A modern computer is fast, but Python is not. Even Bun’s startup time, which has been heavily optimized, is nowhere near the startup time of a Rust program, and even that is slow compared to calling into an in-process library.

### Example

Here’s a Mog hook that an agent might write to monitor its own tool calls for errors:

```
requires fs;  // must be provided by host
optional log; // runs without it

pub fn on_tool_result(tool_name: string, stderr: string) {
  if (stderr.contains("permission denied")) {
    log.warn(f"{tool_name}: permission denied");
    fs.append_file("agent.log", f"[warn] {tool_name}: {stderr}\n");
  }
}
```

The first two lines tell the security story: this hook can append to a file and optionally log, but it cannot make HTTP requests, run shell commands, or read environment variables. The host decides what this program is allowed to do – it can even interdict the `fs.append_file()` call if this program doesn’t have that permission.

As agents get more complex and more of their code is bespoke, performance, correctness, and security of the combined system become harder to maintain. Mog is designed to address these issues.

The Capability System
---------------------

Mog is an embedded language. It runs inside a host program, much like Lua – the way a Mog host provides functions to the guest Mog program is based directly on Lua’s elegant and battle-tested design. By itself, a Mog program cannot do any I/O, perform syscalls, or access raw memory. It can only run functions and return values. That is the extent of Mog’s sandbox.

Any I/O, FFI, syscalls, or interaction with other systems can only be done by calling a host function – a function that the host makes available to the Mog program. This is the essence of Mog’s capability system: the host decides exactly which functions it will allow the guest to call. The host is also free to filter the inputs to such a function and to filter the response delivered back to the Mog program.

Part of this isolation involves preventing a Mog program from taking over the host process in subtler ways. The host can control whether a Mog program can request a larger memory arena, preventing the guest from consuming all available RAM. Cooperative interrupt polling means Mog loops all have interrupt checks added at back-edges, which allows the host to halt the guest program without killing the process. This enables timeout enforcement. There is no way for a guest program to corrupt memory or kill the process (assuming correct implementation of the compiler and host).

Since a typical agent runs an event loop, Mog programs are designed to run inside an event loop, familiar to anyone who has written JavaScript or TypeScript. Mog’s support for this consists primarily of async/await syntax. Mog programs can define async functions, and importantly, the host can also provide async functions that the guest can call. This allows a guest program to fire off an HTTP request and a timer and do something different depending on which one finishes first – internally the compiler implements this using coroutine lowering, based on LLVM’s design for the same.

The Compiler
------------

The compiler uses [QBE](https://c9x.me/compile/) as its code generation backend, rewritten in safe Rust. The entire toolchain for compiling, loading, and running a Mog program is in Rust – the goal is for all of it to be safe Rust, making it much more difficult to find an exploit in the toolchain.

The first implementation of Mog used LLVM as the backend. LLVM can produce somewhat faster code due to its wide array of optimizations, but it had two major issues. First, compile times were not fast enough. The new compiler has compile times that are not quite as good as Go’s, but within an order of magnitude for programs under 1000 lines – fast enough that the start time for one-off scripts is not painful. Mog does not claim to provide zero-cost abstractions or arbitrary opportunities for low-level optimization. It compiles to native code, but an expert can still write faster C or C++.

The second issue with LLVM is that for Mog, the compiler itself is part of the trusted computing base. If the compiler has a security flaw, the agent has a security flaw. This rules out an enormous codebase like LLVM’s. The compiler needs to be small enough to control and audit.

Current Status
--------------

The first version of Mog was created entirely using the [Volt](https://github.com/Martian-Engineering/volt) coding agent, the vast majority of which used a single continuous session spanning over three weeks, using Voltropy’s [Lossless Context Management](https://papers.voltropy.com/LCM) to maintain its memory after compactions. This session ported the QBE compiler to safe Rust. The models used were Claude Opus 4.6, Kimi k2.5, and GLM-4.7.

Significant work remains to standardize the functions that hosts provide to Mog programs. This should include much of what the Python standard library provides: support for JSON, CSV, SQLite, POSIX filesystem and networking operations, etc. The Mog standard library should also provide async functions for calling LLMs – both high-level interfaces (like Simon Willison’s `llm` CLI tool or `DSPy` modules) and low-level interfaces that allow fine-grained context management.

To be clear: Mog has *not* been audited, and it is presented without security guarantees. It should be possible to secure it, but that work has not yet been done. There are tests that check that a malicious Mog program cannot access host functionality that the host does not want to provide, but this design has enough security attack surface to warrant careful scrutiny.

Even without audited security properties, Mog is already useful for extending AI agents *with their own code* – they’re not trying to exploit themselves. For untrusted third-party code, treat the security model as unverified until a formal audit is completed.



The Mog Language Guide
======================

> A complete guide to learning and using the Mog programming language.

---



Chapter 1: Your First Mog Program
=================================

This chapter walks through the basics of writing and running Mog code. By the end, you will understand how a Mog program is structured, how to print output, how to write comments, and how to define and call functions.

Hello, World
------------

A Mog host runtime can provide a `main()` function as the entry point, though not all do. Here is a simple program using one:

```
fn main() -> int {
  println("Hello, world!");
  return 0;
}
```

`fn main() -> int` declares an entry point. The `-> int` annotation means the function returns an integer — by convention, `0` signals success. The `println` function prints a string followed by a newline. The `return 0;` statement exits the program.

Semicolons are required after every statement. Curly braces delimit blocks. If you are coming from Go or Rust, this will feel natural. If you are coming from Python, the semicolons may take a few minutes to get used to.

How Mog Programs Are Compiled and Run
-------------------------------------

Mog is a compiled language. You write a `.mog` source file, compile it to a native executable, and run the executable. The compiler is written in Rust:

```
# Build the compiler (once)
cargo build --release --manifest-path compiler/Cargo.toml

# Compile a Mog program to a native executable
mogc hello.mog

# Run the resulting binary
./hello
```

The compilation pipeline works like this: the Rust compiler reads your `.mog` file, lexes it into tokens, parses it into an abstract syntax tree, analyzes and type-checks it, generates QBE intermediate language, and passes it to rqbe (a safe Rust QBE backend that runs in-process). rqbe emits assembly, which the system assembler and linker turn into a native binary linked with the Mog runtime. The whole process takes milliseconds for small programs.

There is also a convenience script that compiles, links, and runs in a single step:

```
./algb hello.mog
```

In production, Mog programs run embedded inside a host application. The host compiles the script, registers capabilities, and invokes the compiled code through a C API. But for learning the language, the standalone compilation path is all you need.

There is a third compilation mode: **plugins**. You can compile a `.mog` file into a shared library (`.dylib` on macOS, `.so` on Linux) instead of a standalone executable. The host loads the library at runtime with `dlopen`, queries what functions are available, and calls them by name. Functions marked `pub` in the source become exported symbols; everything else gets internal linkage and is invisible to the loader. This is the right path when you want pre-compiled, hot-swappable modules — the host never sees the source code, just a binary it can load and unload. See Chapter 14 for the full plugin API.

The compiler uses rqbe, a safe Rust implementation of the QBE backend, as its code generation engine. rqbe runs entirely in-process — no external tools are needed beyond the system assembler and linker. It compiles fast and produces correct native code for ARM64 and x86.

Program Structure
-----------------

A Mog source file is a sequence of top-level declarations followed by a `main` function. Top-level declarations include functions, structs, and capability requirements. You cannot put executable statements at the top level — all code runs inside functions.

```
// Top-level: struct declaration
struct Point {
  x: float,
  y: float
}

// Top-level: function declaration
fn distance(a: Point, b: Point) -> float {
  dx := a.x - b.x;
  dy := a.y - b.y;
  return sqrt((dx * dx) + (dy * dy));
}

fn main() -> int {
  p1 := Point { x: 3.0, y: 0.0 };
  p2 := Point { x: 0.0, y: 4.0 };
  d := distance(p1, p2);
  println(f"Distance: {d}");
  return 0;
}
```

The order of declarations does not matter — you can call a function that is defined later in the file. The compiler resolves all names before generating code.

Here is a program with multiple functions that call each other:

```
fn square(x: int) -> int {
  return x * x;
}

fn sum_of_squares(a: int, b: int) -> int {
  return square(a) + square(b);
}

fn main() -> int {
  result := sum_of_squares(3, 4);
  println(f"3² + 4² = {result}");  // 3² + 4² = 25
  return 0;
}
```

And a program that uses a struct and a helper function:

```
struct Rectangle {
  width: float,
  height: float
}

fn area(r: Rectangle) -> float {
  return r.width * r.height;
}

fn main() -> int {
  r := Rectangle { width: 5.0, height: 3.0 };
  a := area(r);
  print_string("Area: ");
  print_f64(a);
  println("");
  return 0;
}
```

Comments
--------

Mog supports two kinds of comments. Single-line comments start with `//` and run to the end of the line. Multi-line comments are delimited by `/*` and `*/`.

```
// This is a single-line comment

/* This is a
   multi-line comment */

fn main() -> int {
  // Comments can appear on their own line
  x := 42;  // or at the end of a line

  /*
   * Multi-line comments are useful for temporarily
   * disabling blocks of code or writing longer
   * explanations.
   */

  println(f"x = {x}");
  return 0;
}
```

Multi-line comments do not nest. A `/*` inside a multi-line comment is treated as ordinary text, and the first `*/` ends the comment. In practice, single-line comments are far more common.

```
fn main() -> int {
  // Calculate the sum of integers from 1 to 10
  sum := 0;
  i := 1;
  while (i <= 10) {
    sum = sum + i;
    i = i + 1;
  }
  println(f"Sum: {sum}");  // Sum: 55

  /* Temporarily disabled:
  println("This line does not execute");
  */

  return 0;
}
```

Print Functions
---------------

Mog provides several built-in functions for printing output. These are always available — no imports needed.

| Function | Description |
| --- | --- |
| `println(s)` | Print a string followed by a newline |
| `print_string(s)` | Print a string without a newline |
| `print(n)` | Print an integer |
| `println_i64(n)` | Print an integer followed by a newline |
| `print_f64(x)` | Print a float |

The most common is `println`, which prints a string with a trailing newline. For formatted output, combine it with f-string interpolation:

```
fn main() -> int {
  println("Hello, world!");

  name := "Mog";
  println(f"Welcome to {name}!");

  x := 42;
  println(f"The answer is {x}");

  return 0;
}
```

Output:

```
Hello, world!
Welcome to Mog!
The answer is 42
```

When you need to print numbers without f-string formatting, use the type-specific print functions:

```
fn main() -> int {
  // Print an integer
  print_string("Count: ");
  println_i64(42);

  // Print a float
  print_string("Pi: ");
  print_f64(3.14159);
  println("");

  // print() also works for integers
  print_string("Score: ");
  print(100);
  println("");

  return 0;
}
```

Output:

```
Count: 42
Pi: 3.141590
Score: 100
```

The `print_string` function is useful when you want to build a line of output from multiple parts without newlines between them:

```
fn main() -> int {
  print_string("Loading");
  print_string(".");
  print_string(".");
  print_string(".");
  println(" done!");
  return 0;
}
```

Output:

```
Loading... done!
```

F-string interpolation (the `f"..."` syntax) is the preferred way to format output in Mog. It can embed any expression inside `{}` delimiters:

```
fn main() -> int {
  width := 10;
  height := 5;
  println(f"Rectangle: {width} x {height} = {width * height}");

  name := "Alice";
  score := 95;
  println(f"{name} scored {score} points");

  a := 3.14;
  println(f"Value: {a}");

  return 0;
}
```

Output:

```
Rectangle: 10 x 5 = 50
Alice scored 95 points
Value: 3.14
```

A More Complete Example
-----------------------

Let’s put everything together. Here is a program that defines a few functions, uses variables and arithmetic, and prints formatted output:

```
fn factorial(n: i64) -> i64 {
  if (n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

fn fibonacci(n: i64) -> i64 {
  if (n <= 0) { return 0; }
  if (n == 1) { return 1; }
  a: i64 = 0;
  b: i64 = 1;
  i: i64 = 2;
  while (i <= n) {
    temp: i64 = a + b;
    a = b;
    b = temp;
    i = i + 1;
  }
  return b;
}

fn main() -> int {
  // Factorial
  println(f"5! = {factorial(5)}");
  println(f"10! = {factorial(10)}");

  // Fibonacci
  println(f"fib(10) = {fibonacci(10)}");
  println(f"fib(20) = {fibonacci(20)}");

  // Simple arithmetic
  x := 42;
  y := 13;
  println(f"{x} + {y} = {x + y}");
  println(f"{x} - {y} = {x - y}");
  println(f"{x} * {y} = {x * y}");
  println(f"{x} / {y} = {x / y}");
  println(f"{x} % {y} = {x % y}");

  return 0;
}
```

Output:

```
5! = 120
10! = 3628800
fib(10) = 55
fib(20) = 6765
42 + 13 = 55
42 - 13 = 29
42 * 13 = 546
42 / 13 = 3
42 % 13 = 3
```

A few things to notice:

* Functions are defined with `fn`, parameters have type annotations, and the return type follows `->`.
* The `factorial` function calls itself recursively. Mog supports recursion naturally.
* The `fibonacci` function uses a `while` loop with mutable variables. The `:=` operator is used inside the loop (`i = i + 1`) to reassign. Variables declared with an explicit type annotation like `a: i64 = 0` can be reassigned with `=`.
* F-strings can embed arbitrary expressions: `{x + y}` computes the sum inline.
* Integer division (`/`) truncates toward zero, and `%` gives the remainder.

Here is one more example — a program that computes the sum of the first N squares:

```
fn sum_of_squares(n: int) -> int {
  total := 0;
  for i in 1..n + 1 {
    total = total + (i * i);
  }
  return total;
}

fn main() -> int {
  for n in [5, 10, 20, 100] {
    println(f"Sum of squares(1..{n}) = {sum_of_squares(n)}");
  }
  return 0;
}
```

Output:

```
Sum of squares(1..5) = 55
Sum of squares(1..10) = 385
Sum of squares(1..20) = 2870
Sum of squares(1..100) = 338350
```

This example shows `for-in` loops over both ranges (`1..n + 1`) and arrays (`[5, 10, 20, 100]`). We will cover control flow in detail in a later chapter — for now, the syntax should be readable.

What Mog Is Not
---------------

Mog is deliberately not many things. Each omission keeps the language small, the security model tractable, and the compilation fast:

* **Not a systems language.** No raw pointers, no manual memory management, no POSIX syscalls, no direct OS access.
* **Not standalone.** Mog is always embedded in a host application. There is no standard library for file I/O or networking — the host provides everything.
* **Not general-purpose.** Mog is for scripts, plugins, and orchestration. It is not designed for building web servers, operating systems, or databases.
* **Not object-oriented.** No classes, no inheritance, no methods on types. Structs hold data; functions operate on data. Higher-order functions and closures provide the abstraction mechanisms.
* **No macros or metaprogramming.** The language you see is the language that runs. No code generation, no compile-time evaluation, no syntax extensions.
* **No generics.** Beyond tensor dtype parameterization (`tensor<f32>`, `tensor<f16>`), there are no generic types or functions. This keeps the type system simple and the compiler small.
* **No exceptions with stack unwinding.** Error handling uses `Result<T>` with explicit propagation via `?`. Errors are values, not control flow.
* **No threads or locks.** Concurrency is cooperative via `async`/`await`, with the host managing the event loop.

If you need any of these features, Mog is probably not the right language for your use case — and that’s fine. Mog is designed to do a few things well rather than everything adequately.

What’s Next
-----------

You now know how to write, compile, and run a Mog program. You have seen the basic program structure, comments, print functions, and how to define and call functions with typed parameters. Chapter 2 covers variables and bindings in depth — how `:=` and `=` work, type annotations, and scoping rules.



Chapter 2: Variables and Bindings
=================================

Mog keeps variable declaration simple: there are no `var`, `let`, or `const` keywords. You create bindings with `:=` and reassign them with `=`. That’s it.

Creating Bindings with `:=`
---------------------------

The `:=` operator declares a new variable and assigns it a value. The type is inferred from the right-hand side:

```
name := "Alice";
age := 30;
score := 95.5;
active := true;
```

Every binding needs an initial value — there are no uninitialized variables in Mog.

```
fn main() {
  greeting := "hello, world";
  count := 0;
  pi := 3.14159;
  print(greeting);
  print(count);
  print(pi);
}
```

You can create bindings in sequence, and later bindings can reference earlier ones:

```
fn main() {
  width := 10;
  height := 20;
  area := width * height;
  print("area = {area}");  // area = 200
}
```

Bindings work inside any block scope — function bodies, `if` branches, loop bodies:

```
fn main() {
  x := 42;
  if x > 0 {
    label := "positive";
    print(label);
  }
  // label is not accessible here
}
```

Reassignment with `=`
---------------------

Once a variable exists, use `=` to change its value. All variables in Mog are mutable:

```
fn main() {
  count := 0;
  count = 1;
  count = count + 1;
  print(count);  // 2
}
```

The distinction matters: `:=` creates, `=` updates. Using `=` on a name that doesn’t exist is a compile error. Using `:=` on a name that already exists in the same scope creates a new shadowed binding (see below).

```
fn main() {
  x := 10;
  x = 20;       // reassignment — fine
  x = x * 2;    // reassignment — x is now 40
  print(x);     // 40
}
```

A common pattern is accumulating a result in a loop:

```
fn main() {
  total := 0;
  for i in 1..11 {
    total = total + i;
  }
  print(total);  // 55
}
```

Building a string incrementally:

```
fn main() {
  result := "";
  names := ["Alice", "Bob", "Charlie"];
  for i, name in names {
    if i > 0 {
      result = result + ", ";
    }
    result = result + name;
  }
  print(result);  // Alice, Bob, Charlie
}
```

Type Annotations
----------------

Mog infers types from the right-hand side, but you can annotate explicitly when you want to be clear about intent:

```
x := 42;             // inferred as int
x: int = 42;         // explicit — same result

ratio := 3.14;       // inferred as float
ratio: float = 3.14; // explicit — same result

name := "Mog";       // inferred as string
name: string = "Mog"; // explicit
```

Explicit annotations are useful when the default inference isn’t what you want:

```
// Without annotation, 42 is int
n := 42;

// With annotation, you can specify a different integer type
n: i32 = 42;
n: u64 = 42;
```

They also help document intent in longer functions:

```
fn process_data(items: [string]) -> int {
  count: int = 0;
  total_length: int = 0;

  for item in items {
    count = count + 1;
    total_length = total_length + item.len;
  }

  average: float = total_length as float / count as float;
  print("average length: {average}");
  return count;
}
```

Note: function parameters and return types always require type annotations. There is no inference for function signatures:

```
fn add(a: int, b: int) -> int {
  return a + b;
}
```

Shadowing
---------

Using `:=` with a name that already exists in the current scope creates a *new* binding that shadows the old one. The old value is no longer accessible:

```
fn main() {
  x := 10;
  print(x);     // 10

  x := "hello";  // shadows the previous x — this is a new binding
  print(x);      // hello
}
```

Shadowing is useful when you want to transform a value and keep the same name:

```
fn main() {
  input := "  hello world  ";
  input := input.trim();
  input := input.upper();
  print(input);  // HELLO WORLD
}
```

Each `:=` creates a genuinely new variable. The shadowed and shadowing variables can have different types:

```
fn main() {
  value := 42;          // int
  value := str(value);  // string — shadows the int
  print(value);         // "42"
}
```

Inner scopes can also shadow outer variables without affecting them:

```
fn main() {
  x := "outer";
  if true {
    x := "inner";  // shadows outer x inside this block
    print(x);      // inner
  }
  print(x);        // outer — unchanged
}
```

Compare this to reassignment, which modifies the existing variable:

```
fn main() {
  x := "outer";
  if true {
    x = "modified";  // reassigns the outer x
  }
  print(x);          // modified
}
```

Practical Examples
------------------

### Swapping Two Values

```
fn main() {
  a := 10;
  b := 20;

  temp := a;
  a = b;
  b = temp;

  print("a = {a}, b = {b}");  // a = 20, b = 10
}
```

### Fibonacci Sequence

```
fn fibonacci(n: int) -> int {
  if n <= 1 { return n; }

  a := 0;
  b := 1;
  for i in 2..n+1 {
    temp := a + b;
    a = b;
    b = temp;
  }
  return b;
}

fn main() {
  for i in 0..10 {
    print(fibonacci(i));
  }
}
```

### Processing a List

```
fn main() {
  scores := [85, 92, 78, 95, 88];

  sum := 0;
  max_score := scores[0];
  min_score := scores[0];

  for score in scores {
    sum = sum + score;
    if score > max_score {
      max_score = score;
    }
    if score < min_score {
      min_score = score;
    }
  }

  average := sum as float / scores.len as float;
  print("average: {average}");
  print("max: {max_score}");
  print("min: {min_score}");
}
```

### Counting Occurrences

```
fn count_char(s: string, target: string) -> int {
  count := 0;
  parts := s.split("");
  for ch in parts {
    if ch == target {
      count = count + 1;
    }
  }
  return count;
}

fn main() {
  text := "hello world";
  l_count := count_char(text, "l");
  print("l appears {l_count} times");  // l appears 3 times
}
```

Summary
-------

| Syntax | Meaning |
| --- | --- |
| `x := 42;` | Create a new binding (type inferred) |
| `x: int = 42;` | Create a new binding (type explicit) |
| `x = 100;` | Reassign an existing binding |
| `x := "hi";` | Shadow — create a new binding with the same name |

The rule is simple: `:=` introduces, `=` updates. When in doubt, use `:=` for new things and `=` for changing existing things.



Chapter 3: Types and Operators
==============================

Mog is statically typed with no implicit coercion. Every value has a known type at compile time, and the compiler will reject any operation that mixes types without an explicit conversion.

Scalar Types
------------

Mog has four categories of scalar types: integers, floats, booleans, and strings.

### Integers

The default integer type is `int` — a 64-bit signed integer. This is what you should use for virtually all integer work:

```
count := 42;              // int (inferred)
count: int = 42;          // int (explicit)
negative := -17;          // int
big := 1_000_000;         // int — underscores for readability
```

Integer literals support multiple bases:

```
decimal := 255;           // decimal
hex := 0xFF;              // hexadecimal
binary := 0b11111111;     // binary
with_sep := 1_000_000;    // underscores ignored, just for readability
```

All four of these hold the same value: 255 (except `with_sep`, which is 1,000,000).

### Explicit-Width Integers

When precision matters — tensor element types, bitwise operations, or interop with hardware — Mog provides explicit-width integers:

```
small: i32 = 42;          // 32-bit signed
index: u32 = 0;           // 32-bit unsigned
offset: u64 = 1024;       // 64-bit unsigned
```

The commonly used integer types:

| Type | Width | Range |
| --- | --- | --- |
| `int` | 64-bit signed | -2^63 to 2^63 - 1 |
| `i32` | 32-bit signed | -2^31 to 2^31 - 1 |
| `u32` | 32-bit unsigned | 0 to 2^32 - 1 |
| `u64` | 64-bit unsigned | 0 to 2^64 - 1 |

> Mog also supports `i8`, `i16`, `u8`, and `u16`, but you’ll rarely need them outside of tensor element types. Use `int` unless you have a specific reason to reach for something else.

In practice, the explicit-width types exist primarily for tensors and low-level work:

```
// Scalar code: just use int
count := 0;
limit := 100;

// Tensor code: width matters
indices := tensor<i32>([1000]);
image := tensor<u8>([3, 224, 224]);
```

### Floats

The default float type is `float` — a 64-bit (double-precision) floating point number:

```
pi := 3.14159;            // float (inferred)
pi: float = 3.14159;      // float (explicit)
small := 1.0e-5;          // scientific notation
half := .5;               // leading dot is allowed
```

For single-precision, use `f32`:

```
ratio: f32 = 0.75;
```

The commonly used float types:

| Type | Width | Use case |
| --- | --- | --- |
| `float` | 64-bit (double) | Default for all float math |
| `f32` | 32-bit (single) | Tensor element type, GPU work |

> Mog also supports `f16` and `bf16` (bfloat16) for ML tensor element types — see Chapter 15 for details on tensors. For scalar code, always use `float`.

```
// Scalar code: just use float
loss := 0.0;
learning_rate := 0.001;

// Tensor code: precision matters
weights := tensor<f16>([768, 768]);
gradients := tensor<f32>([768, 768]);
```

### Booleans

The `bool` type has two values: `true` and `false`.

```
active := true;
found := false;
is_valid: bool = true;
```

Booleans are returned by comparison and logical operators:

```
fn main() -> int {
  x := 42;
  is_positive := x > 0;       // true
  is_even := (x % 2) == 0;     // true
  both := is_positive && is_even;  // true
  println(both);
  return 0;
}
```

There are no truthy/falsy values in Mog. Conditions must be actual `bool` values — you can’t use `0`, `""`, or `none` as a boolean:

```
count := 0;
// if count { ... }       // compile error — count is int, not bool
if count == 0 { ... }     // correct
```

> **No implicit boolean conversions.** This is deliberate — it catches a whole class of bugs at compile time. If you want a boolean, write a comparison.

### Strings

Strings are UTF-8, immutable, and double-quoted only:

```
name := "Alice";
greeting := "hello, world";
empty := "";
```

Strings support escape sequences:

| Escape | Meaning |
| --- | --- |
| `\n` | Newline |
| `\t` | Tab |
| `\\` | Backslash |
| `\"` | Double quote |

```
newline := "line one\nline two";
tab := "col1\tcol2";
quote := "she said \"hello\"";
backslash := "C:\\Users\\alice";
```

String interpolation uses f-strings — prefix the string with `f` and wrap expressions in `{braces}`:

```
name := "Alice";
age := 30;
greeting := f"hello {name}";              // "hello Alice"
info := f"{name} is {age} years old";     // "Alice is 30 years old"
math := f"2 + 2 = {2 + 2}";              // "2 + 2 = 4"
```

Concatenation uses `+`:

```
first := "hello";
second := " world";
combined := first + second;  // "hello world"
```

> For most cases, f-string interpolation is cleaner than concatenation — see the String Concatenation section at the end of this chapter.

Type Conversions
----------------

Mog has no implicit coercion. If you want to convert between types, you must be explicit.

### The `as` Keyword

Use `as` to cast between numeric types:

```
// int to float
x := 42;
y := x as float;          // 42.0

// float to int (truncates toward zero)
pi := 3.14;
n := pi as int;            // 3

// int to narrower int
big := 1000;
small := big as i32;

// Between float widths
precise: float = 3.14159265358979;
approx := precise as f32;
```

`as` works between any numeric types:

```
count := 42;
count_f := count as float;   // 42.0
count_i32 := count as i32;   // 42 (as 32-bit)
count_u64 := count as u64;   // 42 (as unsigned 64-bit)
```

> **Warning:** Narrowing conversions can lose data. Casting a large `int` to `i8` will wrap on overflow — no runtime error, just silent truncation.

### String Conversions

Use `str()` to convert any scalar to a string:

```
s1 := str(42);         // "42"
s2 := str(3.14);       // "3.14"
s3 := str(true);       // "true"
s4 := str(false);      // "false"
```

To parse strings into numbers, use `int_from_string()` and `parse_float()`. These return `Result` because parsing can fail (see Chapter 10 for full coverage of error handling):

```
result := int_from_string("42");
match result {
  ok(n) => println(f"parsed: {n}"),
  err(msg) => println(f"failed: {msg}"),
}

pi := parse_float("3.14");
match pi {
  ok(f) => println(f"got: {f}"),
  err(msg) => println(f"bad float: {msg}"),
}
```

Using the `?` operator for concise error propagation:

```
fn parse_pair(a: string, b: string) -> Result<int> {
  x := int_from_string(a)?;
  y := int_from_string(b)?;
  return ok(x + y);
}
```

### No Implicit Conversions

Mog will not silently convert between types. Every one of these is a compile error:

```
x := 42;
y := 3.14;

// z := x + y;           // error: can't add int and float
z := x as float + y;     // correct: explicit cast first

// flag := x;            // error if flag is typed as bool
flag := x != 0;          // correct: explicit comparison
```

This strictness catches bugs early. If Mog rejects an expression, it’s telling you to think about what conversion you actually want.

Operators
---------

### Arithmetic Operators

Standard math operators work on numeric types. Both operands must be the same type:

```
fn main() -> int {
  a := 10;
  b := 3;

  println(a + b);    // 13   addition
  println(a - b);    // 7    subtraction
  println(a * b);    // 30   multiplication
  println(a / b);    // 3    integer division (truncates)
  println(a % b);    // 1    modulo (remainder)
  return 0;
}
```

With floats:

```
fn main() -> int {
  a := 10.0;
  b := 3.0;

  println(a + b);    // 13.0
  println(a - b);    // 7.0
  println(a * b);    // 30.0
  println(a / b);    // 3.3333333333333335
  println(a % b);    // 1.0
  return 0;
}
```

Integer division truncates toward zero:

```
fn main() -> int {
  println(7 / 2);     // 3
  println(-7 / 2);    // -3
  println(7 / -2);    // -3
  return 0;
}
```

### Comparison Operators

Comparisons return `bool`. Both operands must be the same type:

```
fn main() -> int {
  x := 10;
  y := 20;

  println(x == y);    // false  — equal
  println(x != y);    // true   — not equal
  println(x < y);     // true   — less than
  println(x > y);     // false  — greater than
  println(x <= y);    // true   — less or equal
  println(x >= y);    // false  — greater or equal
  return 0;
}
```

Strings compare lexicographically:

```
fn main() -> int {
  println("apple" < "banana");    // true
  println("abc" == "abc");        // true
  println("Abc" == "abc");        // false — case sensitive
  return 0;
}
```

### Logical Operators

Logical operators work on `bool` values only:

```
fn main() -> int {
  a := true;
  b := false;

  println(a && b);    // false  — logical AND
  println(a || b);    // true   — logical OR
  println(!a);        // false  — logical NOT
  println(!b);        // true
  return 0;
}
```

`&&` and `||` short-circuit: the right side is only evaluated if needed:

```
fn check(items: [int], index: int) -> bool {
  // Safe: if index is out of bounds, the second condition is never evaluated
  return (index < items.len) && (items[index] > 0);
}
```

Combining conditions:

```
fn is_valid_age(age: int) -> bool {
  return (age >= 0) && (age <= 150);
}

fn needs_review(score: int, flagged: bool) -> bool {
  return (score < 50) || flagged;
}
```

### Bitwise Operators

Bitwise operators work on integer types:

```
fn main() -> int {
  a := 0b1100;    // 12
  b := 0b1010;    // 10

  println(a & b);    // 8    — bitwise AND
  println(a | b);    // 14   — bitwise OR
  println(a ^ b);    // 6    — bitwise XOR
  println(a << 2);   // 48   — left shift
  println(a >> 1);   // 6    — right shift
  return 0;
}
```

Common bitwise patterns:

```
fn main() -> int {
  // Check if a number is even
  n := 42;
  is_even := (n & 1) == 0;    // true

  // Set a flag bit
  flags := 0;
  flags = flags | 0b0100;     // set bit 2

  // Clear a flag bit
  flags = flags & 0b1011;     // clear bit 2

  // Toggle a flag bit
  flags = flags ^ 0b0010;     // toggle bit 1
  return 0;
}
```

### String Concatenation

The `+` operator concatenates strings:

```
fn main() -> int {
  greeting := "hello" + " " + "world";
  println(greeting);  // hello world

  name := "Alice";
  message := "hi, " + name + "!";
  println(message);  // hi, Alice!
  return 0;
}
```

For most cases, f-string interpolation is cleaner than concatenation:

```
// Concatenation
message := "User " + name + " scored " + str(score) + " points";

// Interpolation — prefer this
message := f"User {name} scored {score} points";
```

Flat Operators (No Precedence)
------------------------------

Mog has **no operator precedence**. All binary operators are flat — the compiler does not
silently reorder operations based on a precedence table. Instead, Mog enforces explicit
grouping through two simple rules:

**1. Associative operators can chain with themselves.**
The operators `+`, `*`, `and`/`&&`, `or`/`||`, `&`, and `|` are associative, so
repeating the same one is unambiguous:

```
total := a + b + c;           // OK — same operator throughout
mask := READ | WRITE | EXEC;  // OK
all_ok := x && y && z;        // OK
```

**2. Everything else requires parentheses.**

* **Different operators cannot mix.** Use parentheses to show intent:

```
result := a + (b * c);              // OK — parens make grouping explicit
result := a + b * c;                // COMPILE ERROR — mixed + and *

check := (x > 0) && (y > 0);       // OK
check := x > 0 && y > 0;           // COMPILE ERROR — mixed > and &&

is_even := (n % 2) == 0;           // OK
is_even := n % 2 == 0;             // COMPILE ERROR — mixed % and ==
```

* **Non-associative operators cannot chain**, even with themselves:

```
diff := (a - b) - c;               // OK — parenthesized
diff := a - b - c;                  // COMPILE ERROR — - is non-associative

ratio := (a / b) / c;              // OK
ratio := a / b / c;                // COMPILE ERROR — / is non-associative
```

Non-associative operators: `-`, `/`, `%`, `==`, `!=`, `<`, `<=`, `>`, `>=`, `<<`, `>>`, `^`.

### Why no precedence?

Precedence tables are a common source of bugs — especially when mixing arithmetic,
comparison, and logical operators. Mog makes every grouping decision visible in the
source code. The cost is a few extra parentheses; the benefit is that the code always
means exactly what it says.

```
// Clear and correct
fahrenheit := ((celsius * 9) / 5) + 32;
in_range := (x >= low) && (x <= high);
masked := (flags & MASK) != 0;
```

Common Patterns
---------------

### Clamping a Value

```
fn clamp(value: int, low: int, high: int) -> int {
  if value < low { return low; }
  if value > high { return high; }
  return value;
}

fn main() -> int {
  score := 150;
  clamped := clamp(score, 0, 100);
  println(clamped);  // 100
  return 0;
}
```

### Safe Division

```
fn safe_divide(a: float, b: float) -> Result<float> {
  if b == 0.0 {
    return err("division by zero");
  }
  return ok(a / b);
}

fn main() -> int {
  match safe_divide(10.0, 3.0) {
    ok(result) => println(f"result: {result}"),
    err(msg) => println(f"error: {msg}"),
  }
  return 0;
}
```

### Type-Aware Accumulation

```
fn average(numbers: [int]) -> float {
  sum := 0;
  for n in numbers {
    sum = sum + n;
  }
  return (sum as float) / (numbers.len as float);
}

fn main() -> int {
  scores := [85, 92, 78, 95, 88];
  avg := average(scores);
  println(f"average: {avg}");  // average: 87.6
  return 0;
}
```

### Bitflag Permissions

```
fn main() -> int {
  READ := 1;       // 0b001
  WRITE := 2;      // 0b010
  EXEC := 4;       // 0b100

  // Grant read and write
  perms := READ | WRITE;

  // Check permissions
  can_read := (perms & READ) != 0;     // true
  can_exec := (perms & EXEC) != 0;     // false

  // Add execute permission
  perms = perms | EXEC;
  can_exec = (perms & EXEC) != 0;      // true

  println(f"read: {can_read}");
  println(f"exec: {can_exec}");
  return 0;
}
```

### Building Results with Type Conversion

```
fn format_percentage(value: int, total: int) -> string {
  pct := (value as float / total as float) * 100.0;
  return str(round(pct)) + "%";
}

fn main() -> int {
  passed := 87;
  total := 100;
  println(format_percentage(passed, total));  // 87%
  return 0;
}
```

Summary
-------

Mog’s type system is small and strict:

* **Use `int` and `float`** for almost everything. Reach for `i32`, `u32`, `u64`, or `f32` only when working with tensors or hardware interop.
* **No implicit coercion.** Use `as` for numeric casts, `str()` for string conversion, `int_from_string()` and `parse_float()` for parsing.
* **Operators require matching types.** Both sides of `+`, `*`, `==`, etc. must be the same type.
* **Booleans are booleans.** No truthy/falsy — use explicit comparisons.
* **Operators are flat — no precedence.** Different operators cannot mix without parentheses, and non-associative operators cannot chain. This eliminates an entire class of bugs.


Chapter 4: Control Flow
=======================

Mog’s control flow is familiar if you’ve used any C-family language: `if`/`else`, `while`, `for`, `break`, `continue`, and `match`. No surprises — but a few details matter, like braces being required, `if` working as an expression, and `match` handling Result and Optional patterns.

If/Else
-------

The basic form: a condition, a block, and optional `else if` / `else` chains. Braces are always required. Parentheses around the condition are optional.

```
fn main() -> int {
  x := 42;

  if x > 0 {
    println("positive");
  } else if x == 0 {
    println("zero");
  } else {
    println("negative");
  }
  return 0;
}
```

Parentheses are allowed but not required — use them when they help readability:

```
fn main() -> int {
  a := 10;
  b := 20;

  // Both of these are valid
  if a > b {
    println("a wins");
  }

  if (a + b) > 25 {
    println("sum is large");
  }
  return 0;
}
```

### Nested Conditions

Chains of `else if` work exactly as you’d expect. For complex classification, they read top to bottom:

```
fn classify_temperature(temp: int) -> string {
  if temp >= 100 {
    return "boiling";
  } else if temp >= 80 {
    return "very hot";
  } else if temp >= 60 {
    return "warm";
  } else if temp >= 40 {
    return "cool";
  } else if temp >= 20 {
    return "cold";
  } else {
    return "freezing";
  }
}

fn main() -> int {
  println(classify_temperature(95));   // very hot
  println(classify_temperature(55));   // warm
  println(classify_temperature(-10));  // freezing
  return 0;
}
```

Nested `if` blocks inside other `if` blocks:

```
fn describe_number(n: int) -> string {
  if n > 0 {
    if (n % 2) == 0 {
      return "positive even";
    } else {
      return "positive odd";
    }
  } else if n < 0 {
    if (n % 2) == 0 {
      return "negative even";
    } else {
      return "negative odd";
    }
  } else {
    return "zero";
  }
}

fn main() -> int {
  println(describe_number(7));    // positive odd
  println(describe_number(-4));   // negative even
  println(describe_number(0));    // zero
  return 0;
}
```

### If as Expression

`if` can return a value. The last expression in each branch becomes the result. When used this way, `else` is required — the compiler needs a value for every case:

```
fn main() -> int {
  x := 42;

  sign := if x > 0 { 1 } else if x < 0 { -1 } else { 0 };
  println(f"sign of {x}: {sign}");  // sign of 42: 1
  return 0;
}
```

This works anywhere you need an expression:

```
fn abs(n: int) -> int {
  return if n >= 0 { n } else { 0 - n };
}

fn max(a: int, b: int) -> int {
  return if a > b { a } else { b };
}

fn min(a: int, b: int) -> int {
  return if a < b { a } else { b };
}

fn main() -> int {
  println(abs(-17));       // 17
  println(max(10, 20));    // 20
  println(min(10, 20));    // 10
  return 0;
}
```

If-expressions are useful for inline decisions without creating temporary variables:

```
fn format_count(n: int) -> string {
  label := if n == 1 { "item" } else { "items" };
  return f"{n} {label}";
}

fn main() -> int {
  println(format_count(1));   // 1 item
  println(format_count(5));   // 5 items
  println(format_count(0));   // 0 items
  return 0;
}
```

Combining conditions with logical operators:

```
fn can_vote(age: int, is_citizen: bool) -> bool {
  return (age >= 18) && is_citizen;
}

fn main() -> int {
  age := 25;
  citizen := true;

  if can_vote(age, citizen) {
    println("eligible to vote");
  } else {
    println("not eligible");
  }

  // Compound conditions
  score := 85;
  if score >= 90 {
    println("A");
  } else if (score >= 80) && (score < 90) {
    println("B");
  } else if (score >= 70) && (score < 80) {
    println("C");
  } else {
    println("below C");
  }
  return 0;
}
```

While Loops
-----------

`while` repeats a block as long as a condition is true:

```
fn main() -> int {
  i := 0;
  while i < 5 {
    println(f"i = {i}");
    i = i + 1;
  }
  return 0;
}
```

### Accumulator Pattern

The most common use of `while` is accumulating a result when the loop condition depends on something more complex than a simple range:

```
fn sum_1_to_n(n: int) -> int {
  total := 0;
  i := 1;
  while i <= n {
    total = total + i;
    i = i + 1;
  }
  return total;
}

fn main() -> int {
  println(f"sum 1..100 = {sum_1_to_n(100)}");  // sum 1..100 = 5050
  return 0;
}
```

Factorial with a while loop:

```
fn factorial(n: int) -> int {
  result := 1;
  i := 2;
  while i <= n {
    result = result * i;
    i = i + 1;
  }
  return result;
}

fn main() -> int {
  println(f"5! = {factorial(5)}");    // 5! = 120
  println(f"10! = {factorial(10)}");  // 10! = 3628800
  return 0;
}
```

### Convergence Loops

`while` is the right choice when you’re iterating until a condition is met, not over a known range:

```
fn collatz_steps(n: int) -> int {
  steps := 0;
  val := n;
  while val != 1 {
    if (val % 2) == 0 {
      val = val / 2;
    } else {
      val = (val * 3) + 1;
    }
    steps = steps + 1;
  }
  return steps;
}

fn main() -> int {
  println(f"collatz(27) = {collatz_steps(27)} steps");  // collatz(27) = 111 steps
  println(f"collatz(1) = {collatz_steps(1)} steps");    // collatz(1) = 0 steps
  return 0;
}
```

Integer square root by repeated approximation:

```
fn isqrt(n: int) -> int {
  if n <= 1 { return n; }
  guess := n / 2;
  while (guess * guess) > n {
    guess = (guess + (n / guess)) / 2;
  }
  return guess;
}

fn main() -> int {
  println(f"isqrt(100) = {isqrt(100)}");  // isqrt(100) = 10
  println(f"isqrt(50) = {isqrt(50)}");    // isqrt(50) = 7
  return 0;
}
```

### Infinite Loops

Use `while true` for loops that exit with `break`:

```
fn main() -> int {
  sum := 0;
  n := 1;
  while true {
    sum = sum + n;
    if sum > 100 {
      break;
    }
    n = n + 1;
  }
  println(f"stopped at n={n}, sum={sum}");  // stopped at n=14, sum=105
  return 0;
}
```

For Loops
---------

Mog has two styles of `for` loop: `for..to` with an inclusive upper bound, and `for..in` which iterates over ranges, arrays, and maps.

### For-To (Inclusive Range)

`for..to` counts from a start value to an end value, inclusive of both ends:

```
fn main() -> int {
  for i := 1 to 5 {
    println(f"i = {i}");
  }
  // prints: 1, 2, 3, 4, 5
  return 0;
}
```

The counter variable is scoped to the loop body — it doesn’t exist outside:

```
fn main() -> int {
  for i := 1 to 10 {
    println(i);
  }
  // i is not accessible here
  return 0;
}
```

Summing with `for..to`:

```
fn main() -> int {
  total := 0;
  for i := 1 to 100 {
    total = total + i;
  }
  println(f"sum = {total}");  // sum = 5050
  return 0;
}
```

### For-In Range (Exclusive End)

The `..` range operator creates a half-open range — inclusive of the start, exclusive of the end:

```
fn main() -> int {
  for i in 0..5 {
    println(f"i = {i}");
  }
  // prints: 0, 1, 2, 3, 4
  return 0;
}
```

This is the natural choice for zero-based indexing:

```
fn main() -> int {
  names := ["Alice", "Bob", "Charlie"];
  for i in 0..names.len {
    println(f"index {i}: {names[i]}");
  }
  return 0;
}
```

Computing a power function:

```
fn power(base: int, exp: int) -> int {
  result := 1;
  for i in 0..exp {
    result = result * base;
  }
  return result;
}

fn main() -> int {
  println(f"2^10 = {power(2, 10)}");    // 2^10 = 1024
  println(f"3^5 = {power(3, 5)}");      // 3^5 = 243
  return 0;
}
```

### When to Use Which

| Style | Syntax | End Bound | Best For |
| --- | --- | --- | --- |
| `for..to` | `for i := 1 to 10` | Inclusive | Human-friendly ranges (“1 through 10”) |
| `for..in` range | `for i in 0..10` | Exclusive | Array indexing, zero-based iteration |

```
fn main() -> int {
  // Print multiplication table for 7 — "1 through 10" is natural
  for i := 1 to 10 {
    println(f"7 x {i} = {7 * i}");
  }

  // Sum array elements — zero-based indexing is natural
  values := [10, 20, 30, 40, 50];
  total := 0;
  for i in 0..values.len {
    total = total + values[i];
  }
  println(f"total = {total}");  // total = 150
  return 0;
}
```

### For-In Array

Iterating directly over array elements — no index needed:

```
fn main() -> int {
  fruits := ["apple", "banana", "cherry", "date"];
  for fruit in fruits {
    println(f"I like {fruit}");
  }
  return 0;
}
```

Summing, filtering, searching:

```
fn sum(numbers: [int]) -> int {
  total := 0;
  for n in numbers {
    total = total + n;
  }
  return total;
}

fn contains(items: [string], target: string) -> bool {
  for item in items {
    if item == target {
      return true;
    }
  }
  return false;
}

fn main() -> int {
  scores := [85, 92, 78, 95, 88];
  println(f"sum = {sum(scores)}");  // sum = 438

  colors := ["red", "green", "blue"];
  println(contains(colors, "green"));  // true
  println(contains(colors, "pink"));   // false
  return 0;
}
```

Collecting results into a new array:

```
fn filter_even(numbers: [int]) -> [int] {
  result: [int] = [];
  for n in numbers {
    if n % 2 == 0 {
      result.push(n);
    }
  }
  return result;
}

fn main() -> int {
  nums := [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  evens := filter_even(nums);
  for n in evens {
    print_string(f"{n} ");
  }
  println("");  // 2 4 6 8 10
  return 0;
}
```

### For-In with Index

When you need both the index and the value, add a second variable before the comma:

```
fn main() -> int {
  names := ["Alice", "Bob", "Charlie", "Diana"];
  for i, name in names {
    println(f"{i}: {name}");
  }
  // 0: Alice
  // 1: Bob
  // 2: Charlie
  // 3: Diana
  return 0;
}
```

This is cleaner than manually tracking an index counter:

```
fn find_index(items: [string], target: string) -> int {
  for i, item in items {
    if item == target {
      return i;
    }
  }
  return -1;
}

fn main() -> int {
  colors := ["red", "green", "blue", "yellow"];
  idx := find_index(colors, "blue");
  println(f"blue is at index {idx}");  // blue is at index 2

  idx2 := find_index(colors, "purple");
  println(f"purple is at index {idx2}");  // purple is at index -1
  return 0;
}
```

Printing a numbered list:

```
fn main() -> int {
  tasks := ["write code", "run tests", "fix bugs", "deploy"];
  for i, task in tasks {
    println(f"  {i + 1}. {task}");
  }
  //   1. write code
  //   2. run tests
  //   3. fix bugs
  //   4. deploy
  return 0;
}
```

Finding the maximum element and its position:

```
fn max_with_index(numbers: [int]) -> [int] {
  best := numbers[0];
  best_idx := 0;
  for i, n in numbers {
    if n > best {
      best = n;
      best_idx = i;
    }
  }
  return [best_idx, best];
}

fn main() -> int {
  scores := [72, 95, 88, 91, 67];
  result := max_with_index(scores);
  println(f"max value {result[1]} at index {result[0]}");  // max value 95 at index 1
  return 0;
}
```

### For-In Map

Maps iterate as key-value pairs:

```
fn main() -> int {
  scores := {"alice": 95, "bob": 87, "charlie": 92};

  for name, score in scores {
    println(f"{name} scored {score}");
  }
  return 0;
}
```

Building a report from a map:

```
fn main() -> int {
  inventory := {"apples": 12, "bananas": 5, "oranges": 8, "grapes": 0};

  total := 0;
  out_of_stock := 0;

  for item, count in inventory {
    total = total + count;
    if count == 0 {
      println(f"  WARNING: {item} is out of stock");
      out_of_stock = out_of_stock + 1;
    }
  }

  println(f"total items: {total}");
  println(f"out of stock: {out_of_stock}");
  return 0;
}
```

Transforming map data:

```
fn main() -> int {
  temps_celsius := {"London": 15, "Tokyo": 28, "New York": 22, "Sydney": 19};

  for city, celsius in temps_celsius {
    fahrenheit := ((celsius * 9) / 5) + 32;
    println(f"{city}: {celsius}C = {fahrenheit}F");
  }
  return 0;
}
```

Counting occurrences with a map:

```
fn main() -> int {
  words := ["the", "cat", "sat", "on", "the", "mat", "the", "cat"];
  counts: {string: int} = {};

  for word in words {
    if counts[word] is some(n) {
      counts[word] = n + 1;
    } else {
      counts[word] = 1;
    }
  }

  for word, count in counts {
    println(f"{word}: {count}");
  }
  return 0;
}
```

Break and Continue
------------------

`break` exits the innermost enclosing loop immediately. `continue` skips the rest of the current iteration and moves to the next one.

### Break

```
fn main() -> int {
  // Find the first multiple of 7 greater than 50
  for i in 1..100 {
    if (i * 7) > 50 {
      println(f"found: {i} (7 * {i} = {i * 7})");
      break;
    }
  }
  // found: 8 (7 * 8 = 56)
  return 0;
}
```

### Continue

```
fn main() -> int {
  // Print only odd numbers from 0 to 19
  for i in 0..20 {
    if (i % 2) == 0 {
      continue;
    }
    print_string(f"{i} ");
  }
  println("");  // 1 3 5 7 9 11 13 15 17 19
  return 0;
}
```

### Combined Break and Continue

```
fn main() -> int {
  // Sum numbers from 1 to 100, skipping multiples of 3, stopping if sum exceeds 500
  total := 0;
  stopped_at := 0;
  for i in 1..101 {
    if (i % 3) == 0 {
      continue;
    }
    total = total + i;
    if total > 500 {
      stopped_at = i;
      break;
    }
  }
  println(f"stopped at {stopped_at}, total = {total}");
  return 0;
}
```

### Break and Continue in Nested Loops

`break` and `continue` affect only the innermost loop:

```
fn main() -> int {
  // Find the first pair (i, j) where i * j == 42
  found_i := 0;
  found_j := 0;
  done := false;

  for i in 1..20 {
    if done { break; }
    for j in 1..20 {
      if (i * j) == 42 {
        found_i = i;
        found_j = j;
        done = true;
        break;  // breaks the inner loop
      }
    }
  }
  println(f"{found_i} * {found_j} = 42");
  return 0;
}
```

Skipping specific combinations in nested loops:

```
fn main() -> int {
  // Print coordinate pairs, skip the diagonal where i == j
  for i in 0..4 {
    for j in 0..4 {
      if i == j {
        continue;  // skips this iteration of the inner loop
      }
      print_string(f"({i},{j}) ");
    }
  }
  println("");
  return 0;
}
```

A practical example — searching a 2D grid:

```
fn main() -> int {
  grid := [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
  ];

  target := 7;
  found_row := -1;
  found_col := -1;

  for r in 0..3 {
    for c in 0..4 {
      if grid[r][c] == target {
        found_row = r;
        found_col = c;
        break;
      }
    }
    if found_row >= 0 {
      break;
    }
  }

  if found_row >= 0 {
    println(f"found {target} at ({found_row}, {found_col})");  // found 7 at (1, 2)
  } else {
    println(f"{target} not found");
  }
  return 0;
}
```

Match
-----

`match` compares a value against a series of patterns and executes the first one that matches. Arms are separated by commas, and `_` is the wildcard that matches anything.

### Matching Integers

```
fn main() -> int {
  day := 3;
  match day {
    1 => println("Monday"),
    2 => println("Tuesday"),
    3 => println("Wednesday"),
    4 => println("Thursday"),
    5 => println("Friday"),
    6 => println("Saturday"),
    7 => println("Sunday"),
    _ => println("invalid day"),
  }
  return 0;
}
```

### Matching Strings

```
fn describe_color(color: string) -> string {
  return match color {
    "red" => "warm",
    "orange" => "warm",
    "yellow" => "warm",
    "blue" => "cool",
    "green" => "cool",
    "purple" => "cool",
    _ => "unknown",
  };
}

fn main() -> int {
  println(describe_color("red"));      // warm
  println(describe_color("blue"));     // cool
  println(describe_color("magenta"));  // unknown
  return 0;
}
```

### Multi-Statement Arms

When an arm needs more than one expression, wrap it in braces:

```
fn main() -> int {
  code := 404;
  match code {
    200 => println("OK"),
    301 => {
      println("Moved Permanently");
      println("Check the Location header");
    },
    404 => {
      println("Not Found");
      println("The resource does not exist");
    },
    500 => {
      println("Internal Server Error");
      println("Something went wrong on the server");
    },
    _ => println(f"HTTP {code}"),
  }
  return 0;
}
```

### Match as Expression

`match` returns a value, so you can assign its result:

```
fn main() -> int {
  score := 85;
  grade := match score / 10 {
    10 => "A+",
    9 => "A",
    8 => "B",
    7 => "C",
    6 => "D",
    _ => "F",
  };
  println(f"score {score} -> grade {grade}");  // score 85 -> grade B
  return 0;
}
```

Using match to drive computation:

```
fn fibonacci(n: int) -> int {
  return match n {
    0 => 0,
    1 => 1,
    _ => fibonacci(n - 1) + fibonacci(n - 2),
  };
}

fn main() -> int {
  for i in 0..10 {
    print_string(f"{fibonacci(i)} ");
  }
  println("");  // 0 1 1 2 3 5 8 13 21 34
  return 0;
}
```

Assigning different values based on a key:

```
fn http_status_message(code: int) -> string {
  return match code {
    200 => "OK",
    201 => "Created",
    204 => "No Content",
    301 => "Moved Permanently",
    400 => "Bad Request",
    401 => "Unauthorized",
    403 => "Forbidden",
    404 => "Not Found",
    500 => "Internal Server Error",
    502 => "Bad Gateway",
    503 => "Service Unavailable",
    _ => f"Unknown ({code})",
  };
}

fn main() -> int {
  codes := [200, 404, 500, 418];
  for code in codes {
    println(f"{code}: {http_status_message(code)}");
  }
  // 200: OK
  // 404: Not Found
  // 500: Internal Server Error
  // 418: Unknown (418)
  return 0;
}
```

### Matching on Result and Optional

Mog’s `Result<T>` and Optional (`?T`) types have variants that `match` can destructure. This is a brief preview — Chapter 10 covers error handling in depth.

**Result patterns:** `ok(value)` and `err(message)`:

```
fn safe_divide(a: int, b: int) -> Result<int> {
  if b == 0 {
    return err("division by zero");
  }
  return ok(a / b);
}

fn main() -> int {
  result := safe_divide(42, 6);
  match result {
    ok(value) => println(f"result: {value}"),
    err(msg) => println(f"error: {msg}"),
  }

  result2 := safe_divide(10, 0);
  match result2 {
    ok(value) => println(f"result: {value}"),
    err(msg) => println(f"error: {msg}"),
  }
  // result: 7
  // error: division by zero
  return 0;
}
```

**Optional patterns:** `some(value)` and `none`:

```
fn find_positive(numbers: [int]) -> ?int {
  for n in numbers {
    if n > 0 {
      return some(n);
    }
  }
  return none;
}

fn main() -> int {
  result := find_positive([-3, -1, 4, -2, 5]);
  val := match result {
    some(n) => n,
    none => 0,
  };
  println(f"first positive: {val}");  // first positive: 4

  result2 := find_positive([-3, -1, -2]);
  val2 := match result2 {
    some(n) => n,
    none => 0,
  };
  println(f"first positive: {val2}");  // first positive: 0
  return 0;
}
```

Match on Result with multi-statement arms:

```
fn parse_and_double(input: string) -> Result<int> {
  n := int_from_string(input)?;
  return ok(n * 2);
}

fn main() -> int {
  inputs := ["21", "abc", "50"];
  for input in inputs {
    match parse_and_double(input) {
      ok(value) => {
        println(f"  '{input}' -> {value}");
      },
      err(msg) => {
        println(f"  '{input}' failed: {msg}");
      },
    }
  }
  //   '21' -> 42
  //   'abc' failed: invalid integer
  //   '50' -> 100
  return 0;
}
```

Practical Examples
------------------

### Fibonacci (Iterative)

```
fn fibonacci(n: int) -> int {
  if n <= 1 { return n; }

  a := 0;
  b := 1;
  for i in 2..n+1 {
    temp := a + b;
    a = b;
    b = temp;
  }
  return b;
}

fn main() -> int {
  for i in 0..15 {
    println(f"fib({i}) = {fibonacci(i)}");
  }
  return 0;
}
```

### Sum of Squares

```
fn sum_of_squares(n: int) -> int {
  total := 0;
  for i := 1 to n {
    total = total + (i * i);
  }
  return total;
}

fn main() -> int {
  println(f"sum of squares 1..10 = {sum_of_squares(10)}");  // 385
  println(f"sum of squares 1..100 = {sum_of_squares(100)}");  // 338350
  return 0;
}
```

### Linear Search

```
fn linear_search(items: [int], target: int) -> int {
  for i, item in items {
    if item == target {
      return i;
    }
  }
  return -1;
}

fn main() -> int {
  data := [4, 8, 15, 16, 23, 42];

  idx := linear_search(data, 23);
  println(f"23 is at index {idx}");  // 23 is at index 4

  idx2 := linear_search(data, 99);
  println(f"99 is at index {idx2}");  // 99 is at index -1
  return 0;
}
```

### Bubble Sort

```
fn bubble_sort(arr: [int]) -> [int] {
  sorted := arr;
  n := sorted.len;
  for i in 0..n {
    for j in 0..((n - i) - 1) {
      if sorted[j] > sorted[j + 1] {
        temp := sorted[j];
        sorted[j] = sorted[j + 1];
        sorted[j + 1] = temp;
      }
    }
  }
  return sorted;
}

fn main() -> int {
  data := [64, 34, 25, 12, 22, 11, 90];
  sorted := bubble_sort(data);
  for n in sorted {
    print_string(f"{n} ");
  }
  println("");  // 11 12 22 25 34 64 90
  return 0;
}
```

### FizzBuzz

```
fn main() -> int {
  for i := 1 to 30 {
    if (i % 15) == 0 {
      println("FizzBuzz");
    } else if (i % 3) == 0 {
      println("Fizz");
    } else if (i % 5) == 0 {
      println("Buzz");
    } else {
      println(i);
    }
  }
  return 0;
}
```

### GCD (Euclidean Algorithm)

```
fn gcd(a: int, b: int) -> int {
  x := a;
  y := b;
  while y != 0 {
    temp := y;
    y = x % y;
    x = temp;
  }
  return x;
}

fn main() -> int {
  println(f"gcd(48, 18) = {gcd(48, 18)}");    // gcd(48, 18) = 6
  println(f"gcd(100, 75) = {gcd(100, 75)}");   // gcd(100, 75) = 25
  println(f"gcd(17, 13) = {gcd(17, 13)}");     // gcd(17, 13) = 1
  return 0;
}
```

### Prime Checker

```
fn is_prime(n: int) -> bool {
  if n < 2 { return false; }
  if n < 4 { return true; }
  if (n % 2) == 0 { return false; }

  i := 3;
  while (i * i) <= n {
    if (n % i) == 0 {
      return false;
    }
    i = i + 2;
  }
  return true;
}

fn main() -> int {
  println("Primes up to 50:");
  for n in 2..51 {
    if is_prime(n) {
      print_string(f"{n} ");
    }
  }
  println("");  // 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
  return 0;
}
```

### Command Dispatcher with Match

```
fn handle_command(cmd: string) -> string {
  return match cmd {
    "help" => "Available commands: help, version, quit",
    "version" => "Mog v1.0.0",
    "quit" => "Goodbye!",
    _ => f"Unknown command: {cmd}",
  };
}

fn main() -> int {
  commands := ["help", "version", "status", "quit"];
  for cmd in commands {
    println(f"> {cmd}");
    println(f"  {handle_command(cmd)}");
  }
  return 0;
}
```

Summary
-------

| Construct | Syntax | Notes |
| --- | --- | --- |
| If/else | `if cond { } else { }` | Braces required, parens optional |
| If expression | `x := if cond { a } else { b };` | Returns last value of each branch |
| While | `while cond { }` | Loop until condition is false |
| For-to | `for i := 1 to 10 { }` | Inclusive upper bound |
| For-in range | `for i in 0..10 { }` | Exclusive upper bound |
| For-in array | `for item in arr { }` | Iterates values |
| For-in indexed | `for i, item in arr { }` | Iterates index-value pairs |
| For-in map | `for key, val in map { }` | Iterates key-value pairs |
| Break | `break;` | Exits innermost loop |
| Continue | `continue;` | Skips to next iteration |
| Match | `match val { pat => expr, }` | Comma-separated arms, `_` wildcard |
| Match expression | `x := match val { ... };` | Returns value from matched arm |



Chapter 5: Functions
====================

Functions are the primary building blocks of any Mog program. They group reusable logic behind a name, accept typed parameters, and can return values. This chapter covers everything from basic declarations to recursion and the built-in functions that ship with every Mog program.

Basic Function Declarations
---------------------------

A function starts with the `fn` keyword, followed by a name, a parameter list with type annotations, an optional return type after `->`, and a body in curly braces:

```
fn add(a: int, b: int) -> int {
  return a + b;
}

fn multiply(x: float, y: float) -> float {
  return x * y;
}

fn is_even(n: int) -> bool {
  return (n % 2) == 0;
}
```

Every function that produces a value must use an explicit `return` statement. Mog does not support implicit returns — the last expression in a function body is not automatically returned. This keeps control flow unambiguous.

```
// WRONG — this compiles but returns void, discarding the result
fn broken_add(a: int, b: int) -> int {
  a + b;
}

// CORRECT
fn working_add(a: int, b: int) -> int {
  return a + b;
}
```

> **Always use `return`.** Unlike some languages where the last expression is the return value, Mog requires you to be explicit. This avoids subtle bugs when refactoring.

Multiple return points are fine when the logic calls for it:

```
fn classify_temperature(celsius: float) -> string {
  if celsius < 0.0 {
    return "freezing";
  }
  if celsius < 20.0 {
    return "cold";
  }
  if celsius < 35.0 {
    return "warm";
  }
  return "hot";
}
```

Void Functions
--------------

When a function performs an action but doesn’t produce a value, omit the `-> Type` annotation. The function implicitly returns void:

```
fn log_message(level: string, message: string) {
  println(f"[{level}] {message}");
}

fn swap(arr: [int], i: int, j: int) {
  temp := arr[i];
  arr[i] = arr[j];
  arr[j] = temp;
}

fn print_separator(width: int) {
  line := "";
  for _ in 0..width {
    line = line + "-";
  }
  println(line);
}
```

A void function can still use `return;` to exit early:

```
fn print_if_positive(n: int) {
  if n <= 0 {
    return;
  }
  println(n);
}
```

Parameters and Return Types
---------------------------

Parameters are declared with `name: Type` syntax. Every parameter must have a type annotation — Mog does not infer parameter types (see Chapter 2 for why type annotations are required on function signatures).

```
fn format_price(amount: float, currency: string) -> string {
  return f"{currency} {amount}";
}

fn clamp(value: int, low: int, high: int) -> int {
  if value < low {
    return low;
  }
  if value > high {
    return high;
  }
  return value;
}
```

Functions can accept and return composite types — arrays, maps, and structs:

```
fn sum(numbers: [int]) -> int {
  total := 0;
  for n in numbers {
    total = total + n;
  }
  return total;
}

fn zip_names_ages(names: [string], ages: [int]) -> [{name: string, age: int}] {
  result: [{name: string, age: int}] = [];
  for i in 0..names.len {
    result.push({name: names[i], age: ages[i]});
  }
  return result;
}
```

Named Arguments and Default Values
----------------------------------

Functions can declare default values for parameters. Callers may then omit those arguments or pass them by name in any order:

```
fn greet(name: string, greeting: string = "Hello") -> string {
  return f"{greeting}, {name}!";
}

// All of these work:
greet("Alice");                        // "Hello, Alice!"
greet("Bob", "Hey");                   // "Hey, Bob!"
greet(name: "Charlie");                // "Hello, Charlie!"
greet(name: "Dave", greeting: "Hi");   // "Hi, Dave!"
greet(greeting: "Howdy", name: "Eve"); // "Howdy, Eve!"
```

Named arguments are especially useful when a function has several optional parameters:

```
fn create_server(
  host: string = "localhost",
  port: int = 8080,
  max_connections: int = 100,
  timeout_ms: int = 30000,
) {
  println(f"Starting server on {host}:{port}");
  println(f"Max connections: {max_connections}");
  println(f"Timeout: {timeout_ms}ms");
}

// Only override what you need:
create_server();                                // all defaults
create_server(port: 3000);                      // just change port
create_server(host: "0.0.0.0", port: 443);     // host and port
create_server(timeout_ms: 60000, port: 9090);   // any order
```

A practical example — building a configurable search:

```
fn search(
  query: string,
  max_results: int = 10,
  case_sensitive: bool = false,
  sort_by: string = "relevance",
) -> [string] {
  println(f"Searching for '{query}' (max={max_results}, case={case_sensitive}, sort={sort_by})");
  results: [string] = [];
  return results;
}

fn main() -> int {
  search("mog language");
  search("mog language", max_results: 50, sort_by: "date");
  search(query: "Functions", case_sensitive: true);
  return 0;
}
```

Calling Conventions
-------------------

Mog supports both positional and named calling styles. You can mix them, but positional arguments must come before named arguments:

```
fn send_email(to: string, subject: string, body: string = "", urgent: bool = false) {
  println(f"To: {to}");
  println(f"Subject: {subject}");
  if urgent {
    println("[URGENT]");
  }
  if body != "" {
    println(body);
  }
}

// Positional
send_email("alice@example.com", "Meeting", "See you at 3pm", true);

// Named
send_email(to: "bob@example.com", subject: "Lunch?");

// Mixed: positional first, then named
send_email("carol@example.com", "Report", urgent: true);
```

> **Rule of thumb:** Use positional args for 1-2 required parameters. Use named args when a function has 3+ parameters or when the call site would otherwise be ambiguous.

Recursion
---------

Functions can call themselves. Mog does not guarantee tail-call optimization, so deep recursion will consume stack space proportional to the call depth.

**Factorial:**

```
fn factorial(n: int) -> int {
  if n <= 1 {
    return 1;
  }
  return n * factorial(n - 1);
}

fn main() -> int {
  println(factorial(5));   // 120
  println(factorial(10));  // 3628800
  return 0;
}
```

**Fibonacci:**

```
fn fibonacci(n: int) -> int {
  if n <= 0 {
    return 0;
  }
  if n == 1 {
    return 1;
  }
  return fibonacci(n - 1) + fibonacci(n - 2);
}

fn main() -> int {
  for i in 0..10 {
    println(fibonacci(i));
  }
  // 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
  return 0;
}
```

**Binary search — recursion with arrays:**

```
fn binary_search(arr: [int], target: int, low: int, high: int) -> int {
  if low > high {
    return -1;
  }
  mid := (low + high) / 2;
  if arr[mid] == target {
    return mid;
  }
  if arr[mid] < target {
    return binary_search(arr, target, mid + 1, high);
  }
  return binary_search(arr, target, low, mid - 1);
}

fn main() -> int {
  data := [2, 5, 8, 12, 16, 23, 38, 56, 72, 91];
  idx := binary_search(data, 23, 0, data.len - 1);
  println(f"Found 23 at index {idx}");  // Found 23 at index 5
  return 0;
}
```

**Greatest common divisor:**

```
fn gcd(a: int, b: int) -> int {
  if b == 0 {
    return a;
  }
  return gcd(b, a % b);
}

fn main() -> int {
  println(gcd(48, 18));   // 6
  println(gcd(100, 75));  // 25
  return 0;
}
```

> **Tip:** For deep or performance-sensitive recursion, consider rewriting with a loop (see Chapter 4). The recursive Fibonacci above is O(2^n) — the iterative version is O(n):

```
// Iterative fibonacci — much faster for large n
fn fibonacci_fast(n: int) -> int {
  if n <= 0 {
    return 0;
  }
  a := 0;
  b := 1;
  for _ in 1..n {
    temp := b;
    b = a + b;
    a = temp;
  }
  return b;
}
```

Math Builtins
-------------

Mog provides a set of math functions as builtins. No imports required. All math builtins operate on `float` (f64) values.

**Single-argument functions:**

| Function | Description |
| --- | --- |
| `sqrt(x)` | Square root |
| `sin(x)` | Sine (radians) |
| `cos(x)` | Cosine (radians) |
| `tan(x)` | Tangent (radians) |
| `asin(x)` | Arcsine |
| `acos(x)` | Arccosine |
| `exp(x)` | e^x |
| `log(x)` | Natural logarithm |
| `log2(x)` | Base-2 logarithm |
| `floor(x)` | Round down |
| `ceil(x)` | Round up |
| `round(x)` | Round to nearest |
| `abs(x)` | Absolute value |

**Two-argument functions:**

| Function | Description |
| --- | --- |
| `pow(x, y)` | x raised to the power y |
| `atan2(y, x)` | Two-argument arctangent |
| `min(a, b)` | Smaller of two values |
| `max(a, b)` | Larger of two values |

> All math builtins take and return `float`. If you have an `int`, cast it first with `as float` (see Chapter 3).

Examples:

```
// Distance between two points
fn distance(x1: float, y1: float, x2: float, y2: float) -> float {
  dx := x2 - x1;
  dy := y2 - y1;
  return sqrt((dx * dx) + (dy * dy));
}

fn main() -> int {
  println(distance(0.0, 0.0, 3.0, 4.0));  // 5.0
  return 0;
}
```

```
// Convert degrees to radians and compute trig values
fn deg_to_rad(degrees: float) -> float {
  return (degrees * 3.14159265) / 180.0;
}

fn main() -> int {
  angle := deg_to_rad(45.0);
  println(sin(angle));   // ~0.7071
  println(cos(angle));   // ~0.7071
  return 0;
}
```

```
// Compound interest
fn compound_interest(principal: float, rate: float, years: int) -> float {
  return principal * pow(1.0 + rate, years as float);
}

fn main() -> int {
  result := compound_interest(1000.0, 0.05, 10);
  println(round(result));  // 1629.0
  return 0;
}
```

```
// Clamp a float between bounds
fn clamp_float(value: float, lo: float, hi: float) -> float {
  return max(lo, min(hi, value));
}

fn main() -> int {
  println(clamp_float(150.0, 0.0, 100.0));  // 100.0
  println(clamp_float(-5.0, 0.0, 100.0));   // 0.0
  return 0;
}
```

```
// Estimate how many bits are needed to represent n
fn bits_needed(n: int) -> int {
  if n <= 0 {
    return 1;
  }
  return floor(log2(n as float)) as int + 1;
}

fn main() -> int {
  println(bits_needed(255));   // 8
  println(bits_needed(256));   // 9
  return 0;
}
```

Other Builtins
--------------

Mog provides several non-math builtins that are available without imports.

### Output Functions

```
fn main() -> int {
  // println auto-dispatches by type
  println(42);           // prints "42\n"
  println(3.14);         // prints "3.14\n"
  println("hello");      // prints "hello\n"
  println(true);         // prints "true\n"

  // Type-specific print (no newline)
  print_string("name: ");
  print_i64(42);
  print_f64(3.14);
  return 0;
}
```

### Conversion Functions

**`str(value)`** — Convert an int, float, or bool to a string:

```
s1 := str(42);       // "42"
s2 := str(3.14);     // "3.14"
s3 := str(true);     // "true"

println("The answer is " + str(42));
```

**`len(array)`** — Get the length of an array as an int:

```
numbers := [10, 20, 30, 40];
println(len(numbers));  // 4

empty: [string] = [];
println(len(empty));    // 0
```

**`int_from_string(s)`** — Parse a string into an int. Returns `Result<int>` because the parse can fail (see Chapter 10 for full coverage of Result):

```
result := int_from_string("42");
match result {
  ok(n) => println(f"Parsed: {n}"),
  err(msg) => println(f"Failed: {msg}"),
}

// Using ? to propagate errors
fn read_port(input: string) -> Result<int> {
  port := int_from_string(input)?;
  if (port < 1) || (port > 65535) {
    return err("port out of range");
  }
  return ok(port);
}
```

**`parse_float(s)`** — Parse a string into a float. Returns `Result<float>`:

```
result := parse_float("3.14159");
match result {
  ok(f) => println(f"Got pi: {f}"),
  err(msg) => println(f"Not a float: {msg}"),
}

// Practical use: parsing user input
fn parse_temperature(input: string) -> Result<float> {
  temp := parse_float(input)?;
  if temp < -273.15 {
    return err("below absolute zero");
  }
  return ok(temp);
}
```

### A Complete Example

Combining functions, conversions, and error handling:

```
fn parse_csv_row(line: string) -> Result<{name: string, age: int, score: float}> {
  parts := line.split(",");
  if len(parts) != 3 {
    return err(f"expected 3 fields, got {len(parts)}");
  }
  age := int_from_string(parts[1])?;
  score := parse_float(parts[2])?;
  return ok({name: parts[0], age: age, score: score});
}

fn main() -> int {
  row := parse_csv_row("Alice,30,95.5");
  match row {
    ok(data) => println(f"{data.name} is {str(data.age)} years old with score {str(data.score)}"),
    err(msg) => println(f"Parse error: {msg}"),
  }
  return 0;
}
```

Summary
-------

| Feature | Syntax | Notes |
| --- | --- | --- |
| Declaration | `fn name(p: T) -> R { }` | `fn` keyword, typed params, explicit return type |
| Void function | `fn name(p: T) { }` | Omit `-> R` for side-effect-only functions |
| Return | `return value;` | Required — no implicit returns |
| Default args | `fn f(x: int = 10)` | Caller can omit or pass by name |
| Named call | `f(x: 42, y: 10)` | Named args can be in any order |
| Mixed call | `f(42, y: 10)` | Positional before named |
| Recursion | `fn f(n: int) { f(n-1); }` | No guaranteed tail-call optimization |



Chapter 6: Closures and Higher-Order Functions
==============================================

In the previous chapter, functions were always named and declared at the top level. Mog also supports **closures** — anonymous functions that can be created inline, stored in variables, passed as arguments, and returned from other functions. When combined with higher-order functions (functions that accept or return other functions), closures unlock powerful and concise patterns for working with data.

Closure Syntax
--------------

A closure is an anonymous function written with the `fn` keyword but without a name. It is typically assigned to a variable or passed directly as an argument.

```
add := fn(a: int, b: int) -> int { return a + b; };

print(add(3, 4));  // 7
```

The syntax mirrors named functions: parameters with types, an optional return type, and a body in curly braces. The trailing semicolon is required because the closure assignment is a statement.

```
square := fn(n: int) -> int { return n * n; };
is_positive := fn(x: float) -> bool { return x > 0.0; };
greet := fn(name: string) -> string { return "hello, {name}!"; };

print(square(5));         // 25
print(is_positive(-3.0)); // false
print(greet("Alice"));    // hello, Alice!
```

Closures that take no parameters and return nothing work too:

```
say_hi := fn() { print("hi"); };
say_hi();  // hi
```

Capturing Variables
-------------------

Closures can reference variables from their enclosing scope. This is what distinguishes a closure from a plain function pointer — it “closes over” the environment where it was created.

```
multiplier := 3;
triple := fn(n: int) -> int { return n * multiplier; };

print(triple(10));  // 30
print(triple(7));   // 21
```

Closures can capture multiple variables:

```
base_url := "https://api.example.com";
api_key := "sk-12345";

make_url := fn(endpoint: string) -> string {
  return "{base_url}/{endpoint}?key={api_key}";
};

print(make_url("users"));  // https://api.example.com/users?key=sk-12345
```

### Value Capture Semantics

Mog captures variables **by value** — the closure gets a snapshot of each captured variable at the moment the closure is created. Later changes to the original do not affect the closure’s copy.

```
count := 10;
get_count := fn() -> int { return count; };

count = 20;
print(get_count());  // 10 — captured the value 10
print(count);        // 20 — the original is 20
```

This matters in loops. Each iteration creates a new closure that captures the loop variable’s current value:

```
makers: [fn() -> int] = [];
for i in 0..5 {
  makers.push(fn() -> int { return i; });
}

print(makers[0]());  // 0
print(makers[3]());  // 3
```

> Internally, closures are implemented as a fat pointer: `{fn_ptr, env_ptr}`. The runtime copies only the variables the closure actually references. This is an implementation detail you rarely need to think about.

Type Aliases for Function Types
-------------------------------

Function type signatures can get verbose. Use `type` to create aliases:

```
type Predicate = fn(int) -> bool;
type Transform = fn(int) -> int;
type Callback = fn(string);
```

These aliases simplify function signatures:

```
type Transform = fn(int) -> int;

fn apply_twice(f: Transform, value: int) -> int {
  return f(f(value));
}

double := fn(n: int) -> int { return n * 2; };
print(apply_twice(double, 3));  // 12
```

Without the alias, the signature would be `fn apply_twice(f: fn(int) -> int, value: int) -> int` — correct but harder to read at a glance.

```
type Predicate = fn(int) -> bool;
type Formatter = fn(int) -> string;

fn find_first(items: [int], pred: Predicate) -> ?int {
  for item in items {
    if pred(item) { return some(item); }
  }
  return none;
}

fn format_all(items: [int], fmt: Formatter) -> [string] {
  return items.map(fmt);
}
```

Passing Closures to Functions
-----------------------------

Closures are first-class values. You can pass them as arguments using the function type syntax `fn(ParamTypes) -> ReturnType`.

```
fn apply(f: fn(int) -> int, x: int) -> int {
  return f(x);
}

double := fn(n: int) -> int { return n * 2; };
negate := fn(n: int) -> int { return -n; };

print(apply(double, 5));   // 10
print(apply(negate, 5));   // -5
```

You can pass closures inline without naming them:

```
print(apply(fn(n: int) -> int { return n * n; }, 4));  // 16
```

A function that transforms every element of an array:

```
fn transform(arr: [int], f: fn(int) -> int) -> [int] {
  result: [int] = [];
  for item in arr {
    result.push(f(item));
  }
  return result;
}

numbers := [1, 2, 3, 4, 5];

doubled := transform(numbers, fn(n: int) -> int { return n * 2; });
print(doubled);  // [2, 4, 6, 8, 10]

offset := 100;
shifted := transform(numbers, fn(n: int) -> int { return n + offset; });
print(shifted);  // [101, 102, 103, 104, 105]
```

Returning Closures from Functions
---------------------------------

Functions can create and return closures. The returned closure retains access to any variables it captured — even after the enclosing function has returned.

```
fn make_adder(n: int) -> fn(int) -> int {
  return fn(x: int) -> int { return x + n; };
}

add5 := make_adder(5);
add100 := make_adder(100);

print(add5(3));    // 8
print(add100(3));  // 103
```

```
fn make_multiplier(factor: float) -> fn(float) -> float {
  return fn(x: float) -> float { return x * factor; };
}

to_km := make_multiplier(1.60934);
print(to_km(10.0));  // 16.0934
```

This factory pattern is useful for creating families of related functions from a single template. You will see it again in Chapter 8 when we build constructor functions for structs.

Closures with Array Methods
---------------------------

Mog arrays have built-in methods — `filter`, `map`, and `sort` — that accept closures. These methods return new arrays; they do not modify the original. See Chapter 9 for the full set of collection operations.

### filter

`filter` takes a predicate closure and returns a new array containing only the elements for which the predicate returns `true`.

```
numbers := [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

evens := numbers.filter(fn(n: int) -> bool { return (n % 2) == 0; });
print(evens);  // [2, 4, 6, 8, 10]

big := numbers.filter(fn(n: int) -> bool { return n > 7; });
print(big);  // [8, 9, 10]
```

Filter with a captured threshold:

```
scores := [45, 72, 88, 91, 53, 67, 79, 95];
cutoff := 70;

passing := scores.filter(fn(s: int) -> bool { return s >= cutoff; });
print(passing);  // [72, 88, 91, 79, 95]
```

### map

`map` takes a transform closure and returns a new array with each element replaced by the closure’s result.

```
numbers := [1, 2, 3, 4, 5];

doubled := numbers.map(fn(n: int) -> int { return n * 2; });
print(doubled);  // [2, 4, 6, 8, 10]

labels := numbers.map(fn(n: int) -> string { return "item-{str(n)}"; });
print(labels);  // ["item-1", "item-2", "item-3", "item-4", "item-5"]
```

```
names := ["alice", "bob", "carol"];
lengths := names.map(fn(name: string) -> int { return name.len; });
print(lengths);  // [5, 3, 5]
```

### sort

`sort` takes a comparator closure that returns `true` when the first argument should come before the second. It returns a new sorted array.

```
numbers := [5, 2, 8, 1, 9, 3];

ascending := numbers.sort(fn(a: int, b: int) -> bool { return a < b; });
print(ascending);  // [1, 2, 3, 5, 8, 9]

descending := numbers.sort(fn(a: int, b: int) -> bool { return a > b; });
print(descending);  // [9, 8, 5, 3, 2, 1]
```

Sorting structs by a specific field:

```
struct Player {
  name: string,
  score: int,
}

players := [
  Player{name: "Alice", score: 250},
  Player{name: "Bob", score: 180},
  Player{name: "Carol", score: 320},
];

by_score := players.sort(fn(a: Player, b: Player) -> bool {
  return a.score > b.score;
});

for p in by_score {
  print("{p.name}: {str(p.score)}");
}
// Carol: 320
// Alice: 250
// Bob: 180
```

### Chaining Methods

Filter, map, and sort can be chained for expressive data pipelines:

```
numbers := [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

result := numbers
  .filter(fn(n: int) -> bool { return (n % 2) == 0; })
  .map(fn(n: int) -> int { return n * n; })
  .sort(fn(a: int, b: int) -> bool { return a > b; });

print(result);  // [100, 64, 36, 16, 4]
```

> Method chaining reads top-to-bottom: filter the evens, square them, sort descending. Each step returns a new array, so the original `numbers` is untouched.

Summary
-------

| Concept | Syntax |
| --- | --- |
| Create a closure | `fn(params) -> Type { body }` |
| Type alias | `type Name = fn(ParamTypes) -> ReturnType;` |
| Pass to function | `fn do_it(f: fn(int) -> int) { ... }` |
| Return from function | `fn make() -> fn(int) -> int { ... }` |
| Filter an array | `arr.filter(fn(x: T) -> bool { ... })` |
| Map an array | `arr.map(fn(x: T) -> U { ... })` |
| Sort an array | `arr.sort(fn(a: T, b: T) -> bool { ... })` |

Closures capture by value, are first-class values, and combine naturally with array methods for concise data processing. In the next chapter, we will look at Mog’s string type in detail.



Chapter 7: Strings
==================

Strings are one of the most frequently used types in any language. Mog strings are immutable, UTF-8 encoded, and garbage-collected — you create them, pass them around, and the runtime handles the rest. This chapter covers everything from basic literals and escape sequences to interpolation, methods, and parsing.

String Basics
-------------

Mog strings use double quotes only. There are no single-quoted strings, no raw strings, and no heredocs. A string literal is a sequence of bytes between `"` and `"`, encoded as UTF-8 and null-terminated internally.

```
fn main() -> int {
  greeting := "Hello, world!";
  println(greeting);

  empty := "";
  println(empty);  // prints an empty line

  return 0;
}
```

### Escape Sequences

Mog supports the standard escape sequences you’d expect:

| Escape | Meaning |
| --- | --- |
| `\n` | Newline |
| `\t` | Tab |
| `\\` | Literal backslash |
| `\"` | Literal double quote |

```
fn main() -> int {
  multiline := "Line 1\nLine 2\nLine 3";
  println(multiline);
  // Line 1
  // Line 2
  // Line 3

  tabbed := "Name:\tAlice\nAge:\t30";
  println(tabbed);
  // Name:	Alice
  // Age:	30

  path := "C:\\Users\\alice\\docs";
  println(path);  // C:\Users\alice\docs

  quoted := "She said \"hello\" and left.";
  println(quoted);  // She said "hello" and left.

  return 0;
}
```

### Immutability

Strings in Mog are immutable reference types. You can rebind a variable to a new string, but you cannot modify a string’s contents in place. Every operation that “changes” a string — concatenation, `upper()`, `replace()` — returns a new string.

```
fn main() -> int {
  s := "hello";
  s = s.upper();  // rebinds s to a new string "HELLO"
  println(s);     // HELLO

  return 0;
}
```

### UTF-8 Encoding

Mog strings are UTF-8 encoded, so they handle international text and emoji naturally. Keep in mind that `.len` returns the **byte count**, not the number of characters — multibyte characters take more than one byte.

```
fn main() -> int {
  cafe := "café au lait";
  println(cafe);

  emoji := "Hello! 👍";
  println(emoji);

  chinese := "你好世界";
  println(chinese);

  japanese := "こんにちは";
  println(japanese);

  // Byte lengths — not character counts
  ascii := "hello";
  println(ascii.len);    // 5 — one byte per character

  return 0;
}
```

String Interpolation
--------------------

Mog supports f-strings — string literals prefixed with `f` that can embed expressions inside `{}` braces. This is the most readable way to build strings from mixed data.

```
fn main() -> int {
  name := "Alice";
  age := 30;
  println(f"Hello, {name}!");              // Hello, Alice!
  println(f"You are {age} years old.");    // You are 30 years old.

  return 0;
}
```

Expressions inside `{}` can be arithmetic, function calls, or any expression that produces a value. The result is automatically converted to a string.

```
fn main() -> int {
  age := 30;
  println(f"Next year you'll be {age + 1}.");  // Next year you'll be 31.

  x := 7;
  println(f"{x} squared is {x * x}.");  // 7 squared is 49.

  price := 9.99;
  qty := 3;
  println(f"Total: {price * 3.0}");  // Total: 29.970000

  return 0;
}
```

You can have multiple interpolations in a single string, and they can appear anywhere — at the start, middle, or end.

```
fn main() -> int {
  a := 10;
  b := 20;
  println(f"{a} + {b} = {a + b}");  // 10 + 20 = 30

  name := "World";
  println(f"[{name}]");  // [World]

  return 0;
}
```

If you need a literal `{` or `}` in an f-string, escape it by doubling: `{{` and `}}`.

```
fn main() -> int {
  x := 42;
  println(f"The value is: {x} (in braces: {{{x}}})");
  // The value is: 42 (in braces: {42})

  return 0;
}
```

String Concatenation
--------------------

The `+` operator joins two strings together, returning a new string. You can chain multiple `+` operations.

```
fn main() -> int {
  first := "Hello";
  second := " World";
  result := first + second;
  println(result);  // Hello World

  full := "one" + " " + "two" + " " + "three";
  println(full);  // one two three

  return 0;
}
```

To concatenate a non-string value, convert it first with `str()`.

```
fn main() -> int {
  count := 42;
  msg := "Count: " + str(count);
  println(msg);  // Count: 42

  pi := 3.14;
  info := "Pi is approximately " + str(pi);
  println(info);  // Pi is approximately 3.140000

  return 0;
}
```

For most cases, f-strings are cleaner than manual concatenation — they handle the conversion automatically and are easier to read.

```
fn main() -> int {
  name := "Alice";
  score := 95;

  // Concatenation — works, but verbose
  msg1 := name + " scored " + str(score) + " points.";

  // F-string — same result, easier to read
  msg2 := f"{name} scored {score} points.";

  println(msg1);  // Alice scored 95 points.
  println(msg2);  // Alice scored 95 points.

  return 0;
}
```

String Methods
--------------

Mog strings have built-in methods for common operations. These are called with dot syntax on any string value.

### `.len`

Returns the byte length of the string. This is a property, not a function call.

```
fn main() -> int {
  s := "hello";
  println(s.len);  // 5

  empty := "";
  println(empty.len);  // 0

  // Multibyte characters take more than one byte
  accent := "café";
  println(accent.len);  // 5 — the é is 2 bytes

  return 0;
}
```

### `.contains(substr)`

Returns true if the string contains the given substring.

```
fn main() -> int {
  s := "hello world";

  if s.contains("world") {
    println("Found 'world'");
  }

  if s.contains("xyz") == false {
    println("No 'xyz' here");
  }

  // Case-sensitive
  if s.contains("Hello") == false {
    println("'Hello' not found — case matters");
  }

  return 0;
}
```

### `.starts_with(prefix)` and `.ends_with(suffix)`

Check whether a string begins or ends with a given substring.

```
fn main() -> int {
  path := "/usr/local/bin/mog";

  if path.starts_with("/usr") {
    println("System path");  // prints
  }

  if path.ends_with(".mog") == false {
    println("Not a .mog file");  // prints
  }

  filename := "report.csv";
  if filename.ends_with(".csv") {
    println("CSV file detected");  // prints
  }

  return 0;
}
```

### `.upper()` and `.lower()`

Return a new string with all ASCII characters converted to uppercase or lowercase.

```
fn main() -> int {
  s := "Hello World";
  println(s.upper());  // HELLO WORLD
  println(s.lower());  // hello world
  println(s);          // Hello World — original unchanged

  // Useful for case-insensitive comparison
  input := "Yes";
  if input.lower() == "yes" {
    println("Confirmed");
  }

  return 0;
}
```

### `.trim()`

Returns a new string with leading and trailing whitespace removed.

```
fn main() -> int {
  raw := "  hello  ";
  cleaned := raw.trim();
  println(cleaned);       // hello
  println(cleaned.len);   // 5

  padded := "\t spaced \n";
  println(padded.trim());  // spaced

  return 0;
}
```

### `.replace(old, new)`

Returns a new string with all occurrences of `old` replaced by `new`.

```
fn main() -> int {
  s := "hello world";
  println(s.replace("world", "Mog"));  // hello Mog

  csv := "a,b,c,d";
  println(csv.replace(",", " | "));  // a | b | c | d

  // Replaces all occurrences, not just the first
  repeated := "aaa";
  println(repeated.replace("a", "bb"));  // bbbbbb

  return 0;
}
```

### `.split(delimiter)`

Splits a string into an array of substrings at each occurrence of the delimiter.

```
fn main() -> int {
  csv := "alice,bob,carol";
  parts := csv.split(",");

  for i, name in parts {
    println(f"{i}: {name}");
  }
  // 0: alice
  // 1: bob
  // 2: carol

  return 0;
}
```

### `.index_of(substr)`

Returns the byte offset of the first occurrence of `substr`, or -1 if not found.

```
fn main() -> int {
  s := "hello world";
  println(s.index_of("world"));  // 6
  println(s.index_of("xyz"));    // -1

  return 0;
}
```

### Method Chaining

String methods return new strings, so you can chain them.

```
fn main() -> int {
  raw := "  Hello, World!  ";
  result := raw.trim().lower().replace("world", "mog");
  println(result);  // hello, mog!

  return 0;
}
```

String Slicing
--------------

You can extract a substring using bracket syntax with a range: `s[start:end]`. Both `start` and `end` are byte offsets. The slice includes `start` and excludes `end`.

```
fn main() -> int {
  s := "hello world";
  println(s[0:5]);   // hello
  println(s[6:11]);  // world

  // Single character access
  println(s[0]);  // h
  println(s[4]);  // o

  // Using variables
  start := 6;
  end := 11;
  println(s[start:end]);  // world

  return 0;
}
```

String Comparison
-----------------

Use `==` and `!=` to compare string contents. These compare the actual bytes, not pointer identity.

```
fn main() -> int {
  a := "hello";
  b := "hello";
  c := "world";

  if a == b {
    println("a and b are equal");  // prints
  }

  if a != c {
    println("a and c are different");  // prints
  }

  return 0;
}
```

Comparisons are case-sensitive. Use `.lower()` or `.upper()` if you need case-insensitive matching.

```
fn main() -> int {
  input := "YES";
  expected := "yes";

  if input == expected {
    println("exact match");
  }

  if input.lower() == expected {
    println("case-insensitive match");  // prints
  }

  return 0;
}
```

Conversions
-----------

### To String: `str()`

The `str()` function converts integers and floats to their string representation.

```
fn main() -> int {
  s1 := str(42);
  println(s1);  // 42

  s2 := str(-7);
  println(s2);  // -7

  s3 := str(3.14);
  println(s3);  // 3.140000

  // Useful for concatenation
  label := "Score: " + str(100);
  println(label);  // Score: 100

  return 0;
}
```

### From String: Parsing

Mog provides two sets of parsing functions with different error-handling strategies.

**Safe parsing** — `int_from_string()` and `float_from_string()` return a `Result` type that you can match on for error handling (see Chapter 10 for details on Result types):

```
fn main() -> int {
  r := int_from_string("42");
  // r is a Result<int> — use match to handle success or failure

  return 0;
}
```

**Simple parsing** — `parse_int()` and `parse_float()` return the value directly, giving 0 or 0.0 on failure:

```
fn main() -> int {
  n := parse_int("123");
  println(n);  // 123

  f := parse_float("3.14");
  println(f);  // 3.140000

  // Invalid input returns 0
  bad := parse_int("abc");
  println(bad);  // 0

  return 0;
}
```

Use `parse_int` and `parse_float` when you trust the input or have already validated it. Use `int_from_string` and `float_from_string` when you need to handle errors explicitly.

Print Functions
---------------

Mog provides generic `print` and `println` functions that automatically dispatch based on the argument type. There are also type-specific variants when you need precise control.

### Generic Printing

`println()` detects the argument type and calls the appropriate variant:

```
fn main() -> int {
  println("hello");   // dispatches to println_string
  println(42);        // dispatches to println_i64
  println(3.14);      // dispatches to println_f64

  return 0;
}
```

### Type-Specific Variants

These print without a trailing newline, which is useful for building output piece by piece:

| Function | Description |
| --- | --- |
| `print_string(s)` | Print a string, no newline |
| `print_i64(n)` | Print an integer, no newline |
| `print_f64(f)` | Print a float, no newline |
| `println_string(s)` | Print a string with newline |
| `println_i64(n)` | Print an integer with newline |
| `println_f64(f)` | Print a float with newline |

```
fn main() -> int {
  print_string("Loading");
  print_string(".");
  print_string(".");
  print_string(".");
  println_string(" done!");
  // Loading... done!

  print_string("Value: ");
  print_i64(42);
  print_string("\n");
  // Value: 42

  return 0;
}
```

Building Strings
----------------

### Concatenation in Loops

You can build a string incrementally by concatenating in a loop. Since strings are immutable, each `+` creates a new string.

```
fn main() -> int {
  arr := [1, 2, 3, 4, 5];
  result := "";
  for i, v in arr {
    if i > 0 {
      result = result + ", ";
    }
    result = result + str(v);
  }
  println(result);  // 1, 2, 3, 4, 5

  return 0;
}
```

### Formatting Tables

F-strings and concatenation let you format aligned output:

```
fn main() -> int {
  println("Name          Score");
  println("----          -----");
  println(f"Alice         {95}");
  println(f"Bob           {87}");
  println(f"Carol         {92}");

  return 0;
}
```

### Building Messages

F-strings shine when assembling messages with mixed data:

```
fn main() -> int {
  user := "alice";
  action := "login";
  code := 200;

  log_msg := f"[{code}] User '{user}' performed '{action}'";
  println(log_msg);
  // [200] User 'alice' performed 'login'

  items := 3;
  total := 29.97;
  receipt := f"You purchased {items} items for a total of {total}";
  println(receipt);

  return 0;
}
```

### Parsing with Validation

A common pattern is parsing user input and handling the case where it might not be valid:

```
fn main() -> int {
  inputs := ["42", "hello", "100", "3.14"];

  for i, s in inputs {
    n := parse_int(s);
    if n != 0 {
      println(f"Parsed '{s}' as {n}");
    } else {
      if s == "0" {
        println(f"Parsed '{s}' as 0");
      } else {
        println(f"Could not parse '{s}'");
      }
    }
  }

  return 0;
}
```

Summary
-------

| Operation | Syntax | Returns |
| --- | --- | --- |
| Create string | `"hello"` | `string` |
| Interpolation | `f"value is {x}"` | `string` |
| Concatenation | `a + b` | `string` |
| Byte length | `s.len` | `int` |
| Contains | `s.contains("x")` | `bool` |
| Starts with | `s.starts_with("x")` | `bool` |
| Ends with | `s.ends_with("x")` | `bool` |
| Uppercase | `s.upper()` | `string` |
| Lowercase | `s.lower()` | `string` |
| Trim whitespace | `s.trim()` | `string` |
| Replace | `s.replace("a", "b")` | `string` |
| Split | `s.split(",")` | `[string]` |
| Index of | `s.index_of("x")` | `int` |
| Slice | `s[0:5]` | `string` |
| Char at | `s[0]` | `string` |
| To string | `str(42)` | `string` |
| Parse int (safe) | `int_from_string("42")` | `Result<int>` |
| Parse float (safe) | `float_from_string("3.14")` | `Result<float>` |
| Parse int (simple) | `parse_int("42")` | `int` |
| Parse float (simple) | `parse_float("3.14")` | `float` |
| Equality | `a == b`, `a != b` | `bool` |

Strings are straightforward in Mog — double-quoted, immutable, UTF-8, and garbage-collected. For error handling with `int_from_string` and `float_from_string`, see Chapter 10 on Result types.



Chapter 8: Structs
==================

Structs are Mog’s way of grouping related data under a single name. They are simple named product types with typed fields — no methods, no inheritance, no interfaces. You define the shape, construct instances, and pass them around. Functions that operate on structs live outside the struct as standalone functions.

Declaring Structs
-----------------

A struct declaration lists named fields with their types, separated by commas:

```
struct Point {
  x: int,
  y: int,
}
```

Fields can be any type — scalars, strings, arrays, maps, or other structs:

```
struct Color {
  r: int,
  g: int,
  b: int,
  a: float,
}

struct Config {
  name: string,
  version: int,
  debug: bool,
  tags: [string],
}

struct User {
  id: int,
  username: string,
  email: string,
  active: bool,
}
```

Structs are always declared at the top level. They cannot be declared inside functions or other structs.

Constructing Instances
----------------------

Create a struct instance by naming the type and providing values for all fields inside braces:

```
fn main() {
  p := Point { x: 10, y: 20 };
  c := Color { r: 255, g: 128, b: 0, a: 1.0 };
  cfg := Config { name: "myapp", version: 3, debug: false, tags: ["prod", "v3"] };
}
```

Every field must be provided. There are no default values and no partial construction — if a struct has four fields, you supply four values:

```
fn main() {
  // This is a compile error — missing field `a`:
  // c := Color { r: 255, g: 128, b: 0 };

  // All fields required:
  c := Color { r: 255, g: 128, b: 0, a: 1.0 };
}
```

You can use expressions as field values, not just literals:

```
fn main() {
  base := 100;
  p := Point { x: base * 2, y: base + 50 };
  print(p.x);  // 200
  print(p.y);  // 150
}
```

Field Access
------------

Access individual fields with dot notation:

```
fn main() {
  p := Point { x: 10, y: 20 };
  print(p.x);  // 10
  print(p.y);  // 20

  c := Color { r: 255, g: 128, b: 0, a: 1.0 };
  print(c.r);  // 255
  print(c.a);  // 1.0
}
```

Fields work anywhere an expression of that type is expected:

```
fn main() {
  p := Point { x: 3, y: 4 };
  distance_squared := (p.x * p.x) + (p.y * p.y);
  print(distance_squared);  // 25
}
```

Field Mutation
--------------

Struct fields are mutable. Assign to them with `=`:

```
fn main() {
  p := Point { x: 10, y: 20 };
  print(p.x);  // 10

  p.x = 30;
  print(p.x);  // 30

  p.y = p.y + 5;
  print(p.y);  // 25
}
```

You can mutate any field at any time:

```
fn main() {
  user := User { id: 1, username: "alice", email: "alice@example.com", active: true };
  print(user.active);  // true

  user.active = false;
  user.email = "alice@newdomain.com";
  print(user.active);  // false
  print(user.email);   // alice@newdomain.com
}
```

Passing Structs to Functions
----------------------------

Structs are heap-allocated and passed by reference. When you pass a struct to a function, the function receives a pointer to the same data. Modifications inside the function affect the original:

```
fn move_right(p: Point, amount: int) {
  p.x = p.x + amount;
}

fn main() {
  p := Point { x: 0, y: 0 };
  move_right(p, 10);
  print(p.x);  // 10 — the original was modified
}
```

> This is different from closures, which capture variables by value (see Chapter 6). Structs are always passed by reference — there is no copy-on-pass.

Functions can read struct fields without modifying them:

```
struct Rect {
  width: int,
  height: int,
}

fn area(r: Rect) -> int {
  return r.width * r.height;
}

fn main() {
  r := Rect { width: 10, height: 5 };
  print(area(r));  // 50
}
```

Returning structs from functions works naturally — you return a reference to a heap-allocated struct:

```
fn make_point(x: int, y: int) -> Point {
  return Point { x: x, y: y };
}

fn main() {
  p := make_point(3, 7);
  print(p.x);  // 3
  print(p.y);  // 7
}
```

No Methods — Use Standalone Functions
-------------------------------------

Mog structs have no methods. Instead, write standalone functions that take the struct as a parameter. This keeps data and behavior separate:

```
struct Vec2 {
  x: int,
  y: int,
}

fn vec2_add(a: Vec2, b: Vec2) -> Vec2 {
  return Vec2 { x: a.x + b.x, y: a.y + b.y };
}

fn vec2_dot(a: Vec2, b: Vec2) -> int {
  return (a.x * b.x) + (a.y * b.y);
}

fn vec2_to_string(v: Vec2) -> string {
  return "({v.x}, {v.y})";
}

fn main() {
  a := Vec2 { x: 1, y: 2 };
  b := Vec2 { x: 3, y: 4 };

  sum := vec2_add(a, b);
  print(vec2_to_string(sum));  // (4, 6)
  print(vec2_dot(a, b));       // 11
}
```

> A common convention is to prefix function names with the struct name: `point_distance`, `color_mix`, `user_validate`. This makes it clear which type the function operates on.

Constructor Functions
---------------------

Since there are no constructors or default values, a common pattern is to write factory functions that return pre-configured struct instances:

```
fn new_user(name: string, email: string) -> User {
  return User { id: 0, username: name, email: email, active: true };
}

fn main() {
  u := new_user("alice", "alice@example.com");
  print(u.username);  // alice
  print(u.active);    // true
}
```

```
struct DatabaseConfig {
  host: string,
  port: int,
  name: string,
}

fn default_db_config() -> DatabaseConfig {
  return DatabaseConfig { host: "localhost", port: 5432, name: "appdb" };
}

fn main() {
  cfg := default_db_config();
  cfg.name = "testdb";
  print(cfg.host);  // localhost
  print(cfg.name);  // testdb
}
```

This pattern gives you the flexibility of default values while keeping construction explicit. See Chapter 6 for how closures can create factory functions that return configured behavior.

Nested Structs
--------------

Structs can contain other structs as fields:

```
struct Address {
  street: string,
  city: string,
  zip: string,
}

struct Person {
  name: string,
  age: int,
  address: Address,
}

fn main() {
  p := Person {
    name: "Alice",
    age: 30,
    address: Address { street: "123 Main St", city: "Portland", zip: "97201" },
  };

  print(p.name);            // Alice
  print(p.address.city);    // Portland
  print(p.address.zip);     // 97201
}
```

Mutation works through nested field access:

```
fn main() {
  p := Person {
    name: "Bob",
    age: 25,
    address: Address { street: "456 Oak Ave", city: "Seattle", zip: "98101" },
  };

  p.address.city = "Tacoma";
  p.age = 26;
  print(p.address.city);  // Tacoma
}
```

Since structs are passed by reference, modifying a nested struct through a function affects the original all the way up:

```
fn relocate(person: Person, new_city: string) {
  person.address.city = new_city;
}

fn main() {
  p := Person {
    name: "Dana",
    age: 35,
    address: Address { street: "100 Elm St", city: "Austin", zip: "73301" },
  };

  relocate(p, "Houston");
  print(p.address.city);  // Houston
}
```

Structs with Arrays and Maps
----------------------------

Struct fields can hold arrays and maps, enabling rich data models:

```
struct StudentRecord {
  name: string,
  grades: [int],
}

fn average_grade(s: StudentRecord) -> float {
  sum := 0;
  for g in s.grades {
    sum = sum + g;
  }
  return (sum as float) / (s.grades.len as float);
}

fn main() {
  student := StudentRecord { name: "Eve", grades: [88, 92, 75, 96] };
  print(average_grade(student));  // 87.75

  student.grades.push(100);
  print(student.grades.len);     // 5
}
```

```
struct Inventory {
  items: map[string]int,
}

fn add_item(inv: Inventory, name: string, qty: int) {
  if inv.items.has(name) {
    inv.items[name] = inv.items[name] + qty;
  } else {
    inv.items[name] = qty;
  }
}

fn main() {
  inv := Inventory { items: {} };
  add_item(inv, "apples", 5);
  add_item(inv, "bananas", 3);
  add_item(inv, "apples", 2);
  print(inv.items["apples"]);  // 7
}
```

See Chapter 9 for the full set of array and map operations.

Practical Examples
------------------

### RGB Color Manipulation

```
struct Color {
  r: int,
  g: int,
  b: int,
}

fn clamp(val: int, lo: int, hi: int) -> int {
  if val < lo { return lo; }
  if val > hi { return hi; }
  return val;
}

fn brighten(c: Color, amount: int) {
  c.r = clamp(c.r + amount, 0, 255);
  c.g = clamp(c.g + amount, 0, 255);
  c.b = clamp(c.b + amount, 0, 255);
}

fn mix(a: Color, b: Color) -> Color {
  return Color {
    r: (a.r + b.r) / 2,
    g: (a.g + b.g) / 2,
    b: (a.b + b.b) / 2,
  };
}

fn color_to_string(c: Color) -> string {
  return "rgb({c.r}, {c.g}, {c.b})";
}

fn main() {
  red := Color { r: 200, g: 50, b: 50 };
  blue := Color { r: 50, g: 50, b: 200 };

  brighten(red, 40);
  print(color_to_string(red));    // rgb(240, 90, 90)

  purple := mix(red, blue);
  print(color_to_string(purple)); // rgb(145, 70, 145)
}
```

### Tree Structure

Structs that contain arrays of the same type enable tree-like patterns:

```
struct TreeNode {
  value: int,
  children: [TreeNode],
}

fn sum_tree(node: TreeNode) -> int {
  total := node.value;
  for child in node.children {
    total = total + sum_tree(child);
  }
  return total;
}

fn main() {
  tree := TreeNode {
    value: 1,
    children: [
      TreeNode { value: 2, children: [] },
      TreeNode {
        value: 3,
        children: [
          TreeNode { value: 4, children: [] },
          TreeNode { value: 5, children: [] },
        ],
      },
    ],
  };

  print(sum_tree(tree));  // 15
}
```

Summary
-------

| Concept | Syntax |
| --- | --- |
| Declare a struct | `struct Name { field: type, ... }` |
| Construct an instance | `Name { field: value, ... }` |
| Read a field | `instance.field` |
| Mutate a field | `instance.field = value;` |
| Nested field access | `instance.field.subfield` |

Structs are heap-allocated and passed by reference. There are no methods — use standalone functions that take the struct as a parameter. Keep structs simple: they hold data, functions provide behavior.



Chapter 9: Collections
======================

Mog provides three collection types: arrays for ordered sequences, maps for key-value lookup, and SoA (Struct of Arrays) for cache-friendly columnar storage. Together they cover the vast majority of data organization needs.

Arrays
------

Arrays are dynamically-sized, ordered, homogeneous sequences. They grow and shrink as needed and are the most common collection type.

### Array Literals

Create arrays with bracket syntax. The element type is inferred:

```
fn main() -> int {
  numbers := [1, 2, 3, 4, 5];
  names := ["Alice", "Bob", "Charlie"];
  flags := [true, false, true];

  println(numbers.len());  // 5
  println(names.len());    // 3
  return 0;
}
```

### Repeat Syntax

Create arrays filled with a repeated value using `[value; count]`:

```
fn main() -> int {
  zeros := [0; 100];           // 100 zeros
  blank := [""; 10];           // 10 empty strings
  grid := [false; 64];         // 64 false values

  println(zeros.len());   // 100
  println(zeros[50]);     // 0
  return 0;
}
```

Use repeat syntax to create empty arrays — `[0; 0]` gives you an empty `[int]` ready for `.push()`:

```
fn main() -> int {
  buffer := [0; 0];     // empty int array
  scores := [0.0; 50];  // 50 floats, all 0.0
  return 0;
}
```

### Type Annotations

Array types are written as `[ElementType]`. Function parameters and return types always require explicit types:

```
fn sum(numbers: [int]) -> int {
  total := 0;
  for n in numbers {
    total = total + n;
  }
  return total;
}

fn first_or_default(items: [string], fallback: string) -> string {
  if items.len() > 0 {
    return items[0];
  }
  return fallback;
}

fn main() -> int {
  vals := [10, 20, 30];
  println(sum(vals));  // 60

  empty: [string] = [];
  println(first_or_default(empty, "none"));  // none
  return 0;
}
```

### Indexing

Access elements by zero-based index with brackets. Out-of-bounds access is a runtime error:

```
fn main() -> int {
  arr := [10, 20, 30, 40, 50];

  println(arr[0]);   // 10
  println(arr[4]);   // 50

  // Mutation by index
  arr[2] = 99;
  println(arr[2]);   // 99

  // Index with a variable
  i := 3;
  println(arr[i]);   // 40
  return 0;
}
```

> **Warning:** Accessing an index beyond the array’s length causes a runtime panic. Always check `.len()` if the index is computed dynamically.

### Iteration

Use `for` to iterate over elements. The two-variable form gives you the index (see Chapter 4):

```
fn main() -> int {
  colors := ["red", "green", "blue"];

  // Value only
  for color in colors {
    println(color);
  }

  // Index and value
  for i, color in colors {
    println(f"{i}: {color}");
  }
  // 0: red
  // 1: green
  // 2: blue
  return 0;
}
```

### `.push()` and `.pop()`

Append to the end with `.push()`. Remove and return the last element with `.pop()`:

```
fn main() -> int {
  stack := [0; 0];

  stack.push(10);
  stack.push(20);
  stack.push(30);
  println(stack.len());  // 3

  top := stack.pop();
  println(top);          // 30
  println(stack.len());  // 2
  return 0;
}
```

A stack using push/pop:

```
fn main() -> int {
  stack := [0; 0];
  items := [5, 3, 8, 1, 9];

  for item in items {
    stack.push(item);
  }

  for stack.len() > 0 {
    println(stack.pop());
  }
  // 9, 1, 8, 3, 5
  return 0;
}
```

### `.slice()`

Extract a sub-array with `.slice(start, end)`. The range is half-open — `start` is inclusive, `end` is exclusive:

```
fn main() -> int {
  arr := [10, 20, 30, 40, 50];

  first_three := arr.slice(0, 3);
  println(first_three);  // [10, 20, 30]

  middle := arr.slice(1, 4);
  println(middle);  // [20, 30, 40]

  last_two := arr.slice(3, 5);
  println(last_two);  // [40, 50]
  return 0;
}
```

### `.contains()`

Check if an element exists in the array:

```
fn main() -> int {
  primes := [2, 3, 5, 7, 11, 13];

  println(primes.contains(7));   // true
  println(primes.contains(4));   // false

  allowed := ["admin", "editor", "viewer"];
  role := "editor";
  if allowed.contains(role) {
    println("access granted");
  }
  return 0;
}
```

### `.reverse()`

Reverse an array in place:

```
fn main() -> int {
  arr := [1, 2, 3, 4, 5];
  arr.reverse();
  println(arr);  // [5, 4, 3, 2, 1]
  return 0;
}
```

### `.join()`

Combine array elements into a single string with a separator:

```
fn main() -> int {
  words := ["hello", "world"];
  println(words.join(" "));   // hello world
  println(words.join(", "));  // hello, world
  println(words.join(""));    // helloworld

  numbers := [1, 2, 3];
  println(numbers.join("-"));  // 1-2-3
  return 0;
}
```

### `.filter()`

Return a new array containing only elements that pass a test:

```
fn main() -> int {
  numbers := [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

  evens := numbers.filter(fn(n: int) -> bool { (n % 2) == 0 });
  println(evens);  // [2, 4, 6, 8, 10]

  big := numbers.filter(fn(n: int) -> bool { n > 5 });
  println(big);  // [6, 7, 8, 9, 10]
  return 0;
}
```

Filter with a named function:

```
fn is_positive(n: int) -> bool {
  return n > 0;
}

fn main() -> int {
  values := [-3, -1, 0, 2, 5, -7, 4];
  positives := values.filter(is_positive);
  println(positives);  // [2, 5, 4]
  return 0;
}
```

### `.map()`

Return a new array with each element transformed:

```
fn main() -> int {
  numbers := [1, 2, 3, 4, 5];

  doubled := numbers.map(fn(n: int) -> int { n * 2 });
  println(doubled);  // [2, 4, 6, 8, 10]

  as_strings := numbers.map(fn(n: int) -> string { str(n) });
  println(as_strings.join(", "));  // 1, 2, 3, 4, 5
  return 0;
}
```

### `.sort()`

Sort an array in place using a comparator function. The comparator returns a negative integer if the first element should come before the second, positive if after, and zero if equal:

```
fn main() -> int {
  numbers := [5, 2, 8, 1, 9, 3];

  // Ascending
  numbers.sort(fn(a: int, b: int) -> int { a - b });
  println(numbers);  // [1, 2, 3, 5, 8, 9]

  // Descending
  numbers.sort(fn(a: int, b: int) -> int { b - a });
  println(numbers);  // [9, 8, 5, 3, 2, 1]
  return 0;
}
```

Sorting strings:

```
fn main() -> int {
  names := ["Charlie", "Alice", "Bob", "Dana"];

  names.sort(fn(a: string, b: string) -> int {
    if a < b { return -1; }
    if a > b { return 1; }
    return 0;
  });

  println(names.join(", "));  // Alice, Bob, Charlie, Dana
  return 0;
}
```

### Chaining Array Methods

Methods like `.filter()` and `.map()` return new arrays, so you can chain them into pipelines:

```
fn main() -> int {
  numbers := [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

  // Get the squares of even numbers
  result := numbers
    .filter(fn(n: int) -> bool { (n % 2) == 0 })
    .map(fn(n: int) -> int { n * n });
  println(result);  // [4, 16, 36, 64, 100]
  return 0;
}
```

```
fn main() -> int {
  words := ["hello", "world", "", "mog", "", "lang"];

  // Remove empty strings, convert to uppercase, join
  output := words
    .filter(fn(s: string) -> bool { s.len() > 0 })
    .map(fn(s: string) -> string { s.upper() })
    .join(" ");
  println(output);  // HELLO WORLD MOG LANG
  return 0;
}
```

> **Tip:** Chaining `.filter()` then `.map()` is the most common pipeline. If you need to both filter and transform, this reads more clearly than a manual loop.

Maps
----

Maps are unordered key-value collections with string keys. Use them when you need to look up values by name rather than by position.

### Creating Maps

Create maps with brace syntax:

```
fn main() -> int {
  ages := { "Alice": 30, "Bob": 25, "Charlie": 35 };
  config := { "host": "localhost", "port": "8080" };
  return 0;
}
```

### Access and Mutation

Read values with bracket syntax. Set values the same way — writing to a key that doesn’t exist creates it:

```
fn main() -> int {
  scores := { "math": 95, "english": 88, "science": 92 };

  // Read
  println(scores["math"]);     // 95

  // Write — update existing key
  scores["math"] = 100;
  println(scores["math"]);     // 100

  // Write — add new key
  scores["history"] = 87;
  println(scores["history"]);  // 87
  return 0;
}
```

### `.has()` — Checking Key Existence

Check whether a key exists before accessing it:

```
fn main() -> int {
  m := { "name": "Alice", "city": "NYC" };

  if m.has("name") {
    println(m["name"]);  // Alice
  }

  if !m.has("age") {
    println("age not found");
  }
  return 0;
}
```

> **Note:** Accessing a key that doesn’t exist is a runtime error. Always use `.has()` or iterate with `for` when keys are dynamic.

### `.len()`, `.keys()`, `.values()`

```
fn main() -> int {
  m := { "a": 1, "b": 2, "c": 3 };

  println(m.len());     // 3

  ks := m.keys();
  println(ks);          // ["a", "b", "c"] (order may vary)

  vs := m.values();
  println(vs);          // [1, 2, 3] (order may vary)
  return 0;
}
```

### `.delete()` — Removing Entries

```
fn main() -> int {
  m := { "x": 10, "y": 20, "z": 30 };

  m.delete("y");
  println(m.len());     // 2
  println(m.has("y"));  // false
  return 0;
}
```

### Iterating Maps

Use `for key, value in map` to iterate over all entries:

```
fn main() -> int {
  prices := { "apple": 120, "banana": 80, "cherry": 300 };

  for name, price in prices {
    println(f"{name}: {price} cents");
  }
  return 0;
}
```

Collecting keys that meet a condition:

```
fn main() -> int {
  grades := { "Alice": 92, "Bob": 67, "Charlie": 85, "Dana": 45, "Eve": 78 };

  passing := [0; 0];
  for name, grade in grades {
    if grade >= 70 {
      passing.push(name);
    }
  }
  println(passing.join(", "));
  return 0;
}
```

### Practical Example: Word Counting

```
fn word_count(text: string) -> {string: int} {
  counts := { "": 0 };
  counts.delete("");  // start with empty map

  words := text.split(" ");
  for word in words {
    if counts.has(word) {
      counts[word] = counts[word] + 1;
    } else {
      counts[word] = 1;
    }
  }
  return counts;
}

fn main() -> int {
  text := "the cat sat on the mat the cat";
  counts := word_count(text);

  for word, n in counts {
    println(f"{word}: {n}");
  }
  // the: 3
  // cat: 2
  // sat: 1
  // on: 1
  // mat: 1
  return 0;
}
```

### Practical Example: Grouping Data

```
struct Student {
  name: string,
  grade: string,
}

fn group_by_grade(students: [Student]) -> {string: [string]} {
  groups := { "": [""] };
  groups.delete("");

  for s in students {
    if !groups.has(s.grade) {
      groups[s.grade] = [0; 0];
    }
    groups[s.grade].push(s.name);
  }
  return groups;
}

fn main() -> int {
  students := [
    Student { name: "Alice", grade: "A" },
    Student { name: "Bob", grade: "B" },
    Student { name: "Charlie", grade: "A" },
    Student { name: "Dana", grade: "C" },
    Student { name: "Eve", grade: "B" },
  ];

  groups := group_by_grade(students);
  for grade, names in groups {
    println(f"{grade}: {names.join(", ")}");
  }
  // A: Alice, Charlie
  // B: Bob, Eve
  // C: Dana
  return 0;
}
```

SoA (Struct of Arrays)
----------------------

SoA flips the usual memory layout. Instead of storing an array of structs (each struct contiguous in memory), SoA stores one contiguous array per field. This improves cache performance when you iterate over a single field across many elements — common in simulations, game engines, and data processing.

### When to Use SoA

Use SoA when:

* You have many instances of the same struct (hundreds or thousands)
* Your hot loops touch one or two fields at a time, not all of them
* Performance matters and you want cache-friendly access patterns

Use regular arrays of structs when:

* You have few instances
* You access all fields of each element together
* Simplicity matters more than cache behavior

### Construction

Define a regular struct (see Chapter 8), then create an SoA container with `soa StructName[capacity]`:

```
struct Particle {
  x: float,
  y: float,
  mass: float,
}

fn main() -> int {
  particles := soa Particle[1000];
  return 0;
}
```

This allocates three separate arrays of 1000 elements — one for `x`, one for `y`, one for `mass` — instead of one array of 1000 three-field structs.

### Field Access

Read and write fields using array-index-then-dot syntax:

```
fn main() -> int {
  particles := soa Particle[100];

  // Set fields
  particles[0].x = 10.0;
  particles[0].y = 20.0;
  particles[0].mass = 5.0;

  // Read fields
  println(particles[0].x);     // 10.0
  println(particles[0].mass);  // 5.0

  // Initialize several elements
  for i in 0..10 {
    particles[i].x = i as float * 10.0;
    particles[i].y = i as float * 5.0;
    particles[i].mass = 1.0;
  }

  println(particles[5].x);  // 50.0
  println(particles[9].y);  // 45.0
  return 0;
}
```

> **Tip:** The syntax `particles[i].x` looks like regular struct access, but under the hood the compiler lowers it to an index into the `x` column array. You get columnar storage with familiar syntax.

### Iteration Patterns

Iterating over a single field is where SoA shines. The compiler reads from a single contiguous array, keeping the CPU cache hot:

```
struct Entity {
  x: int,
  y: int,
  health: int,
  speed: int,
}

fn main() -> int {
  entities := soa Entity[500];

  // Initialize
  for i in 0..500 {
    entities[i].x = i;
    entities[i].y = i * 2;
    entities[i].health = 100;
    entities[i].speed = 5;
  }

  // Update all x positions — touches only the x array
  for i in 0..500 {
    entities[i].x = entities[i].x + entities[i].speed;
  }

  // Sum all health values — touches only the health array
  total_health := 0;
  for i in 0..500 {
    total_health = total_health + entities[i].health;
  }
  println(total_health);  // 50000
  return 0;
}
```

### Practical Example: Particle Simulation

A physics step that applies gravity and updates positions. Separating the gravity pass (which only touches `vy`) from the position pass (which touches `x`, `y`, `vx`, `vy`) maximizes cache efficiency:

```
struct Particle {
  x: float,
  y: float,
  vx: float,
  vy: float,
  mass: float,
}

fn step(particles: soa Particle, count: int, dt: float) {
  // Apply gravity — only touches vy array
  for i in 0..count {
    particles[i].vy = particles[i].vy - (9.8 * dt);
  }

  // Update positions — touches x, y, vx, vy arrays
  for i in 0..count {
    particles[i].x = particles[i].x + (particles[i].vx * dt);
    particles[i].y = particles[i].y + (particles[i].vy * dt);
  }
}

fn main() -> int {
  particles := soa Particle[1000];

  for i in 0..1000 {
    particles[i].x = 0.0;
    particles[i].y = 100.0;
    particles[i].vx = i as float * 0.1;
    particles[i].vy = 0.0;
    particles[i].mass = 1.0;
  }

  // Run 60 simulation steps
  for frame in 0..60 {
    step(particles, 1000, 0.016);
  }

  println(particles[0].y);
  println(particles[500].x);
  return 0;
}
```

### Practical Example: Column Operations

SoA is natural for column-oriented data processing — summing a column, finding a max, or filtering by a category all read from a single contiguous array:

```
struct Record {
  id: int,
  value: int,
  category: int,
}

fn column_sum(records: soa Record, count: int) -> int {
  total := 0;
  for i in 0..count {
    total = total + records[i].value;
  }
  return total;
}

fn column_max(records: soa Record, count: int) -> int {
  max_val := records[0].value;
  for i in 1..count {
    if records[i].value > max_val {
      max_val = records[i].value;
    }
  }
  return max_val;
}

fn count_category(records: soa Record, count: int, cat: int) -> int {
  n := 0;
  for i in 0..count {
    if records[i].category == cat {
      n = n + 1;
    }
  }
  return n;
}

fn main() -> int {
  data := soa Record[100];

  for i in 0..100 {
    data[i].id = i;
    data[i].value = (i * 7) % 50;
    data[i].category = i % 3;
  }

  println(column_sum(data, 100));
  println(column_max(data, 100));
  println(count_category(data, 100, 0));  // count of category 0
  return 0;
}
```

Putting It All Together
-----------------------

### Data Processing Pipeline

Combining arrays, maps, and structs for a complete processing workflow:

```
struct Sale {
  product: string,
  amount: int,
  region: string,
}

fn total_by_region(sales: [Sale]) -> {string: int} {
  totals := { "": 0 };
  totals.delete("");

  for sale in sales {
    if totals.has(sale.region) {
      totals[sale.region] = totals[sale.region] + sale.amount;
    } else {
      totals[sale.region] = sale.amount;
    }
  }
  return totals;
}

fn main() -> int {
  sales := [
    Sale { product: "widget", amount: 100, region: "east" },
    Sale { product: "gadget", amount: 250, region: "west" },
    Sale { product: "widget", amount: 150, region: "west" },
    Sale { product: "gizmo", amount: 75, region: "east" },
    Sale { product: "gadget", amount: 200, region: "east" },
  ];

  region_totals := total_by_region(sales);
  for region, total in region_totals {
    println(f"{region}: {total}");
  }
  // east: 375
  // west: 400
  return 0;
}
```

### Filter-Map-Sort Pipeline

```
struct Task {
  title: string,
  priority: int,
  done: bool,
}

fn main() -> int {
  tasks := [
    Task { title: "Write docs", priority: 2, done: false },
    Task { title: "Fix bug", priority: 1, done: false },
    Task { title: "Add tests", priority: 3, done: true },
    Task { title: "Review PR", priority: 1, done: false },
    Task { title: "Deploy", priority: 2, done: false },
  ];

  // Get incomplete tasks, sorted by priority
  pending := tasks.filter(fn(t: Task) -> bool { !t.done });
  pending.sort(fn(a: Task, b: Task) -> int { a.priority - b.priority });

  for t in pending {
    println(f"[P{t.priority}] {t.title}");
  }
  // [P1] Fix bug
  // [P1] Review PR
  // [P2] Write docs
  // [P2] Deploy
  return 0;
}
```

Summary
-------

| Collection | Create | Access | Iterate |
| --- | --- | --- | --- |
| Array | `[1, 2, 3]` or `[0; n]` | `arr[i]` | `for item in arr` |
| Map | `{ "key": value }` | `m["key"]` | `for k, v in m` |
| SoA | `soa Struct[n]` | `soa[i].field` | `for i in 0..n` |

**Array methods:** `.len()`, `.push()`, `.pop()`, `.slice()`, `.contains()`, `.reverse()`, `.filter()`, `.map()`, `.sort()`, `.join()`

**Map methods:** `.len()`, `.keys()`, `.values()`, `.has()`, `.delete()`

Arrays are the default choice. Use maps when you need key-based lookup. Use SoA when you have many elements and need to iterate over individual fields efficiently — the syntax stays familiar while the memory layout optimizes for your access pattern.



Chapter 10: Error Handling
==========================

Mog has no exceptions. There is no `throw`, no invisible stack unwinding, no `try`/`finally` cleanup semantics. When a function can fail, it says so in its return type, and the caller decides what to do. Errors are values — you create them, return them, match on them, and propagate them with the same tools you use for everything else.

This design means you can always see where failures are handled by reading the code. Nothing fails silently, and nothing interrupts your control flow from a distance.

Result<T>
---------

`Result<T>` is a built-in type with two variants: `ok(value)` wrapping a success value of type `T`, and `err(message)` wrapping an error message of type `string`. Any function that might fail returns a `Result`:

```
fn divide(a: int, b: int) -> Result<int> {
  if b == 0 {
    return err("division by zero");
  }
  return ok(a / b);
}
```

You construct results directly with `ok()` and `err()` — there are no special constructors or factory functions:

```
fn parse_port(s: string) -> Result<int> {
  n := parse_int(s)?;
  if n < 0 {
    return err("port cannot be negative");
  }
  if n > 65535 {
    return err(f"port out of range: {n}");
  }
  return ok(n);
}
```

Results can wrap any type, including compound types:

```
fn load_settings(path: string) -> Result<{string: string}> {
  content := fs.read(path)?;
  lines := content.split("\n");
  settings: {string: string} = {};

  for line in lines {
    parts := line.split("=");
    if parts.len() != 2 {
      return err(f"malformed setting: {line}");
    }
    settings[parts[0].trim()] = parts[1].trim();
  }
  return ok(settings);
}
```

Use `match` to handle both cases (see Chapter 4 for match syntax):

```
fn main() -> int {
  match divide(100, 7) {
    ok(v) => println(f"100 / 7 = {v}"),
    err(e) => println(f"failed: {e}"),
  }
  return 0;
}
```

You can bind the result first and match later:

```
fn main() -> int {
  result := divide(10, 0);

  match result {
    ok(v) => {
      println(f"result: {v}");
      println(f"doubled: {v * 2}");
    },
    err(e) => {
      println(f"division failed: {e}");
    },
  }
  return 0;
}
```

Match arms can contain any expression or block. A common pattern is returning from the enclosing function inside a match arm:

```
fn half_or_bail(n: int) -> Result<int> {
  match divide(n, 2) {
    ok(v) => return ok(v),
    err(e) => return err(f"halving failed: {e}"),
  }
}
```

Optional ?T
-----------

`?T` is a built-in type with two variants: `some(value)` wrapping a value of type `T`, and `none` representing absence. Use it when a value might not exist — not because something went wrong, but because there may simply be nothing there:

```
fn find_index(arr: [int], target: int) -> ?int {
  for i, v in arr {
    if v == target {
      return some(i);
    }
  }
  return none;
}
```

The `?` prefix goes on the type: `?int`, `?string`, `?User`. You construct values with `some()` and signal absence with `none`:

```
fn first_positive(numbers: [int]) -> ?int {
  for n in numbers {
    if n > 0 {
      return some(n);
    }
  }
  return none;
}
```

```
struct User {
  name: string,
  email: string,
}

fn lookup_user(users: [User], name: string) -> ?User {
  for u in users {
    if u.name == name {
      return some(u);
    }
  }
  return none;
}
```

Match on optionals the same way you match on results:

```
fn main() -> int {
  match find_index([10, 20, 30], 20) {
    some(i) => println(f"found at index {i}"),
    none => println("not found"),
  }
  return 0;
}
```

> **Tip:** Optionals carry no error message. If you need to explain *why* a value is absent, use `Result<T>` instead.

```
// Use ?T when absence is normal
fn get_middle_name(user: User) -> ?string {
  return user.middle_name;
}

// Use Result<T> when absence is a failure
fn get_required_field(data: {string: string}, key: string) -> Result<string> {
  if data.has(key) {
    return ok(data[key]);
  }
  return err(f"missing required field: {key}");
}
```

The ? Propagation Operator
--------------------------

Appending `?` to a `Result` or `?T` expression unwraps the success case and propagates the failure case. If the value is `ok(v)` or `some(v)`, it evaluates to `v`. If the value is `err(e)` or `none`, the current function returns immediately with that error or `none`.

The simplest case — unwrap or bail:

```
fn process() -> Result<int> {
  val := divide(10, 2)?;  // val is 5, or function returns the err
  return ok(val * 2);
}
```

Chaining multiple fallible operations is where `?` shines. Each `?` is an early-return point:

```
fn load_and_parse_config(path: string) -> Result<Config> {
  content := fs.read(path)?;           // bail if read fails
  json := parse_json(content)?;        // bail if parse fails
  config := validate_config(json)?;    // bail if validation fails
  return ok(config);
}
```

Without `?`, the same function requires nested matching:

```
fn load_and_parse_config(path: string) -> Result<Config> {
  match fs.read(path) {
    err(e) => return err(e),
    ok(content) => {
      match parse_json(content) {
        err(e) => return err(e),
        ok(json) => {
          match validate_config(json) {
            err(e) => return err(e),
            ok(config) => return ok(config),
          }
        },
      }
    },
  }
}
```

The `?` operator works inline in larger expressions:

```
fn compute_ratio(a: int, b: int, c: int) -> Result<float> {
  sum := divide(a, b)? + divide(a, c)?;
  return ok(sum as float);
}
```

It also works on optionals. A function returning `?T` can propagate `none` from another optional:

```
fn get_user_email(users: [User], name: string) -> ?string {
  user := lookup_user(users, name)?;  // returns none if not found
  return some(user.email);
}
```

> **Note:** The return type of your function must be compatible: `?` on a `Result` requires your function to return `Result`, and `?` on an optional requires your function to return an optional.

```
fn first_even(arr: [int]) -> ?int {
  for n in arr {
    if (n % 2) == 0 {
      return some(n);
    }
  }
  return none;
}

fn double_first_even(arr: [int]) -> ?int {
  val := first_even(arr)?;  // propagates none
  return some(val * 2);
}
```

try-catch Blocks
----------------

Sometimes you want to handle errors from a group of operations in one place rather than propagating them up. `try`-`catch` catches errors from `?` propagation inside the `try` block:

```
try {
  config := fs.read("config.json")?;
  data := fs.read("data.csv")?;
  process(config, data)?;
  println("done");
} catch(e) {
  println(f"setup failed: {e}");
}
```

The variable `e` in `catch(e)` is a `string` — the error message from whichever `?` failed. The parentheses around `e` are required.

`try`-`catch` is useful at the top level of a program or at the boundary of a subsystem, where you want to handle all errors uniformly:

```
fn run_pipeline() {
  try {
    input := read_input()?;
    validated := validate(input)?;
    result := transform(validated)?;
    write_output(result)?;
    println("pipeline complete");
  } catch(e) {
    println(f"pipeline failed: {e}");
  }
}
```

You can use `try`-`catch` inside loops:

```
fn process_files(paths: [string]) {
  for path in paths {
    try {
      content := fs.read(path)?;
      result := parse(content)?;
      println(f"{path}: {result}");
    } catch(e) {
      println(f"skipping {path}: {e}");
    }
  }
}
```

`try`-`catch` does not change your function’s return type. It’s a local error-handling boundary — it consumes the error instead of propagating it. If you need the function to still return `Result`, use `?` outside the `try` block or return explicitly from within `catch`:

```
fn load_with_fallback(primary: string, backup: string) -> Result<string> {
  try {
    content := fs.read(primary)?;
    return ok(content);
  } catch(e) {
    println(f"primary failed ({e}), trying backup");
  }

  // If we reach here, primary failed — try backup without catching
  content := fs.read(backup)?;
  return ok(content);
}
```

> **Tip:** A `try`-`catch` block lets you use `?` in functions that don’t return `Result`. Since `?` would normally require a `Result` return type, `try`-`catch` gives you a way to use `?` in void functions.

```
fn initialize() {
  try {
    config := load_config("app.json")?;
    connect_db(config.db_url)?;
    println("initialized");
  } catch(e) {
    println(f"init failed: {e}");
    process.exit(1);
  }
}
```

Match Patterns for Result and Optional
--------------------------------------

The `ok`, `err`, `some`, and `none` patterns work like any other match arms. You can combine them with guards and nested patterns.

Matching with variable binding:

```
fn describe_result(r: Result<int>) -> string {
  match r {
    ok(v) => return f"success: {v}",
    err(e) => return f"failure: {e}",
  }
}
```

Matching an optional inside a struct:

```
struct Response {
  status: int,
  body: ?string,
}

fn print_response(resp: Response) {
  match resp.body {
    some(text) => println(f"[{resp.status}] {text}"),
    none => println(f"[{resp.status}] (no body)"),
  }
}
```

> **Warning:** Match arms for `Result` and `?T` must be exhaustive. The compiler warns if you handle `ok` but not `err`, or `some` but not `none`.

```
// Compiler warning: missing err arm
match divide(10, 3) {
  ok(v) => println(v),
}

// Correct: handle both
match divide(10, 3) {
  ok(v) => println(v),
  err(e) => println(f"error: {e}"),
}
```

Practical Patterns
------------------

### Validation Chains

Build up validation by chaining multiple checks that each return `Result`:

```
fn validate_username(name: string) -> Result<string> {
  if name.len() == 0 {
    return err("username cannot be empty");
  }
  if name.len() < 3 {
    return err("username must be at least 3 characters");
  }
  if name.len() > 32 {
    return err("username must be at most 32 characters");
  }
  return ok(name);
}

fn validate_age(age: int) -> Result<int> {
  if age < 0 {
    return err("age cannot be negative");
  }
  if age > 150 {
    return err(f"age seems unrealistic: {age}");
  }
  return ok(age);
}

fn create_user(name: string, age: int) -> Result<User> {
  validated_name := validate_username(name)?;
  validated_age := validate_age(age)?;
  return ok(User { name: validated_name, age: validated_age });
}
```

### Safe Parsing

Parse user input and propagate failures naturally:

```
struct Point {
  x: float,
  y: float,
}

fn parse_point(s: string) -> Result<Point> {
  parts := s.split(",");
  if parts.len() != 2 {
    return err(f"expected 'x,y' but got: {s}");
  }
  x := parse_float(parts[0].trim())?;
  y := parse_float(parts[1].trim())?;
  return ok(Point { x: x, y: y });
}

fn parse_polygon(lines: [string]) -> Result<[Point]> {
  points: [Point] = [];
  for i, line in lines {
    match parse_point(line) {
      ok(p) => points.push(p),
      err(e) => return err(f"line {i + 1}: {e}"),
    }
  }
  if points.len() < 3 {
    return err(f"polygon needs at least 3 points, got {points.len()}");
  }
  return ok(points);
}
```

### Converting Between Result and Optional

Sometimes you have a `Result` but only care about the success case, or you have an optional but need an error message:

```
// Result<T> -> ?T: discard the error message
fn result_to_optional(r: Result<int>) -> ?int {
  match r {
    ok(v) => return some(v),
    err(_) => return none,
  }
}

// ?T -> Result<T>: supply an error message
fn optional_to_result(opt: ?int, msg: string) -> Result<int> {
  match opt {
    some(v) => return ok(v),
    none => return err(msg),
  }
}

fn find_or_fail(arr: [int], target: int) -> Result<int> {
  match find_index(arr, target) {
    some(i) => return ok(i),
    none => return err(f"value {target} not found in array"),
  }
}
```

### Providing Defaults for Optionals

When you have an optional and want a fallback:

```
fn get_port(config: {string: string}) -> int {
  match config["port"] {
    some(p) => {
      match parse_int(p) {
        ok(n) => return n,
        err(_) => return 8080,
      }
    },
    none => return 8080,
  }
}
```

Or using `?` inside `try`-`catch` for a more compact version:

```
fn get_port(config: {string: string}) -> int {
  try {
    p := config["port"]?;
    n := parse_int(p)?;
    return n;
  } catch(_) {
    return 8080;
  }
}
```

### Error Message Formatting

Build descriptive error messages with string interpolation (see Chapter 3):

```
fn load_user_record(id: int) -> Result<User> {
  path := f"data/users/{id}.json";
  content := match fs.read(path) {
    ok(c) => c,
    err(e) => return err(f"failed to read user {id}: {e}"),
  };
  user := match parse_user(content) {
    ok(u) => u,
    err(e) => return err(f"failed to parse user {id}: {e}"),
  };
  return ok(user);
}
```

The same function using `?` is shorter but loses the contextual error messages:

```
fn load_user_record(id: int) -> Result<User> {
  path := f"data/users/{id}.json";
  content := fs.read(path)?;
  user := parse_user(content)?;
  return ok(user);
}
```

Choose based on whether callers need context. Deep library code often adds context; top-level code often just propagates.

### Collecting Results

Process a list and stop at the first error, or collect all successes:

```
// Stop at first error
fn parse_all_ints(strings: [string]) -> Result<[int]> {
  results: [int] = [];
  for s in strings {
    n := parse_int(s)?;
    results.push(n);
  }
  return ok(results);
}

// Collect errors separately
fn parse_all_ints_lenient(strings: [string]) -> [int] {
  results: [int] = [];
  for s in strings {
    match parse_int(s) {
      ok(n) => results.push(n),
      err(_) => {},  // skip bad values
    }
  }
  return results;
}
```

### Nested Results

A function can return `Result<Result<T>>` when the outer and inner operations can both independently fail, though this is rare and usually a sign you should restructure:

```
fn fetch_and_parse(url: string) -> Result<Result<Config>> {
  response := match http.get(url) {
    ok(r) => r,
    err(e) => return err(f"network error: {e}"),
  };
  // Return ok wrapping the parse result — caller sees network vs parse errors separately
  return ok(parse_config(response.body));
}
```

In most cases, flatten the errors into a single `Result` instead:

```
fn fetch_and_parse(url: string) -> Result<Config> {
  response := http.get(url)?;
  config := parse_config(response.body)?;
  return ok(config);
}
```

Summary
-------

| Syntax | Meaning |
| --- | --- |
| `Result<T>` | A value that is either `ok(T)` or `err(string)` |
| `?T` | A value that is either `some(T)` or `none` |
| `ok(value)` | Construct a success result |
| `err(message)` | Construct an error result |
| `some(value)` | Construct a present optional |
| `none` | Construct an absent optional |
| `expr?` | Unwrap success or propagate failure |
| `try { ... } catch(e) { ... }` | Handle propagated errors locally |

Mog’s error handling is explicit and local. You always know which functions can fail by looking at their return type, and you always know where errors are handled by following the `?` operators and `match` arms. There are no hidden control flow paths — what you read is what runs.



Chapter 11: Async Programming
=============================

Mog uses `async`/`await` for asynchronous operations. Agent scripts need to wait on external operations — API calls, model inference, file I/O — and async functions let you express that waiting without blocking the entire program. The host runtime manages the event loop; Mog code never creates threads or manages concurrency primitives directly.

Async Functions
---------------

Mark a function as `async` to indicate it returns a future. Use `await` inside to wait for other async operations:

```
async fn fetch(url: string) -> Result<string> {
  response := await http.get(url)?;
  return ok(response.body);
}
```

An `async fn` can be called like any other function, but its return value is a future that must be `await`ed to get the actual result:

```
async fn greet(name: string) -> string {
  return f"hello, {name}";
}

async fn main() -> int {
  msg := await greet("world");
  println(msg);  // hello, world
  return 0;
}
```

> **Note:** When `main` is declared `async`, the runtime creates the event loop automatically. You don’t need to set up or start the loop yourself.

Async functions can call other async functions. Each `await` suspends the current function until the awaited future completes:

```
async fn fetch_json(url: string) -> Result<string> {
  raw := await http.get(url)?;
  parsed := parse_json(raw.body)?;
  return ok(parsed);
}

async fn get_user_name(id: int) -> Result<string> {
  data := await fetch_json(f"https://api.example.com/users/{id}")?;
  return ok(data["name"]);
}
```

Await
-----

The `await` keyword suspends execution until a future resolves. It works on any expression that produces a future:

```
async fn pipeline() -> Result<string> {
  raw := await fetch_data("https://api.example.com/data")?;
  processed := await transform(raw)?;
  return ok(processed);
}
```

Each `await` is a suspension point. The runtime can run other tasks while this function waits. Without `await`, the future is created but never resolved:

```
async fn example() -> Result<string> {
  // This creates a future but doesn't wait for it — probably a bug
  // fetch_data("https://api.example.com");

  // This creates the future AND waits for the result
  result := await fetch_data("https://api.example.com")?;
  return ok(result);
}
```

> **Warning:** Forgetting `await` is a common mistake. If you call an async function without `await`, you get a future object, not the actual result.

You can combine `await` with the `?` operator from Chapter 10. The `await` resolves the future, then `?` unwraps the `Result`:

```
async fn load_config(path: string) -> Result<Config> {
  content := await fs.read_async(path)?;    // await the I/O, then ? the Result
  config := parse_config(content)?;
```
