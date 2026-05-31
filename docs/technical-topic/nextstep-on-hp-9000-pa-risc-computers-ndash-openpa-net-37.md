---
id: 37
url: https://www.openpa.net/nextstep_pa-risc.html
title: NeXTSTEP on HP 9000 PA-RISC Computers &ndash; OpenPA.net
domain: www.openpa.net
source_date: '2026-01-05'
tags:
- devops
- c
- compilers
summary: NeXTSTEP 3.3 (1994) was NeXT's Unix-based operating system featuring a Mach
  microkernel and advanced GUI that was ported to support several 32-bit HP 9000 PA-RISC
  workstations, marking NeXT's effort to expand beyond proprietary hardware after
  initial success on Motorola 68000 and Intel x86 platforms. The PA-RISC port supported
  specific models including the 712, 715, 725, 735, and 755 workstations with good
  onboard hardware compatibility, though limited third-party software availability
  restricted the port to version 3.3 only. While NeXTSTEP itself had limited commercial
  success, its innovative technologies and design philosophy influenced later systems
  like macOS.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# NeXTSTEP on HP 9000 PA-RISC Computers &ndash; OpenPA.net

[![PA-RISC computer](images/a_735.jpg)](./)

* [OpenPA](./ "OpenPA - PA-RISC and HP 9000 information")* [Hardware](pa-risc_design.html "PA-RISC computers hardware")* [Computers](systems/ "PA-RISC and HP 9000 computers")* [Operating](pa-risc_operating-systems.html "Operating systems for PA-RISC computers")* [Software](hp-ux_software.html "Software for HP-UX and PA-RISC")

* [Operating Systems](pa-risc_operating-systems.html)* [HP-UX Unix](hp-ux_unix.html)
    * [NeXTSTEP on RISC](nextstep_pa-risc.html)* [OSF/1 Unix](osf_1_mkpa_pa-risc.html)* [Linux on PA-RISC](linux_pa-risc.html)* [NetBSD/hppa](netbsd_hp-700.html)* [OpenBSD/hppa](openbsd_hppa.html)* [HPBSD](hp_bsd_utah_pa-risc.html)* [Mach 3/4 on PA-RISC](mach_3_mach_4-lites_utah_pa-risc.html)* [MkLinux on PA-RISC](mklinux_mach-linux_pa-risc.html)* [Chorus on PA-RISC](chorus_pa-risc.html)* [Windows and NetWare](windows_netware_pa-risc.html)* [HP-RT real-time](hp-rt_realtime-vme.html)
                        * [QEMU emulation](qemu_pa-risc_emulation.html)

NeXTSTEP on PA-RISC
===================

