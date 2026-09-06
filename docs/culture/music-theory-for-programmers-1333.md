---
id: 1333
url: https://runjs.app/blog/music-theory-for-programmers
title: Music theory for programmers
domain: runjs.app
source_date: '2026-09-06'
tags:
- music
- tutorial
- web-dev
- mathematics
- physics
summary: This article teaches music theory from first principles using code and the
  Web Audio API, starting with the physics of sound as changing air pressure. The
  author demonstrates how fundamental concepts like frequency, envelopes, and harmonics
  create musical meaning, then builds toward explaining why certain notes and scales
  work together based on mathematical relationships rather than arbitrary convention.
  By working through practical examples with sound generation, readers can understand
  the underlying reasons why music works the way it does without needing to play an
  instrument or memorize rules.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Music theory for programmers

Music theory for programmers
============================

![Luke Haas](/static/luke-haas.jpg)

Luke Haas

Aug 17, 2026

![Music theory for programmers](/static/blog/og/music-theory-for-programmers.png)

I can't play an instrument. I have tried more than once, and each time I got as far as being able to make roughly the right noises without ever understanding why they were the right noises.

The problem was never the practice. It was that every explanation of music theory seemed to miss out the fundamental reasons for how and why things are the way they are. Here is a staff. Here are the notes on it. This is a major scale, memorise the pattern. Why *those* notes? Why *that* pattern? Because that is the convention.

Which is a strange way to teach a system that essentially comes out of physics and arithmetic. There are twelve notes for a reason. The major scale has the shape it has for a reason. Chords that sound good sound good for a reason, and you can compute those reasons.

So I wanted to start from scratch and learn music from first principles, and I began that journey by writing code.

This article is the result. It starts with a single number changing over time, and if you follow along, you will derive the twelve notes, build scales and chords out of arrays, and write a chord progression that sounds like actual music. No instrument needed, and nothing you have to take on faith. Written notation does turn up, but not until the very end, once there is something for it to be notation *of*.

A sound is a number that changes over time
------------------------------------------

Sound is just air pressure wobbling. A speaker makes sound by pushing its cone in and out, and everything your computer does with audio comes down to producing a list of numbers describing where that cone should be, forty-four thousand times a second.

An audio file is that list written down. A synthesiser makes the list up as it goes, and the browser will do that part for you if you say what shape you want. The simplest shape is a sine wave, so here is one repeating 440 times a second:

A sine wave at 440Hz

```
const osc = ctx.createOscillator();



osc.frequency.value = 440;



osc.connect(out);



osc.start();



osc.stop(ctx.currentTime + 1);
```

Run

`ctx` and `out` are mine rather than the browser's. Everything else is the [Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API) exactly as it ships. To run that snippet anywhere else, start with:

```
const ctx = new AudioContext();



const out = ctx.destination;
```

The number 440 is the only thing there that carries any musical meaning, and even that is arbitrary. It is the frequency somebody agreed to call "A", and it is the tuning fork the rest of the system is pinned to. Change it to 300 and run it again. It still works, it just plays a different pitch. The oscillator has no idea what a note is. It only knows how many times a second to swing.

Frequency is pitch: higher number, higher note. Nothing else in music is going to be that simple.

### Why that note clicked

You may have heard a little click at the end of that. The browser did exactly what it was told. The click is physics.

The oscillator was mid-wave when it stopped, so the speaker cone was somewhere out at the edge of its travel and then instantly snapped back. An instant jump in pressure is what a click *is*.

The fix is a second number that changes over time, this one controlling volume rather than pitch. Musicians call the shape of it an envelope:

The same note with an envelope

```
const osc = ctx.createOscillator();



osc.frequency.value = 440;



const env = ctx.createGain();



const t = ctx.currentTime;



env.gain.setValueAtTime(0, t);



env.gain.linearRampToValueAtTime(0.3, t + 0.01);



env.gain.exponentialRampToValueAtTime(0.001, t + 1);



osc.connect(env).connect(out);



osc.start(t);



osc.stop(t + 1);
```

Run

An envelope is the volume curve of a single note, from silence back to silence. The rise at the front is the attack and the fall afterwards is the decay.

Ten milliseconds to fade in, then a slow decay to nearly nothing. That is the difference between a test tone and something you would be willing to listen to twice.

attack **10ms**decay **1.00s**

Playpluckpianobowed

Drag the attack out towards half a second and the note stops arriving and starts swelling. It is no longer something struck, it is something bowed, and the pitch has not moved by a single hertz. Most of what you hear as the character of a note comes from its envelope.

This is a simplified envelope, though. The full version is ADSR: attack, decay, sustain and release, where sustain is the level a note holds at while a key is down, and release is how it fades once you let go.

The function below is a helper that each subsequent example uses:

```
function note(freq, start = 0, length = 0.5, type = "sine") {



const t = ctx.currentTime + start;



const osc = ctx.createOscillator();



const env = ctx.createGain();



osc.type = type;



osc.frequency.value = freq;



env.gain.setValueAtTime(0, t);



env.gain.linearRampToValueAtTime(0.3, t + 0.01);



env.gain.exponentialRampToValueAtTime(0.001, t + length);



osc.connect(env).connect(out);



osc.start(t);



osc.stop(t + length);



}
```

