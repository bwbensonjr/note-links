---
id: 788
url: https://math.ucr.edu/home/baez/tuning_talk/
title: The Mathematics of Tuning Systems
domain: math.ucr.edu
source_date: '2026-02-04'
tags:
- music
- academic-paper
- physics
summary: John Baez explores how mathematical principles underlie musical tuning systems,
  explaining that different scales (5-note, 7-note, and 12-note) have evolved to best
  approximate simple frequency ratios, particularly the "fifth" at 3/2. While Pythagorean
  tuning sought pure rational number ratios, modern 12-tone equal temperament divides
  each octave into 12 equal parts, making it the dominant tuning system since around
  1850 despite being mathematically simpler than its historical predecessors. The
  presentation demonstrates how mathematical innovations in tuning systems have driven
  the development of new musical styles throughout Western music history.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# The Mathematics of Tuning Systems

#### John Baez

#### [Mathematics Colloquium of the Claremont Colleges](https://colleges.claremont.edu/ccms/colloquium/), Claremont McKenna College, January 30, 2026

The Mathematics of Tuning Systems
---------------------------------

![](jpgs/tuning_talk-01.jpg)

> Leibniz said "Music is the pleasure the human mind experiences from
> counting without being aware that it is counting." The first step is
> choosing a tuning system — the frequency ratios between pitches
> in a scale. Different kinds of music sound best in different tuning
> systems! In music from the Middle Ages until today, new musical styles
> have gone hand in hand with mathematical innovations in tuning
> systems. Here I will focus on a few of the most important and
> beautiful Western systems, from Pythagorean tuning to today's reigning
> champion: equal temperament. Can you hear the difference? What will
> come next?

You read a version of my talk with my spoken remarks between the
slides, below! You can also see the [slides](tuning_talk.pdf) of my talk. And you can also read a
preliminary version of a [book](../tuning_book/tuning_book.html) I'm writing on this topic.

---

