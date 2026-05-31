---
id: 1054
url: https://github.com/coalton-lang/coalton
title: 'GitHub - coalton-lang/coalton: Coalton is an efficient, statically typed functional
  programming language that supercharges Common Lisp. · GitHub'
domain: github.com
source_date: '2026-04-25'
tags:
- github-repo
- common-lisp
- compilers
summary: Coalton is a statically typed functional programming language embedded in
  Common Lisp that enables developers to write type-safe code while maintaining integration
  with the Lisp ecosystem. It features compile-time type checking, pattern matching,
  and algebraic data types, and is currently used in production for defense and quantum
  computing applications. The language is still in pre-1.0 development and is primarily
  tested on SBCL, Allegro CL, and Clozure CL implementations.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - coalton-lang/coalton: Coalton is an efficient, statically typed functional programming language that supercharges Common Lisp. · GitHub

[![Coalton](/coalton-lang/coalton/raw/main/docs/assets/coalton-logotype-gray.svg)](https://coalton-lang.github.io/)

[![Github Workflow Status](https://camo.githubusercontent.com/b01671f49ad1c8aa3bd5c0be3987e60360c527b2454981468cd4d35b13f7c6e2/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616374696f6e732f776f726b666c6f772f7374617475732f636f616c746f6e2d6c616e672f636f616c746f6e2f6d61696e2e796d6c3f6272616e63683d6d61696e)](https://github.com/coalton-lang/coalton/actions/workflows/main.yml)
[![Discord](https://camo.githubusercontent.com/a8b5474e48c47c18653d28736cac00d40582a96feb1abf86f3adfbb395b8c4d8/68747470733a2f2f696d672e736869656c64732e696f2f646973636f72642f3838383139363136383036373139393034363f6c6f676f3d646973636f7264)](https://discord.gg/cPb6Bc4xAH)

Coalton is an efficient, statically typed functional programming language that supercharges Common Lisp.

Coalton integrates directly into Common Lisp:

```
(defpackage #:differentiation
  (:use #:coalton #:coalton-prelude)
  (:local-nicknames (#:sym #:coalton/symbol))
  (:export #:Expr #:EConst #:EVar #:E+ #:E*)
  (:export #:diff #:t #:d/dt))

(in-package #:differentiation)

(named-readtables:in-readtable coalton:coalton)

(coalton-toplevel
  ;; Define a new parametric algebraic data type for simple
  ;; mathematical expressions.
  (define-type (Expr :t)
    "A symbolic expression of basic arithmetic."
    (EConst :t)
    (EVar   sym:Symbol)
    (E+     (Expr :t) (Expr :t))
    (E*     (Expr :t) (Expr :t)))

  ;; The classic `diff` function, in Coalton.
  (declare diff (Num :t => sym:Symbol * Expr :t -> Expr :t))
  (define (diff x f)
    "Compute the derivative of `f` with respect to `x`."
    (match f
      ((EConst _)                       ; c' = 0
       (EConst 0))
      ((EVar s)                         ; x' = 1
       (if (== s x) (EConst 1) (EConst 0)))
      ((E+ a b)                         ; (a+b)' = a' + b'
       (E+ (diff x a) (diff x b)))
      ((E* a b)                         ; (ab)' = a'b + ab'
       (E+ (E* (diff x a) b)
           (E* a          (diff x b))))))

  ;; We can use `t` just fine since Coalton doesn't import `cl:t`.
  (define t (sym:make-symbol "t"))

  (declare d/dt (Num :t => Expr :t -> Expr :t))
  (define (d/dt f)
    "The time derivative operator."
    (diff t f)))
```

It also works directly in the REPL:

```
CL-USER> (in-package #:differentiation)
DIFFERENTIATION> (coalton-toplevel
                   (define (square x) (E* x x)))
;; SQUARE :: ∀ A. ((EXPR A) → (EXPR A))

DIFFERENTIATION> (coalton (d/dt (E+ (square (EVar t)) (EConst 1))))
#.(E+ #.(E+ #.(E* #.(ECONST 1) #.(EVAR |t|))
            #.(E* #.(EVAR |t|) #.(ECONST 1)))
      #.(ECONST 0))
```

Type errors are discovered at compile-time, and errors are printed beautifully without sacrificing Common Lisp's interactive debugging facilities.

```
DIFFERENTIATION> (coalton (d/dt (E+ (EConst 1/2) (EConst 0.5))))
error: Type mismatch
  --> repl:1:32
   |
 1 |  (coalton (d/dt (E+ (EConst 1/2) (EConst 0.5))))
   |                                  ^^^^^^^^^^^^ Expected type '(EXPR FRACTION)' but got '(EXPR F32)'
```

Coalton is currently used in production to build defense and [quantum computing software](https://coalton-lang.github.io/20220906-quantum-compiler/).

Getting Started
---------------

Warning

Coalton has **not** reached "1.0" yet. This means that, from time to time, you may have a substandard user experience. While we try to be ANSI-conforming, Coalton is currently only tested on recent versions of SBCL, Allegro CL, and Clozure CL.

The version of Coalton that may be in Quicklisp may not be up-to-date.

**Prepare**: Install [SBCL](http://www.sbcl.org/platform-table.html) (on macOS with Homebrew: `brew install sbcl`). Install Quicklisp by following instructions [here](https://www.quicklisp.org/beta/#installation). (The step command involving `gpg` is not needed.) After installing Quicklisp, you should have a `quicklisp` folder which will make installing Coalton easier.

**Install**: Clone this repository into a place your Lisp can see (e.g., `~/quicklisp/local-projects/`).

**Use**: Either run `(ql:quickload :coalton)`, or add `#:coalton` to your ASD's `:depends-on` list.

**Test**: Compile the tests with `(ql:quickload :coalton/tests)`, then run the tests with `(asdf:test-system :coalton)`.

Note

Running the Coalton test suite on SBCL requires [GNU MPFR](https://www.mpfr.org/mpfr-current/mpfr.html#Installing-MPFR) in order to run `Big-Float` tests. If you would like to run tests without installing `gnu-mpfr`, you can use Coalton's portable `Big-Float` implementation by running `(pushnew :coalton-portable-bigfloat *features*)` before loading Coalton.

**Learn**: Start with [*Whirlwind Tour of Coalton*](/coalton-lang/coalton/blob/main/docs/manual/site/topics/whirlwind-tour.md), the [language manual](https://coalton-lang.github.io/manual/), and the [standard library reference](https://coalton-lang.github.io/reference/), and then take a peek at the [examples directory](/coalton-lang/coalton/blob/main/examples). It may also be helpful to check out the [introductory blog post](https://coalton-lang.github.io/20211010-introducing-coalton/).

**Open Source Community**: [Awesome Coalton](https://github.com/Jason94/awesome-coalton) has a list of community-built libraries, applications, and examples, that you can use in your own projects or as examples to learn from.

What's Here?
------------

This repository contains the source code to the [Coalton compiler](/coalton-lang/coalton/blob/main/src), and the [standard library](/coalton-lang/coalton/blob/main/library).

It also contains a few example programs, such as:

* Some [simple pedagogical programs](/coalton-lang/coalton/blob/main/examples/small-coalton-programs),
* An [implementation](/coalton-lang/coalton/blob/main/examples/thih) of Jones's *Typing Haskell in Haskell*, and
* An [implementation](/coalton-lang/coalton/blob/main/examples/quil-coalton) of a simple [Quil](https://en.wikipedia.org/wiki/Quil_(instruction_set_architecture)) parser using parser combinators.

Lastly and importantly, we maintain a collection of documentation about Coalton in the [docs](/coalton-lang/coalton/blob/main/docs) directory.

Get Involved
------------

Want to ask a question about Coalton, propose a feature, or share a cool program you wrote? Try posting in the [GitHub Discussions](https://github.com/coalton-lang/coalton/discussions) page!

We welcome contributions of all forms, especially as we stabilize toward a 1.0 release. We would be grateful to receive:

* bug reports (filed as issues),
* bug fixes and typo corrections (filed as pull requests),
* small [example programs](/coalton-lang/coalton/blob/main/examples/small-coalton-programs), and
* user experience troubles.