Timbre is the frequencies you did not ask for
---------------------------------------------

A sine wave is a single frequency and nothing else, which is why it sounds like a hearing test and unlike any instrument. Pluck a guitar string tuned to 440Hz and you do get a wave repeating 440 times a second, but the string is also vibrating in halves, and in thirds, and in quarters, all at the same time. Those are extra frequencies at 880, 1320, 1760 and on up, all riding on top of the one you asked for.

That stack is called the harmonic series. The note you asked for is the fundamental, and the series is that frequency multiplied by 1, 2, 3, 4, 5 and on up:

**1x**220Hz

**2x**440Hz

**3x**660Hz

**4x**880Hz

**5x**1100Hz

**6x**1320Hz

**7x**1540Hz

**8x**1760Hz

The harmonic series of 220Hz. Click a bar to hear that harmonic on its own.

Click the bars. On their own they are fairly boring. What matters is that they arrive as a package, and the recipe of how loud each one is relative to the others is what makes a violin sound like a violin and not a trumpet. Musicians call that timbre, and it is the same note either way.

The browser ships four of those recipes ready-made:

Four waveforms, same pitch

```
["sine", "triangle", "square", "sawtooth"].forEach((type, i) => {



note(220, i * 0.7, 0.6, type);



});
```

Run

Same 220Hz, four very different characters. A square wave contains only the odd harmonics, which is why it sounds hollow and slightly electronic. A sawtooth contains all of them and sounds harsh and buzzy. The scope above shows the shape of each one as it plays, and the shape *is* the harmonic recipe.

Remember the harmonic series, because it explains most of what follows. Every note you play drags a stack of quiet extra notes along with it, and which notes those are is not up to us. It is arithmetic, fixed by the physics of vibrating strings and columns of air, and it comes out the same on every instrument built around them.

Doubling the frequency gives you the same note
----------------------------------------------

Here are five notes. Every one is double the frequency of the one before it.

One note, five times

```
[110, 220, 440, 880, 1760].forEach((freq, i) =>



note(freq, i * 0.45, 0.4),



);
```

Run

They are different pitches, and yet they sound like *the same note*. Not just similar, the same. Cultures with no contact with each other have landed on this independently: double the frequency and you get something so alike it deserves the same name. In Western notation these frequencies, in the above example, are all called A, and the distance between them is the octave.

The naming is not arbitrary, and the harmonic series explains why. Every harmonic of 440 is already sitting in the harmonic series of 220, because 220's series is 220, 440, 660, 880, 1100 and 440's is 440, 880, 1320, 1760. The higher note adds no frequency the lower note was not already producing, so your ear hears the same colour at a different brightness.

2:1

Play both220Hz and 440Hz, repeating every cycle of the lower note

That one observation gives us two rules we will lean on for the rest of the article.

Pitch is multiplicative, not additive. Going up an octave means times two, not plus anything. The gap from 110 to 220 is 110Hz and the gap from 880 to 1760 is 880Hz, and they sound like exactly the same distance. Frequency space is logarithmic, and every interval in music is a ratio.

We only have to solve one octave. Because doubling returns you to the same note, the problem of "which pitches should exist" reduces to "how should we divide up the space between a frequency and twice that frequency". Solve it once and the answer repeats across the whole audible range.

So: how do you divide an octave?

Simple ratios sound good, and here is why
-----------------------------------------

The naive answer is to divide it evenly and go home. Nobody does that, because it turns out we do not experience all pairs of frequencies the same way. Some combinations sound settled and some sound like a mistake, and you can hear the difference immediately.

Six ratios against the same note

```
const ratios = [



["2/1   octave", 2],



["3/2   fifth", 3 / 2],



["4/3   fourth", 4 / 3],



["5/4   major third", 5 / 4],



["16/15 semitone", 16 / 15],



["√2    the awkward one", Math.SQRT2],



];



ratios.forEach(([label, ratio], i) => {



note(220, i * 1.4, 1.2);



note(220 * ratio, i * 1.4, 1.2);



console.log(label, "->", (220 * ratio).toFixed(2) + "Hz");



});
```

Run

The first four sound like *chords*. The 16/15 sounds like two notes arguing. The last one sounds like a car alarm. And the pattern is not subtle once you see it: **the simpler the fraction, the better it sounds.** 2/1 the octave, then 3/2 the fifth, then 4/3 the fourth, then 5/4 the major third, and by the time you get to 16/15 it has fallen apart entirely.

That is a suspiciously arithmetic result for something as subjective as "sounds nice", and there are two physical reasons for it.

