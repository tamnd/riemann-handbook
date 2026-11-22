---
id: realization-of-published-alt
title: The local export condition from rational rows, first renaming
kind: theorem
decl: GlobalTheory.T.realization_of_published_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ExportAtOfBundlesStatement
covers: 2150
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [export-at-of-bundles-alt](/entry/export-at-of-bundles-alt/), which has the content. Its only user is [export-at-bundles-alt](/entry/export-at-bundles-alt/).

## Statement

**Theorem.** Assume the 17 named hypotheses from `Cheb` to `ToricDenominator` (see [export-f-is-built-e-alt-alt](/entry/export-f-is-built-e-alt-alt/)). Let $D$, $n$, $x$, $X$, $Y$ and $G$ be as in [export-at-bundles-alt](/entry/export-at-bundles-alt/). Assume:

1. the rationality rows `RatRow` at each nonzero index place, the bound `XiBdd`, and `HkSupAt` for each $j$;
2. `GalHodgeN D G.wd` and `Conclusion5 D`;
3. $L_0$ is Galois over $\mathbb{Q}$ and contains each $z \in \mathbb{C}$ with $z^{g_k(g_k - 1)} = 1$ for $k = 0, 1$;
4. `NChTie D n`, and `BaseTup Y` at the twist index of each twisted place.

Then `ExportAt D n x`.

## Proof

The proof is the term `GlobalTheory.ExportClose.exportAt_of_bundles_alt`. There is nothing else.

## In the Lean code

The theorem is at [ExportAtOfBundlesStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExportAtOfBundlesStatement.lean#L16). The proof is `first | exact @exportAt_of_bundles_alt | ...`, and the two types are the same text, word for word.

The name does not describe the statement: no realization and no published result appears in it. The version without "alt", `GlobalTheory.T.realization_of_published` in [RealizationOfPublishedStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/RealizationOfPublishedStatement.lean#L20), has `GalSide` and `GalHodge` in place of `GalSideAlt` and `GalHodgeN`.
