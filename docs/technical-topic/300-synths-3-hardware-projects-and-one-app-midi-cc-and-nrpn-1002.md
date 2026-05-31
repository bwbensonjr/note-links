---
id: 1002
url: https://midi.guide/blog/three-hunded-synths-one-app/
title: 300 synths, 3 hardware projects, and one app - MIDI CC and NRPN database
domain: midi.guide
source_date: '2026-04-07'
tags:
- github-repo
- database
- cli-tool
summary: MIDI Guide is an open-source database of MIDI control change (CC) and NRPN
  implementations that has grown from a passion project into a comprehensive resource
  with over 300 synthesizers documented by 52 contributors. The project originated
  from the creators' attempt to build a performance MIDI controller app called Condukt,
  but evolved into a valuable community-driven dataset that is now being used by multiple
  hardware and software projects. The success demonstrates how releasing a niche but
  well-designed open-source tool can foster an engaged community that solves a real
  problem for musicians and hardware developers.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# 300 synths, 3 hardware projects, and one app - MIDI CC and NRPN database

300 synths, 3 hardware projects, and one app
============================================

MIDI Guide, the open, "comprehensive" MIDI CC & NRPN dataset, has far outgrown its original purpose.

April 6, 2026

![Chart showing various types of rotary encoders](/static/images/blog/2026-04-06-three-hunded-synths-one-app/comparative-knob-morphology-dark.png)
*Download dark:
[PNG](/static/images/blog/2026-04-06-three-hunded-synths-one-app/comparative-knob-morphology-dark.49185c1c064a.png),
[SVG](/static/images/blog/2026-04-06-three-hunded-synths-one-app/comparative-knob-morphology-dark.32ca1fc34e9a.svg),
[PDF](/static/images/blog/2026-04-06-three-hunded-synths-one-app/comparative-knob-morphology-dark.52b3697a3be2.pdf);
light:
[PNG](/static/images/blog/2026-04-06-three-hunded-synths-one-app/comparative-knob-morphology-light.fcc33981363a.png),
[SVG](/static/images/blog/2026-04-06-three-hunded-synths-one-app/comparative-knob-morphology-light.0cec6ac1a8ad.svg),
[PDF](/static/images/blog/2026-04-06-three-hunded-synths-one-app/comparative-knob-morphology-light.7717afd9ca01.pdf).*

Recently, I merged in the work of a first-time contributor, putting MIDI Guide's dataset over 300 instruments. The pull request was a complete reference for the (somewhat idiosyncratic, in my opinion) MIDI CC implementation of a synth I'd never heard of, the [RozzBox One V2 by L.L. Electronics](/d/ll-electronics/rozzbox-one-v2/) - yet another cool synth introduced to me by MIDI Guide's community.

