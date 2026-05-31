---
id: 494
url: https://github.com/PhialsBasement/Chain-of-Recursive-Thoughts
title: 'GitHub - PhialsBasement/Chain-of-Recursive-Thoughts: I made my AI think harder
  by making it argue with itself repeatedly. It works stupidly well.'
domain: github.com
source_date: '2025-04-29'
tags:
- github-repo
- ai
- llm
- python
summary: Chain of Recursive Thoughts (CoRT) is a technique that improves AI model
  reasoning by having the model generate multiple alternative responses, evaluate
  them against each other, and iteratively refine its answer through multiple "thinking
  rounds." Testing with Mistral 3.1 24B showed significant performance improvements,
  particularly on programming tasks, demonstrating that this self-critique and competitive
  refinement approach substantially enhances AI output quality. The project is open-source
  and available for use through a web UI or command-line interface.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - PhialsBasement/Chain-of-Recursive-Thoughts: I made my AI think harder by making it argue with itself repeatedly. It works stupidly well.

CoRT (Chain of Recursive Thoughts) 🧠🔄 TL;DR: I made my AI think harder by making it argue with itself repeatedly. It works stupidly well. What is this? CoRT makes AI models recursively think about their responses, generate alternatives, and pick the best one. It's like giving the AI the ability to doubt itself and try again... and again... and again. Does it actually work? YES. I tested it with Mistral 3.1 24B and it went from "meh" to "holy crap", especially for such a small model, at programming tasks. How it works AI generates initial response AI decides how many "thinking rounds" it needs For each round: Generates 3 alternative responses Evaluates all responses Picks the best one Final response is the survivor of this AI battle royale How to use the Web UI(still early dev) Open start_recthink.bat wait for a bit as it installs dependencies profit?? If running on linux: pip install -r requirements.txt cd frontend && npm install cd .. python ./recthink_web.py (open a new shell) cd frontend npm start Examples Mistral 3.1 24B + CoRT Mistral 3.1 24B non CoRT Try it yourself pip install - r requirements . txt export OPENROUTER_API_KEY = "your-key-here" python recursive - thinking - ai . py The Secret Sauce The magic is in: Self-evaluation Competitive alternative generation Iterative refinement Dynamic thinking depth Star History(THANK YOU SO MUCH) Contributing Found a way to make it even better? PR's welcome! License MIT - Go wild with it
