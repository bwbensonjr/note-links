---
id: 491
url: https://archives.loomcom.com/contraltojs/
title: Xerox Alto Emulator
domain: archives.loomcom.com
source_date: '2025-05-02'
tags:
- emulator
- web-dev
summary: ContrAltoJS is a web-based emulator that allows users to run the Xerox Alto,
  a pioneering 1970s computer, directly in their browser. The emulator provides access
  to various disk images containing games, programs, and operating systems, with support
  for features like Smalltalk 76 and networked multiplayer applications through a
  virtual shared network. While functional, the emulator has some limitations including
  laggy keyboard input, incomplete Ethernet emulation, and no ability to save changes
  to disk.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Xerox Alto Emulator

ContrAltoJS Xerox Alto Emulator Don't be alarmed. When using this page, your mouse and keyboard are being used by the emulator, so your normal keyboard shortcuts will probably not work. Clark-Games.dsk Josh.dsk allgames.dsk bcpl.dsk bravox.dsk diag.dsk experimental.dsk games.dsk gamesb.dsk gsl.dsk nonprog.dsk os12.5.empty.dsk os20.16.empty.dsk st76.dsk st76boot.dsk st76experiment.dsk st80.dsk tdisk4.dsk tdisk8.dsk xmsmall.dsk Boot Stop Reset Captive mouse Usage Select a disk to boot from the pull-down menu, then click Boot To see all files on the pack, type a single quetsion mark at the prompt. e.g., >? To see only runnable programs, type: >*.run? To run a program, just type its name and hit ENTER. e.g., >trek Checking "Captive Mouse" will cause the emulator to capture the mouse cursor when you click the screen and release it only when you press ESCAPE. This is useful for games that expect relative mouse motion. Running Smalltalk 76 To run Smalltalk 76, boot the xmsmall.dsk image, and type: >resume xmsmall.boot Running networked applications To run network-based applications, you must choose a host ID and click the "Join Network" button below for each running instance of the emulator. The virtual network will be shared among all running instances of ContraltoJS, regardless of location. You can demonstrate networking by running two instances of ContraltoJS and executing Battleship.RUN from the games.dsk image. Enter " ## host_id " as the name of opponent player, where host_id is the host ID of the emulator for the opposing player. Known Bugs Ethernet emulation is a work-in-progress and has not been fully validated. Keyboard input is laggy, keystrokes are easily missed. You cannot save changes to disk. Project Info This is a port of the Living Computer Museum's ContrAlto project to JavaScript. Find ContrAlto On GitHub . The JavaScript project is also On GitHub . For networking, this project makes use of the Retroweb Networking project, a JavaScript networking library for tunneling legacy networking protocols over WebRTC ; that project is build atop the Peerjs communications library.
