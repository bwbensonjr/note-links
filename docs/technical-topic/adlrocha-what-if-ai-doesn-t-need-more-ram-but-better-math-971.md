---
id: 971
url: https://adlrocha.substack.com/p/adlrocha-what-if-ai-doesnt-need-more
title: '@adlrocha - What if AI doesn’t need more RAM but better math?'
domain: adlrocha.substack.com
source_date: '2026-03-29'
tags:
- ai
- llm
- academic-paper
summary: Google's TurboQuant algorithm addresses AI's memory bottleneck through mathematical
  compression rather than hardware expansion, achieving 6x reduction in KV cache memory
  with no accuracy loss. The two-stage algorithm converts vector representations from
  Cartesian to polar coordinates for efficient compression, then applies error correction
  to maintain precision without additional memory overhead. This breakthrough could
  significantly impact the AI infrastructure landscape by enabling longer context
  windows and more efficient inference without requiring larger GPU memory or additional
  hardware investment.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# @adlrocha - What if AI doesn’t need more RAM but better math?

@adlrocha - What if AI doesn’t need more RAM but better math?
=============================================================

### How TurboQuant compresses the KV cache without losing accuracy, and what that could mean for memory stocks

[adlrocha](https://substack.com/@adlrochax)

Mar 29, 2026

9

3

3

Share

[![](https://substackcdn.com/image/fetch/$s_!AgT0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F44cb1e23-c8aa-4d3d-a0d7-30a7130749de_2048x1143.png)](https://substackcdn.com/image/fetch/$s_!AgT0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F44cb1e23-c8aa-4d3d-a0d7-30a7130749de_2048x1143.png)

Last week I was [writing about the hardware side of the AI memory problem](https://adlrocha.substack.com/p/adlrocha-why-ai-is-making-your-ram): the HBM density penalty, the EUV bottleneck, and the supply chain pressure squeezing DRAM prices for everyone from data centre operators down to consumer electronics. This week, Google published something that attacks the exact **same problem using another approach: not “build more memory”, but “need less of it.”**

You guessed it! This post will dive a bit deeper into **what TurboQuant is, and what this may imply to the field of AI.** What Pied Piper achieved in the Silicon Valley TV Show with their general-purpose lossless compression algorithm, Google may have achieved it for the compression of information represented as vectors in a high-dimensional space.

[![](https://substackcdn.com/image/fetch/$s_!2QIB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F090a8ffb-9405-4fe4-88b9-3149f2fd730f_1600x900.png)](https://substackcdn.com/image/fetch/$s_!2QIB!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F090a8ffb-9405-4fe4-88b9-3149f2fd730f_1600x900.png)

---

What is a transformer? And the KV cache?
----------------------------------------

But before getting into what TurboQuant does, let’s make a brief detour to understand what is this algorithm is actually built to compress, and why it is important for LLMs and the memory problem.

**GPT models are what are known as autoregressive**: they generate text one token at a time, where each new token is conditioned on everything that came before. You send a prompt, the model reads all of it, picks the most likely next word, appends it, reads everything again, picks the next word, and so on. One token at a time, left to right, until it decides to stop.

**The core mechanism that lets the model read everything at each step is called attention.** For every token in the sequence, the model computes three vectors: a query, a key, and a value. You can think of these data structures as a bit more complex key-value stores. To generate the next token, the model compares the current query against every previous key, essentially asking “which past tokens are relevant right now?”, and uses the answer to weigh the corresponding values and build up context.

This is implemented (as you may all know by now) through the transformer architecture. Transformer layers are responsible for encoding the input sequences into a meaningful representation, applying the attention mechanism, and decoding into an output representation. **All LLMs are architectural variations of this basic cell.**

To get a sense of each of these variations I highly recommend [Sebastian Raschka’s LLM Architecture gallery](https://sebastianraschka.com/llm-architecture-gallery/): from GPT-2 to DeepSeek and GLM.

[![](https://substackcdn.com/image/fetch/$s_!Ldik!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F863521ce-350a-4d97-80d4-026bb37571e2_1217x1000.png)](https://substackcdn.com/image/fetch/$s_!Ldik!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F863521ce-350a-4d97-80d4-026bb37571e2_1217x1000.png)

The keys and values for every previous token are recomputed from scratch on every single pass through architecture. If your conversation is N tokens long and you’re generating token N+1, the model recalculates N sets of keys and values it already calculated on the previous step. This is slow and wasteful in terms of the resources.

**The obvious fix to this is to cache them.** The query, key and values are computed once per token and stored so they can be looked up in subsequent steps instead of being recalculated. This is the **KV cache**, **a** **running store of QKV tokens from all previous tokens stored in GPU memory** (so they are readily accessible when needed).

The problem is that the KV cache grows with every token. With short messages this is trivial as all tokens fit in memory, but a long conversation, or a full code base, involves hundreds of thousands of tokens. Each token has its own key and value vectors, across every attention layer in the model, each stored as a full-precision floating-point number (as long as there’s no quantisation involved). For a model like Llama 3.1 70B, the KV cache for a single long context can consume more GPU memory than the model weights themselves.

This is one of the key bottlenecks in production inference. Serve more users simultaneously? More KV cache. Support longer contexts? More KV cache. Run cheaper inference? Figure out what to do about the KV cache. We are **trading the compute necessary to compute on-the-fly the QKV values, for increased memory requirements.**

By using quantisation instead of storing each value at 32-bit or 16-bit precision, one can round it down to 4 bits or 3 bits (or even [2 bits, like Microsoft recently showed](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/vptq-quantized-2-bit-models-principles-steps-and-practical-implementation/4372907)). Some accuracy is lost in the approximation, but if it is not significant for the user case, the trade-off is obviously worth it. The question is how to do this well. Standard quantisation techniques add 1-2 extra bits of overhead per value as metadata, which partially undermines the compression you’re trying to achieve. Getting to genuinely low bit-widths without that overhead, and without accuracy degradation, is the hard part. HuggingFace has a really [nice page with an overview of quantisation and a list of methods](https://huggingface.co/docs/transformers/v4.49.0/quantization/overview)

---

Enter TurboQuant
----------------

But things may be about to change. [Google announced this week TurboQuant](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/). TurboQuant ([see paper](https://arxiv.org/abs/2504.19874)) is a two-stage algorithm. The two stages have different jobs.

**Stage 1: PolarQuant.** This is the main compression step. We currently store vectors using Cartesian coordinates as distances of a base to the origin (the x, y, z components that we learnt in primary school). The distribution of those components in space makes them hard to compress efficiently.

**PolarQuant converts the vector to polar coordinates: a radius, and an angle.** The key observation is that, in high-dimensional transformer key spaces, the angle distribution is highly concentrated and predictable, it clusters in ways that maps neatly onto a fixed quantisation grid (like the ones used to compress audio and image). That predictability means you can eliminate the expensive normalisation steps that standard quantisation methods require, and you can do it without any dataset-specific tuning. No fine-tuning or calibration pass required to quantise a specific model. One can directly apply it to the vectors in this new representation independent of the model.

**Stage 2: QJL ([Quantised Johnson-Lindenstrauss](https://arxiv.org/pdf/2406.03482)).** PolarQuant handles the main compression, but any quantisation introduces error, and some of that **error accumulates in the dot products that the transformer uses to compute attention** scores. QJL’s job is to correct for this bias. It applies a Johnson-Lindenstrauss transform to the residual error, a random projection that preserves distances between high-dimensional points, and then reduces each component to a single sign bit: +1 or -1. The result is an unbiased estimator for the inner products, with zero additional memory overhead. The error correction costs nothing to store *(see bottom-left part of the image below for a mental model of the shift from existing quantised KV cache and a QJL-transformed one)*.

[![](https://substackcdn.com/image/fetch/$s_!wStc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbe51226e-8122-4b7f-a595-ef65101a7b43_897x563.png)](https://substackcdn.com/image/fetch/$s_!wStc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbe51226e-8122-4b7f-a595-ef65101a7b43_897x563.png)

The combination achieves 3.5 bits per channel with what the paper calls *“absolute quality neutrality”* across Gemma, Mistral, and Llama-3.1-8B-Instruct, tested on LongBench, Needle In A Haystack, ZeroSCROLLS, RULER, and L-Eval. At 2.5 bits, accuracy degrades only marginally. The headline number from the blog post: **6x reduction in KV memory size with no measurable accuracy loss**, and on H100 GPUs, 4-bit TurboQuant delivers up to **8x performance increase** over 32-bit unquantised keys.

[![](https://substackcdn.com/image/fetch/$s_!ph2G!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F45cf7606-51e2-4d24-aa0e-509045b77dc5_1250x561.png)](https://substackcdn.com/image/fetch/$s_!ph2G!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F45cf7606-51e2-4d24-aa0e-509045b77dc5_1250x561.png)

As briefly described above, most quantisation methods require at least some calibration on representative data, they learn the optimal quantisation grid for a specific model on a specific dataset. TurboQuant is data-oblivious: the algorithm works from first principles, near the theoretical lower bounds of what information theory says is possible, without seeing the data first. That’s what makes it deployable at inference time to any models without having to explicitly train the quantised model. **There is no need for specific training and fine-tuning to achieve the most optimal compression rate** without trading accuracy.

---

What this means for the memory crunch
-------------------------------------

Last week I was writing about how HBM stacking reduces DRAM bit density by 3-4x, and how the entire supply chain for consumer DRAM is under pressure because data centres and consumer electronics are competing for the same wafers. If TurboQuant reduces the memory footprint per inference job by 6x, **applying this compression algorithm at scale may significantly relax the memory bottleneck issue.**

Anthropic is not the only one that is able to crash the market cap of public companies with a single announcement. Immediately after Google’s announcement, the stock from memory manufacturing companies like Micron and Sandisk plunged *(and as an investor in Micron, this hits me home 🙈)***.**

[![](https://substackcdn.com/image/fetch/$s_!d_jS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8b105666-9fa9-4f80-8a96-a76e42fca76a_1600x1561.png)](https://substackcdn.com/image/fetch/$s_!d_jS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8b105666-9fa9-4f80-8a96-a76e42fca76a_1600x1561.png)

This may be an overreaction, like when Nvidia stock plunged after Deepseek’s announcement. Or it may be signalling a complete shift in the economics and resource requirements of AI labs. If I were Google, I wouldn’t release research that exposes a competitive advantage. I would only publish research whose progress has already been factored in as the competitors may have already realised it, or adopted themselves TurboQuant has most probably been already adopted inside Google’s infrastructure before anyone outside read the paper.

If Google is publishing 6x KV cache compression, **the reasonable thing to think is that every serious AI lab has been working on this problem already.** Reducing the memory requirements of the KV cache has been a known problem for quite some time, and advancements like TurboQuant adopted at scale change the memory requirements (justifying the hit on these memory stocks). I can’t wait for the next report from SemiAnalysis analysing this release, the real adoption of this new approach to compression (and similar ones) from big labs, and what it can entail to the memory crunch.

Micron and SanDisk haven’t suddenly become bad businesses. But **any thesis that depends on memory demand growing linearly with AI** context usage deserves a second look. My personal take is that the market is overreacting, but we’ll see.

In [this post](https://adlrocha.substack.com/p/adlrocha-money-and-collateral-in) about money and collateral in an AI-first society, I mentioned the book *“The Last Economy”*. This book describes how extreme volatility and sharp turns over any news without achieving a clear equilibrium is a symptom of a sick system. This big market movements over a single news may be proof of the symptoms of a broken system.

---

Beyond LLMs
-----------

What excites me the most about this release is what this Johnson-Lindenstrauss Transform that powers QJL and compression algorithms like TurboQuant could mean for other use cases outside of LLMs and vector search that rely on high-dimensional vector data.

The obvious one outside of KV caches as mentioned above is vector databases. Any RAG pipeline that stores embedding vectors for retrieval benefits from the same compression. **TurboQuant reduces indexing time to “virtually zero” on vector search tasks and outperforms product quantisation** and RabbiQ on recall benchmarks using GloVe vectors.

Further out: recommendation engines, fraud detection, drug discovery similarity search, genomics, any system that stores large tables of high-dimensional embeddings and needs to run fast nearest-neighbour lookups (assuming a similar distribution in space as the values stored in KV caches, which is something I want to explore). These systems weren’t waiting for transformer-specific optimisation, but they may inherit the benefit directly.

**On-device inference is another field inside the world of LLMs where we could start seeing immediate impac**t. If the KV cache for a long context shrinks by 6x, you can fit substantially more context into the memory envelope of a mid-range phone or a modest edge device. Local models with usable context lengths start to look more tractable. The economics of inference at the edge change, and that’s a different set of winners and losers than the data centre story.

I don’t know if you’ve already seen [how some LLMs are being stored in fast flash memory](https://x.com/danveloper/status/2034353876753592372) in order to be able to run LLM inference of big models in a Mac. I’ll leave this for some other post, but the field of edge inference is getting more interesting every day. And even more now that we got TurboQuant.

---

I need to tinker with this thing
--------------------------------

The TurboQuant code is out, both the QJL and PolarQuant components are available, and I can’t wait to find the time to start applying to other use cases. We’ve seen throughout history the impact that changing the way we represent information can have for performance (and even feasibility) of certain use cases *(think of what the Fourier Transform, FFTs, and the frequency domain already enabled :) ).*

I want to find the time to do the exercise of trying to apply the TurboQuant approach to other use cases to see what this is capable of. I already have some ideas, but I’ll report back. In the meantime, until next week!

9

3

3

Share
