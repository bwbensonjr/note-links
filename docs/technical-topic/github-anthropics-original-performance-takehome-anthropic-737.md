---
id: 737
url: https://github.com/anthropics/original_performance_takehome
title: 'GitHub - anthropics/original_performance_takehome: Anthropic&#39;s original
  performance take-home, now open for you to try!'
domain: github.com
source_date: '2026-01-21'
tags:
- github-repo
- llm
summary: Anthropic has released their original performance take-home challenge, a
  coding optimization task where participants attempt to achieve better performance
  (measured in simulated machine cycles) than Claude Opus 4.5's best result of 1487
  cycles. The challenge showcases how various Claude models perform on the task, with
  scores ranging from 2164 cycles (Claude Opus 4) to 1363 cycles (Claude Opus 4.5
  with improved test-time compute), and anyone beating the 1487-cycle threshold is
  encouraged to contact Anthropic about potential interview opportunities.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - anthropics/original_performance_takehome: Anthropic&#39;s original performance take-home, now open for you to try!

Anthropic's Original Performance Take-Home This repo contains a version of Anthropic's original performance take-home, before Claude Opus 4.5 started doing better than humans given only 2 hours. Now you can try to beat Claude Opus 4.5 given unlimited time! Performance benchmarks measured in clock cycles from the simulated machine: 2164 cycles : Claude Opus 4 after many hours in the test-time compute harness 1790 cycles : Claude Opus 4.5 in a casual Claude Code session, approximately matching the best human performance in 2 hours 1579 cycles : Claude Opus 4.5 after 2 hours in our test-time compute harness 1548 cycles : Claude Sonnet 4.5 after many more than 2 hours of test-time compute 1487 cycles : Claude Opus 4.5 after 11.5 hours in the harness 1363 cycles : Claude Opus 4.5 in an improved test time compute harness If you optimize below 1487 cycles, beating Claude Opus 4.5's best performance at launch, email us at performance-recruiting@anthropic.com with your code (and ideally a resume) so we can be appropriately impressed and perhaps discuss interviewing. Run python tests/submission_tests.py to see which thresholds you pass.
