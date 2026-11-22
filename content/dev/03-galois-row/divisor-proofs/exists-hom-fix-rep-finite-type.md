---
id: exists-hom-fix-rep-finite-type
title: Homomorphisms that respect polarizations, over an affine base, by gluing local schemes
kind: theorem
decl: GlobalTheory.HomFixAff.exists_homFixRep_finiteType
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsFiniteTypeSchemeRepresentingPolarizedHoms
covers: 401
status: drafted
drafted_by: writer@claude
---
This theorem shows that, over the spectrum of a noetherian ring, the homomorphisms between two abelian schemes that carry one polarization bundle to the other are represented by a scheme of finite type. It glues the local schemes of [the local representability](/entry/exists-local-representing-scheme-hom-fixed-pullback/). Its statement form is [the affine representability](/entry/exists-finite-type-scheme-representing-polarized-homs/), which goes into [the representability over a locally noetherian base](/entry/hom-fix-finite-type/).

## Statement

Let $R$ be a noetherian ring and $S = \operatorname{Spec} R$.

- An *abelian scheme* $A/S$ is a commutative group object in schemes over $S$ whose structure map is smooth, proper and geometrically connected (`IsAbelianScheme`).
- A *line bundle* $L$ on a scheme $X$ (`LB`, with `IsLB`) is an open cover $(U_i)$ of $X$ with units $g_{ij} \in \Gamma(U_i \cap U_j)^\times$ that satisfy $g_{ii} = 1$ and the cocycle condition. An isomorphism $L \cong L'$ is a nowhere vanishing section of $L' \otimes L^{-1}$, in the same chart form.
- $L$ on $A$ is *rigidified* if its pullback along the unit section $e \colon S \to A$ is trivial.
- $L$ is *relatively ample* (`Out.RelAmple`) if for each affine open $V \subseteq S$ there is $N \geq 1$ and sections $s_0, \dots, s_m$ of $L^{\otimes N}$ on $A_V$ whose nonvanishing loci are affine and cover $A_V$, and on each locus $\{s_i \neq 0\}$ the ratios $s_j / s_i$ generate the ring of functions over $\Gamma(V)$. So some power of $L$ is very ample over each affine open.

Let $A, B$ be abelian schemes over $S$ with rigidified relatively ample line bundles $L$ on $A$ and $M$ on $B$.

**Theorem.** There is a scheme $H$, a map $\pi \colon H \to S$ that is quasi-compact, separated and locally of finite type, base changes $A_H, B_H$ of $A, B$ as group schemes, and a homomorphism $\Phi \colon A_H \to B_H$ with $\Phi^* M_H \cong L_H$, with this property: for each $t \colon T \to S$, each pair of base changes $A_T, B_T$ and each homomorphism $\Phi' \colon A_T \to B_T$ with $\Phi'^* M_T \cong L_T$, there is a unique $h \colon T \to H$ over $S$ such that $A_T, B_T$ are base changes of $A_H, B_H$ along $h$ and $\Phi'$ is the base change of $\Phi$.

In the Lean code the data $(H, \pi, A_H, B_H, \Phi)$ with this property is the structure `HomFixRep A B L M`.

## Proof

1. For each point $p$ of $S$, [the local representability](/entry/exists-local-representing-scheme-hom-fixed-pullback/) gives an open $U_p \ni p$, base changes $A_{U_p}$, $B_{U_p}$, and a representing scheme for the pulled back data over $U_p$ that is quasi-compact, separated and locally of finite type.
2. The opens $U_p$ cover $S$. `GlobalTheory.T.homFixedPullbackRepresentable_glue_openCover` glues the local representing schemes along this cover into one over $S$ with the same three properties.

## In the Lean code

The theorem is in [ExistsFiniteTypeSchemeRepresentingPolarizedHoms.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsFiniteTypeSchemeRepresentingPolarizedHoms.lean#L15). The lemmas it calls:

- `GlobalTheory.T.exists_local_representing_scheme_homFixedPullback`.
- `GlobalTheory.T.homFixedPullbackRepresentable_glue_openCover`, in [HomFixedPullbackRepresentableGlueOpenCoverStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HomFixedPullbackRepresentableGlueOpenCoverStatement.lean#L11). It is a second name of `GlobalTheory.homFixRep_glue_opens`, whose proof we have not opened. It asks for a locally noetherian base, but not for relative ampleness.

`HomFixRep` is in [NonemptyHomFixRepTrivial.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/NonemptyHomFixRepTrivial.lean#L14). Its field `rep` asks for a unique $h$, and only for some maps $\psi_A, \psi_B$ that exhibit $A_T, B_T$ as base changes, not unique ones.
