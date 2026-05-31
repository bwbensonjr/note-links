---
id: 23
url: https://people.mpi-sws.org/~rossberg/1ml/
title: 1ML - core and modules united
domain: people.mpi-sws.org
source_date: '2026-01-09'
tags:
- compilers
- academic-paper
summary: 1ML is a redesigned programming language that unifies ML's core and module
  layers into a single, consistent language by making modules first-class values.
  This eliminates the syntactic and semantic duplication between the two layers while
  improving expressiveness, allowing functions, functors, and type constructors to
  be treated uniformly. The language is grounded in System F-omega and includes a
  prototype interpreter, with research papers published between 2015-2018 describing
  the design and extensions like effect polymorphism.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# 1ML - core and modules united

1ML — core and modules united
=============================

Description
-----------

1ML is a reboot of ML starting from first-class modules, and unifies core and module layer into one small and consistent language.
It is described in the following papers:

* Andreas Rossberg. [1ML — core and modules united](1ml.pdf). ICFP 2015.
* Andreas Rossberg. [1ML — core and modules united (Extended)](1ml-extended.pdf). 2015. Expanded version including Technical Appendix.
* Andreas Rossberg. [1ML — core and modules united](1ml-jfp.pdf). JFP 28, 2018. Revised and expanded version of ICFP paper, including most of the Technical Appendix.
* Andreas Rossberg. [1ML with Special Effects](1ml-effects.pdf). WadlerFest 2016. Extends 1ML with effect polymorphism and generativity polymorphism.

Here is the abstract from the original paper:

*ML is two languages in one: there is the core, with types and expressions, and there are modules, with signatures, structures and functors.
Modules form a separate, higher-order functional language on top of the core.
There are both practical and technical reasons for this stratification;
yet, it creates substantial duplication in syntax and semantics,
and it reduces expressiveness.
For example, selecting a module cannot be made a dynamic decision.
Language extensions allowing modules to be packaged up as first-class values have been proposed and implemented in different variations.
However, they remedy expressiveness only to some extent, are syntactically cumbersome, and do not alleviate redundancy.We propose a redesign of ML in which modules are truly first-class values,
and core and module layer are unified into one language.
In this "1ML",
functions, functors, and even type constructors are one and the same construct;
likewise, no distinction is made between structures, records, or tuples.
Or viewed the other way round, everything is just ("a mode of use of") modules.
Yet, 1ML does not require dependent types,
and its type structure is expressible in terms of plain System Fω,
in a minor variation of our F-ing modules approach.
We introduce both an explicitly typed version of 1ML,
and an extension with Damas/Milner-style implicit quantification.
Type inference for this language is not complete,
but, we argue, not substantially worse than for Standard ML.An alternative view is that 1ML is a user-friendly surface syntax for System Fω that allows combining term and type abstraction in a more compositional manner than the bare calculus.*

Download
--------

A simple prototype interpreter allows playing with small examples (it does not yet implement the extension with effect polymorphism from the latest paper):

* [Version 0.1](1ml-0.1.zip)
* [GitHub repository](https://github.com/rossberg/1ml)

You will need OCaml 4.02 and Make to build it. Please see the README file for basic documentation.

2015-2017 :: andreas rossberg :: by courtesy of [mangrigdesign](http://www.mangrigdesign.de)
:: [imprint](https://imprint.mpi-klsb.mpg.de/sws/people/rossberg)
:: [data protection](https://data-protection.mpi-klsb.mpg.de/sws/people/rossberg)
