---
id: 1204
url: https://wiki.xxiivv.com/site/uxn.html
title: XXIIVV — uxn
domain: wiki.xxiivv.com
source_date: '2026-07-05'
tags:
- emulator
- github-repo
- compilers
summary: Uxn is a lightweight virtual machine at the core of the Hundred Rabbits ecosystem,
  designed as a portability layer for creating small interactive graphical software
  and capable of hosting personal computing applications. Programmable in the Uxntal
  language, it can be assembled into ROM files and run across multiple emulator platforms
  including x11, SDL2, Windows, and HTML5. The system provides a comfortable computing
  environment with reference implementations, comprehensive instruction sets, and
  an active community through mailing lists and IRC channels.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# XXIIVV — uxn

![Uxn Sticker](../media/diary/739.jpg)

Uxn Sticker15C06

Uxn is the virtual machine living at the heart of the Hundred Rabbits ecosystem.
--------------------------------------------------------------------------------

![](../media/identity/uxn_eyes.png)

The **virtual machine**, programmable in [Uxntal](uxntal.html),
is a [portability layer](devlog.html) and an attempt at crafting a comfortable amber for personal computing that is capable of hosting a variety of small interactive graphical software. It is powering this [wiki](about.html).

* **Uxn Instructions**: [Reference](uxntal.html)
* **Varvara Devices**: [Reference](varvara.html)
* **Emulators**: [x11](../etc/uxn11.c.txt), [sdl2](../etc/uxn2.c.txt), [win32](https://github.com/randrew/uxn32), [html5](https://git.sr.ht/~rabbits/uxn5), [etc..](https://git.sr.ht/~rabbits/uxn)

### Quick Setup

To get started, equip yourself with an assembler to convert tal source files
into rom binary files, and an emulator to evaluate the rom files. The
system below includes the [Console
device](varvara.html#console):

```
# Build an emulator
cc uxnmin.c -o uxnmin

# Build an assembler
cat drifloon.rom.txt | uxnmin xh.txt > drifloon.rom

# Assemble a tal file
cat opctest.tal | uxnmin drifloon.rom > opctest.rom

# Run a rom file
uxnmin opctest.rom
```

### Summary

See the [complete definition](../etc/uxn.napkin.txt).

```
P?O:M[P] P:P+1

	          00  P:0
	      a'  20  a?P:P+M[P]" P:P+2
	          40  P:P+M[P]" P:P+2
	          60  P:P+M[P]" P:P+2 .P" 
	          80  M[P]' P:P+1
	          a0  M[P]" P:P+2
	          c0  .M[P]' P:P+1
	          e0  .M[P]" P:P+2

	  x P+:y  00|O  x' P:P+y'
	  x P+:y  20|O  x" P:y"
	    x .y  00|O  x .y
	    x .y  40|O  .x y
	x y -- z  00|O  x y -- z
	x y -- z  80|O  x y -- x y z

	       a  01  a+1
	       a  02
	     a b  03  b
	     a b  04  b a
	   a b c  05  b c a
	       a  06  a a
	     a b  07  a b a
	     a b  08  a=b'
	     a b  09  a≠b'
	     a b  0a  a>b'
	     a b  0b  a<b'
	       a  0c  P+:a
	    a' b  0d  a?P+:b
	       a  0e  P+:a .P"
	       a  0f  .a
	      a'  10  M[a]
	    a b'  11  M[b]:a
	      a'  12  M[P+a]
	    a b'  13  M[P+b]:a
	      a"  14  M[a]
	    a b"  15  M[b]:a
	      a'  16  D[a]
	    a b'  17  D[b]:a
	     a b  18  a+b
	     a b  19  a-b
	     a b  1a  a×b
	     a b  1b  a÷b|0
	     a b  1c  a&b
	     a b  1d  a|b
	     a b  1e  a^b
	   a hl'  1f  a>>l<<h
```

![](../media/generic/varvara.chill.png)

* **Communities**:
  [Mailing List](https://lists.sr.ht/~rabbits/uxn) •
  [Forum](https://llllllll.co/t/uxn-virtual-computer/46103)
* **Chat**:
  #uxn on irc.libera.chat • [Catlang Discord](https://discord.gg/QKapkAxsg9)
* Original illustrations by [Rekka Bellum](https://kokorobot.ca/).

![Rostiger's Uxn Zine](../media/diary/804.jpg)![The Sound Of Plumpkins](../media/diary/776.jpg)

* `17P04` — Uxn is frozen at 0K.
* `15B13` — Uxn is born!

**incoming:** [forth](forth.html) [macintosh](macintosh.html) [ufx format](ufx_format.html) [ulz format](ulz_format.html) [uxntal](uxntal.html) [uxntal software](uxntal_software.html) [varvara](varvara.html) [playdate](playdate.html) [about](about.html) [oscean](oscean.html) [devine lu linvega](devine_lu_linvega.html) [events](events.html) [now lie in it](now_lie_in_it.html) [2024](2024.html) [2023](2023.html) [2022](2022.html) [2021](2021.html) [hundred rabbits](hundred_rabbits.html)
