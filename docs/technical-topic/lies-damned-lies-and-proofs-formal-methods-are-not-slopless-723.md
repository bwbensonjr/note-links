---
id: 723
url: https://www.lesswrong.com/posts/rhAPh3YzhPoBNpgHg/lies-damned-lies-and-proofs-formal-methods-are-not-slopless
title: 'Lies, Damned Lies, and Proofs: Formal Methods are not Slopless — LessWrong'
domain: www.lesswrong.com
source_date: '2026-01-17'
tags:
- academic-paper
- security
- ai
summary: 'The article challenges the assumption that formal methods guarantee error-free
  code, arguing that formal proofs can still be sloppy and fail to prove what they''re
  intended to. The authors highlight key problems: formal models may not be written
  in ways that theorem provers can easily verify, translations between code and formal
  systems can introduce semantic gaps, and proofs might accidentally prove trivial
  or incorrect statements rather than catching real bugs. They conclude that while
  formal verification is valuable for AI safety, it requires careful attention to
  these pitfalls rather than serving as an automatic safeguard against mistakes.'
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Lies, Damned Lies, and Proofs: Formal Methods are not Slopless — LessWrong

[Secure Program Synthesis](/s/uuY62aBQw8j3ASaCS)

[Formal Proof](/w/formal-proof)[AI](/w/ai)[Frontpage](/posts/5conQhfa4rgb4SaWx/site-guide-personal-blogposts-vs-frontpage-posts)

[2026 Top Fifty: 14%](https://manifold.markets/LessWrong/will-lies-damned-lies-and-proofs-fo)

102
===

[Lies, Damned Lies, and Proofs: Formal Methods are not Slopless](/posts/rhAPh3YzhPoBNpgHg/lies-damned-lies-and-proofs-formal-methods-are-not-slopless)
======================================================================================================================================================

by [Quinn](/users/quinn-dougherty?from=post_header), [Max von Hippel](/users/max-von-hippel?from=post_header)

12th Jan 2026

9 min read

[9](#comments)

102
===

*We appreciate comments from Christopher Henson, Zeke Medley, Ankit Kumar, and Pete Manolios. This post was initialized by* [*Max’s twitter thread*](https://x.com/maxvonhippel/status/2006042845384233245?s=20).

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/rhAPh3YzhPoBNpgHg/jr6n87xgoaxfcv0bvt23)

Introduction
============

There's been a lot of chatter recently on [HN](https://news.ycombinator.com/item?id=46294574) and elsewhere about how formal verification is the obvious use-case for AI. While we broadly agree, we think much of the discourse is kinda wrong because **it incorrectly presumes formal = slopless**.[[1]](#fn-TbaYn65qQfeyQN9uj-1)Over the years, we have written our fair share of good and bad formal code. In this post, we hope to convince you that formal code can be sloppy, and that this has serious implications for anyone [who hopes](https://www.morph.so/blog/verified-superintelligence) to bootstrap superintelligence by using formality to reinforce “good” reasoning.

A mainstay on the Lean Zulip named Gas Station Manager [has written](https://gasstationmanager.github.io/ai/2024/11/04/a-proposal.html) that hallucination-free program synthesis[[2]](#fn-TbaYn65qQfeyQN9uj-2)is achievable by vibing software directly in Lean, with the caveat that the agent also needs to prove the software correct. The AI safety case is basically: wouldn’t it be great if a cheap (i.e. *O(laptop)*) signal could protect you from [sycophantic hubris](https://arxiv.org/abs/2510.04721) and [other classes of mistake](https://www.google.com/url?q=https://arxiv.org/pdf/2503.21934&sa=D&source=docs&ust=1768197513764355&usg=AOvVaw2lUadyr5jPs4s4-ovGUHwu), without you having to manually audit all outputs?

A fable right outta aesop
-------------------------

Recently a computer scientist (who we will spare from naming) was convinced he had solved a major mathematics problem. Lean was happy with it, he reasoned, given that his proof mostly worked, with just a few red squigglies. As seasoned proof engineers, we could have told him that in proof engineering, the growth in further needed edits is superlinear in number-of-red-squigglies (unlike in regular programming). The difference between mistakes in a proof and mistakes in a program is that you cannot fix a broken proof in a way that changes its formal goal (the theorem statement). In contrast, many, if not most changes to traditional software impact its formal spec, for example by adding a side-effect or changing the shape of an output. Therefore proof bugs are 1) harder to fix, and 2) more likely to imply that your goal is fundamentally unachievable (the theorem is wrong). This made up chart illustrates the principle, a rough “lore” level consensus in the field without any hard data.

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/rhAPh3YzhPoBNpgHg/tt9djvmucnyhzewrvjid)

