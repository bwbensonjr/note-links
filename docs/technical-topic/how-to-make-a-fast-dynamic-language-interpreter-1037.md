---
id: 1037
url: https://zef-lang.dev/implementation
title: How To Make a Fast Dynamic Language Interpreter
domain: zef-lang.dev
source_date: '2026-04-19'
tags:
- compilers
- tutorial
- academic-paper
summary: The author optimized an AST-walking interpreter for the dynamic language
  Zef from a baseline to achieve 16x speedup, making it competitive with Lua, QuickJS,
  and CPython despite starting from an intentionally naive implementation. The optimization
  techniques employed—including improved value representation, inline caching, object
  model refinements, and watchpoints—required no advanced features like JIT compilation
  or bytecode, demonstrating that significant performance gains can be achieved through
  fundamental design choices and careful engineering. The post documents the methodology
  and incremental improvements across a benchmark suite of classic language benchmarks,
  showing how even simple interpreters can reach production-quality performance through
  systematic optimization.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# How To Make a Fast Dynamic Language Interpreter

How To Make a Fast Dynamic Language Interpreter
===============================================

This post is about optimizing an *extremely simple* AST-walking interpreter for a [dynamic language called Zef that I created for fun](index.html) to the point where it is competitive with the likes of Lua, QuickJS, and CPython.

Why?
----

