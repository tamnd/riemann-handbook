---
id: normalised-theta-cmcurve-theorems-of-algebraic-translates
title: The theta and CM curve inputs from algebraic translates, restated
kind: theorem
decl: GlobalTheory.T.normalisedThetaCMCurveTheorems_of_algebraicTranslates
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.NormalisedThetaCMCurveTheoremsOfAlgebraicTranslaStatement
covers: 908
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`inputs_of_algT`](/entry/inputs-of-alg-t/). It has the same statement, and its proof applies that theorem. Its user is [`at_of_true_columns`](/entry/at-of-true-columns/), which needs the theta inputs to prove the kernel conditions `Pdv.At`. The content is in `inputs_of_algT`.

## Statement

**Theorem.** `AlgTAll` implies `ThLoc.Inputs`.

`AlgTAll` says that for each datum $D$, each ideal $\mathfrak c$ with `IsCurveIdeal`, each $\delta$ with `IsDiscriminantTwelfthRootOfIdealLattice`, each base $B$ over $(D, \mathfrak c, \delta)$ and each character $\chi$ with `IsChi`, the property `B.AlgT χ` holds: certain Taylor coefficients of torsion translates are algebraic numbers. `Inputs` is a structure of eight propositions about CM elliptic curves and theta functions. Both are described in [`inputs_of_algT`](/entry/inputs-of-alg-t/).

## Proof

Apply `inputs_of_algT`. Nothing else is used.

## In the Lean code

The theorem is at [NormalisedThetaCMCurveTheoremsOfAlgebraicTranslaStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/NormalisedThetaCMCurveTheoremsOfAlgebraicTranslaStatement.lean#L12). The proof is the tactic

```
first | exact @GlobalTheory.ThLoc.inputs_of_algT | exact GlobalTheory.ThLoc.inputs_of_algT | (intros; apply GlobalTheory.ThLoc.inputs_of_algT <;> assumption)
```

The two statements are the same. The name says that theorems on normalised theta functions and CM curves follow from algebraic translates. In fact `AlgTAll` is used only as one field of `Inputs`; the other seven fields are proved with no hypothesis.
