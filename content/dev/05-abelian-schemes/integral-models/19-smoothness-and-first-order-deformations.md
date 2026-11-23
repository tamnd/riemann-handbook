---
title: Smoothness and first-order deformations
decls:
  - GlobalTheory.T.harrisTaylor_firstOrder_deformations_basis_count
  - GlobalTheory.HTUniv.main
  - GlobalTheory.T.exists_universal_firstOrder_deformation_harrisTaylor
  - GlobalTheory.UPel.HT.RepTangent.exists_univ_tangent
  - GlobalTheory.T.exists_universal_tangent_harrisTaylor_representingFamily
  - GlobalTheory.UPel.HT.RepFam.smoothOfRelativeDimension
  - GlobalTheory.T.smoothOfRelativeDimension_repFam_of_isQProjOver
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Smoothness and first-order deformations

This section proves result 4 of Section 8.1: over a noetherian ring, a representing family of level $N \geq 3$, with $N$ prime to $p$, whose map to $\operatorname{Spec} R$ is quasi-projective, is [[smooth|EXKGG9X6J0]] of relative dimension $a(n - 1)$. With the previous section, this gives models in the sense of Definition 8.1.4. Smoothness comes from lifting objects along square-zero extensions of local Artinian rings. The dimension comes from the tangent spaces. An object over an algebraically closed field has a universal first-order deformation with $a(n - 1)$ parameters. Its construction uses the Hodge filtration in de Rham cohomology, in the style of [[deformation theory|H8AAQJ1SZW]] for abelian schemes.

Throughout, $D$ is a datum for $p$, $b$ is a base for $D$ over a ring $R$, and $N \geq 3$ is an integer prime to $p$. Put $d = a(n - 1)$. Let $k$ be an algebraically closed field. For a $k$-vector space $V$, let $k[V] = k \oplus V$ with $V^2 = 0$, so $k[\varepsilon] = k[k]$ is the ring of dual numbers. Let $\iota : k \to k[V]$ be the inclusion and $\pi_0 : k[V] \to k$ the first projection. A linear map $c : V \to k$ gives the ring map $c_* : k[V] \to k[\varepsilon]$, $\alpha + v \mapsto \alpha + c(v)\varepsilon$. For $t : \operatorname{Spec} k \to \operatorname{Spec} R$, a *deformation* of an object $o_0$ of level $N$ over $t$ to $k[V]$ is an object $o$ over $t \circ \operatorname{Spec} \iota$ with a map of objects $o_0 \to o$ over $\operatorname{Spec} \pi_0$ (Definition 8.1.3).

### Filtration lifts

Let $A_0$ be an abelian variety over $k$. Let $H(A_0)$ be the $k$-dual of the space of primitive classes in the first [[algebraic de Rham cohomology|13F5JZPDD0]] of $A_0$. Let $\operatorname{Fil}(A_0) \subseteq H(A_0)$ be the annihilator of the primitive classes in the Hodge filtration $F^1$.

**Definition 8.19.1 (Filtration lift).** Let $A$ be an abelian scheme over $k[V]$ with an identification of $A_0$ with $A \times_{k[V]} \operatorname{Spec} k$ along $\pi_0$. Let $x \in H(A_0)$ and let $y$ be a linear map from the primitive classes of $A_0$ to $V$. Then $y$ is a *filtration lift* of $x$ for $A$ if some element $\delta$ of the crystal of $A_0$ on the thickening $k[V] \to k$ has these properties. The image of $\delta$ in the de Rham space of $A$ lies in the filtration of $A$, and $\delta$ takes the value $x(\gamma) + y(\gamma)$ in $k[V]$ on the constant extension of each primitive class $\gamma$. For $V = k$, we regard $y$ as an element of $H(A_0)$.

Lean: `GlobalTheory.DeRham.IsFilLift` for $V = k$, and `GlobalTheory.FODef.IsFilLiftV` for general $V$.

