---
id: 1408
url: https://shannadige.com/blog/darkroom/
title: Automating my 35mm film scanning pipeline
domain: shannadige.com
source_date: '2026-10-02'
tags:
- cli-tool
- python
- tutorial
summary: The author automated their 35mm film scanning workflow after spending excessive
  time on manual processing. Initial attempts to fully automate the process using
  AI failed when it damaged the scanner, so they pivoted to a hybrid approach using
  existing scanning software combined with custom automation for post-processing tasks
  like negative conversion, dust removal, metadata tagging, and publishing. The new
  pipeline significantly reduces processing time while maintaining quality, allowing
  the author to focus more on photography itself rather than the tedious technical
  work.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Automating my 35mm film scanning pipeline

![Automating my 35mm film scanning pipeline](/_astro/hero-canisters.CByBbBgp_1unCgw.webp) 

Automating my 35mm film scanning pipeline
=========================================

A story about replacing a creative workflow and focusing on another.

October 2, 2026  · 8 min read

[View the experience
-------------------

darkroom.shannadige.com](https://darkroom.shannadige.com) 

I love photography. There is a special feeling to seeing an image through a lens, organizing it to compose a story, and working with the resulting photo. I had cycled through DSLR and mirroless cameras before falling in deep love with the Canon AE-1P, an analog SLR that my dad traveled with around the world before settling down in the States.

Film photography is simple, but particular: you expose reflected light against a strip of plastic and burn-in a chemical image. Depending on the light conditions, film stock used, and lens, you’ll get magically unique compositions.

For years my process looked like this: load film and take photos, send the film to a lab and wait for development, pick up said film, cut the negatives into strips, load them into a holder, capture the negative of each frame in with a specialized scanner, open every file in darktable, invert it by hand, make topical edits, then decide where to store and/or share the exported image. At first this was an exciting process for me. Then as the number of rolls increased, so did my effort to do this for 36 frames per roll.

![A desk lit by a lamp, with a strip of negatives hanging from it, VueScan open on a monitor showing an orange negative, and film holders, a blower and a brush next to a blue Plustek scanner.](/_astro/desk-before.CGApRpoQ_1ynbLE.webp)

On average it would take me about 4 hours to fully scan in a roll of 36 photos and complete edits. It requires delicacy in handling film especially to avoid dust or scratches on the final image. Safe to say, the process grew weary on me quite fast. I was spending more time processing my images than actually taking them. So I began looking for ways I could cut some time, or as the CEOs like to say, “streamline operations” across my personal digital lab.

Giving Claude destructive hardware capabilities
-----------------------------------------------

My first hypothesis was if I could take myself out of the loop entirely. I’d have Claude drive the scanner over SANE (open-source scanner driver stack) and handle scanning, colour conversion and edits end to end.

On the first scan, Claude used SANE with inversed X/Y scanbed directions and nearly broke the gear mechanism inside the scanner. So I unfortunately killed time by needing to perform an emergency surgical operation on the scanner to save $200 from being spent on a new one.

Chat: Blank white scans

Sep 20, 2026

1. Shan 4:54 pm

   there is definitely film in there, maybe its the scanning settings you opted for
2. Claude 4:56 pm

   I've been tracing why the scans come out white, and your guess about settings can be ruled out. … Instead, every one of the 856 rows is identical: smooth vertical bands from the lamp's uneven illumination, with zero variation from top to bottom and no image detail. … So the sensor saw the same unobstructed line of light for the whole scan.
3. Shan 5:01 pm

   i tried with vuescan, but the sensor or the carriage is not moving, you must have done something wrong
4. Shan 5:04 pm

   its definitely in a bad state. can you check on the scanner, until i let you know its moving. i did hear some clicking earlier, so it might have been going an opposite direction
5. Claude 5:05 pm

   I found what the clicking was, and it came from my scans. … At the end of every scan, the genesys backend sends the carriage back with a blind reverse move: 7010 steps at 900 dpi, and more at 3600. It assumes the carriage travelled forward during the scan. … So each scan ended with the motor driving a carriage that was already parked backwards into its end stop. That is the clicking you heard, and your read on the direction was right. I ran seven scans, so it happened seven times.

![The Plustek scanner with its case removed, showing the carriage, a threaded rod, a spring and the motor gear.](/_astro/scanner-open.cg48otdK_1XpUbz.webp)

Surgery. Pushing a rod and gear that did not want to be pushed back into place.

I ended up working with what was already working well. VueScan was the software I’d licensed way back when - given that it had the best compatibility with my scanner, and given that I didn’t have a robot arm automating the physical operation of loading and scanning, I’d just use this myself and find a solution that can handoff from right after this.

Studio
------

Learning from failure fortunately turned my thought process around. I work in VueScan the way I always have, so I needed some way to automate the processing of those scans. After a handful of individual tests against image data I had tested against, I had a full suite of tools working in combination to help me.

### Negative Conversion

Converting negatives into positives is mostly plain code. The inversion is a short *numpy* routine, that works in film density and measures color across the whole roll before adjusting each frame within limits of its negative. So thirty-six frames look consistent to one full roll and a sunset doesn’t get radically color-corrected. This was something I tended to struggle with even doing manually. My agent determined that using the blank leading slot of a roll would be a good reference for how color correction should be weighted against the rest of the frames. Before building anything else, we ran it on an old roll as a go or no-go test.

Chat: Conversion test

Sep 21, 2026

1. Shan 10:35 am

   start the conversion test on film/valentines2026
2. Claude 10:40 am

   The conversion test passed on 28 of 29 frames. Custom conversion works well enough to build on, and it needs no darktable to get there. … Mine are brighter and more neutral, while your exports lean teal and dark (the Hotel del Coronado sky, the beach portrait, the garden). That is taste as much as correctness, so you should judge.
3. Shan 10:40 am

   i like your direction, run the dust detection test

![Frame 2 as scanned, an orange-masked negative of the portrait with the giant paper flower.](/_astro/neg-raw0002.CGyTqUJq_Z218Bfo.webp)![Frame 2 after conversion: the portrait with the giant paper flower in full colour.](/_astro/pos-raw0002.uu-DUJ2__Z1QWGGT.webp)

![Frame 3 as scanned, an orange-masked negative of the “Can you dig it?” sign.](/_astro/neg-raw0003.BRJwUlFh_ZY9WQv.webp)![Frame 3 after conversion: the “Can you dig it?” sign in full colour.](/_astro/pos-raw0003.DTC3OuOz_Z1vMKrk.webp)

![Frame 5 as scanned, an orange-masked negative of the yellow orchids.](/_astro/neg-raw0005.CUwg9xEk_ZOA3zd.webp)![Frame 5 after conversion: the yellow orchids in full colour.](/_astro/pos-raw0005.4bMfduzJ_1N8sTh.webp)

![Frame 20 as scanned, an orange-masked negative of the frozen lake.](/_astro/neg-raw0020.vUSSZL-n_qnGVG.webp)![Frame 20 after conversion: the frozen lake in full colour.](/_astro/pos-raw0020.HEA_0iUZ_Z1zEpEc.webp)

Sample negatives vs. converted positive (those scratch marks are characteristic of the film stock)

### Dust Removal & Editing

The models come in where plain code runs out. Dust is found by image analysis on the negative and marked for removal. This is harder than it sounds: on a beach frame the first detector flagged about 2,000 sun glints on the water as dust. The fix was to affix context and act only where surroundings are smooth. The spots it finds are filled by LaMa (inpainting model), with detail copied back in from nearby film spots so the patch doesn’t look smudged. Kind of like the repair tool on Photoshop.

Not every single area needs to be filled. I have a custom threshold set where I can hold grainy spots for review, and approve/deny them individually or in batch.

This also created a need to adjust light and color properties of each image individually to account for graininess, so I had exposure, contrast, temperature, and other controls embedded in reach.

![The frame review screen in studio: a frozen lake under a pale sky, covered in circles marking dust and scratches, with sliders and dust counts in a panel on the left.](/_astro/studio-dust.DpKR0CZa_Z1UaBey.webp)

Frame review. Green circles were dust-repaired automatically, amber ones held for review.

### Metadata

Indexing data for analog film can be time-consuming, especially if I’m working across separate tools on my own. This was a “hmm, why not?” problem to address since now that I’m using technology I can extend it to identify a photo for easy searching later on.

So Qwen3-VL runs locally in Ollama when scans come in, looks at each finished frame and drafts tags for it in about five seconds. That combined with camera, lens, date, and film stock data gives me a comprehensive library to easily search from.

![The Gallery tab of the review panel beside a portrait of a woman in front of a Green House Motel sign, with drafted tags: woman, sign, motel, plants, flowers, greenhouse.](/_astro/studio-tags.B3jM9FRj_Z1ucmi0.webp)

Tags drafted by Qwen3-VL in 3 seconds, fixed once I pick the frame.

My part is now the part I can thoroughly enjoy, which is looking at the results I’ve snapped and finding inspiration to snap more.

![The studio app with valentines2026 selected in the sidebar's list of roll folders: a roll header with Revolog Rasp 200, the Canon AE-1P and notes about the Chicago Botanic Garden's orchid show, and a contact sheet of all 28 converted frames marked live or check.](/_astro/studio-contact-sheet.gpPWZWTB_2lgeDQ.webp)

Gallery
-------

Once I had gotten a few rolls through the pipeline, the next question was where they’d live.

Typically they’re stored on my 4TB HDD that I’ve set to eternally spin while plugged into my machine. But while off the rush of building enterprise-software-for-one, I wanted to explore a way to share via the world wide web.

### Publish Workflow

I have a Cloudflare account that gets the occassional activity from visitors on some CDN content I have for my personal site, and what better way to max out the free plan than uploading all my images to my own R2 bucket? So I extended the studio to enable publishing.

![The publish dialog for the valentines2026 roll over the studio: label Valentines 2026, stock Revolog Rasp 200, date 2026-02, a private-link checkbox, and all 23 picked photos numbered in the order the gallery shows them.](/_astro/studio-publish.DioFE5SG_yC6Rt.webp)

Publishing a roll. The picked frames go to R2 in the order shown, with their tags and nothing else.

### Showcasing Photos by Roll

A grid of thumbnails felt too cheap for a publish experience. I continued to scan more rolls throughout the days and recounted my earlier times dropping off my rolls for development. Seeing the lab technicians unroll the film itself to spool to their C41 processor gave me a simple idea to emulate the roll itself.

I do acknowledge that this is not the most accurate form of realism, but it was a very fun idea to play with and evolve. I ended up with a felt table covered in film canisters modeled for 3js, each with real label art and random scuff marks. Pick one up and you can yank the film out to expose the frames. Then it just falls back onto the felt table.

I was able to source the effective

[![](/_astro/gallery-roll-poster.CUnLfHBx.webp)](https://r2.shannadige.com/darkroom-rolls.webm)

Demo walkthrough; credits to Opus-5.5 for recording

My corner of the Internet
-------------------------

In total this project took 11 days and 64 commits. The gallery has 22 rolls and 314 photos dating all the way back to 2020.

I will continue to add to this as I purge more money on rolls and development. It’s my corner of the Internet, for you to unplug and enjoy if you choose to revisit.

There’s been something just as alluring about creating a site like this, versus just engaging the scanner and process itself. The manual process is something that someone might enjoy and wouldn’t want to delegate. At least for me, it keeps me off the computer and focused on enjoying the time I have exploring the world. Capturing it in a different perspective. ■

![Shan in a wide-brimmed green hat and a white shirt, looking down at a black Canon film camera held in both hands, on a tree-lined road with a van and a stall of king coconuts behind him.](/_astro/author-canon.B0pnZlAO_ZhvFny.webp)
