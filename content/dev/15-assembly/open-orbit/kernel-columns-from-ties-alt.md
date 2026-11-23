---
id: kernel-columns-from-ties-alt
title: The column rows from the kernel ties (a restatement)
kind: theorem
decl: GlobalTheory.T.kernel_columns_from_ties_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.RowsUOfColPinsStatement
covers: 1103
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`rowsU_of_colPins_alt`](/entry/rows-u-of-col-pins-alt/). It has the same statement, word for word, and its proof only calls that theorem. Its only user is [`definiteSideCondition_of_nprimeDef_of_nuFull`](/entry/definite-side-condition-of-nprime-def-of-nu-full/), which proves the [definite side condition](/step/definite-side-condition-def/) at one bundle with it. The real content is in the entry for `rowsU_of_colPins_alt`, and below it in [`rowsBody_of_kerTies`](/entry/rows-body-of-ker-ties/).

## Statement

The same as [`rowsU_of_colPins_alt`](/entry/rows-u-of-col-pins-alt/). In short: for reals $C_Y$ and $C_T \ge 0$ there is a constant $C_0$ such that, for column data that satisfy the column character ties, the kernel ties, the kernel size bounds with $C_Y, C_T$, `NprimeDef`, `NuFull` and positive ranks, and for each word $u$ with numerical facts whose constant $C_h$ is at least $C_0$, the column row statement `RowsU` holds at $u$, written out in full.

## Proof

The proof is one tactic line:

```
first | exact @_root_.GlobalTheory.ColRows.rowsU_of_colPins_alt | ...
```

The first branch succeeds, because the two statements are the same term.

## In the Lean code

The theorem is at [RowsUOfColPinsStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowsUOfColPinsStatement.lean#L13). The statement text after the name is the same string as the one at [RowsUOfColPins.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowsUOfColPins.lean#L17); we compared the two lines. The same `first | exact ...` proof is in two other "Statement" files below this entry: [`memberRows_of_kernelDatum_sizes`](/entry/member-rows-of-kernel-datum-sizes/) calls `rowsBody_of_kerTies`, and `frames_tilde_gamma_values_alt` calls `ev_ipAt_le_normAt_sq_alt`. We did not compare the statements of those pairs.