Most of what gets written about making language implementations fast focuses on the work you'd do when you already have a stable foundation, like writing yet another JIT (just in time) compiler or fine tuning an already pretty good garbage collector. [I've written](https://webkit.org/blog/3362/introducing-the-webkit-ftl-jit/) [a lot](https://webkit.org/blog/5852/introducing-the-b3-jit-compiler/) [of posts](https://webkit.org/blog/6161/locking-in-webkit/) [about crazy](https://webkit.org/blog/7122/introducing-riptide-webkits-retreating-wavefront-concurrent-garbage-collector/) [optimizations in](https://webkit.org/blog/7536/) [a mature JS runtime](https://webkit.org/blog/10308/speculation-in-javascriptcore/). This post is different. It's about the case where you're starting from scratch, and you're nowhere near writing a JIT and your GC isn't your top problem.

The techniques in this post are easy to understand - *there's no SSA, no GC, no bytecodes, no machine code* - **yet they achieve a massive 16x speed-up** (*67x* if you include the incomplete port to Yolo-C++) and bring my tiny interpreter into the ballpark of QuickJS, CPython, and Lua.

The techniques I'll focus on in this post are:

* Value representation.
* Inline caching.
* Object model.
* Watchpoints.
* Grinding through common sense optimizations.

Evaluation Methodology
======================

To evaluate my progres, I created a [benchmark suite called ScriptBench1](scriptbench1.html). This has ports of classic language benchmarks to Zef:

* [Richards](https://www.cl.cam.ac.uk/%7Emr10/Bench.html) (OS scheduler)
* DeltaBlue (constraint solver)
* N-Body (physics simulation)
* Splay (binary tree test)

These benchmarks are also available in a wide variety of other languages. I found existing ports of these benchmarks to JavaScript, Python, and Lua. For Splay, there weren't existing Python and Lua ports, so I used Claude to port them.

All experiments run on Ubuntu 22.04.5 running on a Intel Core Ultra 5 135U with 32GB RAM and Fil-C++ version 0.677. Lua 5.4.7 is compiled with GCC 11.4.0. [QuickJS-ng 0.14.0 is the binary from QuickJS's GitHub releases page](https://github.com/quickjs-ng/quickjs/releases/download/v0.14.0/qjs-linux-x86_64). CPython 3.10 is just what came with Ubuntu.

All experiments use the average of 30 randomly interleaved runs.

**To be clear: for most of this post, I'll be comparing my interpreter compiled with Fil-C++ to other folks' interpreters compiled with Yolo-C compilers.**

Table Of Contents
=================

This post starts with a high-level description of the original AST-walking, hashtable-heavy Zef interpreter, followed by a section for each optimization that I landed on my journey to a 16.6x speed-up.

| Implementation | vs Zef Baseline | vs Python 3.10 | vs Lua 5.4.7 | vs QuickJS-ng 0.14.0 |
| --- | --- | --- | --- | --- |
| [Zef Baseline](#baseline) | 1x faster | 35.448x slower | 79.588x slower | 22.562x slower |
| [Zef Change #1: Direct Operators](#1-directops) | 1.175x faster | 30.161x slower | 67.716x slower | 19.196x slower |
| [Zef Change #2: Direct RMWs](#2-directrmws) | 1.219x faster | 29.081x slower | 65.291x slower | 18.509x slower |
| [Zef Change #3: Avoid IntObject](#3-avoidintobject) | 1.23x faster | 28.82x slower | 64.705x slower | 18.343x slower |
| [Zef Change #4: Symbols](#4-symbols) | 1.456x faster | 24.338x slower | 54.643x slower | 15.491x slower |
| [Zef Change #5: Value Inline](#5-valueinline) | 1.497x faster | 23.673x slower | 53.15x slower | 15.067x slower |
| [Zef Change #6: Object Model and Inline Caches](#6-objectmodel-and-ic) | 6.818x faster | 5.199x slower | 11.674x slower | 3.309x slower |
| [Zef Change #7: Arguments](#7-arguments) | 9.047x faster | 3.918x slower | 8.798x slower | 2.494x slower |
| [Zef Change #8: Getters](#8-getters) | 9.55x faster | 3.712x slower | 8.333x slower | 2.362x slower |
| [Zef Change #9: Setters](#9-setters) | 9.874x faster | 3.59x slower | 8.06x slower | 2.285x slower |
| [Zef Change #10: callMethod inline](#10-callmethodinline) | 10.193x faster | 3.478x slower | 7.808x slower | 2.213x slower |
| [Zef Change #11: Hashtable](#11-hashtable) | 11.758x faster | 3.015x slower | 6.769x slower | 1.919x slower |
| [Zef Change #12: Avoid std::optional](#12-avoidoptional) | 11.963x faster | 2.963x slower | 6.653x slower | 1.886x slower |
| [Zef Change #13: Specialized Arguments](#13-specializedargs) | 12.39x faster | 2.861x slower | 6.423x slower | 1.821x slower |
| [Zef Change #14: Improved Value Slow Paths](#14-valueslowpaths) | 13.642x faster | 2.598x slower | 5.834x slower | 1.654x slower |
| [Zef Change #15: Deduplicated DotSetRMW::evaluate](#15-dedupdotsetrmw) | 13.609x faster | 2.605x slower | 5.848x slower | 1.658x slower |
| [Zef Change #16: Fast sqrt](#16-sqrt) | 13.824x faster | 2.564x slower | 5.757x slower | 1.632x slower |
| [Zef Change #17: Fast toString](#17-tostring) | 14.197x faster | 2.497x slower | 5.606x slower | 1.589x slower |
| [Zef Change #18: Array Literal Specialization](#18-arrayliterals) | 15.351x faster | 2.309x slower | 5.184x slower | 1.47x slower |
| [Zef Change #19: Value callOperator Optimization](#19-valuecalloperator) | 16.344x faster | 2.169x slower | 4.87x slower | 1.38x slower |
| [Zef Change #20: Better C++ Configuration](#20-cppoptions) | 16.639x faster | 2.13x slower | 4.783x slower | 1.356x slower |
| [Zef Change #21: No Asserts](#21-noasserts) | 16.646x faster | 2.13x slower | 4.781x slower | 1.355x slower |
| [Zef in Yolo-C++](#yolo) | 66.962x faster | 1.889x faster | 1.189x slower | 2.968x faster |

Original Zef Interpreter
========================

[The original Zef interpreter](source-viewers/baseline.html) was written with almost no regard for performance. Only two performance-aware choices were made:

* The [value representation](source-viewers/baseline.html#value.h) is a 64-bit tagged value that may hold a double, a 32-bit integer, or a `Object*`. Doubles are represented by offsetting them by `0x1000000000000` (a technique I learned from JavaScriptCore; the literature has taken to calling this "NuN tagging"). Integers and pointers are represented natively, and I'm relying on the fact that no pointer will have a value below `0x100000000` (a dangerous choice, but one that you could force to be true; note that I could have represented integers by giving them a high bit tag of `0xffff000000000000` if I was worried about this). This makes it easy to have fast paths for operations on numbers (because you can detect if you have a number, and what kind, with a bit test). Even more importantly, this avoids heap allocations for numbers. **If you're building an interpreter from scratch, it's good to start by making good choices about the fundamental value representation, since it's super hard to change later!** *32-bit or 64-bit tagged values are a standard place to start, if you're implementing a dynamically typed language.*
* I used some kind of C++. It's important to pick a language that allows me to do all of the optimizations that language implementations eventually grow to have, and C++ is such a language. Notably, I would not pick something like Java, since there's a ceiling to how many low level optimizations you can do. I would also not pick Rust, since a garbage collected language requires a heap representation that has global mutable state and cyclic references (though you could use Rust for some parts of the interpreter, if you were happy with being multilingual; or you could use Rust if you were happy with lots of `unsafe` code).

I also made tons of expedient choices that were wrong from a performance engineering standpoint:

* I used [Fil-C++](https://fil-c.org/). This did allow me to move very quickly - for example, I get a garbage collector for free. Also, it meant that I spent zero time debugging memory safety issues (Fil-C++ reports memory safety violations with a pretty stack trace and lots of diagnostics) or undefined behavior (Fil-C++ does not have undefined behavior). Fil-C++ costs about 4x performance typically, so I'm starting with that 4x handicap, on top of all of the other suboptimal choices.
* Recursive AST walking interpreter. The interpreter is implemented as a [virtual `Node::evaluate` method](source-viewers/baseline.html#node.h:20) that gets overridden in a bunch of places.
* Strings everywhere. For example, the [`Get` AST node](source-viewers/baseline.html#get.h) holds a `std::string` to describe the name of the variable that it's getting, and that string is used each time a variable is accessed.
* Hashtables everywhere. When that `Get` executes, the string is used as a [key to a `std::unordered_map`](source-viewers/baseline.html#context.cpp:43-45), which contains the variable value.
* [Chains of](source-viewers/baseline.html#context.cpp:51-60) [recursive calls](source-viewers/baseline.html#userobject.cpp:43-50) to crawl the scope chain. Zef allows almost all constructs to be nested and nesting leads to closures; for example, class A nested in function F nested in class B nested in function G means that member functions of class A can see A's fields, F's locals, B's fields, and G's locals. The original interpreter achieved this by recursing in C++ over functions that can query different scope objects.

That said, those "poor choices" allowed me to implement an interpreter for a fairly sophisticated language with very little code. The largest module by far is the [parser](source-viewers/baseline.html#parse.cpp). Everything else is simple and crisp.

**This interpreter was 35x slower than CPython 3.10, 80x slower than Lua 5.4.7, and 23x slower than QuickJS-ng 0.14.0.** Let's see how far we can get by implementing a bunch of optimizations!

Optimization #1: Directly Call Operators
========================================

[The first optimization](diff-viewers/1-directops.html) is to have the parser generate distinct AST nodes for each operator as opposed to using the `DotCall` node with the name of the operator.

In Zef, this:

```
a + b
```

Is identical to this:

```
a.add(b)
```

So, the original interpreter would [parse `a + b` to `DotCall(a, "add")` with `b` as an argument](source-viewers/baseline.html#parse.cpp:584). That lead to slow execution since every since math operation involved a string lookup of the operator's method name:

* [`DotCall` would pass the string to `Value::callMethod`](source-viewers/baseline.html#dotcall.h:34).
* [`Value::callMethod` would cascade through multiple string comparisons](source-viewers/baseline.html#value.cpp:212-249).

With this optimization, we [have the parser create](diff-viewers/1-directops.html#parser.cpp:584) [`Binary<>`](source-viewers/1-directops.html#binary.h) and [`Unary<>`](source-viewers/1-directops.html#unary.h) nodes. With the help of some template and lambda magic, these nodes have separate virtual overrides for `Node::evaluate` per operator. These call directly into the corresponding [`Value` fast paths for those operators](source-viewers/1-directops.html#value.cpp:23-199). Hence, doing `a + b` now results in a call to `Binary<lambda for add>::evaluate`, which then calls `Value::add`.

**This change is a 17.5% speed-up.** *At this point, Zef is 30x slower than CPython 3.10, 67x slower than Lua 5.4.7, and 19x slower than QuickJS-ng 0.14.0.*

Optimization #2: Directly Call RMWs (Read Modify Write Operators)
=================================================================

In the previous optimization, we made operators fast by avoiding string comparison based dispatch. But that change didn't affect *all* operators! The RMW forms of those operators, like:

```
a += b
```

still used string based dispatch. So, [the second optimization](diff-viewers/2-directrmws.html) is to have the [parser generate distinct nodes](diff-viewers/2-directrmws.html#parse.cpp:745-750) for [each of the RMW cases](diff-viewers/2-directrmws.html#rmw.h). What's happening here is that the parser requests LValue nodes to replace themselves with an RMW via the `makeRMW` virtual call:

* [Get](diff-viewers/2-directrmws.html#get.h:26) - corresponds to getting a variable, i.e. just `id`
* [Dot](diff-viewers/2-directrmws.html#dot.h:24) - corresponds to `expr.id`
* [Subscript](diff-viewers/2-directrmws.html#subscript.h:23) - corresponds to subscript, i.e. `expr[index]`

Each of these virtual calls use the [`SPECIALIZE_NEW_RMW`](source-viewers/2-directrmws.html#rmw.h:14-34) macro to create template specialized forms of:

* [SetRMW](source-viewers/2-directrmws.html#setrmw.h) - corresponds to `id += value`
* [DotSetRMW](source-viewers/2-directrmws.html#dotsetrmw.h) - corresponds to `expr.id += value`
* [SubscriptRMW](source-viewers/2-directrmws.html#subscriptrmw.h) - corresponds to `expr[index] += value`

Note that while the rest of the operator specialization (from change #1) uses lambdas to dispatch to the appropriate operator function `Value`, for RMWs we use an enumeration. This is a practical choice because of the number of places we have to thread the enum through to handle the fact that we may arrive at an RMW three different ways (get, dot, and subscript). All of this magic then bottoms out in the [`Value::callRMW<>`](source-viewers/2-directrmws.html#value.h:150-171) template function, which dispatches the actual RMW operator call.

**This change is a 3.7% speed-up.** *At this point, Zef is 29x slower than CPython 3.10, 65x slower than Lua 5.4.7, and 18.5x slower than QuickJS-ng 0.14.0.* We're now 1.22x faster than where we started.

Optimization #3: Avoid IntObject Checks
=======================================

The [`Value` fast paths](source-viewers/2-directrmws.html#value.cpp:23-199) have a small problem: they use [`isInt()`](source-viewers/2-directrmws.html#value.h:62-65), which uses [`isIntSlow()`](source-viewers/2-directrmws.html#value.cpp:281-284), which does a virtual call to [`Object::isInt()`](source-viewers/2-directrmws.html#object.h:23) to check if we're really dealing with an int.

This is happening because the Zef value representation in the original interpreter had four distinct cases:

1. A tagged int32 value.
2. A tagged double value.
3. An IntObject for int64's that cannot be represented as int32's.
4. All other objects.

In the IntObject case, `Value` still drove the dispatch for all integer methods, since that allowed the interpreter to just have one implementation of all math operators (and that implementation was alwayts in `Value`).

[This simple optimization](diff-viewers/3-avoidintobject.html) causes `Value` fast paths to [only consider int32 and double](diff-viewers/3-avoidintobject.html#value.cpp:25-201), and puts all `IntObject` handling [in `IntObject` itself](diff-viewers/3-avoidintobject.html#intobject.cpp). Additionally, [this change avoids the `isInt()` call on every method dispatch](diff-viewers/3-avoidintobject.html#value.cpp:213-214).

**This is a 1% speed-up.** *At this point, Zef is 29x slower than CPython 3.10, 65x slower than Lua 5.4.7, and 18x slower than QuickJS-ng 0.14.0.* We're now 1.23x faster than where we started.

Optimization #4: Symbols
========================

The original Zef interpreter uses `std::string` *everywhere*. Particularly brutal cases:

* [`Context::get`, `Context::set`, and `Context::callFunction`](source-viewers/3-avoidintobject.html#context.h:48-61) - these are used for local variable and local function access.
* [`Value::callMethod`, `Value::dot`, and `Value::setDot`](source-viewers/3-avoidintobject.html#value.h:143-148) - these are used for any `expr.something` operation.
* [`Value::callOperator<>`](source-viewers/3-avoidintobject.html#value.h:175-219) - how named calls to primitives are resolved
* [`Object::callMethod` and friends](source-viewers/3-avoidintobject.html#object.h:27-46) - how method calls are resolved

This is unfortunate because it means that all of these lookups don't just involve hashtables - they involve hashtables keyed by those strings! So we're hashing and comparing strings all the time when executing Zef.

[This next optimization uses pointers to hash-consed Symbol objects instead of strings for all of those lookups.](diff-viewers/4-symbols.html) This is a large change in terms of files impacted, but it's really quite simple:

* There's a new `Symbol` class in [symbol.h](http://localhost:8000/source-viewers/4-symbols.html#symbol.h) and [symbol.cpp](http://localhost:8000/source-viewers/4-symbols.html#symbol.cpp). Symbols can be turned into strings and vice versa. Turning a string into a symbol involves a global hashtable to perform hash consing. This ensures that pointer equality on `Symbol*` is a valid way to check if two symbols are the same.
* Lots of places where we now refer to pre-cooked symbols instead of string literals, [like `Symbol::subscript` instead of using the string `"subscript"`](diff-viewers/4-symbols.html#value.cpp:229).
* Lots of places where we just change function signatures to use [`Symbol* instead of`const std::string&`](diff-viewers/4-symbols.html#context.cpp).

**This is a 18% speed-up.** *At this point, Zef is 24x slower than CPython 3.10, 54x slower than Lua 5.4.7, and 15x slower than QuickJS-ng 0.14.0.* We're now 1.46x faster than where we started.

Optimization #5: Value Inline
=============================

[This change delivers a significant win by allowing inlining of important functions.](diff-viewers/5-valueinline.html)

Almost all of the action in this change is the introduction of the [new `valueinlines.h` header](source-viewers/5-valueinline.html#valueinlines.h). This has separate header from `value.h`, since it uses headers that need to include `value.h.

**This is a 2.8% speed-up.** *At this point, Zef is 24x slower than CPython 3.10, 53x slower than Lua 5.4.7, and 15x slower than QuickJS-ng 0.14.0.* We're now 1.5x faster than where we started.

Optimization #6: Object Model, Inline Caches, and Watchpoints
=============================================================

Sometimes the only way to make your language implementation better is to land a massive patch. Don't let anyone tell you that good engineering happens in small, easy to digest changes. That's not always the case! It's certainly not the case if you want to have a fast implementation of a dynamic language!

[This is a massive change that redoes how `Object`, `ClassObject`, and `Context` work so that objects are cheaper to allocate and accesses can avoid hashtable lookups.](diff-viewers/6-objectmodel-and-ic.html) This change combines three changes into one:

Object model
------------

Previously, each lexical scope allocated `Context` object, and each `Context` object contained a [hashtable](source-viewers/5-valueinline.html#context.h:149) of "fields" - i.e. the variables in that scope. Objects were even worse: each object was a [hashtable](source-viewers/5-valueinline.html#userobject.h:60) that mapped the classes that the object was an instance of to `Context` objects. This was necessary because if you have an instance of `Bar` that descends from `Foo`, then `Bar` and `Foo` could both close over different scopes and they could share the same names for distinct fields (since fields are private by default in Zef). Clearly this is super inefficient! **This change introduces the idea of [`Storage`](source-viewers/6-objectmodel-and-ic.html#storage.h), which holds data at [`Offsets`](source-viewers/6-objectmodel-and-ic.html#offsets.h) determined by some [`Context`](source-viewers/6-objectmodel-and-ic.html#context.h:101-126).** *So, `Context`s still exist, but they are created [ahead of time as part of the AST `resolve` pass](source-viewers/6-objectmodel-and-ic.html#node.h:30); when objects or scopes are created, we just [allocate](source-viewers/6-objectmodel-and-ic.html#storage.h:9-13) a storage according to the [size computed by the corresponding `Context`](source-viewers/6-objectmodel-and-ic.html#context.h:29).*

Inline caches
-------------

This is a [classic technique](https://bibliography.selflanguage.org/_static/pics.pdf) that [forms the foundation of modern high performance dynamic language implementations](https://webkit.org/blog/10308/speculation-in-javascriptcore/). But while this technique is classically discussed in the context of JIT compilers, in this change we'll use it in an interpreter. **The idea of inline caches is that given a location in code that does `expr.name`, we remember the last type that `expr` dynamically had and the last offset that `name` resolved to.** In this change, the "remembering" is done by [placement constructing a specialized AST node](source-viewers/6-objectmodel-and-ic.html#constructcache.h:989-997) on top of the generic one. There are five parts to this:

1. The [`CacheRecipe`](source-viewers/6-objectmodel-and-ic.html#cacherecipe.h) object is used to track what a particular access did, and whether it's cacheable.
2. There are calls to `CacheRecipe` sprinkled throughout [`Context`](source-viewers/6-objectmodel-and-ic.html#context.cpp:91-92), [`ClassObject`](source-viewers/6-objectmodel-and-ic.html#classobject.cpp:257-258), and [`Package`](source-viewers/6-objectmodel-and-ic.html#package.cpp:98-102).
3. AST evaluation functions like `Dot::evaluate` [pass the `CacheRecipe` they got from whatever polymorphic operation they performed to `constructCache<>` along with `this`](source-viewers/6-objectmodel-and-ic.html#dot.cpp:85-97).
4. [`constructCache` compiles a new AST node specialization according to `CacheRecipe`](source-viewers/6-objectmodel-and-ic.html#constructcache.h). Yes, compiles: `constructcache.h` has a template machine that can produce many different kinds of specialized AST nodes. For example, it might specialize to a [direct load on the `storage` that the AST node was passed](source-viewers/6-objectmodel-and-ic.html#constructcache.h:118-162) (like in case of a local variable access). Or, it might emit a [class check](source-viewers/6-objectmodel-and-ic.html#constructcache.h:325-373) (*"does this object still have the class I last saw?"*) followed by a [direct function](source-viewers/6-objectmodel-and-ic.html#constructcache.h:230-273) call to whatever function was last seen. These may be composed with [chain steps](source-viewers/6-objectmodel-and-ic.html#constructcache.h:419-468) and [watchpoints](source-viewers/6-objectmodel-and-ic.html#constructcache.h:523-581) if the access being cached involved walking the scope chain.
5. Each AST node that is subject to caching has a [cached variant](source-viewers/6-objectmodel-and-ic.html#dot.cpp:25-49) that first attempts a fast call into a `cache` object, whose type is determined by `constructCache<>`.

Watchpoints
-----------

Say that we have a class `Foo` inside a lexical scope that has variable `x`, and one of `Foo`'s methods wants to access `x`. And, let's say that there are no functions or varialbes called `x` inside `Foo`. We should be able to access `x` without any checkes, right? Well, not quite - someone could subclass `Foo` and add a getter called `x`, in which case that access should resolve to the getter, not the outer `x`. The way that inline caches handle this is by setting [`Watchpoint`s`](source-viewers/6-objectmodel-and-ic.html#watchpoint.h) within the runtime. In this example, it's the ["was the name overridden"](source-viewers/6-objectmodel-and-ic.html#class.h:129) watchpoint.

Putting it together
-------------------

Each of these three features is large. I chose to implement all of them at once because:

* A new object model would not be meaningfully better unless it allowed inline caching to work well. So, I codeveloped the object model and inline chaces.
* Inline caches wouldn't provide meaningful benefit unless I also had watchpoints, because so many cacheable conditions require watchpoints.
* The new object model and watchpoints have to work great together.

I started this change by writing a dumb version of [`CacheRecipe`](source-viewers/6-objectmodel-and-ic.html#cacherecipe.h) along with what ended up being the mostly final version of [`Storage`](source-viewers/6-objectmodel-and-ic.html#storage.h) and [`Offsets`](source-viewers/6-objectmodel-and-ic.html#offsets.h).

Some of the hardest work involved replacing the old style of intrinsic classes with a new style. Take arrays as an example. Previously, [`ArrayObject::tryCallMethod`](source-viewers/5-valueinline.html#arrayobject.cpp) implemented all `ArrayObject` methods by simply intercepting the virtual `Object::tryCallMethod` call. But in the new object model, `Object` has no vtable and no virtual methods; instead `Object::tryCallMethod` forwards to [`object->classObject()->tryCallMethod(object, ...)`](source-viewers/6-objectmodel-and-ic.html#classobject.cpp:56-69). So, for `Array` to have methods, we need to [create a class for `Array` that has those methods](diff-viewers/6-objectmodel-and-ic.html#makerootcontext.cpp:208-295). Hence, this change shifts a lot of intrinsic functionality from being spread throughout the implementation to being focused inside [`makerootcontext.cpp`](source-viewers/6-objectmodel-and-ic.html#makerootcontext.cpp). *This is a good outcome, because it means that all of the inline caching machinery just works for native/intrinsic functions on objects!*

**This massive change has a massive win: 4.55x faster!** *At this point, Zef is 5.2x slower than CPython 3.10, 11.7x slower than Lua 5.4.7, and 3.3x slower than QuickJS-ng 0.14.0.* In other words, Zef compiled with Fil-C++'s margin of loss against those other interpreters is right around what Fil-C costs (those other interpreters are compiled with Yolo-C).

We're now 6.8x faster than where we started.

Optimization #7: Arguments
==========================

Before this change, the Zef interpreter would pass arguments to functions using `const std::optional<std::vector<Value>>&`. The `optional` was needed because in some corner cases we have to distinguish between:

```
o.getter
```

and:

```
o.function()
```

In most cases, in Zef, these two things are the same: they are a function call. Here's an exception:

```
o.NestedClass
```

vs:

```
o.NestedClass()
```

The first case gets the `NestedClass` object, while the second case instantiates it.

Therefore, we need to tell if we're passing an empty arguments array because this is a function call with zero arguments, or an empty arguments array because this was a getter-like call.

In any case, this is wildly inefficient because it means that the caller is allocating a `vector` and then the callee is [allocating an arguments scope that is a copy of that vector](source-viewers/6-objectmodel-and-ic.html#userfunction.cpp:128-133).

[This change](diff-viewers/7-arguments.html) introduces the [`Arguments`](source-viewers/7-arguments.html#arguments.h) type, which is shaped exactly like the arguments scope that the callee would have allocated. So, now we have the caller allocate these directly. This more than halves the number of allocations needed to make a call:

* Even in Yolo-C++, we'd be halving the allocations because we'd no longer have to malloc the backing store of the vector.
* In Fil-C++, the `std::optional` needs to be heap allocated. Even if we didn't have a `std::optional`, passing a `const std::vector<>&` would be an allocation because anything stack allocated is heap allocated.
* [It so happened that the callers would reallocate the vector multiple times rather than presizing it.](source-viewers/6-objectmodel-and-ic.html#callbase.h:24-31)

A lot of this change is just [changing function signatures](diff-viewers/7-arguments.html#package.cpp) to take `Arguments*` instead of the optional vectors.

**This is a 1.33x speed-up.** *At this point, Zef is 3.9x slower than CPython 3.10, 8.8x slower than Lua 5.4.7, and 2.5x slower than QuickJS-ng 0.14.0.* We're now 9.05x faster than where we started.

Optimization #8: Getter Specialization
======================================

Like Ruby and many other object oriented languages, Zef has private instance fields by default. They are private in the sense that only that instance can see them. Take this code:

```
class Foo {
    my f
    fn (inF) f = inF
}
```

This is a class `Foo` that takes a value for `f` in its constructor, and stores it to a *local variable scoped just to instances*. For example, this wouldn't work:

```
class Foo {
    my f
    fn (inF) f = inF
    fn nope(o) o.f
}
println(Foo(42).nope(Foo(666)))
```

The `o.f` expression in `nope` cannot access `o`'s `f` even though `o` is of the same type. This is just an outcome of the fact that fields work by appearing in the scope chain of class members. When we do something like `o.f`, we're asking to call a method called `f`. Hence, we get lots of code like:

```
class Foo {
    my f
    fn (inF) f = inF
    fn f f # method called f that returns local variable f
}
```

Or, more tersely:

```
class Foo {
    readable f # shorthand for `my f` and `fn f f`
    fn (inF) f = inF
}
```

Hence, lots of method calls end up being calls to getters. It's super wasteful to have all of those calls evaluate the AST of the getter along with everything this entails!

[So the next change is to specialize getters.](diff-viewers/8-getters.html)

[The heart of this change is in `UserFunction`](diff-viewers/8-getters.html#userfunction.cpp), which uses the new [`Node::inferGetter`](diff-viewers/8-getters.html#node.h:23) method to infer whether the body of the function is just a getter. The important bits of this are:

* [`Block::inferGetter`](diff-viewers/8-getters.html#block.cpp) infers itself to be a getter if all it contains is something that can be inferred to be a getter.
* [`Get::inferGetter`](diff-viewers/8-getters.html#get.cpp) infers itself to be a getter and returns the offset that it would load from.
* [`Context::tryGetFieldOffsets`](diff-viewers/8-getters.html#context.cpp) will only return a non-empty `Offsets` if the lexical scope that the getter executes in will definitely have that field.
* `UserFunction` [resolves](diff-viewers/8-getters.html#userfunction.cpp:116-117) itself to a [special `Function` subclass that just does a get at a known offset](diff-viewers/8-getters.html#userfunction.cpp:88-103), if the body can be inferred to be a getter.

**This is a 5.6% speed-up.** *At this point, Zef is 3.7x slower than CPython 3.10, 8.3x slower than Lua 5.4.7, and 2.4x slower than QuickJS-ng 0.14.0.* We're now 9.55x faster than where we started.

Optimization #9: Setter Specialization
======================================

[Now let's do the same thing to setters!](diff-viewers/9-setters.html)

The inference is a bit more complex this time, since we have to pattern match:

```
fn set_fieldName(newValue) fieldName = newValue
```

This means:

* [`UserFunction`'s inference has to pass down the setter's parameter name.](diff-viewers/9-setters.html#userfunction.cpp:139-142)
* [`Set`'s inference has to make sure that we're not doing a write to a `ClassObject` (those are immutable "fields") and that we're using the setter parameter as the source of the set.](diff-viewers/9-setters.html#set.cpp)

**This is a 3.4% speed-up.** *At this point, Zef is 3.6x slower than CPython 3.10, 8x slower than Lua 5.4.7, and 2.3x slower than QuickJS-ng 0.14.0.* We're now 9.87x faster than where we started.

Optimization #10: `callMethod` inlining
=======================================

[This is a one line change to inline an important function.](diff-viewers/10-callmethodinline.html#classobject.cpp)

**It's a 3.2% speed-up.** *At this point, Zef is 3.5x slower than CPython 3.10, 7.8x slower than Lua 5.4.7, and 2.2x slower than QuickJS-ng 0.14.0.* We're now 10.2x faster than where we started.

Optimization #11: Hashtable
===========================

Before this change, if the inline cache for a method call missed, then we'd have to descend through [`ClassObject::tryCallMethod`](source-viewers/10-callmethodinline.html#classobject.cpp:57-68) and [`ClassObject::TryCallMethodDirect`](source-viewers/10-callmethodinline.html#classobject.cpp:228-300), which are quite large and complex.

Also, that's O(hierarchy depth), or more precisely, two hashtable lookups per level in the hierarchy:

* [For each class in the hierarchy, we check if the call resolves to a member function](source-viewers/10-callmethodinline.html#classobject.cpp:247-256).
* [For each class in the hierarchy, we check if the call resolves to a nested class](source-viewers/10-callmethodinline.html#classobject.cpp:258-297).

[This next change introduces a global hashtable keyed by receiver class and symbol that directly gives the callee in one lookup.](diff-viewers/11-hashtable.html)

[In `classobject.h`, we perform a lookup in this global table before descending into the full `tryCallMethodSlow`](diff-viewers/11-hashtable.html#classobject.h).

[In `classobject.cpp`, we record successful lookups in the global table.](diff-viewers/11-hashtable.html#classobject.cpp)

[The global hashtable is itself quite simple.](diff-viewers/11-hashtable.html#table.h)

**This is a 15% speed-up.** *At this point, Zef is 3x slower than CPython 3.10, 6.8x slower than Lua 5.4.7, and 1.9x slower than QuickJS-ng 0.14.0.* We're now 11.8x faster than where we started.

Optimization #12: Avoid `std::optional`
=======================================

In Fil-C++, the `std::optional` needs to be heap allocated because of a compiler pathology involving unions.

Normally, LLVM plays fast and loose with the types of memory accesses used for unions, but this breaks [invisicaps](https://fil-c.org/invisicaps): pointers in unions will sometimes - quite unpredictably to the programmer - lose their capabilities. This leads to Fil-C panics saying that you're dereferencing an object with a null capability even though the programmer did nothing wrong. To mitigate this, the Fil-C++ compiler inserts intrinsics that force LLVM to be conservative about handling local variables of union type. Later, the `FilPizlonator` pass performs its own escape analysis to try to allow union typed locals to be register allocated - however, this analysis is nowhere near as complete as the usual LLVM `SROA` analysis.

The result: passing around classes like `std::optional` that have a union in them often leads to memory allocations in Fil-C++!

[So, this change avoids a code path that leads to `std::optional` on a hot path.](diff-viewers/12-avoidoptional.html#classobject.h)

**This is a 1.7% speed-up.** *At this point, Zef is 3x slower than CPython 3.10, 6.65x slower than Lua 5.4.7, and 1.9x slower than QuickJS-ng 0.14.0.* We're now 12x faster than where we started.

Optimization #13: Specialized Arguments
=======================================

All of the built-in functions in Zef take one or two arguments, and the native implementations have no need for an `Arguments` object to be allocated to hold those; they could just as easily be taking those arguments directly.

Setters all take one argument, and if we infer the setter, then the [specialized setter implementation](source-viewers/12-avoidoptional.html#userfunction.cpp:114-121) has no need for an `Arguments` object to be allocated; again, that code could just take the value argument directly.

[This next change introduces specialized arguments types called `ZeroArguments`, `OneArgument`, and `TwoArguments` to allow the caller to avoid allocating the `Arguments` object in cases where the callee doesn't need it.](diff-viewers/13-specializedargs.html)

[At the heart of this change are the new specialized arguments types.](diff-viewers/13-specializedargs.html#arguments.h) Note that we need `ZeroArguments` to distinguish from passing a `(Arguments*)nullptr`. We already used `(Arguments*)nullptr` to mean "getter call" and we leave that logic alone, so now `ZeroArguments` means "function call with no arguments".

[A lot of this change is about templatizing functions that take arguments](diff-viewers/13-specializedargs.html#context.h) and then [explicitly instantiating them for `ZeroArguments`, `OneArgument`, `TwoArguments`, and `Arguments*`](diff-viewers/13-specializedargs.html#context.cpp:305-316). A lot of code was already using `Value::getArg` as a helper to extract arguments, [so this change just adds overloads for the argument specializations](diff-viewers/13-specializedargs.html#valueinlines.h:20-69). Consequently, [changes to native code that uses arguments](diff-viewers/13-specializedargs.html#makerootcontext.cpp) are quite straight-forward.

**This is a 3.8% speed-up.** *At this point, Zef is 2.9x slower than CPython 3.10, 6.4x slower than Lua 5.4.7, and 1.8x slower than QuickJS-ng 0.14.0.* We're now 12.4x faster than where we started.

Optimization #14: Improved Value Slow Paths
===========================================

(This next change gets a big speed-up from working around another Fil-C pathology.](diff-viewers/14-valueslowpaths.html)

Before this change, [`Value` out-of-line slow paths were member functions of `Value`](source-viewers/13-specializedargs.html#value.h:208-209), meaning that they took an implicit `const Value*` argument. This means that the caller must stack-allocate a `Value`.

In Fil-C++, all stack allocation is a heap allocation. Hence, code that called slow paths would allocate `Value` in the heap!

[This changes those methods to be static and take `Value` by value](diff-viewers/14-valueslowpaths.html#value.h), obviating the need for any allocation.

**10% speed-up.** *At this point, Zef is 2.6x slower than CPython 3.10, 5.8x slower than Lua 5.4.7, and 1.65x slower than QuickJS-ng 0.14.0.* We're now 13.6x faster than where we started.

"Optimization" #15: Deduplicate `DotSetRMW`
===========================================

[This change removes some duplicated code.](diff-viewers/15-dedupdotsetrmw.html#dotsetrmw.h)

I was hoping it would be a speed-up because less machine code is better - especially in a template function that gets specialized by [`constructCache<>`](source-viewers/15-dedupdotsetrmw.html#constructcache.h).

But it's not a speed-up. This has no effect on performance.

Optimization #16: Specialize `sqrt`
===================================

Inline caches are good at routing calls to exactly the function you want, but they only work for objects. For non-objects, we're relying on the fact that [`Binary<>`](source-viewers/15-dedupdotsetrmw.html#binary.h), [`Unary<>`](source-viewers/15-dedupdotsetrmw.html#unary.h), and [`Value::callRMW<>`](source-viewers/15-dedupdotsetrmw.html#value.h:177-198) take us to fast paths that check if the receiver is an `int` or `double`.

But this only works for operators that are recognized by the parser. It doesn't work if we do `value.sqrt`, for example.

[So this next change teaches `Dot` to specialize for `value.sqrt`.](diff-viewers/16-sqrt.html#dot.cpp)

**This is a 1.6% speed-up.** *At this point, Zef is 2.6x slower than CPython 3.10, 5.75x slower than Lua 5.4.7, and 1.6x slower than QuickJS-ng 0.14.0.* We're now 13.8x faster than where we started.

Optimization #17: Specialize `toString`
=======================================

[This is almost exactly like the previous optimization, but for `toString`](diff-viewers/17-tostring.html#dot.cpp).

There's [a bit of extra logic in this change](diff-viewers/17-tostring.html#valueinlines.h) to reduce the number of allocations that happen when converting an int to a string.

**This is a 2.7% speed-up.** *At this point, Zef is 2.5x slower than CPython 3.10, 5.6x slower than Lua 5.4.7, and 1.6x slower than QuickJS-ng 0.14.0.* We're now 14.2x faster than where we started.

Optimization #18: Specialize Array Literals
===========================================

Say that we do:

```
my whatever = [1, 2, 3]
```

This has to allocate a new array, since arrays are aliasable and mutable in Zef. But worse, prior to this change, this would recurse down the AST every single time to evaluate `1`, `2`, and `3`.

[This change specializes the `ArrayLiteral` node in case it's allocating a constant array.](diff-viewers/18-arrayliterals.html#arrayliteral.cpp)

**This is a 8.1% speed-up.** *At this point, Zef is 2.3x slower than CPython 3.10, 5.2x slower than Lua 5.4.7, and 1.5x slower than QuickJS-ng 0.14.0.* We're now 15.35x faster than where we started.

Optimization #19: `Value::callOperator` Improvement
===================================================

Previously, we got a bit speed-up from not passing `Value` by reference. [This is the same optimization, just for the `callOperator` slow path.](diff-viewers/19-valuecalloperator.html#value.h)

**This is a 6.5% speed-up.** *At this point, Zef is 2.2x slower than CPython 3.10, 4.9x slower than Lua 5.4.7, and 1.4x slower than QuickJS-ng 0.14.0.* We're now 16.3x faster than where we started.

Optimization #20: Better C++ Options.
=====================================

This changes disable RTTI and libc++ hardening, since it's superfluous in Fil-C++.

There aren't any C++ changes here; it's just a build system configuration change.

**This is a 1.8% speed-up.** *At this point, Zef is 2.1x slower than CPython 3.10, 4.8x slower than Lua 5.4.7, and 1.35x slower than QuickJS-ng 0.14.0.* We're now 16.6x faster than where we started.

"Optimization" #21: No Asserts
==============================

[This last optimization turns off assertions by default.](diff-viewers/21-noasserts.html)

Previously, the code used the Fil-C-specific `ZASSERT` macro, which means "assert all the time". Now the code uses the internal [`ASSERT`](diff-viewers/21-noasserts.html#utils.h:13-19) macro, which means "only assert if `ASSERTS\_ENABLED` is set".

This change also includes some other changes to make the code build in Yolo-C++.

I was hoping that this would be a speed-up, but it wasn't.

What About Yolo-C++?
====================

Finally, I tried compiling the code with Yolo-C++. **This yielded a 4x speed-up**, though it's both unsound and suboptimal:

* It's unsound because we're turning what used to be calls into the Fil-C++ GC into calls to `calloc`, which means that memory is never freed. This interpreter will run out of memory for sufficiently long-running workloads. It happens to not run out of memory on ScriptBench1 because those tests run for only a short time.
* It's suboptimal because real GC allocators are faster than the `calloc` that comes with glibc 2.35.

So, if I did add a real GC to Zef as part of the Yolo-C++ port, I'd probably get more than a 4x speed-up.

I used GCC 11.4.0 for this experiment.

*At this point, Zef is 1.9x faster than CPython 3.10, 1.2x slower than Lua 5.4.7, and 3x faster than QuickJS-ng 0.14.0.* We're 67x faster than where we started!

Raw Data
========

Here's raw data, showing the execution times in seconds of all of the benchmarks, as well as the geomean of those benchmarks, on each interpreter.

| Implementation\Benchmark | nbody | splay | richards | deltablue | geomean |
| --- | --- | --- | --- | --- | --- |
| Python 3.10 | 0.0364 | 0.8326 | 0.0822 | 0.1135 | 0.1296 |
| Lua 5.4.7 | 0.0142 | 0.4393 | 0.0217 | 0.0832 | 0.0577 |
| QuickJS-ng 0.14.0 | 0.0214 | 0.7090 | 0.7193 | 0.1585 | 0.2036 |
| [Zef Baseline](#baseline) | 2.9573 | 13.0286 | 1.9251 | 5.9997 | 4.5927 |
| [Zef Change #1: Direct Operators](#1-directops) | 2.1891 | 12.0233 | 1.6935 | 5.2331 | 3.9076 |
| [Zef Change #2: Direct RMWs](#2-directrmws) | 2.0130 | 11.9987 | 1.6367 | 5.0994 | 3.7677 |
| [Zef Change #3: Avoid IntObject](#3-avoidintobject) | 1.9922 | 11.8824 | 1.6220 | 5.0646 | 3.7339 |
| [Zef Change #4: Symbols](#4-symbols) | 1.5782 | 9.9577 | 1.4116 | 4.4593 | 3.1533 |
| [Zef Change #5: Value Inline](#5-valueinline) | 1.4982 | 9.7723 | 1.3890 | 4.3536 | 3.0671 |
| [Zef Change #6: Object Model and Inline Caches](#6-objectmodel-and-ic) | 0.3884 | 3.3609 | 0.2321 | 0.6805 | 0.6736 |
| [Zef Change #7: Arguments](#7-arguments) | 0.3160 | 2.6890 | 0.1653 | 0.4738 | 0.5077 |
| [Zef Change #8: Getters](#8-getters) | 0.2988 | 2.6919 | 0.1564 | 0.4260 | 0.4809 |
| [Zef Change #9: Setters](#9-setters) | 0.2850 | 2.6690 | 0.1514 | 0.4072 | 0.4651 |
| [Zef Change #10: callMethod inline](#10-callmethodinline) | 0.2533 | 2.6711 | 0.1513 | 0.4032 | 0.4506 |
| [Zef Change #11: Hashtable](#11-hashtable) | 0.1796 | 2.6528 | 0.1379 | 0.3551 | 0.3906 |
| [Zef Change #12: Avoid std::optional](#12-avoidoptional) | 0.1689 | 2.6563 | 0.1379 | 0.3518 | 0.3839 |
| [Zef Change #13: Specialized Arguments](#13-specializedargs) | 0.1610 | 2.5823 | 0.1350 | 0.3372 | 0.3707 |
| [Zef Change #14: Improved Value Slow Paths](#14-valueslowpaths) | 0.1348 | 2.5062 | 0.1241 | 0.3076 | 0.3367 |
| [Zef Change #15: Deduplicated DotSetRMW::evaluate](#15-dedupdotsetrmw) | 0.1342 | 2.5047 | 0.1256 | 0.3079 | 0.3375 |
| [Zef Change #16: Fast sqrt](#16-sqrt) | 0.1274 | 2.5045 | 0.1251 | 0.3060 | 0.3322 |
| [Zef Change #17: Fast toString](#17-tostring) | 0.1282 | 2.2664 | 0.1275 | 0.2964 | 0.3235 |
| [Zef Change #18: Array Literal Specialization](#18-arrayliterals) | 0.1295 | 1.6661 | 0.1250 | 0.2979 | 0.2992 |
| [Zef Change #19: Value callOperator Optimization](#19-valuecalloperator) | 0.1208 | 1.6698 | 0.1143 | 0.2713 | 0.2810 |
| [Zef Change #20: Better C++ Configuration](#20-cppoptions) | 0.1186 | 1.6521 | 0.1127 | 0.2635 | 0.2760 |
| [Zef Change #21: No Asserts](#21-noasserts) | 0.1194 | 1.6504 | 0.1127 | 0.2619 | 0.2759 |
| [Zef in Yolo-C++](#yolo) | 0.0233 | 0.3992 | 0.0309 | 0.0784 | 0.0686 |
