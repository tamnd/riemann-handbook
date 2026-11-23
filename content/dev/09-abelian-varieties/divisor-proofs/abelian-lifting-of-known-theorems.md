---
id: abelian-lifting-of-known-theorems
title: Lifting of abelian schemes from five structural inputs
kind: theorem
decl: GlobalTheory.SqLift.abelianLifting_of_known_theorems
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.AbelianSchemeHomLiftingNilDPOfFiveStatements
covers: 303
status: drafted
drafted_by: writer@claude
---
This theorem is a pass-through. It turns five inputs on abelian schemes into the three inputs of `abelianLifting_of_schemeLifts`, which proves the lifting statement `AbelianLifting`. Its statement form is [`abelianSchemeHomLiftingNilDP_of_hodge_cube_duality_unobstructed`](/entry/abelian-scheme-hom-lifting-nil-dp-of-hodge-cube-duality-unobstructed/), and the result goes to [the lifting theorem](/entry/abelian-scheme-hom-lifting-nilpotent-divided-powers/).

## Statement

**Theorem.** `AbelianHodgeDeRham`, `CubeTheorem`, `DualAbelianScheme`, `PoincareDeRhamDuality` and `AbelianUnobstructed` together imply `AbelianLifting`.

The five inputs are stated in [`abelianLifting_of_four`](/entry/abelian-lifting-of-four/), and `AbelianLifting` in [the lifting theorem](/entry/abelian-scheme-hom-lifting-nilpotent-divided-powers/).

## Proof

The proof is one term. `abelianSchemeDeRhamStructure_of_cube_dual_poincare` turns the first four inputs into `AbelianDeRham`, a list of five facts on the de Rham cohomology of abelian schemes. `abelianSchemeSquareZeroLifts_of_deRhamCohomology` turns `AbelianHodgeDeRham` into `AbelianSchemeLifts`: over a Noetherian ring with a square-zero ideal, smooth lifts of an abelian scheme correspond, up to isomorphism, to admissible filtrations. These two facts and `AbelianUnobstructed` go to `abelianLifting_of_schemeLifts`. There is nothing else.

The real content is in `abelianLifting_of_schemeLifts`, which has no entry. It first proves the square-zero case, with the trivial divided powers, from the Noetherian case (`squareZeroLifting_of_noetherian_case`). Then it inducts on the nilpotence exponent $N$ of the divided powers. For $N = 1$ the ideal is zero. For the step, `exists_isStep_nilExp` factors $R \to R_0$ as $R \to R_1 \to R_0$, with a square-zero kernel $J$ for the first map and exponent $N$ for the second. `liftAbelianScheme_along_squareZero_factorization` and `liftHom_of_isStep` then combine the two cases.

## In the Lean code

The theorem is at [AbelianSchemeHomLiftingNilDPOfFiveStatements.lean#L14](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/AbelianSchemeHomLiftingNilDPOfFiveStatements.lean#L14). The induction is in [AbelianLiftingOfDeRhamUnobstructed.lean#L49](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/AbelianLiftingOfDeRhamUnobstructed.lean#L49). The cube input is used only through `abelianSchemeDeRhamStructure_of_cube_dual_poincare`. We have not unfolded that lemma or the two step lemmas.
