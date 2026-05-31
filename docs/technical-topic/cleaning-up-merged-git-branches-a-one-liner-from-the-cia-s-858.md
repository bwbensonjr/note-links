---
id: 858
url: https://spencer.wtf/2026/02/20/cleaning-up-merged-git-branches-a-one-liner-from-the-cias-leaked-dev-docs.html
title: 'Cleaning up merged git branches: a one-liner from the CIA''s leaked dev docs
  | spencer.wtf'
domain: spencer.wtf
source_date: '2026-02-20'
tags:
- cli-tool
- tutorial
- devops
summary: The article describes a git one-liner command discovered in CIA developer
  documentation that efficiently deletes all merged branches from a local repository
  while protecting the current branch and key branches like main or develop. The command
  uses `git branch --merged`, `grep`, and `xargs` to automatically clean up stale
  branches in bulk, saving developers time compared to manual deletion. The author
  recommends creating a git alias for this command to streamline regular repository
  maintenance.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Cleaning up merged git branches: a one-liner from the CIA's leaked dev docs | spencer.wtf

In 2017, WikiLeaks published Vault7 - a large cache of CIA hacking tools and internal documents. Buried among the exploits and surveillance tools was something far more mundane: a page of internal developer documentation with git tips and tricks . Most of it is fairly standard stuff, amending commits, stashing changes, using bisect. But one tip has lived in my ~/.zshrc ever since. The Problem Over time, a local git repo accumulates stale branches. Every feature branch, hotfix, and experiment you’ve ever merged sits there doing nothing. git branch starts to look like a graveyard. You can list merged branches with: git branch --merged But deleting them one by one is tedious. The CIA’s dev team has a cleaner solution: The original command git branch --merged | grep -v "\*\|master" | xargs -n 1 git branch -d How it works: git branch --merged — lists all local branches that have already been merged into the current branch grep -v "\*\|master" — filters out the current branch ( * ) and master so you don’t delete either xargs -n 1 git branch -d — deletes each remaining branch one at a time, safely (lowercase -d won’t touch unmerged branches) The updated command Since most projects now use main instead of master , you can update the command and exclude any other branches you frequently use: git branch --merged origin/main | grep -vE "^\s*(\*|main|develop)" | xargs -n 1 git branch -d Run this from main after a deployment and your branch list goes from 40 entries back down to a handful. I keep this as a git alias so I don’t have to remember the syntax: alias ciaclean='git branch --merged origin/main | grep -vE "^\s*(\*|main|develop)" | xargs -n 1 git branch -d' Then in your repo just run: ciaclean Small thing, but one of those commands that quietly saves a few minutes every week and keeps me organised.