The first is the harmonic series again. Play 220 and 330 together, which is a 3:2 ratio. The first note produces 220, 440, 660, 880, 1100, 1320. The second produces 330, 660, 990, 1320, so they share 660 and 1320 exactly. Two notes a fifth apart are not really two separate sounds, they are two heavily overlapping stacks that reinforce each other. Now try 220 and 311, which is close to √2. Nothing lines up, at any harmonic. You get two full stacks of frequencies that have nothing to do with each other.

The second reason is roughness. When two frequencies are close but not identical, they drift in and out of phase and you hear the volume pulsing. That is beating, and it is the thing that makes an out-of-tune note sound out of tune:

Beating, from wide apart to identical

```
[220, 226, 223, 221, 220.5, 220].forEach((freq, i) => {



note(220, i * 1.3, 1.2);



note(freq, i * 1.3, 1.2);



});
```

Run

The wobble slows down as the two frequencies converge and vanishes when they match, and the rate of it is exactly the difference between them. Six hertz apart, six pulses a second. When the fractions are complicated, the two stacks of harmonics are littered with pairs that are a few hertz apart, and every one of those pairs is beating away against the others. That is what dissonance is.

2:13:24:35:416:15√2

Play both220Hz and 440Hz, repeating every cycle of the lower note

Switch between the ratios above and watch the green line, which is the two waves added together, exactly as your eardrum would add them. For 2:1 and 3:2 the combined shape settles into a repeating pattern almost immediately. For 16:15 it takes fifteen cycles to come back round. For √2 it never does, because √2 is irrational, so there is no pattern for your ear to lock onto at all.

**Consonance is your ear finding a repeating pattern quickly.** As far as I can tell, that is all it is.

Stacking fifths, and the bug you cannot fix
-------------------------------------------

Now we can actually build something. We know that simple ratios are the good ones, and after the octave itself, the cleanest ratio in physics is 3/2, the fifth.

So what happens if we try to build a musical alphabet using only octaves and fifths?

Do the obvious thing: keep going up by fifths, halving whenever you leave the octave. This is roughly what Pythagoras did, and it works beautifully for a while:

Stacking fifths inside one octave

```
let freq = 220;



const notes = [220];



for (let i = 0; i < 12; i++) {



freq = (freq * 3) / 2;



while (freq >= 440) freq = freq / 2;



notes.push(freq);



console.log(`fifth ${i + 1}: ${freq.toFixed(3)}Hz`);



}



notes.sort((a, b) => a - b).forEach((f, i) => note(f, i * 0.22, 0.3));
```

Run

Look at the first note and the last note. We started on 220, applied twelve fifths, and landed on 222.99. Not 220. Close enough to be audibly *trying* to be the same note, and far enough off to be unusable.

The error is not rounding but something structural, and it is easier to see without the octave-folding:

The gap that cannot be closed

```
const twelveFifths = (3 / 2) ** 12;



const sevenOctaves = 2 ** 7;



console.log("twelve fifths:", twelveFifths.toFixed(6));



console.log("seven octaves:", sevenOctaves.toFixed(6));



console.log("ratio:", (twelveFifths / sevenOctaves).toFixed(6));



console.log(



"in cents:",



(1200 * Math.log2(twelveFifths / sevenOctaves)).toFixed(2),



);



note(220, 0, 1.5);



note((220 * twelveFifths) / sevenOctaves, 0, 1.5);
```

Run

Twelve perfect fifths overshoot seven perfect octaves by a factor of 1.0136. That gap is called the Pythagorean comma. Cents are how pitch distances get measured, and there are 1200 of them in an octave, which is where that number in the code comes from. So 23 cents is about a quarter of the gap between two adjacent piano keys, and you can hear it in that last pair of notes as a slow ugly beating.

And it cannot be fixed, for a reason a programmer will recognise. Stacking fifths means multiplying by 3/2, so after `n` fifths you are at `3^n / 2^n`. Stacking octaves means `2^m`. For the two to ever meet you would need `3^n = 2^(n+m)`, which requires a power of three to equal a power of two. Three and two are both prime. It never happens, for any n, ever.

The system we want, where the octave is pure and the fifths are pure and everything closes into a neat loop, does not exist and never has. Every tuning system in history is a different choice about where to dump the error.

Equal temperament is the compromise
-----------------------------------

The modern answer is to give up on pure ratios altogether. Take the octave, divide it into twelve *equal* multiplicative steps, and accept that nothing except the octave will be exactly right ever again.

One step is the twelfth root of two:

The twelfth root of two

```
const semitone = 2 ** (1 / 12);



console.log("one semitone =", semitone);



let freq = 220;



for (let i = 0; i < 13; i++) {



note(freq, i * 0.2, 0.28);



freq = freq * semitone;



}



console.log(



"twelve steps later:",



(220 * semitone ** 12).toFixed(10),



);
```

Run

Twelve steps land on exactly 440, because that is how roots work, so the octave is perfect by construction and everything else is approximated.

The obvious question is why twelve. It is not tradition, and you can find the answer yourself in about fifteen lines. Divide the octave into `n` equal steps for every plausible `n`, then check how close the best available step comes to a real 3/2 fifth:

Brute-forcing the number twelve

