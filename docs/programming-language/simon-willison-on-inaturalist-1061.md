---
id: 1061
url: https://simonwillison.net/tags/inaturalist/
title: Simon Willison on inaturalist
domain: simonwillison.net
source_date: '2026-05-02'
tags:
- python
- cli-tool
- web-dev
- github-repo
- ai
summary: Simon Willison created a tool to view his iNaturalist observations from multiple
  accounts organized by when they occurred. He built the project entirely on his phone
  using Claude Code, combining a Python CLI that groups nearby observations together,
  a Git repository that automatically fetches and stores the data as JSON, and a web
  app that displays the observations with clickable image thumbnails in a modal. The
  entire workflow leverages automation and AI-assisted development to create a personalized
  visualization of his nature sightings.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Simon Willison on inaturalist

[Release](/elsewhere/release/)
[inaturalist-clumper 0.1](https://github.com/simonw/inaturalist-clumper/releases/tag/0.1)

Part of the infrastructure I use for [publishing my iNaturalist sightings on my blog](https://simonwillison.net/2026/May/1/inat-sightings/). I've been running this in production for a few weeks now, inspiring some iterations on how it works, so I decided to ship a 0.1 release.

You can see an example of the output [in this JSON file](https://github.com/simonw/inaturalist-clumps/blob/main/clumps.json).

[15th May 2026, 11:53 pm](/2026/May/15/inaturalist-clumper/) · [projects](/tags/projects/), [inaturalist](/tags/inaturalist/)
