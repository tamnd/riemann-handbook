---
id: amplitude-bound-at-terms-of-local-data
title: The amplitude bound from local data and a tail bound, statement form
kind: theorem
decl: GlobalTheory.T.amplitudeBound_at_terms_of_localData
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.AmplitudeBoundAtTermsOfLocalDataStatement
covers: 912
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [`amplitudeBound_of_localData_of_tailBound`](/entry/amplitude-bound-of-local-data-of-tail-bound/). Its only user is [`typeBound_of_gap`](/entry/type-bound-of-gap/), in step 1 of its proof, where it gives the amplitude bound `AmpP`. The content is in [`amplitudeBound_of_localData_of_tailBound`](/entry/amplitude-bound-of-local-data-of-tail-bound/).

## Statement

**Theorem.** $\mathrm{LocDatC} \wedge \mathrm{TailP} \implies \mathrm{AmpP}$.

The three statements:

- `LocDatC`: for each datum $D$ and Hida setting $X$ with a word, under `GapHyp D` and `dsigTie D`, there is a choice of local data $C$ at the real places, with a Bessel datum, that satisfies `GoodLoc`.
- `TailP`: for constants with $c_b, c_T > 0$ there is $C_H \geq 0$ such that, for each $C_1 \in \mathbb{N}$ and large $C', C_l$, each datum with `Ties`, `KTwoHypotheses` and a lower bound on `Tr` has `TailAt`: good local data at each real place satisfy the tail bound `TailBd` with parameters $C_1 k r$ and $b^{C_H m}$.
- `AmpP`: the amplitude bound of [`typeBound_of_gap`](/entry/type-bound-of-gap/), $\lVert v(t) \rVert \leq w(t) \sqrt{d_\pi}\, \omega(t)\, a(j(t), \delta(t))$ for each relevant term $t$. The constants come in this order: $C_H \geq 0$; for each $C_s \geq 0$ a threshold $C_0 \geq 0$; for each $C \geq C_0$ thresholds for $C'$ and $C_l$. The data must satisfy `Ties`, `KTwoHypotheses` and `ConcTie`.

We have not unfolded `GoodLoc`, `TailBd` or `KTwoHypotheses`.

## Proof

The proof is the term `GlobalTheory.TypeAsm.AmpTerms.amplitudeBound_of_localData_of_tailBound`. There is nothing else.

## In the Lean code

The theorem is in [AmplitudeBoundAtTermsOfLocalDataStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/AmplitudeBoundAtTermsOfLocalDataStatement.lean#L6). The proof is the usual `first | exact … | …` tactic; the first alternative fits. `LocDatC` is in [GoodLoc.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/GoodLoc.lean#L37), `TailP` in [MomAllP.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/MomAllP.lean#L18), and `AmpP` in [PerRowC.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/PerRowC.lean#L36). The file imports `Mathlib` twice.
