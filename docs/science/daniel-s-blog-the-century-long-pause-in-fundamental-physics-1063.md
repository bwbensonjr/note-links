---
id: 1063
url: https://danieltan.weblog.lol/2026/05/the-century-long-pause-in-fundamental-physics
title: Daniel's Blog · The Century-Long Pause in Fundamental Physics
domain: danieltan.weblog.lol
source_date: '2026-05-02'
tags:
- physics
- academic-paper
summary: The article argues that fundamental physics has been stalled for a century
  because it has mastered extending mathematical models faster than renewing the underlying
  physical theories that explain reality. The author distinguishes between quantum
  mechanics as a mathematical calculus (which explains why interpretations debates
  remain unresolved) and as a physical theory with genuine ontology, suggesting the
  field's foundational problems stem from treating computational formalisms as fundamental
  rather than the physical structures they describe. All major confirmations in the
  last fifty years have merely reinforced ontological commitments made before 1973,
  while every beyond-standard-model proposal using mathematical-model methodology
  has failed to produce confirmed predictions.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Daniel's Blog · The Century-Long Pause in Fundamental Physics

The Century-Long Pause in Fundamental Physics
=============================================

Most readers first encountered quantum mechanics through its interpretations debate: Copenhagen, Everett, Bohm, hidden variables, many-worlds. The debate is painted as one of physics's deepest unresolved puzzles. After 95 years the field cannot resolve which interpretation is correct, and there is no possibility of empirical resolution because all interpretations make the same predictions. The puzzle is much smaller once you separate two questions about it: a mathematical model reproduces measurements, while a physical theory says what in the world makes them come out that way. If QM were a physical theory, the persistence of the disagreement would be intolerable. If QM is a mathematical model (a probability calculus on a wave-mechanical system), the situation is unremarkable. Einstein's "God does not play dice" was a complaint of exactly this shape: not that the calculus failed, but that a probability calculus was being treated as physical theory when it described measurements rather than what was being measured. The persistence of the disagreement is itself evidence of which kind of object QM is in the field's working posture.

The two postures look identical when both reproduce the same data. They diverge when you ask what changes if the data is reproduced equally well by an alternative formalism. For a mathematical model, nothing changes; pick whichever is computationally easier. For a physical theory, that is a serious problem requiring resolution, because two different ontologies cannot both be how the world actually is.

The interpretations problem is the visible symptom of a broader pattern. Since 1928, fundamental physics has confirmed a large catalogue of particles and interactions, but the underlying ontology has not changed: spacetime as fixed by general relativity (1915), and relativistic matter as a wave-like spinor field on that spacetime fixed by the Dirac equation (1928). Everything since (QED, the Standard Model, GUTs, SUSY, string theory, LQG, twistor theory, SMEFT) added gauge fields, scalar fields, and other content inside that ontology. No widely accepted, empirically confirmed new ontology has displaced it in the intervening century. Later confirmations, including the Higgs and CKM mixing, added structure inside the inherited ontology rather than replacing it. The question is whether today's impasses (the QM-GR junction, the gauge group, the generation count, the hypercharges, the measurement problem, the cosmological constant) share a cause: physics learned to extend successful calculational formalisms faster than it learned to renew their ontology.

The diagnosis matches the empirical record. The confirmed predictions of the last fifty years (W/Z masses 1983, top quark 1995, Higgs 2012, gravitational waves detected 2015 and announced 2016) all confirm ontological commitments made before 1973. Every BSM extension proposed under mathematical-model methodology has produced no confirmed predictions in fifty years. The persistent foundational problems are visible as artifacts of the methodology rather than features of nature. Senior figures (Smolin, Woit, Hossenfelder, Penrose) have been writing books about the stagnation for over a decade. The diagnosis here is sharper than theirs: the stagnation is not "the easy problems were solved and the hard ones are intrinsically harder." The stagnation is the methodology that produced the empirical successes hitting its structural limit.

What the quantum revolution actually discovered
-----------------------------------------------

The quantum revolution between 1900 and 1928 produced a specific catalogue of ontological discoveries:

