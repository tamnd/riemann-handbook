---
id: exists-local-representing-scheme-hom-fixed-pullback
title: Homomorphisms that respect polarizations form a scheme near each point of the base
kind: theorem
decl: GlobalTheory.T.exists_local_representing_scheme_homFixedPullback
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsLocalRepresentingSchemeHomFixedPullbackStatement
covers: 398
status: drafted
drafted_by: writer@claude
---
This theorem is the statement form of [the local representability on a basic open](/entry/exists-local-hom-fix-rep/). It is a second name of that theorem, with the same statement. [The representability over an affine base](/entry/exists-hom-fix-rep-finite-type/) applies it at each point and glues the results.

## Statement

Use the abelian schemes $A, B$ over $S = \operatorname{Spec} R$, $R$ noetherian, and the rigidified relatively ample line bundles $L$ on $A$ and $M$ on $B$, of [the affine theorem](/entry/exists-hom-fix-rep-finite-type/).

**Theorem.** For each point $p$ of $S$ there is an open $U \ni p$ and base changes $A_U, B_U$ of $A, B$ to $U$ as group schemes, with maps $\varphi_A \colon A_U \to A$ and $\varphi_B \colon B_U \to B$, such that the homomorphisms $A_U \to B_U$ that carry $\varphi_B^* M$ to $\varphi_A^* L$ are represented by a scheme $H \to U$ that is quasi-compact, separated and locally of finite type.

"Represented" has the meaning of the structure `HomFixRep`, as in the affine theorem, with $U$ in place of $S$.

## Proof

The proof is `exact GlobalTheory.HomFixLocal.exists_local_homFixRep`. The real content is in that theorem and below it.

## In the Lean code

The theorem is in [ExistsLocalRepresentingSchemeHomFixedPullbackStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsLocalRepresentingSchemeHomFixedPullbackStatement.lean#L11). The proof is a `first | exact … | …` combinator that closes the goal with the theorem of the same statement. The open $U$ is a subscheme of $\operatorname{Spec} R$ through `(U).toScheme`, with the inclusion `(U).ι`. The theorem states only that $U$ is open; its proof gives a basic open $D(f)$.
