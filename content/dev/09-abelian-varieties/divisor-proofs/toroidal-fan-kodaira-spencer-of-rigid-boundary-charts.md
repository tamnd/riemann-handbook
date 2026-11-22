---
id: toroidal-fan-kodaira-spencer-of-rigid-boundary-charts
title: Rigid boundary charts give the log Kodaira-Spencer isomorphism (statement form)
kind: theorem
decl: GlobalTheory.T.toroidalFanKodairaSpencer_of_rigidBoundaryCharts
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ToroidalFanKodairaSpencerOfRigidBoundaryChartsStatement
covers: 2266
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`toroidalForFanKS_of_rigidForFan`](/entry/toroidal-for-fan-ks-of-rigid-for-fan/), which in turn only moves data; the content is in [`hasLogKS`](/entry/has-log-ks/). Its one user is [`toroidalForFanKS`](/entry/toroidal-for-fan-ks/), which applies it to [`rigidBoundaryChartsForFan_unitaryDatum`](/entry/rigid-boundary-charts-for-fan-unitary-datum/), a proof of `RigidForFan`.

## Statement

Use the statements `RigidForFan` and `ToroidalForFanKS` from [the entry with the proof](/entry/toroidal-for-fan-ks-of-rigid-for-fan/). In short: for each CM datum and each fan, `RigidForFan` gives a smooth projective toroidal model with simple normal crossings boundary and rigid charts at its closed boundary points, and `ToroidalForFanKS` gives such a model with the log Kodaira-Spencer isomorphism.

**Theorem.** `RigidForFan` implies `ToroidalForFanKS`.

## Proof

The statement is the same as that of `GlobalTheory.RigChart.toroidalForFanKS_of_rigidForFan`, and the proof applies it.

## In the Lean code

The theorem is in [ToroidalFanKodairaSpencerOfRigidBoundaryChartsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ToroidalFanKodairaSpencerOfRigidBoundaryChartsStatement.lean#L16). The proof is `first | exact @GlobalTheory.RigChart.toroidalForFanKS_of_rigidForFan | ...`, a tactic that tries the alias in three forms. The type is the same as that of the theorem it calls.
