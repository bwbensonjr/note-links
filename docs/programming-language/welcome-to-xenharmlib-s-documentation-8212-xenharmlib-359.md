---
id: 359
url: https://xenharmlib.readthedocs.io/en/latest/
title: Welcome to xenharmlib’s documentation! &#8212; xenharmlib  documentation
domain: xenharmlib.readthedocs.io
source_date: '2025-07-09'
tags:
- python
- tutorial
- github-repo
summary: Xenharmlib is a generalized Python music theory library designed for exploring
  harmonic systems beyond the traditional 12-tone equal-tempered scale, supporting
  xenharmonic tunings, microtonal scales, posttonal set theory, and non-standard notations.
  The library provides tools for analyzing intervals, scales, and their relationships
  through both Western and alternative notation systems, with a focus on scientific
  exploration rather than score composition. It is built on functional programming
  principles, offering features like modulation suggestions, group theoretical analysis,
  and pattern matching for both traditional and unconventional musical systems.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Welcome to xenharmlib’s documentation! &#8212; xenharmlib  documentation

New Release

Xenharmlib 0.3.0 has just been released.
[Find out what’s new](whats_new_0_3_0.html)

Welcome to xenharmlib’s documentation![¶](#welcome-to-xenharmlibs-documentation "Link to this heading")
=======================================================================================================

---

> **Xenharmonic (adj.):** Pertaining to music which sounds unlike
> that composed in the familiar 12 tone equal-tempered scale.
>
> —*Ivor Darreg*

Xenharmlib is a generalized music theory library that supports traditional
Western and non-western harmonic systems, unconventional microtonal and
macrotonal tunings, diatonic and posttonal set theory and non-standard
notations.

It is easy to use, extendable, and tries to be intuitive. Have a peek:

```
from xenharmlib import WesternNotation
from xenharmlib.periodic import mod_connectors

n = WesternNotation()

# find out which I-III-V triads can be used
# to modulate between d minor and g major

d_minor = n.pc_scale(['D', 'E', 'F', 'G', 'A', 'Bb', 'C'])
g_major = n.pc_scale(['G', 'A', 'B', 'C', 'D', 'E', 'F#'])

for c in mod_connectors(d_minor, g_major, (0, 2, 4)):
    print(c)
```

```
WesternNoteScale([A0, C1, E1])
WesternNoteScale([C1, E1, G1])
```

---

```
from xenharmlib import EDOTuning
from xenharmlib import play
from xenharmlib import UpDownNotation

# create a supermajor 7 chord on vD for an
# equal temperament with 31 notes per octave

edo31 = EDOTuning(31)
n_edo31 = UpDownNotation(edo31)

d_down = n_edo31.note('vD', 4)
SM3 = n_edo31.shorthand_interval('^M', 3)
P5 = n_edo31.shorthand_interval('P', 5)
m7 = n_edo31.shorthand_interval('m', 7)

chord = n_edo31.scale(
   [
      d_down,
      d_down.transpose(SM3),
      d_down.transpose(P5),
      d_down.transpose(m7),
   ]
)
print(chord)
```

```
UpDownNoteScale([vD4, F#4, vA4, vC5], 31-EDO)
```

```
play(chord)
```

Your browser does not support the `audio` element.

```
play(chord, duration=1, play_as_chord=True)
```

Your browser does not support the `audio` element.

---

```
from xenharmlib import EDTuning
from xenharmlib import FrequencyRatio

# analyze group theoretical properties of
# Bohlen-Pierce tunings

bp = EDTuning(13, FrequencyRatio(3))

p1 = bp.pitch(4)
p2 = bp.pitch(18)
i1 = bp.interval(p1, p2)

print(p1.pc_index)
print(p2.pc_index)
print(i1.frequency_ratio)

dist = i1.get_generator_distance(
   bp.pitch(7)
)
print(dist)
```

Audience & Design Philosophy[¶](#audience-design-philosophy "Link to this heading")
-----------------------------------------------------------------------------------

Xenharmlib is targeted at composers and researchers who already have
basic knowledge in python programming.

Xenharmlib does **not** aim to be a score composition tool, sequencer,
or synthesizer (however it is possible to build such things on top of
it). Rather it wants to provide a toolset for exploring different
concepts of harmonic relations with a scientific focus.

Xenharmlib is object-oriented but mostly designed around functional
programming principles: Objects are considered immutable and methods
do not alter internal states but return modified versions of the
original object.

Features[¶](#features "Link to this heading")
---------------------------------------------

A selection of things supported by xenharmlib:

* Equal division tunings (e.g. Western, Modern Arabic, Turkish Makam,
  Bohlen-Pierce, Wendy Carlos’ Gamma Scale)
* Western notation (including interval naming)
* Up/Down notation (a superset of Western notation)
* Analysis of intervals, scales, and their relations to one another
* Group theoretical analysis (integer pitches, pitch classes, etc)
* Interval sequence pattern matching
* Modulation suggestions for arbitrary key changes
* Basic posttonal analysis (normal & prime form calculations, inversion, etc)

Roadmap[¶](#roadmap "Link to this heading")
-------------------------------------------

A list of planned features (not necessarily in chronological order):

* Templates for Western music
* Plugin interface for score rendering backends
* Advanced posttonal analysis (interval vectors, z-Relations, Forte numbers)
* Rothenberg propriety and interval matrices
* MOS scale generation utilities
* Just Intonation and prime limit tunings
* Extended Helmholtz-Ellis JI Pitch Notation
* Odd Limit Tunings
* Arel-Ezgi-Uzdilek notation

License[¶](#license "Link to this heading")
-------------------------------------------

Xenharmlib is released under the [GNU Public License v3](https://www.gnu.org/licenses/gpl-3.0.en.html).

You can find the source code hosted on [Gitlab.com](https://www.gitlab.com/retooth/xenharmlib)

Acknowledgments[¶](#acknowledgments "Link to this heading")
-----------------------------------------------------------

Thanks to [Kite Giedraitis](https://www.tallkite.com/) and
[Lumi Pakkanen](https://lumipakkanen.com/) and everyone else on the
Xenharmonic Alliance Discord who was patient with me when I was
struggling to implement UpDownNotation.

Support and Contact[¶](#support-and-contact "Link to this heading")
-------------------------------------------------------------------

If you want to ask for a new feature or report a bug, take it to the
[Gitlab issue page](https://gitlab.com/retooth/xenharmlib/-/issues).
In case you just wanna chat with the maintainer: I often hang around on
the [Xenharmonic Alliance Discord](https://discord.com/invite/FSF5JFT)
under the name `@retooth`

User Guide[¶](#user-guide "Link to this heading")
-------------------------------------------------

In the following, you will find a guide to most of xenharmlib’s
features.

Contents:

* [Quickstart](quickstart.html)
  + [Installation](quickstart.html#installation)
  + [Tunings and Pitches](quickstart.html#tunings-and-pitches)
  + [Pitch Intervals](quickstart.html#pitch-intervals)
  + [Pitch Scales](quickstart.html#pitch-scales)
  + [Notation](quickstart.html#notation)
  + [Notes](quickstart.html#notes)
  + [Note Intervals](quickstart.html#note-intervals)
  + [Note Scales](quickstart.html#note-scales)
  + [Playing and Exporting](quickstart.html#playing-and-exporting)
* [Western Notation](western_notation.html)
* [Advanced Scale Methods](adv_scale_methods.html)
  + [Index Masks and Partial Scales](adv_scale_methods.html#index-masks-and-partial-scales)
  + [Normalizations](adv_scale_methods.html#normalizations)
  + [Reflection](adv_scale_methods.html#reflection)
  + [Enharmonic ambiguity and set operations](adv_scale_methods.html#enharmonic-ambiguity-and-set-operations)
* [Advanced Notation Features](adv_notation_features.html)
  + [Enharmonic Strategies](adv_notation_features.html#enharmonic-strategies)
* [Interval Sequences](interval_seq.html)
  + [Creating sequences](interval_seq.html#creating-sequences)
  + [Templating and categorization](interval_seq.html#templating-and-categorization)
  + [Pattern matching](interval_seq.html#pattern-matching)
* [The `periodic` Package](periodic_package.html)
  + [Periodic Indexing](periodic_package.html#periodic-indexing)
  + [Periodic Index Masks](periodic_package.html#periodic-index-masks)
  + [Periodic Cutouts](periodic_package.html#periodic-cutouts)
  + [Modulation Connectors](periodic_package.html#modulation-connectors)
  + [Scalar Transposition](periodic_package.html#scalar-transposition)
  + [Pair Iteration](periodic_package.html#pair-iteration)
  + [Deriving Specific From Generic Intervals](periodic_package.html#deriving-specific-from-generic-intervals)
  + [Interval Sequence Pattern Matching](periodic_package.html#interval-sequence-pattern-matching)
* [Posttonal Basics](posttonal.html)
  + [Pitch Class Sets and Scales](posttonal.html#pitch-class-sets-and-scales)
  + [Transposition](posttonal.html#transposition)
  + [Inversion](posttonal.html#inversion)
  + [Normal Form](posttonal.html#normal-form)
  + [Prime Form](posttonal.html#prime-form)
* [Core API documentation](core_api.html)
  + [Frequency](core_api.html#module-xenharmlib.core.frequencies)
  + [Origin Context](core_api.html#module-xenharmlib.core.origin_context)
  + [Frequency Representations](core_api.html#module-xenharmlib.core.freq_repr)
  + [Scales](core_api.html#module-xenharmlib.core.scale)
  + [Intervals](core_api.html#module-xenharmlib.core.interval)
  + [Interval Sequences](core_api.html#module-xenharmlib.core.interval_seq)
  + [Tuning](core_api.html#module-xenharmlib.core.tunings)
  + [Pitch and PitchInterval](core_api.html#module-xenharmlib.core.pitch)
  + [PitchScale](core_api.html#module-xenharmlib.core.pitch_scale)
  + [Notation](core_api.html#module-xenharmlib.core.notation)
  + [Note and NoteInterval](core_api.html#module-xenharmlib.core.notes)
  + [NoteScale](core_api.html#module-xenharmlib.core.note_scale)
  + [Enharmonic Strategies](core_api.html#module-xenharmlib.core.enharm_strategies)
  + [Symbol Codes](core_api.html#module-xenharmlib.core.symbols)
  + [Exceptions](core_api.html#module-xenharmlib.exc)
* [Export and Output API documentation](export_api.html)
  + [Console audio output](export_api.html#module-xenharmlib.play)
  + [Audio export](export_api.html#module-xenharmlib.export.audio)
  + [Scala file export](export_api.html#module-xenharmlib.export.scl)
* [Notation API documentation](notation_api.html)
  + [UpDownNotation](notation_api.html#module-xenharmlib.notation.updown)
  + [WesternNotation](notation_api.html#module-xenharmlib.notation.western)
* [Periodic package API documentation](periodic_api.html)
  + [`cutouts()`](periodic_api.html#xenharmlib.periodic.cutouts)
  + [`find_iseq()`](periodic_api.html#xenharmlib.periodic.find_iseq)
  + [`index()`](periodic_api.html#xenharmlib.periodic.index)
  + [`index_mask()`](periodic_api.html#xenharmlib.periodic.index_mask)
  + [`is_in()`](periodic_api.html#xenharmlib.periodic.is_in)
  + [`mod_connectors()`](periodic_api.html#xenharmlib.periodic.mod_connectors)
  + [`pairs()`](periodic_api.html#xenharmlib.periodic.pairs)
  + [`partial()`](periodic_api.html#xenharmlib.periodic.partial)
  + [`scalar_transpose()`](periodic_api.html#xenharmlib.periodic.scalar_transpose)
  + [`scale_element()`](periodic_api.html#xenharmlib.periodic.scale_element)
  + [`spec_interval()`](periodic_api.html#xenharmlib.periodic.spec_interval)
* [Set class package API documentation](setc_api.html)
  + [`compact_forte()`](setc_api.html#xenharmlib.setc.compact_forte)
  + [`compact_rahn()`](setc_api.html#xenharmlib.setc.compact_rahn)
  + [`nf_forte()`](setc_api.html#xenharmlib.setc.nf_forte)
  + [`nf_rahn()`](setc_api.html#xenharmlib.setc.nf_rahn)
  + [`primeform_forte()`](setc_api.html#xenharmlib.setc.primeform_forte)
  + [`primeform_rahn()`](setc_api.html#xenharmlib.setc.primeform_rahn)
* [Changelog](changelog.html)
  + [0.3.0](changelog.html#changelog-0-3-0)
  + [0.2.0](changelog.html#changelog-0-2-0)
  + [0.1.1](changelog.html#id3)

Contributor Guide[¶](#contributor-guide "Link to this heading")
---------------------------------------------------------------

You are always welcome to open a pull request, however, there are some
prerequisites for a pull request to be accepted that you should know:

* For formatting your commit messages please use
  [conventional commits](https://www.conventionalcommits.org/)
* To format your code please use the
  [black code formatter](https://black.readthedocs.io/en/stable/)
  with string normalization turned off and maximum line length 79.
  In regards to strings, xemharmlib follows the principle single quotes
  (’) for data, double quotes (”) for information meant to be read only
  by humans (like exception descriptions) and triple-double quotes (“””)
  for docstrings.
* Your code should come with tests that cover everything you have done.
  (This includes branch coverage). Xenharmlib’s test framework is
  [pytest](https://docs.pytest.org/)
* Your code should come with type annotations. There are a few
  exceptions: Sometimes python’s typing system is not mature enough to
  do proper static-like typing (for example it doesn’t support
  higher-kinded types). Sometimes there are design reasons to use
  python’s dynamism. Just snoop around the existing code to get a
  feeling for this balance.
* Xenharmlib is designed around functional programming principles.
  Objects should not alter their state when calling methods (except
  on initialization methods)

Changelog[¶](#changelog "Link to this heading")
-----------------------------------------------

For a list of changes see [Changelog](changelog.html)

Indices and tables[¶](#indices-and-tables "Link to this heading")
=================================================================

* [Index](genindex.html)
* [Module Index](py-modindex.html)
* [Search Page](search.html)

[![Logo of xenharmlib](_static/sidebar-logo.png)](#)

[xenharmlib](#)
===============

### Navigation

Contents:

* [Quickstart](quickstart.html)
* [Western Notation](western_notation.html)
* [Advanced Scale Methods](adv_scale_methods.html)
* [Advanced Notation Features](adv_notation_features.html)
* [Interval Sequences](interval_seq.html)
* [The `periodic` Package](periodic_package.html)
* [Posttonal Basics](posttonal.html)
* [Core API documentation](core_api.html)
* [Export and Output API documentation](export_api.html)
* [Notation API documentation](notation_api.html)
* [Periodic package API documentation](periodic_api.html)
* [Set class package API documentation](setc_api.html)
* [Changelog](changelog.html)

### Related Topics

* [Documentation overview](#)
  + Next: [Quickstart](quickstart.html "next chapter")

©2024, Fabian Vallon.
|
Powered by [Sphinx 8.2.3](https://www.sphinx-doc.org/)
& [Alabaster 1.0.0](https://alabaster.readthedocs.io)
|
[Page source](_sources/index.rst.txt)
