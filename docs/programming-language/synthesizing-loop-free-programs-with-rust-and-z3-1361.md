---
id: 1361
url: http://fitzgeraldnick.com/2020/01/13/synthesizing-loop-free-programs.html
title: Synthesizing Loop-Free Programs with Rust and Z3
domain: fitzgeraldnick.com
source_date: '2026-09-15'
tags:
- rust
- tutorial
- compilers
- academic-paper
summary: This article explains program synthesis—the automatic generation of programs
  from specifications—focusing on a specific approach called counterexample-guided
  iterative synthesis (CEGIS) for loop-free, component-based programs. The author
  walks through the motivation for program synthesis (such as solving tricky bit manipulation
  problems or automatically generating compiler optimizations), provides a detailed
  explanation of the CEGIS technique, and shares a Rust implementation using the Z3
  SMT solver to demonstrate how the approach works with practical examples. While
  the technique shows promise, the article also notes performance challenges when
  applied to more complex benchmark problems compared to results reported in academic
  literature.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Synthesizing Loop-Free Programs with Rust and Z3

Automatically finding a program that implements a given specification is called
*program synthesis*. The main difficulty is that the search space is huge: the
number of programs of size \(n\) grows exponentially. Naïvely enumerating
every program of size \(n\), checking whether each one satisfies the
specification, and then moving on to programs of size \(n+1\) and so on
doesn’t scale. However, the field has advanced by using smarter search
techniques to prune the search space, leveraging performance improvements in SMT
solvers, and at times limiting the scope of the problem.

