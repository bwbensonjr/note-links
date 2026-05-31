---
id: 1076
url: https://matt.might.net/articles/implementing-a-programming-language/
title: '7 lines of code, 3 minutes: Implement a programming language'
domain: matt.might.net
source_date: '2026-05-11'
tags:
- compilers
- tutorial
- scheme
- lisp
summary: 'The article demonstrates how to implement a functional, Turing-equivalent
  programming language in just seven lines of code using the eval/apply design pattern,
  a process that takes approximately three minutes. It provides three implementations:
  a minimal 7-line Scheme interpreter, a Racket version, and a more feature-rich 100-line
  interpreter that supports bindings, recursion, side effects, and higher-order functions.
  The author argues that building an interpreter is a valuable learning experience
  that deepens understanding of computation and serves as a scalable foundation for
  developing more complex languages.'
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# 7 lines of code, 3 minutes: Implement a programming language

7 lines of code, 3 minutes: Implement a programming language from scratch
=========================================================================

[[article index](../)]
[]
[[@mattmight](http://twitter.com/mattmight)]
[[rss](../feed.rss)]

Implementing a programming language is an experience no
programmer should go without; the process fosters a deep
understanding of computation, and it's fun!

In this article, I've boiled the entire process down to its
essence: a 7-line interpreter for a functional (Turing-equivalent)
programming language.
It takes about 3 minutes to implement.

This 7-line interpreter showcases a scalable architecture found in many
interpreters--the eval/apply design pattern of
[Structure and Interpretation of Computer Programs](http://www.amazon.com/gp/product/0262510871/ref=as_li_ss_tl?ie=UTF8&tag=mmamzn06-20&linkCode=as2&camp=217145&creative=399369&creativeASIN=0262510871)![](http://www.assoc-amazon.com/e/ir?t=mmamzn06-20&l=as2&o=1&a=0262510871&camp=217145&creative=399369):

[![](http://ws.assoc-amazon.com/widgets/q?_encoding=UTF8&Format=_SL160_&ASIN=0262510871&MarketPlace=US&ID=AsinImage&WS=1&tag=mmamzn06-20&ServiceVersion=20070822)](http://www.amazon.com/gp/product/0262510871/ref=as_li_ss_il?ie=UTF8&tag=mmamzn06-20&linkCode=as2&camp=217145&creative=399369&creativeASIN=0262510871)![](http://www.assoc-amazon.com/e/ir?t=mmamzn06-20&l=as2&o=1&a=0262510871&camp=217145&creative=399369)

In total, there are three language implementations in this article:

* a 7-line, 3-minute interpreter in Scheme;
* a re-implementation in [Racket](http://racket-lang.org/); and
* a 100-line, "1-afternoon" interpreter that implements top-level
  binding forms, explicit recursion, side effects, higher-order
  functions and more!

The last interpreter is a good starting point
for growing a richer language.
