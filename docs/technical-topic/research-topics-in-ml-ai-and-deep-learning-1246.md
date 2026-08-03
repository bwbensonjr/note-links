---
id: 1246
url: https://blog.sparsh.dev/research-topics-in-ml-ai-and-deep-learning/
title: Research topics in ML, AI and Deep Learning
domain: blog.sparsh.dev
source_date: '2026-08-02'
tags:
- ai
- llm
- academic-paper
summary: This page outlines major research areas and emerging topics across machine
  learning, AI, and deep learning, including geometric deep learning, transformers,
  and graph neural networks. Key focus areas include addressing computational efficiency
  challenges (quadratic complexity, context windows), improving model reasoning and
  long-context capabilities, and advancing multimodal AI systems. The content emphasizes
  practical applications like combining LLMs with graph neural networks and knowledge
  graphs, alongside emerging techniques such as diffusion models, reinforcement learning
  from human feedback, and parameter-efficient fine-tuning methods.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Research topics in ML, AI and Deep Learning

### Geometric Deep Learning

Euclidean Geometry

Group Invariance Theorem

Universal Approximation

Player Perceptron, Rosenblatt perceptron

Curse of Dimensionality > neocognitron

LeNet-5

![](https://blog.sparsh.dev/content/images/2026/08/software1.0_2.0.png)

Software 1.0 and 2.0

Graph Neural Network, Chemical Precursors, Weisfeiler-Lehman (WL) test

DeepSets

CNN > Symmetry translation, GNN > Symmetry Permutation

CNNs are translation-equivariant; GNN layers are permutation-equivariant, with permutation-invariant graph readouts. [https://arxiv.org/abs/2104.13478](https://arxiv.org/abs/2104.13478?ref=blog.sparsh.dev)

5G of GDL - [https://arxiv.org/abs/2104.13478](https://arxiv.org/abs/2104.13478?ref=blog.sparsh.dev)

1. Grids
2. Groups
3. Graphs
4. Geodesics
5. Gauges

Supervised ML sources of errors > approximation, estimation, optimization

minimization of empirical risk

Error Decomposition

![](https://blog.sparsh.dev/content/images/2026/08/error_decomposition.png)

error decomposition

Total excess error = approximation error + estimation error + optimization error

![](https://blog.sparsh.dev/content/images/2026/08/error-vs-model-complexity-1.png)

error vs model complexity

Double Descent

![](https://blog.sparsh.dev/content/images/2026/08/Double_Descent.png)

double descent

Nearest Neighbor Classifier

Approximation rates

Soboler Class dimensionality cursed

curse in optimization

benign landscapes

Lipschitz estimation error > too large

Sobolev - approx erro > too small

Graph Foundation Models

knowledge graphs TransE

Message Passing Neural Network

Link Prediction with GNN on Knowledge Graphs

Transferability on Knowledge Graphs

---

Transformers Research Gaps > Feasible with Less Compute

**Quadratic Complexity > LoRA, KV Cache Optimization**

Quadratic attention cost > sparse/local/linear attention or FlashAttention; LoRA is for parameter-efficient fine-tuning, while KV-cache optimization targets inference memory. [https://arxiv.org/abs/2209.04881](https://arxiv.org/abs/2209.04881?ref=blog.sparsh.dev)

Fixed Context window > Flash Attention, Sliding Window, RAG

Context limits > long-context training, positional scaling and sliding-window attention; RAG supplies external context, while FlashAttention mainly improves efficiency. [https://arxiv.org/abs/2205.14135](https://arxiv.org/abs/2205.14135?ref=blog.sparsh.dev)

Lack of Inductive bias > Annotations

Lack of inductive bias > architectural priors such as locality, equivariance, recurrence or structured positional encoding; annotations add supervision. [https://arxiv.org/abs/2104.13478](https://arxiv.org/abs/2104.13478?ref=blog.sparsh.dev)

Struggles with Maths

Stochastic Diffusion Models, Deterministic Flow Matching

Diffusion often uses stochastic dynamics, while flow matching usually learns a deterministic ODE vector field; the frameworks can overlap. [https://arxiv.org/abs/2210.02747](https://arxiv.org/abs/2210.02747?ref=blog.sparsh.dev)

Applied

* Stochastic
* Differential
* Equations

Recipes for ML success

1. Large and diverse dataset
2. clear performance criterion
3. degenerate solution space
   1. Suitable hypothesis class and tractable optimization

Dataset void training areas:

1. simple arithmetic
2. sort listing
3. thermostat regulation
4. moral reasoning

---

Elmo RNN of Language Modeling

ELMo: contextual embeddings derived from a deep bidirectional LSTM language model. [https://arxiv.org/abs/1802.05365](https://arxiv.org/abs/1802.05365?ref=blog.sparsh.dev)

Limitations of RNN

RNN trained with back propagation through time

unroll computation graph to standard back prop for each

Slow and difficult to parallelize over long sequences.

Transformers

Self-attention uses queries, keys and values: Q, K and V.

Residual Connection, LayerNorm

Positional embeddings in addition to word embeddings

Casual LM forward probability:

* p(xt |x<t), predicting token t from preceding tokens.

Transformer decoder

Data: trillions of tokens

Compute: massive parallel training

Outlines Guidance, n grammar:

* Outlines and Guidance support constrained generation using JSON Schema, regular expressions and context-free grammars. [https://dottxt-ai.github.io/outlines/1.0.0/features/core/output\_types/](https://dottxt-ai.github.io/outlines/1.0.0/features/core/output_types/?ref=blog.sparsh.dev)

Repetition penalty, grammar matching,

instruction tuning SFT, ROUGE-Lsum for summarization

Encoded in params, tokenization meets instruction tuning

* Knowledge is partly encoded in model parameters; tokenization and instruction tuning are separate components.

Reward model training, R (prompt, response option) > score

triplet of prompt, winning, losing (prompt, Ow, Oc) train R such that R (prompt, Ow) > R (prompt, Oc)

Reinforcement learning from Human Feedback

good to maximize reward with staying close to original model

![](https://blog.sparsh.dev/content/images/2026/08/RLHF--PPO-and-DPO.png)

KL-regularized, PPO and DPO loss

PPO updates - Proximal Policy Optimization, DPO - Direct preference optimization

RL via PPO, RL with Verifiable Rewards (RLVR)

Efficiency Techniques, memory and compute

KV Cache Optimization > Inference

Memory: quantization, 4-bit quantization > 4x memory reduction

* 4-bit weights are theoretically 4x smaller than FP16 weights, but total runtime savings are lower because of metadata, activations and caches. [https://arxiv.org/abs/2305.14314](https://arxiv.org/abs/2305.14314?ref=blog.sparsh.dev)

Parameter-efficient fine-tuning: LoRA. [https://arxiv.org/abs/2106.09685](https://arxiv.org/abs/2106.09685?ref=blog.sparsh.dev)

vLLM, multimodal: vision + language, LLaVA

spiking NN, state space models,

Model distillation, long context techniques RoPE ALiBi

* Long-context positional methods: RoPE and ALiBi; extending the trained window may still require interpolation, scaling or additional training. [https://arxiv.org/abs/2310.13017](https://arxiv.org/abs/2310.13017?ref=blog.sparsh.dev)

Embedding enable generalization

LLM Foundations

ABC scaling, abc-parameterization in μP

Emergent Ability

MMLU tasks few shot prompting:

* MMLU is a 57-subject evaluation benchmark, commonly tested in zero-shot or few-shot settings. [https://arxiv.org/pdf/2009.03300](https://arxiv.org/pdf/2009.03300?ref=blog.sparsh.dev)

chain of thought prompting Elicit Reasoning in LLM

Reasoning, Question < intermediate steps > answer

Inference time scaling

Agentic AI Recall, LLM augmented system with MRT: Memory Retrieval Tools

RAG, Data ingestion:

* relational deep learning
* Graph MC models
* RDL architectures

User churn model

Graph ML Problem Solving Pipeline

Relational DB > Relational Graph > Graph Problem > Graph ML

RelBench Tasks

Heterogeneous GNN, Temporal GNN, architectures of RDL models

GNN vs Feature Engineering

Relational IGT improvement

KumoRFM and Griffin

* KumoRFM and Griffin are separate relational foundation models; Griffin is explicitly graph-centric. [https://arxiv.org/abs/2604.12596](https://arxiv.org/abs/2604.12596?ref=blog.sparsh.dev)

AI Ready Farm

Graph Transformers: ViT/ MLP-Mixer

* Graphormer and Graph ViT/MLP-Mixer; plain ViT and MLP-Mixer originate as vision architectures. [https://arxiv.org/abs/2106.05234](https://arxiv.org/abs/2106.05234?ref=blog.sparsh.dev)

Graph positional encoding, Spectral GNN

GCN: most popular technique of GNN

LLM with GNN

LLM Reasoning, LLM sequence to vector, G-retriever, Graph tokens

Graph RAG:

* helps LLM hallucinations
* proposed approach to LLM
* context windows limited

LLM + GNN + Graph RAG = Superior Performance

* LLM + GNN + Graph RAG can improve graph-centric tasks, subject to dataset-specific evaluation against strong baselines. [https://arxiv.org/abs/2402.07630](https://arxiv.org/abs/2402.07630?ref=blog.sparsh.dev)

Represent graphs as text

model decay

Medical AI

model centric to system centric AI

data privacy, low end devices, edge computing edge AI

success metric, improve health system performance not algorithmic novelty

Applied use cases in Global Health AI

Leltek, BMGF Apps

AI assisted obstetric ultrasound, Uganda

Hallucinations in LVLMs, Data model uncertainty
