---
id: 33
url: https://gwern.net/forking-path
title: 'Technology Forecasting: The Garden of Forking Paths · Gwern.net'
domain: gwern.net
source_date: '2026-01-07'
tags:
- academic-paper
- nonfiction-book
summary: Gwern argues that pessimistic technology forecasters make a critical error
  by assuming rigid, sequential paths to innovation and fixating on single obstacles
  to declare technologies impossible. In reality, most technological goals are "disjunctive"—meaning
  multiple alternative approaches exist, and success requires only one path to work
  while failure requires all paths to fail. By overlooking these alternative solutions
  and workarounds, critics suffer from functional fixedness and downward bias in probability
  estimates, as demonstrated by historical examples like the Manhattan Project and
  Edison's lightbulb experiments, where persistence through multiple methods ultimately
  succeeded despite individual failures.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Technology Forecasting: The Garden of Forking Paths · Gwern.net

[AI scaling](/doc/ai/scaling/index "Link to ai/scaling tag index"), [experience curve](/doc/economics/experience-curve/index "Link to economics/experience-curve tag index"), [forecasting](/doc/statistics/prediction/index "Link to statistics/prediction tag index")

Pessimistic forecasters are overconfident in fixating, hedgehog-like, on only *one* scenario for how they think something *must* happen; in reality, there are always many ways through the garden of forking paths, and something needs only one path to happen.