```
function bestFifth(n) {



let error = Infinity;



let step = 0;



for (let candidate = 1; candidate < n; candidate++) {



const off = Math.abs(2 ** (candidate / n) - 1.5);



if (off < error) {



error = off;



step = candidate;



}



}



return { step, error };



}



for (let n = 5; n <= 25; n++) {



const { step, error } = bestFifth(n);



const pct = (error / 1.5) * 100;



console.log(



`${n} steps: best fifth is step ${step}, off by ${pct.toFixed(3)}%`,



);



}



// And here is what those errors actually sound like.



[5, 7, 12, 19].forEach((n, i) => {



const { step } = bestFifth(n);



note(220, i * 1.7, 1.5);



note(220 * 2 ** (step / n), i * 1.7, 1.5);



});
```

Run

Those last four lines play the best fifth that 5, 7, 12 and 19 divisions can manage, each against the same 220Hz. The first two wobble, the third is clean, and the fourth sits in between. You are listening to the error column.

Twelve is the first division that gets the fifth right to about a tenth of a percent, and it is more than three times better than anything below it. Twenty-four ties, but only because twenty-four steps is twelve steps with a spare note wedged between each pair, so it is not really a competitor. You have to go all the way to 29 and 41 before the fifth gets better, and nobody is building a keyboard with 41 keys per octave. It is the cheapest number of notes that buys you a convincing fifth, and once the fifth is close the fourth and the thirds come along for the ride.

Here is how close:

Real fifth against the compromise

```
const pure = (220 * 3) / 2;



const tempered = 220 * 2 ** (7 / 12);



console.log("pure fifth:     ", pure.toFixed(4) + "Hz");



console.log("tempered fifth: ", tempered.toFixed(4) + "Hz");



console.log(



"difference:     ",



(1200 * Math.log2(tempered / pure)).toFixed(2),



"cents",



);



note(220, 0, 1.5);



note(pure, 0, 1.5);



note(220, 2, 1.5);



note(tempered, 2, 1.5);
```

Run

Two cents flat. There is a slow beat in the second pair if you listen for it, and that beat is present in every fifth played on every piano on Earth. We all decided that being slightly wrong everywhere was better than being perfect in one key and unusable in the others.

The payoff is that notes are now **integers**. Pick any note as number 0, and every other note is a whole number of semitones away from it. The convention is MIDI numbering, where 69 is our 440Hz A, and the conversion is one line:

Notes are integers now

```
const midiToFreq = (n) => 440 * 2 ** ((n - 69) / 12);



console.log("60 (middle C):", midiToFreq(60).toFixed(2));



console.log("69 (the A above it):", midiToFreq(69).toFixed(2));



console.log("81 (an octave up):", midiToFreq(81).toFixed(2));



[60, 62, 64, 65, 67, 69, 71, 72].forEach((n, i) =>



note(midiToFreq(n), i * 0.25, 0.4),



);
```

Run

That last line is a major scale, and we have not defined what a scale is yet. It is just an array of integers. From here on everything in this article is done with arrays, and I stopped needing to think about frequencies at all.

C4D4E4F4G4A4B4C5D5E5F5G5A5B5C6C#4D#4F#4G#4A#4C#5D#5F#5G#5A#5

Click a key

Twelve notes per octave, repeating forever. The black keys are not special, they are just the ones that did not get letter names.

That keyboard is worth staring at for a second, because the layout is a historical accident. There are twelve equally spaced notes per octave. Seven of them got letters and a big white key, five got a sharp sign and a small black key, and the seven with white keys are exactly the scale you just played. The physics underneath is completely uniform, and the keyboard is not.

Why twelve notes and not all of them
------------------------------------

Having twelve notes does not mean using twelve notes. Play all of them in order and it is remarkably unmusical:

All twelve, in order

```
const midiToFreq = (n) => 440 * 2 ** ((n - 69) / 12);



for (let n = 60; n <= 72; n++) {



note(midiToFreq(n), (n - 60) * 0.18, 0.25);



}
```

Run

It sounds like a sound effect. Every step is identical, so nothing stands out, nothing sounds like home, and there is no way to tell where you are.

Music picks a **subset**. Almost always seven of the twelve, chosen so that the gaps between them are uneven, which is exactly what makes it possible to tell one note from another by ear. The subset is a scale, and a scale is best written not as notes but as the steps between them:

A scale is a list of gaps

```
const midiToFreq = (n) => 440 * 2 ** ((n - 69) / 12);



const major = [2, 2, 1, 2, 2, 2, 1];



function buildScale(root, pattern) {



return pattern.reduce(



(notes, step) => [...notes, notes.at(-1) + step],



[root],



);



}



const cMajor = buildScale(60, major);



console.log("C major:", cMajor);



cMajor.forEach((n, i) => note(midiToFreq(n), i * 0.25, 0.4));
```

Run

The steps are `2 2 1 2 2 2 1`, adding up to 12 so the pattern closes the octave exactly. That is the major scale, the single most familiar sound in Western music, and it is a seven-element array.

