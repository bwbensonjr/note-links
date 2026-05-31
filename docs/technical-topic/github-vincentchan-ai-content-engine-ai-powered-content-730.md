---
id: 730
url: https://github.com/vincentchan/AI-Content-Engine
title: 'GitHub - vincentchan/AI-Content-Engine: AI-powered content engine for research,
  ideation, and drafting. Based on Dan Koe&#39;s content framework.'
domain: github.com
source_date: '2026-01-20'
tags:
- github-repo
- ai
- llm
- cli-tool
summary: 'This GitHub repository features an AI-powered content creation engine inspired
  by Dan Koe''s content framework, built using Claude Code with slash commands and
  subagents to automate research, ideation, and drafting. The tool includes four main
  commands: a swipe file generator that analyzes high-performing content, a content
  ideas generator that creates post outlines, a content draft generator that produces
  multiple variations, and a YouTube title generator that suggests 30 title options.
  Users can clone the repository and follow a guided workflow to build reference libraries,
  generate social media content, or create full drafts with structured outputs organized
  in dedicated folders.'
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - vincentchan/AI-Content-Engine: AI-powered content engine for research, ideation, and drafting. Based on Dan Koe&#39;s content framework.

AI Content Engine Because staring at a blank page hoping for inspiration is so 2023. An AI-powered content creation system that helps you research, ideate, and draft content like a caffeinated content team of one. Built with Claude Code, slash commands, and subagents. The Origin Story I watched this YouTube interview where Greg Isenberg broke down Dan Koe's AI content workflow and my jaw hit the floor. Dan Koe—the guy whose single Twitter thread got 165 million views (not a typo)—was sharing his actual system for creating content that resonates. So naturally, I did what any reasonable person would do: I turned it into a Claude Code project with slash commands and subagents so I could pretend I have Dan's content superpowers. Credits (a.k.a. The People Who Actually Know What They're Doing) Dan Koe — Created the framework. Wrote that 165M+ view Twitter thread . Probably writes better content before breakfast than most of us do all week. Greg Isenberg — Conducted the interview that started this rabbit hole. Also created a downloadable guide if you want the source material. Vincent Chan — That's me. I just wired it all together with Claude Code, slash commands, and subagents. Standing on the shoulders of giants, etc. (No affiliation with Dan or Greg—just a fan who got inspired and started building.) How It Works This engine uses Claude Code's slash commands to run specialized content workflows. Each command is a prompt that orchestrates subagents to do the heavy lifting. The Commands Commands are organized by stage in the content creation process: Research Stage "Know thy audience, know thy swipe file" Command What It Does /swipe-file-generator Analyzes high-performing content from URLs and builds a swipe file of patterns, hooks, and psychological triggers /content-ideas-generator Extracts 5 structured post outlines from your reference material (newsletters, scripts, notes, journal entries) Ideation Stage "Turn research into something people actually want to read" Command What It Does /content-draft-generator Takes reference content, analyzes it, asks you context questions, then generates 3 variations of your new content /youtube-title-generator Generates 30 YouTube title ideas from your content concept using proven formulas and psychological triggers Getting Started Clone this repo (or just copy the .claude folder structure) Open in Claude Code and pick your starting point: Building a swipe file from scratch? Start here: /swipe-file-generator Add URLs to /swipe-file/swipe-file-sources.md and let it analyze high-performing content. Great for building your reference library over time. Have content you want to turn into social posts? Run: /content-ideas-generator Feed it a newsletter, transcript, or notes. Get back 5 structured post outlines with hooks, paradoxes, and transformation arcs. Ready to write a full piece? Use: /content-draft-generator Give it reference content to study, answer some context questions, and get 3 draft variations. The full pipeline. Just need a killer YouTube title? Try: /youtube-title-generator Describe your video concept and get 30 title options using proven formulas. Follow the prompts — each command will ask for input and guide you through the process Find your output in the corresponding folder: /swipe-file/ — Your growing swipe file /content-ideas/ — Post outlines /content-draft/ — Generated drafts /youtube-title/ — Title ideas Project Structure /AI-Content-Engine/ ├── /.claude/ │ ├── /commands/ # Slash commands live here │ └── /subagents/ # Specialized AI workers ├── /swipe-file/ # Research output ├── /content-ideas/ # Post outlines ├── /content-draft/ # Generated drafts ├── /youtube-title/ # Title ideas ├── /specs/ # Command specifications └── /todos/ # Implementation notes Learn More Watch the interview : I Watched Dan Koe Break Down His AI Workflow OMG Download Greg's guide : gregisenberg.com/content-engine Read Dan's newsletter : future/proof by Dan Koe A Note on "Vibe Coding" Yes, this entire project was vibe coded. No, I'm not sorry. The robots are good at this now. Built with Claude Code. Powered by coffee and existential dread about content calendars.
