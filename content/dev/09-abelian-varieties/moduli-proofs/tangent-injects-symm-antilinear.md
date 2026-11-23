---
id: tangent-injects-symm-antilinear
title: Tangent vectors of a theta-level family inject into symmetric antilinear maps
kind: theorem
decl: GlobalTheory.KS.tangent_injects_symm_antilinear
module: Development.AbelianVarietyTheory.Proofs.ModuliProofs.TangentInjectsSymmetricAntilinearCommuting
covers: 404
status: drafted
drafted_by: writer@claude
---
This theorem sends each tangent vector of the base of a theta-level abelian scheme to a $g \times g$ complex matrix, which the Lean names call its Kodaira-Spencer class. The map is injective, and its values are symmetric and commute with the endomorphisms. Through its [statement form](/entry/tangent-injects-symmetric-antilinear-commuting/) it goes to [`finrank_derivation_le`](/entry/finrank-derivation-le/), which bounds the dimension of such matrices for a PEL family.

## Statement

Let $o$ be a ring with a unit $\zeta$ that is a primitive $k$-th root of unity in every field under $o$, and with $k$ invertible (`TBase`). A *theta-level object* $t$ over $S \to \operatorname{Spec} o$ (`TObj`) is an abelian scheme $A/S$ of relative dimension $g$ with a rigidified, symmetric, relatively ample line bundle $L$, sections $P_1, \dots, P_{2g}$ of order $k$ that form a basis of the $k$-torsion on each geometric fibre with Weil pairing given by $\zeta$ and the standard symplectic form, and endomorphisms $a_j$, $j \in J$. For $x \colon \operatorname{Spec} \mathbb{C}[\varepsilon] \to X$, let $x^{c}$ be the composite $\operatorname{Spec} \mathbb{C}[\varepsilon] \to \operatorname{Spec} \mathbb{C} \to \operatorname{Spec} \mathbb{C}[\varepsilon] \xrightarrow{x} X$ (`constPt`).

**Theorem.** Assume `Out.Laws` and `Out.Laws2` (bundles of facts on abelian schemes) and `ThetaUnifAV` (complex uniformisation of polarized abelian varieties with Appell-Humbert data). Let $R$ be an $o$-algebra with a point $R \to \mathbb{C}$, and $t$ a theta-level object over $\operatorname{Spec} R$. Assume: if $x \colon \operatorname{Spec} \mathbb{C}[\varepsilon] \to \operatorname{Spec} R$ and $x^c$ have the same image in $\operatorname{Spec} o$, and some $t'$ is a pullback of $t$ along both $x$ and $x^c$, then $x = x^c$. Then there are:

- the fibre $t_0$ of $t$ at $\operatorname{Spec} \mathbb{C} \to \operatorname{Spec} R$, with $m \colon A_0 \to A$;
- a uniformisation $e \colon \mathbb{C}^g \to A_0(\mathbb{C})$ with kernel a lattice $\Lambda$, a positive definite Hermitian matrix $H$ and a unitary character $\chi$ of $\Lambda$, with the conditions of `GoodU`;
- a $\mathbb{C}$-linear map $\kappa \colon \operatorname{Der}_o(R, \mathbb{C}) \to M_g(\mathbb{C})$,

such that $\kappa$ is injective and, for each $D$:

1. $H(\kappa(D)\bar z, w) = H(\kappa(D)\bar w, z)$ for all $z, w \in \mathbb{C}^g$ (`IsSymm`);
2. if $f$ is an endomorphism of $A$ over $R$, $f_0$ its restriction to $A_0$ and $F$ a linear map with $e(Fz) = f_0(e(z))$, then $F(\kappa(D)\bar z) = \kappa(D)\overline{Fz}$ (`Comm`).

The matrix $\kappa(D)$ is tied to $D$ by `KSRel`: a holomorphic family $s(z)$ of point derivations at $m(e(z))$ that lifts $D$ and satisfies $s(z + l)f = s(z)f + df_z(\kappa(D)\bar l)$ for $l \in \Lambda$. So $z \mapsto \kappa(D)\bar z$ is an antilinear map that records how the lattice moves along $D$.

## Proof

1. `T.exists_thetaLevelAbelianScheme_pullback` gives the fibre $t_0$ and $m$.
2. `T.exists_goodUniformisation_kodairaSpencer` gives $e$, $H$, $\chi$ with `GoodU`, from `ThetaUnifAV`.
3. `T.kodairaSpencer_matrix_linear_in_derivation` gives $\kappa$ and, for each $D$, a family $s$ with `KSRel`. It needs $A \to \operatorname{Spec} R$ smooth, which follows from the relative dimension.
4. Injectivity: if $\kappa(D) = 0$, then `T.derivation_eq_zero_of_kodairaSpencer_zero` gives $D = 0$. This step uses `Out.Laws`, `Out.Laws2`, `ThetaUnifAV` and the hypothesis on $x$ and $x^c$.
5. Symmetry: `T.kodairaSpencer_class_isSymm_of_lift`, with $L$ on $A$ that restricts to $L_0$.
6. Commutation: `T.kodairaSpencer_commutes_with_endomorphism`.

## In the Lean code

The theorem is in [TangentInjectsSymmetricAntilinearCommuting.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/TangentInjectsSymmetricAntilinearCommuting.lean#L21). `IsSymm`, `Comm`, `KSRel` and `GoodU` are in [IsSymm.lean](lean:Development/AbelianVarietyTheory/Definitions/ModuliSpaces/IsSymm.lean#L32), `TObj` and `TMap` in [GoodClass.lean](lean:Development/AbelianVarietyTheory/Definitions/ModuliSpaces/GoodClass.lean#L24), `constPt` in [PushInvertible.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/PushInvertible.lean#L26).

Each of the six lemmas is a statement form of a lemma in `KS`, `KSInh` or `GlobalTheory`. We have not opened those proofs. The hypothesis on $x$ and $x^c$ is used only in step 4. No PEL structure appears: $J$ and the $a_j$ are arbitrary. The parent adds it.