Three hundred instruments! And from 52 contributors, too, almost all of them perfect strangers. And there are at least 3 real-life hardware devices using the dataset (it's CC-BY-SA 4.0, so feel free to use it in your project, too).

Just before adding the three hundredth definition, we released the app that was the genesis of MIDI Guide: [Condukt](https://condukt.app), our performance MIDI controller and sequencer for iOS, iPad, and macOS. But how did an app released in 2026 produce a community project in 2019? Here's how a passion project that was backburnered for seven years spawned something useful, and then finally launched.

How it started
--------------

In early 2019, my cofounder and I awoke from a half-decade folie à deux in which we regrettably made Windows software. It was time to dust off our iPads and try to compete with the big dogs in the *real* App Store. And while considering what to build, we rediscovered the joy of purchasing, and even using, synthesizers.

It was a heady time to start a synth hoard: the #dawless tag promised productivity and happiness, even without a computer, and the OP-1 reissue was denounced as a toy for dilettantes at the hilariously-decadent price of US$1,299. Significantly, Eurorack was still contained in a lab, and had not yet been observed in metropolitan wastewater surveillance.

One of our first synth purchases for our 'market research' was the Elektron Analog Four MKII. It's probably still my favourite synth, because it's so much *more* than a synth: with its sequencer and four tracks, I can make a decent jam without any other device. But what especially fascinated us was its performance mode. When you're done composing, the A4 maps knobs to multiple, customizable parameters. One touch, many changes. Wouldn't it be nice, we thought, if an iPad app could do that, for multiple synths at once?

We envisioned Condukt as a single app that would act like the A4's performance knobs for your entire studio. And we built it! A beta of it, anyway. Here it is in action, running on iPadOS 12:

Creating the app was its own predictable challenge for a couple of rusty carpetbaggers, but it revealed that even using our app was a hurdle. The system requirements were steep:

* a modern iPad...
* and (likely) a Lightning-to-USB adapter...
* and a USB-to-MIDI adapter...
* and a way to power all these things...
* and a synth, of course...
* and a database of MIDI CCs (and NRPNs) so the app could talk to the synths.

Because of all the caveats, this thing was simply not a marketable app. It wasn't enough for customers to own an iPad (already a small market compared to iPhone) - they also needed dongles, cables... And what about the business side? We liked playing with the app, but had no way to get distribution for it. As for monetization, the App Store was just then getting serious about subscriptions, and music app customers were NOT having it.

So we resolved to set Condukt aside. We spent the summer working on [Penbook](https://penbook.app), instead - now an App Store Editor's Choice - but what to do with the MIDI CC implementations I had already documented?

Well, it's not like MIDI documentation goes bad; I've used 40-year-old scans to add some synths to this project. And to be honest, I was a bit vain about the format we designed for documenting MIDI CCs and NRPNs. I thought the format did a decent job of meeting two oft-opposing goals:

1. Be machine-parsable
2. Be normie-readable

CSV files were the ticket. Many of the 'real' musicians I knew IRL had Excel, but none of them knew what a YAML was (please spare me your ACKSHUALLY about readability). I think this has borne out, too, because a significant number of contributions come by email. The emails often include a cute, self-effacing apology for not being able to use git, as if that's their fault.

This was my chance to be opinionated on the Internet, and I even already knew how to make a website. MIDI Guide's first iteration was born.

How it went
-----------

### 2019-06: First post

I launched a simple web app on a subdomain of our app development company. I seeded the repo with 50 synthesizers from 17 manufacturers. It was a good start. Good enough anyway, since it covered all of my synths.

### 2020-01: First external pull request

I've never been a part of an open-source project before, much less in charge of one. This was a big moment for me! Heavy weighs the crown...

Early contributions were motivating. There wasn't much nitpicking about my design decisions, just device additions and corrections. The meta-discussion, when it did occur, was very productive: suggestions for a tighter specification, fields that could be added without breaking existing clients, and so on. A few contributors had forked the repo and were building their own client for it: MIDI librarians, controllers, sequencers, toys. It might be niche, but this dataset had real customers.

Lots of respectful passers-by asked questions that helped me define what the project is and isn't: Can you please document sysex? Can you please switch to JSON? Can you please implement this particular API design? These discussions clarified the project's scope, which strengthened it.

The best part was the feeling that the problem I had picked to solve was valuable and common to others. When you set out to solve something, it's hard to convince others that the problem even exists. These folks didn't need to hear it. They, too, thought looking up numbers in a manual was stupid.

### 2021-05: A real website

As the project's website was getting more traffic, we realized that not having a dedicated domain was a turn-off for potential contributors. Moving the project to `midi.guide` gave the dataset a bit of a brand, and made the project easier to talk about.

### 2021-06 to 2024-08: Slow and unsteady

Over these three years, I added or merged only 14 instrument definitions from 4 manufacturers. This made sense to me at the time: the project's site got a consistent trickle of organic traffic, just sitting there, serving its purpose, and costing a couple of bucks to host. Would adding more definitions at this stage have helped the project? Or was the demand for this kind of dataset simply absent?

### 2024-09: Almost 100 instruments added in a single month

A turning point in the project: the contributions of the indefatigable team behind the [Bacara generative MIDI plugin](https://bonboa.com/products/bacara-plugin) resulted in a huge increase in both the breadth and quality of device coverage. The extra eyes on the project helped me clean up some dusty corners, and paved the way for what came next.

### 2025-05: Neuzeit launches the [Drop MIDI controller](https://www.neuzeit-instruments.com/Drop)

This is the first (to our knowledge) physical device to include MIDI Guide's dataset. It's not just any device, either; this is a truly impressive piece of kit that takes live synth performances to such a level of polish that you might confuse the set with a DJ's. This is what I always hoped MIDI Guide would be used for.

I can say that as a software guy, having a hardware project use your stuff feels like getting drafted to the big leagues.

### 2025-10: Added the 200th instrument

At 200 instruments, it felt like a ratchet had clicked. The tempo of the repo had increased; we were hearing of more hardware and software projects using the dataset.

Our own app's beta was driving some requests for dataset additions, too. Responding to these requests is a piece of cake: with one bit of work, two projects get better.

### 2025-11: Design refresh

The project website's design was based on stock Bootstrap 4, which was already tired in 2019. The unsettling custom font I'd chosen for the dataset's typography wasn't doing it any favours, either. And while the rendering of the data looked fine for simple definitions, complicated or long definitions would stretch tables, add weird scroll areas, and in general just be a mess. You know what that means: REFACTOR TIME.

There was a lot of low-hanging fruit. I tried my hand at redesigning the device page (the page that renders the MIDI implementation for a particular instrument), guided by these principles:

1. **Collapse empty fields.** The project website doesn't need to show every single column that the CSV contains, especially empty columns. Why show NRPN columns for a device that doesn't support NRPN?
2. **Humans only.** Unlike the backing CSV, there is no requirement that the device page be machine-parsable. While the CSV needs to define a separate field for min and max values, that's not how humans talk about ranges; instead, we say, "It's from 0 to 127." The device page should reduce verbosity to match human speech. Robots, delvers, and pedants can always get the source material in one click if they need it.
3. **Don't let tables get ugly.** Be humble, and seek wisdom from the elders on the way of the <table>. Truncating information with a scrollable box is preferable to stubbornly blowing out cells with long strings.
4. **Own goal.** Not having a dark mode was sort of embarrassing.

I also began drawing little monochrome outlines for each instrument. Here I started with the Elektron gear, because their knobs are the easiest to draw.

As of this writing, about 2/3rds of the devices in the dataset have an icon. You might think, isn't that really tedious? You'd be right! But quantity is a quality of its own, and it paid off when I went to make the rotary specimen case at the top of this post.

### 2025-12: [Reliq](https://reliq-instruments.com) announces their use of MIDI Guide

The Reliq wood-trimmed synth/studio/DAW/fetish object/portable God includes a regularly-updated copy of the MIDI Guide dataset for controlling other hardware. This was validating, but the real juice came when Reliq's users began requesting synths and contributing definitions back to the dataset. Is this what success feels like?!

### 2026-03: Released Condukt

That wasn't so hard, was it? It only took seven years. This also happened to be the month of our 300th instrument.

How it's going
--------------

The dataset sits at 21,262 parameters, for 321 instruments, from 98 manufacturers, contributed by 56 community members (April 2026).

As for [Condukt](https://condukt.app), its launch was bigger than we ever hoped for. It hit #8 in the Music section of the App Store. Check it out:

I've gotten faster at adding synths, but no less interested. Of the instruments, 80% were new to me: guitar pedals with razor-sharp MIDI implementations, DIY synth kits from 2010, rack-mounted synths you've heard but could not name, a 200-page manual for a synth that sold 40 units

Approaching a niche synth by reading its manual is the opposite of twisting random knobs in the store; it's something like reading a cookbook. And a request for a synth's addition hints at the flavours. Very often, I get a request for a forgotten synth, and then a day later and without any apparent connection, another request for the same, and then it clicks that this 'forgotten' synth is the only source for an endangered sound.

Thanks for reading my victory lap! Talk to you again at the next round number.

– Ben
