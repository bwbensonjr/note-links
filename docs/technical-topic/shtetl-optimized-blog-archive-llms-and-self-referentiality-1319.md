---
id: 1319
url: https://scottaaronson.blog/?p=10046
title: Shtetl-Optimized  » Blog Archive   » LLMs and self-referentiality
domain: scottaaronson.blog
source_date: '2026-09-03'
tags:
- llm
- ai
- academic-paper
summary: Scott Aaronson argues that self-referentiality and "strange loops," once
  considered central to achieving artificial intelligence by thinkers like Douglas
  Hofstadter, were ultimately unnecessary for building powerful language models like
  GPT and Fable. These models developed sophisticated abilities to discuss themselves
  and complex topics as emergent byproducts of general prediction and compression
  training, rather than through explicit self-referential programming, suggesting
  that the classical theory overestimated self-reference's importance to intelligence.
  While consciousness and subjective experience remain mysterious, the notion that
  explicit self-referentiality is required for conversational intelligence should
  be abandoned as a disproven historical idea.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Shtetl-Optimized  » Blog Archive   » LLMs and self-referentiality

[LLMs and self-referentiality](https://scottaaronson.blog/?p=10046 "Permanent Link: LLMs and self-referentiality")
------------------------------------------------------------------------------------------------------------------

I woke up yesterday with the following thoughts, which are probably either obvious or dumb.

A central thesis that many readers, including me, took from Douglas Hofstadter’s [Gödel Escher Bach](https://en.wikipedia.org/wiki/G%C3%B6del,_Escher,_Bach) when young was that the secret of intelligence (and therefore, of AI) was going to have a lot to do with self-referentiality and “strange loops.”

Even Roger Penrose’s [The Emperor’s New Mind](https://en.wikipedia.org/wiki/The_Emperor%27s_New_Mind), which in some ways was the anti-GEB, ironically agreed with GEB about the fundamental importance of self-reference to the success or failure of the whole AI project. It claimed (incorrectly, in my view and in most experts’) that AI could never work because there was something about Gödel’s Theorem and self-reference that no computer program could ever capture, but that could be captured by exotic physics accessible to the human brain.

Now, in 2026, we’ve succeeded at building AIs that outperform most humans at most intellectual tasks that are well-defined enough to judge. And at no point in the tech stack of those AIs — neither in the transformer neural nets, nor in the GPU clusters they run on, nor in the training process, nor anywhere else — did anyone need to build in anything about self-reference. (Excepting, eg, the system instructions that tell the model about its role and identity, which aren’t needed for intelligent behavior. Also, I’m not going to count the autoregressive nature of LLMs as “self-referential”; that’s just dynamical feedback.)

Of course, GPT 5.6 Pro and Fable can talk about themselves, about Gödel’s Theorem, about self-reference, about what we’re talking about right now, all of it, better than most humans. But at no point did anyone need to build self-referential abilities in. They popped out as a byproduct of the same pretraining that let the models talk about Pokémon and long-chain polymers and cognitive behavioral therapy and plate tectonics and everything else.

No wonder Hofstadter says he’s been stunned by the success of LLMs, and has seemed depressed about current AI capabilities in [essays like this one](https://www.theatlantic.com/ideas/archive/2023/07/the-terrible-downside-of-ai-language-translation/674687/). He’s way too smart to deny what’s happened or invent reasons why it doesn’t really count (the approach many have taken). But he realizes that we now have true conversational intelligence from a path that the GEB worldview would’ve regarded as far too cheap and simple, and that certainly has no “strange loops” built in anywhere.

Of course, a Hofstadterian could argue that a strange loop *emerges* in LLMs — indeed, nothing in GEB ever said that strange loops would need to be explicitly engineered at the outset. But would anyone who hadn’t been brought up on GEB arrive at this as a useful way of thinking about LLMs?

What can we say about this with hindsight? While the ideas of diagonalization and self-reference of course played a central role in the birth of modern mathematical logic and computer science, the most famous uses were *negative*: there is not a bijectjon between the natural numbers and the reals. There is not a complete sound proof system for arithmetic. There is not an algorithm to solve the halting problem.

If your goal was only to build the axioms of ZFC and the rules of first-order inference, or build an electronic computer, you wouldn’t explicitly need self-reference for that. You would just … start building, taking care that your instruction set didn’t fall short of universality.

Yes, ZFC can formalize and prove theorems about itself. Yes, electronic computers can run programs that take their own code as input. But no one ever needed to build those abilities in, any more than self-reference needed to be built in to the alphabet or the rules of grammar. It popped out as a free byproduct of universality.

In the same way, LLMs’ ability to talk about themselves popped out as a byproduct of their ability to talk about anything in the discourse universe they were trained on. The big, old ideas about intelligence that ended up basically vindicated were the ideas about how intelligence is about prediction, and prediction is about compression, and compression is about finding better and better upper bounds on Kolmogorov complexity. Not the self-reference stuff. (Although, if you wanted to know why Kolmogorov complexity *can’t* be computed perfectly, that negative statement would again require a self-referential argument.)

What’s left? Consciousness and subjective experience of course remain extremely mysterious. For all we know, Hofstadter could be right that those have something to do with self-reference. (For all we know, even Penrose could be right that they have something to do with exotic physics accessible to biological brains but not digital computers!)

But the idea that you’d need explicit self-referentiality before you could get convincing and world-changing conversational intelligence? Let it be buried in a Westminster Abbey or Arlington National Cemetery for the most important wrong ideas in human history — geocentrism, Aristotle’s teleological physics, aether, phlogiston, Freud’s psychology, Marx’s prediction of a workers’ uprising followed by a classless utopia, etc. But buried it needs to be.

[![Email, RSS](https://scottaaronson.blog/wp-content/plugins/really-simple-facebook-twitter-share-buttons/images/specificfeeds_follow.png "Email, RSS") Follow](http://www.specificfeeds.com/follow)

This entry was posted
on Tuesday, September 1st, 2026 at 12:17 pm and is filed under [Embarrassing Myself](https://scottaaronson.blog/?cat=18), [Metaphysical Spouting](https://scottaaronson.blog/?cat=12), [Procrastination](https://scottaaronson.blog/?cat=3).
You can follow any responses to this entry through the [RSS 2.0](https://scottaaronson.blog/?feed=rss2&p=10046) feed.
You can [leave a response](#respond), or [trackback](https://scottaaronson.blog/wp-trackback.php?p=10046) from your own site.
