---
id: double-step-adelic-integral-finite-twist-places
title: The double step integral at finitely many split places, second name
kind: theorem
decl: GlobalTheory.T.doubleStep_adelicIntegral_finiteTwistPlaces
module: Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs.DoubleStepAdelicIntegralFiniteTwistPlacesStatement
covers: 588
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the double step integral at finitely many places](/entry/val-q/). Its statement is `∀ D, ValQ D`, and its proof only applies `GlobalTheory.QVal.valQ`. [The law for one character](/entry/one-chart/) uses this theorem with the local data of a pinned tuple.

## Statement

For every datum $D$, the proposition `ValQ D` holds.

In words: the iterated quotient integral of a double theta step over finitely many split places equals a product of local volume factors times a finite sum of values of the same step with new coefficients. The precise form is in [the entry for `valQ`](/entry/val-q/).

## Proof

The proof is one line. It applies `GlobalTheory.QVal.valQ`.

## In the Lean code

The theorem is in [DoubleStepAdelicIntegralFiniteTwistPlacesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/DoubleStepAdelicIntegralFiniteTwistPlacesStatement.lean#L12). Its proof is

```
first | exact @GlobalTheory.QVal.valQ | ...
```

The name speaks of "twist places" and of an "adelic integral". In `ValQ` the places are any finite set of distinct split places that carry a local step `QStep`; no twist appears in the hypotheses. The integral is over the subgroup of adelic points that are $1$ away from these places, modulo a subgroup, and not over a quotient by rational points.
