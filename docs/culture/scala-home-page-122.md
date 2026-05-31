---
id: 122
url: https://www.huygens-fokker.org/scala/
title: Scala Home Page
domain: www.huygens-fokker.org
source_date: '2025-11-30'
tags:
- music
- cli-tool
summary: Scala is a comprehensive software tool designed for experimenting with diverse
  musical tunings, including just intonation, equal temperaments, microtonal scales,
  and non-Western scales. It offers an integrated suite of features for creating,
  editing, analyzing, and storing scales, plus the ability to generate MIDI files
  and tune electronic instruments. The software includes a graphical interface with
  850+ commands, extensive online help, support for exporting to various synthesizers
  and music software, and access to a large free library of scales for both analysis
  and music creation.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Scala Home Page

Scala Home Page
===============

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Scala logo Scala is a powerful software tool for experimentation with musical tunings, such as just intonation scales, equal and historical temperaments, microtonal and macrotonal scales, and non-Western scales. It supports scale creation, editing, comparison, analysis, storage, tuning of electronic instruments, and MIDI file generation and tuning conversion. All this is integrated into a single application with a wide variety of mathematical routines and scale creation methods. Scala is ideal for the exploration of tunings and becoming familiar with the concepts involved. In addition, a very large library of scales is freely available for Scala and can be used for analysis or music creation. Great care has been taken to make Scala's functions and operations very general. The range of parameter values that commands accept is made as general as possible. Often various forms of input are allowed. No arbitrary restrictions are made. Scales are stored in a [flexible format](scl_format.html). Intervals can be entered and saved as either ratios or cents values and be intermixed within a scale. Constructing scales from scratch is one of Scala's strengths. Kinds of scales that can be made with Scala include: [equal temperaments](http://xenharmonic.wikispaces.com/Equal), well-temperaments, Pythagorean (meantone) scales, [Euler-Fokker genera](../microtonality/efg.html), [Fokker periodicity blocks](../docs/fokkerpb.html), [harmonic scales](http://xenharmonic.wikispaces.com/OverToneSeries), Partch diamonds, Polychordal scales, Dwarf scales and [Wilson Combination Product Sets](http://en.wikipedia.org/wiki/Hexany). In addition, a set of command files is included to build other kinds of scales such as triadic scales, circular mirrorings, circulating temperaments, etc., and to serve as examples.| [Features](#features)   [**Download**](downloads.html)   [Distribution](#distribution)   [References](references.html)   [Examples](examples.html)   [Help Index](helpindx.html)   [Related Links](#related-links) | | | | |

---

Features
--------

* **Graphical user interface.** It incorporates the command line interface
  of the old console version but also provides dialogs for almost all functions. The
  remaining functions can be used by typing Scala commands.

  * **Plays scale tones via the soundcard.** Several screens allow different playing
    with tones of a scale via the soundcard's MIDI synthesizer or external MIDI instrument.

    * **Command line interface that recognises more than 850 commands for scale
      analysis and manipulation.** They are case insensitive and most can be
      abbreviated. In addition, the command syntax includes powerful features similar
      to those of a programming language.

      * **Extensive on-line help.** The built-in help function describes every
        command in detail and also includes useful information on other related
        topics. The help text is in HTML so you can view it with a browser and print it.
        In addition, the "tip of the day" function provides many useful hints and
        introduces features.

        * **Extensible functionality through command scripts.** You can create a
          script file containing Scala commands with any text editor, and then execute
          it inside Scala.

          * **Can capture screen output to text files.** Exporting scale data to
            other music software, such as Csound, is straightforward. A set of lexical
            functions is provided to convert program data to text.

            * **Exports tuning data to a variety of synthesizers with an internal tuning
              table.** You can save tuning data in a MIDI file or send it directly to your
              instrument or sound card. Supported tuning dump formats include among others:

              + AccSone crusherX, crusherX-Mac!+ Alphakanal Automat+ Aodyo Instruments Anyma Phi+ Arturia Pigments+ Ashun Sound Machines Hydrasynth+ Audio Damage Quanta, Phosphor+ BeepStreet Sunrizer+ Big Tick Angelina, Rainbow and Rhino softsynths+ Biptunia Synths Microtone 5000, Simple Microtonal Sampler, Freakbone 9000+ Bitheadz Unity softsynth+ Cakewalk Dimension Pro+ Cakewalk Rapture+ Cakewalk Z3ta+ softsynth+ Camel Audio Alchemy and Cameleon5000 softsynths+ Casio AT-3, AT-5, CTK-6000, CTK-6200, CTK-6250, CTK-6300, CTK-7000, CTK-7200, CTK-7300, WK-6500, WK-6600, WK-7500, WK-7600+ Celemony Melodyne 2+ ChucK+ DashSignature EVE one (not two)+ DaTuner+ Dave Smith Instruments OB-6, Prophet 6, Prophet 12 and Pro 2+ Devine Machine OTR88+ E-mu Morpheus+ E-mu Proteus series+ Ensoniq EPS/EPS16/ASR10+ Ensoniq TS-10/TS-12+ EplayOrgan virtual organ+ Fluidsynth and Qsynth softsynths+ FXpansion Strobe2+ Hauptwerk virtual organ+ HERCs series, Abakos Pro softsynths+ H-Pi Instruments microsynth and Xentone+ Humdrum hum2mid program+ Image-Line Harmor+ Kemper Digital Virus+ Korg M1, M1R octave tuning dump+ Korg X5DR octave tuning dump+ Korg OASYS PCI soundcard (and softsynths supporting its .tun tuning textfile)+ LinPlug Albino 2, Alpha 2, CronoX, MorphoX, Octopus, Organ 3, SaxLab and Spectral softsynths+ Macomate 88 VST+ Manytone ManyStation, ManyGuitar, ManyOne softsynths+ Marion Systems MSR-2+ Mark Henning AnaMark softsynth+ Max/MSP+ Max Magic Microtuner for Max/MSP and Pluggo softsynths+ MICROTONE 5000+ MIDI Tuning Standard (both bulk tuning dump and single-note tuning change, 3 byte),
                                                                                                          supported in Timidity and Audio Compositor, E-mu: Proteus 3,
                                                                                                          UltraProteus, Audity/Proteus 1000 and 2000 series, Virtuoso 2000, Proteus FX, Hydrasynth, Biptunia Synths, FabFilter Twin 3,
                                                                                                          Orbit, Planet Phatt, B3, Carnaval, Ensoniq: ASR-X, MR Rack, MR-61, MR-76,
                                                                                                          ZR-76, Turtle Beach: Multisound, Monterey, Maui, Tropez, Rio+ MIDI Tuning Standard 2-byte octave tuning dump+ MIDI Tuning Standard 1-byte octave tuning dump+ MIDI to CSound+ Modartt Pianoteq 4+ Modor NF-1, NF-1m+ MOTU Ethno 2 and Digital Performer+ Mutagene Mukoco, Macomate 88+ Novation Bass Station II, Peak, Summit+ Omringen Oblivion+ OpenMPT ModPlug Tracker+ Native Instruments Absynth 2 (via .gly file)+ Native Instruments FM7 and Pro-52, Pro-53+ Native Instruments Kontakt 2 (via script file)+ Native Instruments Reaktor (via semitones file, frequency file or NTF file)+ Oberheim OB-Mx+ Plaka Physical Modeling softsynth+ Plugin Boutique VirtualCZ+ Pure Data+ Rob Papen Predator 3, Quad, Vecto, RoCoder+ Robin Schmidt's Straightliner softsynth+ Roland GS & JV/XP families+ Roland Fantom-X6/X7/X8+ Roland V-Synth Version 2.0+ Roland Virtual Sound Canvas, SC-8850+ Scale Workshop+ Simple Microtonal Sampler+ Simple Microtonal Synth+ Smart Electronix Foorius+ Sobanth+ Spectrasonics Omnisphere softsynth+ Stone Voices PolyGAS+ Synapse Audio Orion Pro softsynth+ Synthesis Technology MOTM-650+ Synthogy Ivory+ TAL BassLine-101, J-8, Mod, Sampler, U-NO-LX+ ThumbJam+ Timidity MIDI to audio renderer+ Tobybear Helios softsynth and MicroTuner VST plugin+ Togu Audio Line TAL-Sampler, TAL-BassLine-101, TAL-U-NO-LX+ TransFormSynth+ Tubbutec 1oh1 µTune+ TuneLab+ U-He Zebra2, ACE, DIVA and Bazille+ UVI Falcon+ VAZ Plus, 2001 and Modular softsynths+ VirSyn Cube, Poseidon and TERA 2 softsynths+ Waldorf Wave, Microwave and Quantum+ Wallander Instruments WIVI Standard and Professional+ WayOutWare TimewARP 2600+ Wusik Station, Wusik 8000 and Ravernator+ Xen-Arts IVOR2, XenFont2 and Xenharmonic FMTS+ Xenharmonic FMTS VSTi+ Xfer Records Serum+ Xponaut Voice Tweaker+ Yamaha DX7II/TX802+ Yamaha SY77/TG77/SY99/VL-1/VL-7+ Yamaha TX81Z/DX11/V50 (both octave and full keyboard bulk data)+ Yamaha XG family+ Yamaha VL70m+ Zebra 2.0 softsynth+ Zefer Serum

              Nowadays many software synthesizers like AlsaModularSynth, Tobybear Helios, MAZ Sound VSampler,
              Orion Pro, VirSyn Cube, Cantor, TERA 2, rgc:audio z3ta+, Cakewalk Rapture, and Yoshimi have adopted
              the [Scala scale file format](scl_format.html) (see for a complete list) as a means to tune
              them instead of with a native tuning dump file. There's also
              a do-it-yourself hardware synth: [PreenFM2 frequency modulation sound generator](https://ixox.fr/preenfm2/)  
              Other instruments can be supported through modification of an external data file,
              if the system exclusive data format is straightforward.  
              Not all synthesizers have microtuning support in the form of a tuning table,
              or one with sufficient resolution, and therefore cannot be directly tuned by Scala.
              Hopefully more future synthesizers will be equipped with a full keyboard variable tuning
              capability. Be careful to check this before you buy.

              * **Flexible keyboard mapping.** For scales containing more or less than
                12 tones per octave, you can easily assign scale degrees to the standard piano
                keyboard by using a keyboard mapping. Scala supplies an example set of keyboard
                mappings for scales of various sizes that you can quickly adapt to your needs.

                * **Can retune existing MIDI files.** You can convert a standard MIDI file
                  to be in any tuning via pitch bend commands or a MIDI Tuning Standard tuning specification.

                  * **Can relay real-time MIDI.** You play on a MIDI keyboard to a soundcard or external
                    MIDI instrument and have the tuning changed via pitch bend commands. This way you don't need
                    an instrument with microtuning support in order to play in a given tuning.

                    * **Can create MIDI files from a microtonal score.** The score is a
                      text file which can be created with an editor or generated from a MIDI file by
                      Scala. The format is described in [Scala sequence file format](seq_format.html).
                      The tuning is done either with pitch bend commands or MIDI Tuning Standard real-time single-note changes.

                      * **Recognises more than 3300 musical modes.** You can check any scale
                        to see if it approximates an existing mode.

                        * **More than 800 note naming systems built in.** Notes can be named and shown
                          in a consistent way with microtonal accidentals.

                          * **Recognises more than 900 chords.** You can check the occurrence of these chords in any scale.

                            * **Recognises more than 650 rational intervals.**

                              * **Recognises more than 6600 regular temperaments.** You can check the name by giving a generator and period.

                                * **More than 5200 scales available.** Download these for free from this website, see the [**Download page**](downloads.html).

                                  * **Can create WAVE files with sinewave chords with arbitrary partials which can decay independently.**

                                    * **Reliable.** Scala is written in the programming language
                                      [Ada](https://www.adaic.org/advantages/).

                                      * **Available on multiple platforms:** Windows, GNU Linux, MacOS X (10.4 or higher)
                                        and Unix, see the [**Download page**](downloads.html).

                                        * **Free.** Please read the [distribution section](#distribution) below.

See [examples](examples.html) of some of Scala's features.

Screenshots
-----------

Click on the pictures to get a larger image.

[![screenshot 1](snapshot1s.png)](snapshot1.png)
[![screenshot 2](snapshot2s.png)](snapshot2.png)
[![screenshot 3](snapshot3s.png)](snapshot3.png)
[![screenshot 4](snapshot4s.png)](snapshot4.png)
[![screenshot 5](snapshot5s.jpg)](snapshot5.png)
[![screenshot 6](snapshot6s.png)](snapshot6.png)
[![screenshot 7](snapshot7s.png)](snapshot7.png)
[![screenshot 8](snapshot8s.jpg)](snapshot8.png)
[![screenshot 9](snapshot9s.png)](snapshot9.png)
[![screenshot 10](snapshot10s.png)](snapshot10.png)


---

Distribution
------------

Scala was created by Manuel Op de Coul in the Netherlands. E-mail:
[coul@huygens-fokker.org](mailto:coul@huygens-fokker.org)

Suggestions for improvements are always welcome. Contact the author in the event of questions or problems.

User interface languages available: English and Dutch. Help to create more translations is welcome.

**Scala is freeware without warranty and may not be sold, modified, or
distributed for sale in combination with commercial products. It may only be
distributed as one package containing all the files mentioned here and for free.**

Go to the [**Download page**](downloads.html).

---

Related Links
-------------

* [Ada programming](https://en.wikibooks.org/wiki/Ada_Programming)* [Ada programming language](https://ada-lang.io)* [Bibliography of tuning literature](../docs/bibliography.html)* [ChucK](https://chuck.cs.princeton.edu)* [Csound](https://www.csounds.com)* [Gervill software synthesizer](https://java.net/projects/gervill/pages/Home)* [Get Ada Now](https://www.getadanow.com)* [Huygens-Fokker foundation](../index_en.html)* [Learning Ada](https://learn.adacore.com)* [List of microtonal software plugins](https://en.xen.wiki/w/List_of_Microtonal_Software_Plugins)* [List of regular temperaments in Scala](../docs/lintemps.html)* [loopMIDI](https://www.tobias-erichsen.de/software/loopmidi.html) (Windows)* [Microtonal music on CD](../music/discography.html)* [Microtonal Synthesis: tuning capabilities of synthesizers](http://www.microtonal-synthesis.com)* [Pocket Gamelan (about Scala and Pd)](https://ro.uow.edu.au/creartspapers/22/)* [Scala for dummies](dummies.txt)* [Scala home page in Chinese](home-cn.html)* [Scala scale file format](scl_format.html)* [Scala sequence file format](seq_format.html)* [Timidity MIDI to sound converter](https://timidity.sourceforge.net)* [Tutorial for creating TUN files with Scala](Scala_TUN_Tutorial.pdf)
                                          (AnaMark, VAZ Plus, 2001, Modular; Big Tick Angelina, Rainbow, Rhino; LinPlug Albino2, Alpha2, CronoX, Octopus;
                                          Cameleon5000; VirSyn Cube, Tobybear Helios, TERA 2, Wusik WusikStation, Zebra 2.0, etc. softsynths)* [Using
                                            Scala to retune common practice music in meantone](https://en.xen.wiki/w/Using_Scala_to_retune_common_practice_music_in_meantone)* [Xenharmonic (microtonal wiki) page about Scala](https://en.xen.wiki/w/Scala)

Development software
--------------------

Scala was developed in [Ada](https://www.adaic.org/advantages/ada-overview/) with the following excellent free tools:

* [Excel Writer](https://sourceforge.net/projects/excel-writer/)* [GNAT](https://www.adacore.com/community): Gnu [Ada](https://www.adacore.com/about-ada) Translator* [GtkAda](https://www.adacore.com/gtkada)* [Gtk+](https://www.gtk.org)* [Zip-Ada](https://unzip-ada.sourceforge.io)

[![Ada - In Strong Typing We Trust](ada-strong-305-grey.png)](http://www.ada-auth.org/standards/12rat/html/Rat12-TOC.html)  

*27 Nov 2026*
