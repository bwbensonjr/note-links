---
id: 120
url: https://jpt.sh/projects/trifold/
title: trifold - trifold
domain: jpt.sh
source_date: '2025-12-01'
tags:
- cli-tool
- web-dev
- devops
summary: trifold is a CLI tool that enables affordable static website hosting through
  a CDN (currently bunny.net), costing just pennies per month by charging only for
  storage and bandwidth usage. It provides an easy alternative to free services like
  Netlify and GitHub Pages, offering features like custom domains with SSL, cache
  management, and billing limits while maintaining reliability through a paid service.
  The tool is designed for indie developers and students building sites with static-site
  generators like Hugo or Zola, with typical costs remaining negligible for low-traffic
  sites.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# trifold - trifold

trifold ¶ trifold is a tool to serve static websites using a content delivery network (CDN). Source: https://codeberg.org/jpt/trifold/ This allows painless deployment of sites consisting entirely of static assets (HTML, CSS, JS, images) for pennies a month. It is the perfect companion to deploy sites built with static-site generators like Hugo , Zola , Quarto , or zensical . The tool provides a simple CLI that allows: initializing new projects without touching the CDN web interface syncing local HTML/CSS/JS/etc. to the CDN & clearing the cache configuring a custom domain name to point at your files, with SSL enabled setting a maximum monthly cost to avoid surprise bills using CDN edge functions to support redirects This project grew out of frustration with services making their free tier less friendly to indie devs and students that just need a cheap & reliable place they can host things. trifold offers an easy alternative to services like Cloudflare Pages, Netlify, and GitHub pages for static websites. Instead of relying on a free service it is hopefully going to be more stable to rely on a paid service with a reasonable price point and the ability to set billing limits. Installation ¶ If you have uv installed, you can run uvx trifold without a separate installation step. This is the recommended method, uvx is a built-in alias for uv tool run . (See https://docs.astral.sh/uv/guides/tools/#running-tools if you're curious to learn more.) To upgrade: uv tool upgrade trifold You can also use any Python package manager you prefer, pip , pipx , poetry , etc. to install in your preferred manner. bunny.net & pricing ¶ At the moment bunny.net 1 is the only supported provider, but others can be added. bunny.net is a professional-grade CDN that is also very affordable. Like most hosts, they charge for both storage & bandwidth. Both starts at $0.01/GB/mo. The typical static webpage is under 1GB, meaning storage costs will be negligible unless you decide to host audio/video. And if you do, the rates are far cheaper than most competitors, see their pricing for details. In terms of bandwidth, let's say your page size is 2MB (a moderate-sized page) and hits the front page of a popular website, driving a surge of 25,000 hits. ( Congrats! ) Not only will your site handle the traffic just fine, your total bill will be $0.50 for the 50GB of bandwidth used. (You could serve a million hits, ~2TB, for $20.) Of course, most sites will only get a fraction of this traffic. It is possible to host dozens of low-traffic sites for the $1/monthly minimum bill. This is a referral link, using it supports development of the project. ↩
