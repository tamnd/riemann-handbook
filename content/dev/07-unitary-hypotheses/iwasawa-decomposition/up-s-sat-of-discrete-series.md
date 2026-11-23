---
id: up-s-sat-of-discrete-series
title: The new S-stage from five spectral hypotheses
kind: theorem
decl: GlobalTheory.Mem.SRe.UpS.satOfDiscreteSeries
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.LevelThreeToFour
covers: 360
status: drafted
drafted_by: writer@claude
---
This theorem proves `SatNew`, fact 1 of [the step from level three to level four](/entry/has4-of-has3-of-s-ext-none/). It only unpacks one hypothesis and passes everything to [`exists_spectralObjects_over_replacedStages`](/entry/exists-spectral-objects-over-replaced-stages/), a second name for [the S-stage theorem](/entry/sre-sat-of-discrete-series/). The content is there. Below it are 360 declarations.

## Statement

**Theorem.** Assume `DSInfChar`, `HarishChandraFinite`, `CuspRapidDecay`, `DiscreteSeriesUpqUnique` and `RowsFinDim`. Then `SatNew` holds.

`SatNew` says: for each late stage $a$, row package $p$, forms $F_0$ and S-pack $P$ over $F_0$, if the conditions on $a.D$ and $P$ of [the S-stage theorem](/entry/sre-sat-of-discrete-series/) hold and `RowHyp p` holds, then there is a new S-datum $Z_s$ such that for all divisor data $(N, h)$ and all forms $F_1$ on the restaged datum that agree with $F_0$ (`SameL`), the type `SAtL` of S-objects is nonempty.

`RowHyp p` is a conjunction of seven conditions on the real data $R$, face $F$ and map $e_E$ of $p$: the level character condition, `grp_levels`, `GrpPin`, `IsModels`, a range condition on $e_E$, the norm identity $\|e_E x\|^2 = n_P \|x\|^2$, and `DallTie`.

## Proof

The proof destructures `RowHyp p` into its seven parts and applies [`exists_spectralObjects_over_replacedStages`](/entry/exists-spectral-objects-over-replaced-stages/) to the five hypotheses, the fields of $p$ and all the conditions, in its order. There is no other step.

## In the Lean code

The theorem is in [LevelThreeToFour.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/LevelThreeToFour.lean#L68). `SatNew` is on line 60 and `RowHyp` on line 36 of the same file. The proof is a single term (lines 70 to 71).

The same name `satOfDiscreteSeries` is used for [the S-stage theorem](/entry/sre-sat-of-discrete-series/) in the parent namespace `GlobalTheory.Mem.SRe`.
