---
id: 1437
url: https://tildeweb.nl/~michiel/python-on-my-wrist.html
title: "Python on my wrist\n        | Blog"
domain: tildeweb.nl
source_date: '2026-10-30'
tags:
- python
- c
summary: The author describes reviving wasp-os, a MicroPython-based operating system
  for the cheap, open-source PineTime smartwatch, which had gone dormant. Their work
  includes fixing the build, speeding up firmware updates, reducing memory use, fixing
  crashes, and porting the OS to mainline MicroPython by getting three upstream changes
  merged. They also created two new watch faces, a Dutch-language clock and an 8-bit
  style clock, plus an optional "Guido" app that displays a blocky portrait of Guido
  van Rossum and Python-related logos.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-5-5
---

# Python on my wrist
        | Blog

Python on my wrist
------------------

I have a [PineTime](https://pine64.org/devices/pinetime/). It is a cheap, open,
hackable smartwatch from Pine64.

![The Dutch watch face on my PineTime](images/pinetime-dutchclock.jpg)

It’s not an Apple Watch
-----------------------

When people see it, they think: that looks like a smartwatch, so it must be a
smartwatch. Like an Apple Watch. It’s not! An Apple Watch costs around 700 USD,
and this one 25. Think of it as a programmable Casio with a color display,
Bluetooth, a step counter and a heart rate monitor.

It really does not have much CPU or memory: a 64 MHz ARM Cortex-M4, 64 KB of
RAM (yes, kilobytes), 512 KB of flash for the firmware and 4 MB of external
flash for files. After the Bluetooth stack and MicroPython itself have had
their share, about 12 KB of RAM is left for the apps. Everything on this watch
has to be small.

The screen is *fine*, though: 240×240 pixels on 1.3 inches, about 260 pixels
per inch. So if anything on it looks blocky in this post, that’s on purpose.
However, you can’t have an always-on display: the battery would run out too
soon. Apple Watches once had the same limitation, too!

The watch features an app for aforementioned watch monitor and step counter,
and you can send notifications to it via Bluetooth.

How I got here
--------------

I bought my PineTime in March 2023, for 26.99 USD. It ships with
[InfiniTime](https://infinitime.io). That’s fine. But InfiniTime is written in
C++, and I run a [Python group](https://pythonleiden.nl). So I preferred
[wasp-os](https://github.com/wasp-os/wasp-os), a MicroPython-based watch OS.
However, even in 2023 that project was already quite dormant. It was running a
2019 version of MicroPython and was quite hard to build. Recently its
maintainer added a note that wasp-os is
[looking for new maintainers](https://github.com/wasp-os/wasp-os/issues/536).

Reviving the OS
---------------

Then I found my watch in a drawer again, and thought it would be nice to work
on it a bit. So I took it upon myself to get wasp-os into shape again. Besides
moving to mainline MicroPython (more on that below), this is what changed:

* **It builds again.** The Python tooling is
  [managed with `uv`](https://github.com/mbeijen/wasp-os/commit/3789669ce7e66a986a701ae5fb80c5489f6ea5a2),
  so setting up is one command, and the
  [full build works again](https://github.com/mbeijen/wasp-os/commit/37c30e605cda4e62e2933d3bbd8a12980f1362c4),
  including the bootloader bits.
* **Faster flashing.** Updating the firmware over Bluetooth
  [now uses](https://github.com/mbeijen/wasp-os/commit/6da72b7c8441330b5b815d2a02a00ddeb9e81bb5)
  [bleak](https://github.com/hbldh/bleak) instead of the deprecated `gatttool`,
  and
  [takes about three and a half minutes](https://github.com/mbeijen/wasp-os/commit/55dcc8c125c8232126266f43fa29d28bfbb40b56)
  instead of over eight. When it fails, it
  [tells you why](https://github.com/mbeijen/wasp-os/commit/3e19e808ac5e435b71cc5867f9671c04bc187c2c),
  instead of hiding the errors, as it did before.
* **More memory.** The filesystem on the external flash
  [now uses the chip’s real 4 KB blocks](https://github.com/mbeijen/wasp-os/commit/bcb5c033a4b97d333513c984b648bfec31c48dd2),
  which got rid of a permanent 4 KB buffer. Free RAM at boot went from 7.1 KB
  to 12.4 KB. On this watch, that’s a lot!
* **It recovers by itself.** A watchdog
  [now resets the watch](https://github.com/mbeijen/wasp-os/commit/ec666c93fb0f75e2f5c2be5a1d6690dab03e2b32)
  when it hangs, instead of leaving it dead with Bluetooth still up.
* **No more buzzing.** A swipe could leave the vibration motor buzzing until
  you reset the watch. That’s
  [fixed](https://github.com/mbeijen/wasp-os/commit/17a5300b5a8ae1ae82cff62a662e34337ffc7b5b),
  and the
  [motor is driven right](https://github.com/mbeijen/wasp-os/commit/22c9e7c3d1c497a1618232233ea9aa898550e744)
  now.
* **Swipes work reliably.** The touch controller
  [now reports when you lift your finger](https://github.com/mbeijen/wasp-os/commit/0f597cdc7bf6a7c87ff55b85e77ceca0dc914c34),
  and in Settings you can
  [swipe along a slider](https://github.com/mbeijen/wasp-os/commit/96430ce354435e7f4f30462e9e30485e2bc284f7)
  to change it.
* **It survives a flat battery.** After my holiday, where I did not bring the
  watch, I put it on the charger, it booted and the watch said **INIT HARDWARE
  FAILED**. A chip had kept the I2C bus stuck. Now it
  [unsticks the bus at boot](https://github.com/mbeijen/wasp-os/commit/16dadba68771281318be3d16771f6ab37e0c8721),
  shows the actual error if something still fails, and the clock
  [starts at the build date](https://github.com/mbeijen/wasp-os/commit/e9fe31542c25f4c9d837bbade89811a78269f77b)
  instead of somewhere in 2020.

Mainline MicroPython
--------------------

wasp-os ran on a fork of MicroPython from 2019, with patches for the watch.
Porting it to mainline MicroPython also took a few changes in MicroPython
itself, so I submitted three pull requests upstream:
[frozen native code](https://github.com/micropython/micropython/pull/19729), a
fix for [PWM allocation](https://github.com/micropython/micropython/pull/19731)
and an
[ADC sample time option](https://github.com/micropython/micropython/pull/19733).
All three got merged, so for the first time wasp-os
[runs on mainline MicroPython](https://github.com/mbeijen/wasp-os/commit/a36f2863119b82f072c331be4e2d602a6e2e6cea),
and an up-to-date version too. No fork needed! The changes are targeted for
MicroPython 1.30, which is planned for December.

Two new watch faces
-------------------

Of course I wanted my own watch faces. The first one is simple: the existing
week clock, but in Dutch, because I’m Dutch. Dutch abbreviates weekdays with
two letters, so it says *ma 26 okt 2026*. Remember that the memory on this
watch is *tiny*, so there’s no room for a full multilingual OS. But you can
just translate a watch face, build it, and put your localized version on the
watch. You’ll see a picture of it on top of this post.

The second one is more fun: an 8-bit style clock. The digits come from a tiny
6×7 pixel font, and every font pixel is drawn as a block of 7×7 screen pixels
for the time and 3×3 for the rest. That gives the retro look, and it needs no
font data at all. Below the time and the ISO 8601 date (YYYY-MM-DD, obviously),
it shows the [Unix epoch](https://en.wikipedia.org/wiki/Unix_time), counting
every second.

![The pixel watch face on my PineTime](images/pinetime-pixelclock.jpg)

The Guido app
-------------

And then, as a finishing touch and to emphasize the Python angle, I created the
Guido app. It shows a blocky portrait of Guido van Rossum, the creator of
Python. Swipe, and you get the Python logo, then the MicroPython logo, and then
the logo of our own [Python Leiden](https://pythonleiden.nl) meetup. One more
swipe and you’re back at the clock.

![The four screens of the Guido app](images/wasp-guido-app.png)

The portrait is 80×80 pixels in 16 colors, drawn three times larger. That fills
the 240×240 screen and gives it a nice retro look. The logos are drawn sharp,
at full resolution.

Flash is tight on this watch. The firmware has about 330 KB to work with, and a
single full-screen picture as raw pixels takes 112 KB, a third of that. So I
made a small image format of up to 16 colors per picture plus run-length
encoding, with a
[decoder of about 40 lines](https://github.com/mbeijen/wasp-os/blob/af007ef849437301b64b8067334bdabe373bd664/apps/guido.py#L141-L181)
that draws them straight to the display. All four pictures together now take
under 12 KB. Still, that’s too much for something this silly to include by
default, so the app is optional: you have to add it to your build yourself.

The original photo is by
[Kushal Das](https://commons.wikimedia.org/wiki/File:Guido_van_Rossum_in_PyConUS24_(cropped).jpg),
taken at PyCon US 2024 and licensed
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), so the blocky
version is shared under the same license.

Coming up: the PineTime Pro
---------------------------

Pine64 is working on a successor: the
[PineTime Pro](https://pine64.org/2026/03/28/pinetime_march_2026/). It gets a
410×502 AMOLED screen, GPS, a dual-core Cortex-M33 and a digital crown. It’s
still early, there’s no release date yet, and the original PineTime keeps being
made. But that would be a much bigger playground for MicroPython. Guido in
AMOLED!

Try it
------

Everything is in the
[`pinetime-upstream-micropython`](https://github.com/mbeijen/wasp-os/tree/pinetime-upstream-micropython)
branch of my wasp-os fork.

*[Discussion on Hacker News](https://news.ycombinator.com/item?id=50255573)*
