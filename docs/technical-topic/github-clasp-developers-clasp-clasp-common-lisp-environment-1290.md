---
id: 1290
url: https://github.com/clasp-developers/clasp
title: 'GitHub - clasp-developers/clasp: clasp Common Lisp environment · GitHub'
domain: github.com
source_date: '2026-08-15'
tags:
- github-repo
- common-lisp
- compilers
- cpp
summary: Clasp is a Common Lisp implementation built on LLVM that enables seamless
  interoperability with C++ libraries and programs, allowing developers to leverage
  existing scientific computing ecosystems while benefiting from Common Lisp's rapid
  prototyping capabilities. The project supports major Common Lisp components like
  SLIME, ASDF, and Quicklisp, and is available on Linux, Mac OS X, and FreeBSD, though
  building from source requires significant computational resources. The development
  team actively welcomes contributions and provides support through GitHub issues
  and an IRC channel.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - clasp-developers/clasp: clasp Common Lisp environment · GitHub

Clasp — Bringing Common Lisp and C++ Together
=============================================

Clasp is a new [Common Lisp](https://common-lisp.net/) implementation that seamlessly interoperates with
C++ libraries and programs using [LLVM](http://llvm.org/) for compilation to native code. This
allows Clasp to take advantage of a vast array of preexisting libraries and
programs, such as out of the scientific computing ecosystem. Embedding them in a
Common Lisp environment allows you to make use of rapid prototyping, incremental
development, and other capabilities that make it a powerful language.

For more information on using Clasp, see:

* [Clasp Manual](https://clasp-developers.github.io/manual.html)
* [clbind Documentation](https://clasp-developers.github.io/clbind-doc.html)

Releases
--------

See [Releases](https://github.com/clasp-developers/clasp/releases) for current releases of Clasp. For more information please
see the [Release Notes](https://github.com/clasp-developers/clasp/blob/main/RELEASE_NOTES.md).

### Building Clasp

At the moment, Clasp is supported on Linux, Mac OS X and FreeBSD. On these
systems, you should be able to build it from source and you may be able to
install using a package manager. See the [Wiki](https://github.com/clasp-developers/clasp/wiki/) for more information.

In case things go wrong, the quickest way to get help is to either
[file an issue](#reporting-problems), or to [chat with us directly](#irc).

Building takes a lot of resources. In parallel mode
(`:parallel-build t` in config.sexp) you need more than 8 GB of RAM
and it will be 1-2 hours build time. If you do not have 8 GB of RAM you can turn off
the parallel build which will then run for a day or so. Make sure to have some
paging space ("swapfile") configured.

There is also docker image [here](https://github.com/clasp-developers/clasp/pkgs/container/clasp).

### Common Lisp Ecosystem Support

Clasp supports the following major components:

* [SLIME](https://common-lisp.net/project/slime/)
* [ASDF](https://common-lisp.net/project/asdf/)
* [Quicklisp](https://www.quicklisp.org/beta/)
* [CFFI](https://common-lisp.net/project/cffi/)
* [Bordeaux-Threads](https://github.com/clasp-developers/clasp/issues/163)
* [Unicode](https://github.com/clasp-developers/clasp/issues/164)

Post on the issues or [contact us](#irc) if you're interested in changing that.

Contributing to Clasp
---------------------

We very much welcome any kind of contribution to Clasp, even if it is just bug
finding and testing. A lot can be done all around the project, if you want to
dive into something large. See the [Contributing](https://github.com/clasp-developers/clasp/blob/main/CONTRIBUTING.md) file for the few guidelines
we've set up around contributions.

Reporting Problems
------------------

Generally you can report problems in two fashions, either by opening a
[New Issue](https://github.com/clasp-developers/clasp/issues/new) or by [chatting with us directly](#irc). In both cases, though,
you should have the following pieces handy in order for us to be able to help
you out as quickly and painlessly as possible:

* Your operating system name and version.
* The branch that you're using of Clasp.
* A paste of the build log or failure point that you reached.
* Patience.

IRC
---

Clasp has an IRC channel on [Libera](https://libera.chat) called #clasp. If you have questions,
problems, suggestions, or generally would like to just hang out with us devs,
come and stop by!

More on Clasp
-------------

For more information on Clasp and the discussion around it, see the following
sites:

* [Christian Schafmeister's blog](https://drmeister.wordpress.com)
* [Hackernews](https://hn.algolia.com/?query=clasp&sort=byPopularity&prefix&page=0&dateRange=all&type=story)
* [Reddit](https://www.reddit.com/r/lisp/search?q=clasp&restrict_sr=on)
* [Google Tech Talks](https://www.youtube.com/watch?v=8X69_42Mj-g)
* [ELS2016](https://www.youtube.com/watch?v=5bQhGS8V6dQ)
* [Lessons Learned Implementing Common Lisp with LLVM](https://www.youtube.com/watch?v=mbdXeRBbgDM)

Acknowledgments
---------------

Clasp was supported by:

* The Defense Threat Reduction Agency (DOD-DTRA) (HDTRA1-09-1-0009)
* The National Institutes of Health (NIH/NIGMS Grant number: 2R01GM067866-07A2)
* The National Science Foundation (Grant number: 1300231)
