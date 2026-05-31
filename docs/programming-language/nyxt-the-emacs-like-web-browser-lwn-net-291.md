---
id: 291
url: https://lwn.net/Articles/1001773/
title: 'Nyxt: the Emacs-like web browser [LWN.net]'
domain: lwn.net
source_date: '2025-08-14'
tags:
- common-lisp
- web-dev
- github-repo
summary: Nyxt is an unconventional, keyboard-driven web browser written in Common
  Lisp that draws heavy inspiration from Emacs, designed primarily for developers
  who value customization and extensibility. Rather than a traditional graphical interface,
  Nyxt emphasizes command-line functionality and per-buffer customization (modes,
  keybindings, settings), offering users complete control over browser behavior through
  its hackable architecture. The project is transitioning from version 3.x (using
  WebKitGTK) to version 4.0, which will support multiple rendering engines including
  Electron for improved cross-platform performance and macOS/Windows compatibility.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Nyxt: the Emacs-like web browser [LWN.net]

> **We're bad at marketing**
>
> We can admit it, marketing is not our strong suit. Our strength is
> writing the kind of articles that developers, administrators, and
> free-software supporters depend on to know what is going on in the
> Linux world. Please [subscribe today](/Promo/nsn-bad/subscribe) to help us keep doing that, and so
> we don’t have to get good at marketing.

By **Joe Brockmeier**  
June 6, 2025

