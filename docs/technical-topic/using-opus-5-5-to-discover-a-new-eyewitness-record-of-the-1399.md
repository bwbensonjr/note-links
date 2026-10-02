---
id: 1399
url: https://resobscura.substack.com/p/using-opus-55-to-discover-a-new-eyewitness
title: Using Opus 5.5 to discover a new eyewitness record of the dodo
domain: resobscura.substack.com
source_date: '2026-10-02'
tags:
- llm
- academic-paper
summary: Researchers used AI model Opus 5.5 to discover a previously unnoticed 1615
  Dutch ship's log recording the hunting of dodos on Mauritius, filling a gap in the
  historical record of the extinct bird. The AI employed semantic search through the
  Dutch East India Company archives to identify relevant manuscript passages, demonstrating
  how frontier AI models can now conduct novel historical research by processing large
  volumes of primary sources across multiple languages. The findings also suggest
  a possible connection between a dodo described by a Portuguese Jesuit in 1616 and
  the mysterious dodo that appeared in a 17th-century Mughal Emperor's painting, potentially
  explaining the bird's unexplained presence in India.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Using Opus 5.5 to discover a new eyewitness record of the dodo

Using Opus 5.5 to discover a new eyewitness record of the dodo
==============================================================

### Frontier models can now produce novel historical knowledge, but in a really weird way

