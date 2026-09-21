---
id: 1366
url: https://www.amazon.science/blog/why-dont-machine-learning-research-agents-overfit
title: Why machine learning research agents don't overfit — and what compression has
  to do with it - Amazon Science
domain: www.amazon.science
source_date: '2026-09-14'
tags:
- ai
- llm
- academic-paper
- mathematics
summary: 'Machine learning research agents don''t overfit benchmarks despite repeated
  evaluation cycles because successful strategies are highly compressible—they can
  be encoded in very few bits or tokens. This compression principle, rooted in Occam''s
  razor, explains why models that capture genuine data structure rather than memorization
  can generalize well: a strategy too small to memorize training data must rely on
  real patterns instead. The research demonstrates that AI agents can reproduce strong
  performance from minimal descriptions, suggesting that effective ML strategies are
  inherently simple and transferable, which contrasts with the textbook prediction
  that iterative benchmark optimization should lead to overfitting.'
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Why machine learning research agents don't overfit — and what compression has to do with it - Amazon Science

![CompressionModels-03-16x9.png](https://cdn.amazon.science/dims4/default/1d3b996/2147483647/strip/true/crop/1920x1080+0+0/resize/1440x810!/quality/90/?url=https%3A%2F%2Famzn-science-production-science.s3.us-east-1.amazonaws.com%2Fscience%2F28%2F46%2F0121ba1e4b42be0c56e7560c9844%2Fcompressionmodels-03-16x9.png)

The more your listener already knows, the shorter the message you need to send. An expert ML engineer needs only a few sentences; a newcomer needs the whole manual.

[Machine learning](https://www.amazon.science/research-areas/machine-learning)

Why don’t machine learning research agents overfit?
===================================================

New research indicates that AI agents learn compressible models of data, which don’t have enough space to enable memorization.
------------------------------------------------------------------------------------------------------------------------------

By [Martin Bertran Lopez](https://www.amazon.science/author/martin-bertran-lopez), [Aaron Roth](https://www.amazon.science/author/aaron-roth)

September 10, 2026

11 min read

Share

Share

* Copy link
* [Email](mailto:?body=Why%20don%E2%80%99t%20machine%20learning%20research%20agents%20overfit%3F%0A%0Ahttps%3A%2F%2Fwww.amazon.science%2Fblog%2Fwhy-dont-machine-learning-research-agents-overfit%0A%0ANew%20research%20indicates%20that%20AI%20agents%20learn%20compressible%20models%20of%20data%2C%20which%20don%E2%80%99t%20have%20enough%20space%20to%20enable%20memorization.)
* [X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.amazon.science%2Fblog%2Fwhy-dont-machine-learning-research-agents-overfit&text=Why%20don%E2%80%99t%20machine%20learning%20research%20agents%20overfit%3F)
* [LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fwww.amazon.science%2Fblog%2Fwhy-dont-machine-learning-research-agents-overfit&mini=true&title=Why%20don%E2%80%99t%20machine%20learning%20research%20agents%20overfit%3F&summary=New%20research%20indicates%20that%20AI%20agents%20learn%20compressible%20models%20of%20data%2C%20which%20don%E2%80%99t%20have%20enough%20space%20to%20enable%20memorization.&source=Amazon%20Science)
* [Facebook](https://www.facebook.com/dialog/share?app_id=1024652704536162&display=popup&href=https%3A%2F%2Fwww.amazon.science%2Fblog%2Fwhy-dont-machine-learning-research-agents-overfit)
* [Line](https://social-plugins.line.me/lineit/share?url=https://www.amazon.science/blog/why-dont-machine-learning-research-agents-overfit)
* [Reddit](https://www.reddit.com/submit?url=https://www.amazon.science/blog/why-dont-machine-learning-research-agents-overfit&title=Why don’t machine learning research agents overfit?)
* [QZone](http://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?url=https://www.amazon.science/blog/why-dont-machine-learning-research-agents-overfit&title=Why don’t machine learning research agents overfit?&summary=New research indicates that AI agents learn compressible models of data, which don’t have enough space to enable memorization.)
* [Sina Weibo](https://service.weibo.com/share/share.php?url=https://www.amazon.science/blog/why-dont-machine-learning-research-agents-overfit)
* [WeChat](https://www.amazon.science/blog/why-dont-machine-learning-research-agents-overfit "Share on wechat")
* [WhatsApp](https://api.whatsapp.com/send?text=Why don’t machine learning research agents overfit?%20https://www.amazon.science/blog/why-dont-machine-learning-research-agents-overfit)

分享到微信

x

Key takeaways

* ML models don't overfit benchmarks, even after many rounds of iterative improvement. This contradicts textbook predictions that repeatedly evaluating against the same held-out data should lead to overfitting.
* Experiments with ML research agents indicate that successful strategies are highly compressible. When a successful agent's strategy is squeezed through an information bottleneck (as few as 16 tokens), a fresh agent with no memory can reproduce the original agent's performance, meaning the strategy captured real structure, not memorized data.
* Compression provides both an explanation and a diagnostic tool. Strategies that genuinely overfit fail the compression test: their validation-specific gains vanish when passed through the bottleneck.
* LLMs are powerful compression decoders. Because they carry vast world knowledge, they can reconstruct full ML pipelines from terse, expert-shorthand prompts, which is a concrete way of understanding why they're so capable.

Was this answer helpful?

Machine learning, at its core, is about generalization, not memorization. You hand your learning algorithm a pile of training examples and use them to fit a model. But the goal is not to perform well on the training examples — that's easy, you could just memorize the answers. The goal is to perform well on *new* examples that you have never before seen. If a model does well on the data it was trained on but poorly on fresh data, it hasn’t actually learned anything; you have only fooled yourself into thinking it has. This failure mode has a name: overfitting.

Anyone who has taken an introductory statistics or machine learning class knows the standard defense. You hold out some of your data and refuse to train on it. In practice, this held-out data plays two roles. A *validation set* is one you consult repeatedly while building the model — to compare candidates, tune hyperparameters, and decide what to try next. A final *test set* (or *holdout*) is meant to be touched only once, at the very end: because the training procedure never saw it, strong performance there is a correct proxy for the new examples you will encounter in the wild.

> Machine learning, at its core, is about generalization, not memorization

The “holdout” condition is crucial, though. The correct-proxy guarantee holds if the held-out set stays genuinely unseen. If you check your performance on it, tweak your training procedure in response, recheck, and iterate, chasing better and better numbers, that set is no longer unseen; it has become part of your training procedure. Do this enough times, and you can overfit it just as you might have overfit the training set, and you have lost your proxy for unseen data. This is true of any held-out set you reuse this way, including a validation set, which is reused by design.

A puzzle at the heart of machine learning
-----------------------------------------

Real machine learning research looks *exactly* like the iterative improvement loop we just described. Everyone gauges performance using a handful of benchmark datasets that go unrevised for years. The research community repeats an enormous, distributed loop: evaluate a model on the benchmark, revise the training procedure, re-evaluate, publish, and let the next group eke out a little more improvement.

This is precisely the kind of hill-climbing against a held-out set that, by the textbook account, ought to produce rampant overfitting. By now, the leaderboards should be saturated with models that look great on the benchmark and mediocre everywhere else.

And yet that is not what happens. Studies that build entirely fresh test sets for old, heavily reused benchmarks have found that improvements largely *transfer*: on the new data, models demonstrate the same gains they did on the old benchmark. Benchmark-driven machine learning, against the textbook's prediction, has produced rapid and largely *real* progress. Why?

There is no shortage of hypotheses, but they have been hard to test empirically, because the "subject" of the experiment is the entire human research community. You cannot reset a field, wipe its memory, and rerun the last decade under controlled conditions.

But we can do something similar. We now have capable, LLM-based research agents that can autonomously run the same machine-learning optimization loops that human communities run. They engage in the same benchmark hill-climbing — and, intriguingly, they too seem not to overfit. The difference is that an agent, unlike a research community, is something you *can* reset. You can clear its memory, control exactly what information it sees, and run the experiment again. In a recent paper, "[What fits (into few tokens) doesn't overfit: Compression and generalization in ML research agents](https://arxiv.org/abs/2606.11045)", we do exactly that — and in the process offer a concrete explanation for the long-standing mystery.

Occam's razor, made precise
---------------------------

The explanation begins with a very old idea. Occam's razor says that among hypotheses that explain the data equally well, the simpler one is more likely to be correct. It turns out this intuition has a precise mathematical form, and it is what underlies the whole story.

Suppose you can describe your hypothesis — your model, your strategy — in a small number of bits, far fewer than it would take to memorize the training data. If that compact hypothesis performs very well on the training data, it must also perform well on new data.

[

](https://cdn.amazon.science/72/eb/d021ebfc445d8f4acd2fe2ac211c/compressionmodels-01-1x1.mp4)

Occam's razor, formalized: among hypotheses that explain the data equally well, the simpler one — describable in fewer bits — is more likely to generalize to new examples.

The reasoning runs through a counting argument. There simply are not very many *short* descriptions, because there are not very many short strings. The fewer candidate hypotheses there are, the less likely it is that any one of them fooled you on the training set by luck — even though you used the training set to guide your search.

Another way to get the intuition: if your compressed description is too small to secretly record the training data, then when it performs well on the training data, it cannot be because it memorized the answers — it didn't have space to do that. It must be because it captured something true about the data's structure. Short descriptions cannot cheat because there isn't room.

Here is an attractive hypothesis: *successful machine learning strategies are highly compressible.* A researcher might stare at thousands of benchmark scores over the course of a project, but the strategy that ultimately survives is usually a short list of familiar choices — an architecture family, an optimizer, a learning-rate schedule, a data-handling recipe, a regularization scheme. If that final recipe can be communicated in just a few bits, then the model's true dependence on the benchmark is far smaller than the long, winding transcript of experiments would suggest. The hill-climbing was extensive, but the thing that came out the other end was — or could have been — tiny.

Compression, intelligence, and the power of a knowledgeable listener
--------------------------------------------------------------------

Imagine trying to explain a specific machine learning pipeline to a bright high-school student, in enough detail that they could actually reproduce it. It would be a long, laborious conversation. You would have to explain what gradient descent is, what a neural network is, what PyTorch or JAX or TensorFlow does, what a learning rate is, and on and on. Almost none of that is specific to *your* problem; it is general background about how machine learning works.

Now imagine explaining the same pipeline to an expert ML engineer. The conversation now collapses to a few sentences. You skip everything that counts as common knowledge and communicate only what is genuinely specific to *this* problem: the architecture choice, the batch size, the optimizer, a couple of hyperparameters. The more your listener already knows about the world, the shorter the message you need to send — and the more aggressively you can compress. None of this "world knowledge" counts against you in the Occam's-razor argument, because you could have written all of that down without having looked at the training set.

This is where large language models enter the picture. Modern LLMs carry an enormous amount of world knowledge. They know how ML tooling works; they know the standard optimization algorithms; they know the conventional hyperparameter choices and the common defaults. If a detail is left unspecified, they can fill in a plausible value. That makes them extraordinarily good *compression decoders*: hand an LLM a terse, expert-to-expert message, and it can unpack it into a full, working procedure. If you think about it, this is exactly why they are so powerful.

The experiment: Squeezing a strategy through a bottleneck
---------------------------------------------------------

This suggests a clean experiment. Have an ML research agent — *the explorer* — try to solve a new machine learning problem. Give it full access to a validation set and let it experiment and iterate freely, chasing better validation performance over hundreds of rounds. Here the validation set plays the role of the benchmark: a *reusable holdout* the agent queries again and again. This is the hill-climbing loop that *ought* to overfit.

Then test how compressible the solution is. A second agent, the *compressor*, reads the entire transcript of the explorer's work and tries to distill the winning strategy into a very short prompt — just a handful of tokens. That prompt is handed to a third agent, the *reproducer*, which must implement the strategy from scratch using only the prompt and the training data. Critically, the reproducer has *no* access to the validation set, the explorer's code, or its transcript. The short prompt is the only channel through which anything learned from the validation set can reach it. (In the study we report in our paper, the compressor and reproducer are both Claude models.)

If the reproducer — starting cold, armed only with a few tokens — matches the explorer's performance, then all the validation-dependent information needed to specify the strategy fit through that tiny channel. The strategy was compressible. We call this a certificate of *output compression*.

The setup has a very useful property that human research communities lack: the reproducer can be reset over and over. The compressor can try many different compressions and see how well each is decoded, because every attempt lands on a fresh reproducer with no memory of the last one. It is a little like the film *Memento* — you are leaving a terse note for a version of yourself whose memory will be wiped before reading it. You learn to write notes that a knowledgeable but amnesiac copy of you can act on; those notes can be very short because the receiver will fill in anything you leave unsaid exactly as you would have.

![CompressionModels-04-1x1.png](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEuMSIgaGVpZ2h0PSI2NzVweCIgd2lkdGg9IjEyMDBweCI+PC9zdmc+)

In the researchers' experiments, an explorer agent's strategy is squeezed through a narrow information bottleneck. Whatever survives compression must reflect real structure, not memorized data.

What comes out the other end
----------------------------

The compressions turn out to be remarkably small. Across eight datasets — spanning tabular classification, image classification, language modeling, diffusion modeling, and reward modeling — 32-token prompts were enough for a fresh reproducer to match the explorer's adaptively optimized models on the large majority of problems. One language-modeling strategy survived compression down to just 16 tokens with no loss in held-out performance.

What do these prompts actually look like? The most revealing examples are right at the border of conciseness where the compression almost breaks. In one language-modeling experiment, the explorer discovered a custom GPT-style training recipe. Under a 16-token budget, this was still enough for fresh reproducers to match the uncompressed explorer:

**QKn 12L768 Mu .1 R² b2M 4x**

To a human reader this looks cryptic, but to another ML agent it says something concrete: *QKn* means “QK normalization”, *12L768* means a 12-layer, 768-dimensional transformer, *Mu .1* means the Muon optimizer with learning rate 0.1, *R²* means squared-ReLU activations, *b2M* means a two-million-token batch, and *4x* means a fourfold feed-forward block. Cut the budget to eight tokens, however, and the prompt becomes

**12L768 Mu .1 R²**

Now the reproducer no longer matches the explorer. The missing pieces specified real training choices that were made as a function of the data and differ from the most obvious defaults. This boundary shows the limits of compressibility and is important. It shows that the reproducer is not succeeding from prior knowledge alone. A few compressed tokens are carrying genuine information learned from the data itself, and when those tokens disappear, so does the performance.

We also ran a set of experiments that imposed an information bottleneck from the other direction. Instead of compressing the explorer's *output*, we compressed its *input*: rather than telling the explorer each model's numerical validation score, we returned only a single bit — did this model beat the running best, or not? Even reduced to one bit of feedback per query, the explorer found strategies as good as those it found with full numerical scores. The channel between the validation set and the final strategy is narrow in both directions, and the one-bit version even comes with a rigorous mathematical guarantee on generalization.

[

](https://cdn.amazon.science/18/ff/a70ce9fd4f878910640f3d0afeaa/compressionmodels-02-16x9.mp4)

Across eight datasets, strategies that emerged from hundreds of iterative experiments could be compressed into prompts as short as 16 to 32 tokens — small enough for a fresh agent with no memory to reproduce the original results.

Catching cheaters
-----------------

A good empirical theory should be falsifiable — and this one is. If low overfitting is really explained by compressibility, then models that *genuinely* overfit should fail to be compressible via this pipeline.

To check, we deliberately pushed agents into overfitting by handing them direct validation-set access and prompting them to maximize validation performance at any cost. The agents took the bait: in 38 of 102 experimental runs, validation accuracy ran more than 10% ahead of true held-out accuracy.

The theory predicts that these gains should not survive the compression bottleneck, because they encode idiosyncrasies of specific validation examples, not transferable structure. Sure enough, when squeezed through a short prompt to a fresh reproducer, the validation-specific advantages vanished. Compression separated the legitimate strategies from the overfitting ones with very high accuracy.

So compression does not merely *explain* why autonomous research agents tend not to overfit but offers a tool for *catching* overfitting when it does occur, by flagging the cases where no short description can reproduce the result.

What this tells us — and what it doesn't
----------------------------------------

A few caveats are in order. The whole framework assumes that the only path from the validation data to the final model runs through the prompt we feed the reproducer. Of course, if a model had memorized the validation data during pretraining, it would have a side channel that bypasses the information bottleneck we are trying to impose. We don't think that is what is happening in our experiments: agents improve gradually through real search rather than starting at their best, and performance degrades at very short token budgets. But fully resolving this question will likely require experimenting with fresh datasets collected after a model's training cutoff, which we haven’t done.

Most importantly, our results are about LLM agents, because that is where the experiment is possible — where you can reset the subject, control its inputs, and count their length. But the picture they paint is strongly suggestive about human research communities too. When a field spends years climbing a fixed benchmark, and the gains keep transferring to fresh data, it may be for the same reason the agents' strategies survive a 32-token prompt: the recipes that actually work are simple. Or in other words, "What fits (into few tokens) doesn't overfit."

**Acknowledgments:** Steven Wu

Research areas

* [Machine learning](https://www.amazon.science/research-areas/machine-learning)

Tags

* [Generative AI](https://www.amazon.science/tag/generative-models)
* [Agentic AI](https://www.amazon.science/tag/agentic-ai)
* [Language models](https://www.amazon.science/tag/language-models)

About the Author

[Martin Bertran Lopez](https://www.amazon.science/author/martin-bertran-lopez)

Martin Bertran Lopez is an applied scientist in Amazon Web Services' Privacy organization.

[Aaron Roth](https://www.amazon.science/author/aaron-roth)

Aaron Roth is the Henry Salvatori Professor of Computer and Cognitive Science at the University of Pennsylvania and an Amazon Scholar. His research focuses on the algorithmic foundations of data privacy, algorithmic fairness, game theory, learning theory, and machine learning. Together with Cynthia Dwork, he is the author of the book [*The Algorithmic Foundations of Differential Privacy*](https://www.cis.upenn.edu/~aaroth/Papers/privacybook.pdf); together with [Michael Kearns](https://www.amazon.science/author/michael-kearns), he is the author of [*The Ethical Algorithm: The Science of Socially Aware Algorithm Design*](https://www.amazon.com/Ethical-Algorithm-Science-Socially-Design-ebook/dp/B07XLTXBXV).