Change one number and it becomes a completely different mood:

One number is the difference between happy and sad

```
const midiToFreq = (n) => 440 * 2 ** ((n - 69) / 12);



const build = (root, pattern) =>



pattern.reduce(



(notes, step) => [...notes, notes.at(-1) + step],



[root],



);



const patterns = {



major: [2, 2, 1, 2, 2, 2, 1],



naturalMinor: [2, 1, 2, 2, 1, 2, 2],



majorPenta: [2, 2, 3, 2, 3],



minorPenta: [3, 2, 2, 3, 2],



blues: [3, 2, 1, 1, 3, 2],



};



let when = 0;



Object.entries(patterns).forEach(([name, pattern]) => {



const scale = build(60, pattern);



console.log(name.padEnd(13), scale.join(" "));



scale.forEach((n, i) => note(midiToFreq(n), when + i * 0.22, 0.35));



when += scale.length * 0.22 + 0.5;



});
```

Run

Major and natural minor are the same seven-note idea with the gaps shuffled. The pentatonic scales drop two notes, which is why it is so hard to play a wrong note in them, and why every beginner guitar lesson starts there. The blues scale adds one deliberately awkward note back in.

The modes, which I had always seen presented as seven exotic Greek names to be memorised, turn out to be the *same array rotated*. Take the first step off the front, put it on the back, and you have the next one:

Modes are array rotations

```
const midiToFreq = (n) => 440 * 2 ** ((n - 69) / 12);



const build = (root, pattern) =>



pattern.reduce(



(notes, step) => [...notes, notes.at(-1) + step],



[root],



);



const major = [2, 2, 1, 2, 2, 2, 1];



const names = [



"Ionian",



"Dorian",



"Phrygian",



"Lydian",



"Mixolydian",



"Aeolian",



"Locrian",



];



const rotate = (arr, by) =>



arr.map((_, i) => arr[(i + by) % arr.length]);



names.forEach((name, i) => {



const pattern = rotate(major, i);



console.log(name.padEnd(11), pattern.join(" "));



build(60, pattern).forEach((n, j) =>



note(midiToFreq(n), i * 2 + j * 0.2, 0.3),



);



});
```

Run

Seven modes, one array, seven rotations. Ionian is the major scale and Aeolian is the natural minor, which means "major" and "minor" are not two systems, they are rotation 0 and rotation 5 of the same thing. Lydian sounds dreamy and Phrygian sounds Spanish and Locrian sounds broken, and all of that comes from moving which gap sits where relative to the note you started on.

This is the point where I stopped feeling like music theory was arbitrary.

Chords are notes stacked in thirds
----------------------------------

A chord is more than one note at the same time. Which is not much of a definition, because most combinations sound terrible. The useful question is which combinations do not.

We already know the answer from the ratios: notes whose harmonics overlap. In a scale, the notes that fit that description are the ones two scale degrees apart, a gap musicians call a third. So take a scale, pick a starting degree, and grab every *other* note:

A triad is [0, 2, 4]

```
const midiToFreq = (n) => 440 * 2 ** ((n - 69) / 12);



const build = (root, p) =>



p.reduce((n, s) => [...n, n.at(-1) + s], [root]);



const cMajor = build(60, [2, 2, 1, 2, 2, 2, 1]);



const triad = [0, 2, 4].map((i) => cMajor[i]);



console.log("scale:", cMajor.join(" "));



console.log("triad:", triad.join(" "));



console.log("gaps:", triad[1] - triad[0], "and", triad[2] - triad[1]);



triad.forEach((n) => note(midiToFreq(n), 0, 2));
```

Run

That is a C major chord. Three notes, at 0, 4 and 7 semitones above the note it is built on, which musicians call the root. In frequency that is 1 : 1.26 : 1.50, very nearly 4 : 5 : 6. Three simple ratios sharing harmonics all over the place, which is why it sounds so settled.

A third is either 4 semitones (a major third) or 3 semitones (a minor third), and stacking two of them gives you 7 semitones either way: major is 4 + 3, while minor is 3 + 4.

Now move the middle note down by one semitone:

One semitone, entirely different feeling

```
const midiToFreq = (n) => 440 * 2 ** ((n - 69) / 12);



const chord = (shape, root, at) =>



shape.forEach((s) => note(midiToFreq(root + s), at, 1.6));



const shapes = {



major: [0, 4, 7],



minor: [0, 3, 7],



diminished: [0, 3, 6],



augmented: [0, 4, 8],



};



Object.entries(shapes).forEach(([name, shape], i) => {



console.log(name.padEnd(11), shape.join(" "));



chord(shape, 60, i * 2);



});
```

Run

Major to minor is one note moving by one semitone. That is all that separates the two emotional poles of Western music, and in code it is `[0,4,7]` versus `[0,3,7]`. Diminished squashes both gaps and sounds unresolved and anxious. Augmented stretches both and sounds like something is about to go wrong in a film.

I found this genuinely annoying to discover, in a good way. I had absorbed the idea that major and minor were deep categories. They are a single array element differing by one.

