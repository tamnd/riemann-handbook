---
id: fam-joint-bcd
title: Joint hub conditions along a family, from word conditions at large scale
kind: theorem
decl: GlobalTheory.HTW.RecS.fam_jointBCD
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.FamJointBCD
covers: 328
status: drafted
drafted_by: writer@claude
---
This theorem gives a threshold $x_0$ along a family `FamP`, past which the joint hub conditions hold at each member that satisfies `ConclusionJa` and the point inputs `PtIn`. [The closed form](/entry/fam-joint-bcd-closed-alt/) removes these two member hypotheses. The proof joins two results: word conditions at large scale, and a local lemma that turns words into the hub conditions.

## Statement

Let `Fm : FamP eps` be a family, with data $D = $ `Fm.D x j` and size parameters $L = $ `Fm.L x j`, and let $R$ be a `RowK` datum. Assume `adm7 D` and `FontaineAtPlacesOverL` for all data.

**Theorem.** There is $x_0$ such that for $x \ge x_0$ with $x > x_1$, each index $j$, each `HW` and each hub datum $X$ of $D$: if `ConclusionJa D` holds, and `PtIn` holds for $(X.r_i, X.\rho_i, \pi)$ at each twisted place $i$ with $\ell_i$ inert and each good $\pi$, then `JointParametersHubConditions L HW X R` holds.

The conclusion says: at each such $i$ and $\pi$, the bound condition with constant $R.C_2$ holds if $\ell_i$ is in the row range of $L$ (`IsRowB`), and the congruence condition holds if not.

## Proof

1. `fam_joints` gives $x_0$ such that each member past $x_0$ with `ConclusionJa` satisfies `JointB` with constant $R.C_2$ and `JointCD`. These say: at each inert unramified $\ell_i$ and each point with `PtIn`, there is a word with given size bounds. The threshold is the maximum of the thresholds of `inertLongOrbitWordConditions_of_large_scale` and `inertPrimeWordConditions_of_large_scale`.
2. `frozenBCD_of` turns `InertK` into `InertUnr` (`inert_iff`). Then `frozenB_of` gives the bound condition from `JointB`, and `frozenCD_of` gives the congruence condition from `JointCD`.

## In the Lean code

The theorem is at [FamJointBCD.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/FamJointBCD.lean#L18). `fam_joints` is at [FamJEpsPos.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/FamJEpsPos.lean#L30), `frozenBCD_of` at [ClusteredLetterwiseBoxes.lean](lean:Development/AbelianVarietyTheory/Counterexamples/HeckeCharacterExamples/ClusteredLetterwiseBoxes.lean#L205), and `JointB`, `JointCD` at [ThickLetterWordLatticeSurjectionHypotheses.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/ThickLetterWordLatticeSurjectionHypotheses.lean#L65). We did not unfold the bound and congruence conditions or the word predicates.

Odd points:

- $R$ enters only through $R.C_2$.
- `frozenBCD_of` is in a folder named `Counterexamples/HeckeCharacterExamples`, but the proof uses it as a main lemma.
