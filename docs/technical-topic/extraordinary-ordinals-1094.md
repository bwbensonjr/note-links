---
id: 1094
url: https://text.marvinborner.de/2026-04-09-17.html
title: Extraordinary Ordinals
domain: text.marvinborner.de
source_date: '2026-05-14'
tags:
- academic-paper
- haskell
summary: 'This page presents multiple encodings of natural numbers using lambda calculus,
  organized into three categories based on variable usage patterns: Linear (where
  variables are used exactly once), Affine (where variables may be unused), and Non-Linear
  (where variables can be used multiple times). Each category features different classical
  encodings—including Church, Parigot, Scott, and Mogensen numerals—that can all be
  used for arithmetic operations, with the encodings represented as lambda terms with
  specific syntactic structures. The page systematically demonstrates how each encoding
  scheme encodes small numbers (0-3) and their successor function, illustrating the
  mathematical elegance of different approaches to representing ordinals in functional
  programming.'
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Extraordinary Ordinals

*Syntax*.

Expressionse,b,f,a∷=xVariable∣x⇒bAbstraction∣f←aApplicationVariablesx∈k,x,y,…Numbersn∈0,1,2,… \small\begin{array}{lrcll} \mathrm{Expressions}\quad & e,b,f,a & {\Coloneqq} & x & \quad\mathrm{Variable} \\ & & {\mid} & x\Rightarrow b & \quad\mathrm{Abstraction} \\ & & {\mid} & f\leftarrow a & \quad\mathrm{Application} \\ \mathrm{Variables} & x & {\in} & \mathsf{k}, \mathsf{x}, \mathsf{y}, \dots \\ \mathrm{Numbers} & n & {\in} & 0, 1, 2, \dots \end{array} ExpressionsVariablesNumbers​e,b,f,axn​::=∣∣∈∈​xx⇒bf←ak,x,y,…0,1,2,…​VariableAbstractionApplication​

There are 3 categories—*Linear*, *Affine*, and
*Non-Linear*—each having several encodings. Notably, every
presented encoding can be used for arithmetic.

(all diagrams are drawn by hand in latex+tikz without ai; pow: [source](res/strdig/2026-04-09-17.tex), [draft notes](res/notes/numeral_graph_encodings.pdf))

Linear
======

The encoding of lambda terms as graphs consists of named edges
connected to each other.

*Variables*. Encoding a variable
Tk(x)\mathcal{T}\_k(x)Tk​(x)
in the context
kkk
connects the variable to
kkk.

*Application*.
Tk(f←a)\mathcal{T}\_k(f\leftarrow a)Tk​(f←a):

![](res/strdig/2026-04-09-17/app.svg "application encoding")

*Abstraction*.
Tk(x⇒b)\mathcal{T}\_k(x\Rightarrow b)Tk​(x⇒b):

![](res/strdig/2026-04-09-17/abs.svg "abstraction encoding (application upside-down because it's dual!)")

*β\betaβ-reduction*.
In a context
kkk:
k[(x⇒b)←a] ⊳ k[b{a/x}]k[(x\Rightarrow b)\leftarrow a]\ \rhd\ k[b\{a/x\}]k[(x⇒b)←a] ⊳ k[b{a/x}]

![](res/strdig/2026-04-09-17/beta.svg "encoding of beta reduction, just for fun. consists of only a single rewiring!")

*i.e.*
xxx
gets bound to
aaa,
whereas the substituted body
bbb
gets returned to the application’s context.

Mackie
------

