---
id: 145
url: https://generativehistory.substack.com/p/has-google-quietly-solved-two-of
title: Has Google Quietly Solved Two of AI’s Oldest Problems?
domain: generativehistory.substack.com
source_date: '2025-11-15'
tags:
- ai
- llm
- news
summary: Google appears to be testing a new AI model (possibly Gemini-3) through its
  AI Studio that demonstrates near-perfect handwriting recognition combined with sophisticated
  reasoning abilities—capabilities the author describes as solving two longstanding
  AI challenges. The model excels not just at transcribing historical handwritten
  documents at expert human levels, but also at contextual analysis and logical inference
  needed to decipher unclear or ambiguous text. If verified, this breakthrough could
  revolutionize fields requiring both visual precision and skilled reasoning, such
  as historical research and document analysis.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Has Google Quietly Solved Two of AI’s Oldest Problems?

Has Google Quietly Solved Two of AI’s Oldest Problems?
======================================================

### A mysterious new model currently in testing on Google’s AI Studio is nearly perfect on automated handwriting recognition but it is also showing signs of spontaneous, abstract, symbolic reasoning.

[![Mark Humphries's avatar](https://substackcdn.com/image/fetch/$s_!qX8g!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6a9d1f7c-ec5e-4a26-bff1-335bfd4da0aa_3088x2316.jpeg)](https://substack.com/@generativehistory)

[Mark Humphries](https://substack.com/@generativehistory)

Oct 17, 2025

219

43

23

Share

[![](https://substackcdn.com/image/fetch/$s_!00do!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3ee0e0e0-6d52-4155-b334-f12a53de85f8_1344x768.png)](https://substackcdn.com/image/fetch/$s_!00do!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3ee0e0e0-6d52-4155-b334-f12a53de85f8_1344x768.png)

Google has a webapp called [AI Studio](https://aistudio.google.com/) where people can experiment with prompts and models. In the last week, users have found that every once in awhile they will get two results and are asked to select the better one. The big AI labs typically do this type of A/B testing on new models just before they’re released, so speculation is rampant that this might be Gemini-3. Whatever it is, users have reported some truly wild things: it codes fully functioning [Windows and Apple OS clones](https://x.com/kimmonismus/status/1978038877286809833), 3D design software, Nintendo emulators, and productivity suites from single prompts.

Curious, I tried it out on transcribing some handwritten texts and the results were shocking: not only was the transcription very nearly perfect—at expert human levels—but it did a something else unexpected that can only be described as genuine, human-like, expert level reasoning. It is the most amazing thing I have seen an LLM do, and it was unprompted, entirely accidental.

What follows are my first impressions of this new model with all the requisite caveats that entails. But if my observations hold true, this will be a big deal when it’s released. We appear to be on the cusp of an era when AI models will not only start to read difficult handwritten historical documents just as well as expert humans but also analyze them in deep and nuanced ways. While this is important for historians, we need to extrapolate from this small example to think more broadly: if this holds the models are about to make similar leaps in any field where visual precision and skilled reasoning must work together required. As is so often the case with AI, that is exciting and frightening all at once. Even a few months ago, I thought this level of capability was still years away.

#### **A New Model**

[Rumours](https://currently.att.yahoo.com/att/someone-reportedly-used-gemini-3-134036264.html) started appearing on X a week ago that there was a new Gemini model in A/B testing in AI Studio. It’s always hard to know what these mean but I wanted to see how well this thing would do on handwritten historical documents because that has become my own personal benchmark. I am interested in LLM performance on handwriting for a couple of reasons. First, I am a historian so I intuitively see why fast, cheap, and accurate transcription would be [useful to me in my day-to-day work](https://generativehistory.substack.com/p/why-openais-new-model-might-change). But in trying to achieve that, and in learning about AI, I have come to believe that recognizing historical handwriting poses something of a unique challenge and a great overall test for LLM abilities in general. I also think it shines a small amount of light on the larger question of whether LLMs will [ultimately prove capable of expert human levels of reasoning](https://importai.substack.com/p/import-ai-431-technological-optimism) or [prove to be a dead end.](https://www.dwarkesh.com/p/richard-sutton) Let me explain.

Most people think that deciphering historical handwriting is a task that mainly requires vision. I agree that this is true, but only to a point. When you step back in time, you enter a different country, or so the saying goes. People talk differently, using unfamiliar words or familiar words in unfamiliar ways. People in the past used different systems of measurement and accounting, different turns of phrase, punctuation, capitalization, and spelling. Implied meanings were different as were assumptions about what readers would know.

While it can be easy to decipher most of the words in a historical text, without contextual knowledge about the topic and time period it’s nearly impossible to understand a document well-enough to accurately transcribe the whole thing—let alone to use it effectively. The irony is that some of the most crucial information in historical letters is also the most period specific and thus hardest to decipher.

Even beyond context awareness, though, [paleography](https://en.wikipedia.org/wiki/Palaeography) involves linking vision with reasoning to make logical inferences: we use known words and thus known letters to identify uncertain letters. As we shall see, documents very often become logic puzzles and LLMs have mixed performance on logic puzzles, especially novel formulations they have not been trained on. For this reason, it has been my intuition for some time that models would either solve the problem of historical handwriting and other similar problems as they increased in scale, or they would plateau at high but imperfect, sub-human expert levels of accuracy.

#### Prediction Can Only Get You So Far…

I don’t want to get too technical here, but it is important to understand why these types of things are so hard for LLMs and why the results I am reporting here are significant. Since the first vision model, GPT-4, was released in February 2023, we’ve seen HTR scores steadily improve to the point that they get about 90% (or more) of a given text correct. Much of this can be chalked up to technical improvements in image processing and better training data, but it’s that last 10% that I’ve been talking about above.

Remember that LLMs are inherently predictive by nature, trained to choose the most probable way to complete a sequence like “the cat sat on the …”. They are, in effect, made up of tables which record those probabilities. Spelling errors and stylistic inconsistencies are, by definition, unpredictable, low probability answers and so LLMs must chafe against their training data to transcribe “the cat sat on the rugg” instead of “mat”. This is also why LLMs are not very good at transcribing unfamiliar people’s names (especially last names), obscure places, dates, or numbers such as sums of money.

From a statistical point of view, these all appear as arbitrary choices to an LLM with no meaningful differences in their statistical probabilities: in isolation, one is no more likely than another. Was a letter written by Richard Darby or Richard Derby? Was it dated 15 March 1762 or 16 March 1782? Did the author enclosed a bill for 339 dollars or 331 dollars? Correct answer to those questions cannot normally be predicted from the preceding contents of a letter. You need other types of information to find the answer when letters prove indecipherable. Yet basic correctness on these types of information—names, dates, places, and sums—is a prerequisite to their being useful to me as a historian. This makes the final mile of accuracy the only one that really counts.

#### On Scaling, Plateaus, and Benchmarks

More importantly, these issues with handwriting recognition are only one small facet of a much larger debate about whether the predictive architecture behind LLMs is inherently limiting or whether scaling (making the models larger) will allow the models to break free of regurgitation and do something new.

So when I benchmark an LLM on handwriting, in my mind I feel I am also getting some insight into that larger question of whether LLMs are plateauing or continuing to grow in capabilities. To benchmark LLM handwriting accuracy, l[ast year Dr. Lianne Leddy and I developed a set of 50 documents comprising some 10,000 words](https://www.tandfonline.com/doi/abs/10.1080/01615440.2025.2500309)—we had to choose them carefully and experiment to ensure that these documents were not already in the LLM training data (full disclosure: we can’t know for sure, but we took every reasonable precaution). We’ve written about the set [several times before](https://www.tandfonline.com/doi/abs/10.1080/01615440.2025.2500309), but in short it includes dozens of different hands, images captured with a variety of tools from smartphones to scanners, and document with different styles of writing from virtually illiterate scrawl to formal secretary hand. In my experience, they are representative of the types of documents that I, and English-language historian currently working on 18th and 19th century records, most often encounter.

We measure transcription error rates in terms of the percentage of incorrect characters (CER) and words (WER) in a given text. These are standardized but blunt instruments: a word may be spelled correctly but if the first letter is wrongly capitalized or it is followed with a comma rather than a semicolon it counts as an erroneous word. But what constitutes an error is also not always clear. Capitalization and punctuation were not standardized until the 20th century (in English) and are often ambiguous in historical documents. Another example: should we transcribe the long f (as in leſs) using an “f” for the first “s” or just write it out as “less”? That’s a judgement call. Sometimes letters and whole words are simply indecipherable and up for interpretation.

In truth, it’s usually impossible to score 100% accuracy in most real-world scenarios. Studies show that non-professionals typically score [WERs of 4-10%](https://www.tandfonline.com/doi/abs/10.1080/01615440.2025.2500309). Even professional transcription services expect a few errors. They typically guarantee a 1% WER (or around a 2-3% CER), but only when the texts are clear and readable. So that is essentially the ceiling in terms of accuracy.

[![](https://substackcdn.com/image/fetch/$s_!-RQJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F75343be3-e3ef-4867-af15-5e683a6efcc0_1828x843.png)](https://substackcdn.com/image/fetch/$s_!-RQJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F75343be3-e3ef-4867-af15-5e683a6efcc0_1828x843.png)

Figure 1: Performance of Trasnskribus, Humans, and Google models on HTR over time

Last winter, on our test-set, Gemini-2.5-Pro began to score in the human range: a strict CER of 4% and WER of 11%. When we excluded errors of punctuation and capitalization—errors that don’t change the actual meaning of the text or its usefulness for search and readability purposes—those scores dropped to CERs of 2% and WERs of 4%. The best specialized HTR software achieves CERs around 8% and WERs around 20% without specialized training which reduces errors rates to about those of Gemini-2.5-Pro. Improvement has indeed been steady across each generation of models. Those of Gemini-2.5-Pro were about 50-70% better than the ones we reported for Gemini-1.5-Pro a few months before, which were about 50-70% better than the initial scores reported for GPT-4 a few months before that. A similar progression is evident in Google’s faster, cheaper version of Gemini-FlashThe open question has been: will they keep improving at a similar rate.

#### Expert Human Performance?

On a (Canadian) Thanksgiving trip to visit family, I started to play with the new Google model. Here is what I had to do to access it. First, I uploaded an image to [AI Studio](https://aistudio.google.com/), and gave it the following system instructions (the same ones we’ve used on all our tests…I’d like to modify them but I need to keep them consistent across all the tests):

> “Your task is to accurately transcribe handwritten historical documents, minimizing the CER and WER. Work character by character, word by word, line by line, transcribing the text exactly as it appears on the page. To maintain the authenticity of the historical text, retain spelling errors, grammar, syntax, and punctuation as well as line breaks. Transcribe all the text on the page including headers, footers, marginalia, insertions, page numbers, etc. If these are present, insert them where indicated by the author (as applicable). In your final response write “Transcription:” followed only by your transcription.”

But then I had to wait for the result and manually retry the prompt, over and over again—sometimes 30 or more times—until I was given a choice between two answers. Needless to say, this was time consuming, expensive, and I repeatedly hit rate limits which delayed things even more. As a result, I could only get through five documents from our set. In response, I tried to choose the most error-prone and difficult to decipher documents from the set, texts that are not only written in a messy hand but are full of spelling and grammatical errors, lacking in proper punctuation, and that contain lots of inconsistent capitalization. My goal was not to be definitive—that will come later—but to get a sense of what this model could do.

[![](https://substackcdn.com/image/fetch/$s_!JvMG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4d0d32e2-17f6-40c0-85f0-33819976b241_1836x1876.png)](https://substackcdn.com/image/fetch/$s_!JvMG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4d0d32e2-17f6-40c0-85f0-33819976b241_1836x1876.png)

Figure 2: The AI Studio interface showing the A/B Test rather than a single output.

The results were immediately stunning. On each of the five documents I transcribed (totalling a little over 1,000 words or 10% of our total sample), the model achieved a strict CER of 1.7% and WER of 6.5%—in other words, about 1 in 50 characters were wrong including punctuation marks and capitalization. But as analyzed the data I saw something new: for the first time, nearly all the errors were capitalization and punctuation, very few were actual words. I also found that a lot of the punctuation marks and capital letters it was getting wrong were actually highly ambiguous. When those types of errors were excluded from the count, th**e error rates fell to a modified CER of 0.56% and WER of 1.22%**. In other words, the new Gemini model was only getting about 1 in 200 characters wrong, not counting punctuation marks and capital letters.

[![](https://substackcdn.com/image/fetch/$s_!t0Jz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6fc9ae77-331e-4ef0-b4b1-483f15d2bcee_1187x626.png)](https://substackcdn.com/image/fetch/$s_!t0Jz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6fc9ae77-331e-4ef0-b4b1-483f15d2bcee_1187x626.png)

Figure 3: A good side by side comparison on a particularly difficult document.No other model comes close on this letter.

**The new Gemini model’s performance on HTR meets the criteria for expert human performance**. These results are also 50-70% better than those achieved by Gemini-2.5-Pro. In two years, we have in effect gone from transcriptions that were little more than gibberish to expert human levels of accuracy. And the consistency in the leap between each generation of model is exactly what you would expect to see if scaling laws hold: as a model gets bigger and more complex, you should be able to predict how well it will perform on tasks like this just by knowing the size of the model alone.

#### **The Ultimate Test**

Here is where is starts to get really weird and interesting. Fascinated with the results, I decided to push the model further. Up to this point, no model has been able to reliably decipher tabular handwritten data, the kind of data we find in merchant ledger, account books, and daybooks. These are extremely difficult to decipher for humans but (until now) nearly impossible for LLMs because there is very little about the text that is predictive.

Take this page (Figure 4) from a 1758 Albany merchant’s daybook (a running tally of sales) which is especially hard to read. It is messy, to be sure, but was also kept in English by a Dutch clerk who may not have spoken much English and whose spelling and letter formation was highly irregular, mixing Dutch and English together. The sums in the accounts were also written in the [old style of pounds / shillings / pence](https://www.royalmintmuseum.org.uk/journal/history/pounds-shillings-and-pence/) using a shorthand typical of the period: “To 30 Gallons Rum @4/6 6/15/0”. This means that someone purchased (a charge to their account) 30 gallons of rum where each gallon cost 4 shillings and 6 pence for a total of 6 pounds, 15 shillings, and 0 pence.

To most people today, this non-decimalized way of measuring money is foreign: there are 12 pennies (pence) in a shilling and 20 shillings in pound (see [this description by the Royal Mint)](https://www.royalmintmuseum.org.uk/journal/history/pounds-shillings-and-pence/). Individual transactions were written into the book as they happened, divided from one another by a horizontal rule with a number signifying the day of the month written in the middle. Each transaction was recorded as s debt (Dr), that is a purchase, or a Credit (Cr) meaning a payment. Some transactions were also crossed out, probably to indicate they had been balanced or transferred to the client’s account in the merchant’s main ledger (similar to when a pending transaction is posted in your online banking). And none of this was written in a standardized way.

LLMs have had a hard time with such books, not only because there is very limited training data available for these types of records (ledgers are less likely to digitized and even less likely to be transcribed than diaries or letters because: who wants to read them unless they have to?) but because none of this is predictive: a person can buy any amount of anything at any arbitrary cost recorded in sums that don’t add up according to conventional methods…which LLMs have had enough issues with over the years. I’ve found that models can often decipher some of the names and some of the items in a ledger, but become utterly lost on the numbers. They have a hard time transcribing digits in general (again you can’t predict whether it’s 30 or 80 gallons if the first digit is poorly formed), but also tended to merge the item costs and totals together. In effect, they often don’t seem to realize that the old-style sums are amounts of money at all. Telling them to check the numbers by adding the totals together does not help and often makes things worse. Especially complex pages temporarily break the model, causing it to repeat certain numbers or phrases repeatedly until they reach their output limits. Other times they think for a long time and then fail to answer entirely.

#### **Deux Ex Machina**

But there is a something in this new machine that is markedly different. From my admittedly limited tests, the new Gemini model handles this type of data much better than any previous model or student I’ve encountered: after completing the five documents from our test-set I uploaded the Albany merchant’s daybook page above (Figure 4) with the same prompt, just to see what would happen and amazingly, it was again almost perfect. The numbers are, remarkably, all correct. More interesting, though, are that its errors are actually corrections or clarifications. For example, when Samuel Stitt purchased 2 punch bowls, the clerk recorded that they cost 2/ each meaning 2 shillings each; for brevity’s sake he implied 0 pennies rather than writing it out. Yet for consistency, the model transcribed this as @2/0 which is actually a more correct way of writing the sum and clarifies the meaning. Strictly speaking, though, it is an error.

[![](https://substackcdn.com/image/fetch/$s_!M7Fk!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1cdc11e4-6cfa-40f3-a00a-40f139e85dd5_712x745.png)](https://substackcdn.com/image/fetch/$s_!M7Fk!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1cdc11e4-6cfa-40f3-a00a-40f139e85dd5_712x745.png)

Figure 5: Transcription by new unknown Gemini model of page from the Albany Account Book

In tabulating the “errors” I saw the most astounding result I have ever seen from an LLM, one that made the hair stand up on the back of my neck. Reading through the text, I saw that Gemini had transcribed a line as “To 1 loff Sugar 14 lb 5 oz @ 1/4 0 19 1”. If you look at the actual document, you’ll see that what is actually written on that line is the following: “To 1 loff Sugar 145 @ 1/4 0 19 1”. For those unaware, in the 18th century sugar was sold in a hardened, conical form and Mr. Slitt was a storekeeper buying sugar in bulk to sell. At first glance, this appears to be a hallucinatory error: the model was told to transcribe the text exactly as written but it inserted 14 lb 5 oz which is not in the document. This was exactly the type of errors I’ve seen many times before: in the absence of good context the model guessed, inserting a hallucination. But then I realized that it had actually done some extremely clever.

What Gemini did was to correctly infer that the digits 1, 4, 5 were units of measurement describing the total weight of sugar purchased. This was not an obvious conclusion to draw, though, from the document itself. All the other nineteen entries clearly specify total units of purchase up front: 30 gallons, 17 yds, 1 barrel and so on. The sugar loaf entry does this too (1 loaf is written at the start of the entry) and it is the only one that lists a number at the end of the description. There is a tiny mark above the 1 which may also (ambiguously) have been used to indicate pounds (thanks to Thomas Wein for noticing this). But if Gemini interpreted it this way, it would also have read the phrase as something like 1 lb 45 or 145 lb, given the placement of the mark above the 1. It was also able to glean from the text that sugar was being sold at 1 shilling and 4 pence per *something*, and inferred that this something was pounds.

[![](https://substackcdn.com/image/fetch/$s_!PyC4!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F16937510-c583-4c7b-91e8-aefd45c16912_273x45.png)](https://substackcdn.com/image/fetch/$s_!PyC4!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F16937510-c583-4c7b-91e8-aefd45c16912_273x45.png)

Figure 6: Close-up of the transcription

[![](https://substackcdn.com/image/fetch/$s_!Ub6L!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4e135b3a-7adb-4250-b1ae-1fcae452dbbe_1139x256.png)](https://substackcdn.com/image/fetch/$s_!Ub6L!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4e135b3a-7adb-4250-b1ae-1fcae452dbbe_1139x256.png)

Figure 7: Closeup of the Original Document

To determine the correct obverse weight, decoding the 145, Gemini then did something remarkable: it worked through the numbers, using the final total cost of 0/19/1 to work backwards to determine the weight, a series of operations that would require it to convert between two decimalized and two non-decimalized systems of measurement. While we don’t know its actual reasoning process, it must have been something akin to this: the sugar cost 1 shilling and 4 pence per unit, and that that sum can also be expressed as 16 pence. We also know that the total value of the sale was 0 pounds, 19 shillings, and 1 penny, so we can express this as 229 pence to create a common unit of comparison. To find how much sugar was purchased we then divide 229 by 16 to get the result: 14.3125 or 14 and 5/16 or 14 lb 5 oz. Therefore, Gemini concluded, it was not 1 45, nor 145 but 14 5 and then 14 lb 5 oz, and it chose to clarify this in its transcription.

[Added 17/10/2025]: If that ambiguous mark above the 1 tipped it off that the 145 was a measurement in pounds, the result was a similar process of logical deduction and self correction. In that case, Gemini would have had to intentionally question the most obvious version of the transcription, realizing (in effect) that 1 lb 45 or 145 lbs (which is the only way to read the original) did not balance with the tally of 0 19 1. Getting to 14 lb 5 oz would then arise from the same process as above.

This is exactly the type of logic problem at which LLMs often fail: first there is the ambiguity in the writing itself and in the form of the text, then the double meaning of the word “pounds”, and finally the need to convert back and forth between not one but two different non-decimalized systems of measurement. And no one asked Gemini to do this. It took the initiative to investigate and clarify the meaning of the ambiguous number all on its own. And it was correct.

In my testing, no other model has done anything like this when tasked with transcribing the same document. Indeed even if you give Gemini-2.5-Pro hints, asking it to pay attention to missing units of measurement it occasionally inserst “lb” or “wt” after the 5 in 145, but deletes the other numbers. GPT-5 Pro typically transcribes the line as: “To 1 Loaf Sugar 1 lb 5 0 19 1”. Interestingly, you can nudge both GPT-5 and Gemini-2.5-Pro towards the correct answer by asking it what the numbers 1 4 5 mean in the sugar loaf entry. And even then answers vary, often suggesting that it was 145 lbs of sugar rather than 14 lb 5 oz.

[![](https://substackcdn.com/image/fetch/$s_!W-ph!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72a96a76-0f6f-400f-ae78-fadf4287cc09_1249x1849.png)](https://substackcdn.com/image/fetch/$s_!W-ph!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72a96a76-0f6f-400f-ae78-fadf4287cc09_1249x1849.png)

I have diligently tried to replicate this result, but sadly after hundreds of refreshes on AI Studio, I have yet to see the A/B test again on this document. I suspect that Google may have ended it, or at least for me.

#### Symbolic Reasoning and LLMs

What makes this example so striking is that it seems to cross a boundary that some experts have long claimed current models cannot pass. Strictly speaking, the Gemini model is not engaging in symbolic reasoning in the traditional sense: it is not manipulating explicit rules or logical propositions as a classical AI system would be expected to do. Yet its behaviour mirrors that outcome. Faced with an ambiguous number, it inferred missing context, performed a set of multi-step conversions between historical systems of currency and weight, and arrived at a correct conclusion that required abstract reasoning about the world the document described. In other words, it behaved *as if* it had access to symbols, even though none were ever explicitly defined. Did it create these symbolic representations for itself? If so, what does that mean? If not, how did it do this?

What appears to be happening here is a form of emergent, implicit reasoning, the spontaneous combination of perception, memory, and logic inside a statistical model that (I don’t believe…Google please clarify!) was designed to reason symbolically at all. And the point is that we don’t know what it *actually* did or why.

The safer view is to assume that Gemini did not “know” that it was solving a problem of eighteenth-century arithmetic at all, but its internal representations were rich enough to emulate the process of doing so. But that answer seems to ignore the obvious facts: it followed an intentional, analytical process across several layers of symbolic abstraction, all unprompted. This seems new and important.

If this behaviour proves reliable and replicable, it points to something profound that [the labs are also starting to admit](https://importai.substack.com/p/import-ai-431-technological-optimism): that true reasoning may not require explicit rules or symbolic scaffolding to arise, but can instead emerge from scale, multimodality, and exposure to enough structured complexity. In that case, the sugar-loaf entry is more than a remarkable transcription, it is a small but clear (and I think unambiguous) sign that the line between pattern recognition and genuine understanding is beginning to blur.

#### Conclusion

For historians, the implications are immediate and profound. If these results hold up under systematic testing, we will be entering an era in which large language models can not only transcribe historical documents at expert-human levels of accuracy, but can also *reason* about them in historically meaningful ways. That is, they are no longer simply seeing letters and words—and correct ones at that—they are beginning to interpret context, logic, and material reality. A model that can infer the meaning of “145” as “14 lb 5 oz” in an 18th-century merchant ledger is not just performing text recognition: it is demonstrating an understanding of the economic and cultural systems in which those records were produced…and then using that knowledge to re-interpret the past in intelligible ways. This moves the work of automated transcription from a visual exercise into an interpretive one, bridging the gap between vision and reasoning in a way that mirrors what human experts do.

But the broader implications are even more striking. Handwritten Text Recognition is one of the oldest problems in the field of AI research, going back to the late 1940s before AI even had a name. For decades, AI researchers have treated handwritten text recognition as a bounded technical problem, that is an engineering challenge in vision. This began with the IBM 1287 which could read digits and five letters when it debuted in 1966 and continued on through the creation of specialized HTR models developed only a few years ago.

What this new Gemini model seems to show is that near-perfect handwriting recognition is better achieved through the generalist approach of LLMs. Moreover, the model’s ability to make a correct, contextually grounded inference that requires several layers of symbolic reasoning suggests that something new may be happening inside these systems—an emergent form of abstract reasoning that arises not from explicit programming but from scale and complexity itself.

If so, the “handwriting problem” may turn out to have been a proxy for something much larger. What began with a test on the readability of old documents may now be revealing, by accident, the beginnings of machines that can actually reason in abstract, symbolic ways about the world they see.

Thanks for reading Generative History! Subscribe for free to receive new posts and support my work.

219

43

23

Share
