---
id: 205
url: http://users.rcn.com/david-moon/Lunar/introduction.html
title: "Lunar\n: \nIntroduction"
domain: users.rcn.com
source_date: '2025-10-14'
tags:
- lisp
- compilers
summary: Lunar is a programming language designed by David A. Moon that distills 40
  years of programming experience into a simplified yet powerful language. It reimagines
  Lisp by stripping away what Moon considers historical accidents (like CONS-based
  data structures and traditional syntax) while retaining essential principles, prioritizing
  simplicity, readability, extensibility, and mathematical correctness. The language
  emphasizes clean design through features like hygienic macros, inferred typing,
  immutable data structures by default, and indentation-based syntax rather than punctuation.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Lunar
: 
Introduction

Lunar Programming Language
==========================

by David A. Moon  
January 2017 - January 2018  
  


---

  

Introduction
------------

Lunar
is my attempt to distill 40 years of programming language experience
into the "best" language I can come up with. I hope that this will bring
some forgotten ideas back into the spotlight of public attention.

Lunar
can also be viewed as an exploration of what Lisp would be like if
pared down to what I view as its essential principles, with historical
accidents and dead-ends stripped away. Perhaps shockingly to some, I
view both Lisp's syntax and its data structures' basis in CONS as two of
those accidents.

I have been developing
Lunar
as a hobby, with the idea of creating a programming language which
does everything the right way for once.
You know it is right when both simplicity and power are maximized,
while at the same time confusion and the need for kludges are minimized.

I have adopted good ideas wherever I find them, and ruthlessly rooted out
bad ideas, whether my own or others'.

Those familiar with my previous PLOT (Programming Language for Old Timers)
will find that
Lunar
is similar, but significantly simplified and with less redundancy.

You will not find it possible to read and understand this book in front-to-back
linear order. Many concepts are used informally before they are defined.
Feel free to jump around.

### Principles

Everything about the language is to be defined in the language itself. The
language is to be fully extensible by users, with no magic constructs that are
built-in and not replicable as user-defined extensions. Of course to be
implementable this requires bootstrapping.

Emphasize cleanliness, readability, flexibility, and extensibility.

Memory management is too important for both safety and performance to
be left in the hands of programmers.

Define as much as possible by the binding of names to values. There is
only one namespace, with static nesting of scopes.

Discourage assignment, and make it syntactically obvious where it is
allowed or occurs. But do not forbid it.

For similar reasons, use constant (aka immutable) data structures primarily, but also
allow for variable (aka mutable) versions of most data structures.

Discourage unnecessary type declarations, but allow them where needed.
Most type information can easily be inferred by the compiler.

Use hygienic macros pervasively.

Language-enforced access control is incompatible with macros and with
debugging within the language, so do not attempt to provide that type of
feature. Use naming conventions and social enforcement instead.

Arithmetic operations must always produce mathematically correct results
or an error signal.
No insanity like (x + y) / 2 is sometimes a negative number when both x and
y are positive.

Strive for programs to be readable yet concise. Hence use infix syntax,
case-insensitive names, and nesting structure indicated by indentation
rather than punctuation.

Minimize the use of punctuation and maximize the use of whitespace, for
readability.

Avoid abbreviation, but when you must abbreviate, do it consistently.

Anything that must be intrinsically known to the compiler is explicitly
marked.

Strive for simple concepts that combine in powerful ways. Keep removing
unnecessary complex features until no more can be removed.

Take full advantage of classes and methods.

Do not conflate the concepts of class, module, scope, and encapsulation.
Use simple concepts that combine in powerful ways instead of one overly
powerful concept that tries to do everything.

I am not attempting to address issues of parallel computation, nor
take advantage of special-purpose hardware, at this time.

### Examples

Here are some small code examples to whet your appetite.

The classic Fibonacci series:

```
def fibonacci(n)
  if n < 2 then 1
  else fibonacci(n - 1) + fibonacci(n - 2)
```

Greatest common divisor, from the *Lisp 1.5 Programmer's Manual*:

```
def gcd(x integer, y integer)
  if x > y then gcd(y, x)
  else if y mod x = 0 then x
  else gcd(y mod x, x)
```

Construct an integer from a string:

```
;; Construct an integer from a string in any base between 2 and 36 (default base 10)
def integer(s string, named: base = 10 2..36)
  ;; Get the digit value of a character, assuming ASCII (Unicode) encoding
  def digit(char '0'..'9') char.code - '0'.code
  def digit(char 'A'..'Z') char.code - 'A'.code + 10
  def digit(char 'a'..'z') char.code - 'a'.code + 10
  def digit(char) 999   ; force error("'$char' is not a digit in base $base")

  ;; Parse optional leading sign and digits
  def result := 0
  def sign   := false
  def digits := false
  for char in s
    if char = '-' and not sign
      sign := -1
    else if char = '+' and not sign
      sign := +1
    else
      def dig = digit(char)
      if dig < base
        result := result * base + dig
      else
        error("'$char' is not a digit in base $base")
      sign := sign or 1
      digits := true

  ;; Assemble the answer
  if digits
    result * sign
  else
    error("\"$s\" does not contain any digits")
```

See [Stacks](collection_types.html#stacks)
for an adjustable-length array example.

see [Thrilling Examples](thrilling_examples.html#)
for some larger examples.

[Previous page](index.html)   [Table of Contents](index.html)   [Next page](organizing_mechanisms.html)

---

[![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/)  
Lunar
by David A. Moon
is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
