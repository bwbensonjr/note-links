---
id: 803
url: https://github.com/naver/lispe
title: 'GitHub - naver/lispe: An implementation of a full fledged Lisp interpreter
  with Data Structure, Pattern Programming and High level Functions with Lazy Evaluation
  à la Haskell.'
domain: github.com
source_date: '2026-02-09'
tags:
- github-repo
- lisp
- compilers
- haskell
summary: LispE (Lisp Elémentaire) is a compact, multi-platform Lisp dialect that combines
  functional programming, array language features, and object-oriented capabilities
  in a single language. It includes traditional Lisp operators, pattern matching,
  data structures, classes, threading support, and array operators—enabling complex
  tasks like Conway's Game of Life to be solved in minimal code. The project is open-source
  under the BSD 3-Clause License and provides precompiled binaries for Windows and
  macOS, along with documentation and interactive examples to help users explore its
  features.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - naver/lispe: An implementation of a full fledged Lisp interpreter with Data Structure, Pattern Programming and High level Functions with Lazy Evaluation à la Haskell.

LispE: Lisp Elémentaire
=======================

#### (*To test LispE in your browser click:* [HERE](https://naver.github.io/lispe))

Welcome to **Lisp Elémentaire**, a version of Lisp that is both compact and offers a large variety of functional and array language features. The code also comes with a small internal editor from another NAVER's project: [TAMGU](https://github.com/naver/tamgu).

The main goal of **LispE** is to provide a multi-platform language that can harness the power of functional languages with array languages.
The real strength of the Lisp language, of which *LispE* is a dialect, is its very simple but pretty versatile formalism that helps combining all these programming trends together in one single language.

