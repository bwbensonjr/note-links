---
id: 198
url: https://verdik.substack.com/p/how-to-get-consistent-classification
title: How to Get Consistent Classification From Inconsistent LLMs?
domain: verdik.substack.com
source_date: '2025-10-20'
tags:
- llm
- ai
- tutorial
summary: 'The article presents a technique for achieving consistent classification
  from Large Language Models (LLMs) by combining embeddings with vector similarity
  search. While LLMs generate lexicographically inconsistent labels for the same content,
  the author discovered they remain semantically consistent—allowing labels to be
  clustered in vector space and mapped to root categories through a disjoint set union
  approach.


  Benchmarked results show this vectorization method significantly outperforms pure
  LLM classification at scale: it reduces unique labels by 80% (from 6,520 to 1,381
  for 10K tweets), achieves 94% cache hit rates, and becomes 10x cheaper per classification
  while eventually being faster than direct LLM calls, despite initial overhead.'
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# How to Get Consistent Classification From Inconsistent LLMs?

How to Get Consistent Classification From Inconsistent LLMs?
============================================================

### A technique for deterministic labeling from stochastic models, with benchmarked Golang implementation.

[![Verdi's avatar](https://substackcdn.com/image/fetch/$s_!wyku!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3674e146-68a2-457c-8d11-700f7f0bb605_982x982.png)](https://substack.com/@verdik)

[Verdi](https://substack.com/@verdik)

Oct 10, 2025

34

8

1

Share

TLDR: If you don’t care for the entrée, you can jump directly to [Results](https://verdik.substack.com/i/174718824/analyzing-results) & [Code](https://verdik.substack.com/i/174718824/show-me-the-code) section.

---

I saw a recent [Reddit post](https://www.reddit.com/r/MachineLearning/comments/1npdfh1/d_is_senior_ml_engineering_just_api_calls_now/) where a senior ML engineer was complaining that his job has been reduced to calling APIs of the big model providers and he no longer does ML work himself anymore.

[![](https://substackcdn.com/image/fetch/$s_!w2VC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F03677db5-58d5-4025-b703-0d24e526a63b_1024x1024.png)](https://substackcdn.com/image/fetch/$s_!w2VC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F03677db5-58d5-4025-b703-0d24e526a63b_1024x1024.png)

Courtesy of Gemini

In fact, Andrew Ng said during a lecture titled [Opportunities in AI](https://www.youtube.com/watch?v=5p248yoa3oE&t=1307s) at Stanford (2023 is the time of recording), that it no longer makes sense to train a NLP sentiment classifier. 7 lines of code calling OpenAI’s API will get you the same or superior results in less than 5 minutes, at a reasonably low marginal cost.

One of the biggest data problems that LLMs can help us solve is labeling large amounts of unlabeled data using an unconstrained label set. This was a task where previously a human painstakingly had to label every piece of data one by one. This was expensive, slow and error prone.

LLM just make sense! … right?

Well, yes and no. The truth is, large language models can be incredibly inconsistent with the class labels they generate. Now, if you have a pre-defined list, then you are good to go! You can use `logit_bias` and `json_schema` topped with an tight prompt to get satisfying results. If you don’t however, then you need to grapple with this problem:

> How do I get consistent classification, out of this inconsistency-spitting machine?

Funny paradox but there is a way. I discovered it through pain, blood and suffering; and you will get it for free 🙂. I will present it here, how to set it up, demonstrate its efficacy in terms of accuracy, cost, and latency, and lastly share a repo with all the code you will need.

If you are grateful for my blood sacrifice, please subscribe!

The Moment It All Clicked
=========================

I was working on a use-case where I was pulling ten of thousands of tweets from Twitter/X per day and I needed to classify what kind of posts they were. As you can imagine, my label space was impossible large to accurately map ahead of time.

My prompt looked something like this:

```
Read the following tweet and provide a classification string to categorize it.

Your class label should be between 30 and 60 characters and be precise in snake_case format. For example:
- complain_about_political_party
- make_joke_about_zuckerberg_rebranding

Now, classify this tweet: {{tweet}}
```

This sorta worked. Some labels were bad but most were good. In order to train an AI model to tweet like a real human, I needed to be able to group “similar tweets” together so I could establish both:

1. A pattern for what Verdi typically tweets about (topic-wise)
2. A user-specific dataset of how Verdi typically tweets (style-wise, sharded by topic)

When looking to create these grouping, I could not query my SQL database by `category_label` because they were slightly different each time I ran the LLM for the exact same tweet… For instance

```
const tweet = `Rust programmer be like: 'I rewrote your 10-line Python script in Rust. It’s now 200 lines, took me 3 weeks, but it’s MEMORY SAFE and runs 0.002ms faster. You’re welcome.'`

const labels = [
  ‘joke_about_bad_technology_choices’,
  ‘make_fun_of_rust_programmers’,
  ‘humor_concerning_rust_programmers’
]
```

This is when it hit me:

Language models are **lexicographically** inconsistent, but **semantically** consistent!

This meant I could adapt concepts from [Bag of Words](https://machinelearningmastery.com/gentle-introduction-bag-words-model/) modeling to:

1. cluster the inconsistent labels by embedding them in a vector space
2. and upon generating a new label, I could do a vector search to find its nearest siblings,
3. and run path compression on a dsu to consistently retrace to a root label for that cluster.

[![a man with glasses is surrounded by a glowing circle and the website pmitf.com is displayed below him](https://substackcdn.com/image/fetch/$s_!_aZo!,w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbe304609-b071-4b99-ab45-c2435fc8ca4d_640x408.gif "a man with glasses is surrounded by a glowing circle and the website pmitf.com is displayed below him")](https://substackcdn.com/image/fetch/$s_!_aZo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbe304609-b071-4b99-ab45-c2435fc8ca4d_640x408.gif)

How coming to that realization felt

Analyzing Results
=================

Enough talk. Let’s look at numbers to see how effective this truly is and then we will dig into the code. I used:

* `gpt-4.1-mini` for the LLM
* `voyage-3.5-lite` for embedding (@ 1024 dims)
* Pinecone for vector storage and search

[![](https://substackcdn.com/image/fetch/$s_!rurH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F17af7f55-c0c2-454e-a299-e42898fd51a3_2850x1581.png)](https://substackcdn.com/image/fetch/$s_!rurH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F17af7f55-c0c2-454e-a299-e42898fd51a3_2850x1581.png)

This chart confirms a few key findings and reveals a few surprising ones which are:

* With vectorization, we end up with a convergence of labels
* At scale, it’s both faster and cheaper to classify with vectorization
* It is about 15% more expensive in the beginning to vectorize
* Lastly, vectorization is 130% *slower* than a pure LLM-only classifier early on!

Let us dig into this. First let us consider the number of labels we end up with.

[![](https://substackcdn.com/image/fetch/$s_!bASt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7efb8c3a-3658-43ea-9160-04c8366c5fd4_3049x1651.png)](https://substackcdn.com/image/fetch/$s_!bASt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7efb8c3a-3658-43ea-9160-04c8366c5fd4_3049x1651.png)

We notice that the number of labels grows linearly with LLM-only while it follows a square root curve in the vectorize flow.

\(\begin{gather}
\text{for LLM: }slope\_\mathcal{L} = 0.652n
\\
\text{for Vector: }slope\_\mathcal{V} = 13.8\sqrt{n}
\end{gather}\)

We end up with approximately 6,520 labels using an LLM and 1,381 with vectors for 10K tweets. 1/5th the amount!

This confirms our theory that LLMs will generate many lexicographically inconsistent labels that are semantically consistent. Our use of a vector index to perform a cosine similarity search reveals this and causes the classifier to increasingly find more near-identical hits as the size of the dataset grows. Let us observe our cache hit rate:

[![](https://substackcdn.com/image/fetch/$s_!It6I!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcca0f15d-307d-4c9f-b085-fc6d5c1b39ec_2116x842.png)](https://substackcdn.com/image/fetch/$s_!It6I!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcca0f15d-307d-4c9f-b085-fc6d5c1b39ec_2116x842.png)

In the first 100 tweets we saw, we were below 5% and by the time we reach tweet 500 we are at a 23% cache hit rate. We can model how this would continue to scale for the entire dataset.

[![](https://substackcdn.com/image/fetch/$s_!WLAk!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbd2cfafd-0356-4f55-9ed4-1290a2fad5fa_3023x1717.png)](https://substackcdn.com/image/fetch/$s_!WLAk!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbd2cfafd-0356-4f55-9ed4-1290a2fad5fa_3023x1717.png)

By the time we have processed the 10,000th tweets, we are hitting our vector index cache more than 94% of the time! Based on this formula:

\(\text{hit\_rate}(n) = 0.95\times(1-e^{-0.28n})\)

We have a asymptotic ceiling at 95% because we are making the assumption that no matter how large our dataset grows, there is always going to be a certain number of tweets that do not fit into any pre-existing cluster we must classify with an LLM.[1](#footnote-1)

Marginal Cost per Tweet
-----------------------

I was not surprised to see initial cost for the vectorize flow to be higher. I expected a small lift in cost in the beginning since we are doing:

\(\begin{gather}
\mathcal{C}\text{(LLM)} + \mathcal{C}(\text{Embedding}) + \mathcal{C}(\text{VectorWrite})
\\
\text{vs.}
\\
\mathcal{C}(\text{LLM})
\\
\\
\text{Where }\mathcal{C(x)}=\text{ cost for operation } x.
\end{gather}\)

The embedding and vector operations are comparably cheaper than the LLM calls (which dominates the cost chart). Thus, seeing 15% higher costs in the beginning made sense. Furthermore, we can observe how this cost trends down over time.

[![](https://substackcdn.com/image/fetch/$s_!nInV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdf12acb0-6795-4f33-a761-075a0e36754a_3116x1651.png)](https://substackcdn.com/image/fetch/$s_!nInV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdf12acb0-6795-4f33-a761-075a0e36754a_3116x1651.png)

We start of at $0.00017/tweet to vectorize as opposed to $0.00013 /tweet via LLM but by the 500th, tweet our vector costs have dipped below and they will continue this downward trajectory as we classify more data.

[![](https://substackcdn.com/image/fetch/$s_!EzO7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7297e199-9b3a-4439-9b1d-3e61528480a7_3116x1651.png)](https://substackcdn.com/image/fetch/$s_!EzO7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7297e199-9b3a-4439-9b1d-3e61528480a7_3116x1651.png)

By the time we reach the 10,000th tweet, it is 10x cheaper to classify using vectors. This makes intuitive sense: as the dataset in our vector index grows, the chance of a cache hit grows accordingly. A cache hit = no calls to the LLM = lower costs per classification.

Marginal Latency per Tweet
--------------------------

This was a huge surprise to me, to see processing time be 130% slower in the vectorize flow as opposed to pure-LLM in the beginning. I knew it would be slower, but not *this* slow. Let us observe the marginal latency.

[![](https://substackcdn.com/image/fetch/$s_!GImT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1a33b3d6-b821-4b29-9f2f-a57a929a2c05_3049x1651.png)](https://substackcdn.com/image/fetch/$s_!GImT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1a33b3d6-b821-4b29-9f2f-a57a929a2c05_3049x1651.png)

Unfortunately, I did not track the time for individual components in the chain but my assumption is the average latency to generate an embedding is to blame.

My theory behind this chart presupposes that vectorize is slower because we need to:

1. Embed the piece of content
2. Do a vector search to find near-identical hits already classified
3. if not found, then do the LLM call to classify

Step 1 and 2 add time, but as we start finding more and more cache hits, we are able to delete the 3rd step. This allows us to observe:

\(\begin{gather}
\mathcal{T(x)}=\text{ time for operation } x.
\\
\mathcal{T}(\text{embed}) + \mathcal{T}(\text{search}) < \mathcal{T}(\text{LLM})
\end{gather}\)

I ran out of pretty charts I could create for you so let’s move on to look at the code behind this experiment but hopefully this show satisfying results and proves why this technique should be a strong candidate for some of your future classification needs.

Show Me The Code
================

You can find the Github repo here: [consistent-classifier](https://github.com/FrenchMajesty/consistent-classifier). This is how I’ve organized it:

```
pkg/
├── classifier/         # Core classification logic
│   ├── classifier.go   # Main Classifier implementation
│   ├── config.go       # Configuration and defaults
│   ├── interfaces.go   # Client interfaces
│   └── types.go        # Result and Metrics types
├── adapters/           # External service adapters
│   ├── adapters.go     # Voyage and Pinecone adapters
│   ├── llm_client.go   # OpenAI adapter
│   ├── openai/         # OpenAI client implementation
│   ├── pinecone/       # Pinecone client implementation
│   └── voyage/         # Voyage AI client implementation
└── types/              # Shared types

utils/disjoint_set/     # DSU implementation for label clustering
```

The way the `classifier` package works is very simple.

1. **Embedding Generation**: Text is converted to a vector using Voyage AI (or custom provider)
2. **Cache Check**: Searches vector store for similar previously-classified text
3. **On Cache Hit**: Uses the cached label we found from the search to return its root
4. **On Cache Miss**: Calls LLM for classification, then:

   1. Stores text embedding for future lookups
   2. Searches for similar labels and clusters them using DSU
   3. Stores label embedding for clustering

[![](https://substackcdn.com/image/fetch/$s_!whwT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9e1cab63-85b3-40f8-936a-aa3fce94f55a_926x1016.png)](https://substackcdn.com/image/fetch/$s_!whwT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9e1cab63-85b3-40f8-936a-aa3fce94f55a_926x1016.png)

Example of usage for the classifier

Feel free to dig into the code to see how it’s setup. One of the important defaults you might want to play round with is the minimum cosine similarity threshold for clustering.

I chose `0.80` for both the content and labels. I don’t recommend changing it for labels unless you want it more tight/strict but I definitively recommend playing around with the threshold for the content.

I was classifying tweet replies, which are short (< 140 chars) so `0.80` was enough to capture near-identical but I’m not sure this heuristic holds if the content you’re classifying is less than 80 chars or more than 1,000.

### Benchmarking

I did not do anything fancy here. I created [llm.go](https://github.com/FrenchMajesty/consistent-classifier/blob/main/cmd/benchmark/llm.go) where I classify with an LLM only and [vectorize.go](https://github.com/FrenchMajesty/consistent-classifier/blob/main/cmd/benchmark/vectorize.go) where we use the classifier package. For each operation, we track various metrics that fit into the following interface:

[![](https://substackcdn.com/image/fetch/$s_!ssat!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8dbbc751-a4d4-4686-adf5-51ad5de57719_1092x948.png)](https://substackcdn.com/image/fetch/$s_!ssat!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8dbbc751-a4d4-4686-adf5-51ad5de57719_1092x948.png)

Benchmark metrics collected from both runs

I ran:

```
go run cmd/benchmark/** --classify=vectorize --limit=500
go run cmd/benchmark/** --classify=llm --limit=500
```

And graphed the metrics collected from both runs. That’s it!

Conclusion
==========

In conclusion, we discussed in this short essay a key insight that help us understand LLMs better.

Given an identical input I , language models create N lexicographically inconsistent labels that are semantically consistent.

We can leverage this semantical consistency to clusters our labels in a vector space and derive a consistent root label from each cluster using an algorithm like Disjoint Set Union. This helps us to create a tighter and cleaner dataset of class labels when your label space is unconstrained.

We saw how this approach is highly scalable as the margical cost & time to classify the next item trends downward compared to the baseline.

Lastly, we saw how easy it to integrate into a real application and to top it off, I wrapped up my findings here into a easy-to-use Golang package I lazily named `consistent-classifier`.

Thanks for reading! Leave a comment below if you have any questions.

[1](#footnote-anchor-1)

This could totally be disproved with more experiment and data, but this feels like a safe assumption to make for simplicity sake.

34

8

1

Share