* Light is wave-like in propagation but exchanges energy in discrete chunks E = ℏω (Planck 1900, Einstein 1905).
* Matter is wave-like in propagation, with λ = h/p (de Broglie 1924, Davisson-Germer 1927).
* Atomic states are stationary and discrete (Bohr 1913).
* Spin is half-integer angular momentum carried by matter (Stern-Gerlach 1922, Uhlenbeck-Goudsmit 1925).
* Identical particles obey symmetric or antisymmetric statistics (Pauli 1925, Bose 1924).
* Matter is a four-component spinor field on Minkowski space, and antimatter exists (Dirac 1928, confirmed by Anderson 1932).

By the early 1930s, the core catalogue is in place. The catalogue commits to specific physical structure: matter is wave-like, atoms have discrete states, particles have intrinsic angular momentum and specific statistics, matter waves have spinor structure that forces antimatter.

Matrix mechanics organized transitions among stationary states; wave mechanics gave the evolution equation; transformation theory showed the two calculi were equivalent. The unification was mathematical achievement, not physical discovery. The Dirac equation made an ontological commitment to four-component spinor structure. The Hilbert-space formalism that surrounds it is a mathematical model: a calculus any wave-mechanical system would satisfy.

This decomposition is the fact most often blurred when QM is presented. Textbook QM presents Hilbert space as fundamental and the wave/spin/statistics structure as represented in it. The historical and structural ordering is the reverse: the wave/spin/statistics structure is the physical content discovered between 1900 and 1928, and the Hilbert space is the natural mathematical language for a wave-mechanical system with discrete states and probabilistic measurement outcomes.

