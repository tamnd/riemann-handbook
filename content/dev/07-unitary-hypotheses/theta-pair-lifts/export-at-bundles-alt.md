---
id: export-at-bundles-alt
title: The local export condition from the field conditions
kind: theorem
decl: GlobalTheory.ExportClose0.exportAt_bundles_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ExportAtBundles
covers: 2151
status: drafted
drafted_by: writer@claude
---
This theorem proves the local export condition `ExportAt` from the field conditions `FieldOk` on a real side. It proves three conditions on the theta series and the Hecke lattices from named hypotheses, and then calls [export-at-of-bundles-alt](/entry/export-at-of-bundles-alt/), which has the content. Its only user is the renaming [series-realization-of-published-alt](/entry/series-realization-of-published-alt/).

## Statement

Assume 22 named hypotheses, which we have not unfolded: the 12 of Galois cohomology from `Cheb` to `GreenbergWiles`, then `RayCharacterArtin`, `CuspRapidDecay`, `ChebotarevDegreeOne`, `GlobalArtinReciprocity`, `ToricDenominator`, `SeriesRat`, `SerInt`, `HeckeInt`, `HeckeTransform` and `HeckeReadTie`.

Let $D$ be a datum (`D7`), $n$ a norm choice for $D$ and $x$ theta data for $D$, with Hecke form data $E = E(x)$ (`twEOf x`). Let $X$ be a real side for $D$ (`RealSide`), $Y$ a series side over $X$ for $E$ (`SerSide`), and $G$ a Galois side (`GalSideAlt`). Call a place $w$ *twisted* if $\mu_w \neq \mu_0$ (`TwistedAt`).

**Theorem.** Assume:

1. `FieldOk X`: among other fields, the field $L_0$ of $D$ is Galois over $\mathbb{Q}$, and it contains each $z \in \mathbb{C}$ with $z^{g_k(g_k - 1)} = 1$ for $k = 0, 1$;
2. `GalHodgeN D G.wd`;
3. `Conclusion5 D`;
4. `NChTie D n`, which ties $n$ to the twist data of $D$;
5. for each twisted place $w$, the base tuple condition `BaseTup Y` at the twist index of $w$.

Then `ExportAt D n x`, as stated in [export-at-of-bundles-alt](/entry/export-at-of-bundles-alt/).

## Proof

[export-at-of-bundles-alt](/entry/export-at-of-bundles-alt/) needs, in place of `FieldOk X`, five conditions. This proof supplies them.

1. `thetaSeries_rationality_and_coefficientBound` gives the rationality rows `RatRow` at each nonzero index place and the bound `XiBdd`. It uses `CuspRapidDecay`, `GlobalArtinReciprocity`, `SeriesRat`, `SerInt` and `FieldOk X`.
2. `heckeOperator_preserves_supLattice_realSide` gives `HkSupAt` for each $j$: by its name, Hecke operators preserve the sup lattice. It uses `CuspRapidDecay`, `HeckeInt`, `HeckeTransform` and `HeckeReadTie`.
3. The fields `galois` and `roots` of `FieldOk X` give the last two conditions.

The other hypotheses pass through unchanged.

## In the Lean code

The theorem is at [ExportAtBundles.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExportAtBundles.lean#L16). It calls:

- `GlobalTheory.T.realization_of_published_alt`;
- `GlobalTheory.T.thetaSeries_rationality_and_coefficientBound`, at [ThetaSeriesRationalityAndCoefficientBoundStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ThetaSeriesRationalityAndCoefficientBoundStatement.lean#L17);
- `GlobalTheory.T.heckeOperator_preserves_supLattice_realSide`, at [HeckeOperatorPreservesSupLatticeRealSideStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/HeckeOperatorPreservesSupLatticeRealSideStatement.lean#L17).

`FieldOk` is at [UnivChar.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/UnivChar.lean#L63).

The theorem is a copy of `GlobalTheory.ExportClose0.exportAt_bundles` in [SeriesRealizationOfPublished.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/SeriesRealizationOfPublished.lean#L23), with `GalSideAlt` and `GalHodgeN` in place of `GalSide` and `GalHodge`. The name says "bundles", but no bundle appears in the statement. The namespace of `HeckeInt` is `UnusedSlot39`, but the hypothesis is used here.
