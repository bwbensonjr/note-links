---
id: 1074
url: https://www.gnu.org/software/stow/
title: 'Stow

  - GNU Project - Free Software Foundation'
domain: www.gnu.org
source_date: '2026-04-27'
tags:
- cli-tool
- devops
summary: GNU Stow is a free software tool that manages symlink farms, allowing separate
  software packages stored in different directories to appear as if they're installed
  in a unified location—making it particularly useful for organizing system-wide and
  per-user software installations from source code. The tool is implemented as a Perl
  script with a command-line interface and is licensed under the GNU General Public
  License, with the latest version (2.4.1) released in September 2024 featuring bug
  fixes and improvements. Users can access documentation, contribute to development,
  and report issues through the project's mailing lists and Savannah repository.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Stow
- GNU Project - Free Software Foundation

[**Skip to main text**](#content)

[JOIN THE FSF](https://www.fsf.org/associate/support_freedom?referrer=4052)

[![ [A GNU head] ](/graphics/heckert_gnu.transp.small.png)**GNU** Operating System](/)  
Supported by the
[Free Software Foundation](#mission-statement)

[![ [Search www.gnu.org] ](/graphics/icons/search.png)](//www.gnu.org/cgi-bin/estseek.cgi)



[Site navigation](#navigation "More...")
[**Skip**](#content)

* [ABOUT GNU](/gnu/gnu.html)
* [PHILOSOPHY](/philosophy/philosophy.html)
* [LICENSES](/licenses/licenses.html)
* [EDUCATION](/education/education.html)
* =
  [SOFTWARE](/software/software.html)

  =
* [DISTROS](/distros/distros.html)
* [DOCS](/doc/doc.html)
* [MALWARE](/proprietary/proprietary.html)
* [HELP GNU](/help/help.html)
* [AUDIO & VIDEO](/audio-video/audio-video.html)
* [GNU ART](/graphics/graphics.html)
* [FUN](/fun/humor.html)
* [GNU'S WHO?](/people/people.html)
* [SOFTWARE DIRECTORY](//directory.fsf.org)
* [HARDWARE](https://h-node.org/)
* [SITEMAP](/server/sitemap.html)



GNU Stow
--------

---

GNU Stow is a symlink farm manager which takes distinct packages
of software and/or data located in separate directories on the
filesystem, and makes them appear to be installed in the same place.
For example, `/usr/local/bin` could contain symlinks to
files within `/usr/local/stow/emacs/bin`,
`/usr/local/stow/perl/bin` etc., and likewise recursively
for any other subdirectories such as `.../share`,
`.../man`, and so on.

This is particularly useful for keeping track of system-wide and
per-user installations of software built from source, but
[can
also facilitate a more controlled approach to management of configuration
files in the user's home directory](http://brandon.invergo.net/news/2012-05-26-using-gnu-stow-to-manage-your-dotfiles.html), especially when
[coupled
with version control systems](http://lists.gnu.org/archive/html/info-stow/2011-12/msg00000.html).

Stow is implemented as a combination of a [Perl](http://www.perl.org/) script providing a CLI interface,
and a [backend Perl
module](http://search.cpan.org/dist/Stow/) which does most of the work. Stow is [Free Software](http://www.gnu.org/philosophy/free-sw.html),
licensed under the [GNU
General Public License](http://www.gnu.org/copyleft/gpl.html).

### Latest news

*Sun 8 September 2024*
:   Stow 2.4.1 has been released. This release contains some
    minor bug-fixes — specifically, fixing
    the `--dotfiles` option to work correctly with ignore
    lists, allowing options in `.stowrc` with spaces, and
    avoiding a spurious warning on Perl >= 5.40. There were also some
    clean-ups and improvements, mostly internal and not visible to
    users.
    [Read
    details of what's new.](http://git.savannah.gnu.org/cgit/stow.git/tree/NEWS)

*Sun 7 April 2024*
:   Stow 2.4.0 has been released. This release contains some
    much-wanted bug-fixes — specifically, fixing the `--dotfiles`
    option to work with `dot-foo` directories, and avoiding
    a spurious warning when unstowing. There were also very many clean-ups
    and improvements, mostly internal and not visible to users.
    [Read
    details of what's new.](http://git.savannah.gnu.org/cgit/stow.git/tree/NEWS)

### Downloading Stow

Stow
can be found on the main GNU ftp server:
<http://ftp.gnu.org/gnu/stow/>
(via HTTP) and
<ftp://ftp.gnu.org/gnu/stow/>
(via FTP). It can also be found
on the [GNU mirrors](/prep/ftp.html);
please
[use
a mirror](http://ftpmirror.gnu.org/stow/) if possible.

There is also a [git repository](https://savannah.gnu.org/git/?group=stow)
containing the latest development code.

### Documentation

[Documentation for
Stow](manual/)
is available online, as
is [documentation for most GNU software](/manual/). You may
also find more information about
Stow
by running
*info stow*
or
*man stow*,
or by looking at
*/usr/share/doc/stow/*,
*/usr/local/doc/stow/*,
or similar directories on your system. A brief summary is available by
running *stow --help*.

### Mailing lists

Stow
has the following mailing lists:

* [help-stow](https://lists.gnu.org/mailman/listinfo/help-stow) is
  for general user help and discussion.
* [stow-devel](https://lists.gnu.org/mailman/listinfo/stow-devel)
  is used to discuss most aspects of
  Stow,
  including development and enhancement requests.
* [bug-stow](https://lists.gnu.org/mailman/listinfo/bug-stow)
  is for bug reports.

Announcements about
Stow are posted to
[info-stow](http://lists.gnu.org/mailman/listinfo/info-stow)
and also, as with most other GNU software, to
[info-gnu](http://lists.gnu.org/mailman/listinfo/info-gnu)
([archive](http://lists.gnu.org/archive/html/info-gnu/)).

Security reports that should not be made immediately public can be
sent directly to the maintainer. If there is no response to an urgent
issue, you can escalate to the general
[security](http://lists.gnu.org/mailman/listinfo/security)
mailing list for advice.

The Savannah project also has a
[mailing lists](https://savannah.gnu.org/mail/?group=stow) page.

### Getting involved

Development of
Stow,
and GNU in general, is a volunteer effort, and you can contribute. For
information, please read [How to help GNU](/help/). If you'd
like to get involved, it's a good idea to join the [stow-devel](https://lists.gnu.org/mailman/listinfo/stow-devel) mailing
list.

Bug reporting
:   Please send bug reports to the
    [bug-stow](https://lists.gnu.org/mailman/listinfo/bug-stow)
    mailing list (see [Mailing lists](#mail) above).

Development
:   For [development sources](https://savannah.gnu.org/git/?group=stow) and other
    information, please see the
    [Stow
    project page](http://savannah.gnu.org/projects/stow/)
    at [savannah.gnu.org](http://savannah.gnu.org).
    There is also a [stow-devel](https://lists.gnu.org/mailman/listinfo/stow-devel)
    mailing list (see [Mailing lists](#mail) above).

Translating Stow
:   Stow is not currently multi-lingual, but patches would be
    gratefully accepted. Please e-mail [stow-devel](https://lists.gnu.org/mailman/listinfo/stow-devel)
    if you intend to work on this.

Maintainers
:   Stow
    is currently being maintained by Adam Spiers.
    Please use the mailing lists for contact.

### Licensing

Stow
is free software; you can redistribute it and/or modify it under the
terms of the [GNU General Public License](http://www.gnu.org/licenses/gpl.html) as published by the Free
Software Foundation; either version 3 of the License, or (at your
option) any later version.



---

[BACK TO TOP ▲](#header)

> [![ [FSF logo] ](/graphics/fsf-logo-notext-small.png)](//www.fsf.org)**“The Free Software Foundation (FSF) is a nonprofit with a worldwide
> mission to promote computer user freedom. We defend the rights of all
> software users.”**

[JOIN](//www.fsf.org/associate/support_freedom?referrer=4052)
[DONATE](//donate.fsf.org/)
[SHOP](//shop.fsf.org/)

Please send general FSF & GNU inquiries to
[<gnu@gnu.org>](mailto:gnu@gnu.org).
There are also [other ways to contact](/contact/)
the FSF. Broken links and other corrections or suggestions can be sent
to [<bug-stow@gnu.org>](mailto:bug-stow@gnu.org).

Please see the [Translations
README](/server/standards/README.translations.html) for information on coordinating and submitting translations
of this article.

Copyright ©
1993, 1994, 1995, 1996 Bob Glickstein;
2000, 2001 Guillaume Morin;
2007, 2008 Kahlil (Kal) Hodgson;
2009, 2010 Troy Will;
2011 Adam Spiers

Copyright © 2016 Free Software Foundation, Inc.

This page is licensed under a [Creative
Commons Attribution-NoDerivatives 4.0 International License](http://creativecommons.org/licenses/by-nd/4.0/).

[Copyright Infringement Notification](//www.fsf.org/about/dmca-notice)

Updated:
$Date: 2024/09/08 22:11:11 $