For a deformation $o$ of $o_0$, we use the filtration lift of the abelian scheme of $o$, through the map $o_0 \to o$.

### Inputs

We use the following results. Let $o_0$ be an object of level $N$ over $t : \operatorname{Spec} k \to \operatorname{Spec} R$, and let $A_0$ be its abelian variety.

1. (Pullback.) Let $o$ be an object over $s : S \to \operatorname{Spec} R$ and $f : S' \to S$. Then for every $s'$ with $s f = s'$ there is an object $o'$ over $s'$ with a map of objects $o' \to o$ over $f$.
2. (Composition and cancellation.) Let $o_i$ be objects over $s_i : S_i \to \operatorname{Spec} R$ for $i = 1, 2, 3$, and let $f : S_1 \to S_2$ and $g : S_2 \to S_3$. If maps $o_1 \to o_2$ over $f$ and $o_2 \to o_3$ over $g$ exist, then a map $o_1 \to o_3$ over $g f$ exists. If maps $o_1 \to o_3$ over $g f$ and $o_2 \to o_3$ over $g$ exist, then a map $o_1 \to o_2$ over $f$ exists.
3. (Gluing.) Let $f_1, \dots, f_d : H(A_0) \to H(A_0)$ be linear. Suppose that for each $j$ there is a deformation of $o_0$ to $k[\varepsilon]$ for which $f_j x$ is a filtration lift of $x$, for every $x \in \operatorname{Fil}(A_0)$. Then there is a deformation of $o_0$ to $k[k^d]$ for which $(f_1 x, \dots, f_d x)$ is a filtration lift of $x$, for every $x \in \operatorname{Fil}(A_0)$. This is a second name of the theorem in [a later section](/entry/htglue-exists-glue/).
4. (Naturality.) Let $o$ be a deformation of $o_0$ to $k[k^d]$, and $o'$ a deformation of $o_0$ to $k[\varepsilon]$, over any maps to $\operatorname{Spec} R$. Let $c : k^d \to k$ be linear, and suppose that a map of objects $o' \to o$ over $\operatorname{Spec} c_*$ exists. If $y$ is a filtration lift of $x$ for $o$, then $c \circ y$ is a filtration lift of $x$ for $o'$.
5. (Equal lifts give isomorphic objects.) Let $o_1$ and $o_2$ be deformations of $o_0$ to $k[\varepsilon]$, and $g : H(A_0) \to H(A_0)$ a map such that $g x$ is a filtration lift of $x$ for both $o_1$ and $o_2$, for every $x \in \operatorname{Fil}(A_0)$. Then a map of objects $o_1 \to o_2$ over the identity exists.
6. (Square-zero lifting.) Let $C$ be a local Artinian ring, $\pi : C \to C_0$ a surjection with $(\ker \pi)^2 = 0$, and $\beta : R \to C$. Then every object over $\operatorname{Spec}(\pi \beta)$ has a map over $\operatorname{Spec} \pi$ to some object over $\operatorname{Spec} \beta$.
7. (A lifting test for smoothness.) Let $B$ be a [[noetherian|0670T59HGE]] ring and $s : X \to \operatorname{Spec} B$ [[locally of finite type|AHTE5DVX61]]. Suppose that for every local Artinian ring $C$, every surjection $\pi : C \to C_0$ with $(\ker \pi)^2 = 0$, every $t : \operatorname{Spec} C \to \operatorname{Spec} B$ and every $x_0 : \operatorname{Spec} C_0 \to X$ with $s x_0 = t \circ \operatorname{Spec} \pi$, there is $x : \operatorname{Spec} C \to X$ with $x \circ \operatorname{Spec} \pi = x_0$ and $s x = t$. Then $s$ is smooth.
8. (Dimension from tangents.) Let $B$ be a ring, $s : X \to \operatorname{Spec} B$ smooth and $d \geq 0$. Suppose that for every algebraically closed field $k$ and every $x : \operatorname{Spec} k \to X$ there is $u : \operatorname{Spec} k[k^d] \to X$ with $u \circ \operatorname{Spec} \pi_0 = x$ and $s u = s x \circ \operatorname{Spec} \iota$, such that every $v : \operatorname{Spec} k[\varepsilon] \to X$ with $v \circ \operatorname{Spec} \pi_0 = x$ and $s v = s x \circ \operatorname{Spec} \iota$ is $u \circ \operatorname{Spec} c_*$ for a unique linear $c : k^d \to k$. Then $s$ is smooth of relative dimension $d$.

