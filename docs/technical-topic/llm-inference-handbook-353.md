---
id: 353
url: https://bentoml.com/llm/
title: LLM Inference Handbook
domain: bentoml.com
source_date: '2025-07-11'
tags:
- llm
- tutorial
- ai
- devops
summary: The LLM Inference Handbook is a comprehensive technical resource that consolidates
  fragmented knowledge about LLM inference into one centralized guide, covering core
  concepts, performance metrics, optimization techniques, and production deployment
  patterns. Designed for engineers deploying and operating LLMs in production, it
  provides practical, field-tested guidance focused on making LLM inference faster,
  cheaper, and more reliable rather than covering edge cases. The handbook is continuously
  updated with the latest best practices and welcomes community contributions to stay
  current with the rapidly evolving field.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# LLM Inference Handbook

On this page

*LLM Inference Handbook* is your technical glossary, guidebook, and reference - all in one. It covers everything you need to know about LLM inference, from core concepts and performance metrics (e.g., [Time to First Token and Tokens per Second](/llm/llm-inference-basics/llm-inference-metrics)), to optimization techniques (e.g., [continuous batching](/llm/inference-optimization/static-dynamic-continuous-batching) and [prefix caching](/llm/inference-optimization/prefix-caching)), [GPU achitecture](/llm/kernel-optimization/gpu-architecture-fundamentals), and deployment patterns like [BYOC](/llm/getting-started/bring-your-own-cloud) and [on-prem](/llm/getting-started/on-prem-llms).

* Practical guidance for deploying, scaling, and operating LLMs in production.
* Explore concepts with interactive calculators, simulators, and visual tools.
* Boost performance with optimization techniques tailored to your use case.
* Continuously updated with the latest best practices and field-tested insights.

Motivation[​](#motivation "Direct link to Motivation")
------------------------------------------------------

We wrote this handbook to solve a common problem facing developers: LLM inference knowledge is often fragmented; it’s buried in academic papers, scattered across vendor blogs, hidden in GitHub issues, or tossed around in Discord threads. Worse, much of it assumes you already understand half the stack.

There aren’t many resources that bring it all together — like how [inference differs from training](/llm/llm-inference-basics/training-inference-differences), why [goodput matters more than raw throughput](/llm/llm-inference-basics/llm-inference-metrics#goodput) for meeting SLOs, or how [prefill-decode disaggregation](/llm/inference-optimization/prefill-decode-disaggregation) works in practice.

So we started pulling it all together.

Who this is for[​](#who-this-is-for "Direct link to Who this is for")
---------------------------------------------------------------------

This handbook is for engineers deploying, scaling or operating LLMs in production, whether you're fine-tuning a small open model or running large-scale deployments on your own stack.

If your goal is to make LLM inference faster, cheaper, or more reliable, this handbook is for you.

How to use this[​](#how-to-use-this "Direct link to How to use this")
---------------------------------------------------------------------

You can read it start-to-finish or treat it like a lookup table. There’s no wrong way to navigate. We’ll keep updating the handbook as the field evolves, because LLM inference is changing fast, and what works today may not be best tomorrow.

Where are you in the stack?

3 questions · find your most relevant starting point

1

2

3

✦

Question 1 of 3

How are you currently running LLMs?

Via a managed API (OpenAI, Anthropic, etc.)→Self-hosted on my own infrastructure→Still evaluating options→

Interactive tools[​](#interactive-tools "Direct link to Interactive tools")
---------------------------------------------------------------------------

This handbook provides various interactive tools to help you learn by trying the concepts directly:

* [LLM Inference Visualizer](/llm/llm-inference-basics/what-is-llm-inference): Walk through the request lifecycle and see how tokens flow through prefill and decode.
* [Token-by-Token Decode Loop](/llm/llm-inference-basics/how-does-llm-inference-work#decode): Step through autoregressive decoding and watch each new token extend the sequence and KV cache.
* [Context Window Simulator](/llm/llm-inference-basics/how-does-llm-inference-work#what-is-a-context-window-and-how-does-it-work-in-llm-inference): See how the full conversation is re-sent each turn and fills the context window.
* [Latency Metrics Playground](/llm/llm-inference-basics/llm-inference-metrics#latency): Explore TTFT, E2EL, TPOT, and SLO-based goodput.
* [Model Explorer](/llm/getting-started/choosing-the-right-model): Browse popular open-source LLMs and compare their architecture, scale, context, and typical GPU deployment.
* [GPU Comparison Table](/llm/getting-started/choosing-the-right-gpu#matching-gpus-to-open-source-llms): Match popular open-source LLMs to suitable NVIDIA and AMD GPUs.
* [GPU Memory Calculator](/llm/getting-started/calculating-gpu-memory-for-llms): Estimate VRAM requirements for serving an LLM.
* [Quantization Memory Impact Visualizer](/llm/model-preparation/llm-quantization#quantization-formats): Compare weight memory across quantization formats.
* [Batching Strategy Simulator](/llm/inference-optimization/static-dynamic-continuous-batching): Compare static, dynamic, and continuous batching behavior.
* [KV Cache Memory Calculator](/llm/inference-optimization/kv-cache-offloading#how-to-calculate-the-kv-cache-size): Estimate how much memory the KV cache consumes.
* [GPU Execution and Memory Map](/llm/kernel-optimization/gpu-architecture-fundamentals): Visualize how threads, warps, SMs, and the GPU memory hierarchy fit together.

Contributing[​](#contributing "Direct link to Contributing")
------------------------------------------------------------

We welcome contributions! If you spot an error, have suggestions for improvements, or want to add new topics, please open an issue or submit a pull request on our [GitHub repository](https://github.com/bentoml/llm-inference-handbook).

### Stay updated with the handbook

Get the latest insights and updates on LLM inference and optimization techniques.

* Monthly insights
* Latest techniques
* Handbook updates