* [Supported systems](#systems)* [Hardware support](#supported_hardware)* [Software](#software)* [Documentation](#documentation)

![NexTSTEP 3.3](images/next_ug-1994.jpg)


© NeXT 1994

NeXTSTEP is a Unix operating system developed in the 1980s and 90s by NeXT, based on a Mach microkernel with an advanced graphical user interface.
NeXTSTEP supports several 32-bit HP 9000 PA-RISC workstations in release 3.3 from 1994, for which HP and NeXT had high hopes.
This was an effort to open up the NeXT operating system to other hardware platforms after NeXT stopped designing its own custom NeXT computers.

[![NeXTSTEP on PA-RISC](images/nextstep_hp715.jpg)](images/nextstep_hp715.jpg)


NeXTSTEP, [Thomas Schanz](https://commons.wikimedia.org/wiki/File:HP-HP9000-715-Screenshot-Running-NeXTSTEP_02.jpg) [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)

Introduced in 1989 by NeXT, NeXTSTEP featured development and user environments, an unique GUI and the Display Post Script (DPS) display system.
The operating system core is a Mach microkernel, 4.3BSD compatible and runtime-extensible.

In its early years, NeXTSTEP only ran on NeXT "black hardware", sophisticated and expensive NeXT cubes, based on Motorola 68000.
Intel x86 PCs, "white hardware," were first supported in NeXTSTEP 3.1 in 1991 to open up the platform to off-the-shelf hardware.

NeXTSTEP version 3.3 included support for a handful of contemporary HP 9000 700 workstations (712, 715, 725, 735, 755) with good onboard hardware support but admittedly limited software choices.
Third party applications and porting enthusiasm for PA-RISC fell short and the PA-RISC port was limited to NeXTSTEP 3.3 and to thos select set of 32-bit HP 9000 workstations

[![HP running NeXTSTEP](images/hpnext_94.jpg)](images/hpnext_94.jpg)


HP and NeXT advertisement, HP 1994

The PA-RISC version of NeXTSTEP 3.3 [was developed](pa-risc_operating-systems.html#next) on and specifically for the [HP 9000 712 pizzabox](systems/hp-9000_712.html) workstation, a very advanced combination for the 1990s with a nice, integrated user experience.

NeXT tried to get its own NeXT RISC workstation to market ("chased a chimera") and looked at Motorola 88000 and PowerPC, but decided to partner with workstation vendors to bring NeXT to RISC.
Development continued and in 1994 NeXTSTEP 3.3 was released with support for different RISC platforms including Sun SPARC and HP PA-RISC.

NeXTSTEP itself, while revolutionary in aspects, did not have long commercial success.
However some of its ideas and technologies live on in Mac OS, after corporate M&A and consolidation in the tech sector.

[up](#top)

Supported systems
-----------------

NeXTSTEP 3.3 supports some 32-bit HP 9000 700 PA-RISC workstations from the 1990s:

| Class | Supported computers |
| --- | --- |
| HP 9000 700 | [712](systems/hp-9000_712.html), [715](systems/hp-9000_715.html), [725](systems/hp-9000_725.html), [735, 755](systems/hp-9000_735_755.html) |
| Portables | probably [SAIC Galaxy 1100](systems/saic_galaxy_1100.html) |

[![HP 715/64 running NeXTSTEP](systems/images/715next.jpg)](systems/images/715next.jpg)


715 NeXTSTEP, [Thomas Schanz](https://commons.wikimedia.org/wiki/File:HP-HP9000-735-99-Workstation_11.jpg) [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)

Most HP 9000 onboard components and integrated devices in compatible HP workstations are supported.

NeXTSTEP ran rather well on [HP 9000 712 workstations](systems/hp-9000_712.html), on which the 3.3 RISC port was developed.
NeXT provided an unique operating system experience in the early 1990s with an integrated *Unix* (Mach) system and advanced GUI.
NeXTSTEP on the 712 was "where NEXTSTEP belonged all along" when HP had been "trying for years to put a human face on UNIX" on its HP 9000 PA-RISC computers.

The serious [HP 9000 735/125](systems/hp-9000_735_755.html) workstation was the fastest RISC workstation that ran NeXTSTEP in the 1990s, an interesting contrast between the industrial HP 735 workstation and refined NeXTSTEP operating system with a friendly GUI.

[up](#top)

Hardware support
----------------

NeXTSTEP 3.3 supports most standard hardware of supported PA-RISC workstations:

* 32-bit PA-RISC [PA-7100](pa-risc_processor_pa-7100.html) or [PA-7100LC](pa-risc_processor_pa-7100lc.html) processors* HP [ASP](pa-risc_chipsets_asp.html) and [LASI](pa-risc_chipsets_lasi.html) chipsets
  * Storage between 400 MB for a user environment to 700 MB for complete developer* 32-64 MB RAM with a maximum of 256 MB supported* All onboard graphics and [CRX and CRX-24](pa-risc_graphics_crx_hcrx.html#crx) supported* Onboard communication devices were supported
        * [HCRX and HCRX-24](pa-risc_graphics_crx_hcrx.html#hcrx) graphics supported after installation of NeXTSTEP 3.3 patches* Onboard [SCSI controllers](scsi.html) for storage
          * PS/2 keyboards only on 712 and 715/64, 80 and 100 workstations, no HIL* HIL keyboards on all other systems* **Unsupported** on 735/755 are FWD (Fast/Wide Differential) SCSI and FDDI

[up](#top)

Software
--------

There used be to quite a few commercial productivity and publishing applications available for NeXTSTEP, some of which were ported to PA-RISC and NeXTSTEP 3.3.
This included:

* [SoftPC 4.0](hp-ux_emulation.html#softwindows), the PC emulator, was apparently included with or was available for NeXTSTEP, but it is unclear if this applies to the PA-RISC release.
* [FrameMaker 3.2](hp-ux_dtp.html#framemaker), the professional DTP program, was ported in 1994 (again) to NeXTSTEP and included PA-RISC versions.

There used to be a large software archive available at the Peanuts.org FTP server.
It went offline about 2004-2005, without a known mirror.

* [NeXTSTEP Current Patch List](http://www.nextcomputers.org/NeXTfiles/Software/NEXTSTEP/Patches/nextstep_current_patch_list.pdf) (.pdf) Apple Computer 2006, mirror accessed 2009 **nextcomputers.org*** NeXTSTEP 3.3 "User" patch [NS33RISCUserPatch3.tar](http://www.nextcomputers.org/NeXTfiles/Software/NEXTSTEP/Patches/NEXTSTEP_3.3_User_Patch_3/NS33RISCUserPatch3.tar) and release notes
    [NeXTSTEP 3.3 Patch 3 Overview](http://www.nextcomputers.org/NeXTfiles/Software/NEXTSTEP/Patches/NEXTSTEP_3.3_User_Patch_3/nextstep3.3_patch_3_overview.pdf) (.pdf) Apple Computer 2006, mirror January 2009 **nextcomputers.org*** NeXTSTEP 3.3 "Developer" patch [NS33DeveloperPatch2.tar](http://www.nextcomputers.org/NeXTfiles/Software/NEXTSTEP/Patches/NEXTSTEP_3.3_Developer_Patch_2/NS33DeveloperPatch2.tar) **nextcomputers.org**

[up](#top)

Documentation
-------------

### Manuals

* [NeXTstep 3.3 Network and System Administration Manual](http://www.nextcomputers.org/NeXTfiles/Docs/NeXTStep/3.3/nsa/), NeXT Software Inc. 1994, mirror accessed December 2019 **nextcomputers.org*** [NeXTstep 3.3 Developer Documentation Manuals](http://www.nextcomputers.org/NeXTfiles/Docs/NeXTStep/3.3/nd/),
    NeXT Software Inc. 1994, mirror accessed December 2019 **nextcomputers.org**

### Articles

* [The NEXTSTEP/OpenStep FAQ](https://www.levenez.com/NeXTSTEP/faq.html), Bernhard Scholz 1996, mirror accessed December 2019 **levenez*** [First NeXT RISCWorkstation: Our first look at NEXTSTEP on HP's low-cost pizza box](https://simson.net/ref/NeXT/nextworld/94.4/94.4.Apr.PA-RISC1.html), NeXTWORLD, April 1994
  * [First NeXT RISCWorkstation](https://archive.org/details/NeXTWORLDVol.4No.4April1994/page/n19/mode/2up) (PDF), NeXTWORLD, April 1994 **archive.org**
  * [NeXTstep on the HP 712 Part 1: Installation](https://blog.pizzabox.computer/posts/hp712-nextstep-part-1/), Sophie Haskins, Pizza Box Computer, 2020
  * <https://blog.pizzabox.computer/posts/hp712-nextstep-part-2/>, Sophie Haskins, Pizza Box Computer, 2020

[up](#top)

[OpenPA](https://www.openpa.net) is an independent resource for PA-RISC computers, technology and operating systems, edited since 1999 by [Paul Weissmann](about.html#people).
He also publishes [OpenKRITIS](https://www.openkritis.de) on critical infrastructures and [Insel Westberlin](https://westberlin.io), a Berlin archive.
OpenPA is a non-commercial, registered serial publication, ISSN 1866-2757. [The Internet never forgets](sources_internet_history.html).

* [About OpenPA](about.html)
* [Impressum/Datenschutz](impressum.html)
* [News](news.html)
* [Copyright © 1999—2026](about.html#copyright)
