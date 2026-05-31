---
id: 864
url: http://www.lix.polytechnique.fr/Labo/Dale.Miller/lProlog/
title: λProlog Home Page
domain: www.lix.polytechnique.fr
source_date: '2026-02-24'
tags:
- lisp
- compilers
- tutorial
- academic-paper
summary: λProlog is a logic programming language based on higher-order intuitionistic
  logic that pioneered support for higher-order abstract syntax (HOAS) and provides
  a strong logical foundation for modular programming, abstract datatypes, and meta-programming.
  The language has multiple active implementations including ELPI (an embeddable interpreter
  in OCaml) and Teyjus (a compiler), along with comprehensive documentation through
  books, tutorials, and video resources. Related tools like Abella, an interactive
  theorem prover, extend λProlog's capabilities for reasoning about specifications
  with binding and have been used for formal work such as π-calculus verification.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# λProlog Home Page

λProlog: Logic programming in higher-order logic
================================================

λProlog is a logic programming language based on higher-order
intuitionistic logic in the style of
Church's [Simple
Theory of Types](http://plato.stanford.edu/entries/type-theory-church/). Such a strong logical foundation provides
λProlog with logically supported notions of modular
programming, abstract datatypes, higher-order programming, and the
[lambda-tree syntax](../papers/mmr-final.pdf) approach to
the treatment of bound variables in syntax. Implementations of
λProlog contain support for simply typed λ-terms and
(subsets) of higher-order unification. As a result, λProlog
was the world's first programming language to directly
support *higher-order abstract syntax (HOAS)*.

Although λProlog was originally designed and implemented in the
late 1980s
(the [first
distributed version](http://www.cs.cmu.edu/afs/cs/project/ai-repository/ai/lang/prolog/impl/prolog/lp/0.html) was written in Prolog in 1988), interest in
the language continues with new implementations and new applications,
particularly in the area of meta-programming.

Current implementations of λProlog
----------------------------------

1. [Enrico
   Tassi](http://www-sop.inria.fr/members/Enrico.Tassi/) and his colleagues are actively
   developing [ELPI](https://github.com/LPCIC/elpi/): an
   embeddable λProlog
   interpreter. [Version
   3.7](https://github.com/LPCIC/elpi/releases/) was released on 24 April 2026.
   The interpreter is written in OCaml and it is described in
   a [paper](https://hal.inria.fr/hal-01176856/) that appeared in
   LPAR 2015. The Coq
   plugin [Coq-ELPI](https://github.com/LPCIC/coq-elpi) makes
   it possible to execute λProlog programs in a Coq environment.
   See
   Enrico's [Tutorial
   on the ELPI programming language](https://lpcic.github.io/coq-elpi/tutorial_elpi_lang.html).
2. [Gopalan Nadathur](http://www.cs.umn.edu/~gopalan/) and
   his team have developed
   the [Teyjus](http://teyjus.cs.umn.edu/) implementation of
   λProlog. [Version
   2.1.1](https://github.com/teyjus/teyjus/releases) was released on 8 February 2023.
   The Teyjus compiler is written in OCaml, and it now supports
   separate computation, effective uses of types at run-time, a
   restriction of unification to the higher-order pattern fragment, etc.
   The ALP Newsletter (March 2010) has an
   [overview
   article](http://www.cs.nmsu.edu/ALP/2010/03/teyjus-a-lprolog-implementation/) about the Teyjus system.
3. [Antonis Stampoulis](http://astampoulis.github.io/)
   has implemented the
   [Makam](http://astampoulis.github.io/makam/)
   metalanguage which is a refinement of
   λProlog. Makam is implemented from scratch in OCaml.

Language documentation
----------------------

Document of λProlog and its applications are available from a
number of sources.

* [Dale Miller](http://www.lix.polytechnique.fr/Labo/Dale.Miller/) and
  [Gopalan Nadathur](http://www-users.cs.umn.edu/~gopalan/)
  have written the
  book [Programming with
  Higher-Order Logic](https://sites.google.com/site/proghol/) (2012) which focuses on using logic programs in
  higher-order logic to provide declarative specifications for a range
  of applications. The book is available from
  [CUP](http://www.cambridge.org/fr/knowledge/isbn/item6687740/),
  [Amazon.com](http://www.amazon.com/Programming-Higher-Order-Logic-Dale-Miller/dp/052187940X/),
  [Amazon.fr](http://www.amazon.fr/Programming-Higher-order-Logic-Dale-Miller/dp/052187940X/),
  and
  [eBooks](http://www.ebooks.com/944612/programming-with-higher-order-logic/miller-dale-nadathur-gopalan/).
* [Zakaria Chihani](http://sites.google.com/site/zakchihani/)
  has a series
  of [video
  tutorials](https://sites.google.com/site/lambdaprologvideotutorial/home/) providing an introduction to λProlog and to
  higher-order logic programming. Some additional YouTube videos
  related to λProlog are
  also [available](https://www.youtube.com/playlist?list=PL6FEY6-VF5VxCB7CLeP_JQE6ZduMnVH3V).
* [Alwen Tiu](http://users.cecs.anu.edu.au/~tiu/) has course material on
  [Programming
  in Higher-Order Logic](http://users.cecs.anu.edu.au/~tiu/teaching/lprolog/index.html) (2009).
* [Amy Felty](http://www.site.uottawa.ca/~afelty/) has written
  a tutorial on
  [λProlog
  and its Applications to Theorem Proving](felty-tutorial-lprolog97.pdf) (1997).
* [Olivier Ridoux](http://www.irisa.fr/lande/ridoux/) has
  written [*Lambda-Prolog de A à Z... ou presque*](Ridoux-HdR-lambda-Prolog-de-A-a-Z.pdf) (163 pages,
  French, 1998).
* [John Hannan](http://www.cse.psu.edu/~hannan/) has written
  a tutorial on [Program
  Analysis in λProlog](http://www.cse.psu.edu/~hannan/papers/plilp-tutorial.ps.gz) at the 1998 PLILP Conference.
* There is a [bibliography](lprolog.html) that includes papers on the
  theory, design, applications, and implementation of λProlog
  from between 1985 and 2000.

[Dale
Miller](http://www.lix.polytechnique.fr/Labo/Dale.Miller/) has written the
book [Proof
Theory and Logic Programming: Computation as Proof Search](https://www.lix.polytechnique.fr/Labo/Dale.Miller/ptlp/) in
which much of the proof theory behind λProlog (and linear
logic extensions of it) are described in detail.

: a prover for λProlog programs
-------------------------------

[Abella](http://abella-prover.org/)
is an interactive theorem prover based on a number of new ways to
exploit inductive and coinductive reasoning with relations.
Abella is well-suited for reasoning about specification that
manipulate objects with binding since it contains the following three
logically motivated features:

1. direct support of λ-tree syntax (sometimes also called HOAS);
2. the ∇-quantifier and nominal variables; and
3. a built-in, *two-level logic approach* to reasoning about
   computation.

In the latter feature, the *specification logic* is used to
specify computations: this logic is a subset of λProlog.
Abella's logic then serves as the *reasoning logic*.
Probably the most elegant formalization of
the π-calculus and its meta-theory is the one written in Abella.
Principle contributors to the implementation of Abella are
[Kaustuv Chaudhuri](http://chaudhuri.info/),
[Andrew
Gacek](http://loonwerks.com/people/andrew-gacek.html), and
[Yuting Wang](http://www.cs.yale.edu/homes/wang-yuting/).

Examples of code
----------------

Examples of λProlog code can be found various places:
in the [Teyjus distribution](http://code.google.com/p/teyjus/);
in an [extraction](proghol/extract.html) from the
book [*Programming
with Higher-Order Logic*](https://sites.google.com/site/proghol/); and in
a [small collection](examples/code.html).
Since the ELPI implementation is written in OCaml and since OCaml can
be compiled into JavaScript, it is possible to execute λProlog
programs in a web browser: for an example, see the online
[MLTS](https://trymlts.github.io/) implementation.



---

Last updated: 26 April 2026
