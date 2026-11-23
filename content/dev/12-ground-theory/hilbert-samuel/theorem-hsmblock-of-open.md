---
id: theorem-hsmblock-of-open
title: The block Hilbert-Samuel formula from nineteen inputs
kind: theorem
decl: GroundTheory.Heights₂.Heights.HilbertSamuel.TheoremHSMBlock.of_open
module: GroundTheory.HeightsAndTheta.Heights.HilbertSamuel.AssemblyConditional
covers: 1239
status: drafted
drafted_by: writer@claude
---
This theorem proves the arithmetic Hilbert-Samuel formula on one block, with its sup bound, from 19 statements that it takes as hypotheses. It is an assembly: it only puts proved reduction lemmas together and passes the hypotheses to them. Its one caller is [the block formula](/entry/theorem-hsmblock/), which proves the 19 statements and holds the mathematical content. Below this theorem are 1,239 declarations of the proof.

## Statement

The objects (a block datum $d$, the arithmetic Euler characteristic $\widehat\chi(n)$ from the $L^2$ Gram determinant, the $L^2$ norm $\|f\|$) are defined in [the block formula](/entry/theorem-hsmblock/).

**Theorem.** Assume the 19 statements below. Let $I$ be an intersection family that satisfies the axioms `AllFam.IsFamily`. Then for each block datum $d$ of dimension $D+1$ with Hermitian line $\overline{A}$:

$$\widehat\chi(n) = I(\overline{A}^{D+1}) \frac{n^{D+1}}{(D+1)!} + o(n^{D+1}),$$

and there is $C$ with $|f(z)|/h(z)^n \leq C\, n^{D/2} \|f\|$ for all $n \geq 1$, all forms $f$ of degree $n$ on the block $k_0$ and all complex points $z$.

The hypotheses are statements named `X.Statement`, in five groups by name. We have not unfolded them.

- Two-block pieces: `TwoBlockPieceIndex`, `TwoBlockModuleFinite`, `ModulePieceHilbert`, `TwoBlockModuleCycle`.
- Coordinates and models: `PFCoordStatement`, `ChangeOfModelStatement`, `ProjFrameGraphDeg`, `HSMTransport`.
- Resolutions: `ResolutionDegree`, `ResolutionMixedBridge`.
- Block resolutions: `BlockResolutionImageSup`, `BlockResolutionDegreeIntegral`, `BlockResolutionMixedBridge`, `PtsAbsIntegrable`, `BlockImageInverse`.
- Graphs and the Veronese map: `GraphChangeOfModel`, `BlockGraphDeg`, `VeroneseGramMono`, `VeroneseGraphDeg`.

## Proof

The proof is one term. It applies `TheoremHSMBlock.proof` to three statements, as in [the block formula](/entry/theorem-hsmblock/):

1. `ReductionToProjectiveBlock.proof` gives the reduction to $\mathbb{P}^D$. Its inputs are `ReductionToProjective.proof` (from hypotheses 0 to 9), `BlockMetricChange.proof` (from hypotheses 10 to 13), `BlockImageDatum.proof` (from hypothesis 14), `BlockImageTop.proof` (from hypotheses 15 and 16) and `BlockImageGenDeg.full`.
2. `HilbertSamuelProjective.proof` gives the formula for $\mathbb{P}^D$ with the Fubini-Study metric. Its inputs are `ReductionToProjective.proof` again, `SecondVeronese.proof` (from hypotheses 15, 17 and 18) and `PointHeightFS.full`.
3. `SupBoundBlock.full` gives the sup bound. It uses no hypothesis.

Each lemma named `X.full` is a theorem with no hypothesis, proved in `AssemblyBase.lean` or `Assembly.lean`. The rest is bookkeeping.

## In the Lean code

The theorem is in [AssemblyConditional.lean](lean:GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/AssemblyConditional.lean#L124). The conclusion `TheoremHSMBlock.Statement` is in [StatementsArith.lean](lean:GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/StatementsArith.lean#L273). The three-part combination is [PTheoremHSMBlock.lean](lean:GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/PTheoremHSMBlock.lean#L13).

- The word "open" in the name says only that the inputs are hypotheses here. The caller fills all 19 of them. Two of them it fills with theorems with no hypotheses, `ResolutionMixedBridge.full` and `BlockResolutionMixedBridge.full`, from `AssemblyBridge.lean`. This file does not import `AssemblyBridge.lean`.
- The term for `ReductionToProjective.proof` is written out twice, word for word (lines 147 to 161 and 174 to 188).
- Hypothesis 15 (`GraphChangeOfModel`) is used twice: in `BlockImageTop.proof` and in `VeroneseTop.proof`.
- The second half of the conclusion, the sup bound, does not depend on any of the 19 hypotheses.
- The same file proves `TheoremHSM.of_open` (line 72), the version for a datum `HSMDatum` with one block of coordinates, with 13 of the same hypotheses.
