---
id: 44
url: https://arxiv.org/abs/2510.25741
title: '[2510.25741] Scaling Latent Reasoning via Looped Language Models'
domain: arxiv.org
source_date: '2026-01-04'
tags:
- academic-paper
- llm
- ai
summary: This paper introduces Ouro, a family of Looped Language Models (LoopLM) that
  integrate reasoning directly into the pre-training phase through iterative computation
  in latent space rather than relying solely on explicit text generation like chain-of-thought
  methods. The 1.4B and 2.6B parameter models achieve performance comparable to 12B
  parameter state-of-the-art models, with experiments demonstrating their advantage
  comes from superior knowledge manipulation rather than increased knowledge capacity.
  The work proposes LoopLM as a novel scaling direction for reasoning capabilities
  in the era of large language models.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# [2510.25741] Scaling Latent Reasoning via Looped Language Models

Computer Science > Computation and Language
===========================================

**arXiv:2510.25741** (cs)

[Submitted on 29 Oct 2025 ([v1](https://arxiv.org/abs/2510.25741v1)), last revised 17 Nov 2025 (this version, v4)]

Title:Scaling Latent Reasoning via Looped Language Models
=========================================================

Authors:[Rui-Jie Zhu](https://arxiv.org/search/cs?searchtype=author&query=Zhu,+R), [Zixuan Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+Z), [Kai Hua](https://arxiv.org/search/cs?searchtype=author&query=Hua,+K), [Tianyu Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+T), [Ziniu Li](https://arxiv.org/search/cs?searchtype=author&query=Li,+Z), [Haoran Que](https://arxiv.org/search/cs?searchtype=author&query=Que,+H), [Boyi Wei](https://arxiv.org/search/cs?searchtype=author&query=Wei,+B), [Zixin Wen](https://arxiv.org/search/cs?searchtype=author&query=Wen,+Z), [Fan Yin](https://arxiv.org/search/cs?searchtype=author&query=Yin,+F), [He Xing](https://arxiv.org/search/cs?searchtype=author&query=Xing,+H), [Lu Li](https://arxiv.org/search/cs?searchtype=author&query=Li,+L), [Jiajun Shi](https://arxiv.org/search/cs?searchtype=author&query=Shi,+J), [Kaijing Ma](https://arxiv.org/search/cs?searchtype=author&query=Ma,+K), [Shanda Li](https://arxiv.org/search/cs?searchtype=author&query=Li,+S), [Taylor Kergan](https://arxiv.org/search/cs?searchtype=author&query=Kergan,+T), [Andrew Smith](https://arxiv.org/search/cs?searchtype=author&query=Smith,+A), [Xingwei Qu](https://arxiv.org/search/cs?searchtype=author&query=Qu,+X), [Mude Hui](https://arxiv.org/search/cs?searchtype=author&query=Hui,+M), [Bohong Wu](https://arxiv.org/search/cs?searchtype=author&query=Wu,+B), [Qiyang Min](https://arxiv.org/search/cs?searchtype=author&query=Min,+Q), [Hongzhi Huang](https://arxiv.org/search/cs?searchtype=author&query=Huang,+H), [Xun Zhou](https://arxiv.org/search/cs?searchtype=author&query=Zhou,+X), [Wei Ye](https://arxiv.org/search/cs?searchtype=author&query=Ye,+W), [Jiaheng Liu](https://arxiv.org/search/cs?searchtype=author&query=Liu,+J), [Jian Yang](https://arxiv.org/search/cs?searchtype=author&query=Yang,+J), [Yunfeng Shi](https://arxiv.org/search/cs?searchtype=author&query=Shi,+Y), [Chenghua Lin](https://arxiv.org/search/cs?searchtype=author&query=Lin,+C), [Enduo Zhao](https://arxiv.org/search/cs?searchtype=author&query=Zhao,+E), [Tianle Cai](https://arxiv.org/search/cs?searchtype=author&query=Cai,+T), [Ge Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+G), [Wenhao Huang](https://arxiv.org/search/cs?searchtype=author&query=Huang,+W), [Yoshua Bengio](https://arxiv.org/search/cs?searchtype=author&query=Bengio,+Y), [Jason Eshraghian](https://arxiv.org/search/cs?searchtype=author&query=Eshraghian,+J)

View a PDF of the paper titled Scaling Latent Reasoning via Looped Language Models, by Rui-Jie Zhu and 32 other authors

[View PDF](/pdf/2510.25741)
[HTML (experimental)](https://arxiv.org/html/2510.25741v4)
> Abstract:Modern LLMs are trained to "think" primarily via explicit text generation, such as chain-of-thought (CoT), which defers reasoning to post-training and under-leverages pre-training data. We present and open-source Ouro, named after the recursive Ouroboros, a family of pre-trained Looped Language Models (LoopLM) that instead build reasoning into the pre-training phase through (i) iterative computation in latent space, (ii) an entropy-regularized objective for learned depth allocation, and (iii) scaling to 7.7T tokens. Ouro 1.4B and 2.6B models enjoy superior performance that match the results of up to 12B SOTA LLMs across a wide range of benchmarks. Through controlled experiments, we show this advantage stems not from increased knowledge capacity, but from superior knowledge manipulation capabilities. We also show that LoopLM yields reasoning traces more aligned with final outputs than explicit CoT. We hope our results show the potential of LoopLM as a novel scaling direction in the reasoning era. Our model is available here: [this http URL](http://ouro-llm.github.io).

|  |  |
| --- | --- |
| Subjects: | Computation and Language (cs.CL) |
| Cite as: | [arXiv:2510.25741](https://arxiv.org/abs/2510.25741) [cs.CL] |
|  | (or  [arXiv:2510.25741v4](https://arxiv.org/abs/2510.25741v4) [cs.CL] for this version) |
|  | <https://doi.org/10.48550/arXiv.2510.25741> Focus to learn more  arXiv-issued DOI via DataCite |

Submission history
------------------

From: Rui-Jie Zhu [[view email](/show-email/68abbce3/2510.25741)]   
 **[[v1]](/abs/2510.25741v1)**
Wed, 29 Oct 2025 17:45:42 UTC (14,928 KB)  
**[[v2]](/abs/2510.25741v2)**
Mon, 3 Nov 2025 06:54:49 UTC (9,619 KB)  
**[[v3]](/abs/2510.25741v3)**
Fri, 14 Nov 2025 02:14:36 UTC (9,607 KB)  
**[v4]**
Mon, 17 Nov 2025 20:03:56 UTC (9,607 KB)

Full-text links:

Access Paper:
-------------

View a PDF of the paper titled Scaling Latent Reasoning via Looped Language Models, by Rui-Jie Zhu and 32 other authors

* [View PDF](/pdf/2510.25741)
* [HTML (experimental)](https://arxiv.org/html/2510.25741v4)
* [TeX Source](/src/2510.25741)

[![license icon](https://arxiv.org/icons/licenses/by-sa-4.0.png)
view license](http://creativecommons.org/licenses/by-sa/4.0/ "Rights to this article")

Current browse context:

cs.CL

[< prev](/prevnext?id=2510.25741&function=prev&context=cs.CL "previous in cs.CL (accesskey p)")
  |   
[next >](/prevnext?id=2510.25741&function=next&context=cs.CL "next in cs.CL (accesskey n)")

[new](/list/cs.CL/new)
 | 
[recent](/list/cs.CL/recent)
 | [2025-10](/list/cs.CL/2025-10)

Change to browse by:

[cs](/abs/2510.25741?context=cs)

### References & Citations

* [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2510.25741)
* [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2510.25741)
* [Semantic Scholar](https://api.semanticscholar.org/arXiv:2510.25741)

export BibTeX citation
Loading...

BibTeX formatted citation
-------------------------

×

loading...

Data provided by:

### Bookmark

[![BibSonomy logo](/static/browse/0.3.4/images/icons/social/bibsonomy.png)](http://www.bibsonomy.org/BibtexHandler?requTask=upload&url=https://arxiv.org/abs/2510.25741&description=Scaling Latent Reasoning via Looped Language Models "Bookmark on BibSonomy")
[![Reddit logo](/static/browse/0.3.4/images/icons/social/reddit.png)](https://reddit.com/submit?url=https://arxiv.org/abs/2510.25741&title=Scaling Latent Reasoning via Looped Language Models "Bookmark on Reddit")



Bibliographic Tools

Bibliographic and Citation Tools
================================

Bibliographic Explorer Toggle

Bibliographic Explorer *([What is the Explorer?](https://info.arxiv.org/labs/showcase.html#arxiv-bibliographic-explorer))*

Connected Papers Toggle

Connected Papers *([What is Connected Papers?](https://www.connectedpapers.com/about))*

Litmaps Toggle

Litmaps *([What is Litmaps?](https://www.litmaps.co/))*

scite.ai Toggle

scite Smart Citations *([What are Smart Citations?](https://www.scite.ai/))*

Code, Data, Media

Code, Data and Media Associated with this Article
=================================================

alphaXiv Toggle

alphaXiv *([What is alphaXiv?](https://alphaxiv.org/))*

Links to Code Toggle

CatalyzeX Code Finder for Papers *([What is CatalyzeX?](https://www.catalyzex.com))*

DagsHub Toggle

DagsHub *([What is DagsHub?](https://dagshub.com/))*

GotitPub Toggle

Gotit.pub *([What is GotitPub?](http://gotit.pub/faq))*

Huggingface Toggle

Hugging Face *([What is Huggingface?](https://huggingface.co/huggingface))*

Links to Code Toggle

Papers with Code *([What is Papers with Code?](https://paperswithcode.com/))*

ScienceCast Toggle

ScienceCast *([What is ScienceCast?](https://sciencecast.org/welcome))*

Demos

Demos
=====

Replicate Toggle

Replicate *([What is Replicate?](https://replicate.com/docs/arxiv/about))*

Spaces Toggle

Hugging Face Spaces *([What is Spaces?](https://huggingface.co/docs/hub/spaces))*

Spaces Toggle

TXYZ.AI *([What is TXYZ.AI?](https://txyz.ai))*

Related Papers

Recommenders and Search Tools
=============================

Link to Influence Flower

Influence Flower *([What are Influence Flowers?](https://influencemap.cmlab.dev/))*

Core recommender toggle

CORE Recommender *([What is CORE?](https://core.ac.uk/services/recommender))*

* Author
* Venue
* Institution
* Topic


About arXivLabs

arXivLabs: experimental projects with community collaborators
=============================================================

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? [**Learn more about arXivLabs**](https://info.arxiv.org/labs/index.html).

[Which authors of this paper are endorsers?](/auth/show-endorsers/2510.25741) |
[Disable MathJax](javascript:setMathjaxCookie()) ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))
