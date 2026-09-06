---
id: 1334
url: https://bergie.iki.fi/blog/eupl/
title: I changed my license - Henri Bergius in Alofi, Niue
domain: bergie.iki.fi
source_date: '2026-09-06'
tags:
- security
- github-repo
summary: Henri Bergius has switched his software licensing strategy to the European
  Union Public License 1.2 (EUPL), moving away from his previous use of LGPLv2 and
  MIT licenses. EUPL is a strong copyleft license approved by the OSI that closes
  the "SaaS loophole" and requires reciprocal licensing, reflecting his shift away
  from permissive licenses that he believes have primarily benefited large corporations
  at the expense of developers and users. He has already applied EUPL to several projects
  including reticulum-js, dacar, and signalk-energy-predictor, appreciating the license's
  official translations into 23 languages for global use.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# I changed my license - Henri Bergius in Alofi, Niue

![cover image for I changed my license](https://d2vqpl3tx84ay5.cloudfront.net/500x/2026/EU-flags.jpg)

In the last 28 years of publishing software, I’ve had three distinct eras of software licensing. All of my recent stuff is available under the European Union Public License 1.2, and I thought to explain why.

[Midgard](http://midgard-project.org/) was all LGPLv2. This was a simpler time, and there weren’t that many free software licenses around. Since Midgard was a web framework, using a weak copyleft license felt like the right thing to do. The example website shipping with Midgard was X11 licensed.

When I started working more [seriously with JavaScript](https://bergie.iki.fi/blog/the_universal_runtime/) around 2011, I switched to the MIT license. This was a “do whatever you like, just don’t sue me” sort of a simple affair favored by the NPM package ecosystem. Easy interoperability, no hooks attached.

After we closed [Flowhub](https://bergie.iki.fi/blog/flowhub-ug/), there were a few years of hiatus where I published almost no software. Either because it wasn’t feasible due to my work situation, or because I was busy with the boat.

Enter EUPL
----------

This year I decided to switch my “default license” to [EUPL-1.2](https://interoperable-europe.ec.europa.eu/collection/eupl). This is an OSI-approved free software license created and published by the European Union. And it is quite a divergence from the licenses I’ve used in the past. EUPL is a strong copyleft license that closes the “SaaS loophole” by requiring reciprocal licensing regardless of how the software is distributed.

Over the years it has been clear that we in the “open source” camp (as opposed to the “free software” camp) were wrong all along. We won the debate, and gained little for users or developers. All that our efforts did was to make it easier for big corporations build things more cheaply and for billionaires to become trillionaires.

And so it is time to stop messing about with permissive licenses. If corporations don’t want to use our software under our terms, they are free to spend the effort or tokens to build their own.

The fact that EUPL has legally valid official [translations to 23 languages](https://interoperable-europe.ec.europa.eu/collection/eupl/eupl-text-eupl-12) also doesn’t hurt in a world where most of software is built and used in the wider world outside of the Valley.

Here are some things I’ve already published under EUPL:

* [reticulum-js](https://reticulum.js.org/): JavaScript implementation of the Reticulum mesh networking protocol
* [dacar](https://github.com/bergie/dacar): decentralized authorization system built on Reticulum
* [signalk-energy-predictor](https://github.com/meri-imperiumi/signalk-energy-predictor): prediction system for boats powered by renewable energy
* [offshore-blogging-system](https://www.npmjs.com/package/@meri-imperiumi/signalk-offshore-blogging): tool for publishing blog posts and downloading weather data over InReach satellite text messages

In addition the new rewrite of [NoFlo Development Environment](https://github.com/noflo/noflo-ui/tree/next) is being made under EUPL. [NoFlo](https://noflojs.org/) itself will remain MIT-licensed, as it is a pre-existing project with plenty of 3rd party contributions.

Continue reading
----------------

[![cover image for The Grid: Web Design by Artificial Intelligence](https://d2vqpl3tx84ay5.cloudfront.net/500x/bergius_thegrid_lift.jpg)](../../blog/lift-how-does-the-grid-work/)

[The Grid: Web Design by Artificial Intelligence](../../blog/lift-how-does-the-grid-work/)
==========================================================================================

17 February 2016
in Berlin, Germany.

1 minute read.

As mentioned last year, I’m working on a Artificial Intelligence that can do web design. It is called The Grid. Last week I gave a talk at Lift Conference explaining how it all works.

[![cover image for NoFlo Kickstarter, the hacker's perspective](https://d2vqpl3tx84ay5.cloudfront.net/500x/noflo-ui-code.jpg)](../../blog/noflo-kickstarter-launch/)

[NoFlo Kickstarter, the hacker's perspective](../../blog/noflo-kickstarter-launch/)
===================================================================================

01 August 2013
in San Francisco, California.

7 minute read.

This has been a big week for NoFlo, the flow-based programming environment for JavaScript. Yesterday we released NoFlo 0.4, which added support for running flow-based programs in web browsers. And today we launched our NoFlo Development Environment effort on Kickstarter. Before continuing, make sure to watch the video!

---

[Read more Flow-Based Programming posts](../../blog/category/fbp/).
