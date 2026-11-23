---
id: reference-chain-evaluation-bundle-points-over-columns
title: The forms map row at bundle points from true columns
kind: theorem
decl: GlobalTheory.Fc.PeriodEntriesOverColumns.referenceChainEvaluation_bundlePoints_overColumns
module: Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.ReferenceChainEvaluationBundlePointsOverColumnsA
covers: 458
status: drafted
drafted_by: writer@claude
---
This theorem turns a pointwise fact at constructed points into a row statement on family classes. The pointwise fact is [the forms map at a bundle point over true columns](/entry/constructed-point-reference-chain-word-forms-map/). The row statement goes to the relay [the forms map row, the statement form](/entry/reference-chain-evaluation-at-bundle-points-of-over-cols/), and from there to [six rows at a member](/entry/six-rows-at-member-alt/) and the field `aPt0` of [HypsAlt](/step/hyps-alt-def/). The proof has the same shape as that of [column valuations at bundle points from true columns](/entry/row-level-valuations/), which explains the words `Row`, `Row0`, `EvC` and `OverCols`.

## Statement

For a datum $D$ of type `D7` and an object $O$ over it, let $R(D, O)$ be the statement: `Conclusion6 D u` holds for every word $u$ of $D$. $R$ does not depend on $O$. [The forms map from a symmetric comparison](/entry/forms-map-of-symmetric-comparison-lower-map-finite-char/) says what `Conclusion6` means.

**Theorem.** Let $Q$ be a slot with `OverCols Q`. Let `Bd` be any bundle type and `Lk : LkT Bd` any link. Then `ReferenceChainEvaluationAtBundlePoints Q Lk` holds.

This row statement is `Row Q Lk fun 𝒜 _ => ReferenceChainEvaluationAdmissible 𝒜`, and `ReferenceChainEvaluationAdmissible 𝒜` unfolds to `EvC R 𝒜`: [closed](/step/closed-def/) on `W3 𝒜`, eventually in $x$, $R$ holds at the datum of each point of the family.

## Proof

1. `Row0.row` reduces the claim to `Row0 Q (EvC R)`, the row statement for the trivial bundle type and the trivial link. So `Bd` and `Lk` play no role.
2. `validForConstructedPointClasses_eventuallyWorkingClass` reduces `Row0 Q (EvC R)` to this: eventually in the parameters, $R(\beta.D, \beta.O)$ holds at each constructed point $\beta$ in $Q$.
3. `EvP.of_all` reduces this to the same claim for all parameters.
4. [The forms map at a bundle point over true columns](/entry/constructed-point-reference-chain-word-forms-map/) proves the claim at each point $\beta$ in $Q$.

## In the Lean code

The theorem is in [ReferenceChainEvaluationBundlePointsOverColumnsA.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/ReferenceChainEvaluationBundlePointsOverColumnsA.lean#L18). `Row0.row`, `EvP.of_all` and `validForConstructedPointClasses_eventuallyWorkingClass` are in [ValidForConstructedPointClassesEventuallyWorking.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/ValidForConstructedPointClassesEventuallyWorking.lean#L388). The pointwise lemma `constructedPoint_referenceChainWord_formsMap` is in the same file, at [line 12](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/ReferenceChainEvaluationBundlePointsOverColumnsA.lean#L12).

The "eventually" and "closed" parts of the row statement are not used. The property holds at every point, for all parameters, and the threshold $x_0$ is zero. The object $O$ and the bundle data play no role.
