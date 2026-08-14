---
id: 1261
url: https://blog.djhaskin.com/blog/muxxy-like-slime-for-ai-tmux/
title: 'Muxxy: Like Slime, for AI + Tmux — Dan''s Musings'
domain: blog.djhaskin.com
source_date: '2026-08-14'
tags:
- cli-tool
- ai
- common-lisp
- python
- ruby
summary: Muxxy is a new CLI tool that enables AI assistants to interact with REPLs
  (read-eval-print loops) through tmux, inspired by the vim-slime plugin's functionality.
  The author developed it after struggling to get AI tools to effectively interact
  with Common Lisp and other languages' REPLs, addressing limitations of previous
  solutions like MCP servers and Swank. The tool comes with built-in support for SBCL,
  Python, iPython, and Ruby, along with a customizable prompt flag, and includes an
  AI skill that guides language models on how to use it effectively.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Muxxy: Like Slime, for AI + Tmux — Dan's Musings

Muxxy: Like Slime, for AI + Tmux
================================

Published on August 14, 2026

Discovering Jpalardy's [Like Slime, for Vim](https://technotales.wordpress.com/2007/10/03/like-slime-for-vim/) was a revelation to me. I could have *any* repl in my editor? *Whether it knew it was there or not?* It also served as [the basis for my daily driver for writing Common Lisp](https://blog.djhaskin.com/blog/developing-common-lisp-using-vim-with-tmux-or-conemu/) more recently. As I wrote in that post, not only were for-purpose REPL tools complicated, they simply didn't measure up to the functionality I could get out of `vim-slime`.

I missed this switch-out-a-repl functionality when I started moving into the AI era with my hobby coding. I wrote about [how frustrating it was to write Common Lisp](https://blog.djhaskin.com/blog/writing-lisp-is-ai-resistant-and-im-sad/). Looking back, it was mostly because I couldn't effectively have the AI interact with the REPL. Folks on reddit from when I posted that turned me on to [cl-mcp](https://github.com/cl-ai-project/cl-mcp), and I have since learned there were others like it. That worked well enough, but after reading [Mario's post](https://mariozechner.at/posts/2025-11-02-what-if-you-dont-need-mcp/) about skills-over-mcp AND trying [freebuff](https://freebuff.com/) for the first time (it doesn't support MCP), I finally figured I needed a CLI solution.

First, I wrote [swanky](https://github.com/djha-skin/swanky), and that worked a treat, but it required a lisp Swank server running. This had a couple problems. First, if my lisp code printed to standard out, it wouldn't get captured, or it didn't seem so. Second, I had to keep spinning up swank servers and staying on top of making sure the AI had one available. That got old.

I had previously tried building an MCP server for interacting with REPLs over MCP called [tmux-repl-mcp](https://github.com/djha-skin/tmux-repl-mcp). It worked, but I hadn't quite gotten the chops in my AI journey yet around getting the AI to use it right. I didn't realize when I wrote it that you needed to write a skill or the AI wouldn't use the tool right.

The time was right to make that a CLI tool, so I had the AI rewrite it in Rust this morning. The new tool is called [muxxy](https://github.com/djha-skin/muxxy), and it works *really well*!

![image.png](https://mataroa.blog/images/f567a68f.png)

It comes with a skill in its `.agents` folder that tells the AI how to use it. It is capable of spinning up SBCL, Python, iPython, and Ruby shells out of the box, but there's also a custom `--prompt` flag the AI can use to tell the AI what output to look for when scraping from tmux.

I look forward to using this tool for many of my projects, including REPL-intensive ones like Common Lisp, but it would work equally well for anything else -- Clojure, Janet, Julia, Python, Elixir, a custom CL implementation. That old "possibilities are endless" feeling of excitement I felt when I discovered `vim-slime` is back!
