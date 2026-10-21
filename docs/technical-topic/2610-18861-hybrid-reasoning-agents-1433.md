---
id: 1433
url: https://arxiv.org/abs/2610.18861
title: '[2610.18861] Hybrid Reasoning Agents'
domain: arxiv.org
source_date: '2026-10-19'
tags:
- llm
- ai
- academic-paper
summary: The paper introduces Hybrid Reasoning Agents (HybridAgents), which dynamically
  switch between latent-space reasoning and text-based interaction within a unified
  generation process, using a lightweight HybridLink module and a continuous working
  memory to keep context lossless across turns. The authors train the system with
  HybridSFT and HybridRL post-training methods, which teach the model to coordinate
  with HybridLink and to decide when to think latently versus act through text. Across
  11 benchmarks at three model scales, HybridAgents reportedly improves performance
  by 10.4% over frontier LLM agents while cutting token usage by 35.5%-54.7%, speeding
  inference 1.8x-2.6x, and lowering cost 2.7x-3.7x.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-5-5
---

# [2610.18861] Hybrid Reasoning Agents

Computer Science > Computation and Language
===========================================

**arXiv:2610.18861** (cs)

[Submitted on 13 Oct 2026]

Title:Hybrid Reasoning Agents
=============================

Authors:[Jiaru Zou](https://arxiv.org/search/cs?searchtype=author&query=Zou,+J), [Yunzhe Qi](https://arxiv.org/search/cs?searchtype=author&query=Qi,+Y), [Sirui Chen](https://arxiv.org/search/cs?searchtype=author&query=Chen,+S), [Federico Bianchi](https://arxiv.org/search/cs?searchtype=author&query=Bianchi,+F), [Shang Zhu](https://arxiv.org/search/cs?searchtype=author&query=Zhu,+S), [Pan Lu](https://arxiv.org/search/cs?searchtype=author&query=Lu,+P), [Jingrui He](https://arxiv.org/search/cs?searchtype=author&query=He,+J), [James Zou](https://arxiv.org/search/cs?searchtype=author&query=Zou,+J)

View a PDF of the paper titled Hybrid Reasoning Agents, by Jiaru Zou and 7 other authors

[View PDF](/pdf/2610.18861)
[HTML (experimental)](https://arxiv.org/html/2610.18861v1)
> Abstract:How can we build an agent that thinks beyond human language, yet still acts through it in the external environment? Modern LLM agents still reason and interact through text, while latent reasoning offers an efficient internal medium but lacks native tool access and reasoning transparency. We bridge these two directions with Hybrid Reasoning Agents (HybridAgents), which dynamically navigate between latent reasoning and text-based interaction throughout a unified generation process. Architecturally, a lightweight HybridLink enables seamless transitions between text and latent modes, while the agent's continuous working memory preserves lossless hybrid context across multiple turns. These designs preserve tool-integrated agentic capabilities while making latent thoughts directly inspectable. Building on this architecture, we further develop dedicated post-training algorithms for hybrid reasoning: HybridSFT stabilizes tool-integrated hybrid generation by teaching the backbone to coordinate with HybridLink, then HybridRL scales reasoning by learning when to think in latent space and when to act through text. We evaluate HybridAgent at 3 model scales across 11 benchmarks covering mathematics, science, medicine, search, and agentic reasoning. Compared with frontier LLM Agents and agentic frameworks spanning both text-based and latent methods, HybridAgent consistently improves performance by 10.4%, while delivering 35.5%-54.7% token reduction, 1.8x-2.6x faster inference, and 2.7x-3.7x cost savings. Code and data are available at [this https URL](https://github.com/togethercomputer/HybridAgent).

|  |  |
| --- | --- |
| Comments: | 45 pages, 12 figures |
| Subjects: | Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Machine Learning (cs.LG) |
| Cite as: | [arXiv:2610.18861](https://arxiv.org/abs/2610.18861) [cs.CL] |
|  | (or  [arXiv:2610.18861v1](https://arxiv.org/abs/2610.18861v1) [cs.CL] for this version) |
|  | <https://doi.org/10.48550/arXiv.2610.18861> Focus to learn more  arXiv-issued DOI via DataCite |

Submission history
------------------

From: Jiaru Zou [[view email](/show-email/d71dd478/2610.18861)]   
 **[v1]**
Tue, 13 Oct 2026 17:59:31 UTC (8,500 KB)

Full-text links:

Access Paper:
-------------

View a PDF of the paper titled Hybrid Reasoning Agents, by Jiaru Zou and 7 other authors

* [View PDF](/pdf/2610.18861)
* [HTML (experimental)](https://arxiv.org/html/2610.18861v1)
* [TeX Source](/src/2610.18861)

[![license icon](https://arxiv.org/icons/licenses/by-4.0.png)
view license](http://creativecommons.org/licenses/by/4.0/ "Rights to this article")

### Additional Features

* [Audio Summary](/audio/2610.18861)

### Current browse context:

cs.CL

[< prev](/prevnext?id=2610.18861&function=prev&context=cs.CL "previous in cs.CL (accesskey p)")
  |   
[next >](/prevnext?id=2610.18861&function=next&context=cs.CL "next in cs.CL (accesskey n)")

[new](/list/cs.CL/new)
 | 
[recent](/list/cs.CL/recent)
 | [2026-10](/list/cs.CL/2026-10)

Change to browse by:

[cs](/abs/2610.18861?context=cs)  
[cs.AI](/abs/2610.18861?context=cs.AI)  
[cs.LG](/abs/2610.18861?context=cs.LG)

### References & Citations

* [SciX](https://scixplorer.org/abs/arXiv:2610.18861)
* [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2610.18861)
* [Semantic Scholar](https://api.semanticscholar.org/arXiv:2610.18861)

export BibTeX citation
Loading...

BibTeX formatted citation
-------------------------

×

loading...

Data provided by:

### Bookmark

[![BibSonomy](/static/browse/0.3.4/images/icons/social/bibsonomy.png)](http://www.bibsonomy.org/BibtexHandler?requTask=upload&url=https://arxiv.org/abs/2610.18861&description=Hybrid Reasoning Agents "Bookmark on BibSonomy")
[![Reddit](/static/browse/0.3.4/images/icons/social/reddit.png)](https://reddit.com/submit?url=https://arxiv.org/abs/2610.18861&title=Hybrid Reasoning Agents "Bookmark on Reddit")



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

[Which authors of this paper are endorsers?](/auth/show-endorsers/2610.18861) |
[Disable MathJax](javascript:setMathjaxCookie()) ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))