Results 3, 4 and 5 say that, to first order, an object is fixed by the lift of its Hodge filtration. This is the shape of Grothendieck-Messing theory (W. Messing, Lecture Notes in Math. 264, 1972). We have not compared the Lean statements with it.

### The universal first-order deformation

**Theorem 8.19.2 (A basis of first-order deformations).** Let $o_0$ be an object of level $N$ over $t : \operatorname{Spec} k \to \operatorname{Spec} R$, with abelian variety $A_0$. Then there are linear maps $f_1, \dots, f_d : H(A_0) \to H(A_0)$ with two properties. For each $j$ there is a deformation of $o_0$ to $k[\varepsilon]$ for which $f_j x$ is a filtration lift of $x$, for every $x \in \operatorname{Fil}(A_0)$. For every deformation $o'$ of $o_0$ to $k[\varepsilon]$ there are unique $c_1, \dots, c_d \in k$ such that $\sum_j c_j f_j x$ is a filtration lift of $x$ for $o'$, for every $x \in \operatorname{Fil}(A_0)$.

Lean: `GlobalTheory.T.harrisTaylor_firstOrder_deformations_basis_count`.

*Proof.* This is a second name of the theorem proved in [a later section](/entry/htcount-count/). $\square$

**Theorem 8.19.3 (Universal first-order deformation).** Let $o_0$ be an object of level $N$ over $t : \operatorname{Spec} k \to \operatorname{Spec} R$. Then there is a deformation $o$ of $o_0$ to $k[k^d]$ with this property. For every deformation $o'$ of $o_0$ to $k[\varepsilon]$ there is a unique linear $c : k^d \to k$ such that a map of objects $o' \to o$ over $\operatorname{Spec} c_*$ exists.

Lean: `GlobalTheory.HTUniv.main` (also `GlobalTheory.T.exists_universal_firstOrder_deformation_harrisTaylor`, a second name).

*Proof.* The previous theorem gives $f_1, \dots, f_d$. Result 3 gives a deformation $o$ of $o_0$ to $k[k^d]$ for which $(f_1 x, \dots, f_d x)$ is a filtration lift of $x$, for every $x \in \operatorname{Fil}(A_0)$. Let $e_1, \dots, e_d$ be the standard basis of $k^d$.

First we show a claim. Let $o''$ be a deformation of $o_0$ to $k[\varepsilon]$, and let $c : k^d \to k$ be linear with a map $o'' \to o$ over $\operatorname{Spec} c_*$. Then $\sum_j c(e_j) f_j x$ is a filtration lift of $x$ for $o''$, for every $x \in \operatorname{Fil}(A_0)$. Indeed, result 4 shows that $c \circ (f_1 x, \dots, f_d x)$ is a filtration lift of $x$ for $o''$, and this map is $\sum_j c(e_j) f_j x$.

