---
id: 401
url: https://ada-lang.io/
title: ada-lang.io, an Ada community site
domain: ada-lang.io
source_date: '2025-06-10'
tags:
- security
- compilers
summary: Ada-lang.io is a community site promoting Ada, a programming language designed
  for readable, correct, and performant code with features like design-by-contract
  and formal verification through its SPARK subset. The site emphasizes Ada's 40-year
  track record in critical systems (aerospace, transportation) and provides setup
  instructions using the Alire package manager and toolchain. Key features include
  strong type checking, memory safety, C/C++ interoperability, and the ability to
  formally prove program correctness at various assurance levels.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# ada-lang.io, an Ada community site

Ada Readable, correct, performant Express intent with explicitness, describe properties with predicates and pre/post conditions, and import C/C++ functions or intrinsics. Readable Express intent with explicitness and keywords over symbols and special structures. Express concepts like meaning in integers. Use built-in design by contract with pre/post-conditions and invariants. Model problems with typechecks and range constraints. Correct Build with technology used in 40 years of reliability in planes, trains, and satellites. Use the SPARK subset to formally verify part or all of your program, and integrate existing SPARK crates available in the Alire package manager. Performant Build native applications and take advantage of other libraries through binding to C and C++. Use inline assembly or compiler intrinsics when you need it. Control resources with scope-based resource control (RAII) and your own memory allocators. Set-up environment Package manager + toolchain Download the Alire package manager and install the compiler. Download Alire Download Alire v2.1.0 . Install toolchain alr toolchain --select Select gnat_native and gprbuild. Start coding Create a crate: alr init --bin mycrate && cd mycrate Build the crate: alr build Run your application alr run SPARK From memory safety to functional correctness Gradually adopt the SPARK subset to reach various levels of assurance. Higher levels take more effort, but give more benefits and stronger guarantees. Validates code Restricts Ada packages to the SPARK subset. Avoids side-effects in functions and parameter aliasing. Checks initialization and data flow No uninitialized variables are read or undesired access to globals occurs. Proves the absence of run-time errors No buffer and arithmetic overflow, division by zero, or values out of range, among others, can occur. Ensures key integrity properties Verifies integrity of data and valid state transitions.
