---
id: model-statement-of-crystalline-chebotarev-frame-gal
title: The model statement, under a second name
kind: theorem
decl: GlobalTheory.T.model_statement_of_crystalline_chebotarev_frame_gal
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ModelStOfFramesStatement
covers: 1468
status: drafted
drafted_by: writer@claude
---
This theorem is a copy of [`modelSt_of_small_frame_gal`](/entry/model-st-of-small-frame-gal/) under a second name. That entry has the content. Its only user is [the exponent bound](/entry/exponent-bound-of-unitary-theta-standard-theorems-alt/), which gets the model statement from it. Below this theorem are 1,468 declarations, one more than below the copy.

## Statement

**Theorem.** Assume `BhattScholzeCrystallineLattices` and `ChebotarevDegreeOne`, the smallness condition, the frame statement `FrameStatement'` and the Galois statement. Then `ModelStatement` holds: at each twisted place $w$ in range, for each matching pair of parameters and weights, a family of Hida settings covers the block subspace at $w$, and each setting satisfies `WInputsLink` at the residue characteristic of $w$. The [copy](/entry/model-st-of-small-frame-gal/) states this in full.

## Proof

The proof applies `GlobalTheory.ExpModel.modelSt_of_small_frame_gal` to the five hypotheses, in the same order.

## In the Lean code

The theorem is in [ModelStOfFramesStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ModelStOfFramesStatement.lean#L12). Its type is the type of the copy. The proof is the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)`, and the first branch closes the goal.

The caller gives it `small_estimate` for the smallness condition and `frame_statement_of_small_statement small_estimate` for the frame statement, so only the two named hypotheses and the Galois statement are real inputs at that point.
