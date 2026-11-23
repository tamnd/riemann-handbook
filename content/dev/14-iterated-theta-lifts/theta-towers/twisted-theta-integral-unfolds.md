---
id: twisted-theta-integral-unfolds
title: The unfolding step of the row test, restated
kind: theorem
decl: GlobalTheory.T.twisted_theta_integral_unfolds
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.TwistedThetaIntegralUnfolding
covers: 1982
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`twisted_theta_integral_unfolding`](/entry/twisted-theta-integral-unfolding/), which has the content. Its one user is [the five properties of the twisted theta lifts](/entry/theta-lift-row-properties-conj/), which gives its result to the lift formula `Formula2K`.

## Statement

Assume `ThetaLocalInputs`, the [record of named literature statements](/step/theta-local-inputs-def/), the statement `LiftsCuspidal` that along each arrow of the grid the theta kernel lifts cusp forms to cusp forms, and the statement `SumOKK` that the finite sums of the row test are meaningful. Then `StepUnfold` holds: for all large admissible choices, the pairing of a column vector with an iterated theta lift is a finite sum over cosets of local coefficients times periods. A period here is an integral over a fundamental domain. The [entry of the main theorem](/entry/twisted-theta-integral-unfolding/) gives the exact form.

## Proof

The statement is the same as that of `twisted_theta_integral_unfolding`, and the proof applies it.

## In the Lean code

The theorem is in [TwistedThetaIntegralUnfolding.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedThetaIntegralUnfolding.lean#L37). The proof is

```
first | exact @_root_.GlobalTheory.RowUnfLast.twisted_theta_integral_unfolding | ...
```

The two theorems have the same type, so the first branch closes the goal.
