---
id: 1454
url: https://karpathy.bearblog.dev/hacker-tube/
title: HackerTube – karpathy
domain: karpathy.bearblog.dev
source_date: '2026-10-31'
tags:
- video
- web-dev
- ai
summary: Andrej Karpathy built HackerTube, a YouTube-style site (hackertube.org) that
  shows only videos recommended in Hacker News comments, after growing frustrated
  with YouTube's spammy, exaggerated recommendations. Using an AI coding assistant,
  he filtered about 40K comments down to 6,454 videos from 2007 to 2026 across 150
  topics, then added a clean YouTube-like interface, personalized recommendations
  without accounts, and keyboard shortcuts. The site also lets users export its data
  so they can build their own version.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-5-5
---

# HackerTube – karpathy

HackerTube
==========

*31 Oct, 2026*

It was Friday night at 11pm, I was tired, I went to YouTube to watch something and realized that I was looking at an enshittified wall of slop. Insanely exaggerated thumbnails, dumb recommendations of the same tired topics, truly terrible idiocracy-grade content. I'm sure this algorithm works well for the median person on the internet, but it definitely does not work for me. So this morning (Saturday) I took a hold of my Opus 5.5 and gave it the task: Let's write our own YouTube clone based on whatever videos have been recommended on Hacker News. And Opus came back with: [hackertube.org](https://hackertube.org/)!

![image](https://bear-images.sfo2.cdn.digitaloceanspaces.com/karpathy/image-2.webp)

Opus downloaded all comments of HackerNews, filtered them down, ran Sonnet over them in a workflow, got rid of spam and low grade content, and narrowed them down to just 40K comments recommending a YouTube video. In total, we get 6,454 YouTube videos that have been recommended by a few people on HN from 2007-2026 across 150 topics. Then we wrap it up in a YouTube UI, get a domain, push to a VPS, secure, harden, optimize and voila!

HackerTube:

* Contains quality content
* Uses the 50% thumbnail instead of the uploaded thumbnail
* Custom and good ForYou recommendations without any user accounts, storing state in local browser session
* Keyboard shortcuts
* Export of the site's data available to give to your agent to easily create your own version

This takes ~2 hours now. I can breathe again. Thank you Opus 5.5 <3.