Add a fourth note, another third up, and you get seventh chords, and this is where it starts to sound like actual music rather than a hymn:

Sevenths

```
const midiToFreq = (n) => 440 * 2 ** ((n - 69) / 12);



const shapes = {



"major 7th": [0, 4, 7, 11],



"minor 7th": [0, 3, 7, 10],



"dominant 7th": [0, 4, 7, 10],



};



Object.entries(shapes).forEach(([name, shape], i) => {



console.log(name.padEnd(13), shape.join(" "));



shape.forEach((s) => note(midiToFreq(60 + s), i * 2.2, 1.8));



});
```

Run

Major 7th is the jazz-cafe chord. Minor 7th is smooth and slightly melancholy. The dominant 7th is the interesting one. Dominant is just the traditional name for the fifth degree of a scale, and this chord is about to do a lot of work.

A key gives you seven chords
----------------------------

This is the part that made chord charts finally make sense to me.

There is nothing special about starting on the first degree. Do it from each of the seven in turn, wrapping around the octave, and you get seven chords, all built only from the seven notes of the scale:

Seven chords out of one scale

```
const midiToFreq = (n) => 440 * 2 ** ((n - 69) / 12);



const build = (root, p) =>



p.reduce((n, s) => [...n, n.at(-1) + s], [root]);



const scale = build(60, [2, 2, 1, 2, 2, 2, 1]).slice(0, 7);



const names = ["C", "D", "E", "F", "G", "A", "B"];



const chordOn = (degree) =>



[0, 2, 4].map((step) => {



const i = degree + step;



return scale[i % 7] + Math.floor(i / 7) * 12;



});



names.forEach((name, degree) => {



const notes = chordOn(degree);



const shape = notes.map((n) => n - notes[0]);



const quality =



shape[1] - shape[0] === 4



? "major"



: shape[2] - shape[0] === 6



? "diminished"



: "minor";



console.log(`${name} ${quality.padEnd(11)} ${notes.join(" ")}`);



notes.forEach((n) => note(midiToFreq(n), degree * 1.5, 1.3));



});
```

Run

Nobody chose those qualities. Three of them come out major, three come out minor, and the last one comes out diminished, and that pattern is forced by the uneven gaps in the scale. Start the every-other-note process on a degree whose neighbours are spaced 4 then 3, you get a major chord. Spaced 3 then 4, you get a minor one.

Musicians write those seven as Roman numerals: capital for major, lowercase for minor, and a small circle for the diminished one.

**I ii iii IV V vi vii°**

That notation is doing something useful, and it took me an embarrassingly long time to notice what. It describes chords by their *position in the scale*, not by their name. A `V` chord is "the chord built on the fifth degree", whatever key you are in, which is relative addressing. A chord chart written in Roman numerals is key-independent source, and transposing is adding a constant:

Roman numerals are relative addressing

```
const midiToFreq = (n) => 440 * 2 ** ((n - 69) / 12);



const build = (root, p) =>



p.reduce((n, s) => [...n, n.at(-1) + s], [root]);



function chordsInKey(root) {



const scale = build(root, [2, 2, 1, 2, 2, 2, 1]).slice(0, 7);



return (degree) =>



[0, 2, 4].map((step) => {



const i = degree - 1 + step;



return scale[i % 7] + Math.floor(i / 7) * 12;



});



}



// The same four numerals, played in two different keys.



const progression = [1, 5, 6, 4];



[60, 65].forEach((key, k) => {



const chord = chordsInKey(key);



progression.forEach((numeral, i) => {



chord(numeral).forEach((n) =>



note(midiToFreq(n), k * 7 + i * 1.6, 1.5),



);



});



});
```

Run

Same shape, two different starting notes, and your ear recognises it as the same music, which is why the notation exists.

Tension and resolution
----------------------

One chord is just a sound. Music is what happens when you put them in an order, and the order matters. Some sequences feel like they have arrived and some feel like a question.

The strongest pull in the system is from `V` back to `I`, and there are two concrete reasons for it.

The pull of V back to I

```
const midiToFreq = (n) => 440 * 2 ** ((n - 69) / 12);



const play = (notes, at, len = 1.6) =>



notes.forEach((n) => note(midiToFreq(n), at, len));



const C = [60, 64, 67]; // I



const G7 = [55, 59, 62, 65]; // V7



play(G7, 0, 1.8);



play(C, 2, 2.2);



console.log("B is", 59, "and C is", 60, "- one semitone apart");



console.log("F is", 65, "and E is", 64, "- one semitone apart");
```

Run

First, the note B sits in the `V` chord and is one semitone below the root of `I`. A note that close to a destination sounds like it is leaning on the door. Musicians call it the leading tone, and it works like a cliffhanger.

Second, the dominant 7th chord contains both B and F, which are six semitones apart. Six semitones is the tritone, exactly half an octave: `2 ** (6/12)` is the square root of two, the exact irrational ratio we heard earlier. The single most unstable interval available, sitting inside the chord, and both of its notes resolve by one semitone in opposite directions when you move to `I`. The tension you hear is that irrational ratio being swapped for simple ones.

