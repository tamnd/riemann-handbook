---
id: row-counts-of-ties-alt
title: The counting row from the label ties and Siegel-Weil
kind: theorem
decl: GlobalTheory.CountRow.row_counts_of_ties_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.RowCountsOfTies
covers: 2597
status: drafted
drafted_by: writer@claude
---
This theorem proves the counting row `CountsIrreducibilityConstants'` from the label row and the Siegel-Weil hypothesis. Its user is [`row_counts_of_labels_alt`](/entry/row-counts-of-labels-alt/), which puts it in the form `Lg1` for the field `c30` of the record `AllRowsAlt`. That record gives the fields `c30`, `cIc`, `hc30`, `hcI`, `h30` and `irrC` of [HypsAlt](/step/hyps-alt-def/), in branch 1 of [the unitary hypotheses node](/proof/unitary-hypotheses/). The constants come from [`count_constants_of_siegelWeil`](/entry/count-constants-of-siegel-weil/), which holds most of the size (2,065 of 2,597 declarations).

## Statement

The hypothesis `SiegelWeilUnitaryConvergent` says: let $E/F$ be a CM extension with complex conjugation $\sigma$, and let $J$ be a nondegenerate [[hermitian form|48P4A1CX85]] of size $M$ over $E$. Then the adelic group `HA` of $J$ has a fundamental domain for its rational points with finite Haar volume. I read `HA` as the adelic [[unitary group|0R9R0Y1HDK]] of $J$, but I did not unfold it. Also, for $2n < M$, a nondegenerate hermitian $T$ of size $n$ and a factorizable test function $\Phi$, the mean over the fundamental domain of the theta sum over the $X$ with Gram matrix $T$ is a product of local densities $g_\infty(T) \prod_v g_v(T)$. This has the shape of the Siegel-Weil formula for one Fourier coefficient (Weil, Acta Math. 113, 1965). I did not check the normalizations.

The label row is the [row](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/ValidForConstructedPointClassesEventuallyWorking.lean#L268) `Row Q Lk (AtAll ...)`: at each selected bundle point $D$ there are a Hida setting $X$, a good operator $G$ and a linear isometry $\iota$ with three ties `AutTie`, `RowDictTie` and `LabTie`.

`CountsIrreducibilityConstants' Q Lk` says: there are constants `c30` and $c_{Ic} > 0$, with $0 \le C$ and $2(\mathrm{CYL}+1) \le A$ for every family, and the row `Row Q Lk` holds for the conjunction of two [closed](/step/closed-def/) properties on the class `D3 3 𝒜`. The first is `CountAllPointsClass` with the constants. The second says that eventually each point has rows `A` with `LabelCountGoodInjective`, `AllJoinA` and `CountAllRows A (epsC cIc r f)`. I did not unfold these properties.

**Theorem.** Assume `SiegelWeilUnitaryConvergent`. For every slot $Q$ and linkage $L_k$, the label row implies `CountsIrreducibilityConstants' Q Lk`.

## Proof

1. `count_constants_of_siegelWeil` gives `c30`, the bounds on $C$ and $A$, and `CountAllPointsClass` for every family.
2. `irreducibilityRow_of_concreteAutomorphicData`, with `rowsFinDim_link`, gives $c_{Ic} > 0$ and a map $H$. For a class whose families have `TuSize`, $H$ turns the three ties into the second property.
3. Keep the property $E$ of the label row. For a selection $\sigma$, the first property holds by step 1. The second holds by $H$ on `D3 3 𝒜`, with `TuSize` read off the class and the ties read off the label row at the selected points.

## In the Lean code

The theorem is at [RowCountsOfTies.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowCountsOfTies.lean#L12). The hypothesis is defined at [SiegelWeilUnitaryConvergent.lean](lean:Formalism/UnipotentAdelicQuotients/SiegelWeilUnitaryConvergent.lean#L46), and the counting row at [CountsIrreducibilityConstants.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CountsIrreducibilityConstants.lean#L113). `irreducibilityRow_of_concreteAutomorphicData` is a renaming of `irr_row_closed`.

Some details:

- The first property holds for every family. It does not use the label row or $\sigma$.
- `count_constants_of_siegelWeil` also gives its own $c_{Ic}$ and the bound $c_{Ic} \le c$. The proof drops both and takes $c_{Ic}$ from step 2.
- The "eventually" in step 3 uses the threshold $x_0 = 0$ (line 21).
- [`count_constants_of_siegelWeil`](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/CountConstantsOfSiegelWeil.lean#L11) gives `CountAllPointsClass P` for every predicate `P`. I did not unfold `CountAllPointsClass`, so I cannot say how it uses `P`.