Existence. Let $o'$ be a deformation of $o_0$ to $k[\varepsilon]$. The previous theorem gives unique $c_1, \dots, c_d$ such that $\sum_j c_j f_j x$ is a filtration lift of $x$ for $o'$. Let $c = \sum_j c_j \operatorname{pr}_j$, so $c(e_j) = c_j$. As $c_* \iota = \iota$, result 1 gives an object $o_c$ over $t \circ \operatorname{Spec} \iota$ with a map $o_c \to o$ over $\operatorname{Spec} c_*$. As $\pi_0 c_* = \pi_0$, the map $o_0 \to o$ lies over $\operatorname{Spec} c_* \circ \operatorname{Spec} \pi_0$. The cancellation in result 2 gives a map $o_0 \to o_c$ over $\operatorname{Spec} \pi_0$, so $o_c$ is a deformation of $o_0$. By the claim, $\sum_j c_j f_j x$ is a filtration lift of $x$ for $o_c$. Result 5, for $g = \sum_j c_j f_j$, gives a map $o' \to o_c$ over the identity. Composition in result 2 gives a map $o' \to o$ over $\operatorname{Spec} c_*$.

Uniqueness. Let $c'$ be linear with a map $o' \to o$ over $\operatorname{Spec} c'_*$. By the claim, $\sum_j c'(e_j) f_j x$ is a filtration lift of $x$ for $o'$. The uniqueness in the previous theorem gives $c'(e_j) = c_j$ for every $j$. Two linear forms on $k^d$ that agree on the standard basis are equal, so $c' = c$. $\square$

### Tangent spaces and smoothness

**Theorem 8.19.4 (Universal tangent).** Let $R$ be noetherian, and let $(X, s, u_X)$ be a representing family of level $N$ over $b$ (Definition 8.1.4) such that $s$ is quasi-projective and smooth. Let $x : \operatorname{Spec} k \to X$. Then there is $u : \operatorname{Spec} k[k^d] \to X$ with $u \circ \operatorname{Spec} \pi_0 = x$ and $s u = s x \circ \operatorname{Spec} \iota$ with this property. Every $v : \operatorname{Spec} k[\varepsilon] \to X$ with $v \circ \operatorname{Spec} \pi_0 = x$ and $s v = s x \circ \operatorname{Spec} \iota$ is $u \circ \operatorname{Spec} c_*$ for a unique linear $c : k^d \to k$.

Lean: `GlobalTheory.UPel.HT.RepTangent.exists_univ_tangent` (also `GlobalTheory.T.exists_universal_tangent_harrisTaylor_representingFamily`, a second name).

*Proof.* By result 1 there is an object $o_0$ over $s x$ with a map $o_0 \to u_X$ over $x$. The previous theorem, for $t = s x$, gives a deformation $o$ of $o_0$ to $k[k^d]$. The representing property gives $u : \operatorname{Spec} k[k^d] \to X$ with $s u = s x \circ \operatorname{Spec} \iota$ and a map $o \to u_X$ over $u$.

As $\pi_0 \iota = \operatorname{id}_k$, we have $s \circ u \circ \operatorname{Spec} \pi_0 = s x$. Composition gives a map $o_0 \to u_X$ over $u \circ \operatorname{Spec} \pi_0$. As $x$ has the same two properties, the uniqueness in the representing property gives $u \circ \operatorname{Spec} \pi_0 = x$.

Let $v$ be as in the statement. By result 1 there is an object $o'$ over $s v = s x \circ \operatorname{Spec} \iota$ with a map $o' \to u_X$ over $v$. The map $o_0 \to u_X$ lies over $x = v \circ \operatorname{Spec} \pi_0$. Cancellation in result 2 gives a map $o_0 \to o'$ over $\operatorname{Spec} \pi_0$, so $o'$ is a deformation of $o_0$. The previous theorem gives a unique $c$ with a map $o' \to o$ over $\operatorname{Spec} c_*$.

As $c_* \iota = \iota$, we have $s \circ u \circ \operatorname{Spec} c_* = s v$. Composition gives a map $o' \to u_X$ over $u \circ \operatorname{Spec} c_*$. As $v$ has the same two properties, the uniqueness in the representing property gives $v = u \circ \operatorname{Spec} c_*$.

Let $c'$ be linear with $v = u \circ \operatorname{Spec} c'_*$. Then the map $o' \to u_X$ lies over $u \circ \operatorname{Spec} c'_*$, and $o \to u_X$ lies over $u$. Cancellation in result 2 gives a map $o' \to o$ over $\operatorname{Spec} c'_*$. The uniqueness in the previous theorem gives $c' = c$. $\square$