The language of tension and release is built on that mechanism. Here it is with a few of the progressions you have heard ten thousand times:

Four progressions you already know

```
const midiToFreq = (n) => 440 * 2 ** ((n - 69) / 12);



const build = (root, p) =>



p.reduce((n, s) => [...n, n.at(-1) + s], [root]);



const scale = build(60, [2, 2, 1, 2, 2, 2, 1]).slice(0, 7);



const chord = (degree) =>



[0, 2, 4].map((step) => {



const i = degree - 1 + step;



return scale[i % 7] + Math.floor(i / 7) * 12;



});



const progressions = {



"I  V  vi IV": [1, 5, 6, 4],



"ii V  I": [2, 5, 1],



"I  vi IV V": [1, 6, 4, 5],



"vi IV I  V": [6, 4, 1, 5],



};



let when = 0;



Object.entries(progressions).forEach(([name, degrees]) => {



console.log(



name,



"->",



degrees.map((d) => chord(d).join("/")).join("  "),



);



degrees.forEach((d, i) => {



chord(d).forEach((n) => note(midiToFreq(n), when + i * 1.1, 1));



});



when += degrees.length * 1.1 + 0.9;



});
```

Run

`I V vi IV` is the four chords that an alarming share of pop music is built from. `ii V I` is the backbone of jazz. `vi IV I V` is the same four chords as the first one, rotated to start somewhere sadder.

Edit the arrays. Almost any sequence of numbers from 1 to 7 will hang together, because every chord is built from the same seven notes. A key buys you a constrained space where wrong answers are hard to reach. Ending on 1 sounds finished, ending on 5 sounds like there is another line coming, and ending on 7 sounds like something has gone wrong.

Notation is a serialisation format
----------------------------------

None of what came before needed a staff. Everything above is arrays of integers and a function that turns them into frequencies.

But notation exists, it is the format the literature of Western music is stored in, and once you already know what it is encoding it turns out to be a fairly sensible design with some very old constraints. It is a serialisation format, written before printing was cheap, optimised for a human reading it in real time while their hands are busy, and never revised because the install base was too large.

Here is the C major scale, the same seven integers as before:

PlayMIDI 60 62 64 65 67 69 71 72

The vertical axis is pitch, but not linearly. Each line and each space is one step up the scale, so consecutive positions are sometimes two semitones apart and sometimes one. The axis is diatonic rather than chromatic: it steps through the scale rather than through all twelve notes, which means it is showing you scale degrees dressed up as pitches. That is why the major scale looks like a boring straight run up the page and sounds like the most natural sequence in the world. The format is optimised for the case it expects.

The clef declares the origin. A staff is five lines with nothing pinning it to any frequency, so the symbol at the front tells you where you are. The treble clef is a stylised G, and the curl of it wraps around the line that means G. The bass clef is a stylised F with two dots straddling the F line. It is a coordinate system with the origin marked in the margin:

PlayIdentical shape, bass clef, an octave lower

Same shape on the page, different origin, so it plays back an octave down. Treble and bass are the two most common clefs, covering between them most of what people sing and play.

Accidentals patch the lossy encoding. Seven vertical positions per octave, twelve notes to represent. The sharp, flat and natural signs are the escape hatch, and every one of them is an instruction to shift the note the position would otherwise mean:

PlayEight of the twelve chromatic notes, with the sharps written in

The key signature is DRY. If a piece is in D major, its scale contains F sharp and C sharp, and every single F and C in the piece would need a sharp sign next to it. So instead you declare it once, at the front of every line, and it applies until something says otherwise. It is a constant hoisted to the top of the file:

PlayD major: two sharps declared once, not eight times

Note that the two sharps are still being played, they are just not written on each note. This is also why sheet music tells you the key before you have played anything, and why musicians talk about a piece being "in" a key. The key is in the header, not the body.

Durations are powers of two. A whole note, a half note, a quarter, an eighth, a sixteenth. Each one is half the last, and the notation encodes the exponent visually: an empty notehead, then a stem, then a flag per halving. It is a unary encoding of a binary exponent, which is a very medieval way to store a number and impossible to misread at a glance:

PlayOne whole note, two halves, four quarters, eight eighths - all the same total length

Powers of two get you a long way but not everywhere, so there is one more operator: a dot after a notehead multiplies its length by 1.5. Two dots multiply by 1.75. It is a binary fraction, written as punctuation.

None of these durations are times, though. They are *beats*, and beats become seconds only when you fix a tempo:

Beats are not seconds until you say so

```
const midiToFreq = (n) => 440 * 2 ** ((n - 69) / 12);



const bpm = 120;



const beat = 60 / bpm;



// [midi note, length in beats]



const melody = [



[60, 1],



[62, 1],



[64, 2],



[65, 0.5],



[67, 0.5],



[69, 3],



];



let when = 0;



melody.forEach(([n, beats]) => {



note(midiToFreq(n), when, beats * beat * 0.95);



when += beats * beat;



});



console.log("total:", when.toFixed(2), "seconds at", bpm, "bpm");
```

