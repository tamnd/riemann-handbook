---
id: theta-conditions-of-inputs-of-jumps-card
title: The point conditions of a datum, second name
kind: theorem
decl: GlobalTheory.T.theta_conditions_of_inputs_of_jumpsCard
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.GaloisRepIsGeometricAtAllPlaces
covers: 800
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`RowsAll.locComp_of_isRc_classMapD_cenLoc`](/entry/rows-all-loc-comp-of-is-rc-class-map-d-cen-loc/). It gives the record `PointConditions' D` for one datum $D$. Two lemmas below [the proof that HypsAlt is nonempty](/proof/unitary-hypotheses/) call it, in branch 1 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). Below it are 800 declarations, one more than below the first name.

## Statement

The statement is that of the first name, word for word. Assume `ThetaLocalInputsAlt`, `HarishChandraFinite` and `CuspRapidDecay`. Let $h_L$ witness [RecTExists](/step/rect-exists-def/) and let $D$ be a datum. If `LinkedInputs hL D` and `JumpsCard` hold for $D$, then `PointConditions' D` holds. The [entry of the first name](/entry/rows-all-loc-comp-of-is-rc-class-map-d-cen-loc/) says what these records contain.

## Proof

The proof is `exact locComp_of_isRc_classMapD_cenLoc`, inside a `first | … | …` tactic that tries three forms of the same call. There is no other content.

## In the Lean code

The theorem is at [GaloisRepIsGeometricAtAllPlaces.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/GaloisRepIsGeometricAtAllPlaces.lean#L42), and the first name at line 24 of the same file. The callers are in [PreAtMem.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PreAtMem.lean#L57) and [PointwiseGaloisPropertiesOfLocalInputs.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PointwiseGaloisPropertiesOfLocalInputs.lean#L38).

This name is closer to the statement than the first name: "jumps card" is the hypothesis `JumpsCard`. The words "theta conditions" fit loosely, since some fields of the conclusion are about theta lifts.