![](http://math.ucr.edu/home/baez/tuning_talk/jpgs/tuning_talk-02b.jpg)

If you look at a piano keyboard you'll see groups of 2 black notes alternating with groups of 3. So the pattern repeats after 5 black notes, but if you count you'll see there are also 7 white notes in this repetitive pattern. So: the pattern repeats each 12 notes.

Some people who never play the piano claim it would be easier if had all white keys, or simply white alternating with black. But in fact the pattern makes it easier to keep track of where you are — and it's not arbitrary, it's musically significant.

For one thing white notes give a 7-note scale all their own. Most very simple songs use only this scale! The black notes also form a useful scale. And the white and black notes together form a 12-tone scale.

![](http://math.ucr.edu/home/baez/tuning_talk/jpgs/tuning_talk-03b.jpg)

Starting at any note and going up 12 notes, we reach a note whose frequency is almost exactly double the one we started with. Other spacings correspond to other frequency ratios.

I don't want to overwhelm you with numbers. So I'm only showing you a few of the simplest and most important ratios. These are really worth remembering.

![](http://math.ucr.edu/home/baez/tuning_talk/jpgs/tuning_talk-04b.jpg)

We give the notes letter names. This goes back at least to Boethius, the guy famous for writing *The Consolations of Philosophy* before he was tortured and killed at the order of Theodoric the Great. (Yeah, "Great".) Boethius was a counselor to Theodoric, but he really would have done better to stay out of politics — he was quite good at math and music theory.

Boethius may be the reason the lowest note on the piano is called A. We now repeat the names of the white notes as shown in the picture: seven white notes A,B,C,D,E,F,G and then it repeats.

![](http://math.ucr.edu/home/baez/tuning_talk/jpgs/tuning_talk-05b.jpg)

So the scale used to start at A, using only white notes. But due to the irregular spacing of white notes, a scale of all white notes sounds different depending on where you start. Starting at A gives you the 'minor scale', which sounds kinda sad. Now we often start at C, since that gives us the scale most people like best: the 'major' scale.

(Good musicians start wherever they want, and get different sounds that way. But 'C major' is like the vanilla ice cream of scales — now. It wasn't always this way.)

![](http://math.ucr.edu/home/baez/tuning_talk/jpgs/tuning_talk-06b.jpg)

From the late 1100s to about 1600 people called pitches that lie outside 7-tone system "musica ficta": "false" or "fictitious" notes. But gradually these notes — the black keys on the piano when you're playing in C major — became more accepted.

To keep things simple for mathematicians, I'll usually denote these with the "flat" symbol, ♭. For example, G♭ is the black note one down from the white note G.

(Musicians really need both flats and sharps, and they'd also call G♭ something else: F♯. I'll actually need both G♭ and F♯ at some points in this talk!)

![](http://math.ucr.edu/home/baez/tuning_talk/jpgs/tuning_talk-07b.jpg)

Since starting the scale with the letter C takes a little practice, I'll do it a different way that mathematicians may like better. I'll start with 1 and count up. Musicians put little hats on these numbers, and I'll do that.

For example, we'll call the fifth white note up the scale the 'fifth' and write it as \(\hat{5}\).

![](http://math.ucr.edu/home/baez/tuning_talk/jpgs/tuning_talk-08b.jpg)

Now for the math of tuning systems!

The big question is: how do we choose the frequency of each note? This is literally how many times per second the air vibrates, when we play that note.

Since 1850, by far the most common method for tuning keyboards has been "12-tone equal temperament". Here we divide each octave into 12 equal parts.

What do I mean by this, exactly? I mean that each note on the piano produces a sound that vibrates faster than the note directly below it by a factor of the 12th root of 2.

But we can contemplate 'N-tone equal temperament' for N = 1, 2, 3, .... And some people do use these other tuning systems!

![](http://math.ucr.edu/home/baez/tuning_talk/jpgs/tuning_talk-09.jpg)

Here's a picture of the most popular modern tuning system: 12-tone equal temperament. As we march around clockwise, each note has a frequency of \(2^{1/12}\) times the note directly before it.

When we go all the way around the circle, we've gone up an octave. That is, we've reached a frequency that's twice the one we started with.

But a note that's an octave higher sounds 'the same, only higher'. So in a funny way we're back where we started.

![](http://math.ucr.edu/home/baez/tuning_talk/jpgs/tuning_talk-10b.jpg)

But now for a big question: why do we use a scale with 12 notes?

To start answering, notice that we actually use three scales: one with 5 notes (the black keys), one with 7 (the white keys) and one with 12 (all the keys).

As mathematicians we can detect a highly nonobvious pattern here.

![](http://math.ucr.edu/home/baez/tuning_talk/jpgs/tuning_talk-11b.jpg)

What's so good about scales with 5, 7 or 12 notes?

A crucial clue seems to be the 'fifth'. If you go up to the fifth white note here, its frequency is about 3/2 times the first. This is one of the simplest fractions, and it sounds incredibly simple and pure. So it's important. It's a dominant force in western music.

![](http://math.ucr.edu/home/baez/tuning_talk/jpgs/tuning_talk-12a.jpg)

We can make a chart to see how close an approximation to the fraction 3/2 we get in a scale with N equally spaced notes.

N = 5 does better than any scale with fewer notes!

N = 7 does better than any scale with fewer notes!

N = 12 does better than any scale with fewer notes! And it does *much* better. To beat it, we have to go all the way up to N = 29 — and even that is only slightly better.

![](http://math.ucr.edu/home/baez/tuning_talk/jpgs/tuning_talk-13.jpg)

Here's a chart of how close we can get to a frequency ratio of 3/2 using N-tone equal temperament.

See how great 12-tone equal temperament is?

There are also some neat patterns. See the stripes of even numbers and stripes of odd numbers? That's not a coincidence. For more charts like this, and much more cool stuff along these lines, go [here](https://johncarlosbaez.wordpress.com/2023/10/19/perfect-fifths-in-equal-tempered-scales-part-2/).

![](http://math.ucr.edu/home/baez/tuning_talk/jpgs/tuning_talk-14b.jpg)

Here's the 'star of fifths' in 12-tone equal temperament!

![](http://math.ucr.edu/home/baez/tuning_talk/jpgs/tuning_talk-15b.jpg)

12-tone equal temperament is most popular tuning system since maybe 1810, or definitely by 1850. But it's mathematically the most *boring* of the tuning systems that have dominated Western music since the Middle Ages. Now let's go back much earlier, to Pythagorean tuning.

When you chop the octave into 12 equal parts, the frequency ratios of all your notes are irrational numbers... *except* when you go up or down some number of octaves.

The Pythagoreans disliked irrational numbers. People even say they drowned Hippasus at sea after he proved that the square root of 2 is irrational! That's just a myth, but it illustrates how people connected Pythagoras to a love of rational numbers. In Pythagorean tuning, people wanted a lot of frequency ratios of 3/2.

In equal temperament, where we chop the octave into 12 equal parts, when we start at any note and go up 7 of these parts (a so-called 'fifth'), we reach a note that vibrates about 1.4981 times as fast. That's close enough to 3/2 for most ears. But it's not the Pythagorean ideal!

As we'll see, seeking the Pythagorean ideal causes trouble. It will unleash the devil in music.

![](http://math.ucr.edu/home/baez/tuning_talk/jpgs/tuning_talk-16.jpg)

Start at some note and keep multiplying the frequency by 3/2, like a good Pythagorean. After doing this 12 times, you reach a note that's close to 7 octaves higher. But not exactly, since the 12th power of 3/2 is

129.746338

which is a bit more than

27 = 128

The ratio of these two is called the 'Pythagorean comma':

p = (3/2)12 / 27 = 312 / 219 ≈ 1.0136

This is like an unavoidable lump in the carpet when you use Pythagorean tuning.

It's good to stick the lump in your carpet under your couch. And it's good to stick the Pythagorean comma near the so-called 'tritone' — a very dissonant note that you'd tend to avoid in medieval music. This note is halfway around the circle of fifths.

In Pythagorean tuning, going 6 steps clockwise around the circle of fifths doesn't give you the same note as going 6 steps counterclockwise! We call one of them ♭5 and the other ♯4.

Their frequency ratio is the Pythagorean comma!

![](http://math.ucr.edu/home/baez/tuning_talk/jpgs/tuning_talk-17.jpg)

In equal temperament, the tritone is exactly halfway up the octave: 6 notes up. Since going up an octave doubles the frequency, going up a tritone multiplies the frequency by √2. It's no coincidence that this is the irrational number that got Hippasus in trouble.

In Pythagorean tuning, going 6 steps up the scale doesn't match jumping up an octave and then going 6 steps down. We call one of them ♭5 and the other ♯4. They're both decent approximations to √2, built from powers of 2 and 3.

Their frequency ratio is the Pythagorean comma!

![](http://math.ucr.edu/home/baez/tuning_talk/jpgs/tuning_talk-18b.jpg)

The tritone is sometimes called 'diabolus in musica' — the devil in music. Some say this interval was actually *banned* by the Catholic church! But that's another myth.

It could have gotten its name because it sounds so dissonant — but mathematically, the 'devil' here is that the square root of 2 is irrational. If we're trying to use only numbers built from powers of 2 and 3, we have to arbitrarily choose one to approximate √2.

In Pythagorean tuning we can choose either

1024/729 ≈ 1.4047

called the sharped fourth, ♯4, or

729/512 ≈ 1.4238

called the flatted fifth, ♭5, to be our tritone. In this chart I've chosen the ♭5.

No matter which you choose, one of the fifths in the circle of fifths will be noticeably smaller than the rest. It's called the 'wolf fifth' because it howls like a wolf. You can hear a wolf fifth [here](../cultural/tuning/fifth_comparison.html).

![](http://math.ucr.edu/home/baez/tuning_talk/jpgs/tuning_talk-19.jpg)

If you're playing medieval music, you can easily avoid the wolf fifth: just don't play one of the two fifths that contains the tritone!

A more practical problem concerns the 'third': the third white note in the scale. Ideally this vibrates 5/4 as fast as the first. But in Pythagorean tuning it vibrates 81/64 times as fast. That's annoyingly high!

Sure, 81/64 is a rational number. But it's not the really *simple* rational number our ears are hoping for when we hear a third. You can compare a Pythagorean third to a third of 5/4 [here](../cultural/tuning/third_comparison.html).

Indeed, Pythagorean tuning punishes the ear with some very complicated fractions. The first, fourth, fifth and octave are great. But the rest of the notes are not. There's no way that 243/128 sounds better than an irrational number!

In the 1300s, when thirds were becoming more important in music, theorists embraced a beautiful solution to this problem, called 'just intonation'. Now let's talk about that.

![](http://math.ucr.edu/home/baez/tuning_talk/jpgs/tuning_talk-20.jpg)

It's an amazing fact that in western composed music, harmony became important only around 1200 AD, when Perotin expanded the brand new use of two-part harmony to four-part harmony.

This put pressure on musicians to use a new tuning system — or rather, to revive an old tuning system. It's often called 'just intonation' (though experts will find that vague). We can get using a cool trick, though I doubt this is how it was originally discovered.

First, draw a hexagonal grid of notes. Put a note with frequency 1 in the middle. Label the other notes by saying that moving one step to the right multiplies the frequency of your note by 3/2, while going up and to the right multiplies it by 5/4.

![](http://math.ucr.edu/home/baez/tuning_talk/jpgs/tuning_talk-21b.jpg)

Next, cut out a portion of the grid to use for our scale. We use this particular parallelogram — you'll soon see what's so great about it.

![](http://math.ucr.edu/home/baez/tuning_talk/jpgs/tuning_talk-22b.jpg)

Now, multiply each number in our parallelogram by whatever power of 2 it takes to get a number between 1 and 2.

We do this because we want frequencies that lie within an octave, to be notes in a scale. Remember: if 1 is the note we started with, 2 is the note an octave up.

![](http://math.ucr.edu/home/baez/tuning_talk/jpgs/tuning_talk-23.jpg)

Now we want to curl up our parallelogram to get a torus. If we do this, gluing together opposite edges, there will be exactly 12 numbers on our torus — just right for a scale! This is a remarkable coincidence.

There's a problem: the numbers at the corners are not all equal. But they're pretty close! And they're close to √2: the frequency of the tritone, the 'devil in music'.

25/18 = 1.3888...

45/32 = 1.40625

64/45 = 1.4222...

36/25 = 1.44

So we'll just pick one.

![](http://math.ucr.edu/home/baez/tuning_talk/jpgs/tuning_talk-24.jpg)

When we curl up our parallelogram to get a torus, there's also another problem. The numbers along the left edge aren't equal to the corresponding numbers at the right edge. But they're close! Each number at right is 81/80 times the corresponding number at left. I've drawn red lines connecting them.

So, we just choose one from each of these 4 pairs. We've already picked one number for all the corners, so we just need to do this for the remaining 2 pairs.

![](http://math.ucr.edu/home/baez/tuning_talk/jpgs/tuning_talk-25.jpg)

So, here are the various choices for notes in our scale!

For the tritone we have 4 choices. That's okay because this note sucks anyway. That is: in Western music from the 1300s, it was considered very dissonant. So there's no obviously best choice of how it should sound.

For the 2 we have two choices, and for the ♭7 we also have 2 choices. So there's a total of 16 possible scales here.

Regardless of how we make our choices, we'll get really nice simple fractions for the 1, ♭3, 3, 4, 5 ,♭6, 6, and 8. And that makes this approach, called 'just intonation', really great!

(If you like math: notice the 'up-down symmetry' in this whole setup. For example the minor second is 16/15, but the reciprocal of that is 15/16, which is the seventh... at least after we double it to get a number between 1 and 2, getting 15/8.)

![](http://math.ucr.edu/home/baez/tuning_talk/jpgs/tuning_talk-26.jpg)

Here's a chart of all possible just intonation scales: start at the top and take any route you want to the bottom. There are 16 possible routes.

A single step between notes in a 12-tone scale is called a 'semitone', since most white notes are two steps apart. In just intonation the semitones come in 4 different sizes, which is kind of annoying.

Notice that if we choose our route cleverly, we can completely avoid the large diatonic semitone. Or, we can avoid the greater chromatic semitone. But we can't avoid both. So, we can get a scale with just 3 sizes of semitone, but not fewer.

How should we choose???

![](http://math.ucr.edu/home/baez/tuning_talk/jpgs/tuning_talk-27.jpg)

This is the most commonly used form of just intonation, I think. It has a few nice features:

1) It has up-down symmetry except right next to the tritone in the middle, where this symmetry is impossible.

2) It uses 9/8 for the second rather than 10/9, which is a bit nicer: a simpler fraction.

3) It completely avoids the large diatonic semitone, which is the largest possible semitone.

These don't single out this one scale. I'd like to find some nice features that only this one of the 16 possibilities has.

But let's see what this scale looks like on the keyboard!

![](http://math.ucr.edu/home/baez/tuning_talk/jpgs/tuning_talk-28.jpg)

Here's the most common scale in just intonation!

The white notes are perhaps the most important here, since those give the 'major scale'. The fractions here are beautifully simple.

Well, okay: the second (9/8) and seventh (15/8) are not so simple. But that's to be expected, since these notes are the most dissonant! Of these, the seventh was more important in the music of the 1300s, and even today. It's called the 'leading-tone', because we often play it right near the end of a piece of music, or a passage within a piece of music, and its dissonance leads us up to the octave, with a tremendous sense of relief.

![](http://math.ucr.edu/home/baez/tuning_talk/jpgs/tuning_talk-29a.jpg)

Here's the really great thing about the white notes in just intonation. They form three groups, each with frequencies in the ratios

1 : 5/4 : 3/2

or in other words,

4 : 5 : 6

This pattern is called a 'major triad' and it's absolutely fundamental to music — perhaps not so much in the 1300s, but certainly as music unfolded later. Major triads became the bread and butter of music, and still are.

The fact that every white note — that is, every note in the 7-note 'major scale' — lies in a mathematically perfect major triad is a *gigantic* feature in favor of just intonation.

Listen to the difference between some simple chords in just intonation and in equal temperament. You probably won't *hate* equal temperament, but you can hear the difference. Equal temperament vibrates as the notes drift in and out of phase.

https://www.youtube.com/watch?v=AcCkn0p7HDE

![](http://math.ucr.edu/home/baez/tuning_talk/jpgs/tuning_talk-30.jpg)

But let's take a final peek at the dark underbelly of just intonation: the tritone. As I mentioned, there are four choices of tritone in just intonation. You can divide them into two pairs that are separated by a ratio of 81/80, or two pairs separated by a ratio of 128/125.

These numbers are fundamental glitches in the fabric of music. They have names! People have been thinking about them at least since Boethius around 500 AD, but probably earlier.

• The 'syntonic comma', 81/80, is all about trying to approximate a power of 3 by products of 2's and 5's.

• The 'lesser diesis', 128/125, is all about trying to approximate powers of 2 by powers of 5.

If these numbers were 1, music would be beautiful in a very simple way. But reality cannot be wished away.

And as we'll see, these numbers are lurking in the spacing between notes in just intonation — not just near the tritone, but everywhere!

![](http://math.ucr.edu/home/baez/tuning_talk/jpgs/tuning_talk-31.jpg)

Look! The four kinds of semitone in just intonation are related by the lesser diesis and syntonic comma!

In this chart, adding vectors corresponds to multiplying numbers. For example, the green arrow followed by the red one gives the dark blue one, so

25/24 × 81/80 = 135/138

Or in music terminology: the lesser chromatic semitone times the syntonic comma is the greater chromatic semitone.

And so on.

The parallelogram here is secretly related to the parallelogram we curled up to get the just intonation scale. Think about it! Music holds many mysteries.

![](http://math.ucr.edu/home/baez/tuning_talk/jpgs/tuning_talk-32b.jpg)

Just intonation is great if you're playing in just one 'key', always ending each passage with the note I've been calling 1. But when people started trying to 'change keys', musicians were pressed into other tuning systems.

It's sad in a way that this historical development winds up with equal temperament: the most *boring* of all the systems, which is equally good, and thus equally bad, in every key. But the history of music is not done, and computers make it vastly easier than ever before to explore tuning systems.

What will come next? It's up to us. To explore more of the mathematics of tuning systems, you can read some of my more detailed articles about it:

* **[Pythagorean Tuning](../tuning_book/tuning_book.html#pythagorean_tuning_1)**

  + [Part 1](../tuning_book/tuning_book.html#pythagorean_tuning_1): Pythagorean tuning, the Pythagorean comma, and the wolf fifth.
* **[Equal Temperament](../tuning_book/tuning_book.html#equal_temperament_1)**

  + [Part 1](../tuning_book/tuning_book.html#equal_temperament_1): Some equal-tempered scales with better perfect fifths than all equal-tempered scales with fewer notes.
  + [Part 2](../tuning_book/tuning_book.html#equal_temperament_2): Patterns that emerge when we study which equal-tempered scales have the best perfect fifths, major thirds or minor thirds.
* **[Just Intonation](../tuning_book/tuning_book.html#just_intonation_1)**

  + [Part 1](../tuning_book/tuning_book.html#just_intonation_1): The history of just intonation. Just intonation versus Pythagorean tuning. The syntonic comma.
  + [Part 2](../tuning_book/tuning_book.html#just_intonation_2): Just intonation from the Tonnetz. The four possible tritones in just intonation. The small and large just whole tones. Ptolemy's intense diatonic scale, and its major triads.
  + [Part 3](../tuning_book/tuning_book.html#just_intonation_3): Curling up a parallelogram in the Tonnetz to get just intonation. The frequency ratios of the four possible tritones: the syntonic comma, the lesser and greater diesis, and the diaschisma.
  + [Part 4](#just_intonation_4): Choices involved in just intonation. Two symmetrical 13-tone scales, and two 12-tone scales obtained from these by removing the diminished fifth. The four kinds of half-tone that appear in these scales: the diatonic, large diatonic, lesser chromatic and greater chromatic semitones.
  + [Part 5](../tuning_book/tuning_book.html#just_intonation_5): Frequency ratios between the four possible tritones in just intonation, and how they are related to frequency ratios between the four kinds of half-tone. The syntonic comma, lesser and greater diesis, diaschisma, and the relations they obey.
  + [Part 6](../tuning_book/tuning_book.html#just_intonation_6): Classifying all 174,240 12-tone scales where the intervals between successive notes are always diatonic, large diatonic, lesser chromatic and greater chromatic semitones. The scales of Isaac Newton, Nicolas Mercator, William Holder and Leonhard Euler.* **[Quarter-Comma Meantone](quarter-comma_meantone_1)**

    + [Part 1](../tuning_book/tuning_book.html#quarter-comma_meantone_1): Review of Pythagorean tuning. How to obtain quarter-comma meantone by expanding the Pythagorean major thirds to just major thirds.
    + [Part 2](../tuning_book/tuning_book.html#quarter-comma_meantone_21): How Pythagorean tuning, quarter-comma meantone and equal temperament all fit into a single 1-parameter family of tuning systems.
    + [Part 3](../tuning_book/tuning_book.html#quarter-comma_meantone_3): What ‘quarter-comma' means in the phrase ‘quarter-comma meantone': most of the fifths are lowered by a quarter of the syntonic comma.
    + [Part 4](../tuning_book/tuning_book.html#quarter-comma_meantone_4): Omitting the diminished fifth or augmented fourth from quarter-comma meantone. The relation between the Pythagorean comma, lesser diesis and syntonic comma.
    + [Part 5](../tuning_book/tuning_book.html#quarter-comma_meantone_5): The sizes of the two kinds of semitone in quarter-comma meantone: the chromatic semitone and diatonic semitone. The size of the tone, and what the ‘meantone' means in the phrase ‘quarter-comma meantone'.
    + [Part 6](../tuning_book/tuning_book.html#quarter-comma_meantone_6): What happens to quarter-comma meantone when you change it from a 13-tone scale to a more useful 12-tone scale by removing the diminished fifth.
    + [Part 7](../tuning_book/tuning_book.html#quarter-comma_meantone_7): Why it's better to start the quarter-comma meantone scale on D rather than C.
  * **[Well-Tempered Scales](../tuning_book/tuning_book.html#well-tempered_scales-1)**

    + [Part 1](../tuning_book/tuning_book.html#well-tempered_scales-1): An introduction to well temperaments.
    + [Part 2](../tuning_book/tuning_book.html#well-tempered_scales_1): How small intervals in music arise naturally from products of integral powers of primes that are close to 1. The Pythagorean comma, the syntonic comma and the lesser diesis.
    + [Part 3](../tuning_book/tuning_book.html#well-tempered_scales_3): Kirnberger's rational equal temperament. The schisma, the grad and the atom of Kirnberger.
    + [Part 4](../tuning_book/tuning_book.html#well-tempered_scales_4): The music theorist Kirnberger: his life, his personality, and a brief introduction to his three well temperaments.
    + [Part 5](../tuning_book/tuning_book.html#well-tempered_scales_5): Kirnberger's three well temperaments: Kirnberger I, Kirnberger II and Kirnberger III.

---

© 2026 John Baez  
baez@math.removethis.ucr.andthis.edu

### [home](http://math.ucr.edu/home/baez/README.html)