[Mackie (2019)](#ref-mackie2019linear)

Definition

⟨0⟩≏x⇒x⟨1⟩≏x⇒x←(x⇒x)⟨2⟩≏x⇒x←(x⇒x)←(x⇒x)⟨3⟩≏x⇒x←(x⇒x)←(x⇒x)←(x⇒x)  ⋮⟨S(n)⟩≏x⇒⟨n⟩←x←(x⇒x) \begin{align\*} \braket{0} &\bumpeq \mathsf{x}\Rightarrow \mathsf{x} \\ \braket{1} &\bumpeq \mathsf{x}\Rightarrow \mathsf{x}\leftarrow (\mathsf{x}\Rightarrow \mathsf{x}) \\ \braket{2} &\bumpeq \mathsf{x}\Rightarrow \mathsf{x}\leftarrow (\mathsf{x}\Rightarrow \mathsf{x})\leftarrow (\mathsf{x}\Rightarrow \mathsf{x}) \\ \braket{3} &\bumpeq \mathsf{x}\Rightarrow \mathsf{x}\leftarrow (\mathsf{x}\Rightarrow \mathsf{x})\leftarrow (\mathsf{x}\Rightarrow \mathsf{x})\leftarrow (\mathsf{x}\Rightarrow \mathsf{x}) \\ &\ \,\vdots\\ \braket{S(n)} &\bumpeq \mathsf{x}\Rightarrow \braket{n}\leftarrow \mathsf{x}\leftarrow (\mathsf{x}\Rightarrow \mathsf{x}) \end{align\*} ⟨0⟩⟨1⟩⟨2⟩⟨3⟩⟨S(n)⟩​≏x⇒x≏x⇒x←(x⇒x)≏x⇒x←(x⇒x)←(x⇒x)≏x⇒x←(x⇒x)←(x⇒x)←(x⇒x) ⋮≏x⇒⟨n⟩←x←(x⇒x)​

⟨0⟩\braket{0}⟨0⟩
and
⟨3⟩\braket{3}⟨3⟩:

![](res/strdig/2026-04-09-17/mackie-identity.svg "diagram of a 0 and 3. kinda looks like a water drop and a heart (as in Anatomy)?")

Parigot
-------

[Parigot (1989)](#ref-parigot1989representation) and [Mackie (2019)](#ref-mackie2019linear)

Definition

⟨0⟩≏z⇒z⟨1⟩≏z⇒s⇒s←z⟨2⟩≏z⇒s⇒s←(s⇒s←z)⟨3⟩≏z⇒s⇒s←(s⇒s←(s⇒s←z))  ⋮⟨S(n)⟩≏z⇒s⇒s←(⟨n⟩←z) \begin{align\*} \braket{0} &\bumpeq \mathsf{z}\Rightarrow \mathsf{z} \\ \braket{1} &\bumpeq \mathsf{z}\Rightarrow \mathsf{s}\Rightarrow \mathsf{s}\leftarrow \mathsf{z}\\ \braket{2} &\bumpeq \mathsf{z}\Rightarrow \mathsf{s}\Rightarrow \mathsf{s}\leftarrow(\mathsf{s}\Rightarrow \mathsf{s}\leftarrow \mathsf{z})\\ \braket{3} &\bumpeq \mathsf{z}\Rightarrow \mathsf{s}\Rightarrow \mathsf{s}\leftarrow(\mathsf{s}\Rightarrow \mathsf{s}\leftarrow(\mathsf{s}\Rightarrow \mathsf{s}\leftarrow \mathsf{z}))\\ &\ \,\vdots\\ \braket{S(n)} &\bumpeq \mathsf{z}\Rightarrow \mathsf{s}\Rightarrow \mathsf{s}\leftarrow(\braket{n}\leftarrow \mathsf{z}) \end{align\*} ⟨0⟩⟨1⟩⟨2⟩⟨3⟩⟨S(n)⟩​≏z⇒z≏z⇒s⇒s←z≏z⇒s⇒s←(s⇒s←z)≏z⇒s⇒s←(s⇒s←(s⇒s←z)) ⋮≏z⇒s⇒s←(⟨n⟩←z)​

![](res/strdig/2026-04-09-17/mackie-nested.svg "diagram of a 0 and 3. kinda looks like a water drop and a malformed puzzle piece?")

Affine
======

If a variable is not bound, let’s just leave it hanging!

Scott
-----

[Scott (1963)](#ref-scott1963func)

Definition

⟨0⟩≏s⇒z⇒z⟨1⟩≏s⇒z⇒s←(s⇒z⇒z)⟨2⟩≏s⇒z⇒s←(s⇒z⇒s←(s⇒z⇒z))⟨3⟩≏s⇒z⇒s←(s⇒z⇒s←(s⇒z⇒s←(s⇒z⇒z)))  ⋮⟨S(n)⟩≏s⇒z⇒s←⟨n⟩ \begin{align\*} \braket{0} &\bumpeq \mathsf{s}\Rightarrow\mathsf{z}\Rightarrow\mathsf{z} \\ \braket{1} &\bumpeq \mathsf{s}\Rightarrow\mathsf{z}\Rightarrow\mathsf{s}\leftarrow(\mathsf{s}\Rightarrow\mathsf{z}\Rightarrow\mathsf{z}) \\ \braket{2} &\bumpeq \mathsf{s}\Rightarrow\mathsf{z}\Rightarrow\mathsf{s}\leftarrow(\mathsf{s}\Rightarrow\mathsf{z}\Rightarrow\mathsf{s}\leftarrow(\mathsf{s}\Rightarrow\mathsf{z}\Rightarrow\mathsf{z})) \\ \braket{3} &\bumpeq \mathsf{s}\Rightarrow\mathsf{z}\Rightarrow\mathsf{s}\leftarrow(\mathsf{s}\Rightarrow\mathsf{z}\Rightarrow\mathsf{s}\leftarrow(\mathsf{s}\Rightarrow\mathsf{z}\Rightarrow\mathsf{s}\leftarrow(\mathsf{s}\Rightarrow\mathsf{z}\Rightarrow\mathsf{z}))) \\ &\ \,\vdots\\ \braket{S(n)} &\bumpeq \mathsf{s}\Rightarrow\mathsf{z}\Rightarrow\mathsf{s}\leftarrow\braket{n} \end{align\*} ⟨0⟩⟨1⟩⟨2⟩⟨3⟩⟨S(n)⟩​≏s⇒z⇒z≏s⇒z⇒s←(s⇒z⇒z)≏s⇒z⇒s←(s⇒z⇒s←(s⇒z⇒z))≏s⇒z⇒s←(s⇒z⇒s←(s⇒z⇒s←(s⇒z⇒z))) ⋮≏s⇒z⇒s←⟨n⟩​

![](res/strdig/2026-04-09-17/scott.svg "diagram of a 0 and 3. kinda looks like a water drop on a branch and several leaves attached to each other?")

Bruijn
------

[Borner
(2026)](https://text.marvinborner.de/2023-08-22-22.html)

Definition

⟨0⟩≏x⇒x⟨1⟩≏x⇒\_⇒x⟨2⟩≏x⇒\_⇒\_⇒x⟨3⟩≏x⇒\_⇒\_⇒\_⇒x  ⋮⟨S(n)⟩≏x⇒\_⇒⟨n⟩←x \begin{align\*} \braket{0} &\bumpeq \mathsf{x}\Rightarrow \mathsf{x} \\ \braket{1} &\bumpeq \mathsf{x}\Rightarrow \\_\Rightarrow \mathsf{x}\\ \braket{2} &\bumpeq \mathsf{x}\Rightarrow \\_\Rightarrow \\_\Rightarrow \mathsf{x}\\ \braket{3} &\bumpeq \mathsf{x}\Rightarrow \\_\Rightarrow \\_\Rightarrow \\_\Rightarrow \mathsf{x}\\ &\ \,\vdots\\ \braket{S(n)} &\bumpeq \mathsf{x}\Rightarrow \\_\Rightarrow \braket{n}\leftarrow \mathsf{x} \end{align\*} ⟨0⟩⟨1⟩⟨2⟩⟨3⟩⟨S(n)⟩​≏x⇒x≏x⇒\_⇒x≏x⇒\_⇒\_⇒x≏x⇒\_⇒\_⇒\_⇒x ⋮≏x⇒\_⇒⟨n⟩←x​

![](res/strdig/2026-04-09-17/bruijn.svg "diagram of a 0 and 3. kinda looks like a water drop and a single leaf?")

Non-Linear
==========

If a variable is bound multiple times, let’s duplicate it
explicitly!

*Duplication*.
Tx(xi)\mathcal{T}\_x(x\_i)Tx​(xi​),
with any
xxx
being linearly substituted for
xix\_ixi​:

![](res/strdig/2026-04-09-17/dup.svg "duplication encoding. kinda looks like a Greek psi!")

(read [Asperti and Guerrini
(1998)](#ref-asperti1998optimal) for more details)

Church
------

[Church (1932)](#ref-church1932set)

Definition

⟨0⟩≏s⇒z⇒z⟨1⟩≏s⇒z⇒s←z⟨2⟩≏s⇒z⇒s←(s←z)⟨3⟩≏s⇒z⇒s←(s←(s←z))  ⋮⟨S(n)⟩≏s⇒z⇒s←(⟨n⟩←s←z) \begin{align\*} \braket{0} &\bumpeq \mathsf{s}\Rightarrow \mathsf{z}\Rightarrow \mathsf{z} \\ \braket{1} &\bumpeq \mathsf{s}\Rightarrow \mathsf{z}\Rightarrow \mathsf{s}\leftarrow \mathsf{z} \\ \braket{2} &\bumpeq \mathsf{s}\Rightarrow \mathsf{z}\Rightarrow \mathsf{s}\leftarrow (\mathsf{s}\leftarrow \mathsf{z}) \\ \braket{3} &\bumpeq \mathsf{s}\Rightarrow \mathsf{z}\Rightarrow \mathsf{s}\leftarrow (\mathsf{s}\leftarrow (\mathsf{s}\leftarrow \mathsf{z})) \\ &\ \,\vdots\\ \braket{S(n)} &\bumpeq \mathsf{s}\Rightarrow \mathsf{z}\Rightarrow \mathsf{s}\leftarrow (\braket{n}\leftarrow \mathsf{s}\leftarrow \mathsf{z}) \end{align\*} ⟨0⟩⟨1⟩⟨2⟩⟨3⟩⟨S(n)⟩​≏s⇒z⇒z≏s⇒z⇒s←z≏s⇒z⇒s←(s←z)≏s⇒z⇒s←(s←(s←z)) ⋮≏s⇒z⇒s←(⟨n⟩←s←z)​

![](res/strdig/2026-04-09-17/church.svg "diagram of a 0 and 3. kinda looks like a water drop on a branch and a very weird heart (as in love)?")

Mogensen
--------

[Mogensen (2001)](#ref-mogensen2001investigation)

Definition

Mogensen’s system works for arbitrary bases
bbb.
For example, with
b=2b=2b=2,
the system is *binary*. An
nnn-digit
number gets decomposed into
dn−1 … d1 d0d\_{n-1}\,\dots\,d\_1\,d\_0dn−1​…d1​d0​
(with
dn−1>0d\_{n-1}>0dn−1​>0):

⟨n⟩b≏z⇒xb−1⇒xb−2⋯⇒x0⇒xd0←(xd1←(…(xdn−1←z)… ))⟨0⟩2≏z⇒i⇒o⇒z⟨1⟩2≏z⇒i⇒o⇒i←z⟨2⟩2≏z⇒i⇒o⇒o←(i←z)⟨3⟩2≏z⇒i⇒o⇒i←(i←z)  ⋮ \begin{align\*} \braket{n}\_b &\bumpeq \mathsf{z}\Rightarrow\mathsf{x}\_{b-1}\Rightarrow\mathsf{x}\_{b-2}\dots\Rightarrow\mathsf{x}\_0\Rightarrow\mathsf{x}\_{d\_0}\leftarrow(\mathsf{x}\_{d\_1}\leftarrow(\dots(\mathsf{x}\_{d\_{n-1}}\leftarrow\mathsf{z})\dots)) \\ \\ \braket{0}\_2 &\bumpeq \mathsf{z}\Rightarrow\mathsf{i}\Rightarrow\mathsf{o}\Rightarrow\mathsf{z} \\ \braket{1}\_2 &\bumpeq \mathsf{z}\Rightarrow\mathsf{i}\Rightarrow\mathsf{o}\Rightarrow\mathsf{i}\leftarrow\mathsf{z} \\ \braket{2}\_2 &\bumpeq \mathsf{z}\Rightarrow\mathsf{i}\Rightarrow\mathsf{o}\Rightarrow\mathsf{o}\leftarrow(\mathsf{i}\leftarrow\mathsf{z}) \\ \braket{3}\_2 &\bumpeq \mathsf{z}\Rightarrow\mathsf{i}\Rightarrow\mathsf{o}\Rightarrow\mathsf{i}\leftarrow(\mathsf{i}\leftarrow\mathsf{z}) \\ &\ \,\vdots\\ \end{align\*} ⟨n⟩b​⟨0⟩2​⟨1⟩2​⟨2⟩2​⟨3⟩2​​≏z⇒xb−1​⇒xb−2​⋯⇒x0​⇒xd0​​←(xd1​​←(…(xdn−1​​←z)…))≏z⇒i⇒o⇒z≏z⇒i⇒o⇒i←z≏z⇒i⇒o⇒o←(i←z)≏z⇒i⇒o⇒i←(i←z) ⋮​

in binary:

![](res/strdig/2026-04-09-17/mogensen-binary.svg "diagram of a 0 and 3. kinda looks like a small leaf and a finger idk")

*challenge*: what does the following encode?

![](res/strdig/2026-04-09-17/mogensen-binary-42.svg "diagram of a mysterious number. kinda looks like a weird fist?")

Wadsworth
---------

[Wadsworth (1980)](#ref-wadsworth1980some)

Definition

⟨0⟩≏z⇒z←(K←K)⟨1⟩≏z⇒s1⇒z←(s1←(K←K))←s1⟨2⟩≏z⇒s1⇒s2⇒z←(s1←(s2←(K←K)))←s1←s2⟨3⟩≏z⇒s1⇒s2⇒s3⇒z←(s1←(s2←(s3←(K←K)))←s1←s2←s3  ⋮⟨S(n)⟩≏z⇒s⇒⟨n⟩←p⇒z←(s←p)←s \begin{align\*} \braket{0} &\bumpeq \mathsf{z}\Rightarrow\mathsf{z}\leftarrow(\mathsf{K}\leftarrow\mathsf{K}) \\ \braket{1} &\bumpeq \mathsf{z}\Rightarrow\mathsf{s}\_1\Rightarrow\mathsf{z}\leftarrow(\mathsf{s}\_1\leftarrow(\mathsf{K}\leftarrow\mathsf{K}))\leftarrow\mathsf{s}\_1 \\ \braket{2} &\bumpeq \mathsf{z}\Rightarrow\mathsf{s}\_1\Rightarrow\mathsf{s}\_2\Rightarrow\mathsf{z}\leftarrow(\mathsf{s}\_1\leftarrow(\mathsf{s}\_2\leftarrow(\mathsf{K}\leftarrow\mathsf{K})))\leftarrow\mathsf{s}\_1\leftarrow\mathsf{s}\_2 \\ \braket{3} &\bumpeq \mathsf{z}\Rightarrow\mathsf{s}\_1\Rightarrow\mathsf{s}\_2\Rightarrow\mathsf{s}\_3\Rightarrow\mathsf{z}\leftarrow(\mathsf{s}\_1\leftarrow(\mathsf{s}\_2\leftarrow(\mathsf{s}\_3\leftarrow(\mathsf{K}\leftarrow\mathsf{K})))\leftarrow\mathsf{s}\_1\leftarrow\mathsf{s}\_2\leftarrow\mathsf{s}\_3 \\ &\ \,\vdots\\ \braket{S(n)} &\bumpeq \mathsf{z}\Rightarrow\mathsf{s}\Rightarrow\braket{n}\leftarrow\mathsf{p}\Rightarrow\mathsf{z}\leftarrow(\mathsf{s}\leftarrow\mathsf{p})\leftarrow\mathsf{s} \end{align\*} ⟨0⟩⟨1⟩⟨2⟩⟨3⟩⟨S(n)⟩​≏z⇒z←(K←K)≏z⇒s1​⇒z←(s1​←(K←K))←s1​≏z⇒s1​⇒s2​⇒z←(s1​←(s2​←(K←K)))←s1​←s2​≏z⇒s1​⇒s2​⇒s3​⇒z←(s1​←(s2​←(s3​←(K←K)))←s1​←s2​←s3​ ⋮≏z⇒s⇒⟨n⟩←p⇒z←(s←p)←s​

![](res/strdig/2026-04-09-17/wadsworth1.svg "diagram of a 0 and 3. kinda looks like a snail or a seashell?")

∗ ∗ ∗\*\ \*\ \*∗ ∗ ∗

Definition

⟨0⟩≏z⇒s0⇒z←s0⟨1⟩≏z⇒s0⇒s1⇒s0←(z←s1)⟨2⟩≏z⇒s0⇒s1⇒s2⇒s0←s1←(z←s2)⟨3⟩≏z⇒s0⇒s1⇒s2⇒s3⇒s0←s1←s2←(z←s3)  ⋮⟨S(n)⟩≏z⇒s0⇒s1⇒⟨n⟩←z←(s0←s1)[1] \begin{align\*} \braket{0} &\bumpeq \mathsf{z}\Rightarrow\mathsf{s}\_0\Rightarrow\mathsf{z}\leftarrow\mathsf{s}\_0 \\ \braket{1} &\bumpeq \mathsf{z}\Rightarrow\mathsf{s}\_0\Rightarrow\mathsf{s}\_1\Rightarrow\mathsf{s}\_0\leftarrow(\mathsf{z}\leftarrow\mathsf{s}\_1) \\ \braket{2} &\bumpeq \mathsf{z}\Rightarrow\mathsf{s}\_0\Rightarrow\mathsf{s}\_1\Rightarrow\mathsf{s}\_2\Rightarrow\mathsf{s}\_0\leftarrow\mathsf{s}\_1\leftarrow(\mathsf{z}\leftarrow\mathsf{s}\_2) \\ \braket{3} &\bumpeq \mathsf{z}\Rightarrow\mathsf{s}\_0\Rightarrow\mathsf{s}\_1\Rightarrow\mathsf{s}\_2\Rightarrow\mathsf{s}\_3\Rightarrow\mathsf{s}\_0\leftarrow\mathsf{s}\_1\leftarrow\mathsf{s}\_2\leftarrow(\mathsf{z}\leftarrow\mathsf{s}\_3) \\ &\ \,\vdots\\ \braket{S(n)} &\bumpeq \mathsf{z}\Rightarrow\mathsf{s}\_0\Rightarrow\mathsf{s}\_1\Rightarrow\braket{n}\leftarrow\mathsf{z}\leftarrow(\mathsf{s}\_0\leftarrow\mathsf{s}\_1)^{[1]} \end{align\*} ⟨0⟩⟨1⟩⟨2⟩⟨3⟩⟨S(n)⟩​≏z⇒s0​⇒z←s0​≏z⇒s0​⇒s1​⇒s0​←(z←s1​)≏z⇒s0​⇒s1​⇒s2​⇒s0​←s1​←(z←s2​)≏z⇒s0​⇒s1​⇒s2​⇒s3​⇒s0​←s1​←s2​←(z←s3​) ⋮≏z⇒s0​⇒s1​⇒⟨n⟩←z←(s0​←s1​)[1]​

[1]: see note in original paper for successor of
⟨0⟩\braket{0}⟨0⟩.

![](res/strdig/2026-04-09-17/wadsworth2.svg "diagram of a 0 and 3. kinda looks like a snail or a seashell? Wadsworth really liked such terms!")

❦❦❦

Contact me via [email](mail). Support on [Ko-fi](https://ko-fi.com/marvinborner). Subscribe on [RSS](/feed.rss). Follow on [Mastodon](https://types.pl/@marvin).

References
==========

Asperti, Andrea, and Stefano Guerrini. 1998. *The Optimal
Implementation of Functional Programming Languages*. Vol. 45.
Cambridge University Press.

Church, Alonzo. 1932. “A Set of Postulates for the Foundation of
Logic.” *Annals of Mathematics* 33 (2): 346–66.

Mackie, Ian. 2019. “Linear Numeral Systems.” *Journal of
Automated Reasoning* 63 (4): 887–909.

Mogensen, Torben Æ. 2001. “An Investigation of Compact and
Efficient Number Representations in the Pure Lambda Calculus.” In
*International Andrei Ershov Memorial Conference on Perspectives of
System Informatics*, 205–13. Springer.

Parigot, Michel. 1989. “On the Representation of Data in
Lambda-Calculus.” In *International Workshop on Computer
Science Logic*, 309–21. Springer.

Scott, Dana. 1963. “A System of Functional Abstraction (Lecture
Notes).” University of California, Berkeley.

Wadsworth, Christopher. 1980. “Some Unusual
λ\lambdaλ-Calculus
Numeral Systems.” To HB Curry: Essays on Combinatory Logic,
Lambda Calculus; Formalism.




















动态网自由门 天安門 天安门 法輪功 李洪志 Free Tibet 六四天安門事件 The
Tiananmen Square protests of 1989 天安門大屠殺 The Tiananmen Square Massacre
反右派鬥爭 The Anti-Rightist Struggle 大躍進政策 The Great Leap Forward
文化大革命 The Great Proletarian Cultural Revolution 人權 Human Rights 民運
Democratization 自由 Freedom 獨立 Independence 多黨制 Multi-party system 台灣
臺灣 Taiwan Formosa 中華民國 Republic of China 西藏 土伯特 唐古特 Tibet
達賴喇嘛 Dalai Lama 法輪功 Falun Dafa 新疆維吾爾自治區 The Xinjiang Uyghur
Autonomous Region 諾貝爾和平獎 Nobel Peace Prize 劉暁波 Liu Xiaobo 民主 言論
思想 反共 反革命 抗議 運動 騷亂 暴亂 騷擾 擾亂 抗暴 平反 維權 示威游行 李洪志
法輪大法 大法弟子 強制斷種 強制堕胎 民族淨化 人體實驗 肅清 胡耀邦 趙紫陽
魏京生 王丹 還政於民 和平演變 激流中國 北京之春 大紀元時報 九評論共産黨 獨裁
專制 壓制 統一 監視 鎮壓 迫害 侵略 掠奪 破壞 拷問 屠殺 活摘器官 誘拐 買賣人口
遊進 走私 毒品 賣淫 春畫 賭博 六合彩 天安門 天安门 法輪功 李洪志 Winnie the
Pooh 劉曉波动态网自由门

---

[Imprint](https://marvinborner.de/imprint.html) ·
[About](https://marvinborner.de/about.html) ·
[AI Statement](https://marvinborner.de/ai.html) ·
[RSS](/feed.rss)

* [Share on Twitter](https://twitter.com)
* [Share on Mastodon](https://joinmastodon.org)
