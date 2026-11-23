---
id: twisted-lift-flip-invariant
title: The flip step of the row test, second name
kind: theorem
decl: GlobalTheory.T.twisted_lift_flip_invariant
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.TwistedLiftFlipInvariant
covers: 404
status: drafted
drafted_by: writer@claude
---
This theorem is a second name. It proves the flip step `StepFlip` of the row test, which [the five properties of the twisted theta lifts](/entry/theta-lift-row-properties-conj/) pass to `rowTestLiftFormula_principalLevel`. The proof only applies [`twist_sign_flip_succ`](/entry/twist-sign-flip-succ/), and that entry has the real content.

## Statement

**Theorem.** Assume [`ThetaLocalInputs`](/step/theta-local-inputs-def/), `LiftsCuspidal`, `WeilConvergence`, [`ThetaIntegralsAgree`](/step/theta-integrals-agree-def/) and `ConstK`. Then `StepFlip` holds.

`StepFlip` is $\mathrm{Big}(\texttt{FlipAt})$. In words: for all large admissible choices, the theta lift $\theta_\chi$ along the row from node $(0,0)$ to node $(m,0)$ of the grid of Hermitian spaces is a fixed multiple of an iterated lift of a form on node $(0,m)$ along the opposite path, through node $(m,m)$. The factor is $(z_t\, c_{\mathrm{tot}}(t))^{-1}$, with $z_t$ in the group `xiVals` and $c_{\mathrm{tot}}(t)$ the product of the square constants $c_{ij}(t)$ of `ConstK`. [The child entry](/entry/twist-sign-flip-succ/) gives the full statement.

## Proof

The proof is `first | exact twist_sign_flip_succ | ...`. The first branch closes the goal, since the two statements are the same.

## In the Lean code

The theorem is in [TwistedLiftFlipInvariant.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedLiftFlipInvariant.lean#L37). `StepFlip` and `FlipAt` are in [StepUnfold.lean](lean:Development/AbelianVarietyTheory/Statements/HeckeThetaIntegrals/StepUnfold.lean#L99).

The word "invariant" in the name is misleading. The statement is not an invariance: it is an identity between two lifts, with the constant $(z_t\, c_{\mathrm{tot}}(t))^{-1}$.