I based a large part of this work on the following article: [The Root of Lisp](http://www.paulgraham.com/rootsoflisp.html).

* The description of the language is available here: [Introduction to LispE](https://github.com/naver/lispe/wiki/1.-Introduction)
* LispE provides a large set of functions, see the [index here](https://github.com/naver/lispe/wiki/Index-of-functions).
* A help to the available functions is here: [LispE Language Description](https://github.com/naver/lispe/wiki/5.-Description-of-Functions,-Operators-and-Libraries)
* The wiki index is here: [HOME](https://github.com/naver/lispe/wiki)
* Artificial Intelligence libraries:
  + [lispe\_torch](https://github.com/naver/lispe/tree/master/lispetorch): encapsulates PyTorch internal libtorch library and SentencePiece
  + [lispe\_gguf](https://github.com/naver/lispe/tree/master/lispegguf): based on `llama.cpp`, load and run gguf models
  + [lispe\_mlx](https://github.com/naver/lispe/tree/master/lispemlx): based on the `MLX` library to access Mac GPUs
  + [lispe\_tiktoken](https://github.com/naver/lispe/tree/master/lispetiktoken): based on the `tiktoken` library by Open AI for tokenization

TEST LispE in your browser
--------------------------

Since LispE is *also* a WASM library: you can test [LispE HERE](https://naver.github.io/lispe).

See also: [Predicate-Based Agent in the Browser (PREDIBAG)](https://github.com/naver/lispe/wiki/6.1.5-PREDIBAG-in-the-Browser)

CHECK binaries
--------------

We have stashed [here](https://github.com/naver/lispe/tree/master/binaries) precompiled versions for Window and Mac OS (including M1)...

A Lisp with all the bells and whistles
--------------------------------------

**LispE** is a true Lisp with all the traditional operators that one can expect from such a language:

```
(cons 'a '(b c)) ; (a b c)
(cdr '(a b c d e)) ; '(b c d e)
(car '(a b c d e)) ; 'a

(+ 10 20 (* 3 4)) ; 42

(list 'a 'b 'c 'd 'e) ; (a b c d e)

; It also provides some built-in types to handle numbers

(setq l1 (integers 1 2 3))
(setq l2 (integers 4 5 6))

; We can then add these lists together
(+ l1 l2) ; 5 7 9

; or strings

(setq s1 (strings "a" "b" "c"))
(setq s2 (strings "d" "e" "f"))

; We can then add these lists together
(+ s1 s2) ; ("ad" "be" "cf")

; Lists are treated as vectors

(@ s1 1) ; "b"
(@ l1 2) ; 3

; You can loop in a list
(loop i s1 (println i))
```

### You can easily run threads

```
; Variables in threadspace are protected against
; value concurrencies.
(threadspace
   (seth titi 10)
   (seth toto (rho 2 10 '(0)))
)

; You declare a thread with the keyword: dethread
(dethread tst(x y)
   (threadspace
      (+= titi x)
      (set@ toto 0 y titi)
   )
)

; We launch 10 threads
(loop i (range 1 10 1)
   (tst (+ i 10) i)
)

; We wait for the threads to terminate
(wait)

; threadspace is actually a specific name space
(space thread
   (println titi) ; 145
   ; Note that the order of values is random, due to thread execution
   (println toto) ; ((0 21 46 34 60 75 108 92 126 145) (0 0 0 0 0 0 0 0 0 0))
)
```

Modern Functional Properties
----------------------------

**LispE** provides an alternative to parentheses with the [composition operator: "."](https://github.com/naver/lispe/wiki/5.-Description-of-Functions,-Operators-and-Libraries#composition-):

```
(sum (numbers 1 2 3)) can be written (sum . numbers 1 2 3)
```

**LispE** provides a powerfull built-in [pattern matching](https://github.com/naver/lispe/wiki/6.1-Pattern-Functions) mechanism:

```
; You can call a function in the pattern definition of the function
(defun checking (x y) (eq 0 (% y x)))

; the argument should be an integer, whose value is a multiple of 15
; The argument is stored in x
(defpat fizzbuzz ((integer_ (checking 15 x))) 'fizzbuzz)
(defpat fizzbuzz ((integer_ (checking 3 x))) 'fizz)
(defpat fizzbuzz ((integer_ (checking 5 x))) 'buzz)
(defpat fizzbuzz (x) x)
(mapcar 'fizzbuzz (range 1 100 1))
```

**LispE** provides also some interesting properties such as: [Data Structures](https://github.com/naver/lispe/wiki/6.7-Data-Structures)

```
; First we define some data structures
; nil or _ this is the same value

(data@ (Point integer_ integer_) (Pixel _ _) (Circle (Point _ _)  _) (Rectangle (Point _ _)  _ nil))

; Then some pattern methods
(defpat Surface ((Circle (Point x y) r)) (* _pi r r))
(defpat Surface ((Rectangle _ h w)) (* h w))
(defpat Surface (true) 'wrong)

(println "Circle:" (Surface (Circle (Point 12 32) 10)))
(println "Rectangle:" (Surface (Rectangle (Point 21 20) 10 20)))

(setq x 10)
(setq y 20)
(setq r 12)

(setq cercle (Circle (Point x y) r))

(println "Circle:" (Surface cercle))
(println "Point:" (Surface (Point 10 20)))
(println "Circle:" (Surface ((atom "Circle") (Point 20 30) 3)))

(data@ Shape (Triangle _) (Square _))

(defpat dimension ( (Shape x))
   (println 'Dimension x)
)
(dimension (Triangle 10))
(dimension (Square 20))
```

**LispE** provides also some OOP such as: [Classes](https://github.com/naver/lispe/wiki/6.21-Classes)

```
; Defines a class named 'truc' with fields x, y, and z
(class@ truc (x y z)

   (defun appel(u)
      (setq x 100)
      (println x y z)
      (+ x y z u)
   )
)

; Defines a class named 'machin' with fields x, y, and z (with a default value of 1).

(class@ machin (x y (z 1))
    ; Defines a method 'appel' that takes one argument 'u'.
    (defun appel(u)
       (println 'machin)(+ x y z u)) 

    ; Defines a method 'configure' that takes one argument 'e'.
    (defun configure(e)
        (setqi x e)
        (setqi v 100))) ; add a new field: `v`
```

But also array language capabilities
------------------------------------

Thanks to an internal structure implemented with [arrays](https://github.com/naver/lispe/wiki/2.3-Lists), we also provide some array operators.

For instance, here is how [Game of life](https://github.com/naver/lispe/wiki/6.20-Conway-Game-of-Life-in-LispE) can be solved in one single instruction:

```
(defmacro ⊖(l n) (rotate l n true))

(defun lifeinit(x y) (rho x y . random_choice (* x y) (integers 0 1) 17))

(setq r (lifeinit 20 40))
(defun gol8(⍵) ((λ(⍺) (| (& (== ⍺ 4) r) (== ⍺ 3))) (⌿ '+ (⌿  '+ (° (λ (x ⍺) (⊖ ⍺ x)) '(1 0 -1) (↑ (λ (x) (⌽ ⍵ x)) '(1 0 -1)))))))

(println . prettify (gol8 r) 20)
```

See: [Array Operators](https://github.com/naver/lispe/wiki/5.3-A-la-APL)

Play with it
------------

Finally, **LispE** can also be used as a *Shell*: [Shell](https://github.com/naver/lispe/wiki/7.-Shell)

Come and discover **LispE**: the **Lisp Elémentaire**.

We provide a fun little program to discover some of the most interesting aspects of LispE: [minizork](https://github.com/naver/lispe/blob/master/examples/patterns/minizork_en.lisp)

*Have a look and try it*

License
-------

BSD 3-Clause License

```
LispE
Copyright (c) 2020-present NAVER Corp.

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions 
are met:

1. Redistributions of source code must retain the above copyright 
notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright 
notice, this list of conditions and the following disclaimer in the 
documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its 
contributors may be used to endorse or promote products derived from 
this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
POSSIBILITY OF SUCH DAMAGE.
```
