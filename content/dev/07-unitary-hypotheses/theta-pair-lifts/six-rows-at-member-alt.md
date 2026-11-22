---
id: six-rows-at-member-alt
title: Six period and valuation rows in the large base form
kind: theorem
decl: GlobalTheory.Fc.six_rows_at_member_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.SixRowsAtMember
covers: 3301
status: drafted
drafted_by: writer@claude
---
This theorem puts six rows about periods, twisted points, ties and column valuations into the form `Lg1`, which the record `AllRowsAlt` asks for. Its user is [`allRows_of_open0_alt`](/entry/all-rows-of-open0-alt/), which fills the fields `aPt0`, `aPtTw`, `aPer0`, `aPerTw`, `tie` and `aP10` from it. These become the fields of the same names in [HypsAlt](/step/hyps-alt-def/), in branch 1 of [the unitary hypotheses node](/proof/unitary-hypotheses/). The statement is also available under the name [`period_entries_tie_and_level_valuations_at_built`](/entry/period-entries-tie-and-level-valuations-at-built/). Most of its size (2,426 of 3,301 declarations) is in [`levelPrimeColumnValuations_bundlePoints_overColumns`](/entry/level-prime-column-valuations-bundle-points-over-columns/).

## Statement

`Lg1 KP Q Q' r` means: there is a slot $R$ with `LargeBaseCondition KP Q R` and $r(Q' \wedge R)$. Each of the six rows has the form `Row S Lk (fun 𝒜 _ => Closed (W3 𝒜) P)` (see [Row](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/ValidForConstructedPointClassesEventuallyWorking.lean#L268) and [Closed](/step/closed-def/)). The property $P$ of a family $F$ is, for the six rows:

1. eventually, `Conclusion6` holds at each point of $F$ and each $u$;
2. eventually, `TwistedPointIntegral` holds at each point and its twist;
3. eventually, `PeriodClassSumWeyl` holds at each point;
4. eventually, `TwistedPeriodAdmissible` holds at each point and its twist;
5. `RealPlaceSecondLayerConditions` holds for $F$;
6. eventually, `Conclusion5Sharp` and `TwistedColumnBoundAtT` hold at each point and each $u$.

I did not unfold these six properties.

**Theorem.** For every family of slots $\mathcal S$ and every linkage $L_k$ of bundles, each of the six rows $X$ satisfies `Lg1 KPx (IsBuiltE 𝒮) (IsGoodE 𝒮) (fun S => X S Lk)`.

## Proof

1. Take for $R$ the slot that is always true. `largeBaseProperty_true` proves `LargeBaseCondition KPx (IsBuiltE 𝒮) R`. Its proof uses zero constants, empty sets and `trivial`.
2. `goodTwistCores_over_trueColumns` (a renaming of `overCols_goodE`) gives `OverCols` for the slot `IsGoodE 𝒮` $\wedge R$. This means every point of the slot has `HasCols`.
3. Six lemmas each prove one row for any slot that has `OverCols`, any bundle type and any linkage. Apply them to the slot of step 2 and to $L_k$.

## In the Lean code

The theorem is at [SixRowsAtMember.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SixRowsAtMember.lean#L11). The six rows are defined in [ReferenceChainEvaluationAtBundlePoints.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/ReferenceChainEvaluationAtBundlePoints.lean#L16) and [LevelPrimeColumnValuationsAtBundlePoints.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/LevelPrimeColumnValuationsAtBundlePoints.lean#L15). `largeBaseProperty_true` is in [EventuallyAllScaleContextsAndOfBoth.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/EventuallyAllScaleContextsAndOfBoth.lean#L91). The six lemmas are in the folder `Development/AbelianVarietyTheory/Proofs/GlobalInterpolation`. I did not unfold their proofs.

Three points about the statement:

- The large base condition is free for the true slot. So `KPx` and `IsBuiltE 𝒮` play no role.
- The six lemmas hold for every linkage. So no property of $L_k$ is used.
- Each row ignores the selection $\sigma$ of bundles. It is a property of the family class only.

The name says "at member", but no membership condition appears in the statement or the proof.