**Theorem 8.19.5 (Smoothness of a representing family).** Let $R$ be noetherian, and let $(X, s, u_X)$ be a representing family of level $N$ over $b$ such that $s$ is quasi-projective. Then $s$ is smooth of relative dimension $a(n - 1)$.

Lean: `GlobalTheory.UPel.HT.RepFam.smoothOfRelativeDimension` (also `GlobalTheory.T.smoothOfRelativeDimension_repFam_of_isQProjOver`, a second name).

*Proof.* By definition, $s$ is a quasi-compact immersion into a projective space $\mathbb{P}^m_R$, followed by the [[proper|9537RKBZPP]] map $\mathbb{P}^m_R \to \operatorname{Spec} R$. Both maps are locally of finite type, so $s$ is locally of finite type.

Smoothness. We apply result 7. Let $C$, $\pi : C \to C_0$, $t$ and $x_0$ be as there. A map of affine schemes is the spectrum of a ring map, so $t = \operatorname{Spec} \beta$ for some $\beta : R \to C$. Then $s x_0 = \operatorname{Spec}(\pi \beta)$. By result 1 there is an object $o_0$ over $\operatorname{Spec}(\pi \beta)$ with a map $o_0 \to u_X$ over $x_0$. Result 6 gives an object $o'$ over $\operatorname{Spec} \beta$ with a map $o_0 \to o'$ over $\operatorname{Spec} \pi$. The representing property gives $x : \operatorname{Spec} C \to X$ with $s x = t$ and a map $o' \to u_X$ over $x$. Composition gives a map $o_0 \to u_X$ over $x \circ \operatorname{Spec} \pi$, and $s \circ x \circ \operatorname{Spec} \pi = \operatorname{Spec}(\pi \beta)$. As $x_0$ has the same two properties, uniqueness gives $x \circ \operatorname{Spec} \pi = x_0$. So $s$ is smooth.

Relative dimension. Now $s$ is smooth and quasi-projective, and $R$ is noetherian. The universal tangent theorem gives, at each geometric point of $X$, the map $u$ that result 8 asks for, with $d = a(n - 1)$. Result 8 shows that $s$ is smooth of relative dimension $a(n - 1)$. $\square$

**Remark 8.19.6 (Formalization).** The first theorem is a wrapper that tries three forms of one proof term under a raised heartbeat limit: [HarrisTaylorFirstOrderDeformationsBasisCountStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HarrisTaylorFirstOrderDeformationsBasisCountStatement.lean#L10). The universal deformation is in [ExistsUniversalFirstOrderDeformationHarrisTaylor.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsUniversalFirstOrderDeformationHarrisTaylor.lean#L15). The universal tangent is in [ExistsUniversalTangentHarrisTaylorRepresentingFa.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsUniversalTangentHarrisTaylorRepresentingFa.lean#L21). Its hypotheses that $R$ is noetherian and that $s$ is quasi-projective and smooth are not used. The file of its second name imports Mathlib twice: [ExistsUniversalTangentHarrisTaylorRepresentingFaStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsUniversalTangentHarrisTaylorRepresentingFaStatement.lean#L1). The smoothness theorem is in [SmoothOfRelativeDimension.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SmoothOfRelativeDimension.lean#L15). There, quasi-projectivity is used only to get a map locally of finite type, and is then passed on to the universal tangent theorem. The space $H(A_0)$, the filtration and filtration lifts for $V = k$ are in [IsKSValueOneOfRetraction.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsKSValueOneOfRetraction.lean#L343), and filtration lifts for general $V$ in [SumProjSingle.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SumProjSingle.lean#L35). We read the statements of results 1 to 8, not their proofs. The descriptions of $H(A_0)$ and of filtration lifts in words are ours.
