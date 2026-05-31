---
id: 484
url: https://github.com/mrkline/modern-latex
title: 'GitHub - mrkline/modern-latex: A short guide to LaTeX that avoids legacy cruft.'
domain: github.com
source_date: '2025-05-05'
tags:
- github-repo
- tutorial
summary: '"Modern LaTeX" is a contemporary guide to LaTeX that strips away outdated
  conventions and focuses on modern best practices for typesetting. The guide uses
  LuaLaTeX (a Unicode-aware version) and provides practical instructions for building
  the document while avoiding legacy complexity that has accumulated over LaTeX''s
  four-decade history. The author welcomes feedback and provides the guide as a PDF
  resource to help users create beautiful documents without getting bogged down in
  irrelevant technical details.'
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - mrkline/modern-latex: A short guide to LaTeX that avoids legacy cruft.

Modern LaTeX LaTeX is a tool for creating beautiful writing, or a torture device that drives users to the brink of madness every time they see bad spacing for the rest of their lives. One of the two. Despite origins that can be traced back four decades, it remains one of the best typesetting programs around. Many of its guides, however, haven't aged as well. This short book will get you started with LaTeX without bogging you down in arcana that lost its relevance back in the 90s. Where do I get it? An up-to-date version should be available at https://assets.bitbashing.io/modern-latex.pdf How do I build it? Install LuaLaTeX, a modern, Unicode-aware version of LaTeX. On Linux, this is usually as simple as installing your distro's TeX Live package, e.g., texlive-base or texlive-core . The same package should also provide the latexmk script. (See below) Check out the online branch of the source repository, which is optimized for digital display instead of a printed book. Changes include even margins, centered page numbers, a lack of blank pages between chapters, and so on. Change the fonts as-needed. The official version of this book is typeset with Garamond Premier, Neue Haas Grotesk, URW Futura, Drive Mono, Noto, and (of course) Latin Modern. In the likely case that you don't have all of these typefaces, change the fontspec commands (e.g., setmainfont , etc.) appropriately, then modify or remove the colophon at the back of the book. Build the book using latexmk -lualatex -latexoption=-halt-on-error modern-latex.tex Note that latexmk will run LuaLaTeX multiple times, since TeX generates cross references in one pass, then links them in a second. If you can't use latexmk for some reason, you can manually invoke lualatex -halt-on-error -shell-escape modern-latex.tex until it no longer warns, "Label(s) may have changed. Rerun to get cross-references right." Feedback ...is welcome! Please issue pull requests on this book's Github page, or contact the author via matt <at> bitbashing.io Enjoy!