[![Benjamin Breen's avatar](https://substackcdn.com/image/fetch/$s_!xsR1!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F257d3bc5-9101-4f5c-a0ac-ce55ca30dbfa_1140x1155.jpeg)](https://substack.com/@benjaminbreen)

[Benjamin Breen](https://substack.com/@benjaminbreen)

Oct 01, 2026

18

12

2

Share

Another day, another historical cipher broken by a frontier model. Yesterday, the security researcher Carter Church [announced](https://x.com/CarterWChurch/status/2105167567706816690) that he had used GPT-6 Astra (working on the problem for six hours) to break a Napoleonic-era cipher that had previously resisted all decryption attempts.

Church’s [post](https://carter.church/writeups/the-letter-to-marmont/) on the subject is an interesting example not just of a reproducible methodology, but also of how to vibe code an information-dense writeup that is notably different from any traditional academic aesthetic, but which actually does surface primary sources and meaningful information in a fairly deep way:

[![](https://substackcdn.com/image/fetch/$s_!pGu3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff48dd1fa-511e-473d-a31c-b81df68e3654_1754x748.png)](https://substackcdn.com/image/fetch/$s_!pGu3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff48dd1fa-511e-473d-a31c-b81df68e3654_1754x748.png)

The aesthetic weirdness is just the tip of the iceberg here. What I notice most about these forays into historical sleuthing using AI (and my own attempts at same) is the ***epistemological weirdness*** of how current frontier models now operate when given historical research tasks.

The best way to demonstrate what I mean here is by sharing the step-by-step process by which I was able to find what appears to be a **previously-unnoticed Dutch report of hunting dodos** dating to 1615. The core steps were:

1. Start from an actual base of specialist knowledge to define a **specific research question** (for example, I had [previously researched](https://resobscura.blogspot.com/2011/02/jahangirs-turkey-early-modern.html) the history of the exotic animal trade in the seventeenth century, and am planning to write a book on animal extinctions in the early modern period which will have a dodo chapter)
2. Identify a large, freely-available, well-edited corpus of historical sources (in this case, the [GLOBALISE archive](https://globalise.huygens.knaw.nl) of Dutch East India Company archives, which is an amazing resource)
3. Download the sources and run them through an embedding model to allow semantic search to find passages that might help answer the research question
4. Use semantic search to surface candidate passages and then ask frontier models to read them and produce a ranked list of the best matches for human review
5. Do any of the source passages help answer the question? If so, iterate on them. If not, keep looking in new archives or with new search terms.

This is not, on its face, all *that* different from how I do research on my own. I tend to search around in historical databases using various search terms that pop into my head, and then scan through the results until a passage catches my interest, then I read more carefully and iterate.

The difference is that an AI agent like Opus 5.5 can spawn dozens of copies of itself to read through sources in multiple languages. If you give these agents an API key, they can also run their own embedding searches on new sources that emerge during their research, as Opus did here during the run that led it to the newly-discovered passage:

[![](https://substackcdn.com/image/fetch/$s_!Movy!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2bbdd8c-62d7-4ad5-a139-480b60451c59_1738x702.png)](https://substackcdn.com/image/fetch/$s_!Movy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2bbdd8c-62d7-4ad5-a139-480b60451c59_1738x702.png)

So what is that dodo passage and why does it matter?

A dodo in a haystack
--------------------

Few historical creatures have been more widely studied than the dodo, the large Mauritius bird that famously went extinct due to overhunting around 1681. But this is actually a large part of why finding *more* information about the animal turned out to be “[tractable](https://resobscura.substack.com/p/ai-labs-need-to-start-funding-historical)” for an AI agent: it already had a very large identified source base to draw on, and it was able to scan the scholarly literature to find out where previous archival finds relating to dodos had been made (here is Opus 5.5 [writing up its own process in a research dossier](https://claude.ai/artifact/4nLg6iQE1154NEz1thp2MU)).

Most of what Opus 5.5 found as it searched through the millions of records in the Dutch East India Company records was already known to the many historians and scientists who have studied the history of the dodo. But one manuscript source from 1615, a ship’s log available [here](https://www.nationaalarchief.nl/onderzoeken/archief/1.04.02/invnr/1059/file/NL-HaNA_1.04.02_1059_0277), seems not to have been noticed before.

The journal was probably written by Isbrant Cornelisz van Petten, who captained a Dutch East India Company merchant vessel called *Wapen van Amsterdam*. The *Wapen* made landfall on the island of Mauritius in April, 1615, where the crew collected water and food to prepare for the rest of their voyage to the East Indies.

Among other things, they “caught many tortoises, dodos [*dodeersen*], and some geese and parrots.”

[![User attachment](https://substackcdn.com/image/fetch/$s_!o2z1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7689db62-fd80-48f1-b660-8588670b437b_2864x322.png "User attachment")](https://substackcdn.com/image/fetch/$s_!o2z1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7689db62-fd80-48f1-b660-8588670b437b_2864x322.png)

A detail from Nationaal Archief, The Hague, VOC 1.04.02, inv. 1059, fol. 141. “dodersen” (dodos) is visible at lower left here.

Here is the Dutch transcription and English translation of the relevant passages (note that the transcription and translation are not perfect — if you work on early modern Dutch please let me know of any corrections!):

[![](https://substackcdn.com/image/fetch/$s_!LMyM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa9af7e67-052f-4411-a625-e290bd9655a6_1494x632.png)](https://substackcdn.com/image/fetch/$s_!LMyM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa9af7e67-052f-4411-a625-e290bd9655a6_1494x632.png)

I read through the available secondary literature on the topic, like Parrish’s 2013 book *[The Dodo and the Solitaire](https://www.google.com/books/edition/The_Dodo_and_the_Solitaire/k5mgPMHqTt8C?hl=en)*, and other specialist articles. It genuinely looks like this is a new addition to the timeline of dodo, which previously had a gap in the 1611-16 period.

Now, as for whether this actually matters all that much: it not exactly earth-shattering. But I do think that this is a publishable result, especially when combined with another new finding from the same search, which found a probable new reference to *another* extinct bird from Mauritius, the [red rail](https://en.wikipedia.org/wiki/Red_rail). An account from 1638, the year the Dutch first colonized the island, turns out to describe “field-hens” using the Dutch word (*velthoenderen*). Experts on the topic have previously identified this word as one that the Dutch used to describe red rails. But this particular reference was apparently missed because a French scholar in 1890 mistranslated the word as *perdrix (*partridges).

[![](https://substackcdn.com/image/fetch/$s_!K7RS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fac7f45b3-4e50-4d87-9d3a-5ee995f0ff52_1924x532.png)](https://substackcdn.com/image/fetch/$s_!K7RS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fac7f45b3-4e50-4d87-9d3a-5ee995f0ff52_1924x532.png)

From the writeup [here](https://claude.ai/artifact/4nLg6iQE1154NEz1thp2MU).

Opus 5.5 was able to go back to the original manuscript source and correct this.

For me, though, the most interesting *possible* finding is still very much in doubt. But if it can be nailed down, it really would be quite fascinating. This is because it might help explain one of the most mysterious paintings from the 17th century: the [Mughal Emperor Jahangir](https://en.wikipedia.org/wiki/Jahangir) apparently owned a living dodo. However, no one knows who gave it to him, when, or why, and Jahangir never writes anything about it in his [memoirs](https://en.wikipedia.org/wiki/Tuzk-e-Jahangiri).

[![](https://substackcdn.com/image/fetch/$s_!m5zR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe2436883-8d77-4a69-bca7-d0b1ec95a226_966x1553.jpeg)](https://substackcdn.com/image/fetch/$s_!m5zR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe2436883-8d77-4a69-bca7-d0b1ec95a226_966x1553.jpeg)

Ustad Mansur, Institute for Eastern Studies, Novo-Mikhailovsky Palace, Saint Petersburg ([Wikipedia link](https://en.wikipedia.org/wiki/Dodo#/media/File:DodoMansur.jpg))

I actually [wrote about this painting back in 2012](https://resobscura.blogspot.com/2011/02/jahangirs-turkey-early-modern.html):

> Two years earlier Mansur had painted a Mauritian dodo that is still cited by biologists as the most accurate surviving representation of the bird. In other words, Jahangir was *exactly* who a canny merchant or courtier would go to if they came across a highly unusual-looking bird.

It turns out that no one really knows the exact date of this painting. Some scholars go with “circa 1625,” others with “circa 1615.” (We do know that an English merchant reported the existence of Mauritian dodos in India in 1628, but whether this included the dodo shown in the painting is unknowable).

To my great surprise, Opus 5.5 dug around in a very wide range of manuscripts to surface the following theory: Jahangir’s dodo was quite possibly the same animal that a Portuguese Jesuit described on Mauritius in 1616. The Jesuit referred to this Mauritian bird as an “ostrich.” The thing is, Mauritius *has* no ostriches!

Unfortunately, the original Portuguese text of this account is now thought to be lost, but a [French translation](https://www.google.com/books/edition/Collection_des_ouvrages_anciens_concerna/Ry6gAAAAMAAJ?hl=en&gbpv=1&dq=gross+qu+un+dindon+ordinaire&pg=PA117&printsec=frontcover) survives, and that’s what Opus is citing here:

[![](https://substackcdn.com/image/fetch/$s_!DMzW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fda6b4c3e-1b63-48f3-bda6-47eaf3a77598_1980x684.png)](https://substackcdn.com/image/fetch/$s_!DMzW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fda6b4c3e-1b63-48f3-bda6-47eaf3a77598_1980x684.png)

The theory that this “ostrich” was actually a dodo is already known to experts on the topic, and the French translator glosses it as such. But it appears that the connection between this Portuguese dodo caught en route to Goa in 1616 and the dodo that ended up reaching Jahangir at some point between 1615 and 1625 has not yet been made.

Granted, the chain of transmission has not been established. But my hunch is that this may in fact be the origin of Jahangir’s dodo. This is because we happen to already have a very clear chain of transmission of *another* exotic bird from the Portuguese based in Goa to Jahangir’s court, dating to 1612: an American turkey!

[![](https://substackcdn.com/image/fetch/$s_!zpZU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6e48cb55-82bb-4a52-b88b-ba12e91b6e63_1812x1762.png)](https://substackcdn.com/image/fetch/$s_!zpZU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6e48cb55-82bb-4a52-b88b-ba12e91b6e63_1812x1762.png)

This is something I plan to dig into more. If it can be traced more reliably, I think the identification of Jahangir’s dodo would be a pretty big deal. The Mughal court dodo is possibly the most famous and scientifically important individual dodo that ever lived, because Jahangir’s brilliant court painter, Ustad Mansur, left behind the most accurate surviving depiction of it.

At minimum, I can say that this deep dive into the Dutch records has made it clear to me that frontier AI models are capable of surfacing new historical finds based on independent archival sleuthing. That’s not something I could have said months ago.

What they can’t currently do is ask the right questions or determine the significance of finds.

[Share](https://resobscura.substack.com/p/using-opus-55-to-discover-a-new-eyewitness?utm_source=substack&utm_medium=email&utm_content=share&action=share)

Epistemological weirdness
-------------------------

**The main thing that contemporary AI can do for historical research is, in effect, the digital equivalent of counting sheep. Because they never get bored, they can search through enormous datasets to find new evidence for existing claims (or, potentially, disprove them).**

They are worse at coming up with new ideas of their own. What seems to work best is if they are placed on the boundary between two disciplines, given a source base, and told to work methodically toward answering a *human-generated question*.

They are also notably bad at judging the historical significance of what they find.

Again and again, in my attempts to find something tractable, Opus 5.5 and GPT-6 ended up spawning up to a dozen independent agents that that drilled down into minutiae and got utterly lost in the weeds.

Sometimes, the weeds ended up being fun. For instance, one agent discovered a very entertaining and novel account of an English ship captain, Jonathan Hide, who stole valuable ebony wood plus “two sea cows” (!) from the Dutch colony in Mauritius. When a Dutch official confronted Hide and his crew, “their carpenter threatened to split my head with his axe.” The official adds:

> The Captain also took about 20 land tortoises on the voyage, **claiming he intended to put them ashore on St Helena, so as to breed the said tortoises there**.

This is historically significant as an environmental history finding. It turns out that the animal in question, the [Mauritius giant tortoise](https://en.wikipedia.org/wiki/Domed_Mauritius_giant_tortoise), *also* ended up going extinct. Whether these twenty individuals ever did end up on St. Helena, many thousands of miles away, is unknown. But we do know that Captain Hide’s ship sank near the Azores on the return voyage home.

This is a pretty great story! Early modern people transplanting crops and animals is very much in my wheelhouse, and I love the carpenter brandishing an axe at the Dutch official. I will likely use it in some of my published work at some point.

Most of the time, however, agents veered off into archives that are totally illegible to me and require very extensive specialist knowledge to fact check. For instance, this was the product of a multi-hour search into Inca [khipu](https://en.wikipedia.org/wiki/Quipu):

[![](https://substackcdn.com/image/fetch/$s_!oT1Z!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F440ac280-8cbb-4739-8aec-5f18dae43ead_1488x814.png)](https://substackcdn.com/image/fetch/$s_!oT1Z!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F440ac280-8cbb-4739-8aec-5f18dae43ead_1488x814.png)

*Is* that decisive? Does any of this mean anything? I genuinely have no idea. I assume [Gary Urton](https://en.wikipedia.org/wiki/Gary_Urton) does. But I don’t really want to bother someone who has dedicated his life to the study of Inca khipu with a question generated by an AI agent which spent a few hours on the same topic.

This is really the crux of the current problem in a number of fields that AI research agents stand poised to transform: *how should human experts interface with these things?*

I feel comfortable working with the material relating to, say, English merchants stealing giant tortoises, or Jahangir’s dodo, because this is the sort of stuff I’ve been studying for well over a decade now. But what happens when amateurs running AI research agents veer off into genuine new scholarly territory, without the knowledge or network to double check it?

This is what Carter Church gets at in the post I linked to at the top:

> A patient specialist could have done this in 1970. But it would have meant weeks of a specialist’s time: period French, a steady eye for 1,300 hand-drawn signs, and the statistics, all spent on one plate in one army journal. People with those skills exist, and they have more important problems to solve. So the letter sat unread, because no one who could read it could justify the time.
>
> I spent six hours of model time and a few evenings of my own. Tomokiyo says he’s receiving solutions faster than he can record them. I’m sure few of these are from cryptographers. A year ago that sentence probably wouldn’t have made sense.
>
> I’d guess most “unsolved” lists, in most fields, hold more problems like this than anyone assumes. Those lists are about to get a lot shorter, and the people shortening them will increasingly be people who were simply curious.

Personally, I would be thrilled if a bunch of curious amateurs running a small army of AI agents dug into the dodo material, or into the early modern drug trade, or the history of consciousness science in the 19th century, or any number of other things I’m actively researching. But it is going to get really weird, really soon, when these things happen.

The bottleneck will soon become not research findings themselves, but *the attention of experts in niche topics*.

A [guest post](https://terrytao.wordpress.com/2026/09/24/were-gonna-need-a-lot-more-mathematicians/) on mathematician Terrence Tao’s blog recently concluded: “We’re gonna need a lot more mathematicians.”

I agree, and I would add: we’re gonna need a lot more historians and humanists.

[![](https://substackcdn.com/image/fetch/$s_!ye1S!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8a7962ec-7ec3-467e-a61a-fb4e967cfc00_3000x241.png)](https://substackcdn.com/image/fetch/$s_!ye1S!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8a7962ec-7ec3-467e-a61a-fb4e967cfc00_3000x241.png)

Weekly links
============

• Why the Bronze Age collapsed ([Works in Progress](https://www.worksinprogress.news/p/why-really-caused-the-bronze-age))

• Who wrote Queen Elizabeth I’s most scathing letters? (*[Smithsonian](https://www.smithsonianmag.com/history/who-wrote-elizabeth-is-most-scathing-letters-new-research-suggests-the-tudor-queens-male-secretaries-revised-her-correspondence-to-emphasize-her-temper-180989565/)* - this is a great example of original historical analysis based on cross-comparison between manuscript sources).

• [More breakthroughs relating to the Herculaneum scrolls](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0353485).

---

Res Obscura is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

[Leave a comment](https://resobscura.substack.com/p/using-opus-55-to-discover-a-new-eyewitness/comments)

[Share](https://resobscura.substack.com/p/using-opus-55-to-discover-a-new-eyewitness?utm_source=substack&utm_medium=email&utm_content=share&action=share)

18

12

2

Share

Previous
