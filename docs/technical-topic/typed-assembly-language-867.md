---
id: 867
url: https://www.cs.cornell.edu/talc/
title: Typed Assembly Language
domain: www.cs.cornell.edu
source_date: '2026-02-24'
tags:
- compilers
- academic-paper
- security
- c
summary: Typed Assembly Language (TAL) is an extension of traditional assembly language
  that incorporates type annotations and memory management to guarantee memory safety,
  control flow safety, and type safety while remaining flexible for compiler optimizations.
  TAL can express complex programming features like records, arrays, higher-order
  functions, exceptions, and modules, making it an ideal target for secure compilers
  and safe mobile code applications. The researchers have implemented TALx86, a TAL
  variant for Intel IA32 architecture, and developed a Popcorn compiler that translates
  safe C-like code into TALx86.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Typed Assembly Language

|  |
| --- |
| Typed Assembly Language |

|  |  |  |
| --- | --- | --- |
| Typed Assembly Language (TAL) extends traditional untyped assembly languages with typing annotations, memory management primitives, and a sound set of typing rules.  These typing rules guarantee the memory safety, control flow safety, and type safety of TAL programs.  Moreover, the typing constructs are expressive enough to encode most source language programming features including records and structures, arrays, higher-order and polymorphic functions, exceptions, abstract data types, subtyping, and modules.  Just as importantly, TAL is flexible enough to admit many low-level compiler optimizations.  Consequently, TAL is an ideal target platform for type-directed compilers that want to produce verifiably safe code for use in secure mobile code applications or extensible operating system kernels.  We have implemented a variant of TAL for Intel's IA32 architecture called TALx86, and have written a compiler for a safe C-like language called Popcorn to TALx86.   |  |  | | --- | --- | | tal-logo-medium.gif (2647 bytes) | ***What do you want to type check today?*** |       [TAL Overview](overview.html) [Papers](papers.html) [Software](releases.html) [Members](members.html) [Related Projects](related.html) |

|  |
| --- |
|  |
