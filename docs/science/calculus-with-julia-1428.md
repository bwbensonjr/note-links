---
id: 1428
url: https://jverzani.github.io/CalculusWithJuliaNotes.jl/
title: Calculus with Julia
domain: jverzani.github.io
source_date: '2026-10-12'
tags:
- mathematics
- tutorial
summary: These notes teach calculus through the Julia programming language, emphasizing
  the graphical and numerical perspectives, with some algebraic and symbolic treatment
  added on. They take a "rule of four" approach and use a small set of computational
  actions of the form action(function, arguments...) to tackle introductory calculus
  problems. The notes are presented as a Quarto book, come with a companion Julia
  package (CalculusWithJulia), and include try-it-yourself questions at the end of
  each page.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-5-5
---

# Calculus with Julia

Preface
=======

![](misc/logo.png)

Calculus with Julia

---

This is a set of notes for learning [calculus](http://en.wikipedia.org/wiki/Calculus) using the [`Julia`](https://julialang.org) language. `Julia` is an open-source programming language with an easy to learn syntax that is well suited for this task.

Read “[Getting started with Julia](./misc/getting_started_with_julia.html)” to learn how to install and customize `Julia` for following along with these notes. Read “[Julia interfaces](./misc/julia_interfaces.html)” to review different ways to interact with a `Julia` installation.

Since the mid 90s there has been a push to teach calculus using many different points of view. The [Harvard](http://www.math.harvard.edu/~knill/pedagogy/harvardcalculus/) style rule of four says that as much as possible the conversation should include a graphical, numerical, algebraic, and verbal component. These notes use the programming language [Julia](http://julialang.org) to illustrate the graphical, numerical, and, at times, the algebraic aspects of calculus.

There are many examples of integrating a computer algebra system (such as `Mathematica`, `Maple`, or `Sage`) into the calculus conversation. Computer algebra systems can be magical. The popular [WolframAlpha](http://www.wolframalpha.com/) website calls the full power of `Mathematica` while allowing an informal syntax that is flexible enough to be used as a backend for Apple’s Siri feature. (“Siri what is the graph of x squared minus 4?”) For learning purposes, computer algebra systems model very well the algebraic/symbolic treatment of the material while providing means to illustrate the numeric aspects. These notes are a bit different in that `Julia` is primarily used for the numeric style of computing and the algebraic/symbolic treatment is added on. Doing the symbolic treatment by hand can be very beneficial while learning, and computer algebra systems make those exercises seem kind of redundant, as the finished product can be produced much more easily.

Our real goal is to get at the concepts using technology as much as possible without getting bogged down in the mechanics of the computer language. We feel `Julia` has a very natural syntax that makes the initial start up not so much more difficult than using a calculator, but with a language that has a tremendous upside. The notes restrict themselves to a reduced set of computational concepts. This set is sufficient for working many of the problems in calculus, but do not cover thoroughly many aspects of programming. (Those who are interested can go off on their own and `Julia` provides a rich opportunity to do so.) Within this restricted set, are operators that make many of the computations of calculus reduce to a function call of the form `action(function, arguments...)`. With a small collection of actions that can be composed, many of the problems associated with introductory calculus can be attacked.

These notes are presented in pages covering a fairly focused concept, in a spirit similar to a section of a book. Just like a book, there are try-it-yourself questions at the end of each page. All have a limited number of self-graded answers. These notes borrow ideas from many sources, for example Strang ([n.d.](references.html#ref-Strang)), Knill ([n.d.](references.html#ref-Knill)), Schey ([1997](references.html#ref-Schey)), Hass et al. ([2018](references.html#ref-Thomas)), Rogawski et al. ([2019](references.html#ref-RogawskiAdams)), Angenent ([2012](references.html#ref-Angenent)), several Wikipedia pages, and other sources.

These notes are accompanied by a `Julia` package `CalculusWithJulia` that provides some simple functions to streamline some common tasks and loads some useful packages that will be used repeatedly.

These notes are presented as a Quarto book. To learn more about Quarto books visit <https://quarto.org/docs/books>.

Compiling these notes into a `pdf` file with Quarto is possible with some piecing together of parts. The result is less than optimal and also quite large.

[Download pdf version](https://www.dropbox.com/scl/fi/vv8ee9a5xb9qbsw87f3bl/CalculusWithJulia.pdf?rlkey=u7ambk19sowelxtgiaosjozzo&st=i0hxwx29&dl=0)

To *contribute* – say by suggesting additional topics, correcting a mistake, or fixing a typo – click the “Edit this page” link and join the list of [contributors](https://github.com/jverzani/CalculusWithJuliaNotes.jl/graphs/contributors). Thanks to all contributors.

A *very* special thanks goes out to `@fangliu-tju` for their careful and most-appreciated proofreading and error spotting spread over a series of PRs.

Running Julia
-------------

For individual users `Julia` is installed quite easily with the `juliaup` utility or by other means. There are some brief installation notes in the overview of `Julia` commands.

---

Calculus with Julia version 0.27, produced on August 31, 2026.

Angenent, Sigurd. 2012. *Wisconsin Calculus*. Https://github.com/SigurdAngenent/WisconsinCalculus/tree/master.

Hass, Joel R., Christopher E. Heil, and Maurice D. Weir. 2018. *Thomas’ Calculus*. Pearson.

Knill, Oliver. n.d. *Some Teaching Notes*. <https://people.math.harvard.edu/~knill/teach/index.html>.

Rogawski, Jon, Colin Adams, and Robert Franzosa. 2019. *Calculus*. Macmillan.

Schey, H. M. 1997. *Div, Grad, Curl, and All That*. W.W. Norton.

Strang, Gilbert. n.d. *Calculus*. Wellesley-Cambridge Press. <https://ocw.mit.edu/courses/res-18-001-calculus-online-textbook-spring-2005/>.