The reconstruction theorems of the 2000s (Hardy 2001, Masanes-Müller 2011, Chiribella-D'Ariano-Perinotti 2011) made this formal: QM follows from a small set of operational axioms about probability and measurement. Those reconstructions can be read two ways. The standard reading inside quantum foundations is that QM is natural given operational principles. The reading used here is narrower: operational axioms recover the calculus, but they do not by themselves supply an ontology, so the wave/spin/statistics content has to come from outside.

The measurement problem is then exactly what the framing predicts: an artifact of treating the calculus as fundamental and the field equation as derived. Reverse the order, with the field equation fundamental and the calculus derived as the statistical behavior of the field, and the measurement problem reduces to a specific question about how continuous evolution produces single outcomes. Real, but bounded, not the open-ended Copenhagen-vs-Everett-vs-Bohm interpretive sprawl of the last 95 years.

The same reframing applies to the Standard Model. The SM is wave-mechanics applied to a catalog of internal labels (color, weak isospin, hypercharge, generation index). The cataloging is empirical. The formalism is the standard wave-mechanics-plus-probability machinery. There is no new ontological move in the SM beyond "wave-like matter has internal structure that can be cataloged." That is why "why does the SM have this gauge group?" has been an open structural problem for fifty years, with no SM-internal answer: SM methodology is mathematical-model methodology, which does not ask the question.

The ML analogy
--------------

The same distinction is currently live in machine learning. The dispute is whether large neural networks build internal models of the world or are sophisticated function approximators that fit the statistics of training data without any commitment to what generates them. Yann LeCun has argued for years that current LLMs are autoregressive predictors that learn surface statistics of language without internalizing how the world works, and that genuine intelligence requires architectures predicting physical futures from internal world models, not token futures from text. Karpathy, Chollet, Marcus, and Mitchell have argued versions of the same point: these systems pattern-match at scale, and whether that pattern-matching constitutes understanding is contested. The opposing camp argues that with enough parameters and the right training, structure that looks like understanding emerges; mechanistic interpretability is the open empirical front on which that question is being adjudicated.

The dispute is exactly the math-model-vs-physical-theory dispute, with "function approximator" playing the role of mathematical model and "system with an internal world model" playing the role of physical theory. Both sides agree the distinction matters. A system that fits the training data without representing the structure that generates it has predictable failure modes: adversarial fragility, out-of-distribution collapse, hallucination, no principled reason to be right outside the cases it has seen. Physics had the same argument in the 1920s. It settled in 1932 by quietly conflating the calculus with the theory, and the question of whether the calculus refers to anything got handed off to the philosophers. The ML field has not settled its version of the question yet, which is why the debate is still legible there and almost invisible in physics.

A neural network trained on a dataset is a function approximator. Given inputs, it produces outputs that match observed values to some accuracy. The internal structure (weights, activations) is constrained only by the requirement that the function reproduce the data. The model has no commitment to what generates the data. A different architecture trained on the same data might fit equally well, with completely different internal representations. The choice between them is purely pragmatic.

Heisenberg's matrix mechanics in its original construction was structurally identical. Heisenberg renounced visualizable atomic models and replaced them with a calculus on observables. The matrix elements ⟨n|X|m⟩ are direct analogues of an ML model's outputs: they reproduce observed transition frequencies and intensities, but they do not tell you what is happening between states. The commutation relation [X, P] = iℏ is a structural constraint on the calculus, not a statement about physical reality.

The analogy matters because fitted representations can predict without referring. Adversarial examples make the failure mode visible: tiny imperceptible perturbations to an input flip the classification, revealing that the network was responding to texture statistics that correlate with cats in the training distribution but do not refer to anything cat-shaped about the world. The same critique applies to Heisenberg's matrices treated ontologically. If you ask what X(t) refers to physically, the honest answer in matrix mechanics is that it refers to a column of numbers in a calculation that produces correct predictions. Position only manifests in measurements; between measurements the matrix does not represent anything physical. The matrix has the same ontological status as a hidden layer activation: instrumentally useful, semantically empty.

Fitting the data also does not constrain extrapolation past the training distribution. A model that achieves 100% accuracy on its training set has no principled basis for predicting anything outside that distribution. Out-of-distribution failure is generic, not exceptional, because the model has no theory of what it is modeling.

A physical theory makes a stronger claim. The structure that fits the existing data also forces what happens in untested regimes, because the structure refers to physical reality. GR predicts gravitational waves before they are detected because the metric is real. Dirac predicts antimatter before it is discovered because spinor structure is real. The empirical confirmations are not fits. They are consequences of ontological commitments.

The universal approximation theorem says a sufficiently wide neural network can represent any continuous function. This is the strength of ML models as fitters and the limit of them as theories: universal approximation means the model has zero distinctive content. Any data could be fit by a sufficiently large model; therefore fitting the data is not evidence of underlying structure.

QM as a mathematical model has a weaker version of the same property. The Hilbert-space/POVM machinery is highly expressive: given measurement statistics on a known operator algebra, you can usually find a Hilbert space, a state, and operators that reproduce them. The expressiveness has a hard limit. No-signaling alone does not pin quantum correlations down: the PR-box correlations of Popescu-Rohrlich (1994) are non-signaling but supraquantum, so quantum statistics occupy a stricter subset of the broader probability-theoretic landscape. Quantum-NLP makes the portability concrete from the other direction: the same Hilbert-space and tensor-product machinery used to describe particle states has been used to model compositional language meaning (Coecke and Sadrzadeh's DisCoCat), with implementations on quantum hardware. The machinery handles linguistic meaning as readily as physical observables, which is what you would expect of a mathematical model and not of a physical theory. The reconstruction theorems above sharpen this: operational axioms beyond no-signaling are what carve out the quantum subset.

The qualifier matters. QM as taught is more like an ML model that has been heavily structurally regularized using physical priors (continuous symmetries forcing momentum, rotational invariance forcing angular momentum, special relativity forcing Dirac structure, unitary evolution forcing conservation laws) than an ML model with arbitrary architecture. The structural constraints leak ontological content into the formalism even when practitioners disavow ontological commitment. But the working posture remains mathematical-model, and the field treats the formalism as the fundamental object that the wave/spin/statistics structure is "represented in," rather than the reverse.

SMEFT is the cleanest contemporary example of the inverse posture made explicit. The Warsaw basis catalogues 59 baryon-number-conserving dimension-six operators before flavor; with three-generation flavor structure, common counts give 2499 independent real Wilson-coefficient degrees of freedom. Any UV physics you discover gets absorbed by setting the coefficients appropriately. SMEFT is not designed to pick a unique UV completion; it can only accommodate one. That is honest mathematical-model posture, and it is also where the methodology terminates: an explicit measurement framework with no ontological commitment whatsoever.

What hasn't happened in 98 years
--------------------------------

Measure progress by ontological commitments confirmed empirically as physical structure. The count after 1928 is approximately zero independent commitments. Each confirmed prediction since is a consequence of an earlier ontological move:

* W/Z masses (1983) confirmed Weinberg-Salam (1967), which committed ontologically to gauge symmetry breaking by a scalar.
* Top quark (1995) confirmed CKM (1973), which committed ontologically to a third generation.
* Higgs (2012) confirmed BEH (1964), which committed ontologically to a Higgs scalar acquiring a vacuum expectation value.
* Gravitational waves (detected 2015, announced 2016) confirmed GR (1915).

Each is a confirmation of physical-theory commitment. The commitments date from periods when ontology-first methodology was still partially operative, between 1915 and 1973. The SM's own subsequent extensions (GUTs, SUSY, technicolor, string theory's specific compactifications) have produced no confirmed predictions in fifty years.

The persistent failures of the major BSM programs are structurally consistent with mathematical-model methodology hitting its limits. SUSY's failure to appear at the LHC, string theory's often-quoted order-of-magnitude landscape estimate of around 10⁵⁰⁰ flux vacua, LQG's classical-limit problem, twistor theory's googly problem are each the kind of structural impasse you would expect from running expressive mathematical formalisms without ontological commitment. The formalisms are too flexible to be falsified and not constrained enough to predict.

The diagnosis
-------------

Physics, as a discipline, has been collecting astronomical amounts of empirical data and producing increasingly elaborate mathematical formalisms to fit them, while the substantive ontological work has been deferred for nearly a century. The field's prestige rests on the empirical successes, which are real. The intellectual stagnation in fundamental physics, also real and widely admitted, is the structural consequence of the methodological inversion that produced the empirical successes in the first place.

The same methodology that gave us the SM is the methodology that has prevented us from understanding why the SM has the structure it does.

The empirical achievements are real. The formalism is useful. The empirical catalogue, the precision tests, and the confirmations are all genuine. The claim is that the bookkeeping has not been a substitute for the missing ontological work, and that the field's current impasse (no fundamental progress on QM measurement, on the QM-GR junction, on gauge group origin, on generations, on hierarchies) is the structural consequence of the substitution. The work that was deferred between 1925 and 1932 is the work that still needs to be done now.

The bet
-------

Physics took the Copenhagen deal in 1932 and the deal has held for 95 years. The deal was that mathematical-model success can substitute for ontological commitment. The substitution worked extraordinarily well for half a century and has been failing for the last forty years. The field is asking why nothing has worked since 1973. The diagnosis offers an answer: nothing structurally new can happen inside mathematical-model methodology, because mathematical-model methodology is what produced the impasse in the first place. Resuming pre-inversion methodology (Einstein's order, Dirac's order, ontology-first) is the only path forward that does not recapitulate the failures of the last fifty years.

The claim is stronger than "we should be more careful about interpretation" and weaker than "everything since 1928 is wrong." The form of progress was correct through 1928. The form of progress that replaced it has reached its limit. The methodology that was load-bearing in 1915 and 1928 is the one that remains load-bearing now.

The field did not go wrong because the formalism was useless. It went wrong if the formalism became protected from ontological revision. After a century, the test is no longer taste; it is whether the method can generate commitments that survive contact with experiment. The work that was deferred in 1932 is still waiting.

---

*If the diagnosis lands and you want to see a recent attempt to resume the methodology with worked structural derivations of the Standard Model, see [Wave Relativity](https://doi.org/10.5281/zenodo.19663818) (Tan, 2026, CC BY-NC 4.0).*
