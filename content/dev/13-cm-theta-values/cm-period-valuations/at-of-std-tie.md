---
id: at-of-std-tie
title: The kernel conditions at a standard tie
kind: theorem
decl: GlobalTheory.PdvTie.at_of_stdTie
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.KernelDatumConditionsAtStandardKernelComparison
covers: 2306
status: drafted
drafted_by: writer@claude
---
This theorem proves the kernel conditions `Pdv.At` for a tied kernel entry that has a standard tie. It only opens the tie and passes the data to [`at_of_true_columns`](/entry/at-of-true-columns/), which has the content. Its user is the renaming [`kernelDatumConditions_at_standardKernelComparison`](/entry/kernel-datum-conditions-at-standard-kernel-comparison/), and through it [`rowAt_of_stdTie`](/entry/row-at-of-std-tie/).

## Statement

The statement is the same as that of [`kernelDatumConditions_at_standardKernelComparison`](/entry/kernel-datum-conditions-at-standard-kernel-comparison/): from the four hypotheses `AlgTAll`, `GenusOneModelExistsLattice`, `CurveDict`, `IntInert`, a standard tie `StdTie D O t`, the three size bounds and the shape condition on every entry, it concludes `Pdv.At O.ex t.ent`.

`StdTie D O t` ([HasPartAnd.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/HasPartAnd.lean#L28)) says that the triple $(D, O, t)$ equals $(I.\mathrm{rec7}(l, Z), O', t')$ for a true-columns datum $I$ (`TC B X`) and data $l, l_0, Z, O', t'$ with `StdAt`. The record `StdAt` collects nine facts: `I.Ok`, the pins, `I.IsTw`, the jets `JetsIn`, the twist identity $O'.\mathrm{tw} = I.\mathrm{tw}(l, l_0, Z)$, `I.StdKer l Z t'`, `IsEntC t'`, `t'.Adapted` and `t'.TopPinned`. We have not unfolded these.

## Proof

`StdTie.ind` reduces to the case where $(D, O, t)$ is the triple of a true-columns datum. `colNorm_of_tw` turns `I.IsTw` into `ColNorm I`. Then `at_of_true_columns` applies, with the other fields of `StdAt` and the remaining hypotheses passed along.

## In the Lean code

The theorem is at [KernelDatumConditionsAtStandardKernelComparison.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/KernelDatumConditionsAtStandardKernelComparison.lean#L13). The lemmas it calls: `StdTie.ind` in the same file as `StdTie`, `GlobalTheory.Pdv.colNorm_of_tw` in [StepRepEqOneAtTypePrimes.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/StepRepEqOneAtTypePrimes.lean#L38), and `at_of_true_columns`. The proof only passes hypotheses along.
