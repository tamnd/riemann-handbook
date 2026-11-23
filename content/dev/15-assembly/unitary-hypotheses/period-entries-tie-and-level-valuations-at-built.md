---
id: period-entries-tie-and-level-valuations-at-built
title: Six period and valuation rows in the large base form, restated
kind: theorem
decl: GlobalTheory.T.period_entries_tie_and_level_valuations_at_built
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.SixRowsAtMemberStatement
covers: 3302
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`six_rows_at_member_alt`](/entry/six-rows-at-member-alt/). It has the same statement, and its proof applies that theorem. The six rows feed the fields `aPt0`, `aPtTw`, `aPer0`, `aPerTw`, `tie` and `aP10` of [HypsAlt](/step/hyps-alt-def/), through [`allRows_of_open0_alt`](/entry/all-rows-of-open0-alt/) in [the unitary hypotheses node](/proof/unitary-hypotheses/). The real content is in [`levelPrimeColumnValuations_bundlePoints_overColumns`](/entry/level-prime-column-valuations-bundle-points-over-columns/), below `six_rows_at_member_alt`.

## Statement

For every family of slots $\mathcal S$ and every linkage $L_k$ of bundles, six statements of the form `Lg1 KPx (IsBuiltE 𝒮) (IsGoodE 𝒮) (fun S => X S Lk)` hold. The six rows $X$ are listed in the entry [`six_rows_at_member_alt`](/entry/six-rows-at-member-alt/).

## Proof

The proof is `six_rows_at_member_alt`. Nothing else is used.

## In the Lean code

The theorem is at [SixRowsAtMemberStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SixRowsAtMemberStatement.lean#L12). Its proof is the tactic

```
first | exact @six_rows_at_member_alt | exact six_rows_at_member_alt | (intros; apply six_rows_at_member_alt <;> assumption)
```

(namespaces shortened), under `set_option maxHeartbeats 1000000`. The first branch closes the goal, because the two statements are the same. So this theorem is a renaming. The name ends in "at built". The only built object in the statement is the slot `IsBuiltE 𝒮` in the large base condition. That condition plays no role in the proof, as the entry on `six_rows_at_member_alt` shows.