[Nyxt](https://nyxt.atlas.engineer/) is an unusual web
browser that tries to answer the question, "what if Emacs was a
*good* web browser?". Nyxt is not an Emacs package, but a full
web browser written in Common Lisp and available under the BSD
three-clause license. Its target audience is developers who want a
browser that is keyboard-driven and extensible; Nyxt is also developed
for Linux first, rather than Linux being an afterthought or just a
sliver of its audience. The philosophy (as described in its [FAQ](https://nyxt.atlas.engineer/faq))
behind the project is that users should be able to customize all of
the browser's functionality.

#### Background

Nyxt was started in 2017 by John Mercouris, and is currently
sponsored as a project by [Atlas](https://atlas.engineer/about), which seems to be a
two-person business focusing on Common Lisp development. The team
consists of Mercouris and André
A. Gomes. The [post
about Nyxt's origins](https://nyxt.atlas.engineer/article/article-how-can-i-make-emacs-my-web-browser.org) states that it was built by Emacs users
and developed to provide ""a good Emacs experience while using
the Internet"". It is meant to enable user freedom not only through
its license, but also by focusing on the browser's
""hackability"" so users can fully control the browser:

> Nyxt and Emacs take a different approach than Unix. Instead of doing
> one thing and doing it well, Nyxt and Emacs share a core foundation
> built upon extensibility. They are designed to be introspected,
> changed, and hacked on the fly.

With Emacs being a heavy influence on Nyxt, one might wonder why it
isn't developed as an Emacs package or browser extension rather than as a
standalone project. In 2021, contributor Pedro Delfino and Mercouris
addressed that question in a [blog
post](https://nyxt.atlas.engineer/article/why-building-nyxt-instead-of-an-emacs-package.org). In short, despite all of its merits, Mercouris felt that Emacs
had too much technical debt to make a good basis for a web browser, and
wanted to start with a clean slate. He also wanted to make
Nyxt welcoming to non-Emacs users, which meant that it would be a bad
idea to require people to use Emacs in order to run Nyxt. It should be
noted that Nyxt has support for vi-like keybindings as well as [common
user access](https://en.wikipedia.org/wiki/IBM_Common_User_Access) (CUA) keybindings.

According to their FAQ, it was not possible to develop Nyxt as a
browser extension, either:

> It would not be able to utilize Lisp as a powerful and modern language
> (a source of many of Nyxt's powerful features). Additionally, many of
> Nyxt's features are simply not possible due to restrictions in
> plugin-architecture.

The current stable version of Nyxt is 3.12.0, which was [released](https://github.com/atlas-engineer/nyxt/releases/tag/3.12.0)
in October 2024. The 3.x series uses [WebKitGTK](https://webkitgtk.org/) as its rendering engine,
with experimental support for [Blink](https://en.wikipedia.org/wiki/Blink_(browser_engine)). The
project's [security
policy](https://github.com/atlas-engineer/nyxt/security) is terse and to the point: only the latest stable version
of Nyxt will receive security updates. There is no announcement list
specifically for security issues, and the project requests that
vulnerability reports be sent to hello@atlas.engineer.

The 3.x series appears to be in maintenance mode at this point,
with work focused on a 4.0 release series that was [unveiled](https://github.com/atlas-engineer/nyxt/releases/tag/4.0.0-pre-release-1)
at the end of December. The 4.0 pre-releases support two renderers:
WebKitGTK and [Electron](https://www.electronjs.org/). According to the [blog
post](https://nyxt.atlas.engineer/article/release-4.0.0-pre-release-1.org) by Gomes announcing the first preview release, 4.0 will mark
""a new era for Nyxt"" as a ""renderer-agnostic web
browser"". The project is adding Electron due to shortcomings in
WebKitGTK's performance. This has required the project to improve its
API ""in order to achieve render agnosticism"". The move to
Electron, said Gomes, will provide better performance as well as
support for macOS and Windows.

The latest preview release ([4.0.0-pre-release-8](https://github.com/atlas-engineer/nyxt/releases/tag/4.0.0-pre-release-8))
is only available as an AppImage with Electron as the rendering
engine. Users who wish to use the WebKitGTK version will need to
compile from source. Users should not expect a bunch of new features
or functionality in the first stable 4.0 release; the bulk of the work
seems to be refactoring for Electron support, bug fixes, and
user-interface improvements.

#### Getting Nyxt

The recommended way to install the stable release of Nyxt for Linux
is via [Flatpak](https://flathub.org/apps/engineer.atlas.Nyxt). (Despite
offering an AppImage for preview releases, there is no AppImage for
the stable series.) The project also maintains a list of [packages](https://repology.org/project/nyxt/versions) for a
variety of Linux distributions, but asks that any bugs found in
third-party packages be reported to the distribution rather than the Nyxt
project.

Compiling from source is also an option, of course, and might even
be a necessity. The Nyxt Flatpak package would not run on
Fedora 41 on a system with an NVIDIA card without disabling
WebKit compositing and sandboxing using the following command:

```
    $ flatpak run --env=WEBKIT_DISABLE_COMPOSITING_MODE=1 \
      --env=WEBKIT_DISABLE_SANDBOX_THIS_IS_DANGEROUS=1 \
      engineer.atlas.Nyxt
```

Starting Nyxt with a variable that explicitly informs the user
"this is dangerous" seemed unwise over the long term, so I went ahead
and compiled Nyxt myself for that machine. The [developer
manual](https://github.com/atlas-engineer/nyxt/blob/master/developer-manual.org) has information on dependencies that might be needed and
that are unlikely to be installed by default. To enable copy and paste
functions under Wayland, it will be necessary to install the [Wayland clipboard
utilities](https://github.com/bugaevc/wl-clipboard) in addition to any dependencies needed to compile
Nyxt. On Fedora, this is the wl-clipboard package.

For this article, I primarily used Nyxt 3.12, though I did spend
some time with the 4.0.x preview releases as well. As one might
expect, they are still too unstable to use full-time.

#### Getting started

When Nyxt is started, it displays a page with four buttons:
Quick-Start, Describe-Bindings, Manual,
and Settings. Unlike Chrome, Firefox, and other popular web browsers,
Nyxt does not have a point-and-click interface for all (or even most)
of its features; the expectation is that users are going to do almost
everything from the keyboard, and much of Nyxt's functionality is
*only* accessible by using key combinations or entering
commands. Users can still use the mouse to click links, etc., but
there are no buttons to open new windows, add bookmarks, and no URL
bar or location bar to type "lwn.net" into.

The quick start introduces some of the concepts that set Nyxt
apart from other browsers. Instead of tabs, Nyxt has [buffers](https://nyxt.atlas.engineer/documentation#buffers). In
practice, buffers are similar to tabs, except that a Nyxt buffer can
have its own behavior and settings. For instance, users can set a
buffer's keybindings individually to use a different set than the
global default. Likewise, a buffer can use different [modes](https://nyxt.atlas.engineer/documentation#modes)—which
are similar to Emacs modes.

Nyxt commands are invoked with keybindings or by bringing up the
[prompt
buffer](https://nyxt.atlas.engineer/documentation#prompt-buffer) and typing the command to be used. Users can summon the
prompt buffer with Ctrl-Space and Alt-x if using
Emacs mode or : in vi mode. Users can see the modes that are
enabled in a buffer by bringing up the prompt buffer and using the
toggle-modes command.

> [![[Nyxt with prompt buffer open]](https://static.lwn.net/images/2025/nyxt-sm.png "Nyxt with prompt buffer open")](/Articles/1023878/)

The Settings page, which can be opened from the Nyxt start page or
by running the common-settings command in the prompt buffer,
has several tabs for configuring high-level Nyxt options. These include the browser's
default keybindings, the theme (dark or light), its privacy settings,
and the text editor. Nyxt comes with an ad-blocker mode, but it needs to be enabled in
the privacy settings. Users can also set the cookie policy, turn on
the reduce-tracking mode, and turn off JavaScript if desired with the
no-script mode. And, of course, each of
these settings can be enabled or disabled on a per-buffer basis as well.

Even though Nyxt developers have a strong preference for Emacs, it
is set to use CUA keybindings by default. Folks who prefer Emacs or
vi-like bindings will want to change the keybinding setting and
restart the browser for that to take effect. (Note that users can
change the keybindings (or other modes) in a buffer without having to
restart—a restart is only required for the global setting.) It's
best to do this early, rather than committing the CUA keybindings to
memory and then relearning them later for vi or Emacs. It will likely
make Nyxt more intuitive as well—I
found that it was relatively easy to make the move from [Firefox with
Vimium](https://lwn.net/Articles/1005332/#vimium) to Nyxt. The CUA bindings, aside from some familiar ones
like Ctrl-l to enter a URL to browse to, were much harder
(for me, anyway) to commit to memory.

Over the years, a lot of work has been done to reduce the amount of
space that is taken up by browser "chrome"—that is, the
user-interface components (UI) such as window title bars, toolbars,
tabs, and so forth—to maximize the amount of space available for
the web pages being viewed. Nyxt solves this by having almost no UI at
all while browsing, though there are a few tiny buttons in a small
toolbar at the bottom of the Nyxt window. The toolbar has elements for
navigating backward or forward, reloading the page, raising the
command prompt, and for displaying the modes enabled in each
buffer. Nyxt also has a minimal right-click menu that lets users move
one page backward or forward in a buffer, reload a buffer, or bring up
the [WebKit Inspector tools](https://webkit.org/web-inspector/).

One feature Nyxt has that other browser makers should copy is the
history tree. Running the history-tree command will bring up
a navigable tree-type visualization of the browser's history across
all buffers. This not only lets users trace their steps and quickly hop
back (or forward) to pages they've visited, Nyxt can operate on the
history with other commands, such as bookmark-buffer-url to
bookmark pages that are currently open in the browser.

Just as with Emacs and Vim, users can operate on multiple buffers
at once. After a long browsing session, for instance, one might have
20 pages open from Wikipedia after going down a rabbit hole about a
topic. Open the command buffer, enter the delete-buffer
command, and Nyxt will list all open buffers. Type "wikipedia" and it
will list only those buffers that match the term; select each one and
hit Enter, and they will all be closed. The same is true for
other commands, of course. Instead of closing all buffers, a user
could choose to bookmark all pages matching certain terms, or to use
the print-buffer command to send them all to the printer.

#### Extending Nyxt

Firefox and Chrome allow developers to add features to the browser
as extensions, but there are limits to what developers can do within
the boundaries of the extension frameworks for each browser. Nyxt, on
the other hand, is designed to be entirely customizable and extensible
via Lisp. Nyxt targets the [Steel Bank
Common Lisp](https://www.sbcl.org/) (SBCL) implementation. Users can create their own [URL-dispatchers](https://nyxt.atlas.engineer/documentation#url-dispatchers)
to configure applications to handle certain types of URLs, or even
create [custom
URL scheme handlers](https://nyxt.atlas.engineer/documentation#custom-url-schemes) to deal with URL schemes that Nyxt doesn't know
about. Users can also create [custom
commands](https://nyxt.atlas.engineer/documentation#custom-commands), add new menu entries to the right-click menu, and (of
course) [add
and modify keybindings](https://nyxt.atlas.engineer/documentation#keybinding-configuration). Nyxt also features a [built-in
REPL](https://nyxt.atlas.engineer/documentation#built-in-repl) to run Lisp code in the browser.

Nyxt will automatically load configurations and code from the
user's config.lisp file, usually found under
~/.config/nyxt. As a short example, this code will add an
item to the right-click menu to bookmark the current page:

```
    (define-command-global my-bookmark-url
        nil
      "Query which URL to bookmark."
      (let ((url
             (prompt :prompt "Bookmark URL" :sources
                     'prompter:raw-source)))
        (nyxt/mode/bookmark:bookmark-current-url)))
    
    (ffi-add-context-menu-command 'my-bookmark-url "Bookmark")
```

One of the great things about both Emacs and Vim is that each editor has
a large community of users, many of whom like to share their knowledge
about using and extending their editor of choice. New users can find
copious amounts of documentation and examples online to learn from or
copy and modify as needed. The odds are that anything one might want
to do with Emacs or Vim has already been done and blogged about with
examples for others to copy.

That is decidedly not true of Nyxt, at least not yet. There are not
many people blogging about Nyxt and few examples online that I could
find. Few, but not zero. Artyom Bologov has a [repository](https://github.com/aartaka/nyxt-config/tree/master)
with a treasure-trove of Nyxt configuration files, as well as a [separate
repository](https://github.com/aartaka/nx-search-engines/tree/master) for adding search engines to Nyxt. These are bound to
be helpful for many new Nyxt users, but the bad news is that Bologov
[stopped using
Nyxt](https://www.aartaka.me.eu.org/nyxt-to-surf) in favor of the [surf](https://surf.suckless.org/)
browser from [suckless.org](https://suckless.org/). The
examples are still useful today, but will become less so as Nyxt
evolves.

Nyxt also lacks the kind of extension ecosystem that other browsers
enjoy. It is possible to create extensions for Nyxt, but the project
only lists [two
extensions](https://nyxt.atlas.engineer/extensions) currently—and both are created by Atlas.

#### Notes on Nyxt

It takes some time to get used to using Nyxt after using a browser
like Chrome or Firefox full-time. It took several sessions with Nyxt
before I felt productive with it, and a few more to really appreciate
its features.

Nyxt's performance is notably slower than Firefox or Chrome on some
sites. For example, using the date-picker widget on GitHub, posting
content to Mastodon, and browsing [Codeberg](https://codeberg.org/) was sluggish compared
to Firefox. Nyxt is probably not suitable as a primary browser
replacement if one's work (or play) involves a lot of JavaScript-heavy
web applications. It also [lacks WebRTC
support](https://nyxt.atlas.engineer/faq#:~:text=WebRTC), so users need to look elsewhere for video
conferencing.

On the other hand, it's quite usable for most of my day-to-day work
with LWN and performs well on sites, like [sourcehut](https://sr.ht/), that have minimal JavaScript. It
seems likely it would be a suitable option as a primary browser for
many system administrators and developers.

The Electron port should offer a better experience once it has
stabilized. I tried it on GitHub and Mastodon and didn't experience
the same slowdowns that I ran into with the stable series.

Nyxt has an [online manual](https://nyxt.atlas.engineer/documentation) that
is also included with the browser to help users dig more deeply into its
functionality. It is only fully usable when viewed with Nyxt; links to
commands and functions are prefixed with nyxt: to point to
internal documents, so they do not work when viewed with other
browsers from the Nyxt web site. Unfortunately, the manual is outdated
in spots, and that can lead to frustration. As an example, it explains
how users can [customize
settings with the "Configure" button](https://nyxt.atlas.engineer/documentation#configuration), but that [feature was
removed](https://github.com/atlas-engineer/nyxt/issues/3487).

It's not entirely surprising that the documentation has fallen out
of date in places: Nyxt is an ambitious project and only has a few
active developers. Only seven people have
contributed to the [Nyxt repository on
GitHub](https://github.com/atlas-engineer/nyxt) since June 4 last year, with Mercouris and Gomes
responsible for all but 13 of the 633 commits; one of the other
contributors has nine commits, the rest only have one each.

The 4.0 series does not have a target date for a stable release,
but a list of [GitHub
issues tagged for the 4.0 series](https://github.com/atlas-engineer/nyxt/issues?q=is:issue%20label:4-series) suggests that the project is
making good progress toward it. There are currently 17
open issues and 46 closed issues, and there have been 4.0.0
development versions released about every two to three weeks since
December.

Nyxt has received some funding from the European Union's [Next Generation Internet](https://www.ngi.eu/) initiative
and has a plan to raise additional funding by [selling
applications](https://nyxt.atlas.engineer/article/sustainable-open-source.org) that use Nyxt as an application framework. The first
application is an RSS feed reader called [Demeter](https://nyxt.atlas.engineer/extension/demeter.org). It
is not open source, but it is offered under a "pay-what-you-can"
model, with a suggested price of $10—and a link to a [direct
download](https://nyxt.atlas.engineer/extension/demeter.org/download) to the source for users who cannot afford to pay. As a
business strategy, Atlas's approach is fairly user-friendly but unlikely
to generate a huge revenue stream.

Like Emacs and Vim, Nyxt is not for everyone—it takes more
time than most would want to invest to really explore the features it
has to offer and even longer to start making it one's own through
customization. Also, like Emacs and Vim, it has the promise of letting
users mold the application exactly to their specifications if they are
willing to expend the time and effort to do so.

  

---
