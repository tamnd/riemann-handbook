---
id: has4-of-has3-of-s-ext-none
title: From level three to level four, with the trivial S-extension
kind: theorem
decl: GlobalTheory.Mem.SRe.UpS.has4_of_has3_of_sExt_none
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.LevelThreeToFour
covers: 2284
status: drafted
drafted_by: writer@claude
---
This theorem proves one step of the construction of a member: for all large contexts, each pinned column that has a point of level three also has a point of level four. Its user is the restatement [`has4_of_has3_of_lv3Mv`](/entry/has4-of-has3-of-lv3-mv/), which [`memberE_closing_alt_alt`](/entry/member-e-closing-alt-alt/) calls twice. This is in branch 1 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/), below the step [HypsAlt is nonempty](/step/nonempty-hyps/). Below this theorem are 2,284 declarations.

## Statement

The hypotheses are nine named statements. We have not unfolded them, except where we say so: `DSInfChar`, `HarishChandraFinite`, `CuspRapidDecay` (rapid decay of cusp forms, unfolded in the [chapter](/proof/unitary-hypotheses/)), `DiscreteSeriesUpqUnique`, `RowsFinDim`, `SiegelWeilUnitaryConvergent` (the copy in `HeckeCharacterZeroLocus.SiegelWeilU`: for each CM extension $E/F$ of number fields and each nondegenerate hermitian matrix $J$, a finite volume statement `FinVol` and a product formula `SiegelDensities`, not unfolded further), `DiscreteSeriesExist`, `FormalDegreeFormula₂` and `SiegelMassRatioCM`.

**Theorem.** Assume these nine statements. Let $h_L$ be a proof of `RecTExists` and let $p$ be parameters over $h_L$. Suppose that the S-extension of $p$ is `SExt.none`, and that the slots $p.s$ satisfy `LevelThreeCondition`. Then `StepW (pinAnd (Has3 p.s)) (Has4 p.s)`.

The objects:

- A point is a context $K$, a base $B$, a frame $f$, twist data $T$ and a column $w$. `Has3 s` at $w$ says that there is a stage $Z$ of $w$ with an element of `Lv3 s K w Z`. Level 3 data are a group condition, a cohomology datum, a set of places, a row table, a norm choice, theta data, values $\chi_T(j) = x^{2(j+1)}$ for a unit $x$ of order $g_k - 1$ modulo $g_k$, and elements of the R-slot and N-slot of $s$. `Lv4` adds column data at split primes, the condition `RealTied`, two equalities of scale constants, and an element of the S-slot.
- `pinAnd q` adds to $q$ that $w$ has a pin (`ColPin w`).
- `StepW q q'` says: for all large contexts $K$ (in the sense of `EvLgG`), for each $B$ and $f$ with the field condition `KPx`, and each $T$ that contains all forced primes, each column with $q$ has $q'$.
- `LevelThreeCondition s`: each level 3 point at $Z$ moves to a level 3 point at each new stage `upL Z S' N h`, and its row package moves with it.
- `SExt.none` is the constant family `PUnit`. So the S-slot asks only for an element of `SX`.

## Proof

The proof is one call to `pin_has3_to_has4_of_sat_new p hS hM` with five facts:

1. `SatNew`, from `satOfDiscreteSeries` and the first five hypotheses. It calls `exists_spectralObjects_over_replacedStages`, which we have not unfolded.
2. `RealOf`, from `realOf` with `DiscreteSeriesExist` and `FormalDegreeFormula₂`.
3. `PackEx`, from [`exists_sPack_integrable_alt`](/entry/exists-s-pack-integrable-alt/) with `SiegelWeilUnitaryConvergent` and `RowsFinDim`. This is the largest part.
4. `VolumeEqMass₂`, from `volumes_eq_masses_of_unfold` applied to `volumeRatio`, which uses `SiegelWeilUnitaryConvergent`.
5. `IdempotentRealFixed`, from `goodIdempotent_real_of_harishChandra_series`, with no hypothesis.

Inside `pin_has3_to_has4_of_sat_new`, the gap condition `GapHyp` holds for large contexts by `ev_gapHyp`. For a pinned column with a level 3 point, the lemma picks a new S-stage (`exists_sStage_true`) and moves the point by `LevelThreeCondition`. Then `exists_late_level_of_gap` takes an S-pack from fact 3, `RealTied` from fact 2, an equality $D^* = D^*_{\mathrm{std}}$ from fact 4, and fact 5. Fact 1 gives a new stage. `LevelThreeCondition` moves the point again, and `sat_col` gives the element of `SX`. The S-extension part is `PUnit.unit`. The rest is bookkeeping.

## In the Lean code

The theorem is in [LevelThreeToFour.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LevelThreeToFour.lean#L19). The lemmas it calls:

- `pin_has3_to_has4_of_sat_new` and `exists_late_level_of_gap` in [StepOf.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/StepOf.lean#L42).
- `satOfDiscreteSeries`, `realOf` and `goodIdempotent_real_of_harishChandra_series` in [IwasawaDecomposition/LevelThreeToFour.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/LevelThreeToFour.lean#L68).
- `volumes_eq_masses_of_unfold` and `volumeRatio`.

Odd points:

- The hypothesis `SiegelMassRatioCM` is bound to `_` and never used.
- `goodIdempotent_real_of_harishChandra_series` uses no Harish-Chandra hypothesis.
- An older copy, `stepW_has4` at [IwasawaDecomposition/LevelThreeToFour.lean#L160](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/LevelThreeToFour.lean#L160), also takes `BesselMapUniq` and a local Langlands hypothesis. This version does not need `BesselMapUniq`, because fact 3 gets it from a proof (see [the spectral setting](/entry/exists-spectral-data-gap-alt/)).