In this post, I’ll explain one approach to modern program synthesis:
counterexample-guided iterative synthesis of component-based, loop-free
programs, as described in [*Synthesis of Loop-Free Programs* by Gulwani et
al](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/12/pldi11-loopfree-synthesis.pdf). We’ll dissect exactly what each of those terms
mean, and we’ll also walk through an implementation written in Rust that uses
[the Z3 solver](https://github.com/Z3Prover/z3).

My hopes for this post are two-fold:

1. I hope that people who are unfamiliar with program synthesis — just
   like I was not too long ago — get a little less unfamiliar and learn
   something new about the topic. I’ve tried to provide many examples, and break
   down the dense logic formulas from the paper into smaller, approachable
   pieces.
2. I hope that folks who are already familiar with this kind of program
   synthesis can help me diagnose some performance issues in the implementation,
   where I haven’t been able to reproduce the synthesis results reported in the
   literature. For some of the more difficult benchmark problems, the
   synthesizer fails to even find a solution before my patience runs out.

Table of Contents
-----------------



* [Motivation](#motivation)
* [An Overview of Our Task](#an-overview-of-our-task)
* [Formalizing the Problem](#formalizing-the-problem)
* [A Brief Introduction to SMT Solvers](#a-brief-introduction-to-smt-solvers)
* [Counterexample-Guided Iterative Synthesis](#counterexample-guided-iterative-synthesis)
  + [CEGIS with Components](#cegis-with-components)
    - [Verifying a Component-Based Program](#verifying-a-component-based-program)
    - [Finite Synthesis of a Component-Based Program](#finite-synthesis-of-a-component-based-program)
* [Implementation](#implementation)
  + [Program Representation](#program-representation)
  + [Building Programs](#building-programs)
  + [Defining Components](#defining-components)
  + [Specifications](#specifications)
  + [The Synthesizer](#the-synthesizer)
  + [Location Mappings](#location-mappings)
  + [Verification](#verification)
  + [Finite Synthesis](#finite-synthesis)
  + [The CEGIS Loop](#the-cegis-loop)
* [Results](#results)
* [Conclusion](#conclusion)
* [References](#references)

Motivation
----------

Why write a program that writes other programs for me? Am I just too lazy to
write them myself? Of course I am. However, there are many valid reasons why a
person who is not as lazy as I am might want to synthesize programs.

Some programs are quite tricky to write correctly by hand, and a program
synthesizer might succeed where you or I might fail. Quick! How do you isolate
the rightmost zero bit in a word using only three bit manipulation
instructions?!

```
              ,--- The rightmost zero bit.
              |
              V
Input:  011010011

Output: 000000100
              ^
              |
              '--- Only that bit is set.
```

Did you get it yet?

…

Okay, here’s the answer:

```
isolate_rightmost_zero_bit(x): // x = 011010011
    a ← not x                  // a = 100101100
    b ← add 1, x               // b = 011010100
    c ← and a, b               // c = 000000100
    return c
```

Our program synthesizer will find *a* solution in under a second, and that
*minimal-length* solution in a minute or so. It would take me quite a while
longer than that to do the same by hand. We’ll return to this problem throughout
the rest of this post, and use it as a running example.

Another reason to use a program synthesizer might be that we need to write many
more programs than we have time to write by hand. Take for example a compiler’s
[peephole optimizer](https://en.wikipedia.org/wiki/Peephole_optimization): it considers a sliding window of
instruction sequences, and for each sequence, it checks if it knows of an
equivalent-but-faster-or-smaller instruction sequence. When it does know of a
better instruction sequence, it replaces the original instructions with the
better ones.

Peephole optimizers are typically constructed from pattern-matching rules that
identify suboptimal instruction sequences paired with the improved instruction
sequence to replace matches with:

```
new PeepholeOptimizer(
    pattern0 → replacement0
    pattern1 → replacement1
    pattern2 → replacement2
    // ...
    patternn → replacementn
)
```

Each `replacementi` is a little, optimized
mini-program. If we were writing a new peephole optimizer from scratch and by
hand, we would have to write \(n\) optimized mini-programs ourselves. And
\(n\) can be big: LLVM’s `InstCombine` peephole optimizer has over 1,000
pattern-and-replacement pairs. Even half that many is way more than I want to
write myself.

Instead of writing those optimized mini-programs by hand, we can use each
original instruction sequence as a specification, feed it into a program
synthesizer, and see if the synthesizer can find the optimal instruction
sequence that does the same thing. Finally, we can use all these original
instruction sequences and their synthesized, optimal instruction sequences as
pattern-and-replacement pairs to automatically construct a peephole optimizer!
This idea was first proposed by Bansal et al in [*Automatic Generation of
Peephole Superoptimizers*](https://theory.stanford.edu/~aiken/publications/papers/asplos06.pdf).

> ***Edit:** [John Regehr](https://twitter.com/johnregehr) pointed out to me
> that this idea has been floating around since much earlier than 2006, when the
> Bansal et al paper was published. He pointed me to [The Design and Application
> of a Retargetable Peephole Optimizer by Davidson et
> al](https://dl.acm.org/doi/10.1145/357094.357098) from 1980 as an example, but
> noted that even this wasn’t the first time it came up.*

An Overview of Our Task
-----------------------

Program synthesis is the act of taking a specification, and automatically
finding a program that satisfies it. In order to make the problem a little more
tractable, we’re limiting its scope in two ways:

1. **Loop-free:** We are only synthesizing programs without loops.
2. **Component-based:** We are only synthesizing programs that can be expressed
   as the composition of a given library of components.

The loop-free limitation is not very limiting for many use cases. For example,
peephole optimizers often don’t consider instruction sequences that span across
loop boundaries.

Component-based synthesis means that rather than synthesizing programs using any
combination of any number of the target language’s expressions, the synthesizer
is given a library of components and synthesizes programs that use each of those
components exactly once. The synthesizer rearranges the components, rewiring
their inputs and outputs, until it finds a configuration that satisfies the
specification.

That is, given a library of \(N\) components, it constructs a program of the
form

```
synthesized_program(inputs...):
    temp0 ← component0(params0...)
    temp1 ← component1(params1...)
    // ...
    tempN-1 ← componentN-1(paramsN-1...)
    return tempN-1
```

where each parameter in `paramsi` is either a
`tempj` variable defined earlier in the program or one of
the original `inputs`.

For example, given the two components

* `f(a)`
* `g(a, b)`

and an input parameter `x`, the synthesizer can construct any of the following
candidate programs (implicitly returning the variable defined last):

```
a ← g(x, x)
b ← f(x)
```

or

```
a ← g(x, x)
b ← f(a)
```

or

```
a ← f(x)
b ← g(x, x)
```

or

```
a ← f(x)
b ← g(a, x)
```

or

```
a ← f(x)
b ← g(x, a)
```

or

```
a ← f(x)
b ← g(a, a)
```

That’s it. That’s *all* of the programs it can possibly construct given just
those two components.

The synthesizer *cannot* construct the following program, because it doesn’t use
every component:

```
a ← f(x)
```

And the synthesizer *cannot* construct this program, because it uses the `f`
component more than once:

```
a ← f(x)
b ← f(a)
c ← g(b, b)
```

And, finally, it *cannot* construct this last program, because this last program
uses some function `h` that is not a component in our given library:

```
a ← f(x)
b ← h(a, x)
```

The following table describes some of the properties of component-based
synthesis by comparing it to the fully general version of program synthesis:

|  | General Synthesis | Component-Based Synthesis |
| --- | --- | --- |
| Shape of Synthesized Programs | Using any number of any of the target language's expressions | Using only the components in the library |
| Size of Synthesized Programs | Varies | Exactly the size of the library, since each component in the library is used exactly once |

In our synthesizer, the components will be functions over fixed bit-width
integers (also known as “bitvectors” in the SMT solver parlance) and they will
correspond to a single instruction in our virtual instruction set: `add`, `and`,
`xor`, etc. But in principle they could also be higher-level functions or
anything else that we can encode in SMT queries. More on SMT queries later.

While component-based synthesis makes the synthesis problem easier, it does
foist a decision on us each time we invoke the synthesizer: we must choose the
library of available components. Each component is used exactly once in the
synthesized program, but if we want to synthesize a program that performs
multiple additions, we can include multiple instances of the `add` component in
the library. Too few components, and the synthesizer might not be able to find a
solution. Too many components will slow down the synthesizer, and let it
generate non-optimal programs that potentially contain dead code.

To summarize, in component-based synthesis of loop-free programs, our
synthesizer’s inputs are

* a specification, and
* a library of components.

Its output is a program that satisfies the specification, expressed in terms of
the given components, or an error if can’t find such a program.

Formalizing the Problem
-----------------------

In order to synthesize a program, we need a specification describing the desired
program’s behavior. The specification is a logical expression that describes the
output when the program is given these inputs.

We define the specification with:

* \(\vec{I}\) as the program inputs,
* \(O\) as the program output, and
* \(\phi\_\mathrm{spec}(\vec{I}, O)\) as the expression relating the inputs to
  the output. This expression should be true when \(O\) is the desired output
  of running the program on inputs \(\vec{I}\).

The library of components we’re given is a multi-set of specifications
describing each component’s behavior. Each component specification comes with
how many inputs it takes (e.g. an `add(a, b)` component takes two inputs, and a
`not(a)` component takes one input) as well as a logical formula relating the
component’s inputs to its output. The component inputs, output, and expression
all have similar notation to the program specification, but with a subscript:

* \(\vec{I}\_i\) is the \(i^\mathrm{th}\) component’s input variables,
* \(O\_i\) is the \(i^\mathrm{th}\) component’s output variable, and
* \(\phi\_i(\vec{I}\_i, O\_i)\) is the logical expression relating the
  \(i^\mathrm{th}\) component’s inputs with its output.

We define \(N\) as the number of components in the library.

For our isolating-the-rightmost-zero-bit example, what is the minimal components
library we could give to the synthesizer, while still preserving its ability to
find our desired solution? It would be a library consisting of exactly the
components that correspond to each of the three instructions in the solution
program: a `not`, an `add1`, and an `and` component.

| Component | Definition | Description |
| --- | --- | --- |
| \( \phi\_0(I\_0, O\_0) \) | \( O\_0 = \texttt{bvadd}(1, I\_0) \) | The add-one operation on bitvectors. |
| \( \phi\_1(I\_1, I\_2, O\_1) \) | \( O\_1 = \texttt{bvand}(I\_1, I\_2) \) | The bitwise and operation on bitvectors. |
| \( \phi\_2(I\_3, O\_2) \) | \( O\_0 = \texttt{bvnot}(I\_3) \) | The bitwise not operation on bitvectors. |

Program synthesis can be expressed as an *exists-forall* problem: we want to
find whether there *exists* some program \(P\) that satisfies the
specification *for all* inputs given to it and outputs it returns.

> \(
> \begin{align}
> & \exists P:
> \\ & \quad \forall \vec{I},O:
> \\ & \quad \quad P(\vec{I}) = O \implies \phi\_\mathrm{spec}(\vec{I}, O)
> \end{align}
> \)

Let’s break that down and translate it into English:

|  |  |
| --- | --- |
| \( \exists P \) | There *exists* some program \(P\), such that |
| \( \forall \vec{I},O \) | *for all* inputs \(\vec{I}\) and output \(O\), |
| \( P(\vec{I}) = O \) | if we run the program on the inputs \(\vec{I}\) to get the output \(O\), |
| \( \implies \) | then |
| \( \phi\_\mathrm{spec}(\vec{I}, O) \) | our specification \(\phi\_\mathrm{spec}\) is satisfied. |

This *exists-forall* formalization is important to understand because our
eventual implementation will query the SMT solver (Z3 in our case) with pretty
much this formula. It won’t be *exactly* the same:

* \(P\) is an abstraction that’s hiding some details about components,
* there are a few algebraic transformations we will perform, and
* we won’t pose the whole problem to the solver in a single query all at once.

Nonetheless, the implementation follows from this formalization, and we won’t
get far if we don’t have a handle on this.

A Brief Introduction to SMT Solvers
-----------------------------------

We can’t continue any further without briefly discussing SMT solvers and their
capabilities. SMT solvers like Z3 take a logical formula, potentially containing
unbound variables, and return whether it is:

* *Satisfiable:* there is an assignment to the unbound variables that makes the
  assertions true, and also here is a model describing those assignments.
* *Unsatisfiable:* the formula’s assertions are false; there is no assignment of
  values to the unbound variables that can make them true.

SMT solvers take their assertions in a Lisp-like input language called
[SMT-LIB2](http://smtlib.cs.uiowa.edu/). Here is an example of a satisfiable SMT query:

```
;; `x` is some integer, but we don't know which one.
(declare-const Int x)

;; We do know that `x + 2 = 5`, however.
(assert (= 5 (+ x 2)))

;; Check whether the assertions are satisfiable. In
;; this case, they should be!
(check-sat)

;; Get the model, which has assignments to each of
;; the free variables. The model should report that
;; `x` is `3`!
(get-model)
```

[Open and run this snippet in an online Z3 editor!](https://rise4fun.com/Z3/QZ3N)

Note that even though there isn’t any \(\exists\) existential quantifier in
there, the solver is implicitly finding a solution for \(x\) in \(\exists x:
x + 2 = 5\), i.e. there *exists* some \(x\) such that \(x + 2\)
equals 5. While some SMT solvers have some support for working with higher-order
formulas with explicit \(\exists\) existential and \(\forall\) universal
quantifiers nested inside, these modes tend to be much slower and also
incomplete. We can only rely on first-order, implicitly \(\exists\)
existential queries: that is, formulas with potentially unbound variables and
without any nested \(\exists\) existential and \(\forall\) universal
quantification.

We can add a second assertion to our example that makes it unsatisfiable:

```
(declare-const x Int)

(assert (= 5 (+ x 2)))

;; NEW: also, x + 1 should be 10.
(assert (= 10 (+ x 1)))

;; This time, the result should be unsatisfiable,
;; because there are conflicting requirements for `x`.
(check-sat)
(get-model)
```

[Open and run this snippet in an online Z3 editor!](https://rise4fun.com/Z3/ENRt)

The assertions `10 = x + 1` and `5 = x + 2` put conflicting requirements on `x`,
and therefore there is no value for `x` that can make both assertions true, and
therefore the whole query is unsatisfiable.

Counterexample-Guided Iterative Synthesis
-----------------------------------------

Counterexample-guided iterative synthesis (CEGIS) enables us to solve
second-order, *exists-forall* queries — like our program synthesis problem
— with off-the-shelf SMT solvers. CEGIS does this by decomposing these
difficult queries into multiple first-order, \(\exists\) existentially
quantified queries. These are the kind of queries that off-the-shelf SMT solvers
excel at solving. First, we’ll look at CEGIS in general, and after that we’ll
examine what is required specifically for component-based CEGIS.

CEGIS begins by choosing an initial, finite set of inputs. There has to be at
least one, but it doesn’t really matter where it came from; we can use a random
number generator. Then we start looping. The first step of the loop is *finite
synthesis*, which generates a program that is correct at least for the inputs in
our finite set. It may or may not be correct for all inputs, but we don’t know
that yet. Next, we take that candidate program and *verify* it: we want
determine whether it is correct for all inputs (in which case we’re done), or if
there is some input for which the candidate program is incorrect (called a
*counterexample*). If there is a counterexample, we add it to our set, and
continue to the next iteration of the loop. The next program that finite
synthesis produces will be correct for all the old inputs, and also this new
counterexample. The counterexamples force finite synthesis to come up with more
and more general programs that are correct for more and more inputs, until
finally it comes up with a fully general program that works for all inputs.

Without further ado, here is the general CEGIS algorithm:

\(\begin{align}
& \texttt{CEGIS}(\phi\_\mathrm{spec}(\vec{I}, O)): \\
& \qquad S = \langle \text{initial finite inputs} \rangle \\
& \qquad \\
& \qquad \textbf{loop}: \\
& \qquad \qquad \texttt{// Finite synthesis.} \\
& \qquad \qquad \textbf{solve for $P$ in } \exists P,O\_0,\ldots,O\_{\lvert S \rvert - 1}: \\
& \qquad \qquad \qquad \left( P(S\_0) = O\_0 \land \phi\_\mathrm{spec}(S\_0, O\_0) \right) \\
& \qquad \qquad \qquad \land \ldots \\
& \qquad \qquad \qquad \land \left( P(S\_{\lvert S \rvert - 1}) = O\_{\lvert S \rvert - 1} \land \phi\_\mathrm{spec}(S\_{\lvert S \rvert - 1}, O\_{\lvert S \rvert - 1}) \right) \\
& \qquad \qquad \textbf{if } \texttt{unsat}: \\
& \qquad \qquad \qquad \textbf{error} \text{ “no solution”} \\
& \qquad \qquad \\
& \qquad \qquad \texttt{// Verification.} \\
& \qquad \qquad \textbf{solve for $\vec{I}$ in } \exists \vec{I},O: \,\, P(\vec{I}) = O \land \lnot \phi\_\mathrm{spec}(\vec{I}, O) \\
& \qquad \qquad \textbf{if } \texttt{unsat}: \\
& \qquad \qquad \qquad \textbf{return $P$} \\
& \qquad \qquad \textbf{else}: \\
& \qquad \qquad \qquad \textbf{append $\vec{I}$ to $S$} \\
& \qquad \qquad \qquad \textbf{continue}
\end{align}\)

CEGIS decomposes the *exists-forall* synthesis problem into two parts:

1. **Finite synthesis:** The first query, the finite synthesis query, finds a
   program that is correct for at least the finite example inputs in
   \(S\). Here’s its breakdown:

   |  |  |
   | --- | --- |
   | \( \exists P,O\_0,\ldots,O\_{\lvert S \rvert - 1}: \) | There exists some program \(P\) and outputs \(O\_0,\ldots,O\_{\lvert S \rvert - 1}\) such that |
   | \( ( \,\, P(S\_0) = O\_0 \) | \(O\_0\) is the output of running the program on inputs \(S\_0\) |
   | \( \land \) | and |
   | \( \phi\_\mathrm{spec}(S\_0, O\_0) \,\, ) \) | the specification is satisfied for the inputs \(S\_0\) and output \(O\_0\), |
   | \( \land \ldots \) | and… |
   | \( \land \left( P(S\_{\lvert S \rvert - 1}) = O\_{\lvert S \rvert - 1} \land \phi\_\mathrm{spec}(S\_{\lvert S \rvert - 1}, O\_{\lvert S \rvert - 1}) \right) \) | and \(O\_{\lvert S \rvert - 1}\) is the output of running the program on inputs \(S\_{\lvert S \rvert - 1}\), and the specification is satisfied for these inputs and output. |

   Note that this is a first-order, existential query; it is *not* using nested
   \(\forall\) universal quantification over all possible inputs! Instead, it
   is instantiating a new copy of \(P(S\_i) = O\_i \land \phi\_\mathrm{spec}(S\_i,
   O\_i)\) for each example in our finite set \(S\).

   For example, if \(S = \langle 3, 4, 7 \rangle\), then the finite synthesis
   query would be

   > \(\begin{align}
   > & \exists P,O\_0,O\_1,O\_2: \\
   > & \qquad \left( P(3) = O\_0 \land \phi\_\mathrm{spec}(3, O\_0) \right) \\
   > & \qquad \land \,\, \left( P(4) = O\_1 \land \phi\_\mathrm{spec}(4, O\_1) \right) \\
   > & \qquad \land \,\, \left( P(7) = O\_2 \land \phi\_\mathrm{spec}(7, O\_2) \right) \\
   > \end{align}\)

   This inline expansion works because the finite set of inputs \(S\) is much
   smaller in practice (typically in the tens, if even that many) than the size
   of the set of all possible inputs (e.g. there are \(2^{32}\) bitvectors 32
   bits wide).

   If the query was unsatisfiable, then there is no program that can implement
   the specification for every one of the inputs in \(S\). Since \(S\) is a
   subset of all possible inputs, that means that there is no program that can
   implement the specification for all inputs. And since that is what we are
   searching for, it means that the search has failed, so we return an error.

   If the query was satisfiable, the resulting program \(P\) satisfies the
   specification for all the inputs in \(S\), but we don’t know whether it
   satisfies the specification for all possible inputs or not yet. For example,
   if \(S = \langle 0, 4 \rangle \), then we know that the program \(P\) is
   correct when given the inputs \(0\) and \(4\), but it may or may not be
   correct when given the input \(1\). We don’t know yet.
2. **Verification**: Verification takes the program \(P\) produced by finite
   synthesis and checks whether it satisfies the specification *for all*
   inputs. That’s naturally expressed as a \(\forall\) universally quantified
   query over all inputs, but we can instead ask if there *exists* any input to
   the program for which the specification is *not* satisfied thanks to [De
   Morgan’s law](https://en.wikipedia.org/wiki/De_Morgan%27s_laws#Extension_to_predicate_and_modal_logic).

   Here’s the breakdown of the verification query:

   |  |  |
   | --- | --- |
   | \( \exists \vec{I}, O: \) | Does there exist some inputs \(\vec{I}\) and output \(O\) such that |
   | \( P(\vec{I}) = O\) | \(O\) is the result of running the program on \(\vec{I}\) |
   | \( \land \) | and |
   | \( \lnot \phi\_\mathrm{spec}(\vec{I}, O) \) | the specification is *not* satisfied. |

   If the verification query is unsatisfiable, then there are no inputs to
   \(P\) for which the specification is not satisfied, which means that
   \(P\) satisfies the specification for all inputs. If so, this is what we
   are searching for, and we’ve found it, so return it!

   However, if the verification query is satisfiable, then we’ve discovered a
   *counterexample*: a new input \(\vec{I}\) for which the program does not
   satisfy the specification. That is, the program \(P\) is buggy when given
   \(\vec{I}\), so \(P\) isn’t the program we are searching for.

   Next, we add the new \(\vec{I}\) to our finite set of inputs \(S\), so
   that in the next iteration of the loop, we will synthesize a program that
   produces a correct result when given \(\vec{I}\) in addition to all the
   other inputs in \(S\).

As the loop iterates, we add more and more inputs to \(S\), forcing the finite
synthesis query to produce more and more general programs. Eventually it
produces a fully general program that satisfies the specification for all
inputs. In the worst case, we are adding every possible input into \(S\):
finite synthesis comes up with a program that fails verification when given 1,
and then when given 2, and then 3, and so on. In practice, each counterexample
\(\vec{I}\) that verification finds tends to be representative of *many* other
inputs that are also currently unhandled-by-\(P\). By adding \(\vec{I}\) to
\(S\), the next iteration of finite synthesis will produce a program that
handles not just \(\vec{I}\) but also all the other inputs that \(\vec{I}\)
was representative of.

For example, finite synthesis might have produced a program that handles all of
\(S = \langle 0,1,5,13 \rangle\) but which is buggy when given a positive,
even number. Verification finds the counterexample \(I = 2\), which gets
appended to \(S\), and now \(S = \langle 0,1,5,13,2 \rangle\). Then, the
next iteration of the loop synthesizes a program that doesn’t *just* also work
for 2, but works for *all* positive even numbers. This is what makes CEGIS
effective in practice.

Finally, notice that both finite synthesis and verification are first-order,
\(\exists\) existentially quantified queries that off-the-shelf SMT solvers
like Z3 can solve.

### CEGIS with Components

Now that we know how CEGIS works in the abstract, let’s dive into how we can use
it to synthesize component-based programs.

For every loop-free program that is a composition of components, we can flip the
program’s representation into a *location mapping*:

* Instead of listing the program line-by-line, defining what component is on
  each line, we can list components, defining what line the component ends up
  on.
* Instead of referencing the arguments to each component by variable name, we
  can reference either the line on which the argument is defined (if it comes
  from the result of an earlier component) or as the \(n^\mathrm{th}\) program
  input.

For example, consider our program to isolate the rightmost zero bit in a word:

```
isolate_rightmost_zero_bit(x):
    a ← not x
    b ← add 1, x
    c ← and a, b
    return c
```

We can exactly represent this program with the following location mapping:

```
{
    inputs: ["x"],

    components: {
        // Line 1: `b ← add 1, x`
        add1: {
            // The line in the program where this
            // component is placed.
            line: 1,

            // Each entry `a` represents where the
            // argument comes from.
            //
            // If `0 <= a < inputs.len()`, then the
            // argument is `inputs[a]`.
            //
            // Otherwise, when `inputs.len() <= a`,
            // then the argument comes from the value
            // defined by the component on line
            /// `a - inputs.len()`.
            arguments: [
                // `x`
                0,
            ],
        },

        // Line 2: `c ← and a, b`
        and: {
            line: 2,
            arguments: [
                // `a`
                1,
                // `b`
                2,
            ],
        },

        // Line 0: `a ← not x`
        not: {
            line: 0,
            arguments: [
                // `x`
                0,
            ],
        },
    },
}
```

With component-based CEGIS, we’ll be synthesizing this kind of location
mapping. This lets us represent a whole component-based program with a handful
of numbers for lines and argument indices. And numbers are something that we can
represent directly in an SMT query.

#### Verifying a Component-Based Program

Let’s start with verying a component-based program before we look at their
finite synthesis. Verification takes a location mapping, connects the
components’ input and output variables together as described by the location
mapping, and asks the SMT solver to find a counterexample.

For convenience, so we don’t have to keep repeating
\(\vec{I}\_0,\ldots,\vec{I}\_{N-1}\) all the time, we define \(\textbf{P}\) as
the set of all the parameter variables for each component in the library:

> \( \textbf{P} = \, \vec{I}\_0 \, \cup \, \ldots \, \cup \, \vec{I}\_{N-1} \)

And similarly we define \(\textbf{R}\) as the set of all temporary result
variables for each component in the library:

> \( \textbf{R} = \{O\_0, \, \ldots, \, O\_{N-1}\} \)

With our running example of isolating the rightmost zero bit, our minimal
library consists of

> \(
> \begin{align}
> \phi\_0(I\_0, O\_0) &= [O\_0 = \texttt{bvadd}(1, I\_0)] \\
> \phi\_1(I\_1, I\_2, O\_1) &= [O\_1 = \texttt{bvand}(I\_1, I\_2)] \\
> \phi\_2(I\_3, O\_2) &= [O\_2 = \texttt{bvnot}(I\_3)]
> \end{align}
> \)

and therefore its

> \(
> \begin{align}
> N &= 3 \\
> \textbf{P} &= \{ I\_0, I\_1, I\_2, I\_3, I\_4 \} \\
> \textbf{R} &= \{ O\_0, O\_1, O\_2 \}
> \end{align}
> \)

We want to constrain the whole library to behave according to its individual
component specifications. The output of each `and` component should indeed be
the bitwise *and* of its inputs, and the output of each `not` component should
indeed be the bitwise *not* of its input, etc… We define
\(\phi\_\mathrm{lib}\) as the combination of every component specification
\(\phi\_i\):

> \( \phi\_\mathrm{lib}(\textbf{P}, \textbf{R}) = \phi\_i(\vec{I}\_0, O\_0) \land \ldots \land \phi\_i(\vec{I}\_{N-1}, O\_{N-1}) \)

So for our minimal example library, the \(\phi\_\mathrm{lib}\) we get is:

> \(
> \begin{align}
> \phi\_\mathrm{lib}(\textbf{P}, \textbf{R}) &= [ O\_0 = \texttt{bvadd}(1, I\_0) ] \\
> &\land [ O\_1 = \texttt{bvand}(I\_1, I\_2) ] \\
> &\land [ O\_2 = \texttt{bvnot}(I\_3) ]
> \end{align}
> \)

That is, the library’s constraints are satisfied when all of

* \(O\_0\) is the wrapping addition of \(I\_0\) and 1,
* \(O\_1\) is the bitwise *and* of \(I\_1\) and \(I\_2\), and
* \(O\_2\) is the bitwise *not* of \(I\_3\),

Because finite synthesis runs before verification, we already have access to the
candidate program’s location mapping when we’re constructing our verification
query. This location mapping tells us which actual arguments align with which
formal parameters of a component. That means we know what the connections are
from each component’s input variables to the program inputs and the temporary
result variables for other components. We know the dataflow between components.

Let’s make this concrete with our isolating-the-rightmost-zero-bit
example. Having produced this candidate program:

```
a ← not x
b ← add 1, x
c ← and a, b
```

With this library:

> \(
> \begin{align}
> \phi\_0(I\_0, O\_0) &= [O\_0 = \texttt{bvadd}(1, I\_0)] \\
> \phi\_1(I\_1, I\_2, O\_1) &= [O\_1 = \texttt{bvand}(I\_1, I\_2)] \\
> \phi\_2(I\_3, O\_2) &= [O\_2 = \texttt{bvnot}(I\_3)]
> \end{align}
> \)

We know that \(\texttt{a} = O\_2\), since it is the result of the `not`
component \(\phi\_2(I\_3, O\_2)\). And since `a` is the first argument to `and a,
b`, which uses component \(\phi\_1(I\_1, I\_2, O\_1)\), we know that \(\texttt{a}
= I\_1\). Therefore, we know that \(O\_2 = I\_1\).

We have these equalities from each component input variable \(I\_i\) in
\(\textbf{P}\) to either some other component’s output variable \(O\_j\) in
\(\textbf{R}\) or to one of the program inputs \(\vec{I}\). These equalities
are given to us directly by the location mapping for the candidate program that
we’re verifying.

Additionally, because our candidate program is implicitly returning the last
temporary variable `c`, which is the result of the and component
\(\phi\_1(I\_1, I\_2, O\_1)\), and because the \(O\) in
\(\phi\_\mathrm{spec}(\vec{I}, O)\) represents the result of the whole program,
we know that \(O = O\_1\).

If we put all these equalities together for our example program we get:

> \( \left( I\_0 = x \right) \land \left( I\_1 = O\_2 \right) \land \left( I\_2 = O\_1 \right) \land \left( I\_3 = x \right) \land \left( O = O\_1 \right)\)

This represents all the connections between our library’s various components and
to the candidate program’s inputs and output. If you imagine connecting the
components together like a circuit, this represents all the wires between each
component.

We define these component-connecting equalities as \(\phi\_\mathrm{conn}\), and
its general definition is:

> \(
> \begin{align}
> \phi\_\mathrm{conn}(\vec{I}, O, \textbf{P}, \textbf{R}) &= \left( O = O\_\mathrm{last} \right) \\
> & \land \left( \vec{I}\_0 \, = \, \vec{V}\_0 \right) \\
> & \land \, \ldots \\
> & \land \left( \vec{I}\_{N-1} \, = \, \vec{V}\_{N-1} \right)
> \end{align}
> \)

Where

* \(\vec{V}\_i\) are the actual arguments that the candidate program passes
  into the \(i^\mathrm{th}\) component \(\phi\_i\). Each \(\vec{V}\_i\) is
  made up of entries from either the program’s inputs \(\vec{I}\) or from
  temporary results from \(\textbf{R}\) that are defined by earlier components
  in the program. This is equivalent to the `arguments` field defined for each
  component in our example location mapping’s `components` map.
* \(O\_\mathrm{last}\) is the output variable for the component on the last
  line of the program, according to our candidate program’s location mapping.

Once again, let’s break that down:

|  |  |
| --- | --- |
| \( \left( O = O\_\mathrm{last} \right) \) | The output of the whole program is equal to the result of the component on the last line of the program, |
| \( \land \) | and |
| \( \left( \vec{I}\_0 \, = \, \vec{V}\_0 \right) \) | the first component's inputs and its assigned arguments are equal to each other, |
| \( \land \, \ldots \) | and... |
| \( \left( \vec{I}\_{N-1} \, = \, \vec{V}\_{N-1} \right) \) | the last component's inputs and its assigned arguments are equal to each other. |

Note that both \(O\_\mathrm{last}\) and each \(\vec{V}\_i\) are properties of
the candidate program’s location mapping, and are known at “compile time” of the
verification query. They are *not* variables that we are \(\exists\)
existentially or \(\forall\) universally quantifying over in the query
itself. We expand them inline when constructing the verification query.

Ok, so with all of that out of the way, we can finally define the verification
constraint that we use in component-based CEGIS:

> \(
> \begin{align}
> & \exists \vec{I}, O, \textbf{P} , \textbf{R} : \\
> & \qquad \phi\_\mathrm{conn}(\vec{I}, O, \textbf{P}, \textbf{R})
> \land \phi\_\mathrm{lib}(\textbf{P}, \textbf{R})
> \land \lnot \phi\_\mathrm{spec}(\vec{I}, O)
> \end{align}
> \)

The verification constraint asks: given that we’ve connected the components
together as described by the candidate program’s location mapping, are there any
inputs for which the specification is not satisfied?

Let’s break that down once more:

|  |  |
| --- | --- |
| \( \exists \vec{I}, O, \textbf{P} , \textbf{R} : \) | Does there exist some inputs and output such that |
| \(\phi\_\mathrm{conn}(\vec{I}, O, \textbf{P}, \textbf{R}) \) | when the components are connected together as described by our candidate program's location mapping, |
| \( \land \,\, \phi\_\mathrm{lib}(\textbf{P}, \textbf{R}) \) | and when the components behave as defined by our library, |
| \( \land \,\, \lnot \phi\_\mathrm{spec}(\vec{I}, O) \) | the specification is *not* satisfied? |

Finding a solution to this query gives us a new counterexample \(\vec{I}\)
that we can add to our set of examples \(S\) for future iterations of the
CEGIS loop. Failure to find any solution to this query means that the candidate
location mapping corresponds to a program that is correct for all inputs, in
which case we’re done.

#### Finite Synthesis of a Component-Based Program

Finite synthesis composes the library components into a program that will
correctly handle all the given example inputs. It does this by querying the SMT
solver for a location mapping that contains assignments of components to lines
in the program, and assignments of variables to each component’s actual
arguments.

Recall our example location mapping:

```
{
    inputs: ["x"],

    components: {
        // Line 1: `b ← add 1, x`
        add1: {
            line: 1,
            arguments: [0], // `[x]`
        },

        // Line 2: `c ← and a, b`
        and: {
            line: 2,
            arguments: [1, 2], // `[a, b]`
        },

        // Line 0: `a ← not x`
        not: {
            line: 0,
            arguments: [0], // `[x]`
        },
    },
}
```

To encode a location mapping in the finite synthesis query, every component
parameter in \(\textbf{P}\) and every component result in \(\textbf{R}\)
gets an associated location variable. The finite synthesis query is searching
for an assignment to these location variables.

We call the set of all location variables \(L\), and we refer to a particular
location variable as \(l\_x\) where \(x\) is either a component result in
\(\textbf{R}\) or component parameter in \(\textbf{P}\):

> \( L = \{ \, l\_x \, \vert \, x \in \textbf{P} \cup \textbf{R} \, \} \)

The location variable for a result \(l\_{O\_i}\) is equivalent to the `line`
field for a component in our JSON-y syntax for example location mappings. It
determines the line in the program that the component is assigned to, and
therefore where its temporary result is defined.

The location variable for a parameter \(l\_p\) is equivalent to an entry in a
component’s `arguments` list in our JSON-y syntax. These location variables
determine where the associated parameter gets its value from: either the
\(i^\mathrm{th}\) program input or the temporary result defined on the
\(j^\mathrm{th}\) line of the program.

To use one index space for both line numbers and program inputs, we follow the
same convention that we did with entries in the `arguments` list in the JSON
syntax:

* When \(l\_x\) is less than the number of program inputs, then it refers to
  the \({l\_x}^\mathrm{th}\) program input.
* Otherwise, when \(l\_x\) is greater than or equal to the number of program
  inputs, then subtract the number of inputs from \(l\_x\) to get the line
  number it’s referring to.

| Value of \(l\_x\) | Refers To Location | |
| --- | --- | --- |
| 0 | Input 0 | Program Inputs \(\vec{I}\) |
| 1 | Input 1 |
| ... | ... |
| \( \lvert \vec{I} \rvert - 1 \) | Input \( \lvert \vec{I} \rvert - 1 \) |
| \(\lvert \vec{I} \rvert + 0\) | Line 0 | Line Numbers |
| \(\lvert \vec{I} \rvert + 1\) | Line 1 |
| ... | ... |
| \(\lvert \vec{I} \rvert + N - 1\) | Line \(N - 1\) |

All loop-free, component-based programs can be described with a location
mapping. However, the reverse is not true: not all location mappings describe a
valid program.

Consider this location mapping:

```
{
    inputs: ["x"],

    components: {
        // Line 0: `a ← add 1, x`
        add1: {
            line: 0,
            arguments: [0], // `[x]`
        },

        // Line 0: `a ← sub x, 1`
        sub1: {
            line: 0,
            arguments: [0], // `[x]`
        }
    }
}
```

This line mapping is *inconsistent* because it wants to put both its components
on line zero of the program, but each line in the program can only use a single
component.

To forbid the solver from providing bogus answers of this sort, we add the
consistency constraint \(\psi\_\mathrm{cons}\) to the finite synthesis
query. It requires that no pair of distinct component result location variables
can be assigned the same line.

> \(
> \psi\_\mathrm{cons}(L) =
> \bigwedge\limits\_{x,y \in \textbf{R}, x \not\equiv y} \left( l\_x \neq l\_y \right)
> \)

Once more, let’s break that down:

|  |  |
| --- | --- |
| \( \bigwedge\limits\_{x,y \in \textbf{R}, x \not\equiv y} \) | For each \(x,y\) pair of component results, where \(x\) and \(y\) are not the same result variable, |
| \( \left( l\_x \neq l\_y \right) \) | the location of \(x\) and the location of \(y\) are not the same. |

But there are even more ways that a location mapping might describe an invalid
program! Consider this location mapping:

```
{
    inputs: ["x"],

    components: {
        // Line 0: `a ← and x, b`
        and: {
            line: 0,
            arguments: [0, 2], // `[x, b]`
        },

        // Line 1: `b ← sub a, 1`
        sub1: {
            line: 1,
            arguments: [1], // `[a]`
        }
    }
}
```

That location mapping describes this program:

```
f(x):
    a ← and x, b
    b ← sub a, 1
```

The `b` temporary result is used before it is defined, and in order to compute
`b`, we need to compute `a`, but computing `a` requires computing `b`, which
requires computing `a`, etc… We have a cycle on our hands.

To forbid mappings that correspond to bogus programs with dataflow cycles, we
use the acyclicity constraint \(\psi\_\mathrm{acyc}\). This constraint enforces
that a particular component’s parameters are defined before this component’s
line.

> \(
> \psi\_\mathrm{acyc}(L) =
> \bigwedge\limits\_{i=0}^{N-1}
> \left(
> \bigwedge\limits\_{p \in \vec{I}\_i} \left( l\_p < l\_{O\_i} \right)
> \right)
> \)

Let’s break that down:

|  |  |
| --- | --- |
| \( \bigwedge\limits\_{i=0}^{N-1} \) | For each component index \(i\), |
| \( \bigwedge\limits\_{p \in \vec{I}\_i} \) | and for each of the \(i^\mathrm{th}\) component's input parameters, |
| \( l\_p < l\_{O\_i} \) | the location of the parameter should be less than the location of the component, meaning that the parameter is defined before the component is used. |

The only other way that location mappings can be invalid is if a location is out
of bounds of the program inputs and line numbers, so we’re ready to define the
well-formed-program constraint \(\psi\_\mathrm{wfp}\). This constraint enforces
that any location mapping we synthesize will correspond to a well-formed
program.

A well-formed program is

* consistent,
* acyclic,
* its component parameter locations point to either a program input or a line
  number, and
* its component temporary result locations point to a line number.

Let’s define \(M\) as the number of program inputs plus the number of
components in the library:

> \( M = \lvert \vec{I} \rvert + N \)

A component parameter location \(l\_{p \in \textbf{P}}\) can point to either

* a program input in the range from zero to the number of program inputs: \(0
  \leq l\_{p} \lt \lvert \vec{I} \rvert\), or
* a line number, which corresponds to the \(N\) locations following the
  program inputs: \(\lvert \vec{I} \rvert \leq l\_p \lt M \).

Since those two ranges are contiguous, it means that component parameter
locations ultimately fall within the range \(0 \leq l\_p \lt M\).

A component temporary result location \(l\_{r \in \textbf{R}}\) must point to a
line number, which means that they fall within the range \(\lvert \vec{I}
\rvert \leq l\_r \lt M\).

Put all that together and we get the well-formed-program constraint
\(\psi\_\mathrm{wfp}\):

> \(
> \begin{align}
> \psi\_\mathrm{wfp}(L) &= \bigwedge\limits\_{p \in \textbf{P}} \left( 0 \leq l\_p \lt M \right) \\
> & \land \, \bigwedge\limits\_{r \in \textbf{R}} \left( \lvert \vec{I} \rvert \leq l\_r \lt M \right) \\
> & \land \, \psi\_\mathrm{cons}(L) \\
> & \land \, \psi\_\mathrm{acyc}(L)
> \end{align}
> \)

And here is its breakdown:

|  |  |
| --- | --- |
| \( \bigwedge\limits\_{p \in \textbf{P}} \left( 0 \leq l\_p \lt M \right) \) | Each component parameter location \(l\_p\) points to either a program input or a line number, |
| \( \land \, \bigwedge\limits\_{r \in \textbf{R}} \left( \lvert \vec{I} \rvert \leq l\_r \lt M \right) \) | and each component result location \(l\_r\) points to a line number, |
| \( \land \, \psi\_\mathrm{cons}(L) \) | and the location mapping is consistent, |
| \( \land \, \psi\_\mathrm{acyc}(L) \) | and the location mapping is acyclic. |

Now that we can constrain finite synthesis to only produce location mappings
that correspond to well-formed programs, all we need to do is encode the
connections between components and the behavior of the library. This should
sound familiar: we need the finite synthesis equivalent of
\(\phi\_\mathrm{conn}\) and \(\phi\_\mathrm{lib}\) from verification. And it
turns out that \(\phi\_\mathrm{lib}\) doesn’t need to be tweaked at all,
because the behavior of the library remains the same whether we are in
verification or finite synthesis. But while \(\phi\_\mathrm{conn}\) was
checking a set of already-known connections between components, in finite
synthesis we are searching for those connections, so we need a different query.

These connections define the dataflow between components. They are the wires in
the circuit built from our components. A connection from some component result
into another component’s input means that we need to constrain the result and
input variables to be equal in the finite synthesis query. For example, if
component \(\phi\_i\) get’s placed on line 3, and parameter \(p\) is assigned
the location 3, then \(p\) must take on the same value as the output \(O\_i\)
of that component.

This leads us to our definition of \(\psi\_\mathrm{conn}\): for every pair of
location variables \(l\_x\) and \(l\_y\), if they refer to the same
location, then \(x\) and \(y\) must have the same value.

> \( \psi\_\mathrm{conn}(L, \vec{I}, O, \textbf{P}, \textbf{R}) = \bigwedge\limits\_{x,y \in \vec{I} \cup \textbf{P} \cup \textbf{R} \cup { O } } \left( \left( l\_x = l\_y \right) \implies \left( x = y \right) \right) \)

Here is its piece-by-piece breakdown:

|  |  |
| --- | --- |
| \( \bigwedge\limits\_{x,y \in \vec{I} \cup \textbf{P} \cup \textbf{R} \cup \{ O \} } \) | For each pair of location variables \(l\_x\) and \(l\_y\), where \(x\) and \(y\) are either a program input, or a component's parameter, or a component's temporary result, or the program output, |
| \( \left( l\_x = l\_y \right) \) | if the location variables refer to the same location, |
| \( \implies \) | then |
| \( \left( x = y \right) \) | \(x\) and \(y\) must have the same value. |

We’re finally ready to define our finite synthesis query for a location
mapping. This query asks the solver to find some location mapping that
corresponds to a well-formed program that satisfies our specification for each
example input in \(S\). In other words, it must enforce that

* the location mapping corresponds to a well-formed program, and
* when the components are connected as described by the location mapping, and
  when the components behave as described by our library,
* then the specification is satisfied for each of our example inputs in \(S\).

Here it is, finally, our finite synthesis query:

> \(
> \begin{align}
> & \exists L, O\_0, \ldots, O\_{\vert S \rvert - 1}, \textbf{P}\_0, \ldots, \textbf{P}\_{\vert S \rvert - 1}, \textbf{R}\_0, \ldots, \textbf{R}\_{\vert S \rvert - 1}: \\
> & \qquad \psi\_\mathrm{wfp}(L) \,\, \land \\
> & \qquad \qquad \bigwedge\limits\_{i=0}^{\lvert S \rvert - 1} \left( \phi\_\mathrm{lib}(\textbf{P}\_i, \textbf{R}\_i) \land \psi\_\mathrm{conn}(L, S\_i, O\_i, \textbf{P}\_i, \textbf{R}\_i) \land \phi\_\mathrm{spec}(S\_i, O\_i) \right) \\
> \end{align}
> \)

That’s quite a mouthful, so, one last time, let’s pull it apart and break it down:

|  |  |
| --- | --- |
| \( \exists L, O\_0, \ldots, O\_{\vert S \rvert - 1}, \textbf{P}\_0, \ldots, \textbf{P}\_{\vert S \rvert - 1}, \textbf{R}\_0, \ldots, \textbf{R}\_{\vert S \rvert - 1}: \) | There exists some location mapping \(L\), and program outputs, component parameters, and component results variables for each example in \(S\), such that |
| \( \psi\_\mathrm{wfp}(L) \,\, \land \) | the location mapping is a well-formed program, and |
| \( \bigwedge\limits\_{i=0}^{\lvert S \rvert - 1} \) | for each example input index \(i\), |
| \( \phi\_\mathrm{lib}(\textbf{P}\_i, \textbf{R}\_i) \) | the components behave as described by the library, |
| \( \land \,\, \psi\_\mathrm{conn}(L, S\_i, O\_i, \textbf{P}\_i, \textbf{R}\_i) \) | and the components are connected as described by the location mapping, |
| \( \land \,\, \phi\_\mathrm{spec}(S\_i, O\_i) \) | and the specification is satisfied for the \(i^\mathrm{th}\) example input. |

When the solver finds a satisfiable assignment for this query, we get a new
candidate location mapping that corresponds to a program that is correct for
each of the example inputs in \(S\). When the solver finds the query
unsatisifiable, that means there is no locaiton mapping that corresponds to a
program that is correct for each of the example inputs, which means that our
search has failed.

Implementation
--------------

I implemented a loop-free, component-based program synthesizer in Rust that uses
Z3 to solve the finite synthesis and verification queries. [The implementation’s
repository is over here.](https://github.com/fitzgen/synth-loop-free-prog)

Our target language has all the operations you would expect for working with
fixed-width integers. It has arithmetic operations like `add` and `mul`. It has
bitwise operations like `and` and `xor`. It has comparison operations like `eq`,
that evaluate to one if the comparison is true and zero otherwise. Finally, it
has a `select` operation that takes three operands: a condition, a consequent,
and an alternative. When the condition is non-zero, it evaluates to the
consequent, and otherwise it evaluates to the alternative.

Values are neither signed nor unsigned. For operations like division that behave
differently on signed and unsigned integers, we have a different instruction for
each behavior: `div_s` for signed division and `div_u` for unsigned division.

### Program Representation

A program is a sequence of instructions:

```
pub struct Program {
    instructions: Vec<Instruction>,
}
```

An instruction has an operation and binds its result to an identifier:

```
pub struct Instruction {
    result: Id,
    operator: Operator,
}
```

An identifier is an opaque wrapper around a number:

```
pub struct Id(u32);
```

We won’t support any nice names for identifiers, since essentially everything is
a temporary. When we stringify programs, we’ll turn the identifiers into `a`,
`b`, `c`, etc…

Additionally, we will uphold the invariant that `Id(i)` always refers to the
value defined by the `i`th instruction in the program.

Finally, the `Operator` enumeration has a variant for each operation in the
language, along with the identifiers of its operands:

```
pub enum Operator {
    Var,                // New input variable.

    Const(u64),         // A constant value.

    Eqz(Id),            // Equals zero?
    Clz(Id),            // Count leading zeros.
    Ctz(Id),            // Count trailing zeros.
    Popcnt(Id),         // Population count.

    Eq(Id, Id),         // Equal?
    Ne(Id, Id),         // Not equal?
    LtS(Id, Id),        // Signed less than?
    LtU(Id, Id),        // Unsigned less than?
    GtS(Id, Id),        // Signed greater than?
    GtU(Id, Id),        // Unsigned greater than?
    LeS(Id, Id),        // Signed less than or equal?
    LeU(Id, Id),        // Unsigned less than or equal?
    GeS(Id, Id),        // Signed greater than or equal?
    GeU(Id, Id),        // Unsigned greater than or equal?

    Add(Id, Id),        // Addition.
    Sub(Id, Id),        // Subtraction.
    Mul(Id, Id),        // Multiplication.
    DivS(Id, Id),       // Signed division.
    DivU(Id, Id),       // Unsigned division.
    RemS(Id, Id),       // Signed remainder.
    RemU(Id, Id),       // Unsigned remainder.

    And(Id, Id),        // And.
    Or(Id, Id),         // Or.
    Xor(Id, Id),        // Exclusive or.
    Shl(Id, Id),        // Shift left.
    ShrS(Id, Id),       // Signed shift right.
    ShrU(Id, Id),       // Unsigned shift right.
    Rotl(Id, Id),       // Rotate left.
    Rotr(Id, Id),       // Rotate right.

    Select(Id, Id, Id), // If then else.
}
```

### Building Programs

To make constructing programs by hand easier, we have a builder for programs. It
wraps an inner `Program` and exposes a method for each operation, to append an
instruction using that operation to the program thats being built.

```
pub struct ProgramBuilder {
    program: Program,
}

impl ProgramBuilder {
    /// Start building a new program!
    pub fn new() -> ProgramBuilder {
        ProgramBuilder {
            program: Program {
                instructions: vec![],
            },
        }
    }

    /// Finish building this program!
    pub fn finish(self) -> Program {
        self.program
    }

    fn next_id(&self) -> Id {
        Id(self.program.instructions.len() as u32)
    }

    // ...

    /// Append an `add a, b` instruction!
    pub fn add(&mut self, a: Id, b: Id) -> Id {
        let result = self.next_id();
        self.program.instructions.push(Instruction {
            result,
            operator: Operator::Add(a, b),
        });
        result
    }

    // ...
}
```

Here is our isolate-the-righmost-zero-bit example program constructed via the
`ProgramBuilder`:

```
// isolate_rightmost_zero_bit(x):
//     a ← not x
//     b ← add 1, x
//     c ← and a, b
//     return c

let builder = ProgramBuilder::new();

let x = builder.var();
let a = builder.not(x);
let one = builder.const_(1);
let b = builder.add(one, x);
let c = builder.and(a, b);

let isolate_rightmost_zero_bit = builder.finish();
```

Having the builder is nice since we intend to write unoptimized programs
ourselves, that we then use as specifications for synthesizing optimized
programs.

### Defining Components

Every operator has an associated component, so that we can synthesize programs
that use that operator. Because a library can have a heterogeneous set of
components, we’ll define an object-safe `Component` trait, so we can box them up
as [trait objects](https://doc.rust-lang.org/1.30.0/book/second-edition/ch17-02-trait-objects.html) with dynamically dispatched methods, and
store them all in the same collection.

A `Component` has two roles:

1. It must provide the constraints between its inputs and its output for the
   solver. This is its \(\phi\_i(\vec{I}\_i, O\_i)\) that will be part of the
   whole library’s \(\phi\_\mathrm{lib}(\textbf{P}, \textbf{R})\).
2. After we’ve synthesized some location mapping for a program that uses this
   component, in order to construct the corresponding `Program`, the component
   needs to know how to create the `Operator` it represents.

The `make_expression` trait method will handle the first role, and the
`make_operator` trait method will handle the second. `make_expression` takes Z3
`BitVec` variables as its operands (the \(\vec{I}\_i\) input variables) and
returns a new Z3 `BitVec` expression that represents the result of running the
operation on the operands (the \(O\_i\) output variable). `make_operator` takes
the `Id`s of its operands (as described by a synthesized location mapping) and
returns its associated `Operator` with those `Id`s as its operands.

Note that, because different components have different arities, these methods
don’t take their operands as multiple, individual parameters like `a: BitVec, b:
BitVec` or `a: Id, b: Id`. Instead, components report their arity with the
`operand_arity` trait method and callers pass in a slice of that many operands.

Finally, we also support synthesizing constant values for the `const`
operator. These immediates are handled separately from operands, and so we also
have the `immediate_arity` trait method, and `make_expression` and
`make_operator` also takes slices of immediates.

```
pub trait Component {
    /// How many operands does this component take?
    fn operand_arity(&self) -> usize;

    /// How many immediates does this component need
    /// synthesized?
    fn immediate_arity(&self) -> usize;

    /// Construct this component's constraint as a Z3
    /// expression.
    fn make_expression<'a>(
        &self,
        context: &'a z3::Context,
        immediates: &[BitVec<'a>],
        operands: &[BitVec<'a>],
        bit_width: u32,
    ) -> BitVec<'a>;

    /// Construct an `Operator` from the given
    /// immediates and operands.
    fn make_operator(
        &self,
        immediates: &[u64],
        operands: &[Id]
    ) -> Operator;
}
```

Let’s take a look at the implementation of a simple, representative component:
the `add` component.

* It has two operands and zero immediates.
* The `make_operator` implementation is mechanical, pulling out its individual
  operands from the given slice, just to push them into the `Operator::Add`.
* The `make_expression` implementation is similarly concise, but is not quite
  mechanical. This is where we encode the `add` operator’s semantics into a Z3
  expression. SMT-LIB2 defines a `bvadd` operatoin for wrapping addition on
  bitvectors, and [the `z3` crate](https://crates.io/crates/z3) we’re using exposes it to us as a
  method on `BitVec`. Wrapping addition is exactly what we want for our `add`
  instruction, and so all we have to do to encode our `add` operation’s
  semantics is `bvadd` our two operands.
* Because we are always working with components as trait objects, we also define
  a helper function for boxing up the `Add` component and turning it into a
  trait object with dynamically dispatched methods.

```
struct Add;

impl Component for Add {
    fn operand_arity(&self) -> usize {
        2
    }

    fn immediate_arity(&self) -> usize {
        0
    }

    fn make_operator(
        &self,
        immediates: &[u64],
        operands: &[Id],
    ) -> Operator {
        Operator::Add(operands[0], operands[1])
    }

    fn make_expression<'a>(
        &self,
        _context: &'a z3::Context,
        immediates: &[BitVec<'a>],
        operands: &[BitVec<'a>],
        _bit_width: u32,
    ) -> BitVec<'a> {
        operands[0].bvadd(&operands[1])
    }
}

pub fn add() -> Box<dyn Component> {
    Box::new(Add) as _
}
```

Most components look pretty much like that: there is some direct encoding into a
single SMT expression for the operation.

Other components, like `eqz`, don’t have a direct encoding as a single SMT
expression, and we need to compose multiple.

```
impl Component for Eqz {
    // ...

    fn make_expression<'a>(
        &self,
        context: &'a z3::Context,
        _immediates: &[BitVec<'a>],
        operands: &[BitVec<'a>],
        bit_width: u32,
    ) -> BitVec<'a> {
        let zero = BitVec::from_i64(
            context,
            0,
            bit_width,
        );
        let one = BitVec::from_i64(
            context,
            1,
            bit_width,
        );
        // `ite` is "if-then-else". If the operand
        // is zero, evaluate to one, otherwise
        // evaluate to zero.
        zero._eq(&operands[0]).ite(&one, &zero)
    }
}
```

The `const` component is the only component that uses immediates. It doesn’t
have operands. Either its constant value is unbound, in which case we’re
synthesizing the value, or we provide a value for it upon constructing the
component:

```
struct Const(Option<u64>);

impl Component for Const {
    fn operand_arity(&self) -> usize {
        0
    }

    fn immediate_arity(&self) -> usize {
        if self.0.is_some() {
            0
        } else {
            1
        }
    }

    fn make_operator(
        &self,
        immediates: &[u64],
        _operands: &[Id]
    ) -> Operator {
        if let Some(val) = self.0 {
            Operator::Const(val)
        } else {
            Operator::Const(immediates[0])
        }
    }

    fn make_expression<'a>(
        &self,
        context: &'a z3::Context,
        immediates: &[BitVec<'a>],
        _operands: &[BitVec<'a>],
        bit_width: u32,
    ) -> BitVec<'a> {
        if let Some(val) = self.0 {
            BitVec::from_i64(
                context,
                val as i64,
                bit_width,
            )
        } else {
            immediates[0].clone()
        }
    }
}

pub fn const_(val: Option<u64>) -> Box<dyn Component> {
    Box::new(Const(val)) as _
}
```

Finally, a library is just a vector of components:

```
pub struct Library {
    pub components: Vec<Box<dyn Component>>,
}
```

### Specifications

A specification looks quite similar to a component, but we only need to create
its SMT constraints. We don’t need to construct `Operator`s from it, so it
doesn’t have an equivalent of the `Component::make_operator` method.

```
pub trait Specification {
    fn arity(&self) -> usize;

    fn make_expression<'a>(
        &self,
        context: &'a z3::Context,
        inputs: &[BitVec<'a>],
        output: &BitVec<'a>,
        bit_width: u32,
    ) -> Bool<'a>;
}
```

We want to use existing, unoptimized programs as specifications for new,
optimized programs, and so we implement `Specification` for `Program`.

The arity of a program specification is how many input variables the program
defines with the `var` operator:

```
impl Specification for Program {
    fn arity(&self) -> usize {
        self.instructions
            .iter()
            .take_while(|inst| {
                inst.operator == Operator::Var
            })
            .count()
    }

    // ...
}
```

To create a Z3 expression for a whole program, we build up subexpressions
instruction by instruction in a table. This table serves as our lexical
environment. By inspecting an operation’s operand `Id`s, we pluck the
corresponding subexpressions out of this table to pass as operands into the
instruction’s `Component::make_expression` implementation. The final entry in
the table is the expression for the whole program, since the program implicitly
returns its last value.

```
impl Specification for Program {
    // ...

    fn make_expression<'a>(
        &self,
        context: &'a z3::Context,
        inputs: &[BitVec<'a>],
        output: &BitVec<'a>,
        bit_width: u32,
    ) -> Bool<'a> {
        // `exprs[i]` is the Z3 subexpression for the
        // value defined on the `i`th instruction of
        // this program.
        let mut exprs: Vec<_> = inputs
            .iter()
            .cloned()
            .collect();

        let mut operands = vec![];

        for instr in self
            .instructions
            .iter()
            .skip(inputs.len())
        {
            // All `const`s in the program already have
            // a bound value, so no instruction will
            // require new immediates.
            let immediates = [];

            // Gather the subexpressions for each
            // operand that this operator is using.
            operands.clear();
            instr
                .operator
                .operands(|Id(i)| {
                    let v = exprs[i as usize].clone();
                    operands.push(v);
                });

            // Create the Z3 expression for this
            // instruction and push it onto `exprs`.
            exprs.push(
                instr
                    .operator
                    .make_expression(
                        context,
                        &immediates,
                        &operands,
                        bit_width,
                    )
            );
        }

        // The last instruction defines our return
        // value, and it should be equal to the
        // `output` variable.
        exprs.last().unwrap()._eq(output)
    }
}
```

### The Synthesizer

The `Synthesizer` structure solves one synthesis problem for us. It takes a
library and spec upon construction, and then we can configure how it will run
with a few builder-style methods, and then finally we call its `synthesize`
method to actually kick off the CEGIS loop.

```
/// A program synthesizer for creating a component-
/// based, loop-free program.
pub struct Synthesizer<'a> {
    // ...
}

impl<'a> Synthesizer<'a> {
    /// Create a new synthesizer with the given
    /// library and specification.
    ///
    /// After creation, we have the opportunity
    /// to configure the synthesis process with
    /// the various builder-style methods.
    pub fn new(
        context: &'a z3::Context,
        library: &'a Library,
        spec: &'a dyn Specification,
    ) -> Result<Self> {
        // ...
    }

    /// Configure whether we should require synthesis
    /// to find the minimal-length program that
    /// satisfies the specification.
    ///
    /// This produces the optimally smallest possible
    /// program, but it tends to take more time.
    pub fn should_synthesize_minimal_programs(
        &mut self,
        should: bool,
    ) -> &mut Self {
        // ...
    }

    /// Configure the timeout.
    ///
    /// No timeout means that we will keep going forever
    /// if necessary. Providing a number of milliseconds
    /// means we will have a soft maximum runtime of of
    /// that many milliseconds before giving up.
    pub fn set_timeout(
        &mut self,
        milliseconds: Option<u32>,
    ) -> &mut Self {
        // ...
    }

    /// Run this configured synthesizer to find a
    /// program that satisfies the specification!
    pub fn synthesize(
        &mut self,
    ) -> Result<Program> {
        // ...
    }
}
```

This allows us to create, configure, and run a synthesis problem like this:

```
let program = Synthesizer::new(&context, &library, &spec)
    .should_synthesize_minimal_programs(true)
    .set_timeout(Some(60 * 60 * 1000))
    .synthesize()?;
```

### Location Mappings

A location mapping uses a bunch of line indices to represent a component-based
program. Lines are something we can represent directly in SMT expressions, and
so location mappings are how we will encode programs for synthesis.

We have the choice of either encoding a line as a mathematical integer, or as a
bitvector. I originally used mathematical integers, and perhaps unsurprisingly,
it is way slower than using a bitvector. By using a bitvector representation, we
can use the minimal number of bits required for our library of components. For
example, if there is one program input and seven components in the library, the
largest zero-based line number we will ever need is seven, which means we only
need bitvectors that are three bits wide to represent every line. The narrower
the bitvector, the faster Z3 can work with it. I haven’t seen line
representation mentioned in any of the papers I’ve read, but I’m sure it is
tribal knowledge that “everyone knows.”

```
// The index of a line that a component is located
// at, or gets a parameter from.
type Line<'a> = BitVec<'a>;
```

Location mappings are used differently at different phases of CEGIS. Before we
synthesize a program, they are a collection of unbound variables in an SMT query
that we’re constructing. After synthesis, those variables get bound to concrete
values and we only want to work with the values from then on; we don’t need the
variables anymore. Therefore, we split the location mapping into two distinct
representations:

1. Before and during finite synthesis we have `LocationVars`, which is a
   collection of line variables.
2. After finite synthesis, we pull the values assigned to those variables out
   into an `Assignments` structure that is a collection of index values.

A `LocationVars` has line variables for the program inputs \(\vec{I}\), for
all the components’ parameters \(\textbf{P}\), for all the components’
temporary results \(\textbf{R}\), and for the whole program’s output
\(O\). It also keeps track of how wide our line location bitvectors are.

```
struct LocationVars<'a> {
    // Variables for lines assigned to program inputs.
    // These are always assigned `0..inputs.len()`.
    inputs: Vec<Line<'a>>,

    // `params[i]` is the variable for the line that
    // defines the `i`th component parameter.
    params: Vec<Line<'a>>,

    // `results[i]` is the variable for the line on
    // which the `i`th component is placed in the
    // synthesized program, and therefore where the
    // `i`th component's temporary result is defined.
    results: Vec<Line<'a>>,

    // The variable for the line on which the program's
    // output is defined.
    output: Line<'a>,

    // The minimum bit width necessary to represent
    // any line location.
    line_bit_width: u32,
}
```

Unlike the original paper, we do not always take the program output from the
last line in the synthesized location mapping. Instead, we allow setting the
`output` line earlier in the program, essentially inserting early returns. This
lets us (optionally) synthesize programs with optimal code size: we can find the
earliest `output` line for which we can still synthesize a correct program. This
little trick is taken from [Souper](https://github.com/google/souper).

The `Assignments` are all those same things, but instead of the variable for the
line, we have the value of the line that we pulled out of the model the SMT
solver gave us. It also has any synthesized immediate values.

```
struct Assignments {
    // Synthesized immediate values.
    immediates: Vec<u64>,

    // `params[i]` is the line in the program where the
    // `i`th parameter is defined.
    params: Vec<u32>,

    // `results[i]` is the line in the program where the
    // `i`th component is located, and therefore the
    // `i`th temporary result is defined.
    results: Vec<u32>,

    // The line where the program's final output is
    // defined.
    output: u32,
}
```

### Verification

Verification takes an `Assignment` produced by finite synthesis, and attempts
find a counterexample. If it finds one, then we need to continue the CEGIS
loop. If it can’t find a counterexample, then we’ve found a solution and we’re
done.

In the original paper, they represent the candidate program in the verification
query with \(\phi\_\mathrm{lib}\) and \(\phi\_\mathrm{conn}\), essentially
asking the solver to interpret the connections between components. This is what
I originally did as well, but then I had a realization:

* We already need to have the ability to turn an `Assignments` into a `Program`
  for when we find a solution.
* We can already turn a `Program` into an SMT expression, since we use
  unoptimized programs as specifications for finding optimized ones.

That means we can convert our `Assignments` into a `Program` and then into an
SMT expression. Why not verify that this SMT expression implies the
specification directly? This means that

* we don’t need to construct \(\phi\_\mathrm{lib}\) and
  \(\phi\_\mathrm{conn}\) during verification,
* the solver doesn’t need to unify all the connections between components’
  inputs and outputs in \(\phi\_\mathrm{conn}\) to solve the verification
  query, and
* this should generally create smaller queries, which should generally be faster
  to solve than larger queries.

This *did* end up saving a little bit of code in the implementation, but does
*not* seem to have yielded a speed up for overall synthesis time. Probably
because nearly all time is spent in finite synthesis, and not verification.

Anyways, here is the verification implementation:

```
impl<'a> Synthesizer<'a> {
    fn verification(
        &mut self,
        assignments: &Assignments,
        bit_width: u32,
    ) -> Result<Verification> {
        // Create fresh input and output variables.
        let inputs: Vec<_> = (0..self.spec.arity())
            .map(|_| {
                fresh_input(self.context, bit_width)
            })
            .collect();
        let output = fresh_output(
            self.context,
            bit_width,
        );

        // Convert the assignments into a program, and
        // then convert that into an SMT expression.
        let mut prog = assignments
            .to_program(self.spec.arity(), self.library)
            .make_expression(
                self.context,
                &inputs,
                &output,
                bit_width,
            );

        let spec = self
            .spec
            .make_expression(
                self.context,
                &inputs,
                &output,
                bit_width,
            );

        // Are there any inputs to our program for
        // which the specification is not upheld?
        let not_spec = spec.not();
        let query = prog.and(&[&not_spec]);
        let solver = self.solver();
        solver.assert(&query);

        match solver.check() {
            // We don't know whether there is a
            // counterexample or not. This typically
            // means that we hit a timeout limit that
            // was previously configured.
            z3::SatResult::Unknown => {
                Err(Error::SynthesisUnknown)
            }

            // There are no more inputs that don't
            // satisfy the spec! We're done!
            z3::SatResult::Unsat => {
                Ok(Verification::WorksForAllInputs)
            }

            // There still exist inputs for which the
            // synthesized program does not satisfy the
            // spec. Return the counterexample.
            z3::SatResult::Sat => {
                let model = solver.get_model();
                self.add_invalid_assignment(assignments);
                let inputs = eval_bitvecs(
                    &model,
                    &inputs,
                );
                Ok(Verification::Counterexample(inputs))
            }
        }
    }
}
```

In the case where verification finds a counterexample, we make a call to the
`add_invalid_assignment` method. This is another trick taken from Souper: we
remember assignments that work for some inputs, but not all of them, and
explicitly forbid them in future finite synthesis queries. This saves the SMT
solver from reconsidering these seemingly promising assignments, only to find
once again that they don’t work for one of the example inputs.

### Finite Synthesis

Recall that finite synthesis searches for a location mapping that satisfies the
specification for each of our example inputs, but might or might not satisfy the
specification when given other inputs.

The first constraint on the location mapping is that it corresponds to a
well-formed program. This constraint actually remains the same for every
iteration of CEGIS, so we generate the constraint once when creating a new
`Synthesizer` instance, and then reuse the already constructed constraint for
each finite synthesis query. Similarly, we also store the location variables in
the `Synthesizer` and reuse them across all iterations of the CEGIS loop.

```
pub struct Synthesizer<'a> {
    // ...
    locations: LocationVars<'a>,
    well_formed_program: Bool<'a>,
    // ...
}
```

Recall the definition of the \(\psi\_\mathrm{wfp}\) well-formed program
constraint:

> \(
> \begin{align}
> \psi\_\mathrm{wfp}(L) &= \bigwedge\limits\_{p \in \textbf{P}} \left( 0 \leq l\_p \lt M \right) \\
> & \land \, \bigwedge\limits\_{r \in \textbf{R}} \left( \lvert \vec{I} \rvert \leq l\_r \lt M \right) \\
> & \land \, \psi\_\mathrm{cons}(L) \\
> & \land \, \psi\_\mathrm{acyc}(L)
> \end{align}
> \)

It says that each parameter location \(l\_p\) falls within the range \(0 \leq
l\_p < M \), each temporary result location \(l\_r\) falls within the range
\(\lvert \vec{I} \rvert \leq l\_r < M\), that the locations are consistent, and
that there are no dataflow cycles.

Constructing the equivalent SMT expression in Z3 follows pretty much directly
from that, except it is a bit noisier, since we’re passing contexts around and
need to convert Rust `usize`s and `u32`s into Z3 bitvectors of the appropriate
width:

```
impl<'a> LocationVars<'a> {
    fn well_formed_program(
        &self,
        context: &'a z3::Context,
        library: &Library,
        invalid_connections: &mut HashSet<(u32, u32)>,
    ) -> Bool<'a> {
        // We'll build up all of our well-formed program
        // constraints in this list, and then `and` them
        // all together at the end.
        let mut wfp = vec![];

        // A well-formed program is consistent.
        wfp.push(self.consistent(
            context,
            invalid_connections,
        ));

        // A well-formed program is acyclic.
        wfp.push(self.acyclic(context, library));

        let i_len = self.line_from_u32(
            context,
            self.inputs.len() as u32,
        );
        let m = self.line_from_u32(
            context,
            (self.results.len() +
                self.inputs.len()) as u32,
        );
        let zero = self.line_from_u32(context, 0);

        // The inputs are always assigned to the first
        // locations.
        for (i, l) in self.inputs.iter().enumerate() {
            let i = self.line_from_u32(
                context,
                i as u32,
            );
            wfp.push(l._eq(&i));
        }

        // All component parameter locations are in
        // the range `0 <= l < M`.
        for l in &self.params {
            // 0 <= l
            wfp.push(line_le(&zero, l));
            // l < M
            wfp.push(line_lt(l, &m));
        }

        // All component result locations are in the
        // range `|i| <= l < M`.
        for l in &self.results {
            // |i| <= l
            wfp.push(line_le(&i_len, l));
            // l < m
            wfp.push(line_lt(l, &m));
        }

        // `and` all of our constraints together.
        and(context, &wfp)
    }
}
```

Remember that the \(\psi\_\mathrm{cons}\) consistency constraint ensures that
we don’t assign two components to the same line:

> \(
> \psi\_\mathrm{cons}(L) =
> \bigwedge\limits\_{x,y \in \textbf{R}, x \not\equiv y} \left( l\_x \neq l\_y \right)
> \)

Our `consistent` method creates the corresponding SMT expression for Z3, and
additionally records pairs of location indices into the `invalid_connections`
map. This map keeps a record of location variables that well-formed programs
*cannot* have dataflow between. Therefore, we don’t need to add connection
clauses for these pairs of location variables in our eventual implementation of
the \(\psi\_\mathrm{conn}\) connectivity constraint. Leaving those pairs out of
the connectivity constraint keeps the SMT expressoin that much smaller, which
should help Z3 solve it that much faster. Once again, this trick was taken from
Souper.

```
impl LocationVars<'a> {
    fn consistent(
        &self,
        context: &'a z3::Context,
        invalid_connections: &mut HashSet<(u32, u32)>,
    ) -> Bool<'a> {
        // Build up all the consistency constraints
        // in this list.
        let mut cons = vec![];

        for (i, (index_x, loc_x)) in self
            .results_range()
            .zip(&self.results)
            .enumerate()
        {
            for (index_y, loc_y) in self
                .results_range()
                .zip(&self.results)
                .skip(i + 1)
            {
                // Can't have dataflow from a result to
                // another result directly, they need to
                // be connected through parameters, so
                // add this pair to the invalid
                // connections map.
                invalid_connections.insert(
                    (index_x, index_y)
                );

                // Components cannot be assigned to the
                // same line, so these location variables
                // cannot have the same value:
                // `loc_x != loc_y`.
                cons.push(loc_x._eq(loc_y).not());
            }
        }

        // `and` all the constraints together.
        and(context, &cons)
    }
}
```

The \(\psi\_\mathrm{acyc}\) acyclicity constraint enforces that our synthesized
location mappings don’t have dataflow cycles:

> \(
> \psi\_\mathrm{acyc}(L) =
> \bigwedge\limits\_{i=0}^{N-1}
> \left(
> \bigwedge\limits\_{p \in \vec{I}\_i} \left( l\_p < l\_{O\_i} \right)
> \right)
> \)

Our implementation of the acyclicity constraint doesn’t do anything fancy, and
is just a direct translation of the constraints into an SMT expression:

```
impl LocationVars<'a> {
    fn acyclic(
        &self,
        context: &'a z3::Context,
        library: &Library,
    ) -> Bool<'a> {
        // Build up the constraints in this list.
        let mut acycs = vec![];

        let mut params = self.params.iter();

        for (result_loc, comp) in self
            .results
            .iter()
            .zip(&library.components)
        {
            for _ in 0..c.operand_arity() {
                let param_loc = params.next().unwrap();

                // The component's param's location
                // must be less than the component's
                // result's location, meaning the
                // param is already defined before it
                // is used: `param_loc < result_loc`.
                acycs.push(
                    line_lt(param_loc, result_loc)
                );
            }
        }

        // `and` all the constraints together.
        and(context, &acycs)
    }
}
```

Our next steps are implementing the \(\psi\_\mathrm{conn}\) connectivity
constraint and the \(\phi\_\mathrm{lib}\) library specification. These do
change with each iteration of the CEGIS loop, because we instantiate them for
each example input we’re working with. That means we can’t cache-and-reuse them,
like we do with the well-formed program constraint.

The \(\psi\_\mathrm{conn}\) connectivity constraint encodes the dataflow
connections between components in the library. If two location variables refer
to the same location, then the entities whose location is assigned by those
variables must have the same value.

> \( \psi\_\mathrm{conn}(L, \vec{I}, O, \textbf{P}, \textbf{R}) = \bigwedge\limits\_{x,y \in \vec{I} \cup \textbf{P} \cup \textbf{R} \cup { O } } \left( \left( l\_x = l\_y \right) \implies \left( x = y \right) \right) \)

The `connectivity` method constructs a Z3 expression that implements this
constraint. Previously, we had recorded pairs of location variables that cannot
be connected directly. Now, we filter out any such connections from this
constraint, keeping the SMT expression smaller, as explained earlier.

```
impl<'a> Synthesizer<'a> {
    fn connectivity(
        &self,
        inputs: &[BitVec<'a>],
        output: &BitVec<'a>,
        params: &[BitVec<'a>],
        results: &[BitVec<'a>],
    ) -> Bool<'a> {
        // A table mapping a location variable's index
        // to the location variable and its associated
        // entity: `index -> (l[x], x)`.
        let locs_to_vars: Vec<_> = self
            .locations
            .inputs
            .iter()
            .zip(inputs)
            .chain(
                self.locations
                    .params
                    .iter()
                    .zip(params)
            )
            .chain(
                self.locations
                    .results
                    .iter()
                    .zip(results)
            )
            .chain(iter::once(
                (&self.locations.output, output)
            ))
            .collect();

        // Build up the constraints in this list.
        let mut conn = vec![];

        for (index_x, (l_x, x)) in locs_to_vars
            .iter()
            .enumerate()
        {
            for (index_y, (l_y, y)) in locs_to_vars
                .iter()
                .enumerate()
                .skip(i + 1)
            {
                // If these locations can't ever be
                // connected directly, don't bother
                // constraining them.
                if self.is_invalid_connection(
                    index_x as u32,
                    index_y as u32,
                ) {
                    continue;
                }

                // If these two location variables
                // refer to the same location, then
                // their entities are connected to
                // each other, and must have the
                // same value.
                conn.push(
                    l_x._eq(l_y).implies(&x._eq(y))
                );
            }
        }

        // `and` all the constraints together.
        and(self.context, &conn)
    }
}
```

Our final prerequisite before we can implement the whole finite synthesis query
is the \(\phi\_\mathrm{lib}\) library specification, which describes the
behavior of the library as a whole:

> \( \phi\_\mathrm{lib}(\textbf{P}, \textbf{R}) = \phi\_i(\vec{I}\_0, O\_0) \land \ldots \land \phi\_i(\vec{I}\_{N-1}, O\_{N-1}) \)

Implementing the \(\phi\_\mathrm{lib}\) library specification involves getting
the immediates, operands, and result variables for each component, asking the
component to make its SMT expression relating those variables to each other, and
finally *and*ing all those expressions together:

```
impl<'a> Synthesizer<'a> {
    fn library(
        &self,
        immediates: &[BitVec<'a>],
        params: &[BitVec<'a>],
        results: &[BitVec<'a>],
        bit_width: u32,
    ) -> Bool<'a> {
        // Build up each component's spec expression
        // in here.
        let mut lib = vec![];

        let mut immediates = immediates;
        let mut params = params;

        for (result, comp) in results
            .iter()
            .zip(&self.library.components)
        {
            // Chop the immediates for this component off
            // the front of the list.
            let (these_imms, rest) = immediates.split_at(
                comp.immediate_arity()
            );
            immediates = rest;

            // Chop the params for this component off the
            // front of the list.
            let (these_params, rest) = params.split_at(
                comp.operand_arity()
            );
            params = rest;

            // Create the spec for this component, and
            // make sure its result is constrained by it.
            lib.push(
                result._eq(&comp.make_expression(
                    self.context,
                    these_imms,
                    these_params,
                    bit_width,
                ))
            );
        }

        // `and` all of the component specs together.
        and(self.context, &lib)
    }
}
```

Ok, we finally have all the functions we need to implement finite synthesis! The
finite synthesis query assigns values to our location variables such that the
resulting mapping corresponds to a well-formed program, and that program
satisfies our specification for each of our example inputs.

> \(
> \begin{align}
> & \exists L, O\_0, \ldots, O\_{\vert S \rvert - 1}, \textbf{P}\_0, \ldots, \textbf{P}\_{\vert S \rvert - 1}, \textbf{R}\_0, \ldots, \textbf{R}\_{\vert S \rvert - 1}: \\
> & \qquad \psi\_\mathrm{wfp}(L) \,\, \land \\
> & \qquad \qquad \bigwedge\limits\_{i=0}^{\lvert S \rvert - 1} \left( \phi\_\mathrm{lib}(\textbf{P}\_i, \textbf{R}\_i) \land \psi\_\mathrm{conn}(L, S\_i, O\_i, \textbf{P}\_i, \textbf{R}\_i) \land \phi\_\mathrm{spec}(S\_i, O\_i) \right) \\
> \end{align}
> \)

Our implementation of the finite synthesis query mostly follows the same
structure as that formula:

* We already have the well-formed program constraint cached and ready for reuse,
  so we don’t need to recreate it here.
* We loop over each of our example inputs:

  + Create fresh program output variables, fresh component parameter variables,
    and fresh component result variables for each example.
  + Constrain each component’s parameters and output to behave as dictated by
    our library.
  + Connect cross-component variables together as described by the location
    mapping, with the connectivity constraint.
  + Require that the program specification is satisfied for this example input.
* Additionally, we assign the program’s output’s location to the line we were
  given. This lets callers optionally force the synthesis of optimally small
  programs.
* Finally, we run the query and parse the resulting location mapping’s
  assignments out of the solver’s model.

```
impl<'a> Synthesizer<'a> {
    fn finite_synthesis(
        &mut self,
        example_inputs: &HashSet<Vec<u64>>,
        output_line: u32,
        bit_width: u32,
    ) -> Result<Assignments> {
        let immediates = self.fresh_immediates(
            bit_width
        );

        // We'll build up the constraints that the
        // location assignments work for each input
        // in this list.
        let mut works_for_inputs = vec![];

        for inputs in example_inputs {
            // Convert the inputs into bitvectors.
            let inputs: Vec<_> = inputs
                .iter()
                .map(|i| BitVec::from_i64(
                    self.context,
                    *i as i64,
                    bit_width,
                ))
                .collect();

            // Create fresh params, results, and
            // output variables. These are the
            // existentially-quantified `P[i]`,
            // `R[i]`, and `O[i]` from the formula.
            let params = self.fresh_param_vars(
                bit_width
            );
            let results = self.fresh_result_vars(
                bit_width
            );
            let output = fresh_output(
                self.context,
                bit_width,
            );

            // The components behave as described by
            // the library.
            let lib = self.library(
                &immediates,
                &params,
                &results,
                bit_width,
            );
            works_for_inputs.push(lib);

            // The components are connected together as
            // described by the location variables.
            let conn = self.connectivity(
                &inputs,
                &output,
                &params,
                &results,
            );
            works_for_inputs.push(conn);

            // And given that, our specification for
            // desired program behavior is satisified.
            let spec = self
                .spec
                .make_expression(
                    self.context,
                    &inputs,
                    &output,
                    bit_width,
                );
            works_for_inputs.push(spec);
        }

        let works_for_inputs: Vec<&_> = works_for_inputs
            .iter()
            .collect();

        // Enforce that the output is on the required
        // line.
        let output_line = self.locations.line_from_u32(
            self.context,
            output_line,
        );
        let output_on_line = self
            .locations
            .output
            ._eq(&output_line);

        // Put all the pieces together!
        let query = self
            .well_formed_program
            .and(&works_for_inputs)
            .and(&[
                &output_on_line,
                // Do not synthesize any of the
                // assignments we've already
                // discovered to be invalid.
                &self.not_invalid_assignments,
            ]);

        let solver = self.solver();
        solver.assert(&query);

        match solver.check() {
            // It is unknown whether an assignment
            // that fits the constraints exists or
            // not. Usually this is because a timeout
            // was configured and we ran out of time.
            z3::SatResult::Unknown => {
                Err(Error::SynthesisUnknown)
            }

            // There are no assignments for the
            // location variables that satisfies our
            // synthesis constraints. We can't create
            // a program that satisfies the spec with
            // this component library.
            z3::SatResult::Unsat => {
                Err(Error::SynthesisUnsatisfiable)
            }

            // Ok, we have an assignment for the
            // location variables that fits our
            // synthesis constraints! Pull them out
            // of the model and return them.
            z3::SatResult::Sat => {
                let model = solver.get_model();

                let immediates = eval_bitvecs(
                    &model,
                    &immediates,
                );

                let params = eval_lines(
                    &model,
                    &self.locations.params
                );

                let results = eval_lines(
                    &model,
                    &self.locations.results,
                );

                let output = eval_line(
                    &model,
                    &output_line,
                );

                Ok(Assignments {
                    immediates,
                    params,
                    results,
                    output,
                })
            }
        }
    }
}
```

### The CEGIS Loop

When the synthesizer is configured to produce optimally small programs, we wrap
the CEGIS loop in another loop, similar to how Souper does. Souper begins
synthesizing at the shortest program length and then allows longer and longer
programs until it finds an optimally short solution. In contrast, we start by
synthesizing the longest programs that can be expressed with the given library
first, and then try shorter and shorter programs from there. This is motivated
by two insights:

1. In practice, it appears that a failed search for a program of length `n-1`,
   because no such program exists, takes much longer than searching for and
   successfully finding a program of length `n`. By iterating longest to
   shortest target program lengths, we only hit the expensive case once.
2. When we synthesize a longer-than-necessary program, often that program
   contains dead code. Running [dead code elimination (DCE)](https://en.wikipedia.org/wiki/Dead_code_elimination) on a loop-free
   program is super easy, and when the dead code is removed, it additionally
   lets us skip ahead a bunch of iterations in this loop.

When the synthesizer is not configured to produce optimally small programs, we
adjust the range of target program lengths such that we only call into the CEGIS
loop once. We accomplish this by setting the shortest length equal to the
longest length.

```
impl<'a> Synthesizer<'a> {
    pub fn synthesize(
        &mut self,
    ) -> Result<Program> {
        let mut example_inputs = self
            .initial_concrete_inputs()?;

        // The length of the longest program we can
        // synthesize with this library.
        let longest = self.spec.arity() as u32
            + self.library.components.len() as u32;

        // The shortest length program we'll attempt to
        // synthesize.
        let shortest = if self
            .should_synthesize_minimal_programs
        {
            self.spec.arity() as u32 + 1
        } else {
            longest
        };

        // In practice, the cost of searching for a
        // program of length `n-1` when no such program
        // exists is much more expensive than
        // successfully searching for a program of
        // length `n`. Therefore, start synthesizing
        // longer programs first, shortening the length
        // as we iterate.
        let mut best = Err(Error::SynthesisUnknown);
        let mut target_length = longest;
        while target_length >= shortest {
            // Call into the CEGIS loop, synthesizing
            // a program of the current target length.
            match self.synthesize_with_length(
                target_length,
                &mut example_inputs,
            ) {
                // We found a program at this length --
                // it's our new `best`!
                //
                // Run DCE on it, potentially allowing us
                // to skip a few iterations of this loop,
                // and then search for a program that is
                // one instruction shorter than it.
                Ok(mut program) => {
                    program.dce();
                    target_length =
                        program.instructions.len() as u32
                        - 1;
                    best = Ok(program);

                    // Reset the invalid-assignments set,
                    // since an assignment that was an
                    // invalid program when returning
                    // line `i` might be valid when
                    // returning line `i-1`.
                    self.reset_invalid_assignments();
                    continue;
                }

                // We can't synthesize a program with the
                // target length, or we timed out. Return
                // our current `best` result, or if we
                // don't have one, return this error.
                err => return best.or_else(|_| err),
            }
        }

        // If we completed the loop without ever failing
        // to synthesize a program and then early
        // returning, that means we have a program of
        // length `shortest` on our hands. Return it!
        best
    }
}
```

Originally, this implementation was choosing the initial example inputs with a
random number generator. After reading through the Souper sources, I saw that
they are presenting the program specification to the solver with all the inputs
and output variables unbound. Then they have solver solve for example inputs
itself. These inputs are presumably more “interesting” than what a random number
generator might choose, which should in turn help finite synthesis come up with
better solutions more quickly.

I implemented this technique for our synthesizer and additionally constrain the
input variables to be distinct from any that we’ve already added to our initial
inputs \(S\).

Here’s the logic formula for the find-an-example-input query:

> \(
> \begin{align}
> & \exists \vec{I}, O: \\
> & \qquad \phi\_\mathrm{spec}(\vec{I}, O) \land \bigwedge\limits\_{i=0}^{\lvert S \rvert - 1} \left( \vec{I} \neq S\_i \right)
> \end{align}
> \)

And here’s its breakdown:

|  |  |
| --- | --- |
| \( \exists \vec{I}, O: \) | Find some inputs \(\vec{I}\) and output \(O\) such that |
| \( \phi\_\mathrm{spec}(\vec{I}, O) \) | our specification is satisfied |
| \(\land\) | and |
| \( \bigwedge\limits\_{i=0}^{\lvert S \rvert - 1} \left( \vec{I} \neq S\_i \right) \) | we don't already have those inputs in our list of example inputs \(S\). |

The `initial_concrete_inputs` method constructs this query, passes it to Z3, and
pulls each discovered example out of each query’s resulting model:

```
impl<'a> Synthesizer<'a> {
    fn initial_concrete_inputs(
        &mut self,
    ) -> Result<HashSet<Vec<u64>>> {
        // Shamelessly cargo cult'd from Souper.
        const NUM_INITIAL_INPUTS: usize = 4;

        let mut inputs: HashSet<Vec<u64>> =
            HashSet::with_capacity(NUM_INITIAL_INPUTS);

        // Create unbound inputs and output variables.
        let input_vars: Vec<_> = (0..self.spec.arity())
            .map(|_| fresh_input(
                self.context,
                FULL_BIT_WIDTH,
            ))
            .collect();
        let output_var = fresh_output(
            self.context,
            FULL_BIT_WIDTH,
        );

        let spec = self.spec.make_expression(
            self.context,
            &input_vars,
            &output_var,
            FULL_BIT_WIDTH,
        );

        for _ in 0..NUM_INITIAL_INPUTS {
            // Make sure that we find unique new
            // inputs by constraining the input
            // vars to be not equal to any of the
            // ones we've already found.
            let mut existing_inputs = vec![];
            for input_set in &inputs {
                // Build up all the expressions
                // `var[i] == input_set[i]` in
                // `eq_this_input`.
                let mut eq_this_input = vec![];
                for (inp, var) in input_set
                    .iter()
                    .zip(&input_vars)
                {
                    let inp = BitVec::from_i64(
                        self.context,
                        *inp as i64,
                        FULL_BIT_WIDTH,
                    );
                    eq_this_input.push(inp._eq(var));
                }
                let eq_this_input = and(
                    self.context,
                    &eq_this_input,
                );
                existing_inputs.push(eq_this_input);
            }

            // The new inputs should not be equal
            // to any of the existing inputs
            let not_existing_inputs = or(
                self.context,
                &existing_inputs,
            ).not();

            let query = spec.and(&[
                &not_existing_inputs,
            ]);

            let solver = self.solver();
            solver.assert(&query);

            match solver.check() {
                // If the result is unknown, try and
                // use the examples we've already got,
                // but if we don't have any, just bail
                // out now.
                z3::SatResult::Unknown => {
                    if inputs.is_empty() {
                        return Err(
                            Error::SynthesisUnknown
                        );
                    } else {
                        break;
                    }
                }

                // If the query is unsatisfiable, then
                // our spec is bogus.
                z3::SatResult::Unsat => {
                    return Err(
                        Error::SynthesisUnsatisfiable
                    );
                }

                // Found some example inputs, so pull
                // them out of the model and add them
                // to our set.
                z3::SatResult::Sat => {
                    let model = solver.get_model();
                    let new_inputs = eval_bitvecs(
                        &model,
                        &input_vars,
                    );
                    inputs.insert(new_inputs);
                }
            }
        }

        Ok(inputs)
    }
}
```

Alright so now we are ready to examine the implementation of our inner CEGIS
loop!

Close readers will have noticed all the `bit_width` parameters being passed
around everywhere and the usage of a `FULL_BIT_WIDTH` constant in earlier code
samples. That’s because we implement the well-known optimization of synthesizing
programs initially at narrow bit widths, and then verifying with wider and wider
bit widths until we’ve verified at our target bit width: `FULL_BIT_WIDTH`, aka
32 in this implementation.

This works well because programs that are correct at, say, eight bits wide can
often work just as well at 32 bits wide. Note that this is “often” and not
“always”: widening synthesized constants, in particular, can be troublesome.
However, with many fewer bits for the solver to keep track of, synthesis at
eight bits wide is a lot faster than synthesis at 32 bits wide.

When verifying a program synthesized at a narrower bit width, we verify at the
narrow bit width, and then verify at double that bit width, and then we double
the bit width again, etc… until we’ve reached the full bit width, at which
point we’re done. Whenever verification finds a counterexample, from then on we
synthesize at whatever bit width we’ve reached so far. That is, we’ll never
narrow our current bit width again after widening it.

```
impl<'a> Specification<'a> {
    fn synthesize_with_length(
        &mut self,
        program_length: u32,
        inputs: &mut HashSet<Vec<u64>>,
    ) -> Result<Program> {
        let output_line = program_length - 1;
        let mut bit_width = 2;

        'cegis: loop {
            // Finite synthesis finds some assignments
            // that satisfy the specification for our
            // example inputs at the current bit width.
            let assignments = self.finite_synthesis(
                inputs,
                output_line,
                bit_width,
            )?;

            // Now start the verification and bit width
            // widening loop.
            loop {
                // Verify the assignments at the current
                // bit width.
                match self.verification(
                    &assignments,
                    bit_width,
                )? {
                    // This assignment works for all
                    // inputs at the current bit width!
                    // If we're at our full bit width,
                    // then we have the answer and we're
                    // done. Otherwise, double our bit
                    // width and keep verifying at the
                    // new bit width.
                    Verification::WorksForAllInputs => {
                        if bit_width == FULL_BIT_WIDTH {
                            let program =
                                assignments.to_program(
                                    self.spec.arity(),
                                    self.library,
                                );
                            return Ok(program);
                        } else {
                            bit_width *= 2;
                        }
                    }

                    // Verification found a counter-
                    // example, so add it to our set of
                    // example inputs and try finite
                    // synthesis again.
                    Verification::Counterexample(
                        new_inputs
                    ) => {
                        inputs.insert(new_inputs);
                        continue 'cegis;
                    }
                }
            }
        }
    }
}
```

Results
-------

We have a new program synthesizer, and the natural next question is: how well
does it work? How does it compare to existing synthesizers? Can it solve as many
synthesis problems as other synthesizers? Can it find programs as fast as other
synthesizers can?

First off, our synthesizer can indeed find an optimal solution for isolating the
rightmost zero bit in a word! However, there are multiple optimal solutions, and
it doesn’t always find the one that’s exactly how we would probably write it by
hand. According to our synthesizer’s cost model, which is just number of
instructions used, a less-than-or-equal comparison that always evaluates to true
is just as good as a `const 1`:

```
a ← var           // a = 011010011
b ← le_u a, a     // b = 000000001 (aka `b ← const 1`)
c ← add a, b      // c = 011010100
d ← xor c, a      // d = 000000111
e ← and d, c      // e = 000000100
```

Phew!

The *Synthesis of Loop-Free Programs* paper by Gulwani et al defines a benchmark
suite of 25 bitvector problems taken from the big book of bit-twiddling hacks,
[*Hacker’s Delight*](https://www.goodreads.com/book/show/276079.Hacker_s_Delight). They use it to benchmark their program
synthesizer, Brahma. Our running example of isolating the rightmost zero bit in
a word is the seventh problem in the benchmark suite. Other benchmark problems
include:

* turning off the rightmost one bit in a word,
* taking the average of two integers without overflow,
* rounding up to the next power of two,
* etc…

The problems are roughly ordered in increasing difficulty: the first problem is
much easier than the last problem.

They use a standard library of twelve base components for the first seventeen
problems. For the last eight problems, they augment that library with additional
components, depending on the problem at hand.

I ported the benchmark problems into `Program`s that can be fed into our
synthesizer as specifications, and created a small runner that times how long it
takes our synthesizer to rediscover solutions to these problems.

Porting their standard library over to our synthesizer required some small
changes. For example, our language does not allow immediates in the `add`
operation, so their `add1` component becomes two components in our library: an
`add` component and a `const 1` component. There are a couple other instances
where they had a single component that corresponded to multiple operations. We
don’t support that scenario, so I split those components into multiple
components when porting them over to our synthesizer. Additionally, for the
later, more difficult problems, I used the minimal library required to solve the
problem, since these more difficult problems are prone to take quite a long
time.

For these benchmarks, I’m using Z3 version 4.4.1 which comes in my OS’s package
manager. Brahma used the Yices solver, and my understanding is that Souper can
plug in a few different solvers, including Z3.

Our goal here is only to get a general sense of our synthesizer’s
performance. We are *not* precisely evaluating our synthesizer’s performance and
comparing it with Brahma in excruciating detail because this isn’t an
apples-to-apples comparison. But we should get a sense of whether anything is
horribly off.

All problems are run with a timeout of one hour, meaning that if we can’t find a
solution in that amount of time, we give up and move on to the next problem. For
comparison, the longest that Brahma took on any problem was 46 minutes.

First, I measured how long it takes to synthesize a program of *any* length for
each problem. Next, I measured how long it takes to synthesize an *optimally
small* program for each problem. Finally, I measured how long it takes to
synthesize both an optimally small program and the constant values used in each
`const` operation, rather than being given the necessary constant value as part
of the `const` component.

The results are summarized in the table below, alongside the results reported in
the paper for their Brahma synthesizer. The timings are in units of seconds.

| Benchmark | Brahma | Our Synthesizer | | |
| --- | --- | --- | --- | --- |
|  |  | Any Length | Min. Length | Min. Length & Synth. Constants |
| p1 | 3.2 | 0.5 | 109.0 | 170.4 |
| p2 | 3.6 | 1.1 | 136.0 | 99.4 |
| p3 | 1.4 | 0.6 | 32.8 | 31.9 |
| p4 | 3.3 | 0.5 | 100.5 | 130.1 |
| p5 | 2.2 | 0.3 | 125.2 | 119.2 |
| p6 | 2.4 | 0.6 | 96.3 | 87.7 |
| p7 | 1.0 | 0.5 | 100.1 | 80.3 |
| p8 | 1.4 | 1.0 | 90.5 | 77.6 |
| p9 | 5.8 | 36.5 | 241.4 | 165.6 |
| p10 | 76.1 | 6.8 | 34.2 | 42.1 |
| p11 | 57.1 | 4.1 | 31.9 | 36.9 |
| p12 | 67.8 | 11.5 | 30.6 | 52.8 |
| p13 | 6.2 | 20.9 | 129.7 | 165.0 |
| p14 | 59.6 | 85.1 | 1328.7 | 1598.8 |
| p15 | 118.9 | 20.0 | 1897.3 | 1742.7 |
| p16 | 62.3 | 25.2 | 3600.0\* | 3600.0\* |
| p17 | 78.1 | 8.2 | 102.0 | 243.5 |
| p18 | 45.9 | 1.5 | 27.4 | 33.5 |
| p19 | 34.7 | 3.3 | 10.0 | 6.0 |
| p20 | 108.4 | 757.5 | 3600.1\* | 3600.0\* |
| p21 | 28.3 | timeout | timeout | timeout |
| p22 | 279.0 | timeout | timeout | timeout |
| p23 | 1668.0 | Z3 crash | timeout | timeout |
| p24 | 224.9 | timeout | timeout | timeout |
| p25 | 2778.7 | timeout | timeout | timeout |

\* For these problems, the synthesizer found *a* solution, but not necessarily the optimally small solution. It timed out before it could complete the search and either discover or rule out the existence of smaller programs.

For the easier, early problems, our synthesizer does pretty well. Finding an
optimally small program takes much longer than finding a program of any
length. Synthesizing constants doesn’t seem to add much overhead to synthesis
over finding an optimally small program. Our synthesizer hits some sort of cliff
around problems 20 and 21, and run times start skyrocketing and running into the
timeout ceiling.

Problem 23 is to synthesize an implementation of popcount. Brahma solves the
problem in just under 28 minutes. The Souper folks report that they can solve
this problem as well, although they do say that their synthesizer scales less
well than Braham does. When I was running this benchmark, Z3 repeatedly crashed
while trying to solve a finite synthesis query. Ultimately, the synthesizer
wasn’t able to complete the problem. I ran earlier versions of our synthesizer
on this problem during development, when Z3 wasn’t crashing, and I was still
never able to synthesize a program for popcount. I let the synthesizer run for
nearly three days, and it couldn’t do it.

Maybe Yices is much better at solving these sorts of queries than Z3 is?
Perhaps there are some well-known optimizations to make these queries easier for
solvers to solve, and I’m just ignorant of them? Maybe the fact that compound
components get split into multiple components in our library, resulting in a
larger library and more location variables to solve for, is the root of the
problem? I don’t know.

This performance cliff with larger synthesis problems is my one disappointment
with this project. If anyone has ideas about why the synthesizer is falling off
this cliff, or how to profile Z3 and dig into why it is struggling with these
queries, I’d love to hear from you. Particularly if you have experience with
this kind of program synthesis. SMT solvers are very much a black box to me
right now.

Conclusion
----------

Counterexample-guided iterative synthesis is a wonderfully clever way to
transform a single problem that is too difficult for SMT solvers to solve, into
multiple little problems, each of which off-the-shelf solvers can handle.
Inverting the representation of a component-based program into a location
mapping, so that it can be wholly represented inside an SMT query, is equally
deft.

Program synthesis — writing programs that write other programs — is
fun and delightful in a meta, ouroboros-y sense. It also foretells a future
where we can mechanically generate large swaths of an optimizing compiler’s
backend. A future where compilers emit actually *optimal* code sequences. I find
that lofty promise exciting, but I’m also frustrated by my lack of insight into
SMT solver performance. There do exist other approaches to program synthesis
that only rely on SMT solvers for verification, and not for finite
synthesis. However, it seems premature to give up on this approach when I
haven’t yet reproduced the results reported for Brahma and Souper. Nonetheless,
I remain optimistic, and I intend to keep digging in until I resolve these
discrepancies.

Thanks for reading!

References
----------

* [`fitzgen/synth-loop-free-prog`:](https://github.com/fitzgen/synth-loop-free-prog) The git repository for the
  synthesizer described in this post!
* [*Synthesis of Loop-Free Programs* by Gulwani et al:](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/12/pldi11-loopfree-synthesis.pdf)
  This is the paper that most of this post is based upon! A great paper, and you
  should read it if you found this interesting!
* [*Program Synthesis* by Gulwani et
  al:](https://www.microsoft.com/en-us/research/wp-content/uploads/2017/10/program_synthesis_now.pdf)
  A survey paper summarizing the state of the art for program synthesis. A great
  way to quickly get an overview of the whole field!
* [*A Synthesizing Superoptimizer* by Sasnauskas et
  al:](https://arxiv.org/pdf/1711.04422.pdf) This paper describes [Souper](https://github.com/google/souper), a
  superoptimizer for LLVM that uses program synthesis at its core. Souper’s
  synthesizer is also based on the Gulwani paper, but extends it in a few
  different ways. I’ve looked through its sources quite a bit to find
  optimizations and tricks!
* [*Automatic Generation of Peephole Superoptimizers* by Bansal et
  al:](https://theory.stanford.edu/~aiken/publications/papers/asplos06.pdf) The first paper describing how to generate a table-driven
  peephole optimizer offline with a superoptimizer.
* [*Hacker’s Delight* by Henry S. Warren:](https://www.goodreads.com/book/show/276079.Hacker_s_Delight) A book dedicated to
  concise and non-obvious bit twiddling tricks. It is an incredible book if
  you’re into that sort of thing! The benchmark problems presented in the
  *Synthesis of Loop-Free Programs* paper are taken from this book.
* [SyGuS:](https://sygus.org/) SyGuS, or Syntax-Guided Synthesis, formalizes a class of
  program synthesis problems, standardizes a language for describing them, and
  holds a yearly competition for synthesizers. The aim is to drive innovations
  in the field with a little friendly competition.
