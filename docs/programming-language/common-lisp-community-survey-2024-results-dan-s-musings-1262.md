---
id: 1262
url: https://blog.djhaskin.com/blog/common-lisp-community-survey-2024-results/
title: Common Lisp Community Survey 2024 Results — Dan's Musings
domain: blog.djhaskin.com
source_date: '2026-08-14'
tags:
- common-lisp
- news
summary: 'The 2024 Common Lisp Community Survey gathered responses from 293 community
  members and revealed that approximately 37% use Common Lisp professionally while
  97% use it for personal projects, with a significant portion having experience spanning
  more than 10 years. The survey identified Steel Bank Common Lisp as the dominant
  implementation (87.67%), while Reddit''s r/Common_Lisp community (31.89%) and IRC''s
  #commonlisp channel (19.96%) emerged as the primary platforms where developers engage
  with the community. The results highlighted that the Common Lisp community remains
  active and engaged, though the survey''s creator acknowledged methodological limitations
  and plans to improve future iterations through pre-survey community feedback.'
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Common Lisp Community Survey 2024 Results — Dan's Musings

Common Lisp Community Survey 2024 Results
=========================================

Published on August 9, 2024

Common Lisp Community Survey 2024 Results
=========================================

Introduction
------------

*My name is Dan Haskin and I conducted the Common Lisp Community Survey 2024. I
have taken longer than promised getting this out, but I recently lost my job and
have been dealing with the fallout. If you or anyone you know needs a [fantastic
DevOps engineer](https://about.djhaskin.com), [let me
know!](mailto:djhaskin987@gmail.com)*

Hello!

