---
id: 24
url: https://pithlessly.github.io/1ml-intro
title: '1ML for non-specialists: introduction — Christine''s World Wide Web Site'
domain: pithlessly.github.io
source_date: '2026-01-09'
tags:
- compilers
- tutorial
- academic-paper
- haskell
summary: This article is an introductory guide to 1ML, a type system designed by Andreas
  Rossberg for integrating ML-style module systems into programming languages. The
  author aims to demystify 1ML's technical papers for compiler authors by explaining
  how 1ML functions as syntactic sugar for System Fω (the core type system of Haskell)
  and walking through its key concepts, including the type system architecture, record
  field handling, and semantic types. The series is designed as a companion to Rossberg's
  2018 paper and assumes readers have familiarity with type system notation, ML modules,
  and Fω, with the goal of enabling them to understand 1ML's inference rules and implementation
  details.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# 1ML for non-specialists: introduction — Christine's World Wide Web Site

[@pithlessly](./) · [github](https://github.com/pithlessly) · λ

1ML for non-specialists: introduction
=====================================

Date: 2023-12-25  
Last updated: 2025-12-28

*This is the first entry in what I intend as a multi-part series.*

1ML is a type system designed by Andreas Rossberg and described in
[a collection of papers](https://people.mpi-sws.org/~rossberg/1ml/) by him.
When it comes to integrating an ML-style module system into a new language,
I think 1ML currently provides the best overall story
(although it’s not perfect).

Unfortunately, Rossberg’s papers are pretty technical.
He is a good writer, but I feel that right now there is still a communication barrier
between academics who are in a position to discuss 1ML in depth
and people who are in a position to write new compilers.
I see a lot more discussion online that merely *references* 1ML
than I do discussion that seems to deeply *understand* it.

I’ve been studying 1ML for the last several months,
and working on my own prototype implementation
(which unfortunately isn’t yet in a publishable state).
In an effort to help these ideas percolate down towards mainstream adoption,
I want to help demystify some things that I found confusing.

This series will not substitute for reading the paper,
but I hope it can be a useful companion.
I’ll be working from [the version of the paper published in the Journal of Functional Programming](https://www.cambridge.org/core/journals/journal-of-functional-programming/article/1ml-core-and-modules-united/47B10882829E4B32F98FBA93B28CEF30)
in 2018.
It’ll be very helpful to be able to look at that paper as you read this.
In fact, you can press this button to pull it up on the side in this page:
Open
(It probably doesn’t look great on mobile, unfortunately.)

Prerequisite knowledge
----------------------

In writing this, I assume the reader:

* Has some familiarity with inference rule notation
  and how type systems are defined using a combination of grammars and inference rules.
* Has some familiarity with the module system of OCaml or Standard ML,
  from a user’s perspective (not necessarily knowing their internals).
* Has familiarity with 1ML’s design goals as outlined in the
  [paper introduction](./1ml-common/1ml-jfp-official.pdf#page=1).
* Has *not* necessarily read the prequel, [F-ing modules](https://people.mpi-sws.org/~rossberg/f-ing/),
  Rossberg’s earlier paper on compiling module calculi to Fω.

Goals
-----

By the end of this series of articles,
the reader will have the tools they need
to understand every single inference rule,
including those of the type inference algorithm described in
[Section 7](./1ml-common/1ml-jfp-official.pdf#page=43).

I also want to discuss some implementation concerns that are not mentioned in the paper
(such as how to integrate type inference with levels).

Non-goals
---------

A decent portion of the paper is dedicated to meta-theory
(e.g. the proofs that the type system is sound, etc.).
I have not read these sections in depth, and will not be discussing them here.
It is reasonable for compiler authors to take these results as given
and not focus on their details.

In some places, I will be criticizing the way the paper presents its ideas.
Please do not take these as prescriptions for how it *should have* been written.
I do not have the standing to make prescriptions like that;
the paper was written with considerations other than the ones most important to me
(such as brevity of the rules, ease of meta-theory, & an intended audience of other academics).

System Fω and the architecture of the type system
-------------------------------------------------

At a basic level, 1ML is really just a sophisticated syntactic sugar for
a version of the lambda calculus called
[System Fω](./1ml-common/1ml-jfp-official.pdf#page=18).
If you’re not familiar, this is basically the core type system of Haskell,
including higher-kinded type constructors, with all polymorphism being explicit.
1ML terms (I’ll use *term* and *expression* interchangeably) are converted into Fω terms
and 1ML types are converted into Fω types.

The specific structure of this translation is best saved for a later article.
For now, I’ll say that whenever a type TTT appears in the surface syntax,
it is immediately converted to a Fω type written with the variable Ξ\XiΞ.
After this translation, the rules completely forget about TTT and don’t touch it again.
This is why we see similar constructs written with two different syntaxes,
like (= type T)\text{(= \textbf{type} $T$)}(= type T) and [=τ][= \tau][=τ].

This may seem a little unfamiliar; I was used to seeing type systems
that don’t distinguish between the surface syntax for types and the internal representation of types.
But of course, a routine like this exists in any real-world type checker,
it’s just that many papers would consider it “out of scope” and not discuss it.

Technical note: order of record fields

Whenever a type system defines a class of objects CCC,
it will often come with some invariants (“every c∈Cc \in Cc∈C has property PPP”)
and some equivalences (“any c,c′∈Cc, c' \in Cc,c′∈C are equivalent if QQQ, even if they aren’t the same as written”).
In situations like this, it is useful to pay attention to which properties and equivalences
are being enforced through the grammar of CCC,
and which are defined using the inference rules.

Unfortunately, when it comes to how Fω’s record field labels work,
the paper isn’t so clear.
[Fig. 3](./1ml-common/1ml-jfp-official.pdf#page=18),
which defines the syntax of Fω,
has only this to say:

τ::=⋯∣{l:τ‾}e::=⋯∣{l=e‾}
\tau ::= \dots \mid \{ \overline{ l : \tau } \}
\qquad
e ::= \dots \mid \{ \overline{ l = e } \}
τ::=⋯∣{l:τ}e::=⋯∣{l=e}

(See [below](#overline-notation) for an explanation of the overline notation.)

However,
[Fig. 4](./1ml-common/1ml-jfp-official.pdf#page=19),
which provides typing rules, has this rule for typing field access:

Γ⊢e:{l:τ,l′:τ′‾}Γ⊢e.l:τ
\frac{
\Gamma \vdash e : \{ l : \tau, \overline{ l' : \tau' } \}
}{
\Gamma \vdash e.l : \tau
}
Γ⊢e.l:τΓ⊢e:{l:τ,l′:τ′}​

This rule only makes sense if we understand record fields to be intrinsically unordered.
I think we can also reasonably assume that l‾\overline{ l }l
is understood to contain no duplicates.
That resolves our question;
however, for reasons I’ll get into later,
I suspect a type checker will want to keep around the original order of field labels in practice.

I want to linger on
[the type system of Fω](./1ml-common/1ml-jfp-official.pdf#page=19)
for a bit longer.
We can think of Fω type expressions τ\tauτ as terms in a simply-typed lambda calculus
whose base “type” is Ω\OmegaΩ, the kind of types.
This is the core of what gives Fω, and therefore 1ML, its power —
type checking can invoke some form of computation at the type level.
This power comes with a corresponding burden for the implementer,
who must essentially build an interpreter for
STLC
into their type checker.

The key rule is this one:

Γ⊢e:τ′τ′≡τΓ⊢τ:ΩΓ⊢e:τ
\frac{
\Gamma \vdash e : \tau'
\qquad
\tau' \equiv \tau
\qquad
\Gamma \vdash \tau : \Omega
}{
\Gamma \vdash e : \tau
}
Γ⊢e:τΓ⊢e:τ′τ′≡τΓ⊢τ:Ω​

In words: “whenever an Fω term eee is considered to have a type τ′\tau'τ′,
we could also consider it to have type τ\tauτ
if τ\tauτ is another well-formed type which is *equivalent* to τ′\tau'τ′.”

The type equivalence rules are presented as two-directional equalities (≡\equiv≡),
but in practice, a compiler will want to think of these as one-directional reductions.
You can use a technique like [normalization by evaluation](https://en.wikipedia.org/wiki/Normalisation_by_evaluation) for this.
Bringing types all the way to normal form whenever you construct them is a viable approach,
but it gets slow for very large types;
there are standard techniques available for being lazier (this is not 1ML-specific).

Semantic types and modeling them in code
----------------------------------------

[Figure 6](./1ml-common/1ml-jfp-official.pdf#page=22)
defines the grammar for semantic types. It’s important, so I’ll reproduce it here.

(abstracted)Ξ::=∃α‾.Σ(large)Σ::=π∣bool∣[=Ξ]∣{l:Σ‾}∣∀α‾.Σ→ηΞ(small)σ::=π∣bool∣[=σ]∣{l:σ‾}∣σ→Iσ(paths)π::=α∣πσ‾(purity)η::=P∣I
\begin{align\*}
\text{(abstracted)} \quad && \Xi \quad & ::= \quad \exists \overline\alpha. \Sigma
\\
\text{(large)} \quad && \Sigma \quad & ::= \quad \pi \mid \text{bool} \mid [= \Xi] \mid \{ \overline{ l : \Sigma } \} \mid \forall \overline\alpha. \Sigma \to\_\eta \Xi
\\
\text{(small)} \quad && \sigma \quad & ::= \quad \pi \mid \text{bool} \mid [= \sigma] \mid \{ \overline{ l : \sigma } \} \mid \sigma \to\_{\texttt{I}} \sigma
\\
\text{(paths)} \quad && \pi \quad & ::= \quad \alpha \mid \pi \overline\sigma
\\
\text{(purity)} \quad && \eta \quad & ::= \quad \texttt{P} \mid \texttt{I}
\end{align\*}
(abstracted)(large)(small)(paths)(purity)​​ΞΣσπη​::=∃α.Σ::=π∣bool∣[=Ξ]∣{l:Σ}∣∀α.Σ→η​Ξ::=π∣bool∣[=σ]∣{l:σ}∣σ→I​σ::=α∣πσ::=P∣I​

Note: the meaning of overline notation, as in l:Σ‾\overline{l : \Sigma}l:Σ

This is meta-theoretic syntax that just means “zero or more”
(sometimes including delimiting commas).
For those familiar with Rust’s macro system,
it is comparable to something like `{ $($l:label : $sigma:large_typ),* }`.

### Large and small semantic types

The first thing we should observe is that large and small types aren’t really defining a new grammar,
but instead a *subgrammar* of Fω types
(so we have {σ}⊆{Σ}⊆{Ξ}⊆{τ}\{ \sigma \} \subseteq \{ \Sigma \} \subseteq \{ \Xi \} \subseteq \{ \tau \}{σ}⊆{Σ}⊆{Ξ}⊆{τ}).
This is why the metavariable τ\tauτ doesn’t appear much in the rest of the paper from now on —
most of the Fω stuff going on will be restricted to semantic types.

The only wrinkle is the new type formers:
the singleton [=Ξ][= \Xi][=Ξ] and the function type with a purity annotation Σ→ηΞ\Sigma \to\_\eta \XiΣ→η​Ξ.
The paper defines these via desugaring to Fω types with single-field records,
but an implementation will find it easier to treat them as their own type constructors.

### Paths

The path grammar is a little wonky. It allows repetition of σ\sigmaσ in two different ways,
suggesting that a path is an Fω type variable applied to a *list of lists* of small types,
like π::=ασ‾‾\pi ::= \alpha \overline{\overline\sigma}π::=ασ.
My guess is that this is just a mistake;
it suggests that paths have structure beyond the Fω types of which they are supposed to be a subgrammar,
and nothing in the rest of the paper goes wrong if we just treat it as π::=ασ‾\pi ::= \alpha \overline\sigmaπ::=ασ.

I honestly find the whole idea of a path a little poorly motivated.
My best attempt to articulate the role paths play in the rest of the paper
is that they enforce that a semantic type is (roughly) in normal form
(since type-level function applications always have a variable at their head),
and that only small types can be applied as arguments to functions.
“Path” is really a misnomer from this perspective.
(The fact that a set of paths is an input to the subtyping relation
Γ⊢Σ′≤π‾Σ\Gamma \vdash \Sigma' \leq\_{\overline\pi} \SigmaΓ⊢Σ′≤π​Σ is actually a red herring,
as I’ll discuss in a later article.)

### Abstracted types

**The abstracted type grammar Ξ::=∃α‾.Σ\Xi ::= \exists \overline\alpha. \SigmaΞ::=∃α.Σ
risks giving the reader poor intuitions.**[1](#footnote-1)
You should think of “abstracted types” as corresponding to signatures (a.k.a. module types)
in traditional descriptions of ML.
They can contain one or more abstract types (the α‾\overline\alphaα),
but thinking of them as existentially quantified is too limiting,
since they can be specialized to concrete types after the fact
by constructs like `T where type t = bool`.

As an illustration of this, you can look at the desugaring rules
[on page 25](./1ml-common/1ml-jfp-official.pdf#page=25),
which say that the surface signature `{ type t; x : t }` gets desugared
to Ξ=∃α:Ω.{t:[=α],x:α}\Xi = \exists \alpha : \Omega. \{ t : [= \alpha], x : \alpha \}Ξ=∃α:Ω.{t:[=α],x:α}.
This is an Fω type which is *provably useless*![2](#footnote-2)
But this signature isn’t useless — we could readily imagine a functor in OCaml having it as an argument.

In my opinion, writing ∃\exists∃ here is an abuse of notation.
A better mental model of an abstracted type is something like (α:κ‾.Σ)(\overline{\alpha : \kappa}. \Sigma)(α:κ.Σ) —
a large type expression that has a number of free variables,
and is equipped with a description of those variables (their kinds),
but does not prescribe an interpretation for the variables,
allowing them to later become existentially quantified, universally quantified, or substituted with concrete types.
This is what the paper calls
[translucency](./1ml-common/1ml-jfp-official.pdf#page=11);
if you’re familiar with nominal sets, you can also think of it as a binder.

### A summary of my implementation recommendations

* Don’t create a separate data type for Fω types τ\tauτ;
  instead, create a data type that represents large types Σ\SigmaΣ.
* Contexts Γ\GammaΓ contain large types.
* Don’t have a separate data type for small types; it will result in too much code duplication.
  Instead, smallness should be an invariant not tracked by the type system.
* Do create a separate data type for Ξ\XiΞ, along the lines of:

  ```
  type signat = (type_variable * kind) list * large_type
  ```
* Introduce a dedicated constructor for [=Ξ][= \Xi][=Ξ] in your large type ADT.
* Either have a dedicated constructor for ∀α‾.Σ→ηΞ\forall \overline\alpha. \Sigma \to\_\eta \Xi∀α.Σ→η​Ξ,
  or separate it out based on η\etaη to model
  [the syntactic invariant](./1ml-common/1ml-jfp-official.pdf#page=24)
  for pure functions
  (∀α‾.Σ→IΞ\forall \overline\alpha. \Sigma \to\_{\texttt{I}} \Xi∀α.Σ→I​Ξ and
  ∀α‾.Σ→PΣ\forall \overline\alpha. \Sigma \to\_{\texttt{P}} \Sigma∀α.Σ→P​Σ).

Wrapping up
-----------

That’s all I have time for today.
In the next entry, I’ll cover the surface syntax of 1ML,
the desugaring judgement Γ⊢T⇝Ξ\Gamma \vdash T \leadsto \XiΓ⊢T⇝Ξ,
the role of the [=Ξ][= \Xi][=Ξ] type,
and how I think about phase separation.

Footnotes
---------

1:
The use of this notation goes at least back to F-ing modules,
so there is at least precedent for it,
and it makes the rules more concise to not have to coerce from Ξ\XiΞ to a “real” existential type,
but I still don’t like it.
[↩︎](#footnote-1-link)

2:
This type is isomorphic to A:=∃α.αA := \exists \alpha. \alphaA:=∃α.α,
a type whose values cannot be distinguished in any way —
there’s no way to write a function A→boolA \to \textbf{bool}A→bool that isn’t constant.
[↩︎](#footnote-2-link)
