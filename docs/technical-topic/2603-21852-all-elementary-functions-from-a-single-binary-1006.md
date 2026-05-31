---
id: 1006
url: https://arxiv.org/abs/2603.21852
title: '[2603.21852] All elementary functions from a single binary operator'
domain: arxiv.org
source_date: '2026-04-13'
tags:
- academic-paper
- ai
summary: A researcher discovered a single binary operator, eml(x,y) = exp(x) - ln(y),
  that can generate all elementary mathematical functions—including trigonometric,
  logarithmic, exponential, and arithmetic operations—comparable to how a single logic
  gate suffices for all Boolean logic in computers. The operator, found through exhaustive
  computational search, creates a uniform binary tree structure that enables both
  the symbolic representation of any scientific calculator function and the recovery
  of exact closed-form equations from numerical data using gradient-based optimization.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# [2603.21852] All elementary functions from a single binary operator

Computer Science > Symbolic Computation
=======================================

**arXiv:2603.21852** (cs)

[Submitted on 23 Mar 2026 ([v1](https://arxiv.org/abs/2603.21852v1)), last revised 4 Apr 2026 (this version, v2)]

Title:All elementary functions from a single binary operator
============================================================

Authors:[Andrzej Odrzywołek](https://arxiv.org/search/cs?searchtype=author&query=Odrzywo%C5%82ek,+A)

View a PDF of the paper titled All elementary functions from a single binary operator, by Andrzej Odrzywo{\l}ek

[View PDF](/pdf/2603.21852)
[HTML (experimental)](https://arxiv.org/html/2603.21852v2)
> Abstract:A single two-input gate suffices for all of Boolean logic in digital hardware. No comparable primitive has been known for continuous mathematics: computing elementary functions such as sin, cos, sqrt, and log has always required multiple distinct operations. Here I show that a single binary operator, eml(x,y)=exp(x)-ln(y), together with the constant 1, generates the standard repertoire of a scientific calculator. This includes constants such as e, pi, and i; arithmetic operations including addition, subtraction, multiplication, division, and exponentiation as well as the usual transcendental and algebraic functions. For example, exp(x)=eml(x,1), ln(x)=eml(1,eml(eml(1,x),1)), and likewise for all other operations. That such an operator exists was not anticipated; I found it by systematic exhaustive search and established constructively that it suffices for the concrete scientific-calculator basis. In EML (Exp-Minus-Log) form, every such expression becomes a binary tree of identical nodes, yielding a grammar as simple as S -> 1 | eml(S,S). This uniform structure also enables gradient-based symbolic regression: using EML trees as trainable circuits with standard optimizers (Adam), I demonstrate the feasibility of exact recovery of closed-form elementary functions from numerical data at shallow tree depths up to 4. The same architecture can fit arbitrary data, but when the generating law is elementary, it may recover the exact formula.

|  |  |
| --- | --- |
| Comments: | 2 figures, Supplementary Information, code available at [this https URL](https://zenodo.org/records/19183008) |
| Subjects: | Symbolic Computation (cs.SC); Machine Learning (cs.LG) |
| MSC classes: | 26A09 (Primary) 08A40, 68W30 (Secondary) |
| ACM classes: | I.1.1; F.1.1 |
| Cite as: | [arXiv:2603.21852](https://arxiv.org/abs/2603.21852) [cs.SC] |
|  | (or  [arXiv:2603.21852v2](https://arxiv.org/abs/2603.21852v2) [cs.SC] for this version) |
|  | <https://doi.org/10.48550/arXiv.2603.21852> Focus to learn more  arXiv-issued DOI via DataCite |

Submission history
------------------

From: Andrzej Odrzywolek [[view email](/show-email/a915ff5b/2603.21852)]   
 **[[v1]](/abs/2603.21852v1)**
Mon, 23 Mar 2026 11:40:24 UTC (1,393 KB)  
**[v2]**
Sat, 4 Apr 2026 06:31:05 UTC (1,245 KB)

Full-text links:

Access Paper:
-------------

View a PDF of the paper titled All elementary functions from a single binary operator, by Andrzej Odrzywo{\l}ek

* [View PDF](/pdf/2603.21852)
* [HTML (experimental)](https://arxiv.org/html/2603.21852v2)
* [TeX Source](/src/2603.21852)

[![license icon](https://arxiv.org/icons/licenses/by-4.0.png)
view license](http://creativecommons.org/licenses/by/4.0/ "Rights to this article")

Ancillary-file links:

Ancillary files ([details](/src/2603.21852v2/anc)):
---------------------------------------------------

* [SupplementaryInformation.pdf](/src/2603.21852v2/anc/SupplementaryInformation.pdf)

### Current browse context:

cs.SC

[< prev](/prevnext?id=2603.21852&function=prev&context=cs.SC "previous in cs.SC (accesskey p)")
  |   
[next >](/prevnext?id=2603.21852&function=next&context=cs.SC "next in cs.SC (accesskey n)")

[new](/list/cs.SC/new)
 | 
[recent](/list/cs.SC/recent)
 | [2026-03](/list/cs.SC/2026-03)

Change to browse by:

[cs](/abs/2603.21852?context=cs)  
[cs.LG](/abs/2603.21852?context=cs.LG)

### References & Citations

* [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2603.21852)
* [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2603.21852)
* [Semantic Scholar](https://api.semanticscholar.org/arXiv:2603.21852)

export BibTeX citation
Loading...

BibTeX formatted citation
-------------------------

×

loading...

Data provided by:

### Bookmark

[![BibSonomy](/static/browse/0.3.4/images/icons/social/bibsonomy.png)](http://www.bibsonomy.org/BibtexHandler?requTask=upload&url=https://arxiv.org/abs/2603.21852&description=All elementary functions from a single binary operator "Bookmark on BibSonomy")
[![Reddit](/static/browse/0.3.4/images/icons/social/reddit.png)](https://reddit.com/submit?url=https://arxiv.org/abs/2603.21852&title=All elementary functions from a single binary operator "Bookmark on Reddit")



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

[Which authors of this paper are endorsers?](/auth/show-endorsers/2603.21852) |
[Disable MathJax](javascript:setMathjaxCookie()) ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))
