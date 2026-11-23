---
id: level-prime-column-valuations-bundle-points-over-columns
title: Column valuations at bundle points, the statement form
kind: theorem
decl: GlobalTheory.T.levelPrimeColumnValuations_bundlePoints_overColumns
module: Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.LevelPrimeColumnValuationsBundlePointsOverColumnStatement
covers: 2426
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It states the result of [column valuations at bundle points from true columns](/entry/row-level-valuations/) and proves it by calling that theorem. The real content is in that entry. Its only user is [six rows at a member](/entry/six-rows-at-member-alt/), which uses it for the last of its six rows. That row becomes the field `aP10` of [the record HypsAlt](/step/hyps-alt-def/).

## Statement

Let $Q$ be a slot (a predicate on constructed points) such that every point in $Q$ comes from true columns (`OverCols Q`). Let `Bd` be any bundle type and `Lk` any link for it. Then the row statement `LevelPrimeColumnValuationsAtBundlePoints Q Lk` holds.

[Column valuations at bundle points from true columns](/entry/row-level-valuations/) says what this row statement means.

## Proof

The proof is `first | exact @GlobalTheory.Fc.Cv.row_level_valuations | ...`. It applies that theorem. The two statements are the same, word for word.

## In the Lean code

The theorem is in [LevelPrimeColumnValuationsBundlePointsOverColumnStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/LevelPrimeColumnValuationsBundlePointsOverColumnStatement.lean#L8). It is used once, in [SixRowsAtMember.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SixRowsAtMember.lean#L24). There the slot is `sAnd (IsGoodE 𝒮) fun _ _ _ _ _ => True` and the bundle type is `BundleCondition`.
