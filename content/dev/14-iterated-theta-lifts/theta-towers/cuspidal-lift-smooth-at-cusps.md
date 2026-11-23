---
id: cuspidal-lift-smooth-at-cusps
title: The lift property on all theta functions, as a copy
kind: theorem
decl: GlobalTheory.T.cuspidal_lift_smooth_at_cusps
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.CuspidalLiftSmoothAtOfCuspidalLift
covers: 1415
status: drafted
drafted_by: writer@claude
---
This theorem is a copy of [the smooth form of the lift property](/entry/cuspidal-lift-smooth-at-of-cuspidal-lift/), with the same statement. Its only use is in [the cusp step along the grid](/entry/cusp-step-of-large-flip-run/). All the content is in the theorem that it copies. Below this theorem are 1,415 declarations.

## Statement

**Theorem.** Assume `LiftsCuspidal` (theta lifts with Fock test vectors keep cusp forms) and the record [ThetaLocalInputs](/step/theta-local-inputs-def/). Then `LiftsCuspidalSmoothAt D` holds for each datum $D$: along each of the five kinds of arrows of a grid, the theta lift with any theta function $\Phi$ as test function converges on cusp forms of the right type and gives a cusp form of the right type. The [entry of the copied theorem](/entry/cuspidal-lift-smooth-at-of-cuspidal-lift/) states this in full.

## Proof

The proof applies `GlobalTheory.CuspSmoothLift.cuspidal_lift_smooth_at_of_cuspidal_lift`. There is no other step.

## In the Lean code

The theorem is in [CuspidalLiftSmoothAtOfCuspidalLift.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/CuspidalLiftSmoothAtOfCuspidalLift.lean#L59), in the same file as the theorem it copies. The proof is the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)`.

The name is misleading. "At cusps" suggests a statement about the behaviour of forms near the cusps. The statement is about all theta functions as test vectors; the suffix "At" in `LiftsCuspidalSmoothAt` refers to the datum $D$, and the word "cusp" refers to cusp forms.
