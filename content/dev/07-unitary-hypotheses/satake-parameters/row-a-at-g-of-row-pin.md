---
id: row-a-at-g-of-row-pin
title: The arithmetic row at bundle points, from pinned rows and the split jet bound
kind: theorem
decl: GlobalTheory.AtG.row_aAtG_of_rowPin
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.ConstructionAtBundlePointsOfTrueColumns
covers: 572
status: drafted
drafted_by: writer@claude
---
This theorem proves the row `aAtG` at the points of a slot whose rows are pinned. It is used through its second name [`holds_at_bundlePoints_of_trueColumns`](/entry/holds-at-bundle-points-of-true-columns/), and from there by [`row_aAtG_at_built_alt`](/entry/row-a-at-g-at-built-alt/). The proof passes one proved input, the jet bound at split primes, to a lemma that has it as a hypothesis. The analytic content is in [`jetTableBound_splitPrime`](/entry/jet-table-bound-split-prime/) (319 of the 572 declarations below this theorem); the rest is in `row_atG_pinned` and the lemmas that it calls.

## Statement

The statement is the one of [`holds_at_bundlePoints_of_trueColumns`](/entry/holds-at-bundle-points-of-true-columns/). Let $Q$ be a slot and $L_k$ a linkage of bundles. If each point of $Q$ has a part at which `RowPin` holds for each tuple, then `ArithmeticConditionAtBundlePoints Q Lk`, the row of `H_aAtG` on the families of $Q$.

## Proof

The proof term is `atGRows_bundlePoints_of_jetSplitAmbient jetTableBound_splitPrime`. The first lemma is a second name for `row_atG_pinned`, which has the extra hypothesis `JetSplitAmb`; the second proves `JetSplitAmb`. `row_atG_pinned` works in two steps.

1. **Ties from pinned rows.** For each slot point $\beta$ and each tuple $\mu$, `concreteChainAgreesAtTuple_of_normalisedRows` (through `Svd.tiesAt_of_rowPin`) turns the hypothesis on $\beta$ into `TiesAt D EX Dx μ`. This asserts characters, a selection, a base $B$, a number $\delta$, a function $\chi$ and constants $c_D$, with four ties: `HostTie`, `CharTie`, `AnTie`, and `ChainTie` for each word, the last stated with the ambient kernel `ambOf (recSeam D) B χ cD`. `RowE.of_all` collects these over all points.
2. **The row.** `typePrimePeriodRow_of_constructedPointChains` takes `JetSplitAmb` and the ties at $\mu_0$ and at each $\mu_w$, and gives the row: the bound `UsedTuplesBoundByConstant` with a constant $C_1$, and `familySizeBoundAtTypePrime`. It calls `row_atG_of_jetSplitAmb`.

`JetSplitAmb` bounds the $p$-adic size of the jets of the ambient kernel `ambOf s B χ cD` at a prime $p \ge 5$ that splits as $\pi\bar\pi$; it is stated in [`jetSplitAmb_holds`](/entry/jet-split-amb-holds/). We have not opened `row_atG_of_jetSplitAmb`, so we do not say how the jet bound becomes the valuation bound.

## In the Lean code

The theorem is at [ConstructionAtBundlePointsOfTrueColumns.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/ConstructionAtBundlePointsOfTrueColumns.lean#L11). The lemmas:

- `atGRows_bundlePoints_of_jetSplitAmbient` at [PeriodValuationsTypePrimesOfJetTableSplitPrimeStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/PeriodValuationsTypePrimesOfJetTableSplitPrimeStatement.lean#L8), a second name for `row_atG_pinned` at [PeriodValuationsTypePrimesOfJetTableSplitPrime.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/PeriodValuationsTypePrimesOfJetTableSplitPrime.lean#L11);
- `typePrimePeriodRow_of_constructedPointChains` at [TypePrimePeriodRowOfConstructedPointChainsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/TypePrimePeriodRowOfConstructedPointChainsStatement.lean#L9);
- `concreteChainAgreesAtTuple_of_normalisedRows` at [ConcreteChainAgreesAtTupleOfNormalisedRowsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/ConcreteChainAgreesAtTupleOfNormalisedRowsStatement.lean#L7);
- [`jetTableBound_splitPrime`](/entry/jet-table-bound-split-prime/).

`TiesAt` is at [JetSplitAmb.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/JetSplitAmb.lean#L29). The ties are produced at every tuple, but `typePrimePeriodRow_of_constructedPointChains` asks for them only at $\mu_0$ and the $\mu_w$.