Run

Change `bpm` to 200 and the same array is the same tune, faster. That split is what makes a score portable. It stores relative durations, and the performer supplies the clock.

The time signature groups the beats. 4/4 means four quarter-note beats per bar, 3/4 means three, and the vertical bar lines are there so your eye can find its place on a page. It is mostly a readability feature, but it also carries a real musical claim, which is that the first beat of each group is the strong one. Play the same six notes grouped in threes and grouped in twos and they become different pieces of music.

That is more or less all there is to it. Pitch on a diatonic axis with an origin and an escape hatch, duration as negative powers of two, and a couple of header fields. Everything else on a page of sheet music is performance instructions layered on top: how loud, how smoothly, which finger.

Putting it together
-------------------

Here is everything above in one place. A key, its diatonic chords, a progression, those chords broken into an arpeggio one note at a time, and a melody that sticks to the scale. About forty lines, no library, and it is the first thing I made with code that I would describe as music rather than as a demonstration:

A key, a progression, and a tune

```
const midiToFreq = (n) => 440 * 2 ** ((n - 69) / 12);



const build = (root, p) =>



p.reduce((n, s) => [...n, n.at(-1) + s], [root]);



const key = 57; // A



const scale = build(key, [2, 1, 2, 2, 1, 2, 2]).slice(0, 7); // natural minor



const bpm = 104;



const beat = 60 / bpm;



const chord = (degree) =>



[0, 2, 4].map((step) => {



const i = degree - 1 + step;



return scale[i % 7] + Math.floor(i / 7) * 12;



});



const progression = [1, 6, 3, 7];



const melody = [0, 2, 4, 2, 3, 2, 1, 0, 4, 3, 2, 1, 0, 2, 1, 0];



progression.forEach((degree, bar) => {



const at = bar * 4 * beat;



const notes = chord(degree);



// Bass note on the downbeat.



note(midiToFreq(notes[0] - 12), at, beat * 3.6, "triangle");



// Arpeggio: up, down, up, across the bar.



[0, 1, 2, 1, 0, 1, 2, 1].forEach((which, i) => {



note(midiToFreq(notes[which]), at + i * beat * 0.5, beat * 0.45);



});



// Melody, four notes per bar, always from the scale.



melody.slice(bar * 4, bar * 4 + 4).forEach((step, i) => {



note(



midiToFreq(scale[step % 7] + 12),



at + i * beat,



beat * 0.9,



"triangle",



);



});



});
```

Run

Every number in there means something we derived. `57` is A because of the twelfth root of two and a tuning fork. `[2,1,2,2,1,2,2]` is the minor scale because it is the major scale rotated five places. `[0,2,4]` is a chord because harmonics overlap when notes are two scale degrees apart. `[1,6,3,7]` sounds like it goes somewhere because of where the tension sits.

Change the key to 60 and it moves. Change the scale pattern to `[2,2,1,2,2,2,1]` and the same tune turns cheerful. Change the melody array to anything at all and it will still fit, because it is indexing into the scale rather than choosing frequencies. That constraint is what all the theory above was for.

What I still do not understand
------------------------------

Quite a lot. This article covers pitch and almost nothing else, and pitch may be the easy half.

Rhythm I have barely touched, and everything I have read suggests it is deeper than it looks. Voice leading, which is the business of moving between chords by the smallest possible distance rather than jumping around, is where written music starts sounding good rather than merely correct, and I can state the rule without hearing why it works. Why a melody wants to land where it lands is still mostly opaque to me. And the whole thing above is one tradition's answer. Plenty of music divides the octave differently, or does not treat the octave as the unit at all, and none of it is wrong.

But I no longer feel like I am being asked to memorise trivia. Twelve notes is what you get when you try to reconcile powers of two with powers of three and settle for a rounding error. A scale is a subset of those notes with gaps uneven enough that you can tell where you are. A chord is a set of notes whose harmonics already overlap, a key is a way of naming chords relative to a starting note, and notation is an old and slightly lossy way of writing all of that down. Each of those was an engineering decision, made a long time ago, under constraints, and the reasons are still there if you go looking.

If you want to go further, the two things that made me start writing this were [Music Theory for Nerds](https://eev.ee/blog/2016/09/15/music-theory-for-nerds/) by Eevee, which is a great read, and [LightNote](https://www.lightnote.co/), which is the most beautiful thing on the internet about this subject. For the API side, MDN's [Web Audio](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API) documentation is unusually good.

Every example on this page is plain JavaScript with no dependencies, so all of it runs anywhere with a browser engine. If you want to keep pulling on the thread, [RunJS](https://runjs.app) is a desktop JavaScript playground that ships with the Web Audio API alongside Node and npm, so there is nothing to set up. Paste any of the snippets above into it, add `const ctx = new AudioContext()` and `const out = ctx.destination` at the top, and carry on from there.
