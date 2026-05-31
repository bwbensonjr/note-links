---
id: 970
url: https://github.com/white-flame/am
title: 'GitHub - white-flame/am: Douglas Lenat''s AM (Automated Mathematician) from
  SAIL archives circa 1977 · GitHub'
domain: github.com
source_date: '2026-03-30'
tags:
- github-repo
- ai
- lisp
- academic-paper
summary: This GitHub repository contains the restored source code for Douglas Lenat's
  AM (Automated Mathematician), a landmark AI system from 1977 originally developed
  on a PDP-10 computer using Interlisp. The code has been extracted from the SAILDART
  archive and includes the original execution environment details, documentation,
  and notes on loading the various component files, with the software being in the
  public domain as it was government-funded through ARPA.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - white-flame/am: Douglas Lenat's AM (Automated Mathematician) from SAIL archives circa 1977 · GitHub

Douglas Lenat's AM from SAIL archives circa 1977 These files are extracted from the SAILDART archive maintained by Bruce Baumgart, in Douglas Lenat's AM section here: https://www.saildart.org/[AM,DBL]/ The accompanying PhD thesis can be found here: https://apps.dtic.mil/sti/pdfs/ADA155378.pdf Execution environment Quoted from the thesis, page 124: Machine: SUMEX, PDP-10, KI-10 uniprocessor, 256k core memory. Language: Interlisp, January '75 release, which occupies 140k of the total 256k, but which provides a surplus "shadow space" of 256k additional words available for holding compiled code. Notes LT is the initial loader file, which will load the others. While the thesis notes that the file TOP6 will be loaded, at some point this was split into loading TA and TB . The CON6 file is much newer than the others. While I grabbed the newest version, older versions still exist on the archive above and might be required instead. Any other applicable files found in the SAILDART archive such as documentation or demonstration logs should be committed here as well. A general description of the DBL areas can be found in the EURISKO project wiki . This should be in the public domain, or international equivalent, as it was funded by the USA government through ARPA. The thesis additionally encourages others to copy, modify, and use the software. Discord: https://discord.gg/vhsmVCwgvK
