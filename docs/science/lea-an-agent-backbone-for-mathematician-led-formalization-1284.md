---
id: 1284
url: https://vida-nyu.github.io/Lea/
title: Lea — An agent backbone for mathematician-led formalization.
domain: vida-nyu.github.io
source_date: '2026-08-17'
tags:
- mathematics
- ai
- academic-paper
summary: Lea is an agent-based system that helps mathematicians formalize proofs in
  the Lean programming language by allowing users to state theorems in natural language
  and automatically generating corresponding Lean code. The system provides an interactive
  interface where mathematicians can guide the proof development step-by-step, with
  the ability to edit, refine, or backtrack through previous versions. The example
  demonstrates Lea proving that the sum of √2 and √3 is irrational through an automated
  formalization process integrated into a web-based environment.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Lea — An agent backbone for mathematician-led formalization.

LeaChat · proof canvas

LLea

✓Done — Proof complete

`irrational_sqrt_two_add_sqrt_three` is proved and compiles cleanly in
`Lea/Misc/SqrtIrrational.lean`.

How the proof works

√6 is irrational by `norm_num`; squaring `q = √2 + √3` gives
`q² = 5 + 2√6`, so √6 would be rational — contradiction.

SqrtIrrational.leanstep 5 of 5

```
import Mathlib
open Real

namespace Lea.Misc

/-- √6 is irrational: 6 is not a square. -/
lemma sqrt_six_irrational :
    Irrational (Real.sqrt 6) := by
  norm_num

/-- The sum √2 + √3 is irrational. -/
theorem irrational_sqrt_two_add_sqrt_three :
    Irrational (Real.sqrt 2 + Real.sqrt 3) := by
  rintro ⟨q, hq⟩
  have h_sq : (q : ℝ) ^ 2 = 5 + 2 * Real.sqrt 6
```

✓ lean\_check: 0 errors
Run SafeVerify

### Prove it in the browser

State a theorem in natural language and watch the Lean file take shape beside the transcript. Every step is a version you can walk back through, edit by hand, or hand back.
