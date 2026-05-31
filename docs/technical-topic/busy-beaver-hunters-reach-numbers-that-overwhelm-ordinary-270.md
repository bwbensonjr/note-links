---
id: 270
url: https://www.quantamagazine.org/busy-beaver-hunters-reach-numbers-that-overwhelm-ordinary-math-20250822/
title: Busy Beaver Hunters Reach Numbers That Overwhelm Ordinary Math | Quanta Magazine
domain: www.quantamagazine.org
source_date: '2025-08-25'
tags:
- academic-paper
- compilers
summary: Researchers hunting for "busy beaver numbers"—which measure the longest-running
  simple computer programs with a given number of rules—have discovered that the sixth
  busy beaver number (BB(6)) is incomprehensibly larger than previously thought. The
  number is so vast that it would be physically impossible to write it down even if
  you carved a digit into every atom in the universe. This breakthrough comes from
  the Busy Beaver Challenge, an online community of amateur and professional mathematicians,
  and reveals just how quickly the complexity of computational problems escalates
  as parameters increase.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Busy Beaver Hunters Reach Numbers That Overwhelm Ordinary Math | Quanta Magazine

[Home](/)

Busy Beaver Hunters Reach Numbers That Overwhelm Ordinary Math

[Comment](https://www.quantamagazine.org/busy-beaver-hunters-reach-numbers-that-overwhelm-ordinary-math-20250822/#comments)

Save Article 

Read Later

###### Share



[Facebook](http://www.facebook.com/sharer.php?u=https://www.quantamagazine.org/busy-beaver-hunters-reach-numbers-that-overwhelm-ordinary-math-20250822/)

Copied!

Copy link
[Email](/cdn-cgi/l/email-protection#457a3630272f202631780730363c6e0720243320376e0d302b312037366e172024262d6e0b3028272037366e112d24316e0a332037322d2029286e0a37212c2b24373c6e0824312d63272a213c78112d2065343020363165312a65232c2b2165312d2065292a2b222036316837302b2b2c2b2265362c2835292065262a2835303120376535372a22372428652d2436652c21202b312c232c20216524652b203265262d2428352c2a2b6b650c31a7c5dc3665352d3c362c262429293c652c28352a36362c27292065312a6532372c3120652a303165312d20652b302827203736652c2b332a293320216530362c2b22653631242b21243721652824312d202824312c262429652b2a3124312c2a2b6b65192b192b2d313135367f6a6a3232326b3430242b3124282422243f2c2b206b2a37226a2730363c68272024332037682d302b3120373668372024262d682b30282720373668312d2431682a332037322d202928682a37212c2b24373c682824312d6877757770757d77776a)

[Pocket](https://getpocket.com/save?url=https://www.quantamagazine.org/busy-beaver-hunters-reach-numbers-that-overwhelm-ordinary-math-20250822/&title=Busy+Beaver+Hunters+Reach+Numbers+That+Overwhelm+Ordinary+Math)
[Reddit](https://www.reddit.com/submit?url=https://www.quantamagazine.org/busy-beaver-hunters-reach-numbers-that-overwhelm-ordinary-math-20250822/)
[Ycombinator](https://news.ycombinator.com/submitlink?u=https://www.quantamagazine.org/busy-beaver-hunters-reach-numbers-that-overwhelm-ordinary-math-20250822/&t=Busy+Beaver+Hunters+Reach+Numbers+That+Overwhelm+Ordinary+Math)

* [Comment

  Comments](#comments)
* Save Article

  Read Later

  Read Later

[Turing machines](/tag/turing-machines/)

Busy Beaver Hunters Reach Numbers That Overwhelm Ordinary Math
==============================================================

*By* 
[Ben Brubaker](https://www.quantamagazine.org/authors/brubaker_ben/)

*August 22, 2025*

The quest to find the longest-running simple computer program has identified a new champion. It’s physically impossible to write out the numbers involved using standard mathematical notation.

[Comment](#comments)

Save Article 

Read Later

![A beaver traveling on a mountain path lined with 0s and 1s, stretching up to the sky](https://www.quantamagazine.org/wp-content/uploads/2025/08/BusyBeaver6Update-crKristinaArmitage-Lede-scaled.webp)

Kristina Armitage/*Quanta Magazine*

Introduction
------------

Imagine that someone gives you a list of five numbers: 1, 6, 21, 107 and — wait for it — 47,176,870. Can you guess what comes next?

If you’re stumped, you’re not alone. These are the first five busy beaver numbers. They form a sequence that’s intimately tied to one of the most notoriously difficult questions in theoretical computer science. Determining the values of busy beaver numbers is a daunting challenge that has attracted a cult following among both professional and amateur mathematicians for over 60 years.

Researchers identified the first four busy beaver numbers in the 1960s and 1970s. The conspicuously larger fifth number, called BB(5), was only [definitively pinned down last year](https://www.quantamagazine.org/amateur-mathematicians-find-fifth-busy-beaver-turing-machine-20240702/), by a team made up mostly of amateur mathematicians working together in an online community called the [Busy Beaver Challenge](https://bbchallenge.org/).

No one knows how big BB(6) is. All we have are lower limits — truly staggering ones. In 2022 busy beaver hunters established that BB(6) must be, at a minimum, so large that it’s literally impossible to write down in ordinary decimal notation. Even if you somehow carved a digit into every atom in the cosmos, you’d run out of atoms before making any measurable progress.

“It’s way beyond anything that we could ever grasp or get our hands on,” said [Scott Aaronson](https://www.cs.utexas.edu/people/faculty-researchers/scott-aaronson), a computer scientist at the University of Texas, Austin.

Busy beaver hunters have [now discovered](https://wiki.bbchallenge.org/wiki/TMBR:_July_2025) that this stupefyingly big number must be even bigger. The finding comes from one of the most mysterious and prolific contributors to the Busy Beaver Challenge, who proved a new lower limit on BB(6) in June and broke the record again a mere nine days later. The new results make the 2022 lower bound look positively puny.

“I keep on being surprised,” said [William Gasarch](https://www.cs.umd.edu/people/gasarch), a computer scientist at the University of Maryland. “Six is getting us into the stratosphere of large numbers.”

**Beaver Trap**
---------------

The notoriously difficult question behind the busy beaver numbers is this: Given the code of a computer program, can you tell whether it will eventually stop or run forever?

In 1936, the pioneering logician Alan Turing proved that there’s no universal procedure for answering this question, which became known as the halting problem. Any method that works for some programs will fail for others, and in some cases, no method will work.

Turing proved this seminal result by inventing a formal mathematical model of computation in which programs are represented by hypothetical devices now called [Turing machines](https://www.quantamagazine.org/alan-turings-most-important-machine-was-never-built-20230503/). Each Turing machine performs computations in discrete steps according to a unique list of simple rules. The more rules a Turing machine has, the more complex its behavior can get, and the harder it can be to determine whether it will halt.

![A graphic explaining how turing machines work](https://www.quantamagazine.org/wp-content/uploads/2025/08/HowTuringMachinesWork-cr.KristinaArmitage-Mobile.V2.svg)![A graphic explaining how turing machines work](https://www.quantamagazine.org/wp-content/uploads/2025/08/HowTuringMachinesWork-cr.KristinaArmitage-Desktop.V2.svg)

Kristina Armitage/*Quanta Magazine*

But just how much harder? In 1962, the mathematician Tibor Radó invented a new way to explore this question through what he called [the busy beaver game](https://onlinelibrary.wiley.com/doi/abs/10.1002/j.1538-7305.1962.tb00480.x). To play, start by choosing a specific number of rules — call that number *n*. Your goal is to find the *n*-rule Turing machine that runs the longest before eventually halting. This machine is called the busy beaver, and the corresponding busy beaver number, BB(*n*), is the number of steps that it takes.

In principle, if you want to find the busy beaver for any given *n*, you just need to do a few things. First, list out all the possible *n*-rule Turing machines. Next, use a computer program to simulate running each machine. Look for telltale signs that machines will never halt — for example, many machines will fall into infinite repeating loops. Discard all these non-halting machines. Finally, record how many steps every other machine took before halting. The one with the longest runtime is your busy beaver.

In practice, this gets tricky. For starters, the number of possible machines grows rapidly with each new rule. Analyzing them all individually would be hopeless, so you’ll need to write a custom computer program to classify and discard machines. Some machines are easy to classify: They either halt quickly or fall into easily identifiable infinite loops. But others run for a long time without displaying any obvious pattern. For these machines, the halting problem deserves its fearsome reputation.

The more rules you add, the more computing power you need. But brute force isn’t enough. Some machines run for so long before halting that simulating them step by step is impossible. You need clever mathematical tricks to measure their runtimes.

“Technology improvements definitely help,” said [Shawn Ligocki](https://www.sligocki.com/about/), a software engineer and longtime busy beaver hunter. “But they only help so far.”

**End of an Era**
-----------------

Busy beaver hunters started chipping away at the BB(6) problem in earnest in the 1990s and 2000s, during an impasse in the BB(5) hunt. Among them were Shawn Ligocki and his father, Terry, an applied mathematician who ran their search program in the off hours on powerful computers at Lawrence Berkeley National Laboratory. In 2007, they found a six-rule Turing machine that broke the record for the longest runtime: The number of steps it took before halting had nearly 3,000 digits. That’s a colossal number by any ordinary measure. But it’s not too big to write down. In 12-point font, those 3,000 digits will just about cover a single sheet of paper.

Three years later, a Slovakian undergraduate computer science student named Pavel Kropitz decided to tackle the BB(6) hunt as a senior thesis project. He wrote his own search program and set it up to run in the background on a network of 30 computers in a university lab. After a month he found a machine that ran far longer than the one discovered by the Ligockis — a new “champion,” in the lingo of busy beaver hunters.

“I was lucky, because people in the lab were already complaining about my CPU usage and I had to scale back a bit,” Kropitz wrote in a direct message exchange on the [Busy Beaver Challenge Discord server](https://discord.com/invite/3uqtPJA9Uv). After another month of searching, he broke his own record with a machine whose runtime had over 30,000 digits — enough to fill about 10 pages.

Kropitz’s machine held the BB(6) record for 12 years. Then, in May 2022, Shawn Ligocki started a new job where he had access to a powerful computer cluster, and he decided to try running his old code on newer hardware. Sure enough, he found a new champion that beat Kropitz’s record. The discovery kicked off a flurry of activity. Twice in the span of two weeks, Ligocki announced a [new](https://groups.google.com/g/busy-beaver-discuss/c/iRHDmAQ5jr8) [champion](https://groups.google.com/g/busy-beaver-discuss/c/-zjeW6y8ER4) on a busy beaver mailing list. Each time, Kropitz beat his record within three days. Ligocki remembers his father marveling at how Kropitz pulled it off.

“He was joking that he imagines Pavel has already solved BB(6),” Ligocki said. “Whenever we find a champion, he just goes and pulls out of his bag one that’s a little bit bigger.”

But the last two machines that Ligocki and Kropitz discovered didn’t run just a bit longer than the reigning champion — their runtimes were on an entirely new level.

To understand numbers this large, we need to go back to the familiar mathematics of addition and multiplication. Start by adding up *n* copies of a number — that’s just the definition of multiplication by *n*. If you instead multiply *n* copies of a number, that’s known as exponentiation. So what happens if you repeatedly exponentiate a number? That process defines a new operation called tetration, denoted by two arrows pointing up.

Tetration gets big fast. $latex 10 \uparrow\uparrow 1$ is just 10. But $latex 10 \uparrow\uparrow 2$ is 1010, or 10 billion, and $latex 10 \uparrow\uparrow 3$ is 10 raised to the 10-billionth power: a 1 followed by 10 billion zeros. To write out all the digits you’d need a stack of paper a thousand feet high. At $latex 10 \uparrow\uparrow 4$, you cross a symbolic threshold where it’s no longer a matter of finding enough paper — there are far more digits than atoms in the universe.

![A graphic depicting how large number are notated](https://www.quantamagazine.org/wp-content/uploads/2025/08/LargeNumberLadder-cr.SamuelVelasco-Mobile.svg)![A graphic depicting how large number are notated](https://www.quantamagazine.org/wp-content/uploads/2025/08/LargeNumberLadder-cr.SamuelVelasco-Desktop.svg)

Samuel Velasco/*Quanta Magazine*

When Ligocki beat Kropitz’s record for the second time, it was with a six-rule Turing machine that ran for over $latex 10 \uparrow\uparrow 5$ steps before halting. Kropitz countered with a machine that ran for $latex 10 \uparrow\uparrow 15$ steps — that’s a tower of tens 15 stories high. They’d left the familiar world of digits far behind.

“That was the end of an era,” Kropitz wrote over direct message.

It was also the end of an era in another respect. Until then, the busy beaver game had been a competition, and researchers mostly worked alone. Then the Busy Beaver Challenge was formed, ushering in a new age of collaboration.

**A New Class of Crazy**
------------------------

The Busy Beaver Challenge was founded in 2022 by a computer science graduate student named [Tristan Stérin](https://tristan.st) with the express purpose of rigorously proving the true value of BB(5). In summer 2024 the group succeeded, with a key contribution from a mysterious newcomer known only by the pseudonym mxdys.

News of the result [appeared in *Quanta*](https://www.quantamagazine.org/amateur-mathematicians-find-fifth-busy-beaver-turing-machine-20240702/), where [Katelyn Doucette](https://katelyndoucette.com/), an undergraduate computer science student at Virginia Tech, happened to see it. She soon joined the Busy Beaver Challenge community, at first just dropping in to the Discord server from time to time. But in May she made an exciting discovery, and since then she’s become one of the most active contributors to the BB(6) hunt. “I’ve just been kind of hooked,” she said. “It’s such a beautiful set of problems.”

In the year since putting the finishing touches on the BB(5) proof, mxdys had steadily chipped away at the BB(6) problem, using sophisticated automated methods to classify all but a few thousand “holdout” machines. Doucette was rooting around in the list of holdouts when she found [one that looked especially promising](https://wiki.bbchallenge.org/wiki/1RB0LF_1RC1RB_1LD0RA_1LB0LE_1RZ0LC_1LA1LF). Analyzing it further with some help from Shawn Ligocki, she discovered that its runtime was second only to that of Kropitz’s reigning champion. What’s more, Doucette’s machine belonged to a class of machines known as [shift overflow counters](https://www.sligocki.com/2023/02/05/shift-overflow.html), which achieve long runtimes using a very different mechanism than Kropitz’s champion.

“It’s exciting to see that these busy beavers have found a new technology,” Ligocki said.

A few other busy beaver hunters had [previously](https://wiki.bbchallenge.org/wiki/1RB3LA4RB0RB2LA_1LB2LA3LA1RA1RZ) [discovered](https://wiki.bbchallenge.org/wiki/1RB1RC_1LC1RE_1LD0LB_1RE1LC_1LE0RF_1RZ1RA) shift overflow counters that halted after a long time, but Doucette’s discovery made the team suspect that these machines were more plentiful than they’d realized. And if some of the first ones to be studied had come within striking distance of Kropitz’s record, others would likely surpass it. Busy Beaver Challenge contributors rushed to analyze other shift overflow counters, but mxdys got there first. On June 16, they announced the discovery of [a new champion](https://wiki.bbchallenge.org/wiki/1RB1LC_1LA1RE_0RD0LA_1RZ1LB_1LD0RF_0RD1RB) that halted after $latex 10 \uparrow\uparrow 10^7$ steps— that is, its runtime is a tower of tens that’s 10 million stories high. Writing this number down as a string of digits is out of the question. But even writing it as a tower of powers gets dicey: In 12-point font, that line of tens would stretch out for about 25 miles.

Kropitz, who saw the news while away on vacation, accepted the loss of his title graciously, writing in the Discord server, “unfortunately, i won’t be performing my 3-day trick this time.” It helped that he had a consolation prize. A month earlier, he’d nabbed the record for the longest-running known seven-rule Turing machine. At least for now, Kropitz is still on the leaderboard.

**Beyond the Biggest**
----------------------

The new record didn’t last long. A week later, mxdys [broke it again](https://wiki.bbchallenge.org/wiki/1RB1RA_1RC1RZ_1LD0RF_1RA0LE_0LD1RC_1RA0RE) with a machine whose runtime is — yet again — on a qualitatively new level. To write it down in its most succinct form, we need to introduce an absurd mathematical operation called pentation, represented by three arrows pointing up. Pentation is repeated tetration — in other words, it bears the same relationship to tetration as tetration does to exponentiation.

The total number of steps that mxdys’ new champion took before halting was greater than $latex 2 \uparrow\uparrow\uparrow 5$, or $latex 2 \uparrow\uparrow (2\uparrow\uparrow(2\uparrow\uparrow(2\uparrow\uparrow2)))$. To unpack this expression, you work outward from the innermost parentheses: $latex 2 \uparrow\uparrow 2$ is 4, and $latex 2 \uparrow\uparrow 4$ is a bit over 65,000. That leaves you with $latex 2 \uparrow\uparrow (2\uparrow\uparrow65,000)$, making the height of the final stack of 2s an incomprehensibly large number. Forget about writing a tower of powers that stretches out for miles or megaparsecs. Even this more compact notation no longer fits in the universe.

![A graphic depicting the six rules a recently discovered turing machine follows](https://www.quantamagazine.org/wp-content/uploads/2025/08/ANewChampion-cr.KristinaArmitage-Mobile.svg)![A graphic depicting the six rules a recently discovered turing machine follows](https://www.quantamagazine.org/wp-content/uploads/2025/08/ANewChampion-cr.KristinaArmitage-Desktop.svg)

Kristina Armitage/*Quanta Magazine*

This new result is still just a lower limit on BB(6) — the true value could be even higher. Busy beaver hunters don’t expect to have a definitive answer anytime soon. The first sign of trouble was a monstrous six-rule Turing machine that the team has named [Antihydra](https://bbchallenge.org/antihydra), discovered by mxdys last year.

Antihydra almost certainly never halts. But researchers haven’t been able to prove it. And there’s a good reason for that: A busy beaver hunter who goes by Racheline has shown that the question of whether Antihydra halts is closely related to a famous unsolved problem in mathematics called the [Collatz conjecture](https://www.quantamagazine.org/mathematician-proves-huge-result-on-dangerous-problem-20191211/). Since then, the team has discovered many other six-rule machines with similar characteristics. Slaying the Antihydra and its brethren will require conceptual breakthroughs in pure mathematics.

But to avid busy beaver hunters, that’s no reason to be discouraged. There are still thousands of six-rule Turing machines to explore, each with its own rich behavior.

“For me, the most valid reason to do math is because it’s fun. It is art,” Racheline wrote in a Discord direct message. “There will always be something new to do.”

The Quanta Newsletter

*Get highlights of the most important news delivered to your email inbox*

[Recent newsletters](http://us1.campaign-archive2.com/home/?u=0d6ddf7dc1a0b7297c8e06618&id=f0cb61321c)

Also in Computer Science
------------------------

[Key Chemistry Question Answered, No Quantum Computer Required

![](https://www.quantamagazine.org/wp-content/uploads/2026/05/Chem-Quantum-Advantage-cr-Nash-Weerasekera-Default.webp)](https://www.quantamagazine.org/key-chemistry-question-answered-no-quantum-computer-required-20260529/)

[chemistry](/tag/chemistry/)

[### Key Chemistry Question Answered, No Quantum Computer Required](https://www.quantamagazine.org/key-chemistry-question-answered-no-quantum-computer-required-20260529/)

*By* 
[Kevin Hartnett](https://www.quantamagazine.org/authors/kevin-hartnett/)

May 29, 2026

[Comment](https://www.quantamagazine.org/key-chemistry-question-answered-no-quantum-computer-required-20260529/#comments)

Save Article 

Read Later

[How Unknowable Math Can Help Hide Secrets

![](https://www.quantamagazine.org/wp-content/uploads/2026/05/GodelCryptography-crKristinaArmitage-Default.jpg)](https://www.quantamagazine.org/how-unknowable-math-can-help-hide-secrets-20260511/)

[cryptography](/tag/cryptography/)

[### How Unknowable Math Can Help Hide Secrets](https://www.quantamagazine.org/how-unknowable-math-can-help-hide-secrets-20260511/)

*By* 
[Ben Brubaker](https://www.quantamagazine.org/authors/brubaker_ben/)

May 11, 2026

[Comment](https://www.quantamagazine.org/how-unknowable-math-can-help-hide-secrets-20260511/#comments)

Save Article 

Read Later

[The AI Revolution in Math Has Arrived

![](https://www.quantamagazine.org/wp-content/uploads/2026/04/Math-AI-Update-cr-Nash-Weerasekera-Default.webp)](https://www.quantamagazine.org/the-ai-revolution-in-math-has-arrived-20260413/)

[foundations of mathematics](/tag/foundations-of-mathematics/)

[### The AI Revolution in Math Has Arrived](https://www.quantamagazine.org/the-ai-revolution-in-math-has-arrived-20260413/)

*By* 
[Konstantin Kakaes](https://www.quantamagazine.org/authors/konstantin-kakaes/)

April 13, 2026

[Comment](https://www.quantamagazine.org/the-ai-revolution-in-math-has-arrived-20260413/#comments)

Save Article 

Read Later

Comment on this article
-----------------------

*Quanta Magazine moderates comments to facilitate an informed, substantive, civil conversation. Abusive, profane, self-promotional, misleading, incoherent or off-topic comments will be rejected. Moderators are staffed during regular business hours (New York time) and can only accept comments written in English.*

Show comments

![Two cranes symmetrically poised with their beaks together below a full moon](https://www.quantamagazine.org/wp-content/uploads/2025/08/JOW-Ep12-HP-NO-LOGO-1720x728.webp)

Next article
------------

Do Beautiful Birds Have an Evolutionary Advantage?
