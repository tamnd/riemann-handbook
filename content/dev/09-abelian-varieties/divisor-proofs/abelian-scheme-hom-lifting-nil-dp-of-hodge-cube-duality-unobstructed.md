---
id: abelian-scheme-hom-lifting-nil-dp-of-hodge-cube-duality-unobstructed
title: Lifting of abelian schemes from five structural inputs, statement form
kind: theorem
decl: GlobalTheory.T.abelianSchemeHomLiftingNilDP_of_hodge_cube_duality_unobstructed
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.AbelianSchemeHomLiftingNilDPOfFiveStatementsStatement
covers: 304
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [`abelianLifting_of_known_theorems`](/entry/abelian-lifting-of-known-theorems/). It has the same statement and no proof of its own. Its only caller is [`abelianLifting_of_four`](/entry/abelian-lifting-of-four/), which supplies the theorem of the cube.

## Statement

**Theorem.** Assume five statements about abelian schemes: the de Rham and Hodge structure (`AbelianHodgeDeRham`), the theorem of the cube over any base (`CubeTheorem`), the existence of the dual (`DualAbelianScheme`), the perfect de Rham pairing with an isotropic Hodge filtration (`PoincareDeRhamDuality`), and square-zero unobstructedness (`AbelianUnobstructed`). Then `AbelianLifting` holds: over a nilpotent divided power thickening, abelian schemes lift with any admissible Hodge filtration, and homomorphisms that respect the filtrations lift uniquely.

The four inputs other than the cube are stated in [`abelianLifting_of_four`](/entry/abelian-lifting-of-four/), and `AbelianLifting` in [the lifting theorem](/entry/abelian-scheme-hom-lifting-nilpotent-divided-powers/).

## Proof

The proof is the term `abelianLifting_of_known_theorems`. There is nothing else.

## In the Lean code

The theorem is at [AbelianSchemeHomLiftingNilDPOfFiveStatementsStatement.lean#L12](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/AbelianSchemeHomLiftingNilDPOfFiveStatementsStatement.lean#L12). The proof is the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)`, with `maxHeartbeats` set to 1,000,000. The two statements have the same type.