2014-06-01–5y2019-06-09
*finished*
[certainty](/about#confidence-tags "Explanation of 'confidence' metadata: probability of overall being meaningfully correct, expressed as Kesselman Estimative Words (ranging 0–100%: 'certain'/'highly likely'/'likely'/'possible'/'unlikely'/'highly unlikely'/'remote'/'impossible')"): *likely*
[importance](/about#importance-tags "Explanation of 'importance' metadata: rating 1–10 about how much a topic matters to the world."): *6*
[backlinks](#backlinks "Reverse citations/backlinks for this page (the list of other pages which link to this page).")
[similar](#similars "Similar links for this link (by text embedding).")
[bibliography](#link-bibliography "Bibliography of links cited in this page (forward citations).")

* [Functional Fixedness](#functional-fixedness)
* [Try, Try, Try Again](#try-try-try-again)
* [Forecasting Questions](#forecasting-questions)
* [External Links](#external-links)

> A classic cognitive bias in technological forecasting is [motivated-stopping](https://www.lesswrong.com/posts/L32LHWzy9FzSDazEg/motivated-stopping-and-motivated-continuation "Motivated Stopping and Motivated Continuation") and lack of imagination in considering possibilities for a [steelman](https://en.wikipedia.org/wiki/Straw_man#Steelmanning "Straw man § Steelmanning").
>
> Many people use a mental model of technologies in which they proceed in a serial sequential fashion and assume every step is necessary and only all together are they sufficient, and note that some particular step is difficult or unlikely to succeed and thus as a whole it will fail & never happen. But in reality, few steps are truly *required*.
>
> Progress is predictably unpredictable: A technology only needs to succeed in one way to succeed, and to fail it must fail in all ways. There may be many ways to work around, approximate, brute force, reduce the need for, or skip entirely a step, or redefine the problem to no longer involve that step at all. Examples of this include the parallel projects used by the Manhattan Project & Apollo program, which reasoned that despite the formidable difficulties in each path to the end goal, at least one would work out—and they did.
>
> In forecasting, to counter this bias, one should make a strong effort to imagine *all* possible alternatives which could be pursued in parallel, and remember that overall failure requires *all* of them to fail.

One of the most common errors in criticizing a technology or in forecasting future progress is to engage in overly rigid interpretation of what that technology is: ask “how can it fail” and not “how can it work”, to assume that it will be the same in 20 years as it is now, using the same components to achieve the same goals, and each component helplessly dependent on another component such that failure of one is failure of all. This then leads to pessimistic extrapolations and assumptions of imminent failure which will look comic in retrospect, as the current technology is merely a strawman of the true (but then unknown) technology. And too often a critic settles for finding a single way in which, if a technology were implemented or used in the dumbest way possible, that would be bad—as if that was the only way possible or if misuse were universally-inevitable—and declares the question settled.

An example is noting that a problem, say, protein-folding is difficult in some sense such as a computational complexity class, and declaring that it is impossible to solve well, and that in fact, AI is impossible in general, without asking about whether there is any way around the conditions for that specific technical statement—as [there so often are](/complexity "'Complexity no Bar to AI', Gwern 2014"). (One is reminded of the joke about a patient who goes to the doctor, assumes a yoga position, and complains, “doctor, it hurts when I do this!”, to which he replies, “don’t do that, then.”)

[Functional Fixedness](#functional-fixedness "Link to section: § 'Functional Fixedness'")
=========================================================================================

> In expressing full function, there are no fixed methods.
>
> [Ummon](https://en.wikipedia.org/wiki/Yunmen_Wenyan "Yunmen Wenyan")[1](#fn1)

The core mistake in this fallacy is reminiscent of the creativity tests which ask the subject to accomplish a task like making a candle holder from common objects like a box of soap and thumbtacks, or to come up with as many possible uses for a brick as possible; a subject who insists that a brick is a brick, and will not reimagine the box of soap as an open box which could be mounted on the wall, will never solve the tasks well, will be surprised when others accomplish it easily, and perhaps feel deep down that the others cheated (even if it worked perfectly well).

Defining a system, one might treat it as a “conjunctive” system where everything has to work: D depends on C1, C1 depends on B1, and B1 depends on A1; so if any problem is found is A1, B1, or C1, the entire system can be treated as debunked and an impossible contraption. It suffices to show that probably A1~, so probably ~D too. The problem with this way of thinking is that it may be adequate for immediate criticism of a specific system and a useful approach for engineering it, but it is *not* the same thing as answering whether D will be accomplished in 10 years or if the system is a good idea! Because such a criticism can be fixed by using a different A2, or perhaps A3, or A4, or A5, or A6, or maybe not even needing something like A at all and switching to a different system {D, X1, Y1, Z1}. And omitting any of these scenarios by considering only a subset will lead to [downwards bias in total probability](/doc/statistics/prediction/2022-karmarkar.pdf "‘The unlikelihood effect: When knowing more creates the perception of less’, Karmarkar & Kupor 2022"). The critic asks “is there any way this system might not work?” and stops there; but the forecaster asks, “is there any system with a way that works?” and keeps going.

[Try, Try, Try Again](#try-try-try-again "Link to section: § 'Try, Try, Try Again'")
====================================================================================

> Gallant fellows, these soldiers; they always go for the thickest place in the fence.
>
> [Admiral De Robeck](https://en.wikipedia.org/wiki/John_de_Robeck "John de Robeck"), of the [Gallipoli landing](https://en.wikipedia.org/wiki/Landing_at_Cape_Helles "Landing at Cape Helles")[2](#fn2)

Most technology goals are “disjunctive” in the sense that “anything goes” as long as it accomplishes the final goal, and it doesn’t matter how many dead ends get tried. If one way ‘hurts’, “don’t do that, then” and find a different way. The critic needs to disprove *all* possible ways, and not just fall for the [curse of expertise](/doc/statistics/bias/2016-boudreau.pdf "'Looking Across and Looking Beyond the Knowledge Frontier: Intellectual Distance, Novelty, and Resource Allocation in Science', Boudreau et al 2016") in settling for using their expertise for the far easier (and far more useless) task of scattering around doubts about a handful of ways. To fly, it is not necessary to recreate a bird’s wing, only to find *some* way to fly—and there turn out to be many different propulsion methods which succeed at the task of flight but bear little resemblance to how a bird flies (hot air, lighter-than-air gases, jet engines, [ramjets](https://en.wikipedia.org/wiki/Ramjet "Ramjet"), rockets, [ground-effect](https://en.wikipedia.org/wiki/Ground-effect_vehicle "Ground-effect vehicle"), propellers, helicopters/[autogyros](https://en.wikipedia.org/wiki/Autogyro "Autogyro"), [rotor kites](https://en.wikipedia.org/wiki/Rotor_kite "Rotor kite")/[wings](https://en.wikipedia.org/wiki/Rotor_wing "Rotor wing")…). A critic of the Wright or Montgolfier brothers would have been perfectly correct in noting that their methods could not and would never lead to bird flight, and wrong if they had then tried to proclaim that human flight was impossible or centuries away. Similarly, the Manhattan Project and the Apollo Project had a specific technology goal, but the goal was disjunctive in that any of several methods of refining uranium or plutonium or going to the Moon could have achieved the goal, each had formidable technological & scientific obstacles and had critics predicting failure, but only one had to work out; with money no object, they pursued multiple methods in parallel, and at least one did work out. Similarly, Thomas Edison knew many people had failed to create a useful electric lightbulb before him, and failed to create one himself after trying out hundreds of variants; did this mean that an electric lightbulb would never be invented? No, it just meant that he had to keep trying filaments until he found one that worked, and that was all he needed. One might analogize R&D to computer hackers: both share a [security mindset](https://intelligence.org/2017/11/25/security-mindset-ordinary-paranoia/ "Security Mindset and Ordinary Paranoia") where they only need to find one way in past the defenses thrown up in their path by Nature or corporations; if the firewall can’t be penetrated, then try hacking their printer, inject a [weird machine](/turing-complete "'Surprisingly Turing-Complete', Gwern 2012") into their servers, or just try calling up the secretary, say you’re the CEO, and ask for the password!

There is rarely a need to be rigid about the exact method, as long as the result works; we are free to be flexible.

If virtual reality headsets require 4K resolution per eye to deliver satisfactory VR experiences but this is too hard for GPUs to render fast enough, does this prove VR is impossible, or does it simply mean we must get a little creative and explore alternative solutions like using “foveated rendering” to cheat and render only a fraction of the 4K? In 10 years, should you expect this to be an issue? No, because resolution & quality is a disjunctive problem, just like motion-sickness in VR before it, which was fixed by a combination of continuous resolution/optics/FPS/locomotion/controller-hand-tracking/software/game-design fixes; there is no component which can be proven to be unfixable and universal across all possible solutions. If vacuum tubes will, for good physics reasons, cease to be shrinkable soon, does that mean Moore’s law is doomed and computers will always be ENIAC-sized, or, is it a disjunctive problem where any computational substrate can work, and the sigmoid of vacuum tubes will be replaced by other sigmoids of transistors, maintaining Moore’s law into the modern era? (Indeed, any exponential growth may turn out on closer inspection to be a stack of sigmoid growths, where alternatives are regularly found in order to make further progress; a correct argument that a particular technology will soon top out still does not prove that the exponential growth will stop, which would require proving that *no* alternatives would be found after the current sigmoid.) If GOFAI expert systems turn out to not be great, are expert systems a conjunctive problem where they are the only possible way of approaching artificial intelligence, or can artificial intelligence be solved in many ways and progress continue? If Bitcoin transactions are only pseudonymous and cryptocurrency blockchains scale poorly, are those conjunctive or disjunctive problems? (The answer should be easy even if you do not follow all the proposals for improvements like SegWit/Mimblewimble/sharding/MAST/scriptless scripts/Schnorr etc.) If genetic studies like GWASes are only able to explain a small percentage of measured individual differences at a particular time, does that prove GWASes are a failed methodology and that genetics in general is unimportant, or should we note that data will continue piling up and that there are [a dozen ways](/embryo-selection#polygenic-scores) in which GWASes are inefficient & we expect the growth in predictive power to continue? [How many different sensors](https://ideas.4brad.com/all-about-sensors-advanced-radar-and-more-future-perception "All about sensors: Advanced radar and more for the future of perception") could self-driving cars draw on to achieve human-level safety? etc. A similar observation holds for impossibility proofs and no-go theorems.[3](#fn3)

Often, these arguments seem impressive but in practice, people continue to do the impossible or go where they shouldn’t; why?

The proofs may be entirely correct, but as with any proof’s assumptions and theorem, the devil is in the details: perhaps the assumptions are not plausible in the first place, or the theorem doesn’t mean what you thought it meant. It might be impossible to create an algorithm with 100% accuracy, but the errors occur only on inputs that never occur, or the result is an approximation which is however indistinguishable from an exact answer for all intents & purposes or is less likely to be wrong than one’s computer or brain to be hit by a cosmic ray or stroke while thinking it through. And so on. A relevant example of this phenomenon comes up in discussing AI risk: one type of argument that AIs *cannot* ever be dangerous and AI risk is not real relies on an argument from worst-case algorithmic complexity, observing that many important problems like 3SAT are NP-hard, where the required computation quickly increases to infeasible levels, so humans and AIs must be equivalently intelligent, therefor AIs cannot be dangerous (see above); unfortunately, every premise is vulnerable—worst-case is often irrelevant, the ignored constant factors can be critical, small differences in intelligence/capability can have large compounding effects particularly in competitions, problems can be rearranged to bypass or make them easier, extremely large amounts of computation can be thrown at problems, AIs could have many advantages like immortality which are simply orthogonal to computational complexity, etc. There is nothing wrong with the proofs of what complexity class 3SAT is in, it’s just that what is proven is not necessary to the argument and what is necessary to the argument is not proven.

When is it valid to argue from a conjunctive perspective?

Sometimes, it is possible to come up with a universal proof like one based on laws of physics; if a goal turns out to be thermodynamically or information-theoretically impossible, that’s a good hint that no one is going to achieve it. So for the much-debated possibility of cryonics, a valid disproof would be to demonstrate that all the relevant information in the human brain is lost or destroyed within minutes/hours of death; an invalid conjunctive disproof would be to set up a chain of probabilities like “10% chance you die in a hospital, 10% chance you are vitrified within a few hours, 10% chance ALCOR doesn’t go bankrupt, 10% chance your body can be regrown healthily… thus, there’s ~0% chance it’ll work”, because each step is not really conjunctive but disjunctive (one can die elsewhere, the time window is not known, a cryonics organization bankruptcy ≠ rethawing, growing bodies is not the only possible good outcome, etc.).

Other times a technology may be inherently bottlenecked at a step all of which possible implementations are very difficult and it becomes quasi-conjunctive, versus a competing paradigm which is disjunctive. An example there is iterated embryo selection (IES) vs genome synthesis for creating ultra-highly-optimized human genomes: iterated embryo selection requires close control over converting stem cells to gametes and back in order to exert selection pressure over many ‘generations’ to optimize for particular traits, and given the trickiness of coaxing cells into regressing to stem cells and developing into particular cell types, there is probably only one effective procedure and no real alternatives; but ‘genome synthesis’ is simply the idea of synthesizing an entire human genome from scratch to a pre-specified optimally-designed genome, and, like the many competing techniques in genome sequencing, there are many different methods of combining nucleotides to build up a custom genome, which contribute to the (yes, exponential) fall in genome synthesis costs, and many further methods proposed (like specialized yeast) to reduce costs even further to the point where human genomes can be synthesized for a few million dollars each (and then reused arbitrarily often). IES is strongly conjunctive: if the stem cell steps can’t be solved, the entire cycle falls apart; genome synthesis is disjunctive: any of several methods can be used to synthesize nucleotides, and many more can be tried. Which one can we expect first? IES has a considerable headstart but genome synthesis progresses like a metronome because if it gets blocked on one track, it can hop to another; so my money is on genome synthesis at the moment.

[Forecasting Questions](#forecasting-questions "Link to section: § 'Forecasting Questions'")
============================================================================================

So in forecasting something like GWASes, Bitcoin, or VR, here are some useful questions to ask:

1. Are there any hard constraints from powerful theories like thermodynamics, evolution, or economics bounding the system as a whole?
2. Breaking down by functionality, how many different ways are there to implement each logical component? Is any step a serious bottleneck with no apparent way to circumvent, redefine, or solve with brute force?
3. Do its past improvements describe any linear or exponential trend? What happens if you extrapolate it 20 years (in the grand scheme of things, a minor error of timing)? If the trend is exponential, is it a set of stacked sigmoids indicating considerable flexibility in choice of technology/method?
4. What [experience curves](https://en.wikipedia.org/wiki/Experience_curve_effects "Experience curve effects") could this benefit from in each of its components and as a whole? If the cost decreases 5% for every doubling of cumulative production, what happens and how much demand do the price drops induce? Are any of the inputs cumulative, like dataset size (eg. number of genomes sequenced to date)?
5. Does it benefit from various forms of Moore’s laws for CPUs, RAM, HDD, or GPU FLOPs? Can fixed-cost hardware or humans be replaced by software, Internet, or statistics? Is any part parallelizable?
6. What caliber of intellect has been applied to optimization? What amount of ‘constant factor’ slack is left in the system to be micro-optimized away?

[External Links](#external-links "Link to section: § 'External Links'")
=======================================================================

* [“The Frontier of Scientific Plausibility”](/doc/www/www.macroscience.org/a510032f97efcf1eaa298f61f8a4f75e3201ad08.html), Tim Hwang 2023
* [“Defenders think in lists. Attackers think in graphs. As long as this is true, attackers win.”](https://github.com/JohnLaTwC/Shared/blob/master/Defenders%20think%20in%20lists.%20Attackers%20think%20in%20graphs.%20As%20long%20as%20this%20is%20true%2C%20attackers%20win.md "'Defenders think in lists. Attackers think in graphs. As long as this is true, attackers win.', Lambert 2015")

---

1. As quoted by [Dōgen](https://en.wikipedia.org/wiki/D%C5%8Dgen "Dōgen") in [“Who is Arguing about the Cat? Moral Action and Enlightenment according to Dōgen”](/doc/philosophy/ethics/1997-mikkelson.pdf "'Who Is Arguing About the Cat? Moral Action and Enlightenment According to Dōgen', Mikkelson 1997"), Mikkelson 199729ya.[↩︎](#fnref1)
2. Spoken to [Sir Roger Keyes](https://en.wikipedia.org/wiki/Roger_Keyes,_First_Baron_Keyes "Roger Keyes, First Baron Keyes"); recorded pg296 of [*The Naval Memoirs 1910–51915111ya*](https://archive.org/details/in.ernet.dli.2015.176420/page/n317 "The Naval Memoirs 1910–1915 : Sir Roger Keyes"), Keyes 193492ya.[↩︎](#fnref2)
3. For some reason, a lot of people are absolutely convinced that the Halting Theorem or Gödelian incompleteness do things like prove that creating any artificial intelligence is impossible in principle. (They do no such thing, any more than they prove the impossibility of, say, typecheckers, or [supersized machines](/doc/www/arxiv.org/69d5ddfbc1da2c2cd512dc63528fcde280203050.pdf "'On the Impossibility of Supersized Machines', Garfinkel et al 2017"), or their own existence.)[↩︎](#fnref3)

[Backlinks](#backlinks-section "Link to section: § 'Backlinks'")
================================================================

[[Backlinks (what links here)]](/metadata/annotation/backlink/%252Fforking-path.html "Reverse citations/backlinks for this page (the list of other pages which link to this page).")

[Similar Links](#similars-section "Link to section: § 'Similar Links'")
=======================================================================

[[Similar links by topic]](/metadata/annotation/similar/%252Fforking-path.html "Similar links for this link (by text embedding). Lazily-transcluded version at footer of page for easier scrolling.")

[Bibliography](#link-bibliography-section "Link to section: § 'Bibliography'")
==============================================================================

[[Bibliography of links/references used in page]](/metadata/annotation/link-bibliography/%252Fforking-path.html "Bibliography of links cited in this page (forward citations). Lazily-transcluded version at footer of page for easier scrolling.")
