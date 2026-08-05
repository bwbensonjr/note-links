---
id: 1257
url: https://nostarch.com/art-64-bit-assembly-v2
title: The Art of 64-Bit Assembly, Volume 2 | No Starch Press
domain: nostarch.com
source_date: '2026-08-05'
tags:
- nonfiction-book
- tutorial
- c
- compilers
summary: The Art of 64-Bit Assembly, Volume 2 is an advanced programming book by Randall
  Hyde that teaches how to implement complex programming constructs like object-oriented
  programming, exception handling, and concurrency at the machine-instruction level
  in x86-64 assembly. Rather than relying on theoretical explanations, the book dissects
  real-world implementations used by Windows and other systems, showing readers how
  to build vtables, closures, coroutines, and concurrent programs directly in MASM
  assembly language. The book is designed for programmers who already know assembly
  and want to move beyond surface-level understanding to truly grasp how the runtime
  and high-level language features actually work beneath the surface.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# The Art of 64-Bit Assembly, Volume 2 | No Starch Press

[![The Art of 64-Bit Assembly, Volume 2](https://nostarch.com/sites/default/files/styles/uc_product/public/art-of-64-bit-assembly-v2_frontcover.jpg?itok=Zp0NJ4P6 "The Art of 64-Bit Assembly, Volume 2")](https://nostarch.com/sites/default/files/styles/uc_product_full/public/art-of-64-bit-assembly-v2_frontcover.jpg?itok=Y39YsZyt "The Art of 64-Bit Assembly, Volume 2")

The Art of 64-Bit Assembly, Volume 2
====================================

Machine-Level OOP, Exceptions, and Concurrency

by Randall Hyde

Available June 2026, 792 pp.

ISBN-13:

9781718504349

* [Contents](#content)

[Download Chapter 1: Advanced Macros](/download/samples/art-64-bit-assembly-v2_chapter-1.pdf)

You can ask an AI to explain how vtables work in x86. It will give you something that sounds right. What it won’t give you is what Windows actually expects the vtable to look like, why method dispatch behaves the way it does at the instruction level, or what breaks when you deviate from convention. This volume of *The Art of 64-Bit Assembly* closes the gap between a plausible explanation and genuine understanding.

Every chapter takes a construct you’ve used in C++, Python, or Rust, strips away the runtime, and rebuilds it from scratch in MASM, running under Windows. Objects, exceptions, closures, coroutines, concurrency: Each is dissected at the instruction level, with every decision made visible and explicit.

What you’ll build:

* Object-oriented programs in MASM: vtables, method dispatch, and inheritance, from scratch by hand
* Windows structured exception handling (SEH) installed and managed at the instruction level
* Thunks, closures, and iterators that behave like higher-order functions
* Coroutines, generators, and fibers without resorting to HLL code
* Concurrent programs with real synchronization primitives, directly from assembly
* Unicode string handling done correctly, at the level where most code gets it wrong
* Domain-specific macro languages inside MASM, built from first principles

If you already know assembly and want to stop taking the hard parts on faith, this is the book.

Author Bio

**Randall Hyde** has spent decades writing assembly for medical devices, nuclear systems, and embedded hardware where correctness is not optional. He taught assembly language programming at the university level and is the author of *The Art of Assembly Language*, *The Art of ARM Assembly*, and the Write Great Code series, all from No Starch Press.

Table of contents

Acknowledgments  
Introduction

Chapter 1: Advanced Macros  
Chapter 2: Unicode Strings  
Chapter 3: Transcendental Functions  
Chapter 4: Advanced Procedures  
Chapter 5: Concurrent Programming  
Chapter 6: Object-Oriented Programming With MASM  
Chapter 7: Exception Handling  
Chapter 8: Thunks and Closures  
Chapter 9: Advanced Parameter Implementation  
Chapter 10: Iterators  
Chapter 11: Coroutines, Generators, and Fibers

Appendix A: ASCII Character Set  
Appendix B: Glossary  
Appendix C: Installing and Using Visual Studio

Index

[**View the Copyright page**](download/resources/art-64-bit-assembly-v2_copyright.pdf)  
[**View the detailed Table of Contents**](/download/resources/art-64-bit-assembly-v2_TOC.pdf)  
[**View the Index**](/download/resources/art-64-bit-assembly-v2_index.pdf)
