---
id: loop-row-bounds-along-family-large-gaps
title: The row bounds along a family with large gaps (renaming)
kind: theorem
decl: GlobalTheory.T.loopRowBounds_along_family_largeGaps
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.LoopRowBoundsAlongFamilyLargeGapsStatement
covers: 365
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [`rows_along_family`](/entry/rows-along-family/). It adds no mathematics. Its only user is [`loop_rows_closed_gap`](/entry/loop-rows-closed-gap/), where it gives the constants of step 3. The proof is in the entry of the original.

## Statement

Assume the Siegel mass ratio `SiegelMassRatio`, the gap hypothesis `GapIn.Hyp` and `ThmBpDS`. Then for all real constants $C_g, c_b, C_u, c_T, C_T, C_0, A, C_1, c_V, C_\Gamma$ there are $C_0'$ and a threshold $t$ with this property. Let $F$ be a family with constant $C_\Gamma$, with $t \le C'(F)$ and $t \le C_l(F)$, and with the rank hypothesis `RanksF`. Then:

1. for all large $x$, the counting hypothesis `Cnt.Hyp0` gives `FormAt` for each word $u$;
2. for term ties $X$ and loop ties $Y$ that meet `rows_TiesF`, `wordPairTermInjective`, `wordPairBetaLattice` and, for all large $x$, the cell bound `TermVolumeSmallCellBound` with $c_V$, and for each $C \ge C_0'$: for all large $x$ and all word pairs that meet `Cnt.Hyp`, the bounds `RowsND`, `RowsDeg` and `RowsOne` hold with $C$.

## Proof

The proof is the term `rows_along_family`, tried in three forms by a `first | exact @X | exact X | (intros; apply X <;> assumption)` tactic. The two statements are the same, so the first form works.

## In the Lean code

The theorem is at [LoopRowBoundsAlongFamilyLargeGapsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/LoopRowBoundsAlongFamilyLargeGapsStatement.lean#L13). The original is `GlobalTheory.LoopRowBoundsGap.rows_along_family` in [LoopRowBoundsAlongFamilyLargeGaps.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/LoopRowBoundsAlongFamilyLargeGaps.lean#L25).
