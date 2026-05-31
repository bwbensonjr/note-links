---
id: 1096
url: https://discuss.python.org/t/reverting-the-incremental-gc-in-python-3-14-and-3-15/107014
title: Reverting the incremental GC in Python 3.14 and 3.15 - Core Development - Discussions
  on Python.org
domain: discuss.python.org
source_date: '2026-05-14'
tags:
- python
- compilers
summary: Python 3.14's new incremental garbage collector is being reverted in both
  3.14 and 3.15 due to significant memory pressure issues reported in production environments,
  with the system reverting to the generational GC from 3.13. The decision was made
  by the Python core team and Steering Council, with plans to reintroduce the incremental
  GC for Python 3.16 through the formal PEP process after more thorough evaluation.
  Python 3.14.5 will be released early with the old garbage collector, and an additional
  alpha 9 for 3.15 will be prepared before the first beta release.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Reverting the incremental GC in Python 3.14 and 3.15 - Core Development - Discussions on Python.org

hugovk (Hugo van Kemenade) April 16, 2026, 6:15pm 1 Python 3.14 shipped with a new incremental garbage collector . However, we’ve had a number of reports of significant memory pressure in production environments. We’ve decided to revert it in both 3.14 and 3.15, and go back to the generational GC from 3.13. 3.15 is still in alpha, so such changes are fine. For 3.14, it is unusual for a patch release, but the old GC is a known quantity, the new incremental GC didn’t go through the PEP process, and was rolled back just before the final release of 3.13 . We’ve discussed this in the core team and with the Steering Council. If we want to reintroduce the incremental GC for 3.16, it can go through the regular PEP process and be more thoroughly evaluated. Schedules: 3.15 : The first beta is scheduled for 2026-05-05, just under three weeks from now. If the revert is ready to release within the next week or so, we can put out an extra alpha 9. 3.14 : the next patch release 3.14.5 was planned for 2026-06-09, but we’ll release that early when the revert is ready. I’ll update this topic and the release PEPs when those dates are known. 34 Likes Python 3.14.5 is here, with a new (old) garbage collector! Python 3.14.5 release candidate Improving incremental gc
