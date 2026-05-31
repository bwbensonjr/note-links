---
id: 199
url: https://github.com/felipap/sicp-code
title: 'GitHub - felipap/sicp-code: Digitized code from MIT&#39;s 1986 SICP video
  lectures.'
domain: github.com
source_date: '2025-10-20'
tags:
- github-repo
- scheme
- academic-paper
- tutorial
- compilers
summary: This GitHub repository contains digitized transcriptions of code from MIT's
  1986 SICP video lectures taught by Gerald Sussman and Harold Abelson. The project
  aims to make the lectures' content readable and accessible in digital format, since
  the original video quality (240p-360p) makes it difficult to view the code on slides.
  The code files are annotated with timestamps, comments, and notes to aid comprehension,
  though they represent literal transcriptions and may not compile in standard Scheme
  interpreters.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - felipap/sicp-code: Digitized code from MIT&#39;s 1986 SICP video lectures.

Code in the 1986's MIT SICP lectures
====================================

Lectures by Gerry Sussman and Hal Abelson
=========================================

---

Motivation
----------

MIT lectures on **Structure and Interpretation of Computer Programs**, as taught in 1986 by [Gerald Sussman](http://groups.csail.mit.edu/mac/users/gjs/) and [Harold Abelson](http://groups.csail.mit.edu/mac/users/hal/hal.html), are available online in [youtube](https://www.youtube.com/course?list=ECE18841CABEA24090) and [MIT OCW's website](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-001-structure-and-interpretation-of-computer-programs-spring-2005/video-lectures/). The videos are available in 240p/360p: very poor quality for visualizing the code in the slides. In addition to that, the camera won't fixate on the board for long, making it extremely difficult to follow.

### This is a digitized version of the code featured in the lectures.

This project's intent is to make the lectures' code and content readable (**unlike the slide below**) and available in digital format.

[![Unreadable Slide](https://camo.githubusercontent.com/ba0d1f8632013a0c2eef5d6ec64534a5c9c462d6956c087aef9e294a278666fc/687474703a2f2f692e696d6775722e636f6d2f6e696e304d396e2e706e67 "This is nearly impossible to read")](https://camo.githubusercontent.com/ba0d1f8632013a0c2eef5d6ec64534a5c9c462d6956c087aef9e294a278666fc/687474703a2f2f692e696d6775722e636f6d2f6e696e304d396e2e706e67)

---

Files Syntax and Notation
-------------------------

I tried to maintain consistency of notation, comments and indentation throughout the lectures. Much of the original indentation on the slides was maintained, except for when I was able to improve readability by changing it. Lecture breaks are also noted.

Every `SLIDE`, `TERMINAL` or `BOARD` content is marked with the time of appearance. E.g.

```
;# SLIDE 0:00:00
    ... slide content
;# END SLIDE
```

---

Notes and Observations
----------------------

* I have added comments and remarks throughout the code to help comprehension.
* Though all files have extension .scm, their content represent a literal transcription of the slides, some of which isn't code. **They're expected to fail to compile in all Scheme interpreters.**
* I have fixed the code on a few, rare occasions. In all of them I've noted the correction using a colon followed by an exclamation mark. Notice that ';!' was also used, once or twice, in the lecture slides.

#### A slide might have been ommited because

* it's clearly readable
* it's not code
* its content isn't "textable"

---

### Feel free to create an issue whenever you spot errors in the transcription.

#### Things left to do:

* Standardize syntax and style across the transcription files.

---

Useful Links
------------

* [Official SICP (book) website](http://mitpress.mit.edu/sicp/)
* [Sussman and Abelson's lectures - Official website](http://groups.csail.mit.edu/mac/classes/6.001/abelson-sussman-lectures/)
* [Video lectures hosted by MIT (notice transcripts of the classes are available)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-001-structure-and-interpretation-of-computer-programs-spring-2005/video-lectures/)
* [Course notes from the 2005 lectures](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-001-structure-and-interpretation-of-computer-programs-spring-2005/lecture-notes/)