It is possible he will post a finished proof, but the referee-time of bets he made has lapsed, so we can take away some lessons. Did our protagonist take to heart the promise of formal methods as slopless?

Your formal model might not be proof-idiomatic.
===============================================

In much the same way that vibed code might *work* yet be “sloppy” in the sense that it’s difficult to maintain, vibed formal models can be correct, yet very challenging to prove anything about.

Often when you model a system – or write code in a theorem-prover, with the intention of proving things about it – you actually need to make implementation decisions informed by the limitations and capabilities of the prover. For example, it's pretty common that inducting in one direction (say, car/head) on a list will be easy for a prover but the other direction (say cdr/tail) will be difficult. (This is a necessary evil if you want the prover to not enter infinite rewrite loops.) Thus, as an example, you might implement *isort* in a particular “direction” in order to make the proofs easier about it. If you want to autoformalize arbitrary code in a way that makes proofs straightforward, you’ll need models that understand how to implement something in a way that’s idiomatic for the given interactive theorem-prover.

This is a solvable problem but a real one nonetheless. For example, one [Aristotle](https://aristotle.harmonic.fun/) user we spoke to reported: “... in Lean you can put theorems inside mutual blocks to let them use each other. I wrote such a theorem, but then later realized proving it this way would be unnecessarily difficult. [...] The model won't do this, so it spent >24 hours on this almost hopeless proof.” Autoformalization companies like [math.inc](https://www.math.inc/), [Harmonic](https://harmonic.fun/), [Axiom](https://axiommath.ai/), [Logical Intelligence](https://t.co/tEU2AddGt9), etc. are actively working on improving their models to have this kind of expert folklore knowledge as we speak, but we’re not quite there yet.

Mind the (semantic) gap
=======================

There are basically two ways to make your software amenable to an interactive theorem prover (ITP). The first is to [lift it into an ITP](https://dl.acm.org/doi/10.1145/3519939.3523702) using a formal semantics – somewhat like a compiler or interpreter for the original language but implemented in the ITP itself. In this case, you can define the lifting so that it produces functionally equivalent code (say, Lean code that “does the same thing” as the input Python) but in a shape that the theorem-prover tends to like (incorporating heuristics like the car/cdr one mentioned above). The second approach is to just rewrite the original software directly in the language of the ITP, making those kinds of idiomacy improvements as-you-go. Both approaches, however, produce the same formal problem: ensuring that the software you wanted to study in the first place is semantically equivalent to the thing you introduced in the theorem-prover. IE., either ensuring the lifting is correct, or ensuring the manual translation is equivalent. Let’s dig into some of the ways this can be difficult.

A formal proof might not prove the thing you think it proves.
-------------------------------------------------------------

When we talk about using formal methods to assure that LLM-generated code is safe, what we want is a short, readable description of what the generated code is intended to do, some proof (which might be far too boring and long to read) that the code does this, and the ability to run the proof through a prover and validate that it indeed proves the aforementioned statement. But this is not necessarily a reasonable ask, *regardless of model intelligence*.

First, it’s very common that you mis-define some concept such that the proof is accidentally trivial. For example, when defining a lifting from Python to Lean you might prove that the lifting preserves the semantics of the original Python code, but your proof could be undermined by the presumption that the code terminates, making it basically useless.

Second, if you re-implement the original software in your ITP of choice, your re-implementation [might not be fully faithful](https://arxiv.org/pdf/2107.00723), particularly if it’s LLM-generated. For example, the LLM might say, "The code you wanted me to verify was too complex, so I rewrote it to be simpler and proved the simpler thing correct." Well, yeah, but the bugs I wanted you to find were in the complexity. As a concrete example, we asked an early version of Gemini to write a [property based test (PBT)](https://hypothesis.readthedocs.io/en/latest/) for a (deliberately flawed) *isort* implementation which we provided; Gemini did so but rewrote the *isort* code to be correct in the process and then executed the PBT and cheerfully reported that it passed.

These first two problems are commonly addressed using tests which compare the original software to its representation in the ITP. For example, we (Max) did this with coauthors for GossipSub, connecting the Golang implementation to [its ACL2(s) model](https://github.com/gossipsubfm/) via both unit tests and property-based tests.[[3]](#fn-TbaYn65qQfeyQN9uj-3)To quote Knuth: “Beware of bugs in the above code; I have only proved it correct, not tried it.”

Third, you need to decide how far “down the stack” you want to go. That is to say, the software you want to verify operates over some kind of more complex system, for instance, maybe it’s C code which gets compiled down to X86 and runs on a particular chip, or maybe it’s a controller for a nuclear reactor and part of the system is the actual physical dynamics of the reactor. Do you really want your proof to involve specifying the semantics of the C compiler and the chip, or the way that the temperature and other variables fluctuate in the reactor? Keeping in mind these semantics might not truly be known – e.g., RowHammer can be viewed as an attack on our understanding of the semantics of the chip. In essence, you can only get more specificity by vastly increasing the length of your proof statement to capture the semantics of the underlying system, which then produces a new (and perhaps equally difficult) code review problem. Typically this problem is handled by leaving the underlying semantics nondeterministic, so your proof is *stronger* (it holds regardless of how the C compiler handles floating point, or how the temperature fluctuates in the nuclear silo) but often the thing you want to prove really does require some pretty specific guarantees about those underlying semantics, and ensuring those guarantees are “reasonable” can be extraordinarily difficult.

Interactive theorem proving is not adversarially robust
=======================================================

Axioms
------

The AI might introduce axioms that conflict with your own presuppositions or the specific requirements of your domain. In Lean, for example, the **Axiom of Choice** (`Classical.choice`) is available but transforms a proof from a constructive one—where you can actually compute a result—into a non-constructive one. An AI tasked with verifying a program might realize that a proof is significantly easier if it assumes AC. It might inform you that the theorem is "proven," and the prover will confirm this, but you may not realize that the resulting proof is now a "lie" for your specific use case. If you needed that proof to generate an executable, verified algorithm, the introduction of non-constructive axioms shifts you into an incompatible register.

The person designing the harness for the AI needs to be an expert who knows how to parse these imports and error messages. Without that oversight, the AI will naturally gravitate toward the path of least resistance—even if that path involves an axiomatic shift that renders the entire exercise useless for the user's true intent.

Backdoors
---------

Consider the proof assistant ACL2, which accepts arbitrary lisp code.[[4]](#fn-TbaYn65qQfeyQN9uj-4)You write `defttag`, the *trusted* tag to open the “trust me” scope. In other words, `defttag` offloads the soundness obligations to the user. Observe a proof that 1+1=3 in ACL2 with `defttag`.

```
;; 1. Open the "backdoor"
(defttag :evil-math)the two of them.

;; 2. Inject raw Lisp to redefine addition
(progn!
  (set-cmds-allowed t) ; Allow internal state changes
  (raw-lisp
    (defun acl2::binary-+ (x y)
      (if (and (eql x 1) (eql y 1))
          3   ; The "Evil" part: 1 + 1 is now 3
          (+ x y)))))

;; 3. Prove something that is now "true" but logically insane
(thm (equal (+ 1 1) 3))
```

“Well yeah”, perhaps comes a reply. “It only looks like 1+1=3 in the nonsensical sense if you deliberately ignore that the meaning of plus has shifted”. “Besides”, they continue. “When my coworker sends me code with `defttag` in it, I read it very rigorously”. Our retort is that we don’t assume our coworkers are competent or trustworthy, we assume that they’re AIs with a tendency to [reward hack](https://youtu.be/nKJlF-olKmg?si=1Bob5vrTnzROE0oB). To recap:

1. Defining the allowable surface is nontrivial. The person who designs the harness for the malicious AI to prove things needs to personally be an expert in the given ITP and know all its caveats and danger-cases.
2. In the glorious proof synthesis future, it’ll all be way too much to read. Theorems are not necessarily short, even devoid of the proofs.

Additionally, proof tools like Lean pile a bunch of ergonomic and notational niceties on top of their core calculus, in Lean’s case with powerful metaprogramming. But this metaprogramming can lead to [backdoors](https://x.com/elliotglazer/status/2007938754565271890?s=46) much like the ACL2 example.[[6]](#fn-TbaYn65qQfeyQN9uj-6)

Proofs of false
---------------

From nothing arises everything. From a proof of false you can derive literally any proposition.

In Agda, a calculus of inductive constructions popular with mathematical type theorists, the [github issue label “false” tracking proofs of false is standing at 9 open and 74 closed issues at time of this writing](https://github.com/agda/agda/issues?q=label%3Afalse). A proof of false is a *soundness bug*[[7]](#fn-TbaYn65qQfeyQN9uj-7), which if you think proof synthesis plays a role in high stakes AI security (like SL5), means you have to be paranoid about a glaring *attack surface*.

While we can’t yet think of a case of sicophancy/hubris that was accelerated by an arcane proof of false, we expect this becomes increasingly likely as insecure program synthesis tools get more capable and accessible in contexts where they are incentivized to reward-hack a proof.

Conclusion
==========

If someone says "stats don’t lie" you say "well don’t be naive, you can tell misleading stories with technically true statistics".[[8]](#fn-TbaYn65qQfeyQN9uj-8)Formal verification is the same. Don’t be lured into the false sense of security. To paraphrase Twain, “There are three kinds of lies: lies, damned lies, and proofs.” We already know models lie to us; we should fully expect them to prove falsehoods, too.

What are the bottlenecks?
-------------------------

In spite of our warnings, which may seem pessimistic, we’re working on secure program synthesis (or what [Mike Dodds](https://mikedodds.org/) calls scalable formal oversight) for AI security. The reason we can work on this anyway is because we see a lit path, principally routing through *specification elicitation*[[9]](#fn-TbaYn65qQfeyQN9uj-9)*and validation* as well as hardened proof cores and (the cherry on top) superpowered proof synthesis. Spec elicitation and validation, in particular, have not seen the upside from language model assisted transpilation fully harvested just yet.

1. This intuition might be in part driven by academic papers that push formality as a cure to sloppiness, e.g., [Run Your Research](https://dl.acm.org/doi/10.1145/2103656.2103691) and [HACMS](https://pmc.ncbi.nlm.nih.gov/articles/PMC5597724/). But [even formally verified software can be buggy](https://dl.acm.org/doi/pdf/10.1145/3064176.3064183)! [↩︎](#fnref-TbaYn65qQfeyQN9uj-1)
2. As a historical aside, the original citation for program synthesis is: Church, A.: [Application of recursive arithmetic to the problem of circuit synthesis](https://iiif.library.cmu.edu/file/Simon_box00077_fld06240_bdl0001_doc0001/Simon_box00077_fld06240_bdl0001_doc0001.pdf) (7 1957), presented at [IDA](https://en.wikipedia.org/wiki/Institute_for_Defense_Analyses), as cited in doi:10.2307/2271310. [↩︎](#fnref-TbaYn65qQfeyQN9uj-2)
3. [Cedar](https://github.com/cedar-policy/cedar-spec) comes to mind as a similar case-study in Lean. [↩︎](#fnref-TbaYn65qQfeyQN9uj-3)
4. This feature is useful for proving things about [real-world LISP code](https://link.springer.com/chapter/10.1007/978-3-540-73086-6_1), or connecting ACL2 code which is proven to be correct to real-world systems via LISP harnesses. [↩︎](#fnref-TbaYn65qQfeyQN9uj-4)
5. Lean has [something similar](https://lean-lang.org/doc/reference/latest/Axioms/#standard-axioms). [↩︎](#fnref-TbaYn65qQfeyQN9uj-5)
6. See also [Pollack-consistency](https://www.cs.ru.nl/~freek/pubs/rap.pdf), a kind of [LangSec](https://langsec.org/) concept of theorem-prover backdooring. [↩︎](#fnref-TbaYn65qQfeyQN9uj-6)
7. There are some subtleties here we elide, which Christopher Henson plans to explore in a more technical forthcoming blog post. [↩︎](#fnref-TbaYn65qQfeyQN9uj-7)
8. See also [The Difference Between “Significant” and “Not Significant” is not Itself Statistically Significant](https://sites.stat.columbia.edu/gelman/research/published/signif4.pdf). [↩︎](#fnref-TbaYn65qQfeyQN9uj-8)
9. Academia is certain that [specification is hard](https://cacm.acm.org/research/it-takes-a-village-bridging-the-gaps-between-current-and-formal-specifications-for-protocols/) (see also [Formal Methods for Security](https://arxiv.org/pdf/1608.00678)) and [we should fix it](https://datatracker.ietf.org/rg/ufmrg/about/), but unsure as to why or how to improve the situation. [↩︎](#fnref-TbaYn65qQfeyQN9uj-9)

[Lies, Damned Lies, and Proofs: Formal Methods are not Slopless](#)

[13β-redex](#LskTB4K65KmgfCStH)

[5Max von Hippel](#89n8mz2uy4jsotn4t)

[8Oliver Sourbut](#tmS6p9cXoB9jRasYo)

[3β-redex](#G57Bd6euMFdJBDyYo)

[2Aprillion](#4fsjwTaHDJJmLeyCG)

[1Max von Hippel](#pacP5r2LnhLbWMx9X)

[2Max von Hippel](#wLcFDdbEP5GFNaGuk)

[1Michal Šustr](#CtrmznnP5PoezYp3K)

[1Max von Hippel](#nr6xvZzBfMg4pRsCw)
