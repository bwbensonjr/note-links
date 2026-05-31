---
id: 1088
url: https://lcamtuf.substack.com/p/a-nicer-voltmeter-clock
title: A nicer voltmeter clock - lcamtuf’s thing
domain: lcamtuf.substack.com
source_date: '2026-05-17'
tags:
- tutorial
- cli-tool
summary: The author documents the design and construction of an improved voltmeter
  clock that uses three analog panel meters to display hours, minutes, and seconds
  with continuous motion. The project showcases meticulous craftsmanship, from custom-printed
  meter decals and CNC-machined maple enclosure with kerf-bent curved walls to a simple
  microcontroller circuit that drives the meters using PWM-like digital signals. The
  result is an elegant timepiece that demonstrates how electronic design often requires
  as much attention to mechanical and woodworking details as it does to circuitry.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# A nicer voltmeter clock - lcamtuf’s thing

A nicer voltmeter clock
=======================

### Sometimes, electronic circuit design is mostly about wood

May 16, 2026

45

27

4

Share

Back in 2019, I built a simple voltmeter clock:

[![](https://substackcdn.com/image/fetch/$s_!Z11a!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F36abddfb-0eec-414b-a161-dec9f99c9652_1200x800.jpeg)](https://substackcdn.com/image/fetch/$s_!Z11a!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F36abddfb-0eec-414b-a161-dec9f99c9652_1200x800.jpeg)

*The clock, version 1. Cherry enclosure.*

As the name implies, these clocks use analog panel voltmeters instead of traditional clock faces to display time. I didn’t come up with the idea, so I never really blogged about the design; I just built one and kept it on my office desk.

Other people keep building these too, but most of the designs I see on the internet are just… sort of janky. So, I figured it might be good to build a better-looking one and document the process more properly.

The design started with a rough mockup in a 3D design program:

[![](https://substackcdn.com/image/fetch/$s_!tavR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F15b70ea2-2faf-42f9-b78e-baf54eeb7921_2481x1473.png)](https://substackcdn.com/image/fetch/$s_!tavR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F15b70ea2-2faf-42f9-b78e-baf54eeb7921_2481x1473.png)

*A mockup of the new design in Rhino3D.*

For this version of the meter clock, I used three generic, 90° panel voltmeters from Amazon ([link](https://www.amazon.com/dp/B092VBLGR2), about $9 a piece). I disassembled them, took careful measurements of the faces, and then printed replacement decals on adhesive paper. Printable PDF templates can be found [here](https://lcamtuf.coredump.cx/soft/embedded/meter_clock2.pdf).

[![](https://substackcdn.com/image/fetch/$s_!ownk!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F70462256-5017-4960-b097-244b8e982f6f_2000x1334.jpeg)](https://substackcdn.com/image/fetch/$s_!ownk!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F70462256-5017-4960-b097-244b8e982f6f_2000x1334.jpeg)

*Customizing 5 V panel meters.*

Note that the new hour gauge has 13 divisions, from 0 to 12, while the minute and second templates have 61 divisions, from 00 to 60. This is because I wanted to implement continuous motion for each hand; this meant that at 11:30, the hour dial couldn’t be just stuck at 11; it needed to be moving toward the twelfth division, even if it was never to reach it.

In addition to a host of other problems, the cheap “Baomain 65C5” meters I’m using have a rather hideous plastic flange. I decided to hide this flange from view and use a decorative recessed pattern to keep the front panel interesting. This detail made it more expedient to cut the front and back on a CNC mill instead of making the entirety of the enclosure by hand (as I did for version 1).

[![](https://substackcdn.com/image/fetch/$s_!mNd6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faaa1ecca-93e3-460b-8b62-3cfcc788a681_2282x1329.png)](https://substackcdn.com/image/fetch/$s_!mNd6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faaa1ecca-93e3-460b-8b62-3cfcc788a681_2282x1329.png)

*CNC toolpath view.*

The stock material for the enclosure is maple lumber — resawn, squared, and planed using conventional tools before letting the CNC machine take care of the finishing touches:

[![](https://substackcdn.com/image/fetch/$s_!Oonp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F110dd37d-c767-4e63-aeec-4ca2b73650db_2000x1334.jpeg)](https://substackcdn.com/image/fetch/$s_!Oonp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F110dd37d-c767-4e63-aeec-4ca2b73650db_2000x1334.jpeg)

*Machined front and back faces.*

Without a CNC mill, the path of least resistance would be to construct the panel as two-part glue-up, each part cut by following a printed (paper) template. A simple way to get the curves perfectly right would be to use a spindle sander.

The curved side wall posed a different challenge. For a seamless appearance, I needed to bend a flat piece of wood to conform to a template. To accommodate the tight radius without a steam bending rig, I opted to cut a series of notches on the inside:

[![](https://substackcdn.com/image/fetch/$s_!jzUh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F95f07cbd-39fa-4d3a-9073-6385ecc4f0ad_2000x1334.jpeg)](https://substackcdn.com/image/fetch/$s_!jzUh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F95f07cbd-39fa-4d3a-9073-6385ecc4f0ad_2000x1334.jpeg)

*Kerf-bending side walls using a template.*

The wood needed to be moistened, clamped, and then allowed to dry. After a couple of days, I glued the curved side wall to the front and back faces. Another template cut out of scrap plywood helped with precise fit without the need for gymnastics with clamps and ratchet straps:

[![](https://substackcdn.com/image/fetch/$s_!gYFN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc0d2eaff-6c6e-4e7d-b6f0-5fbd1f8a57dc_2000x1334.jpeg)](https://substackcdn.com/image/fetch/$s_!gYFN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc0d2eaff-6c6e-4e7d-b6f0-5fbd1f8a57dc_2000x1334.jpeg)

*Gluing up clock body using an external template (plywood).*

Anyway — here’s the assembled piece after sanding and a coat of nitrocellulose lacquer:

[![](https://substackcdn.com/image/fetch/$s_!1eR0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb5d890c5-76a0-4e16-b076-8671682e26e7_2000x1334.jpeg)](https://substackcdn.com/image/fetch/$s_!1eR0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb5d890c5-76a0-4e16-b076-8671682e26e7_2000x1334.jpeg)

*Initial fitting.*

Not bad, right?

The circuit is far less interesting than the enclosure. It took an hour or so to put it together: I grabbed the venerable [AVR128DB28](https://ww1.microchip.com/downloads/en/DeviceDoc/AVR128DB28-32-48-64-DataSheet-DS40002247A.pdf) MCU, powered it off a wall wart, and interfaced it to an 8 MHz crystal ([ECS-80-18-4X-CKM](https://www.ecsxtal.com/store/pdf/hc-49usx.pdf)). A 32.768 kHz crystal would also work fine. The panels are connected to three digital output pins (PC0, PC1, PC2). Finally, two input pins (PD6, PD7) are interfaced to two small pushbuttons mounted on the back and used to set time.

[![](https://substackcdn.com/image/fetch/$s_!_wDV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3b6448b3-c452-4d4a-bbbf-1b449ef96536_2150x1250.jpeg)](https://substackcdn.com/image/fetch/$s_!_wDV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3b6448b3-c452-4d4a-bbbf-1b449ef96536_2150x1250.jpeg)

*Circuit schematic.*

Note that the circuit doesn’t require digital-to-analog converters or any other additional components to drive the meters; I’m just using a relatively high-frequency, 1-bit digital pulse train. The inertia of the meter (and the inductance of the electromagnet coil) does the rest, settling in an intermediate position proportional to the software-controlled signal duty cycle.

The code can be viewed [here](https://lcamtuf.coredump.cx/soft/embedded/meter_clock2.c); it’s short and well-commented. The basic idea is to advance a 10 Hz counter using a timer interrupt synchronized with the crystal. With this out of the way, the main event loop computes the appropriate duty cycle and then manually toggles the output pins. Although the chip has a hardware PWM module, the application is simple enough that using the PWM circuitry wouldn’t really buy us anything.

Here’s the obligatory “rollover” video captured around 11:59:59:

Peace out.

---

**I**f you’re new here, you might enjoy some of my other articles:

[![Notched sticks to calculators: the history of counting machines](https://substackcdn.com/image/fetch/$s_!XvLP!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1ca07078-2ebe-4538-8792-3390559450a2_1600x1068.jpeg)

#### Notched sticks to calculators: the history of counting machines

[lcamtuf](https://substack.com/profile/92541588-lcamtuf)

·

August 26, 2023

[Read full story](https://lcamtuf.substack.com/p/a-brief-history-of-counting-stuff)](https://lcamtuf.substack.com/p/a-brief-history-of-counting-stuff)

[![See it with your lying ears](https://substackcdn.com/image/fetch/$s_!__I0!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd603e902-82e7-426e-9aaf-a6e88d13e995_1500x1000.jpeg)

#### See it with your lying ears

[lcamtuf](https://substack.com/profile/92541588-lcamtuf)

·

Jan 10

[Read full story](https://lcamtuf.substack.com/p/see-it-with-your-lying-ears)](https://lcamtuf.substack.com/p/see-it-with-your-lying-ears)

[![A breakthrough in C/C++ dependency management](https://substackcdn.com/image/fetch/$s_!ddgA!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feb2c3c8c-deb1-4d86-a445-35dc617ee0b6_1280x720.png)

#### A breakthrough in C/C++ dependency management

[lcamtuf](https://substack.com/profile/92541588-lcamtuf)

·

Apr 25

[Read full story](https://lcamtuf.substack.com/p/a-breakthrough-in-cc-dependency-management)](https://lcamtuf.substack.com/p/a-breakthrough-in-cc-dependency-management)

[![How has mathematics gotten so abstract?](https://substackcdn.com/image/fetch/$s_!pBMz!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb0cbc2ef-a44e-4110-b29a-db8ab4934ad2_1920x1080.avif)

#### How has mathematics gotten so abstract?

[lcamtuf](https://substack.com/profile/92541588-lcamtuf)

·

September 27, 2025

[Read full story](https://lcamtuf.substack.com/p/how-has-mathematics-gotten-so-abstract)](https://lcamtuf.substack.com/p/how-has-mathematics-gotten-so-abstract)

45

27

4

Share
