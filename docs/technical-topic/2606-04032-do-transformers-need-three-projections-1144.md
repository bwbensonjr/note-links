---
id: 1144
url: https://arxiv.org/abs/2606.04032
title: '[2606.04032] Do Transformers Need Three Projections? Systematic Study of QKV
  Variants'
domain: arxiv.org
source_date: '2026-06-04'
tags:
- academic-paper
- ai
- llm
summary: This paper systematically investigates whether transformers require three
  separate projections (query, key, value) in their attention mechanism, testing variants
  that share projections across different components. The researchers find that sharing
  key-value projections achieves comparable performance to standard transformers while
  reducing KV cache by 50% with minimal perplexity degradation, and when combined
  with other optimization techniques like head sharing, enables up to 96.9% cache
  reduction for on-device inference. The findings demonstrate that projection sharing
  is an underexplored and practical approach to reducing memory requirements in transformer
  models without significant quality loss.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# [2606.04032] Do Transformers Need Three Projections? Systematic Study of QKV Variants

Computer Science > Machine Learning
===================================

**arXiv:2606.04032** (cs)

[Submitted on 1 Jun 2026 ([v1](https://arxiv.org/abs/2606.04032v1)), last revised 4 Jun 2026 (this version, v2)]

Title:Do Transformers Need Three Projections? Systematic Study of QKV Variants
==============================================================================

Authors:[Ali Kayyam](https://arxiv.org/search/cs?searchtype=author&query=Kayyam,+A), [Anusha Madan Gopal](https://arxiv.org/search/cs?searchtype=author&query=Gopal,+A+M), [M Anthony Lewis](https://arxiv.org/search/cs?searchtype=author&query=Lewis,+M+A)

View a PDF of the paper titled Do Transformers Need Three Projections? Systematic Study of QKV Variants, by Ali Kayyam and 2 other authors

[View PDF](/pdf/2606.04032)
[HTML (experimental)](https://arxiv.org/html/2606.04032v2)
> Abstract:Transformers have become the standard solution for various AI tasks, with the query, key, and value (QKV) attention formulation playing a central role. However, the individual contribution of these three projections and the impact of omitting some remain poorly understood. We systematically evaluate three projection sharing constraints: a) Q-K=V (shared key-value), b) Q=K-V (shared query-key), and c) Q=K=V (single projection). The last two variants produce symmetric attention maps; to address this, we also explore asymmetric attention via 2D positional encodings. Through experiments spanning synthetic tasks, vision (MNIST, CIFAR, TinyImageNet, anomaly), and language modeling (300M and 1.2B parameter models on 10B tokens), we discovered that our transformers perform on par or occasionally better than the QKV transformer. In language modeling, Q-K=V projection sharing achieves 50% KV cache reduction with only 3.1% perplexity degradation. Crucially, projection sharing is complementary to head sharing (GQA/MQA): combining Q-K=V with GQA-4 yields 87.5% cache reduction, while Q-K=V + MQA achieves 96.9%, enabling practical on-device inference. We show that Q-K=V preserves quality because keys and values can occupy similar representational spaces and attention operates in a low-rank regime, whereas Q=K-V breaks attention directionality. Our results systematically characterize projection sharing as an underexplored instance of weight tying in attention, with direct, quantifiable inference memory benefits, particularly valuable for edge deployment. The code is publicly available at [this https URL](https://github.com/Brainchip-Inc/Do-Transformers-Need-3-Projections)

|  |  |
| --- | --- |
| Comments: | Accepted at ICML 2026 (PMLR vol. 306). 26 pages, 12 figures, 16 tables. Code: [this https URL](https://github.com/Brainchip-Inc/Do-Transformers-Need-3-Projections) |
| Subjects: | Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Performance (cs.PF) |
| ACM classes: | I.2.6; I.2.7; I.2.10 |
| Cite as: | [arXiv:2606.04032](https://arxiv.org/abs/2606.04032) [cs.LG] |
|  | (or  [arXiv:2606.04032v2](https://arxiv.org/abs/2606.04032v2) [cs.LG] for this version) |
|  | <https://doi.org/10.48550/arXiv.2606.04032> Focus to learn more  arXiv-issued DOI via DataCite |

Submission history
------------------

From: Anusha Madan Gopal [[view email](/show-email/278822ff/2606.04032)]   
 **[[v1]](/abs/2606.04032v1)**
Mon, 1 Jun 2026 20:59:05 UTC (2,017 KB)  
**[v2]**
Thu, 4 Jun 2026 17:08:43 UTC (2,017 KB)

Full-text links:

Access Paper:
-------------

View a PDF of the paper titled Do Transformers Need Three Projections? Systematic Study of QKV Variants, by Ali Kayyam and 2 other authors

* [View PDF](/pdf/2606.04032)
* [HTML (experimental)](https://arxiv.org/html/2606.04032v2)
* [TeX Source](/src/2606.04032)

[![license icon](https://arxiv.org/icons/licenses/by-4.0.png)
view license](http://creativecommons.org/licenses/by/4.0/ "Rights to this article")

### Current browse context:

cs.LG

[< prev](/prevnext?id=2606.04032&function=prev&context=cs.LG "previous in cs.LG (accesskey p)")
  |   
[next >](/prevnext?id=2606.04032&function=next&context=cs.LG "next in cs.LG (accesskey n)")

[new](/list/cs.LG/new)
 | 
[recent](/list/cs.LG/recent)
 | [2026-06](/list/cs.LG/2026-06)

Change to browse by:

[cs](/abs/2606.04032?context=cs)  
[cs.AI](/abs/2606.04032?context=cs.AI)  
[cs.CL](/abs/2606.04032?context=cs.CL)  
[cs.PF](/abs/2606.04032?context=cs.PF)

### References & Citations

* [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2606.04032)
* [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2606.04032)
* [Semantic Scholar](https://api.semanticscholar.org/arXiv:2606.04032)

export BibTeX citation
Loading...

BibTeX formatted citation
-------------------------

×

loading...

Data provided by:

### Bookmark

[![BibSonomy](/static/browse/0.3.4/images/icons/social/bibsonomy.png)](http://www.bibsonomy.org/BibtexHandler?requTask=upload&url=https://arxiv.org/abs/2606.04032&description=Do Transformers Need Three Projections? Systematic Study of QKV Variants "Bookmark on BibSonomy")
[![Reddit](/static/browse/0.3.4/images/icons/social/reddit.png)](https://reddit.com/submit?url=https://arxiv.org/abs/2606.04032&title=Do Transformers Need Three Projections? Systematic Study of QKV Variants "Bookmark on Reddit")



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

IArxiv recommender toggle

IArxiv Recommender
*([What is IArxiv?](https://iarxiv.org/about))*

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

[Which authors of this paper are endorsers?](/auth/show-endorsers/2606.04032) |
[Disable MathJax](javascript:setMathjaxCookie()) ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))
