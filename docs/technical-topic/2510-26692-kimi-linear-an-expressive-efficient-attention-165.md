---
id: 165
url: https://arxiv.org/abs/2510.26692
title: '[2510.26692] Kimi Linear: An Expressive, Efficient Attention Architecture'
domain: arxiv.org
source_date: '2025-11-03'
tags:
- academic-paper
- llm
- ai
summary: Kimi Linear introduces a hybrid linear attention architecture that, for the
  first time, outperforms full attention mechanisms across various scenarios including
  short-context, long-context, and reinforcement learning tasks. The architecture
  combines Kimi Delta Attention (KDA)—an expressive linear attention module—with Multi-Head
  Latent Attention (MLA), achieving up to 75% reduction in KV cache usage and 6x faster
  decoding throughput while maintaining superior performance. The researchers have
  open-sourced the implementation and released pre-trained model checkpoints, positioning
  Kimi Linear as a practical drop-in replacement for traditional attention architectures.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# [2510.26692] Kimi Linear: An Expressive, Efficient Attention Architecture

Computer Science > Computation and Language
===========================================

**arXiv:2510.26692** (cs)

[Submitted on 30 Oct 2025 ([v1](https://arxiv.org/abs/2510.26692v1)), last revised 1 Nov 2025 (this version, v2)]

Title:Kimi Linear: An Expressive, Efficient Attention Architecture
==================================================================

Authors:[Kimi Team](https://arxiv.org/search/cs?searchtype=author&query=Kimi+Team): [Yu Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+Y), [Zongyu Lin](https://arxiv.org/search/cs?searchtype=author&query=Lin,+Z), [Xingcheng Yao](https://arxiv.org/search/cs?searchtype=author&query=Yao,+X), [Jiaxi Hu](https://arxiv.org/search/cs?searchtype=author&query=Hu,+J), [Fanqing Meng](https://arxiv.org/search/cs?searchtype=author&query=Meng,+F), [Chengyin Liu](https://arxiv.org/search/cs?searchtype=author&query=Liu,+C), [Xin Men](https://arxiv.org/search/cs?searchtype=author&query=Men,+X), [Songlin Yang](https://arxiv.org/search/cs?searchtype=author&query=Yang,+S), [Zhiyuan Li](https://arxiv.org/search/cs?searchtype=author&query=Li,+Z), [Wentao Li](https://arxiv.org/search/cs?searchtype=author&query=Li,+W), [Enzhe Lu](https://arxiv.org/search/cs?searchtype=author&query=Lu,+E), [Weizhou Liu](https://arxiv.org/search/cs?searchtype=author&query=Liu,+W), [Yanru Chen](https://arxiv.org/search/cs?searchtype=author&query=Chen,+Y), [Weixin Xu](https://arxiv.org/search/cs?searchtype=author&query=Xu,+W), [Longhui Yu](https://arxiv.org/search/cs?searchtype=author&query=Yu,+L), [Yejie Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+Y), [Yu Fan](https://arxiv.org/search/cs?searchtype=author&query=Fan,+Y), [Longguang Zhong](https://arxiv.org/search/cs?searchtype=author&query=Zhong,+L), [Enming Yuan](https://arxiv.org/search/cs?searchtype=author&query=Yuan,+E), [Dehao Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+D), [Yizhi Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+Y), [T.Y. Liu](https://arxiv.org/search/cs?searchtype=author&query=Liu,+T), [Haiming Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+H), [Shengjun Fang](https://arxiv.org/search/cs?searchtype=author&query=Fang,+S), [Weiran He](https://arxiv.org/search/cs?searchtype=author&query=He,+W), [Shaowei Liu](https://arxiv.org/search/cs?searchtype=author&query=Liu,+S), [Yiwei Li](https://arxiv.org/search/cs?searchtype=author&query=Li,+Y), [Jianlin Su](https://arxiv.org/search/cs?searchtype=author&query=Su,+J), [Jiezhong Qiu](https://arxiv.org/search/cs?searchtype=author&query=Qiu,+J), [Bo Pang](https://arxiv.org/search/cs?searchtype=author&query=Pang,+B), [Junjie Yan](https://arxiv.org/search/cs?searchtype=author&query=Yan,+J), [Zhejun Jiang](https://arxiv.org/search/cs?searchtype=author&query=Jiang,+Z), [Weixiao Huang](https://arxiv.org/search/cs?searchtype=author&query=Huang,+W), [Bohong Yin](https://arxiv.org/search/cs?searchtype=author&query=Yin,+B), [Jiacheng You](https://arxiv.org/search/cs?searchtype=author&query=You,+J), [Chu Wei](https://arxiv.org/search/cs?searchtype=author&query=Wei,+C), [Zhengtao Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+Z), [Chao Hong](https://arxiv.org/search/cs?searchtype=author&query=Hong,+C), [Yutian Chen](https://arxiv.org/search/cs?searchtype=author&query=Chen,+Y), [Guanduo Chen](https://arxiv.org/search/cs?searchtype=author&query=Chen,+G), [Yucheng Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+Y), [Huabin Zheng](https://arxiv.org/search/cs?searchtype=author&query=Zheng,+H), [Feng Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+F), [Yibo Liu](https://arxiv.org/search/cs?searchtype=author&query=Liu,+Y), [Mengnan Dong](https://arxiv.org/search/cs?searchtype=author&query=Dong,+M), [Zheng Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+Z), [Siyuan Pan](https://arxiv.org/search/cs?searchtype=author&query=Pan,+S), [Wenhao Wu](https://arxiv.org/search/cs?searchtype=author&query=Wu,+W), [Yuhao Wu](https://arxiv.org/search/cs?searchtype=author&query=Wu,+Y), [Longyu Guan](https://arxiv.org/search/cs?searchtype=author&query=Guan,+L), [Jiawen Tao](https://arxiv.org/search/cs?searchtype=author&query=Tao,+J), [Guohong Fu](https://arxiv.org/search/cs?searchtype=author&query=Fu,+G), [Xinran Xu](https://arxiv.org/search/cs?searchtype=author&query=Xu,+X), [Yuzhi Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+Y), [Guokun Lai](https://arxiv.org/search/cs?searchtype=author&query=Lai,+G), [Yuxin Wu](https://arxiv.org/search/cs?searchtype=author&query=Wu,+Y), [Xinyu Zhou](https://arxiv.org/search/cs?searchtype=author&query=Zhou,+X), [Zhilin Yang](https://arxiv.org/search/cs?searchtype=author&query=Yang,+Z), [Yulun Du](https://arxiv.org/search/cs?searchtype=author&query=Du,+Y)

View a PDF of the paper titled Kimi Linear: An Expressive, Efficient Attention Architecture, by Kimi Team: Yu Zhang and 58 other authors

[View PDF](/pdf/2510.26692)
> Abstract:We introduce Kimi Linear, a hybrid linear attention architecture that, for the first time, outperforms full attention under fair comparisons across various scenarios -- including short-context, long-context, and reinforcement learning (RL) scaling regimes. At its core lies Kimi Delta Attention (KDA), an expressive linear attention module that extends Gated DeltaNet with a finer-grained gating mechanism, enabling more effective use of limited finite-state RNN memory. Our bespoke chunkwise algorithm achieves high hardware efficiency through a specialized variant of the Diagonal-Plus-Low-Rank (DPLR) transition matrices, which substantially reduces computation compared to the general DPLR formulation while remaining more consistent with the classical delta rule.
>   
> We pretrain a Kimi Linear model with 3B activated parameters and 48B total parameters, based on a layerwise hybrid of KDA and Multi-Head Latent Attention (MLA). Our experiments show that with an identical training recipe, Kimi Linear outperforms full MLA with a sizeable margin across all evaluated tasks, while reducing KV cache usage by up to 75% and achieving up to 6 times decoding throughput for a 1M context. These results demonstrate that Kimi Linear can be a drop-in replacement for full attention architectures with superior performance and efficiency, including tasks with longer input and output lengths.
>   
> To support further research, we open-source the KDA kernel and vLLM implementations, and release the pre-trained and instruction-tuned model checkpoints.

|  |  |
| --- | --- |
| Comments: | Kimi Linear tech report |
| Subjects: | Computation and Language (cs.CL); Machine Learning (cs.LG) |
| Cite as: | [arXiv:2510.26692](https://arxiv.org/abs/2510.26692) [cs.CL] |
|  | (or  [arXiv:2510.26692v2](https://arxiv.org/abs/2510.26692v2) [cs.CL] for this version) |
|  | <https://doi.org/10.48550/arXiv.2510.26692> Focus to learn more  arXiv-issued DOI via DataCite |

Submission history
------------------

From: Yulun Du [[view email](/show-email/19b5afec/2510.26692)]   
 **[[v1]](/abs/2510.26692v1)**
Thu, 30 Oct 2025 16:59:43 UTC (645 KB)  
**[v2]**
Sat, 1 Nov 2025 12:05:18 UTC (691 KB)

Full-text links:

Access Paper:
-------------

View a PDF of the paper titled Kimi Linear: An Expressive, Efficient Attention Architecture, by Kimi Team: Yu Zhang and 58 other authors

* [View PDF](/pdf/2510.26692)
* [TeX Source](/src/2510.26692)

[![license icon](https://arxiv.org/icons/licenses/by-nc-nd-4.0.png)
view license](http://creativecommons.org/licenses/by-nc-nd/4.0/ "Rights to this article")

### Current browse context:

cs.CL

[< prev](/prevnext?id=2510.26692&function=prev&context=cs.CL "previous in cs.CL (accesskey p)")
  |   
[next >](/prevnext?id=2510.26692&function=next&context=cs.CL "next in cs.CL (accesskey n)")

[new](/list/cs.CL/new)
 | 
[recent](/list/cs.CL/recent)
 | [2025-10](/list/cs.CL/2025-10)

Change to browse by:

[cs](/abs/2510.26692?context=cs)  
[cs.LG](/abs/2510.26692?context=cs.LG)

### References & Citations

* [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2510.26692)
* [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2510.26692)
* [Semantic Scholar](https://api.semanticscholar.org/arXiv:2510.26692)

export BibTeX citation
Loading...

BibTeX formatted citation
-------------------------

×

loading...

Data provided by:

### Bookmark

[![BibSonomy](/static/browse/0.3.4/images/icons/social/bibsonomy.png)](http://www.bibsonomy.org/BibtexHandler?requTask=upload&url=https://arxiv.org/abs/2510.26692&description=Kimi Linear: An Expressive, Efficient Attention Architecture "Bookmark on BibSonomy")
[![Reddit](/static/browse/0.3.4/images/icons/social/reddit.png)](https://reddit.com/submit?url=https://arxiv.org/abs/2510.26692&title=Kimi Linear: An Expressive, Efficient Attention Architecture "Bookmark on Reddit")



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

[Which authors of this paper are endorsers?](/auth/show-endorsers/2510.26692) |
[Disable MathJax](javascript:setMathjaxCookie()) ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))