Roughly eight weeks ago, I asked people to fill out a
[survey](https://cl-survey-2024.djhaskin.com/) about their use of Common Lisp.
The response I got through the end of August was awe inspiring. People copied
this post to mailing lists, boosted my posts on the fediverse, and generally
responded very positively. I am deeply grateful for the community's response to
my humble attempt at gathering this information. Here are the results of that
survey.

I should note that this is my first time running such a survey. I made a lot of
mistakes, but I learned a lot! Next time I do this, I will do the following
differently:

* Before running the survey, solicit feedback for which questions to ask.

Yep, that's the biggest lesson. Some of the questions I asked were less useful
than others. You live and you learn.

Questions will be gone through one at a time, mostly with histogram results.
The data is as of the cut-off at around 8/5/2024, with 293 respondents as of
that date. Effort has been made to ensure anonymity within the results.

Histogram information generated using [VisiData](https://www.visidata.org/).
Several, if not most, histograms have been truncated (entries removed) to
preserve privacy. Some answers were only given by a few people and might be
traced back to their original answerers, and I'm trying to protect those who
gave me such valuable information. However, some answers that were truncated are
given "honorable mention" and represented here in my own words, because they
were super cool.

With that said, let's dive in!

Questions
---------

### Do you use Common Lisp?

```
Do yo~║ percent%│ histogram                             ~║
Yes   ║   97.95 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ║
No    ║    2.05 │                                        ║
```

I don't even know why I asked this question, other than completeness. Still,
most did answer in the affirmative :)

### Do you use it for work?

```
Do yo~║ percent%│ histogram                             ~║
No    ║   63.01 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ║
Yes   ║   36.99 │ ■■■■■■■■■■■■■■■■■■■■■■                 ║
```

A surprising result! At least within the population of respondents, fully 1/3 of
them use it for work.

### If so (that you use it for work), for how long?

```
If so, for how long?~║ percent%│ histogram                             ~║
                     ║   38.36 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ║
More than 10 years   ║   20.55 │ ■■■■■■■■■■■■■■■■■■■■                   ║
1-3 years            ║   13.01 │ ■■■■■■■■■■■■                           ║
Less than a year     ║   10.96 │ ■■■■■■■■■■                             ║
5-10 years           ║    9.93 │ ■■■■■■■■■                              ║
3-5 years            ║    7.19 │ ■■■■■■■                                ║
```

This one's math didn't add up perfectly with that of the previous question --
there are less than 63% "not applicable" respondents -- such is the life of a
surveyor.

A good chunk of people have used it more than 10 years, but 24% have started
using Common Lisp more recently, an interesting result.

### Do you use it for fun?

```
Do yo~║ percent%│ histogram                             ~║
Yes   ║   97.26 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ║
No    ║    2.74 │ ■                                      ║
```

There was a few respondents who actually (presumably, I did not check) use CL,
but don't use it for fun. Interesting!

However, the "hobby" side of Common Lisp comes out strong in the results of this
question.

### If so (that you use it for fun), for how long?

```
If so, for how long? ║ percent%│ histogram                             ~║
More than 10 years   ║   29.79 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ║
1-3 years            ║   23.63 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■         ║
5-10 years           ║   20.21 │ ■■■■■■■■■■■■■■■■■■■■■■■■■              ║
3-5 years            ║   13.70 │ ■■■■■■■■■■■■■■■■■                      ║
Less than a year     ║   10.27 │ ■■■■■■■■■■■■■                          ║
                     ║    2.40 │ ■■■                                    ║
```

There are a *lot* of developers within our community that have done Common Lisp
for A Long Time. I was quite surprised. Nevertheless, there's still a sizeable
chunk of people who are new. There was plenty of spread with this question.

### Which version of the spec do you find yourself the most using in the past month?

```
Which versi~║ percent%│ histogram                             ~║
HyperSpec   ║   79.45 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ║
NovaSpec    ║   11.30 │ ■■■■■                                  ║
            ║    8.22 │ ■■■                                    ║
```

The [HyperSpec](http://clhs.lisp.se/) takes the lion's share here, with the
[NovaSpec](http://novaspec.org/) carving out a respectable 11%. I personally
appreciate the HyperSpec because it *is* just HTML. I have a full copy on my
hard drive, for example.

Honorable mention from write-in answers:

* [the "Common Lisp Community
  Spec"](https://cl-community-spec.github.io/pages/index.html), a new one to me.
  Looks pretty nice!
* ["Common Lisp Docs"](https://lisp-docs.github.io/), a very cool docs page that
  I only just learned about from this survey.

### Where do you go to chat with other Common Lispers?

```
Value                      ║ percent%│ histogram                             ~║
Reddit.com/r/Common_Lisp   ║   31.89 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ║
IRC: #commonlisp           ║   19.96 │ ■■■■■■■■■■■■■■■■■■■■■■■                ║
I don't typically engage.. ║   17.79 │ ■■■■■■■■■■■■■■■■■■■■■                  ║
The Lisp Discord           ║   13.23 │ ■■■■■■■■■■■■■■■                        ║
Fediverse                  ║    5.42 │ ■■■■■■                                 ║
Matrix.org:Common Lisp     ║    3.04 │ ■■■                                    ║
Telegram                   ║    1.52 │ ■                                      ║
X.com                      ║    0.87 │ ■                                      ║
```

I was particularly interested in this one, and blown away with responses. This
is the first of the questions with a *substantial* number of write-ins. I
clearly didn't put down in the multiple choices all the places in which this
community communes.

Here are some honorable mentions from the write-ins:

* There is a telnet server at `lambda.moo.mud.org`, port 8888. When I joined
  there were 47 other people on that server!
* The European Common Lisp Symposium was mentioned.
* Usenet! `comp.lang.lisp` lives on.

To the surprise of *definitely me*, and probably no one else, [the Common Lisp
Subreddit](https://www.reddit.com/r/Common_Lisp/) took the top spot here.

Bonus round, I did a pivot table against how long people were in the community.

Here it is:

```
If so, for how long? ║ Discord: The Lisp #│ Reddit: The Common#│ I don't typically #│ IRC: #commonlisp o#│ Fediverse#│
More than 10 years   ║                 12 │                 35 │                 26 │                 31 │         6 │
5-10 years           ║                 19 │                 39 │                  8 │                 28 │         3 │
3-5 years            ║                 10 │                 24 │                  6 │                 16 │         5 │
1-3 years            ║                 15 │                 32 │                 30 │                 11 │         6 │
Less than a year     ║                  5 │                 13 │                 10 │                  4 │         4 │
```

Some rows/columns were truncated, as usual, for privacy (when there was just 1
data point in a row/column, I elided the results).

Experts agree! Across the board, be they experienced or new, people like Reddit
the best.

The [IRC channel](https://web.libera.chat/) `#commonlisp` enjoys comparable
popularity among the long-timers, with those newer to the craft more slow to
adopt it. However, this might be considered a feature -- if you want someone
with *experience* to answer your question, try IRC, the folks over there are
great!

Before I put this question to bed, it must be noted that the Fediverse placed
*purely on write-ins* and there's plenty of Lispers there as well, something I
didn't grasp when starting this survey.

Last little pitch from my side though: [The Lisp
Discord](https://discord.gg/HsxkkvQ) is *fantastic*. Give it a
try!

### What is your primary day-to-day Common Lisp implementation?

```
What is your primary day~║ percent%│ histogram                             ~║
Steel Bank Common Lisp   ║   87.67 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ║
LispWorks                ║    3.77 │ ■                                      ║
Clozure Common Lisp      ║    3.42 │ ■                                      ║
```

With its outstanding support for things like Unicode characters, bivalent
streams, good debugging tools, and support on all three major OS's (Windows,
Mac, and Linux), it is little wonder that SBCL has achieved such ubiquity. This
one was a huge eyebrow raiser for me. Talking with folks in the community, it
feels like most people like to "shop around" for different CL distros. However,
looking at this data, it appears that when people just want to Get Stuff Done,
they reach for [Steel Bank Common Lisp](https://www.sbcl.org/).

It's nice to see that [LispWorks](https://www.lispworks.com/) and
[ClozureCL](https://ccl.clozure.com/) has gotten a pretty good share as well,
though.

### Which implementations have you seriously used in the last 12 months OTHER than your daily driver?

```
Value                    ║ percent%│ histogram                             ~║
None                     ║   33.07 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ║
Steel Bank Common Lisp   ║   18.35 │ ■■■■■■■■■■■■■■■■■■■■■                  ║
Embeddable Common Lisp   ║   13.44 │ ■■■■■■■■■■■■■■■                        ║
Clozure Common Lisp      ║   12.92 │ ■■■■■■■■■■■■■■                         ║
Armed Bear Common Lisp   ║    4.91 │ ■■■■■                                  ║
LispWorks                ║    4.91 │ ■■■■■                                  ║
Allegro Common Lisp      ║    2.84 │ ■■■                                    ║
CLASP                    ║    1.81 │ ■■                                     ║
CLISP                    ║    1.29 │ ■                                      ║
                         ║    1.29 │ ■                                      ║
SICL                     ║    0.78 │                                        ║
```

This question may be a better question to help us gauge the relative popularity
of the different implementations than the first question, since people could
give more than one answer each and the spread of the answers are more even. Care
should be taken though, when judging the relative popularity of the different
implementations, since not every implementation is targeting the same audience.
Embedded work or C work? Use ECL. Java integration work? Use ABCL. Etc.

A good chunk of people just "use what they use" and don't dabble with anything
else, and SBCL also has a sizeable chunk here. After those, the numbers fall
give us rankings of the other implementations thus:

1. [ECL](https://ecl.common-lisp.dev/)
2. [ClozureCL](https://ccl.clozure.com/)
3. [Armed Bear Common Lisp](https://armedbear.common-lisp.dev/)
4. [LispWorks](https://www.lispworks.com/)
5. [Allegro Common Lisp](https://franz.com/products/allegro-common-lisp/)
6. [CLASP](https://github.com/clasp-developers/clasp)
7. [CLISP](https://clisp.sourceforge.io/)
8. [SICL](https://www.reddit.com/r/Common_Lisp/)

Here are some honorable mentions from the write-ins:

* "Genera" Symbolics Lisp
* [Fennel](https://fennel-lang.org/) (Hey Lua folks!)
* Interlisp

### Which editor do you use as your daily driver?

My *apologies* to the SLY folks on this question. Another "Oops" that happened
because "I'm new at this".

There were SO MANY SLY write-ins. I mean, so, so many. I don't want to get a
perfectly accurate number because that would be a bit of data clean-up, though
what data clean-up I did do suffices to establish their presence in the
rankings:

```
Editor: Which editor do yo ~║ percent%│ histogram                             ~║
Emacs + SLIME               ║   67.12 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ║
Emacs + SLY                 ║   13.70 │ ■■■■■■■                                ║
Lem                         ║    5.14 │ ■■                                     ║
Vim + SLIMV/VLIME/jpalardy  ║    3.42 │ ■                                      ║
VSCode + Alive              ║    1.03 │                                        ║
LispWorks IDE               ║    1.03 │                                        ║
Emacs + Sly                 ║    0.68 │                                        ║
Lispworks                   ║    0.68 │                                        ║
```

[`Emacs + SLIME`](https://slime.common-lisp.dev/) takes the gold here, with
[SLY](https://github.com/joaotavora/sly) and [Lem](https://lem-project.github.io/) users "on the podium" as well.

Again, there are more sly users than are represented above, 4 or five more,
bumping them up to 15-16% of the population of respondents.

Lem has gotten a lot of excitement of late, and has carved out some market share
as well. Neat.

LISP VIMMERS, UNITE! I was most pleased to see that, in total, there were 14
([Neo](https://neovim.io/))Vimmers among the respondents, putting it nearly on
par with the Lem folks (many Vimmers use an alternative workflow than those
libraries posted, and so were truncated from the above histogram). [I'm in
NeoVim
myself](https://blog.djhaskin.com/blog/developing-common-lisp-using-gnu-screen-rlwrap-and-vim/),
so that was fun to see.

Here are some honorable mentions from the write-ins:

* SEdit -- this is the Interlisp editor, apparently
* "Vanilla" emacs (without SLY or SLIME)
* [LispIDE](https://www.daansystems.com/lispide/)
* [Helix](https://helix-editor.com/)
* Vim + [Conjure](https://github.com/Olical/conjure)
* [Hemlock](https://www.cliki.net/hemlock)

I was particularly interested in the Conjure plugin,
linked above. Learned something new :)

### Dependency Management: Have you used one of these tools in the last 12 months? If so, which ones?

```
Value          ║ percent%│ histogram                             ~║
Quicklisp      ║   62.53 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ║
Ultralisp      ║   17.01 │ ■■■■■■■■■■                             ║
Qlot           ║    8.97 │ ■■■■■                                  ║
Not Applicable ║    2.76 │ ■                                      ║
OCICL          ║    2.53 │ ■                                      ║
Guix           ║    1.61 │                                        ║
CLPM           ║    1.61 │                                        ║
Nix            ║    0.92 │                                        ║
```

More surprises! No one was surprised at the top spot in this histogram -- that
of [Quicklisp's](https://www.quicklisp.org/beta/) and
[Ultralisp's](https://ultralisp.org/) -- but the others were very
surprising indeed:

* Not everyone needs dependency management, an eye opener.
* [Qlot](https://github.com/fukamachi/qlot) is pretty popular.
* My "track favorite", [OCICL](https://github.com/ocicl/ocicl), is doing okay
  for itself as a newcomer!

But here's the big surprise: [GUIX](https://guix.gnu.org/) and
[NIX](https://nixos.org/)! They are used as much (in this particular survey's
respondent group) as [CLPM](https://www.clpm.dev/)! Make of that what you will
-- GUIX appears to be a nice sheme-based dep tool, and I've heard Nix is also
based on functional programming. GUIX and NIX placed in the histogram purely
based on write-ins.

### Testing Framework: Which testing framework do you reach for when creating new projects?

```
Testing Framework║ percent%│ histogram                             ~║
Not Applicable   ║   46.23 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ║
Fiveam           ║   27.74 │ ■■■■■■■■■■■■■■■■■■■■■■                 ║
Parachute        ║   10.62 │ ■■■■■■■■                               ║
Rove/Prove       ║    6.85 │ ■■■■■                                  ║
Homegrown        ║    2.74 │ ■■                                     ║
Fiasco           ║    1.71 │ ■                                      ║
lisp-unit2       ║    1.71 │ ■                                      ║
```

The conclusion I draw from this one is that Common Lispers have testing
needs that are, in a word, simple. Many do not need it for their purposes at
all, or employ home-grown solutions and that suits them fine.

While [FiveAM](https://github.com/lispci/fiveam) still has the dominant mindshare,
[Shinmera's](https://shinmera.com/)
[Parachute](https://github.com/Shinmera/parachute) is a strong contender. It has
drop-in replacement functionality that makes it relatively easy to replace a
FiveAM test suite with it, and runs pretty fast. I've been pleased with it
myself so far. [Rove](https://github.com/fukamachi/rove) also enjoys a healthy
following.

I'll also note that [Fiasco](https://github.com/joaotavora/Fiasco) and
[lisp-unit2](https://github.com/AccelerationNet/lisp-unit2) placed on the charts
on write-ins alone, so it has a popular following as well.

Here are some honorable mentions from the other write-ins:

* [`hu.dwim.stefil`](https://github.com/hu-dwim/hu.dwim.stefil)
* Plain old [`ASSERT`](http://clhs.lisp.se/Body/m_assert.htm)

### Web Server: Which web server do you reach for when creating new projects?

### Web Framework: Which web framework do you reach for when creating new projects?

I must first apologize about these two questions for several reasons.

When I first wrote this survey, I didn't actually have any web dev experience
with Common Lisp, so I thought Web Server and Web Framework were two different
questions, like they'd be under a language like, say, Python.

The other reason is that I botched the question when I first started anyways. I
think I copied the first question's contents into the second question on
accident for the first few days, or something.

In order to clean up the results, I looked for all or any mention of the web
servers and counted those occurrences for the web server table, and reserved any
mention of frameworks for the frameworks table.

Here is the web server table:

```
Value               ║ percent%│ histogram                             ~║
N/A HTTP server     ║   51.55 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ║
Hutchentoot         ║   36.08 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■             ║
Clack/Woo           ║    7.22 │ ■■■■■                                  ║
Clack               ║    2.41 │ ■                                      ║
```

Of those who are interested in web programming, most use
[Hutchentoot](http://edicl.github.io/hutchentoot/), with the minority using
[Clack](https://github.com/fukamachi/clack) and/or
[Woo](https://github.com/fukamachi/woo). Nothing too out-of-the-ordinary here.

Next, we look at frameworks.

```
Value                      ║ percent%│ histogram                             ~║
N/A HTTP framework         ║   67.66 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ║
Caveman/Caveman2           ║    6.60 │ ■■■                                    ║
Homegrown HTTP framework   ║    3.96 │ ■■                                     ║
Ningle                     ║    2.97 │ ■                                      ║
CLOG                       ║    2.97 │ ■                                      ║
Radiance                   ║    2.64 │ ■                                      ║
Easy-routes                ║    2.31 │ ■                                      ║
No HTTP framework          ║    1.98 │ ■                                      ║
```

The Common Lisp community seems to have not made a consensus yet on web
frameworks. Firstly, many are "N/A" meaning they haven't had a need for this; in
the second place, the tail was very long on this question. Answers are truly all
over the map. As noted above, columns with very few responses get truncated.
There were a lot of these in this question. I knew of
[Caveman](https://github.com/fukamachi/caveman) and
[Radiance](https://shirakumo.github.io/radiance-homepage/), which is why they
were featured, and while Caveman seems more used than others, none seem to have
captured a dominant marketshare.

[Ningle](https://github.com/fukamachi/ningle), a micro-framework, and
[CLOG](https://github.com/rabbibotton/clog), a -- UI? -- framework, were popular
write-ins of note, as well as Easy-routes and Radiance, but it is interesting
that many more folks just wrote in "Hutchentoot" for either question.

All in all, it seems that using Hutchentoot plain, with no frameworks or frills,
seems to be the most popular option in the web space.

### JSON library: Which JSON library do you reach for when creating new projects?

```
Value            ║↓count♯│ percent%│ histogram                             ~║
Not Applicable (I║   113 │   38.44 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ║
cl-json          ║    67 │   22.79 │ ■■■■■■■■■■■■■■■■■■■■■■                 ║
com.inuoe.jzon   ║    56 │   19.05 │ ■■■■■■■■■■■■■■■■■■                     ║
YASON            ║    20 │    6.80 │ ■■■■■■                                 ║
Shast            ║    12 │    4.08 │ ■■■■                                   ║
Jonathan         ║     7 │    2.38 │ ■■                                     ║
st-json          ║     6 │    2.04 │ ■■                                     ║
Homegrown        ║     4 │    1.36 │ ■                                      ║
jsown            ║     4 │    1.36 │ ■                                      ║
```

About a third of Common Lispers haven't had the need for a JSON parser in the
last 12 months. That's actually pretty low. Most of these "favorite library"
questions have that number over half. This makes sense. Serialization in a
common format is a big deal.

Of those still interested,
[cl-json](https://cl-json.common-lisp.dev/cl-json.html) takes the top spot, a
library that I have
heard of but I couldn't tell how popular it was. Now we know ;) The next
entry is [`com.inuoe.jzon`](https://github.com/Zulu-Inuoe/jzon), a strong
contender and my personal favorite. [YASON](https://phmarek.github.io/yason/)
and [Shasht](https://github.com/yitzchak/shasht) also place.

Strong write-ins include [Jonathan](https://github.com/rudolph-miller/jonathan),
[st-json](https://marijnhaverbeke.nl/st-json/) and
[jsown](https://github.com/madnificent/jsown), libraries I had never heard of.

### XML parser: Which XML parser library do you reach for when creating new projects (if applicable)?

```
XML parser: Whic~║ percent%│ histogram                             ~║
Not Applicable   ║   69.52 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ║
Plump            ║   14.04 │ ■■■■■■■                                ║
CXML             ║    6.16 │ ■■■                                    ║
xmls             ║    4.45 │ ■■                                     ║
s-xml            ║    3.77 │ ■■                                     ║
```

More in line with other library questions, 2/3 of the lispers don't need no XML,
but those that do tend to prefer [Plump](https://github.com/Shinmera/plump),
followed by [CXML](https://common-lisp.net/project/cxml/). Also placing are
[xmls](https://github.com/rpgoldman/xmls) and
[s-xml](https://s-xml.common-lisp.dev/).

Pretty
straight-forward, really, but still good to know.

### CLI library: What CLI library do you reach for when creating new projects?

```
CLI library: Wha~║ percent%│ histogram                             ~║
Not Applicable   ║   73.63 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ║
clingon          ║    8.90 │ ■■■■                                   ║
unix-opts        ║    6.51 │ ■■■                                    ║
Homegrown        ║    2.40 │ ■                                      ║
adopt            ║    1.71 │                                        ║
clon             ║    1.71 │                                        ║
```

I asked this question because I was particularly interested in CLI tools, but it
doesn't seem that the community agrees. A higher than usual number put "Not
Applicable", a sign that maybe this wasn't as interesting a question to the
community as I initially thought. Yet another reason to do a "call for
questions" before I do this next year :)

Those who did respond gave [Clingon](https://github.com/dnaeon/clingon) as their
preference the most, followed by [unix-opts](https://github.com/libre-man/unix-opts). The Homegrown crowd was
particularly strong in this category, and may even be unrepresented in this
histogram, since many libraries were given but I suspect those libraries are
chiefly used by their authors. I'm certainly in
the homegrown group, currently. Additional placers are
[adopt](https://github.com/sjl/adopt/) and
[clon](https://github.com/didierverna/clon), the last of which placed via
write-ins.

Honorable mentions from the write-ins include [plain
UIOP](https://asdf.common-lisp.dev/uiop.html) and a surprise entry that got more
than one response:
[`com.google.flag`](https://quickref.common-lisp.net/com.google.flag.html). Huh.

### What other library categories would you like to see in future surveys, if any?

This question was entirely *free form*, so to make sense of the results, I
decided on the "word cloud" approach: I split all the entries into individual
words, lower-cased them all, did a frequency histogram on *that*, and removed
meaningless entries like `the`, `or`, `question`, etc.

Here are the results:

```
Value.lower()   ║↓count♯│ percent%│ histogram                             ~║
gui             ║    36 │    4.97 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ║
graphics        ║    12 │    1.66 │ ■■■■■■■■■■■■                           ║
database        ║     8 │    1.10 │ ■■■■■■■■                               ║
web             ║     7 │    0.97 │ ■■■■■■■                                ║
frameworks      ║     7 │    0.97 │ ■■■■■■■                                ║
learning        ║     7 │    0.97 │ ■■■■■■■                                ║
game            ║     6 │    0.83 │ ■■■■■■                                 ║
databases       ║     6 │    0.83 │ ■■■■■■                                 ║
clog            ║     5 │    0.69 │ ■■■■■                                  ║
math            ║     5 │    0.69 │ ■■■■■                                  ║
http            ║     5 │    0.69 │ ■■■■■                                  ║
programming     ║     5 │    0.69 │ ■■■■■                                  ║
lisp            ║     5 │    0.69 │ ■■■■■                                  ║
alexandria      ║     4 │    0.55 │ ■■■■                                   ║
orm             ║     4 │    0.55 │ ■■■■                                   ║
language        ║     4 │    0.55 │ ■■■■                                   ║
coalton         ║     4 │    0.55 │ ■■■■                                   ║
loop            ║     4 │    0.55 │ ■■■■                                   ║
logging         ║     4 │    0.55 │ ■■■■                                   ║
iterate         ║     3 │    0.41 │ ■■■                                    ║
concurrency     ║     3 │    0.41 │ ■■■                                    ║
ui              ║     3 │    0.41 │ ■■■                                    ║
documentation   ║     3 │    0.41 │ ■■■                                    ║
scientific      ║     3 │    0.41 │ ■■■                                    ║
tui             ║     3 │    0.41 │ ■■■                                    ║
```

From this, I draw the following conclusions:

User interfaces, particular GUIs, are a BIG DEAL to Common Lispers. This is
*definitely* going to be covered next year in its own question. Lots and lots
of Lispers want to know what the community uses for (Graphical) User
Interfaces. This is followed closely by the adjacent concern of graphics.

Databases are probably the runner-up here. We see terms like `database`, `db`
and `orm` crop up relatively frequently.

Other questions that may be of interest to the community, based on this data,
are:

1. `loop`/`iterate`, or: How does the community like to do loops?
2. `game`/`gamedev`
3. `math`/`statistics`
4. `concurrency` ([lparallel](https://github.com/lmj/lparallel), [cl-async](https://orthecreedence.github.io/cl-async/), etc.)

An honorable mentions here might be
[`coalton`](https://github.com/coalton-lang/coalton) and the use of data
structures in Common Lisp. All things that will be considered in next year's
"Call for Questions" :)

### What libraries or tooling would you like to see written for Common Lisp next?

This is going to be the most subjective results section. The word cloud trick
used for the above question kinda works, but not nearly as well. I will give my
own listing based on what I've read.

My own subjective list, in no particular order:

* GUI. CLIM/McClim features, Qt6 bindings (a popular request!), CLOG features,
  etc. The community is *hungry* for GUI stuff. Also graphics: OpenGL, WebGL,
  etc.
* Quicklisp is on peoples' minds. Worry over single maintainers, version
  support.
* Better tooling, particularly in the IDE space. Performance profiling, flame
  graphs, debugging, beginner-friendly, CI/CD, library sanity checking, that
  sort of thing.
* ML featured prominently, with comparisons to the Python programming language.
  More than a few answers were along these lines.
* gRPC, lots of people want a better gRPC story.
* Cryptography libraries
* More C library bindings in general, like for Wayland, audio I/O, and Windows.
* Web: OpenAPI, better web frameworks and components
* Several folks asked for better a AWS SDK story in Common Lisp.

Yeah, I'm happy with that list. I have missed some things, but that's pretty
good for now.

### Is there anything else you wish to let the surveyor know?

There were a lot of "thank you"s here, which I appreciate :), and a lot of
question suggestions which have generally been covered in the above answers. The
best answers here, though, may be those who just took the space to say how much
they love Common Lisp. It's a great language, despite all its quirks.
