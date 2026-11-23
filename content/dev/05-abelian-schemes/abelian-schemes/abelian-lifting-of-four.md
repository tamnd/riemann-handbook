---
id: abelian-lifting-of-four
title: Lifting of abelian schemes from four structural inputs
kind: theorem
decl: GlobalTheory.LiftFour.abelianLifting_of_four
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.AbelianLiftingOfFour
covers: 305
status: drafted
drafted_by: writer@claude
---
This theorem is a pass-through. It reduces the lifting theorem [`abelianScheme_hom_lifting_nilpotent_dividedPowers`](/entry/abelian-scheme-hom-lifting-nilpotent-divided-powers/) from five inputs to four, because it supplies the theorem of the cube itself. The real content is in `abelianLifting_of_schemeLifts`, which [`abelianLifting_of_known_theorems`](/entry/abelian-lifting-of-known-theorems/) calls.

## Statement

**Theorem.** Assume the following four statements about abelian schemes:

1. `AbelianHodgeDeRham`: $H^1_{\mathrm{dR}}$ is projective of rank $2g$, cup product gives $\wedge^2 H^1_{\mathrm{dR}} \cong H^2_{\mathrm{dR}}$, global $1$-forms and $H^1(\mathcal{O})$ are projective of rank $g$, and these facts commute with base change;
2. `DualAbelianScheme`: every abelian scheme has a dual of the same dimension, and the duality goes both ways;
3. `PoincareDeRhamDuality`: the de Rham pairing between $A$ and its dual is perfect, and the Hodge filtration is isotropic;
4. `AbelianUnobstructed`: over a square-zero thickening $R \to R/I$, every abelian scheme over $R/I$ lifts to one over $R$.

Then `AbelianLifting` holds, as stated in [the parent entry](/entry/abelian-scheme-hom-lifting-nilpotent-divided-powers/).

## Proof

The proof is the term `abelianSchemeHomLiftingNilDP_of_hodge_cube_duality_unobstructed a cube c d e`. The second argument is `theoremOfCubeAbelianScheme_over_arbitrary_base`. It says: let $A$ be an abelian scheme over any base $S$, $L$ a line bundle on $A$, and $a, b, c \in A(T)$ for an $S$-scheme $T$. Then the bundle $(a+b+c)^*L \otimes (a+b)^*L^{-1} \otimes (a+c)^*L^{-1} \otimes (b+c)^*L^{-1} \otimes a^*L \otimes b^*L \otimes c^*L \otimes 0^*L^{-1}$ on $T$ is trivial. This is the theorem of the cube (Mumford, *Abelian Varieties*, §6 and §10, over a field). There is nothing else.

## In the Lean code

The theorem is at [AbelianLiftingOfFour.lean#L15](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/AbelianLiftingOfFour.lean#L15). Its only caller is the parent theorem. The four hypotheses are passed on unchanged to [`abelianSchemeHomLiftingNilDP_of_hodge_cube_duality_unobstructed`](/entry/abelian-scheme-hom-lifting-nil-dp-of-hodge-cube-duality-unobstructed/).
