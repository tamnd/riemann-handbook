---
id: series-realization-of-published-alt
title: The local export condition from the field conditions, first renaming
kind: theorem
decl: GlobalTheory.T.series_realization_of_published_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ExportAtBundlesStatement
covers: 2152
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [export-at-bundles-alt](/entry/export-at-bundles-alt/). Its only user is [export-f-is-built-e-alt-alt](/entry/export-f-is-built-e-alt-alt/). The content is in [export-at-of-bundles-alt](/entry/export-at-of-bundles-alt/).

## Statement

**Theorem.** Assume the 22 named hypotheses from `Cheb` to `HeckeReadTie` (see [export-f-is-built-e-alt-alt](/entry/export-f-is-built-e-alt-alt/)). Let $D$ be a datum with a norm choice $n$ and theta data $x$, let $X$ be a real side for $D$, $Y$ a series side over $X$ for the Hecke form data of $x$, and $G$ a Galois side (`GalSideAlt`). Assume `FieldOk X`, `GalHodgeN` for $G$, `Conclusion5 D`, the tie `NChTie D n`, and the base tuple condition `BaseTup` at each twisted place. Then `ExportAt D n x`.

The statement is the same as that of [export-at-bundles-alt](/entry/export-at-bundles-alt/), which says what `ExportAt` means in its turn.

## Proof

The proof is the term `GlobalTheory.ExportClose0.exportAt_bundles_alt`. There is nothing else.

## In the Lean code

The theorem is at [ExportAtBundlesStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExportAtBundlesStatement.lean#L16). The proof is `first | exact @exportAt_bundles_alt | ...`. The two types are the same text, word for word.

The name does not describe the statement. The conclusion is the local export condition `ExportAt`, a statement about good twists and bases of theta series. No realization and no published result appears in it. The file name says "export at bundles", and no bundle appears either.

There is a version without "alt", `GlobalTheory.T.series_realization_of_published` in [SeriesRealizationOfPublishedStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/SeriesRealizationOfPublishedStatement.lean#L20). It has the Galois side `GalSide` and the condition `GalHodge` in place of `GalSideAlt` and `GalHodgeN`.
