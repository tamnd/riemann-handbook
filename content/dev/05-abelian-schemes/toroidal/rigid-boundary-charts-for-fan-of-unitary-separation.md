---
id: rigid-boundary-charts-for-fan-of-unitary-separation
title: Rigid boundary charts from unitary separation, the wrapper
kind: theorem
decl: GlobalTheory.T.rigidBoundaryChartsForFan_of_unitarySeparation
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.RigidBoundaryChartsForFanOfUnitarySeparationStatement
covers: 1299
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [`rigidForFan_of_uStB`](/entry/rigid-for-fan-of-u-st-b/). Its only user is [`rigidForFan_holds`](/entry/rigid-for-fan-holds/), which applies it to [the separation theorem](/entry/unitary-toroidal-separation-of-base/) and gets `RigidForFan` with no hypothesis. The content is in [`rigidForFan_of_uStB`](/entry/rigid-for-fan-of-u-st-b/).

## Statement

**Theorem.** `UStB` implies `RigidForFan`.

`UStB` says: for each unitary moduli scheme $X_F$ and each invariant function $\varphi$ with the fan conditions, there are a projective compactification $Z$ and a normalized blow-up $S \to Z$ of an ideal on the boundary, with the separation property `SepB` at the boundary of $S$. `RigidForFan` says: there is a smooth projective model $Y$ of $X_F$ with simple normal crossings boundary, an ample twist $(\det\omega)^k(-B)$, a chart at each boundary point and a rigid chart at each closed boundary point. See [the main entry](/entry/rigid-for-fan-of-u-st-b/) for the full statement.

## Proof

The proof is the term `GlobalTheory.UChartJoin.rigidForFan_of_uStB`. There is nothing else.

## In the Lean code

The theorem is at [RigidBoundaryChartsForFanOfUnitarySeparationStatement.lean line 10](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/RigidBoundaryChartsForFanOfUnitarySeparationStatement.lean#L10). The proof is a `first | exact … | …` tactic block whose alternatives all try the same lemma. The statement files of this chapter use this pattern: a theorem in the namespace `GlobalTheory.T` states a result, and a theorem in another file proves it.
