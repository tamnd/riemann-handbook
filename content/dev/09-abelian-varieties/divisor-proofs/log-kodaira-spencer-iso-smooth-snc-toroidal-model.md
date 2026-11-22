---
id: log-kodaira-spencer-iso-smooth-snc-toroidal-model
title: The log Kodaira-Spencer isomorphism on a smooth toroidal model (statement form)
kind: theorem
decl: GlobalTheory.T.logKodairaSpencer_iso_smooth_snc_toroidalModel
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.LogKodairaSpencerIsoSmoothSncToroidalModelStatement
covers: 2264
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`hasLogKS`](/entry/has-log-ks/), which has the real content. Its one user is [`toroidalForFanKS_of_rigidForFan`](/entry/toroidal-for-fan-ks-of-rigid-for-fan/), which applies it to the model that `RigidForFan` gives and so gets the last clause of `ToroidalForFanKS`.

## Statement

Use the model $Y$ over the coefficient field $F$, its semi-abelian scheme $G$, its interior $X^\circ_F$ and the condition `HasLogKS` from [the entry with the proof](/entry/has-log-ks/).

**Theorem.** Let $p + q \geq 1$. Let $Y$ be a model of $X^\circ_F$ over $F$ such that $Y$ is smooth over $F$ of relative dimension $\tfrac{[E:\mathbb{Q}]}{2} p q$, the boundary is a simple normal crossings divisor, and each closed boundary point has a rigid chart. Then `HasLogKS` holds for $G$ over $Y$ with interior $X^\circ_F$: on each affine open with a frame of the Lie algebra, the Kodaira-Spencer relation is the graph of an isomorphism from log derivations onto balanced symmetric matrices.

## Proof

The statement is the same as that of `GlobalTheory.LogKSAssembly.hasLogKS`, and the proof applies it.

## In the Lean code

The theorem is in [LogKodairaSpencerIsoSmoothSncToroidalModelStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LogKodairaSpencerIsoSmoothSncToroidalModelStatement.lean#L16). The proof is `first | exact @GlobalTheory.LogKSAssembly.hasLogKS | ...`, a tactic that tries the alias in three forms. The type is copied word for word from the theorem it calls.
