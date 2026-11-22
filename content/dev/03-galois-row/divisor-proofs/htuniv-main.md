---
id: htuniv-main
title: The universal first-order deformation of a Harris-Taylor object
kind: theorem
decl: GlobalTheory.HTUniv.main
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsUniversalFirstOrderDeformationHarrisTaylor
covers: 313
status: drafted
drafted_by: writer@claude
---
This theorem builds a universal first-order deformation of an object of the Harris-Taylor moduli problem over an algebraically closed field, with $a(n-1)$ parameters. It does so with the Hodge filtration: a deformation over the dual numbers is fixed by the lift of the Hodge filtration that it gives. [Its statement form](/entry/exists-universal-first-order-deformation-harris-taylor/) repeats it, and [the tangent space entry](/entry/exists-univ-tangent/) moves it to a representing family.

## Statement

The statement is that of [the statement form](/entry/exists-universal-first-order-deformation-harris-taylor/): for $N \geq 3$ prime to $p$ and an object $o_0$ over $\operatorname{Spec} k$ with $k$ algebraically closed, there is $o$ over $k[V]$, $V = k^d$, $d = a(n-1)$, that restricts to $o_0$, such that each deformation $o'$ of $o_0$ over $k[\varepsilon]$ maps to $o$ over $\operatorname{Spec}(\mathrm{id} \oplus c)$ for a unique linear $c \colon V \to k$.

We need three objects. Let $A_0$ be the abelian variety of $o_0$. $H(A_0)$ (`HdR`) is the $k$-dual of the primitive classes in $H^1_{\mathrm{dR}}(A_0)$, and $\mathrm{Fil} \subseteq H(A_0)$ is the annihilator of the primitive part of the Hodge filtration $F^1$. For a deformation $A'$ of $A_0$ over $k[\varepsilon]$, $x \in \mathrm{Fil}$ and $y \in H(A_0)$, the relation `IsFilLift` says: some class of the crystal of $A_0$ on $k[\varepsilon]$ lies in the filtration of $A'$ and equals $x + \varepsilon y$. So $x \mapsto y$ describes how the filtration of $A'$ moves away from that of the constant deformation.

## Proof

1. `harrisTaylor_firstOrder_deformations_basis_count` gives linear maps $f_1, \dots, f_d \colon H(A_0) \to H(A_0)$. Each $f_j$ is the filtration lift of some deformation. For each deformation $o'$ there are unique $c_1, \dots, c_d \in k$ such that $\sum_j c_j f_j$ is the filtration lift of $o'$.
2. `harrisTaylor_exists_glued_firstOrder_deformation` glues these into one object $o$ over $k[V]$ whose filtration lift is $x \mapsto (f_1 x, \dots, f_d x) \in V$.
3. `harrisTaylor_hodgeFiltration_naturality`: if $o'$ maps to $o$ over $\operatorname{Spec}(\mathrm{id} \oplus c)$, then the filtration lift of $o'$ is $c$ composed with that of $o$, that is, $\sum_j c(e_j) f_j$ (`comp_pi`).
4. Existence. Let $o'$ be a deformation, with coefficients $c_j$ from step 1. Let $c = \sum_j c_j \pi_j$. Pull $o$ back along $\operatorname{Spec}(\mathrm{id} \oplus c)$ to $o_c$. By step 3, $o_c$ has filtration lift $\sum_j c_j f_j$, the same as $o'$. Then `harrisTaylor_firstOrder_iso_of_same_hodge_filtration` gives an isomorphism $o' \cong o_c$ over the identity, and $o' \to o_c \to o$ is the map.
5. Uniqueness. If $o' \to o$ over $c'$, step 3 makes $\sum_j c'(e_j) f_j$ the filtration lift of $o'$. The uniqueness in step 1 gives $c'(e_j) = c_j$ for each $j$, so $c' = c$ (`coord`).

Steps 1 and 4 have the form of Grothendieck-Messing theory (W. Messing, Lecture Notes in Math. 264, 1972): deformations over a square-zero thickening match lifts of the Hodge filtration. We have not checked how closely the Lean lemmas follow it.

## In the Lean code

The theorem is in [ExistsUniversalFirstOrderDeformationHarrisTaylor.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsUniversalFirstOrderDeformationHarrisTaylor.lean#L15). `HdR`, `Fil` and `IsFilLift` are in [IsKSValueOneOfRetraction.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsKSValueOneOfRetraction.lean#L343), and `IsFilLiftV` (the version over $k[V]$), `coord`, `comp_pi` and `sum_proj_single` in [SumProjSingle.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SumProjSingle.lean#L35). The four lemmas of steps 1 to 4 are aliases of `HTCount.count`, `HTGlue.exists_glue`, `HTUniv.Nat.main` and `HTFirstOrderIso.objMap_of_filLift`. We have not opened their proofs. The count $d = a(n-1)$ is the content of `HTCount.count`. The proof also uses `exists_harrisTaylorObject_pullback_along` and `harris_taylor_object_maps_compose_cancel` for pullbacks and composition of maps of objects.
