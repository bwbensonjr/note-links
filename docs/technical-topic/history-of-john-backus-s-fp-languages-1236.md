---
id: 1236
url: https://softwarepreservation.computerhistory.org/FP/
title: History of John Backus's FP languages
domain: softwarepreservation.computerhistory.org
source_date: '2026-07-26'
tags:
- compilers
- academic-paper
summary: John Backus conducted decades of research into functional and applicative
  programming languages from the late 1960s through his retirement in 1991, driven
  by his conviction that conventional programming languages were overly complex and
  inefficient due to the "von Neumann bottleneck." His work began with languages like
  Red and evolved through a series of function-level languages designed to simplify
  programming through composition and combining forms, inspired partly by APL. This
  preservation project documents the history and surviving materials from Backus's
  groundbreaking research, which fundamentally challenged prevailing assumptions about
  programming language design during the software crisis era.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# History of John Backus's FP languages

[![Software Preservation Group of the Computer History Museum](../logo.jpg)](../)

History of John Backus's functional programming project
=======================================================

\*\*\*\*\* Work in progress \*\*\*\*\*
--------------------------------------

Paul McJones  
paul@mcjones.org  
[https://mcjones.org/dustydecks](https://mcjones.org/dustydecks/)

Hacker News discussion: <https://news.ycombinator.com/item?id=49038035>

Last modified 27 July 2026

Abstracts
---------

John Backus explored a sequence of applicative, functional and function-level languages starting before 1969 and continuing until
he retired in 1991. The goal of this project is to preserve the surviving materials from this research and to put them into context. Comments, suggestions, and donations of additional materials are greatly appreciated.

Contents
--------

* [Acknowledgements](#acknowledgements)
* [The software crisis](#crisis)
* [Launching a project](#launch)
* [Another assistant](#assistant)
* [The Turing Lecture](#turing)
* [Refining the algebra](#algebra)
* [The FL team](#FL)
* [Implementations by others](#others)
* [Assessment](#assess)
* [References](#refs)
* [Related resources](#related_resources)

Acknowledgements
----------------

* John Backus for hiring me in 1974 and giving me a number of historic materials in 2004.
* Scott Baden for a copy of [[Baden1983b]](#Baden1983b).
* Edoardo S. Biagioni for the source code to his [FPC](#Biagioni1988) and information about Gyula A. Magó's FFP Machine project.
* Dines Bjørner for information on his work with John Backus.
* Will Partain for information about Gyula A. Magó.
* Barry Rosen for permission to post [[Rosen1974a](#Rosen1974a), [b](#Rosen1974b)].

The software crisis
-------------------

In the late 1960s the "software crisis" became a frequent topic of discussion. Computers had become much
more capable
in speed and memory sizes and prices had come down, but as ambitions grew, a number of programming projects suffered from cost and shedule overruns and poor reliability. A pair of NATO-sponsored conferences on Software Engineering in 1968 and 1969 brought attention to the problems and served as an initial forum for discussing solutions, which included formal methods, design methodologies, and management techniques.

Although John Backus attended neither of these conferences, they resonated with his long-held desire to simplify the task of programming. He'd had early success with his Speedcoding and FORTRAN projects. FORTRAN in particular revolutionized the task of writing numerically-oriented programs, in many cases allowing scientists and engineers to write programs rivalling or exceeding the performance of programs written by professional programmers—members of the "priesthood," as Backus sometimes referred to them. After FORTRAN, he participated in the Algol project, and in 1963 was named an IBM Fellow in 1963, giving him the flexibility to choose any problem to work on. He then spent a number of years working on [four color conjecture](https://en.wikipedia.org/wiki/Four_color_theorem) (now theorem). But somewhere around 1967–1969, Backus decided to take another try at the programming problem:

> "I was just trying to think of some sort of really higher level
> programming that wasn’t as difficult as Fortran. The problem was that the idea of functional programming, the 'combining forms' and stuff like that, came pretty easily. But trying to make it into a real full system where you could deal with all the other issues that you couldn’t express in that language got very confusing and messy." [[Booch2007](#Booch2007)]

Launching a project
-------------------

For several years, Backus worked mostly alone on this new idea. Ted Codd consulted with him briefly, but that didn't last
[Booch2007]. In late 1969, Dines Bjørner began working with him, first explaining the details of lambda-calculus and Curry's Combinatory Logic, then writing an interpreter (in PL/I) based on “finite state tree-transformer” semantic for Backus's language (which was then called RedSys) [[Bjørner2025](#Bjørner2025), [1972](#Bjørner1972)]. Bjørner
worked with Backus until 1972, when they parted ways; Bjørner went on to work with Ted Codd [[Bjørner2025](#Bjørner2025)], [[BjørnerEtAl1973](#BjørnerEtAl1973)].

Backus's first publication was a 1972 research report titled "Reduction languages and variable-free
programming"; the report acknowledges Bjørner "for writing a program to reduce Red items which was used to test some of the operators in this paper."[[Backus1972a](#Backus1972a)] This report introduced a family of expression-oriented languages with semantics given by simple rewrite rules. The featured language, called Red for reduction, was similiar in size to Pure Lisp [McCarthy1960], but rather than defining a function by describing its effect on the formal parameters, the programmer built up a function from a set of base functions using a function composition operator as well as a set of combining forms (here known as 'modifiers'). Each function took one (implicit) argument, which could be a sequence. This led to a programming style somewhat reminiscent of APL's "one-liners", and Backus later cited APL as an inspiration. During 1972, Phil Summers (then probably a graduate student intern from Yale, later an IBM researcher) did an experimental
implementation of Red in Lisp [[Summers1972](#Summers1972)].

This first report was fairly mild in its claims about Red, which he positioned more as a formal system than a practical programming
language. In 1973 he followed up with a paper,presented at the first ACM Principles of Programming Languages conference [Backus1973a, c]. It refined the hierarchy of languages, presented a tidied-up version of Red as the centerpiece and concluded: "Hopefully, this work will lead to a semantic theory for a new class of programming languages, one which possesses an axiomatic foundation of the simplicity required for rigorous mathematical treatment."

During 1973, Backus went on the lecture circuit, giving 14 lectures at universities and research labs across the country [[Backus1973d](#Backus1973d)]. His annual report as an IBM Fellow described that year's work on language frameworks and the Red language, and then made two claims [[Backus1974a](#Backus1974a)]:

1. "Simple, whole-entity programming languages, as contrasted to conventional complex, word-at-a-time programming languages,
   have the potential for drastically reducing the cost of programming.
2. Present efforts to clean up and extend conventional concepts of programming languages have no such potential; ... indeed
   they will continue to add complexity to languages without dealing with the word-at-a-time problem, as they have for the past 15 years, and thereby actually increase the cost of programming and the expertise required for its practice. (Thus PL/I is perhaps 10 times as complex as Fortran, less economical in execution, and only 20-30% more powerful in expressiveness.)"

He concluded, "If there is any truth to the two assertions above, then Research should ask itself whether it has fallen into
a comfortable but mistaken orthodoxy with respect to programming languages. I believe it should re-evaluate its emphasis and goals in computer science and programming; at least IBM computer scientists should be aware that reducing the cost of programming would do more to help IBM's growth than perhaps any other technical, accomplishment." In support of these claims, he introduced the phrase "von Neumann bottleneck"—the word-at-a-time nature of conventional computers—and argued that this carried over to the design of conventional programming languages, leading to their inefficiency and complexity.

It fell to Patricia Goldberg, Manager of the Automatic Programming group at IBM's Watson Research Center, to respond to Backus
[[Goldberg1974](#Goldberg1974)]. She agreed with the criticality of reducing the cost of programming, the need to go beyond languages of the "PL/I genre," the significance of APL, and the importance of discovering aggregate operations in various fields. But she noted, "I am not, however, convinced that we ought altogether to dispense with the notion of an explicit store and an assignment operator." She pointed out ongoing work at IBM on non-von Neumann frameworks as well as attempts to integrate these into useful programming systems. Backus responded with a vigorous reiteration of the need for IBM Research to study language frameworks with the goal of defining a very simple framework supporting rich definitions [[Backus1974b](#Backus1974b)].

Another assistant
-----------------

Despite the lukewarm response from research management, Backus persevered. In the "Plans for 1974" section of his 1973 annual report, Backus had mentioned, "If time and assistance permit, I hope to begin work on an optimizing interpreter for Red languages." He let it be known he was interested in hiring someone to work with him , and Jim Gray, then at IBM San Jose Research and knowing I was looking for permanent employment, introduced me to Backus. I'd attended one of his lectures at UC Berkeley in 1972 and signed up for his mailing list, so I'd received and at least partially digested his two research reports. I'd also worked on interpreters for [Snobol4](https://www.mcjones.org/CAL_SNOBOL/) and [APL](https://doi.ieeecomputersociety.org/10.1109/MAHC.2026.3652780). For the next 15 months or so, I worked with Backus to refine the language and to explore implementation ideas, including writing some experimental interpreters in Lisp and Mcg, an ISWIM-like language designed by W. H. Burge [[Burge1968](#Burge1968)]. I gave a short talk to the department shortly after joining [[McJones1974b](#McJones1974b)] and wrote a technical report on "A Church-Rosser Property of Closed Application Languages" [[McJones1975](#McJones1975)]. During this time Backus and I explored a series of minor variations on the Red language—see [[Backus1974b](#Backus1974b)] through [[Backus1975b](#Backus1975b)]. Work on the algebra of programs (first mentioned in [Backus1974a]) and modeling state transformations also begin. Sensing that the language was still in flux and the emphasis was more on formal methods than actual implementation, I eventually moved over to the [System R](https://bitsavers.org/pdf/dec/tech_reports/SRC-TN-1997-018.pdf) relational database project.

\*\*\*\*\* Include some of my Red evaluators?

During this period several researchers at universities began projects based on Backus's ideas. Klaus Berkling initiated design work at GMD in Germany for a reduction-based machine influenced by [[Backus1973c](#Backus1973c)]; it is said the be the first reduction machine actually implemented [[Berkling1975](#Berkling1975)], [[Kluge1983](#Kluge1983)]. Also Gyula A. Magó at the University of North Carolina initiated the FFPM project [[Magó1976](#Magó1976)]. [[Partain1989](#Partain1989)] describes these and other graph reduction machines.

The Turing Lecture
------------------

John Backus received the 1977 ACM Turing Award "For profound, influential, and lasting contributions to the design of
practical high-level programming systems, notably through his work on FORTRAN, and for seminal publication of formal procedures for the specification of programming languages." His award lecture "Can Programming Be Liberated from the von Neumann Style? A Functional Style and Its Algebra of Programs" was published in the *Communications of the* ACM, received by all ACM members [[Backus1978b](#Backus1978b)]. He argued:

> "Conventional programming languages are growing ever more enormous, but not stronger. Inherent defects at the most basic level cause them to be both fat and weak: their primitive word-at-a-time style of programming, inherited from their common ancestor—the von Neumann computer, their close coupling of semantics to state transitions, their division of programming into a world of expressions and a world of statements, their inability to effectively use powerful combining forms for building new programs from existing ones, and their lack of useful mathematical properties for reasoning about programs."

The alternative he proposed was an "informal" functional programming language FP (with a related "formal" version FFP), an algebra of functional programs, and a framework for
applicative state transitions (AST) for modeling history-sensitive systems. FP included a set of primitive functions for working with numbers, atoms, and sequences, as well as a set of combining forms for constructing more complex functions from simpler ones. Here's an example function for matrix multiplication:

> **Def MM ≡ (ααIP) ○ (αdistl) ○ distr ○ [1st, trans ○ 2nd]**

**○** represents function composition, **α** applies a function to each element of a sequence, and **[,...,]** applies a list of functions to a value, producing a sequence of results. **MM** expects a pair of compatible matrices, each represented as a sequences of rows. Reading from right to left, the function in brackets transposes the second matrix while leaving the first matrix intact. **distr** pairs a copy of the transposed second matrix with each row of the first matrix. **αdistl** applies **distl** to each such pair, resulting in a sequence of sequences of pairs of rows. **ααIP** applies **IP** (inner product) to each such pair, thus producing the desired matrix product.

Note ony functions are mentioned, never the data items (variables or constants) to which they are applied. (There was a combining form for creating a constant-valued function from a data value.) This later became known as point-free style. Backus felt it contributed greatly to the power and simplicity of FP.

One of the problems with conventional languages cited by Backus was their complexity and the resultant difficulty in specifying them and proving properties about them. In contrast, Backus exhibited an algebra of programs for FP that could be used for showing program equivalance, for example when transforming a program to a more efficient form. The algebra was based on identities stemming from the properties of the combining forms, for example:

**[f1, ..., fN] ○ g ≡ [f1 ○ g, ... fN ○ g]**

**αf ○ [g1, ..., gN] ≡ [f ○ g1, ..., f ○ gN]**

**/f ○ [g1, g2, ... gN-1, gN] ≡ f ○ [g1, f ○ [g2, ... f ○ [gN-1, gN]...] ]**

**/** takes a function on pairs and produces a function on sequences, like APL's reduction operator.

There were also theorems based on these laws for more complex transformations, such as for converting a self-referencing
definition into an (infinite) conditional. The paper spent many pages explaining and proving several of these theorems. Examples showed the equivalence between recursive and non-recursive versions of matrix multiplication and factorial.

Finally, Backus presented Applicative State Transition systems, in which the system has a state consisting of a set of named cells
each containing a user-defined function or a data item. The user submits a series of inputs, each of which is examined by a system function that dispatches to the appropriate handler, which runs a computation and then produces a pair (output, new state). The system function does a validity check on the new state, then installs it and sends the output to the user. The paper describes this in some detail, including bootstrapping from an empty state, and suggests various ways the system could be elaborated.

### Reaction to the paper

Given the prestige of the Turing Award and the provocative title, many people read and discussed the paper. Personal letters from Dana Scott and Robin Milner congratulated Backus in his effort to bring proofs of programs to working programmers, but pointed out a number of technical problems with FP and FFP and encouraged him to base his work on an extended typed λ-calculus such as presented in [[Scott1976](#Scott1976)]. (Scott also chided, "Thank you very much indeed for the several kind references to me. Of course, just as you use the name 'von Neumann' in a generic sense, so you use 'Scott'. I would have suggested including references to my Turing lecture [[Scott1977](#Scott1977)] and to the SIAM paper [[Scott1976](#Scott1976)] where some of the other contributors arc mentioned.") [Scott1978a, b] [Milner1978a, b] \*\*\*\*\* Add these plus Backus-Letter\_to\_Dana\_Scott-1978\_09\_14.pdf to References, part 1.

A more energetic interchange was launched when Edsger Dijkstra reviewed Backus's lecture as number 692 in his personal EWD series, which was directly distributed to about a dozen of Dijkstra's friends but made its way indirectly to a larger audience, including Backus. Its conclusion was relatively bland [[Dijkstra1978b](#Dijkstra1978b)]:

> "In short, the article is a progress report on a valid research effort but suffers badly from aggressive
> overselling of its significance, long before convincing results have been reached. This is the more regrettable as it has been published by way of Turing Award Lecture."

but the full review was quite negative, and triggered an exchange of letters between Backus and Dijkstra [[Chin2016](#Chin2016)] in which Dijkstra declared his review had been a "political pamphlet" aimed to counter what he apparently felt was Backus's attack on the axiomatic semantics being developed by Dijkstra, Hoare, and others.

By 2026, the ACM's Digital Library recorded over 2000 citations of [[Backus1978b](#Backus1978b)], with more trickling in. Although the vast majority seemed to cite the paper as a reference for "von Neumann architecture", many dozen papers, especially in the first decade, were genuine attempts to apply or extend Backus's ideas in a variety of ways:

* Extending the algorithm of programs: Banerjee, ...
* Optimizing transformations: Bellegarde, Norman, ...
* Implementations: Baden, Choppy et al., Robinson, Biagionni, Valencia, Deleuze.
* Parallel computation: Ben-Asher et al., Christopher and Ameiss
* Database querying: Bossi and Ghezzi, Buneman and Frankel
* Stream processing: Ida and Tanaka, Sheeran, Shultis, Thomas and Stanat
* Lazy evaluation: Dosch and Möller, Radensky
* VLSI design: Sheeran, Tsanakas et al.
* Data flow machines: Zhang et al.
* and many more -- see [References, part 2](#refs_part2)

Motivating and refining the algebra
-----------------------------------

Backus had worked alone since I moved to the System R project in 1975. In July 1978 he was joined by John Hayden Williams.
Williams received his PhD at the University of Wisconsin-Madison with a dissertation entitled [Bounded Context Parsable Grammars](https://mathgenealogy.org/id.php?id=82728). He joined the faculty at Cornell University, where he conducted research on programming languages. At some point he met John Backus, who mentioned him in the acknowledgements to [[Backus1973a](#Backus1973a)] and [[Backus1978b](#Backus1978b)]. Perhaps the idea of joining IBM was discussed in December 1977, when Backus gave a talk at Cornell [[Backus2003](#Backus2003), item 159].

Backus and Williams set to work to improve the algebra of programs. That summer Williams was one of the lecturers at the annual
NATO Summer School at Marktoberdorf, Germany. Dijkstra reported [[Dijkstra1978a](#Dijkstra1978a)]:

> "The last lecture of the last day --on Reduction Languages-- was given by one of the participants, John
> H. Williams (in the process of moving from Cornell University to IBM? San Jose). It was a brilliant lecture, forcefully delivered. In view of the fact that the participants were the best part of the Summer School, we couldn't have wished for a more appropriate closing lecture."

In August 1979 Backus presented a draft paper at the Summer Workshop on Programming Methodology at UC Santa Cruz
[[Backus1979](#Backus1979)]. As with his Turing Award Lecture, he spent many pages comparing his functional approach to a "von Neumann language". His approach was to focus on formal semantics. In an imperative language with statements, assignments, and side-effects, the meaning of a statement (or expression with side-effects) must be modeled as a function mapping stores (memory states) to stores, whereas a functional program is a function mapping values (inputs) to values (outputs). Although he assured the reader he wasn't setting up a "straw man", his informal description of denotational semantics for imperative languages was written in an acerbic style. He concluded that a functional program, using four main combining forms (constant, composition, condition, and construction)
was much more powerful because of the existence of the algebra of programs interrelating these combining forms. Of course imperative languages have analogs of these combining forms: constants, compound expressions and semicolon for sequencing statements, conditional expressions and statements, and local variables, but admittedly proofs of correctness and equivalence for imperative languages typically require full predicate logic rather than the equational style advocated by Backus. To be fair, Backus pointed out two problems preventing adoption of functional style: "naming" (variables are useful when lots of quantities need to be kept track of) and "forgetting" (simulating variables with functions brings in stores). The second part of the paper further developed the "linear expansion theorem" of his Turing Award lecture.

[Williams80]

[Backus1981a]:  
\*
Long contrast with von Neumann language replaced with much shorter contrast with lambda-calculus language. Admits lambda-calculus langage can define all the program-forming operations, but claims this gives too much freedom; proposes it's time for new generation of functional languages, languages that emphasize function level structure and reasoning.  
\* Language and algebra: more crisply defined,  
\* Paper on algebra of functions by https://fr.wikipedia.org/wiki/François-Henri\_Raymond  
\* https://bibliotheques.cnam.fr/opac/resource/formalisation-du-concept-de-calcul-algebre-des-fonctions/CNA00349392

\*\*\*\*\* [Backus1981b] through [Backus1985c], [Williams1980] through [Williams1982], [HalpernEtAl1985] through [HalpernEtAl1990], ...

\*\*\*\*\* [GuttagEtAl1981]

\*\*\*\*\* Edward L Wimmers since 9/83

\*\*\*\*\* FP84: https://en.wikipedia.org/wiki/FP\_(programming\_language)#FP84, [WilliamsWimmers1988]

> "Informally, FP84 is the result of altering the language FP of [Backus 781 to include infinite sequences, programmer-defined combining forms, and lazy evaluation. Moreover, unlike the formal language FFP of [Backus 781, FP84 makes a clear distinction between objects and functions; i.e., sequences of objects are no longer used to represent functions. These extensions are accomplished in FP84 by removing the FP restriction that sequence construction be applied only to non-l objects; in FP84 the entire set of expressions (including those whose meaning is I) is closed under sequence construction. A complete description of FP84, including an operational and a denotational semantics, may be found in [HWI 853 and [HW2 863."

\*\*\*\*\* Mary Sheeran <https://www.chalmers.se/en/research/meet-our-scientists/researcher-profiles/programming-pioneer-with-a-passion-for-an-inclusive-academia/>

\*\*\*\*\* Note [HughesEtAl1987]: John Hughes is Mary Sheeran's husband...

Implementing FL
---------------

\*\*\*\*\* Peter Lucas since 2/88

\*\*\*\*\* Alexander S. Aiken since 8/88

\*\*\*\*\* Thom Linden since 11/88

\*\*\*\*\* Reports: [BackusEtAl1989], ...

\*\*\*\*\* Status of FL, 1988 (see slide)

Implementations by others
-------------------------

Scott Baden's Berkeley FP was an interpreter written in [Franz Lisp](https://softwarepreservation.computerhistory.org/LISP/maclisp_family.html#Franz_Lisp_) and was distributed with several releases of Berkeley Unix;
see [[BadenPatel198x](#BadenPatel1983)], [[Baden1983a](#Baden1983a)–[c](#Baden1983c)].

Arch Robinson's Illinois FP was also an interpreter written in C; it was distributed via the USENET news group comp.sources.unix. See [[Robinson1987a](#Robinson1987a)–[e](#Robinson1987e)].

Edoardo S. Biagioni's FPC was written in C; it translated FP to C, which was then compiled with a C compiler; version 1.0 was distributed via the USENET news group comp.sources.unix. See [[Biagioni1988](#Biagioni1988)].

Andy Valencia's Stanford FP was an interpreter written in C and distributed via the USENET news group comp.sources.unix. See [[Valencia1986](#Valencia1986)].

Christophe Deleuze's oc-FP was an interpreter written in OCaml and is distributed via the Deleuze's web site. See [[Deleuze2003](#Deleuze2003)].

Assessment
----------

References
----------

### Part 1: By or about Backus and his colleagues

[Aiken1988]
:   Alex Aiken. Optimization Strategies for FL.
    5 October 1988.
    [PDF](doc/Aiken-Optimization_Strategies_for_FL-1988_10_05.pdf)

[AikenEtAl1990]
:   Alexander Aiken, John H. Williams, and Edward L. Wimmers. The Program Feature in FL.
    IBM Almaden Research Center, 16 October 1990.
    [PDF](doc/Aiken_Williams_Wimmers-The_Program_Feature_in_FL-1990_10_16.pdf)

[Aiken1991]
:   AA [Alex Aiken]. Another Stab at Monads. 29 April 1991.
    [PDF](doc/Aiken-Another_Stab_at_Monads-1991_04_29.pdf)

[AikenEtAl1991]
:   Alex Aiken, Brennan Gaunce, Brian Murphy. Implementing FL in C. 22 June 1991.
    Not listed in [[Backus2003](#Backus2003)].
    [PDF](doc/Aiken_Gaunce_Murphy-Implementing_FL_in_C-1991_06_22.pdf)

[AikenMurphy1991a]
:   Alexander Aiken and Brian R. Murphy. Implementing Regular Tree Expressions.
    In *Proceedings of the 5th ACM Conference on Functional Programming Languages and Computer Architecture*.
    Springer-Verlag, Berlin, Heidelberg, 427–447.
    <https://theory.stanford.edu/~aiken/publications/papers/fpca91.pdf>

[AikenMurphy1991b]
:   Alexander Aiken and Brian R. Murphy. Static type inference in a dynamically typed language.
    In *Proceedings of the 18th ACM SIGPLAN-SIGACT symposium on Principles of programming languages (POPL '91).*
    Association for Computing Machinery, New York, NY, USA, 279–290.
    <https://doi.org/10.1145/99583.99621>

[AikenEtAl1991]
:   Programming a language. Unpublished document, 1991. See item 189 of [Backus2003].

[AikenEtAl1993]
:   Alexander Aiken, John H. Williams, and Edward L. Wimmers.
    The FL Project: The design of a Functional Language.
    IBM Almaden Research Center, September 1993.
    <https://theory.stanford.edu/~aiken/publications/trs/FLProject.pdf>
    / [PDF](doc/Aiken_Williams_Wimmers_The_FL_Project-1993.pdf)

[AikenEtAl1995]
:   Alexander Aiken, John H. Williams, and Edward L. Wimmers.
    Safe: a semantic technique for transforming programs in the presence of errors.
    *ACM Trans. Program. Lang. Syst.* 17, 1 (Jan. 1995), 63–84.
    <https://doi.org/10.1145/200994.201002>

[Backus1972a]
:   John Backus. Reduction languages and variable-free programming.
    RJ 1010, IBM Research Laboratory, San Jose, California, 7 April 1972.
    [PDF](doc/Backus-RL_and_VFP-RJ1010-1972.pdf)

[Backus1972b]
:   John Backus. Re: "Reduction languages and variable-free programming."
    Cover letter for RJ 1010.
    IBM Research Laboratory, San Jose, California, 19 April 1972.
    [PDF](doc/Backus-Re_RL_and_VFP-1972_04_19.pdf)

[Backus1973a]
:   John Backus. Programming language semantics and closed applicative languages.
    RJ 1245, IBM Research Laboratory, San Jose, California, 5 July 1973.
    [PDF](doc/Backus-PLS_and_CALs-RJ1245-1973.pdf)

[Backus1973b]
:   John Backus. To Recipients of "Reduction languages and variable-free programming."
    Cover letter for RJ 1245.
    IBM Research Laboratory, San Jose, California, 17 July 1973. Paul McJones's copy, with errata applied.
    [PDF](doc/Backus-Recipients_of-RL_and_VFP-1973_07_17.pdf)

[Backus1973c]
:   John Backus. Programming language semantics and closed applicative languages.
    In *Proceedings of the 1st annual ACM SIGACT-SIGPLAN symposium on Principles of Programming Languages (POPL '73)*. Association for Computing Machinery, New York, NY, USA, 71–86.
    <https://doi.org/10.1145/512927.512934>

[Backus1973d]
:   John Backus. Class notes -- Red languages. Probably for two one-hour lectures at the University of California, Santa Cruz? See [[Backus1974a](#Backus1974a)].
    14 November 1973, 6 pages: [PDF](doc/Backus-Class_notes_Red_languages-1973_11_14.pdf) /
    21 November 1973, 7 pages: [PDF](doc/Backus-Class_notes_Red_languages-1973_11_21.pdf)

[Backus1974a]
:   John Backus. Memorandum for R. E. Gomory. Annual report and Research goals in programming.
    21 January 1974, 7+1 pages.
    [PDF](doc/Backus-Annual_report_and_Research_goals-1974_01_21.pdf)

[Backus1974b]
:   John Backus. Memorandum for P S. Dauber and P. C. Goldberg. Pat Goldberg's memo of 2/15/74.
    IBM San Jose Research Laboratory, 19 March 1974, 3 pages.
    [PDF](doc/Backus-Pat_Goldberg_memo-1974_03_19.pdf)

[Backus1974b]
:   John Backus. Definition of Red with "items" and "rows". As transcribed by Paul McJones, 10 May 1974.
    [PDF](doc/McJones-Red_notes-1974_1975.pdf#page=24)

[Backus1974c]
:   John Backus. Proposal for a quote-like feature: pseudo-applications. As transcribed by Paul McJones, 20 May 1974.
    [PDF](doc/McJones-Red_notes-1974_1975.pdf#page=26)

[Backus1974d]
:   John Backus. Semantic definitions, top down and bottom up. As transcribed by Paul McJones, 23 May 1974.
    [PDF](doc/McJones-Red_notes-1974_1975.pdf#page=27)

[Backus1974e]
:   John Backus. John's definitions: Red with "instruction", "world pair" {e, environment}.
    As transcribed by Paul McJones, 30 October 1974.
    [PDF](doc/McJones-Red_notes-1974_1975.pdf#page=56)

[Backus1974f]
:   John Backus. Red with Rows and Contexts. Includes quoted expressions per [McJones1974a].
    As transcribed by Paul McJones, circa 10 December 1974.
    [PDF](doc/McJones-Red_notes-1974_1975.pdf#page=57)

[Backus1974g]
:   John Backus. Red with Contexts (but no general rows).
    As transcribed by Paul McJones, 20 December 1974.
    [PDF](doc/McJones-Red_notes-1974_1975.pdf#page=61)

[Backus1974h]
:   John Backus. "Proper expressions." As transcribed by Paul McJones, 30 December 1974.
    [PDF](doc/McJones-Red_notes-1974_1975.pdf#page=62)

[Backus1975a]
:   John Backus. Syntax and semantics. 29 January 1975.
    [PDF](doc/McJones-Red_notes-1974_1975.pdf#page=64)

[Backus1975b]
:   John Backus. Class notes -- A variable-free functional programming system, FP.
    19 February 1975, 9 pages:
    [PDF](doc/Backus-Class_Notes_I-FP-1975_02_19.pdf) /
    5 March 1975, 3 pages:
    [PDF](doc/Backus-Class_Notes_II-FP-1975_03_05.pdf) /
    30 April 1975, 7 pages:
    [PDF](doc/Backus-Class_Notes_III-FP-1975_04_30.pdf) /
    7 May 1975, 5 pages:
    [PDF](doc/Backus-Class_Notes_IV-FP-1975_05_07.pdf)

[Backus1978a]
:   John Backus. Can Programming be liberated from the von Neumann Style? A functional style and its algebra of programs.
    RJ 2234, IBM Research Laboratory, San Jose, California 95193, 25 April 1978, 98 pages. Paul McJones's autographed copy.
    [PDF](doc/Backus-Von_Neumann_Style-RJ2234-1978.pdf)

[Backus1978b]
:   John Backus. Can Programming be liberated from the von Neumann Style? A functional style and its algebra of programs.
    1977 ACM Turing Award Lecture. *Commun. ACM* 21, 8 (August 1978), 613–641.
    <https://doi.org/10.1145/359576.359579>

[Backus1979]
:   J. W. Backus. On extending the concept of program and solving linear functional equations.
    Draft paper distributed at Summer Workshop on Programming Methodology, Univ. of Calif. at Santa Cruz, Santa Cruz, Calif., August 1979. Backus's correction copy. A revised version was published as [[Backus1981a](#Backus1981a)].
    [PDF](doc/Backus-On_Extending_the_Concept_of_Program_Correction_Copy-1979.pdf)

[Backus1981a]
:   John Backus. The algebra of functional programs: Function level reasoning, linear equations, and extended definitions.
    In: J. Diaz, I. Ramos (eds.). *Formalization of Programming Concepts.
    International Colloquium, Peniscola, Spain, April 19-25, 1981. Lecture Notes in Computer Science 107*,
    Berlin-Heidelberg-New York: Springer 1981, 1-43.
    <https://doi.org/10.1007/3-540-10699-5_91> /
    [PDF](doc/Backus-Algebra_of_FP_FLR_LE_and_ED-LNCS107_1981.pdf)

[Backus1981b]
:   John Backus. Function level programs as mathematical objects.
    In *Proceedings of the 1981 conference on Functional programming languages and computer architecture (FPCA '81)*. Association for Computing Machinery, New York, NY, USA, 1–10, 18 October 1981.
    <https://doi.org/10.1145/800223.806757>

[Backus1981c]
:   John Backus. Is Computer Science Based on the Wrong Fundamental Concept of 'Program'? An Extended Concept.
    In *Algorithmic Languages*, de Backker and van Vliet (eds).
    International Symposium on Algorithmic Languages Amsterdam, The Netherlands, 26-29 October 1981.
    IFIP, North-Holland Publishing Company, 1981, pages 133-165.
    <https://ir.cwi.nl/pub/34328/34328D.pdf#page=158> /
    Preprint: [PDF](doc/Backus-Is_Computer_Science-1981.pdf)

[Backus1982a]
:   John Backus. The algebra of functional programs: Function level reasoning, linear equations, and extended definitions.
    RJ 3555, IBM Research Laboratory, San Jose, California, 23 July 1982. Reprint of [Backus1981a].
    [PDF](doc/Backus-Algebra_of_FP_FLR_LE_and_ED-RJ3555-1982.pdf) /
    Backus's correction copy: [PDF](doc/Backus-Algebra_of_FP_FLR_LE_and_ED-1981.pdf)

[Backus1982b]
:   John Backus. Function-level computing.
    *IEEE Spectrum* 19:8, August 1982, 22-27.
    <https://doi.org/10.1109/MSPEC.1982.6366967> /
    [PDF](doc/Backus-Function_level_computing-IEEE_Spectrum-1982_08.pdf)

[Backus1983]
:   John Backus. The Coming Revolution.
    RJ 3994, IBM Research Laboratory, San Jose, California, 23 August 1983.
    This paper is the text of a lecture given at MIT on May 5, 1983.
    [PDF](doc/Backus-The_Coming_Revolution_in_Computing-RJ3994-1983.pdf)

[Backus1985a]
:   John Backus. From Function Level Semantics to Program Transformation and Optimization.
    RJ 4567, IBM Research Laboratory, San Jose, California, 8 January 1985.
    [PDF](doc/Backus-From_FLS_to_PT_and_O-RJ4567-1985.pdf) + slides \*\*\* To be scanned

[Backus1985b]
:   John Backus. From Function Level Semantics to Program Transformation and Optimization.
    In: Ehrig, H., Floyd, C., Nivat, M., Thatcher, J. (eds)
    *Mathematical Foundations of Software Development. CAAP 1985.* Lecture Notes in Computer Science, vol 185.
    Springer, Berlin, Heidelberg. <https://doi.org/10.1007/3-540-15198-2_5> (open access)

[Backus1985c]
:   John Backus. The Programming Problem. Text and slides for "Future Computing" series of talks,
    IBM Yorktown, 26 July 1985.
    [PDF](doc/Backus-The_Programming_Problem-1985_07_26.pdf)

[BackusEtAl1986]
:   John Backus, John H. Williams, and Edward L. Wimmers The FL language manual.
    RJ 5339, IBM Research Laboratory, San Jose, California, November 1986.

[Backus1988]
:   John Backus. Plan for implementing an FL system. 29 September 1988.
    [PDF](doc/Backus-Plan_for_implementing_an_FL_system-1988_09_29.pdf)

[Backus1989]
:   Programming Languages. Review slides for Juri Matisoo (lab director), 26 April 1989.
    [PDF](doc/Backus-Programming_Languages-1989.pdf)

[BackusEtAl1989]
:   John Backus, John H. Williams, Edward L. Wimmers, Peter Lucas, and Alexander Aiken. FL language manual, Parts 1 and 2.
    RJ 7100, IBM Almaden Research Center, San Jose, California, 26 October 1989.
    [PDF](doc/Backus_et_al-FL_Language_Manual_Parts_1_and_2-RJ7100-1989.pdf)

[Backus1990]
:   John Backus. Annual Fellow report for 1990: The Functional Programming Project. IBM Corporation. 17 December 1990.
    [PDF](doc/Backus-The_Functional_Programming_Project-1990_12_17.pdf)

[BackusEtAl1990]
:   John Backus, John H. Williams, and Edward L. Wimmers. An Introduction to the FL Language.
    In *Research Topics in Functional Programming*, D.A. Turner (Ed.), Addison-Wesley, Reading, MA, 1990.
    Revised excerpt from [BackusEtAl1986].
    [PDF](doc/BackusEtAl-An_Introduction_to_the_FL_PL-1990.pdf)

[Backus2003]
:   John Backus. Items for the Library of Congress, 2003.
    [https://softwarepreservation.computerhistory.org/FORTRAN/Backus%20-%20LOC%20-%20catalogue%20of%20papers.pdf](../FORTRAN/Backus%20-%20LOC%20-%20catalogue%20of%20papers.pdf)

[BeebeMcJones2026]
:   Nelson H. F. Beebe and Paul McJones. A bibliography of publications of John Warner Backus. Report, University of Utah,
    Department of Mathematics, Salt Lake City, UT 84112-0090, USA, 16 June 2026. 35 pp.
    <https://ftp.math.utah.edu/pub/bibnet/authors/b/backus-john-w.html>

[Bjørner1972]
:   Dines Bjørner. Finite State Tree Computations (Part I). RJ-1053, IBM Research, San José, Calf., June 1972.

[BjørnerEtAl1973]
:   D. Bjørner, E. F. Codd, K. L. Deckert, and I. L. Traiger.
    The Gamma-0 n-ary Relational Data Base Interface Specifications of Objects and Operations.
    RJ-1200, IBM San Jose Research Laboratory, 11 April 1973.
    [PDF](doc/RJ1200-Bjorner_et_al-The_Gamma-0_n-ary_Relational_DB_Interface.pdf)

[Bjørner2025]
:   Dines Bjørner. Reflections. 30 December 2025.
    <https://www.imm.dtu.dk/~dibj/2025/reflections/reflektioner.pdf>

[Booch2007]
:   Grady Booch, interviewer. Oral History of John Backus, recorded 5 September 2006.
    X3715.2007, Computer History Museum, 2007. <https://www.computerhistory.org/collections/catalog/102657970/>

[Burge1968]
:   W. H. Burge. Mcg - A Functional Programming System.
    RC-2189, IBM Research, Yorktown Heights, New York, 29 August 1968.
    [PDF](doc/RC2189-Burge-McG-A_Func_Prog_System.pdf)

[Cartwright1976] \*\*\*\*\*
:   Robert Cartwright, Jr. A practical formal semantic definition and verification system for typed Lisp.
    Tech. Rep. AIM-296, Stanford Artificial Intelligence Laboratory, December 1976.
    <https://apps.dtic.mil/sti/tr/pdf/ADA045722.pdf>

[Chin2016]
:   Jiahao Chen. “This guy’s arrogance takes your breath away”: Letters between John W Backus and Edsger W Dijkstra, 1979.
    *Medium*, 29 May 2016. <https://medium.com/@acidflask/this-guys-arrogance-takes-your-breath-away-5b903624ca5f>

[Dijkstra1978a]
:   Edsger W. Dijkstra. Trip report, Marktoberdorf 24 July–6 August 1978.
    <https://www.cs.utexas.edu/~EWD/ewd06xx/EWD676.PDF> / <https://www.cs.utexas.edu/~EWD/transcriptions/EWD06xx/EWD676.html>

[Dijkstra1978b]
:   Edsger W. Dijkstra. A review of the 1977 Turing Award Lecture by John Backus.
    EWD692, undated (late 1978).
    <http://www.cs.utexas.edu/users/EWD/ewd06xx/EWD692.PDF> /
    <https://www.cs.utexas.edu/~EWD/transcriptions/EWD06xx/EWD692.html>

[Goldberg1974]
:   P. C. Goldberg. John Backus's Remarks on Red Languages and Reducing the Cost of Programming.
    Memo to P. S. Dauber, IBM Research Yorktown Heights, 15 February 1974.
    [PDF](doc/Goldberg-John_Backus_remarks-1974_01_15.pdf)

[GuttagEtAl1981]
:   John Guttag, James Horning, and John Williams. FP with data abstraction and strong typing.
    In *Proceedings of the 1981 conference on Functional programming languages and computer architecture (FPCA '81)*.
    Association for Computing Machinery, New York, NY, USA, 11–24.
    <https://doi.org/10.1145/800223.806758>

[HalpernEtAl1985]
:   Joseph Y. Halpern, John H. Williams, Edward L. Wimmers, and Timothy C. Winkler.
    Denotational Semantics and Rewrite Rules for FP.
    In *Proceedings of the 12th ACM SIGACT-SIGPLAN symposium on Principles of programming languages (POPL '85)*.
    Association for Computing Machinery, New York, NY, USA, 108–120.
    <https://doi.org/10.1145/318593.318623>

[HalpernEtAl1986]
:   Joseph Y. Halpern, John H. Williams, Edward L. Wimmers: Good Rewrite Strategies for FP. LICS 1986: 149-162.

[HalpernEtAl1990]
:   Joseph Y. Halpern, John H. Williams, and Edward L. Wimmers. Completeness of rewrite rules and rewrite strategies for FP.
    *J. ACM* 37, 1 (Jan. 1990), 86–143.
    <https://doi.org/10.1145/78935.78939>

[HughesEtAl1987]
:   John Hughes, John Williams, Ed Wimmers, John Backus. Higher Order Functions and I/O in Strict Functional Languages.
    Slides for talk at Year Of Programming Conf., Univ of Texas, 28 August 1987. Item 28 of [Backus2003].
    [PDF](doc/Hughes_et_al-Higher_Order_Functions_and_IO-1987_08.pdf)

[McCarthy1960]
:   John McCarthy. Recursive functions of symbolic expressions and their computation by machine, Part I.
    *Commun. ACM* 3, 4 (April 1960), 184–195.
    <https://doi.org/10.1145/367177.367199>

[McJones1974a]
:   Paul McJones. Proposal for Quoted Expressions in Red. 15 May 1974.
    [PDF](doc/McJones-Red_notes-1974_1975.pdf#page=25)

[McJones1974b]
:   Paul McJones. [Slides for Red talk for Department K55], 20 June 1974.
    [PDF](doc/McJones-Red_notes-1974_1975.pdf#page=42)

[McJones1975]
:   Paul McJones. A Church-Rosser Property of Closed Applicative Languages.
    RJ 1589, IBM Research Laboratory, San Jose, California 95193, 23 May 1975.
    [PDF](doc/McJones-A_CR_Property_of_CALs-RJ1589-1975.pdf)

[McJones1997]
:   Paul McJones, editor. The 1995 SQL Reunion: People, Projects, and Politics.
    Technical Note 1997–018, Systems Research Center, Digital Equipment Corporation, August 20, 1997.
    [PDF](https://bitsavers.org/pdf/dec/tech_reports/SRC-TN-1997-018.pdf)


[Murphy1990]
:   Brian R. Murphy. A type inference system for FL. Master's thesis, MIT, September 1990.
    [PDF](doc/Murphy-A_Type_Inference_System_for_FL-1990.pdf) (from
    [http://suif.stanford.edu/~brm/papers/msthesis.ps.gz)](http://suif.stanford.edu/~brm/papers/msthesis.ps.gz)

[Raymond1975]
:   François-Henri Raymond. Note sur l’algèbre des fonctions. Revue française d’automatique informatique recherche
    opérationnelle. Informatique théorique, tome 9, no R3 (1975), pp. 25–49.
    (French) <http://www.numdam.org/item?id=ITA_1975__9_3_25_0>
    / English translation by Claude.ai [PDF](doc/Raymond_Algebra_of_Functions_1975_EN.pdf)

[Raymond1977]
:   François-Henri Raymond. Note sur la suppression des étiquettes en programmation RAIRO – Informatique théorique, tome 11, no 1 (1977), p. 3-16. <https://www.numdam.org/item/?id=ITA_1977__11_1_3_0> / English translation by Claude.ai [PDF](doc/Raymond_Suppression_of_Labels_1977_EN.pdf)

[Rosen1974a]
:   Barry K. Rosen. Notes on application of complete posets to RED languages.
    Computer Science Department, IBM Watson Research Center, 1 August 1974.
    [PDF](doc/Rosen-Notes_Complete_posets_and_Red-1974_08_01.pdf)

[Rosen1974b]
:   Barry K. Rosen. More notes on application of complete posets to RED languages.
    Computer Science Department, IBM Watson Research Center, 28 October 1974. [PDF](doc/Rosen-More_Notes_Complete_posets_and_Red-1974_10_28.pdf)

[Scott1976]
:   Dana Scott. Data Types as Lattices.
    SIAM Journal on Computing, Volume 5, Number 3, September 1976, pages 522-587.
    <https://doi.org/10.1137/0205037> /
    <https://www.cs.ox.ac.uk/files/3287/PRG05.pdf>

[Scott1977]
:   Dana Scott. Logic and Programming Languages.
    1976 ACM Turing Award lecture. *Comm. ACM*, Vol. 20, 1975, pp. 634-641.
    <https://doi.org/10.1145/359810.359826>

[Summers1972]
:   P. D. Summers.
    Documentation and source code of RED systems based on [[Backus1972a](#Backus1972a)],
    T. J. Watson Research Center, August 1972. See also item 163 of [Backus2003].

    * Sign on and use of the RED system. 11 August 1972. [PDF](doc/Summers-Sign_on_of_RED_System-1972_08_11.pdf)
    * Three algorithms to convert lambda expressions inlo RED language expressions. 15 August 1972. [PDF](doc/Summers-Algorithms_for_lambda_to_RED-1972_08_15.pdf)
    * Summary of RED primitives and their definitions as lambda notations. 29 August 1972. [PDF](doc/Summers-RED_primitives-1972_08_29.pdf)
    * Adding primitives to the RED systems. 29 August 1972. [PDF](doc/Summers-Adding_primitives_to_the_RED_System-1972_08_29.pdf)
    * Annotated listings of the RED systems. 29 August 1972. [PDF](doc/Summers-Annotated_listings_of_the RED_System-1972_08_29.pdf)

[Williams1980]
:   John H. Williams. On the Development of the Algebra of Functional Programs.
    RJ 2983, IBM Research Laboratory, San Jose, California, 30 October 1980.

[Williams1981a]
:   John H. Williams. Formal Representations for Recursively Defined Functional Programs.
    J. Diaz, I. Ramos (eds.). *Formalization of Programming Concepts.
    International Colloquium, Peniscola, Spain, April 19-25, 1981. Lecture Notes in Computer Science 107*,
    Berlin-Heidelberg-New York: Springer 1981, pages 460-470.
    <https://doi.org/10.1007/3-540-10699-5_119>

[Williams1981b]
:   John H. Williams. Notes on the FP Style of Functional Programming.
    In: *Functional Programming and its Applications: An Advanced Course*,
    J. Darlington, P. Henderson, and D. A. Turner (eds.),
    Cambridge University Press, March 1982.
    Proceedings of an advanced course held at Newcastle University, 20-31 July 1981,
    PDF \*\*\* To be scanned

[Williams1982]
:   John H. Williams. On the Development of the Algebra of Functional Programs.
    *ACM Trans. Program. Lang. Syst.* 4, 4 (Oct. 1982), 733–757.
    <https://doi.org/10.1145/69622.357193>

[WilliamsWimmers1988]
:   J. H. Williams and E. L. Wimmers. Sacrificing simplicity for convenience: Where do you draw the line?
    In *Proceedings of the 15th ACM SIGPLAN-SIGACT symposium on Principles of programming languages (POPL '88)*.
    Association for Computing Machinery, New York, NY, USA, 169–179.
    <https://doi.org/10.1145/73560.73575>

[WilliamsWimmers1990]
:   John H Williams and Edward L Wimmers. The new simplification algorithm. 8 February 1990. See item 201 of [[Backus2003](#Backus2003)].

### Part 2: Influenced by Backus

\*\*\*\*\* Add Smoliar?

[AlderighiEtAl1989]
:   M. Alderighi, G. R. Sechi, R. Vaccaro, and L. Verdoscia. A computing unit for FFP function evaluation in support of correctness proofs. In *Proceedings of the 22nd annual workshop on Microprogramming and microarchitecture (MICRO 22)*, 1989. Association for Computing Machinery, New York, NY, USA, 244–253.
    <https://doi.org/10.1145/75362.75426>

[ChristopherAmeiss1990]
:   T. Christopher and D. Ameiss. Functional programming in a parallel environment: the implementation of FP in MDC. SIGPLAN Not. 25, 11 (Nov. 1990), 85–94. <https://doi.org/10.1145/101356.101362>

[BadenPatel1983]
:   S. B. Baden and D. R. Patel. Berkeley FP — Experiences with a Functional Programming Language. *Conference Record of COMPCON ’83*, San Francisco, California, pp. 274–277, March 1983.

[Baden1983a]
:   Scott Baden. Berkeley FP User's Manual, Version 41.
    UNIX Programmer’s Manual Supplementary Documents

    * 27 July 1983. [PDF](doc/Baden-Berkeley_FP_Users_Manual-1983.pdf) / [https://dn790000.ca.archive.org/0/items/upm-supplement-4.2bsd/Image072917173628.merged.pdf#page=345](tt)
    * 12 August 1987. [PDF](doc/Baden-Berkeley_FP_Users_Manual-1983.pdf) / Source files: <https://stuff.mit.edu/afs/athena/astaff/project/docsourc/doc/unix.manual.progsupp2/07.fp/>

[Baden1983b]
:   Scott Baden. DFT → FFT transformation in FP. University of California, Berkeley, 3 May 1983. [PDF](doc/Baden-DFT to FFT Transformation in FP-1983.pdf)

[Baden1983c]
:   Scott Baden. Berkeley FP source code. 1983–1985.

    * 27 February 1983. <https://www.tuhs.org/cgi-bin/utree.pl?file=4.1cBSD/usr/src/ucb/fp>
    * 2 November 1983. <https://www.tuhs.org/cgi-bin/utree.pl?file=4.2BSD/usr/src/ucb/fp>
    * 7 September 1985. <https://www.tuhs.org/cgi-bin/utree.pl?file=4.3BSD/usr/src/ucb/fp>

[Banerjee1992]
:   Debasish Banerjee. A technique for solving a class of quadratic FP equations.
    *Science of Computer Programming*, Volume 19, Issue 1, 1992, Pages 61-85, ISSN 0167-6423.
    <https://doi.org/10.1016/0167-6423(92)90004-U>

[Bellegarde1984]
:   Francoise Bellegarde. Rewriting systems on FP expressions that reduce the number of sequences they yield.
    In *Proceedings of the 1984 ACM Symposium on LISP and functional programming (LFP '84)*.
    Association for Computing Machinery, New York, NY, USA, 1984, pp63–73.
    <https://doi.org/10.1145/800055.802022>

[Bellegarde1986]
:   Françoise Bellegarde. Rewriting systems on FP expressions to reduce the number of sequences yielded.
    *Science of Computer Programming*, Volume 6, 1986, Pages 11-34, ISSN 0167-6423.
    <https://doi.org/10.1016/0167-6423(86)90017-1>

[Bellot1984]
:   Patrick Bellot. Semantiques comparees des systemes de programmation fonctionnelle FP et FFP de J.W. Backus.
    In: Paul, M., Robinet, B. (eds) *International Symposium on Programming. Programming 1984*.
    Lecture Notes in Computer Science, vol 167. Springer, Berlin, Heidelberg, 1984.
    <https://doi.org/10.1007/3-540-12925-1_25>

[Bellot1985]
:   Patrick Bellot. 1985. High order programming in extended FP.
    High order programming in extended FP. In: Jouannaud, JP. (eds) *Functional Programming Languages and Computer Architecture. FPCA 1985*. Lecture Notes in Computer Science, vol 201. Springer, Berlin, Heidelberg.
    <https://doi.org/10.1007/3-540-15975-4_30>

[Ben-AsherEtAl1993]
:   Y. Ben-Asher, G. Rünger, A. Schuster, and R. Wilhelm.
    2DT-FP: An FP based programming language for efficient parallel programming of multiprocessor networks.
    In: Bode, A., Reeve, M., Wolf, G. (eds) *PARLE '93 Parallel Architectures and Languages Europe. PARLE 1993*.
    Lecture Notes in Computer Science, vol 694. Springer, Berlin, Heidelberg, 1993.
    <https://doi.org/10.1007/3-540-56891-3_4>

[Berkling1975]
:   Klaus J. Berkling. Reduction Languages for Reduction Machines.
    2nd Annual Symposium on Computer Architecture, Houston, Texas,
    20–22 January 1975.
    [PDF](doc/Berkling-Reduction_Languages_for_Reduction_Machines-1975.pdf)

[Biagioni1988]
:   Edoardo S. Biagioni. FPC: A Translator for FP.
    Report R88-027, University of North Carolina, May 1988.
    <https://www.cs.unc.edu/techreports/88-027.pdf>

    * [fpc1.0.tar](src/fpc/fpc1.0.tar)
    * [fpc2.0-incomplete.tar](src/fpc/fpc2.0-incomplete.tar) (requires 1.0 to bootstrap)
    * Also:
      <https://sources.vsta.org/comp.sources.unix/volume20/fpc/>

[BossiGhezzi1984]
:   Annalisa Bossi, Carlo Ghezzi. Using FP as a query language for relational data-bases.
    *Computer Languages*, Volume 9, Issue 1, 1984, Pages 25-37, ISSN 0096-0551.
    <https://doi.org/10.1016/0096-0551(84)90010-9>

[BunemanFrankel1979]
:   Peter Buneman and Robert E. Frankel. FQL: a functional query language.
    In *Proceedings of the 1979 ACM SIGMOD international conference on Management of data (SIGMOD '79)*.
    Association for Computing Machinery, New York, NY, USA, 1979, pp52–58.
    <https://doi.org/10.1145/582095.582104>

[Chen1985]
:   Qiming Chen. Extending the implementation scheme of functional programming system FP for supporting the formal software
    development methodology.
    In *Proceedings of the 8th international conference on Software engineering (ICSE '85)*.
    IEEE Computer Society Press, Washington, DC, USA, 1985, pp50–54.
    <https://dl.acm.org/doi/10.5555/319568.319578>

[Chiarini1980]
:   A. Chiarini. 1980. On FP languages combining forms.
    *SIGPLAN Not*. 15, 9 (September 1980), 25–27.
    <https://doi.org/10.1145/947706.947709>

[ChoppyEtAl1983]
:   C. Choppy, G. Guiho, and S. Kaplan. Algebraic semantics for FP languages, a lisp compiler
    and its proof, Rapport LRI N° 133, Orsay, 1983.

[ChoppyEtAl1985]
:   C. Choppy, G. Guiho, and S. Kaplan. A LISP compiler for FP language and its proof via algebraic semantics. In: Ehrig, H., Floyd, C., Nivat, M., Thatcher, J. (eds) *Mathematical Foundations of Software Development, CAAP 1985*.
    Lecture Notes in Computer Science, vol 185. Springer, Berlin, Heidelberg.
    <https://doi.org/10.1007/3-540-15198-2_26> (open access)

[CremersHibbard1983]
:   A. B. Cremers and T. N, Hibbard. Applicative State Transition Systems in LISP-Like Notation. In: Kupka, I. (eds) GI - 13.
    Jahrestagung. *Informatik-Fachberichte*, vol 73. Springer, Berlin, Heidelberg, 1983.
    <https://doi.org/10.1007/978-3-642-69298-7_6>

[Deleuze2003]
:   Christophe Deleuze. oc-FP: An OCAML implementation of John Backus' FP system. Version 0.21, 2003.

    * Documentation.
      <http://christophe.deleuze.free.fr/D/fp.html>
    * Source code.
      <http://christophe.deleuze.free.fr/P/fp.tgz>

[DoschMöller1984]
:   Walter Dosch and Bernhard Möller. Busy and lazy FP with infinite objects.
    *In Proceedings of the 1984 ACM Symposium on LISP and functional programming (LFP '84)*.
    Association for Computing Machinery, New York, NY, USA, 1984, pp282–292. <https://doi.org/10.1145/800055.802045>

[Ei-Affendi1994]
:   M.A. Ei-Affendi. Imposing an FP Layer on a Risc Machine.
    *Journal of King Saud University - Engineering Sciences*, Volume 6, Issue 2, 1994, Pages 167-183, ISSN 1018-3639.
    <https://doi.org/10.1016/S1018-3639(18)30606-8>

[FickertSudkamp1992]
:   Chris Fickert and Thomas Sudkamp. Unification based FP interpreters.
    *SIGPLAN Not*. 27, 11 (Nov. 1992), 49–58.
    <https://doi.org/10.1145/141018.141042>

[Frank1981]
:   Geoffrey A. Frank. Specification of data structures for FP programs.
    In Proceedings of the 1981 conference on Functional
    programming languages and computer architecture (FPCA '81). Association for Computing Machinery, New York, NY, USA, 221–228. <https://doi.org/10.1145/800223.806782>

[George1988]
:   K. M. George. Objects and data structures in the FP paradigm. *Seventh Annual International Phoenix Conference on Computers an Communications*. 1988 Conference Proceedings, Scottsdale, AZ, USA, 1988, pp. 256-260.
    <https://doi.org/10.1109/PCCC.1988.10081>

[HalpernEtAl1988]
:   Brent Hailpern, T. Huynh, and G. Revesz. Comparing two functional programming systems IEEE Transactions on Software Engineering, 15(5):532-542. <http://doi.ieeecomputersociety.org/10.1109/32.24702> Also RJ-12598, IBM Research Division, 17 March 1988. <https://brent.hailpern.com/wp-content/uploads//2019/12/rc12598.pdf>

[HongLingzi1989]
:   Z. Hong and J. Lingzi. A knowledge-based system to synthesize FP programs from examples.
    In: Martins, J.P., Morgado, E.M. (eds) *EPIA 89. EPIA 1989*.
    Lecture Notes in Computer Science, vol 390. Springer, Berlin, Heidelberg.
    <https://doi.org/10.1007/3-540-51665-4_89>

[HuynhEtAl1985]
:   Tien Huynh Brent Hailpern Lee W. Hoevel. An execution architecture for FP. IBM J. Res. Development, Vol. 30, No. 6, November 1986, pages 609-616. <https://brent.hailpern.com/wp-content/uploads/2017/03/IJRD_30_6_1986.pdf> / <https://doi.org/10.1147/rd.306.0609>

[HuynhHailpern1986]
:   Tien Huynh and Brent Hailpern. An Improved DEL-Style Execution Architecture for FP. RC-12202, IBM Thomas J. Watson Research Center, Yorktown Heights, New York 10598, 2 October 1986. <https://brent.hailpern.com/wp-content/uploads/2017/03/rc12202.pdf> Also published in *Proc. Twentieth Hawaii Int. Conf. System Sciences*, vol. 1, Kona, HI, Jan. 1987, pp. 369-376.

[Ida1982]
:   T. Ida. A manual of IPCR-FP.
    Information Science Laboratory, Institute of Physical and Chemical Research. 1982.

[Ida1983]
:   Tetsuo Ida. Some FP algebra with Currying operation.
    *Information Processing Letters*, Volume 17, Issue 5, 1983, Pages 259-261, ISSN 0020-0190.
    <https://doi.org/10.1016/0020-0190(83)90110-2>

[IdaTanaka1983]
:   Tetsuo Ida and Jiro Tanaka. Functional Programming with Streams.
    *Information Processing '83: Proceedings of the IFIP Ninth World Computer Congress*, Sept 19-23, 1983, pp 265-270.

[IslamEtAl1981]
:   N. Islam, T. J. Myers, and P. Broome. A simple optimizer for FP-like languages.
    In *Proceedings of the 1981 conference on Functional programming languages and computer architecture (FPCA '81)*. Association for Computing Machinery, New York, NY, USA, 1981, pp33–40.
    <https://doi.org/10.1145/800223.806760>

[KapurEtAl1981]
:   D. Kapur, D. R. Musser, and A. A. Stepanov. Operators and algebraic structures. In Proceedings of the 1981 conference on Functional programming languages and computer architecture (FPCA '81). Association for Computing Machinery, New York, NY, USA, pp. 59–64. <https://doi.org/10.1145/800223.806763>

[KiebertzShultis1981]
:   Richard B. Kieburtz and Jonathan Shultis. Transformations of FP program schemes.
    In *Proceedings of the 1981 conference on Functional programming languages and computer architecture (FPCA '81)*. Association for Computing Machinery, New York, NY, USA, 1981, pp. 41–48.
    <https://doi.org/10.1145/800223.806761>

[Kluge1983]
:   Werner E. Kluge. Cooperating reduction machines.
    *IEEE Transactions on Computers*, C-32(11):1002-1012, November, 1983.
    <https://doi.org/10.1109/TC.1983.1676151>

[Koster1980]
:   A. Koster. An algorithm for translating LISP programs into reduction language programs.
    In: Robinet, B. (eds) *International Symposium on Programming. Programming 1980*.
    Lecture Notes in Computer Science, vol 83. Springer, Berlin, Heidelberg.
    <https://doi.org/10.1007/3-540-09981-6_14>

[Koster1985]
:   Alexis Koster. Compiling APL for parallel execution on an FFP machine.
    In *Proceedings of the international conference on APL: APL and the future (APL '85)*.
    Association for Computing Machinery, New York, NY, USA, 1985, pp29–37.
    <https://doi.org/10.1145/17701.255327>

[Leszczyłowski1980]
:   J. Leszczyłowski. On Proving Laws of the Algebra of FP-Systems in Edinburgh LCF.
    In Proceedings of AAAI-80, 1980, pages 84–86.
    <https://cdn.aaai.org/AAAI/1980/AAAI80-024.pdf>

[Leszczyłowski1981]
:   J. Leszczyłowski. FP systems in Edinburgh LCF.
    In: Díaz, J., Ramos, I. (eds) *Formalization of Programming Concepts. ICFPC 1981*.
    Lecture Notes in Computer Science, vol 107. Springer, Berlin, Heidelberg, 1981.
    <https://doi.org/10.1007/3-540-10699-5_112>

[LinLin1988]
:   Yen-Chun Lin and Ferng-Ching Lin. The use of aFP to design regular array algorithms.
    *Proceedings. 1988 International Conference on Computer Languages*, Miami Beach, FL, USA, 1988, pp. 388-395.
    <https://doi.org/10.1109/ICCL.1988.13088>

[LuoKatayama1990]
:   Junhui Luo, Takuya Katayama. A Type Inference System for FP Programs.
    *Advances in Software Science and Technology*, Elsevier, Volume 1, 1990, Pages 105-131.
    <https://doi.org/10.1016/B978-0-12-037101-3.50012-0>

[LichtensteinKaplan1990]
:   Lichtenstein, N., Kaplan, S. FPL : Functional plus logic programming an integration of the FP and Prolog languages.
    In: Kaplan, S., Okada, M. (eds) *Conditional and Typed Rewriting Systems. CTRS 1990*.
    Lecture Notes in Computer Science, vol 516. Springer, Berlin, Heidelberg, 1991.
    <https://doi.org/10.1007/3-540-54317-1_98>

[Magó1976]
:   Gyula A. Magó. A network of microprocessors to execute reduction languages.
    Department fo Computer Science, University of North Carolina, June 1976.
    [PDF](doc/Mago-Network_of_Microprocessors-1976_06.pdf)

[Magó1981]
:   Gyula Magó. Copying operands versus copying results: A solution to the problem of large operands in FFP'S. In Proceedings of the 1981 conference on Functional programming languages and computer architecture (FPCA '81). Association for Computing Machinery, New York, NY, USA, 93–98. https://doi.org/10.1145/800223.806767

[NguyenEtAl1986]
:   Van Nguyen, Alan Demers, and Brent Hailpern. FPL: A Functional Parallel Language. RC-11858, IBM Thomas J. Watson Research Center Yorktown Heights, NY 10598, 5 May 1986. PDF

[Norman1986]
:   Eric Norman. Tracking the Elusive Eureka.
    Technical Report TR636, Computer Sciences Department, University of Wisconsin, March 1986.
    z<https://minds.wisconsin.edu/handle/1793/58710>

[OngEtAl1990]
:   E. Teng Ong, K. M. George and K. A. Teague. BT-Server FP Interpreter.
    *Proceedings of the Fifth Distributed Memory Computing Conference, 1990*,
    Charleston, SC, USA, 1990, pp. 1147-1152.
    <https://doi.org/10.1109/DMCC.1990.556329>

[Pagan1986]
:   Frank G. Pagan. On the feasibility of teaching Backus-type functional programming (FP) as a first language.
    *SIGCSE Bull*. 18, 3 (Sep 1 1986), 31–35.
    <https://doi.org/10.1145/378905.378929>

[Pagan1987]
:   Frank G. Pagan. A graphical FP language.
    *SIGPLAN Notices*. 22, 3 (March 1987), 21–39.
    <https://doi.org/10.1145/24697.24699>

[Partain1989]
:   William Partain. Graph Reduction Without Pointers.
    Ph.D. Thesis, TR89-045, Department of Computer Science, University of North Carolina at Chapel Hll, December 1989.
    <https://www.cs.unc.edu/techreports/89-045.pdf>

[PendergrastRyder1986]
:   J. S. Pendergrast and B. G. Ryder. FPOPT: A globally optimizing compiler for FP. Dep. Comput. Sci., Rutgers Univ., Tech. Rep. DCS-TR-175, Mar. 1986.


[PresnellPargas1981]
:   H. A. Presnell and R. P. Pargas. Communication along shortest paths in a tree machine. In Proceedings of the 1981 conference on Functional programming languages and computer architecture (FPCA '81). Association for Computing Machinery, New York, NY, USA, 107–114. <https://doi.org/10.1145/800223.806769>

[Radensky1987]
:   A Radensky. Lazy evaluation and nondeterminism make Backus' FP-systems more practical.
    *SIGPLAN Not*. 22, 4 (April 1987), pp33–40.
    <https://doi.org/10.1145/24714.24718>

[Robinson1987a]
:   Arch D. Robison. A Functional Programming Interpreter. M.S. Thesis, University of Illinois, Urbana-Champaign, January 1987.

[Robinson1987b]
:   Arch D. Robison. Illinois Functional Programming: A Tutorial.
    *BYTE*, Volume 12, Number 2, February 1987, page 114.
    [https://vintageapple.org/byte/pdf/198702\_Byte\_Magazine\_Vol\_12-02\_Image\_Processing.pdf](https://vintageapple.org/byte/pdf/198702_Byte_Magazine_Vol_12-02_Image_Processing.pdf#page=141)

[Robinson1987c]
:   Arch D. Robison. IFP User's Manual.
    Professional Workstation Research Group Technical Report #7, University of Illinois, Urbana-Champaign, 9 February 1987.
    [ASCII](doc/Robinson-IFP_Manual-1987.txt)

[Robinson1987d]
:   Arch D. Robison. The Illinois functional programming interpreter.
    In *Papers of the Symposium on Interpreters and interpretive techniques (SIGPLAN '87)*.
    Association for Computing Machinery, New York, NY, USA, 64–73.
    <https://doi.org/10.1145/29650.29657>

[Robinson1987e]
:   Arch D. Robinson. IFP source code. 7 July 1987.
    <https://sources.vsta.org/comp.sources.unix/volume10/ifp/>

[RyderPendergrast1988]
:   B. G. Ryder and J. S. Pendergrast. Experiments in optimizing FP.
    *IEEE Transactions on Software Engineering*, vol. 14, no. 4, pp. 444-454, April 1988.
    <https://doi.org/10.1109/32.4668>

[Sheeran1983]
:   Mary Sheeran. μFP: An Algebraic VLS Design Language.
    Ph.D. thesis, PRG39, Oxford University Computing Laboratory, November 1983.
    <https://www.cs.ox.ac.uk/publications/publication3787-abstract.html>

[Sheeran1984]
:   Mary Sheeran. MuFP, a language for VLSI design.
    In *Proceedings of the 1984 ACM Symposium on LISP and functional programming (LFP '84)*.
    Association for Computing Machinery, New York, NY, USA, 1984, pp104–112.
    <https://doi.org/10.1145/800055.802026>

[Shultis1983]
:   Jon Shultis. A functional shell.
    In *Proceedings of the 1983 ACM SIGPLAN symposium on Programming language issues in software systems (SIGPLAN '83)*. Association for Computing Machinery, New York, NY, USA, 1983, pp202–211.
    <https://doi.org/10.1145/800226.806867>

[StanatWilliams1981]
:   Donald F. Stanat and E. Hollins Williams. 1981. Optimal associative searching on a cellular computer. In Proceedings of the 1981 conference on Functional programming languages and computer architecture (FPCA '81). Association for Computing Machinery, New York, NY, USA, 99–106. https://doi.org/10.1145/800223.806768

[Tolle1981]
:   Donald MacDavid Tolle. Implanting FFP trees in binary trees: An architectural proposal.
    In *Proceedings of the 1981 conference on Functional programming languages and computer architecture (FPCA '81)*. Association for Computing Machinery, New York, NY, USA, 1981, pp115–122.
    <https://doi.org/10.1145/800223.806770>

[SrinivasSangal1986]
:   Y. V. Srinivas and R. Sangal. A generalization of Backus' FP.
    In: Nori, K.V*. (eds) Foundations of Software Technology and Theoretical Computer Science. FSTTCS 1986.*
    Lecture Notes in Computer Science, vol 241. Springer, Berlin, Heidelberg, 1986. <https://doi.org/10.1007/3-540-17179-7_8>

[Sun1988]
:   Y. Sun. Verification of systolic array: An FP functional approach.
    *J. of Comput. Sci. & Technol*. 3, 81–101 (1988).
    <https://doi.org/10.1007/BF02943335>

[ThomasStanat1985]
:   T. A. Thomas and D. F. Stanat. An FP domain with infinite objects.
    In: Melton, A. (eds) *Mathematical Foundations of Programming Semantics. MFPS 1985*.
    Lecture Notes in Computer Science, vol 239. Springer, Berlin, Heidelberg, 1986.
    <https://doi.org/10.1007/3-540-16816-8_40>

[TsanakasEtAl1992]
:   Panayotis Tsanakas, George Papakonstantinou, Nikolaos Bilalis.
    Systematic synthesis of parallel VLSI architectures from FP specifications and its application to scene matching. *Microprocessing and Microprogramming*, Volume 35, Issues 1–5, 1992, pages 579-586.
    <https://doi.org/10.1016/0165-6074(92)90371-D>

[Valencia1986]
:   Andy Valencia. Stanford FP source code. 1986.

    * <https://sources.vsta.org/comp.sources.unix/volume13/funcproglang/>
    * <https://github.com/dbremner/fp>

[WeiGaudiot1988]
:   Y.-H. Wei and J.-L. Gaudiot. Demand-driven interpretation of FP programs on a data-flow multiprocessor.
    In *IEEE Transactions on Computers*, vol. 37, no. 8, pp. 946-966, Aug. 1988.
    <https://doi.org/10.1109/12.2246>

[ZhangEtAl1988]
:   Z. Zhang, K. M. George, and G. E. Hedrick. A data flow approach to the evaluation of FP programs.
    In *Proceedings of the 1988 ACM sixteenth annual conference on Computer science (CSC '88)*.
    Association for Computing Machinery, New York, NY, USA, 1988, pp586–592.
    <https://doi.org/10.1145/322609.323131>

Related resources
-----------------

\*\*\*\*\* <https://wiki.haskell.org/Pointfree>

\*\*\*\*\* pointfrip: Interpreter and Library for Pointfree Programming. <https://pointfree-interpreter.github.io>

\*\*\*\*\* https://groups.google.com/g/comp.lang.functional/c/TjgBE-dc63o/m/vIALTjplFfIJ  
Brian R. Murphy's response to a request for information about John Backus's FL

\*\*\*\*\* C. Michael Holloway .A Survey of Functional Programming Language Principles . NASA Technical Memorandum 89019, Langley Research Center, September 1986.
<https://ntrs.nasa.gov/api/citations/19870002073/downloads/19870002073.pdf>

See [[BeebeMcJones2026](#BeebeMcJones2026)].

\*\*\*\*\* Review <https://softwarepreservation.computerhistory.org/FORTRAN/Backus%20-%20LOC%20-%20catalogue%20of%20papers.pdf>

TO DO
-----

\*\*\*\*\* Add papers cited by Backus?
