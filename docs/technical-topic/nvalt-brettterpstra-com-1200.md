---
id: 1200
url: https://brettterpstra.com/projects/nvalt/
title: nvALT - BrettTerpstra.com
domain: brettterpstra.com
source_date: '2026-07-06'
tags:
- cli-tool
- github-repo
summary: nvALT is a retired fork of Notational Velocity, a keyboard-driven note-taking
  application that allows users to quickly create, search, and organize notes with
  features like MultiMarkdown support, tagging, and full-text search. The app, developed
  by Brett Terpstra and David Halter, is being replaced by a new application called
  nvUltra, and users are encouraged to report issues on GitHub rather than through
  other channels. nvALT offers customizable interfaces, multiple color schemes, and
  browser extensions for clipping content directly into notes.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# nvALT - BrettTerpstra.com

> FYI, this project is listed as "retired." It may no longer function or I may
> just not be updating it anymore.

* [Support](https://github.com/ttscoff/nv/issues)
* [Download](#dl)

---

A new app is coming to replace nvALT: [*nvUltra*](https://nvultra.com/). Sign up here for updates [here.](https://nvultra.com/sendy/subscription?f=jdr8924PQl36eFlj9cMCdIww3rfhoNX35Q3LcqcPIdS7GsZr763Hme0Zas2slk8Vb4ke)

*Here’s a [great introduction to nvALT in French](http://aya.io/blog/nvalt-prise-de-notes/).*

nvALT 2 is a fork of the original [Notational Velocity](http://notational.net/) with some additional features and interface modifications, including MultiMarkdown functionality. It has been developed by [Elastic Threads](http://elasticthreads.tumblr.com/) (David Halter) and [Brett Terpstra](http://brettterpstra.com), and made available for free (donations accepted).

> *Please [report issues on GitHub](https://github.com/ttscoff/nv/issues/), **not** on Twitter or via email. It helps keep everything manageable and avoids us having to answer the same questions in a hundred different tweets and messages. Along the same lines, please take a look at existing tickets before starting a new one.*

* [What it is](#whatitis)
* [Notational Velocity Features](#notational-velocity-features)
* [nvALT Additional Features](#additional)
* [Installation](#install)
* [Customization](#custom)
* [PPC/Tiger support](#ppc)
* [Help/Support](#support)
* [Download](#dl)
* [Browser Extensions](#extensions)
* [Source code](#source)
* [Additional Credits](#credits)

What it is
----------



Notational Velocity is a way to take notes quickly and effortlessly using just your keyboard. You press a shortcut to bring up the window and just start typing. It will begin searching existing notes, filtering them as you type. You can use `⌘`+`J` and `⌘`+`K` to move through the list. Enter selects and begins editing. If you’re creating a new note, you just type a unique title and press enter to move the cursor into a blank edit area. Check out the descriptions at [notational.net](http://notational.net/) for a more eloquent synopsis.

Want a great primer on using nvALT? See Michael Schechter’s [nvALT 101](http://bettermess.com/plain-text-primer-nvalt-101/).

Notational Velocity Features
----------------------------

* Option for horizontal layout with multi-line previews in notes list
* Words between [[double-brackets]] will become links to other notes
* Tags are synced to Dropbox and searched by Spotlight, via OpenMeta
* Tags are auto-completed while typing in the tag-entry field
* TaskPaper-compatible strikethrough formatting using the “@done” tag
* Fully plain-text-based automatic list-bullet formatting
* Note-titles inside double-brackets are (optionally) auto-completed
* “Show in Finder” command for revealing selected note-files on disk
* Highlighting of search terms can be disabled
* Dragging the divider to the top or left of the window will hide search field
* and more <http://notational.net/releasenotes/release2/>
* Open in external text editor

nvALT Additional Features
-------------------------

* **NEW:** Auto-pairing and selection wrapping for brackets and quotes ([],(),””,’’)
* **NEW:** Pin a note to the preview while editing other notes
* **NEW:** Shortcut (CMD-Shift-L) for inserting [[Links]]
* **NEW:** Better MultiMarkdown 3 support (if installed locally)
* **NEW:** Right to Left support
* **NEW:** External editor support improved
* **NEW:** Simplenote Tag sync[1](#fn:tagsync)
* Textile and (Multi)Markdown support with Preview window (hold down Control to view temporarily)
* HTML source code tab in the Preview window for fast copy/paste to blogs, etc.
* Unique interface design changes
* Customizable HTML and CSS files for the Preview window
* Social note sharing via [Peggd](http://peg.gd)
* Convert imported URLs to Markdown, and optionally strip excess content with Readability
* Multi-note tagging with autocompletion
* Full-screen mode (requires OS X 10.5 or higher)
* Optional menubar and menubar-only modes
* Color schemes
  + Black/White
  + Low-contrast
  + User customizable
* Collapse/Expand notes list and search field
* Improved readability with optional width limit and margins
* Really cool scrollbars
* Word Count (hold down Option to view temporarily)
* Working localizations (French, German, Portuguese)

Installation
------------

Just download the file, double-click to unzip, then drag to your Applications folder.

If you’ve been using the original (or another fork of) Notational Velocity, you can install nvALT (which has the same application name) alongside the original application. nvALT uses its own preference file and database as of version 2.0. Previous users of Notational Velocity or nvALT will be greeted with the default settings when they first launch 2.0, and will need to set up preferences for color, sync, etc. again.

If you have a custom version of MultiMarkdown installed in ~/Library/Application Support/MultiMarkdown, nvALT will use it. If you don’t, it will just use its bundled version. No problem!

Customization
-------------

After the first time you run the Preview window, look in `~/Library/Application Support/Notational Velocity` and you’ll find two files: `template.html` and `custom.css`. If you’re handy with HTML and CSS, feel free to customize these in whatever way you like. You can add Javascript as well, but you’ll need to load external scripts from a url or using a full file:// path. If worse comes to worst, you can just delete or rename your customizations and the default files will be put back in place automatically.

PPC/Tiger support
-----------------

**Note: Apparently our build is not particularly PowerPC compatible. Since we don’t have PPC machines to test on, it’s difficult to provide compatibility for them. We’ll do our best. In the meantime, it’s probably best for PPC users to hold off or use this experimentally only.**

If you tried v2.1 and found yourself up a creek, here’s the [2.0 download link](http://abyss.designheresy.com/files/nvALT2.0.zip).

Help/Support
------------

Please file any and all issues, questions, feature requests and suggestions in the [GitHub issue tracker](https://github.com/ttscoff/nv/issues). We will respond to tickets as soon as we are able.

Download
--------

See the [announcement post](/nvalt-2-2-public-beta/) for more details on the current version (2.2b).

#### nvALT v2.2.8 (128)

[Download nvALT v2.2.8 (128)](https://updates.designheresy.com/nvalt/nvALT2.2.8128.dmg "Download nvALT v2.2.8 (128)")

A fork of Notational Velocity with MultiMarkdown preview and advanced Markdown editing capabilities. Other good stuff.

Published 06/08/13.

Updated 09/19/17. Changelog

[Donate](/donate/) • [More info…](/projects/nvalt/ "More information on nvALT")

nvALT has its own update stream, so running Check for Updates from the application menu will give you updates only for this fork.

---

A new app is coming to replace nvALT: [*nvUltra*](https://nvultra.com/). Sign up here for updates [here.](https://nvultra.com/sendy/subscription?f=jdr8924PQl36eFlj9cMCdIww3rfhoNX35Q3LcqcPIdS7GsZr763Hme0Zas2slk8Vb4ke).

---
