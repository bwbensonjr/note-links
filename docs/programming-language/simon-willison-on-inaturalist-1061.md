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

Tool iNaturalist Sightings I wanted to see my iNaturalist observations - across two separate accounts - grouped by when they occurred. I'm camping this weekend so I built this entirely on my phone using Claude Code for web. I started by building an inaturalist-clumper Python CLI for fetching and "clumping" observations - by default clumps use observations within 2 hours and 5km of each other. Then I setup simonw/inaturalist-clumps as a Git scraping repository to run that tool and record the result to clumps.json . That JSON file is hosted on GitHub, which means it can be fetched by JavaScript using CORS. Finally I ran this prompt against my simonw/tools repo: Build inat-sightings.html - an app that does a fetch() against https://raw.githubusercontent.com/simonw/inaturalist-clumps/refs/heads/main/clumps.json and then displays all of the observations on one page using the https://static.inaturalist.org/photos/538073008/small.jpg small.jpg URLs for the thumbnails - with loading=lazy - but when a thumbnail is clicked showing the large.jpg in an HTML modal. Both small and large should include the common species names if available 1st May 2026, 7:35 pm · tools , ai , inaturalist , generative-ai , llms , claude-code
