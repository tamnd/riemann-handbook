---
id: reference-chain-evaluation-at-bundle-points-of-over-cols
title: The forms map row at bundle points, the statement form
kind: theorem
decl: GlobalTheory.T.referenceChainEvaluationAtBundlePoints_of_overCols
module: Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.ReferenceChainEvaluationBundlePointsOverColumnsAStatement
covers: 459
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It states the result of [the forms map row from true columns](/entry/reference-chain-evaluation-bundle-points-over-columns/) and proves it by calling that theorem. Its only user is [six rows at a member](/entry/six-rows-at-member-alt/), which uses it for the first of its six rows. That row becomes the field `aPt0` of [the record HypsAlt](/step/hyps-alt-def/). The real content is in [the forms map from a symmetric comparison](/entry/forms-map-of-symmetric-comparison-lower-map-finite-char/).

## Statement

Let $Q$ be a slot (a predicate on constructed points) such that every point in $Q$ comes from true columns (`OverCols Q`). Let `Bd` be any bundle type and `Lk` any link for it. Then the row statement `ReferenceChainEvaluationAtBundlePoints Q Lk` holds.

This row statement is `Row Q Lk fun 𝒜 _ => ReferenceChainEvaluationAdmissible 𝒜`. The property `ReferenceChainEvaluationAdmissible 𝒜` says: [closed](/step/closed-def/) on the class `W3 𝒜`, there is $x_0$ such that `Conclusion6 (Fm.D x i) u` holds for all $x \ge x_0$ with $x > x_1$, all indices $i$ and all words $u$. [The forms map from a symmetric comparison](/entry/forms-map-of-symmetric-comparison-lower-map-finite-char/) says what `Conclusion6` means.

## Proof

The proof is `first | exact @GlobalTheory.Fc.PeriodEntriesOverColumns.referenceChainEvaluation_bundlePoints_overColumns | ...`. The two statements are the same, word for word.

## In the Lean code

The theorem is in [ReferenceChainEvaluationBundlePointsOverColumnsAStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/ReferenceChainEvaluationBundlePointsOverColumnsAStatement.lean#L8). The row statement is in [ReferenceChainEvaluationAtBundlePoints.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/ReferenceChainEvaluationAtBundlePoints.lean#L16). The theorem is used once, in [SixRowsAtMember.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SixRowsAtMember.lean#L22).

The name says "reference chain evaluation", but the property is `Conclusion6`, a set of facts about the period map on forms. No reference chain appears in the statement.
