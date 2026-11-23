---
id: plane-closure
title: Strong approximation for elements that fix the complement of a plane
kind: theorem
decl: GlobalTheory.PlaneSU.plane_closure
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.SpecialUnitaryFixingPlaneComplementMemClosure
covers: 306
status: drafted
drafted_by: writer@claude
---
This theorem proves strong approximation for the elements of a special unitary group that act only on a plane. It reduces them to norm-one elements of a quaternion algebra. Its second name [`T.specialUnitary_fixing_plane_complement_mem_closure`](/entry/special-unitary-fixing-plane-complement-mem-closure/) is one of the inputs of [strong approximation for a special unitary group](/entry/strong-approx-su/).

## Statement

Let $E/F$ be a CM extension of number fields with conjugation $\sigma$. Let $J$ be a nondegenerate Hermitian $M \times M$ matrix over $E$ and $h(x, y) = \sum_{i,j} \sigma(x_i) J_{ij} y_j$. Let $S = S_1 \cup S_2$ be a nonempty finite set of places of $F$ with idempotent $\varepsilon \in \mathbb{A}_F$. Let $SU(J)(F)$, $SU(J)(\mathbb{A}_F)$ and $SU(F_S)$ be as in [the parent](/entry/strong-approx-su/). Let $e_1, e_2 \in E^M$ with:

- $h(e_1, e_2) = 0$, $h(e_1, e_1) \neq 0$ and $h(e_2, e_2) \neq 0$;
- there is $t \in \mathbb{A}_F \otimes_F E$ with $\varepsilon \bigl(t \sigma(t) + h(e_1, e_1)/h(e_2, e_2)\bigr) = 0$. So $-h(e_1, e_1)/h(e_2, e_2)$ is a norm from $E_v$ at each $v \in S$.

**Theorem.** Let $g \in SU(J)(\mathbb{A}_F)$ fix each $v \in E^M$ with $h(e_1, v) = h(e_2, v) = 0$. Then $g$ lies in the closure of $SU(J)(F) \cdot SU(F_S)$.

## Proof

1. `T.orthogonalAnisotropicPair_planeMatrices_facts`: the matrix $A$ with columns $e_1, e_2$ and $B = \operatorname{diag}(h(e_i, e_i)^{-1}) A^* J$ satisfy $BA = 1$. The restriction of $h$ to the plane is $H = \operatorname{diag}(f_1, f_2)$ with $f_i \in F^\times$ (`CMConjInvol.cm_conj_invol_fixed`).
2. `QuadNormBase.exists_basis`: $E = F(\theta)$ with $\theta^2 = \delta \in F$ and $\sigma(\theta) = -\theta$.
3. `T.matrix_fixes_lowRankProjector_of_fixes_rationalKernel` and `T.unitary_fixing_kernel_eq_oneAddLowRank_of_unitary`: since $g$ fixes the complement, $g = 1 + A(X - 1)B$ with $X = BgA$, and $X$ is unitary for $H$. Also $\det X = 1$.
4. `T.exists_quaternionMatrix_eq_of_unitary_det_one`: $X$ is the matrix of an element $x$ of norm $1$ in the quaternion algebra $D = (\delta, -f_2/f_1)$ over $\mathbb{A}_F$.
5. `T.neg_inv_ratio_isNorm_of_neg_ratio_isNorm`: the norm hypothesis gives $p, q \in \mathbb{A}_F$ with $\varepsilon\bigl(-f_2/f_1 - (p^2 - \delta q^2)\bigr) = 0$, so $D$ splits at each place of $S$.
6. `T.strongApproximation_quaternion_normOne_split`: $x$ lies in the closure of the set $H_0$ of products $\gamma h$ with $\gamma \in D(F)$ of norm $1$ and $h$ of norm $1$ with $\varepsilon(h - 1) = h - 1$.
7. The map $\Phi \colon y \mapsto 1 + A(X_y - 1)B$ from norm-one elements of $D$ to $SU(J)(\mathbb{A}_F)$ is a continuous homomorphism (`T.continuous_oneAddLowRankEmbedding_quaternionMatrix`, `emb_mul`). It sends $H_0$ into $SU(J)(F) \cdot SU(F_S)$ and $x$ to $g$. So $g$ lies in the closure.

Step 6 has the form of strong approximation for $SL_1(D)$ with respect to $S$, which holds when $D_v$ is not a division algebra at some $v \in S$ (Platonov and Rapinchuk, Algebraic Groups and Number Theory, chapter 7). We did not open the proofs of the `T.` lemmas.

## In the Lean code

The theorem is at [SpecialUnitaryFixingPlaneComplementMemClosure.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SpecialUnitaryFixingPlaneComplementMemClosure.lean#L19). The maps `emb` and `qm` and the matrices `planeA`, `planeB`, `planeH` are in [EmbUnitary.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/EmbUnitary.lean#L20). The set `H0` is in [OneMemH0WeightZero.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/OneMemH0WeightZero.lean#L30).

The norm condition is asked at every place of $S$. Strong approximation for $SL_1(D)$ needs only one place of $S$ where $D$ splits, so this hypothesis is stronger than needed. [The parent](/entry/strong-approx-su/) gets it from `T.exists_isotropic_places_alt`, which shrinks $S$ to a nonempty subset.
