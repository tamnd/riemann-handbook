---
id: exists-grid-pre
title: A grid of test data matches a given Weil family, under the size rows
kind: theorem
decl: GlobalTheory.GridJoin.exists_gridPre
module: Development.AbelianVarietyTheory.Proofs.TwistedOperators.AuxiliaryPrimeLtFirstTypePrimeOfSizes
covers: 316
status: drafted
drafted_by: writer@claude
---
This theorem gives a grid of test data `GridPre R` that is valid and matches a given Weil family $W$. It is a pass-through: it computes two hypotheses from the size rows and calls [`exists_gridPre_of_sizes`](/entry/exists-grid-pre-of-sizes/), which has the real content. It lies below the step [nonempty-hyps](/step/nonempty-hyps/), through the cusp transitions along the grid arrows.

## Statement

Assume the published inputs `DiscreteSeriesUpqExists`, `DiscreteSeriesCover` and `HarishChandraModules`, and `HostHyp D`. Let `large₂` be size data with `SizeRows large₂`. Let $R$ satisfy `Core R F` for a face $F$, let the scale satisfy `sc.cGap = 1`, and let $W$ be a Weil family `G'.Weil` of a grid $G'$ with `W.Over R`. Then there is $G$ : `GridPre R` with `G.Is` and `Match G W`.

## Proof

1. `RowSizes.sizes_of_sizeRows` turns `SizeRows large₂` into `Sizes D`.
2. `auxiliaryPrime_lt_firstTypePrime_of_sizeRows` (line 112) gives $q_0 < g_0$, where $q_0$ = `q0 D` is the auxiliary prime and $g_0$ = `D.host.g 0`. It bounds $\log q_0$ by the scale $L$ and then compares with $(k\,b)^8$.
3. [`exists_gridPre_of_sizes`](/entry/exists-grid-pre-of-sizes/) gives the grid.

## In the Lean code

The theorem is at [AuxiliaryPrimeLtFirstTypePrimeOfSizes.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/AuxiliaryPrimeLtFirstTypePrimeOfSizes.lean#L176). The file is named after the helper of step 2, not after this theorem. That helper reads its facts by long chains of projections such as `hs.2.2.2.2.2.2.2.2.1`, so it breaks if the fields of `SizeRows` change order. We did not unfold `SizeRows`, `Sizes`, `HostHyp` or `Core`. Callers include `exists_row_lift_matching`, `exists_rowMatchS` and the cusp-transition steps along the right and down arrows.
