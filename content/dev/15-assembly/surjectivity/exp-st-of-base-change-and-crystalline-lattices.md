---
id: exp-st-of-base-change-and-crystalline-lattices
title: The exponent bound, under a second name
kind: theorem
decl: GlobalTheory.T.expSt_of_base_change_and_crystalline_lattices
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ExponentBoundOfUnitaryThetaStandardTheorems
covers: 3719
status: drafted
drafted_by: writer@claude
---
This theorem is a copy of [`exponent_bound_of_unitaryThetaStandardTheorems_alt`](/entry/exponent-bound-of-unitary-theta-standard-theorems-alt/) under a second name. That entry has the content. Its only user is [`ontoX_of_hypotheses_alt_alt`](/entry/onto-x-of-hypotheses-alt-alt/), which gets `ExponentStatement` from it in branch 2 of the [unitary hypotheses node](/proof/unitary-hypotheses/). Below this theorem are 3,719 declarations, one more than below the copy.

## Statement

**Theorem.** Assume `ClozelCohomological`, `HeckeLAdicCharacter`, `ChebotarevDegreeOne`, `CuspUAlt`, `BaseChangeDefiniteUnitaryGroup`, `BhattScholzeCrystallineLattices`, `HeckeLAdicCharacterAbove` and [`RecTExists`](/step/rect-exists-def/). Then `ExponentStatement` holds: at the recorded objects of large families, the exponents $J_0$ at the twisted places are bounded by weights $J_p(j, \ell)$ whose sums $\sum_{\ell \in Q} J_p(j,\ell) \log \ell$ are bounded. The [copy](/entry/exponent-bound-of-unitary-theta-standard-theorems-alt/) states this in full.

## Proof

The proof applies `exponent_bound_of_unitaryThetaStandardTheorems_alt` to the eight hypotheses, in the same order.

## In the Lean code

The theorem is in [ExponentBoundOfUnitaryThetaStandardTheorems.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExponentBoundOfUnitaryThetaStandardTheorems.lean#L38), in the same file as the copy. Its type is the type of the copy, word for word. The proof is the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)`, and the first branch closes the goal.

The name mentions base change and crystalline lattices. These are two of the eight hypotheses (`BaseChangeDefiniteUnitaryGroup` and `BhattScholzeCrystallineLattices`). The name of the copy mentions "unitary theta standard theorems", and neither name says which eight results are assumed.
