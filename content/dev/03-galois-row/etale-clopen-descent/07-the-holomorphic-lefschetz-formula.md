---
title: The holomorphic Lefschetz formula
decls:
  - UpperTheory.Cb.holomorphic_lefschetz_finiteEtale_correspondence
  - UpperTheory.Core.block_fixed
  - UpperTheory.Cb.lefschetz_fixedPoint_finite_etale_correspondence
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The holomorphic Lefschetz formula

The last section proved the Lefschetz formula for a finite étale correspondence when $Z$ and $Y$ are integral. This section removes both conditions. A smooth projective scheme over $\mathbb{C}$ is a finite disjoint union of integral open and closed pieces. So the cohomology splits into blocks, the trace of the correspondence is the sum of the diagonal blocks, and each fixed point lies in exactly one diagonal block. The result is the form of the [Atiyah and Bott formula](/learn/geometry/#complex-manifolds) that the Galois row uses ([[Atiyah-Bott fixed-point theorem|PKS8JE1PW1]]).

We keep the notation of the last section: $H^b(Z, \Omega^a)$, the correspondence $c_{1*} c_2^*$, the fixed points of $(c_1, c_2)$ and the cotangent matrices $A_y$. All schemes are over $\mathbb{C}$. A scheme $Z$ is *projective* if it has a closed immersion into some $\mathbb{P}^N$ over $\mathbb{C}$.

**Theorem 3.7.1 (Lefschetz formula, Z integral).** Let $Z$ be an integral scheme, smooth of relative dimension $d$ and projective. Let $c_1, c_2 : Y \to Z$ be finite étale. Let $\Phi$ be the finite set of fixed points, and for $y \in \Phi$ let $A_y$ be a cotangent matrix at $y$ with $\det(1 - A_y) \neq 0$. Then for each $a$ and $b$ the space $H^b(Z, \Omega^a)$ has finite dimension, and
$$
\sum_{b=0}^{d} (-1)^b \operatorname{tr}\bigl(c_{1*} c_2^* \mid H^b(Z, \Omega^a)\bigr) = \sum_{y \in \Phi} \frac{[t^a] \det(1 + t A_y)}{\det(1 - A_y)}.
$$

Lean: `UpperTheory.Cb.holomorphic_lefschetz_finiteEtale_correspondence`.

*Proof.* We give the proof in four steps.

First, $Z$ is compact because it is projective, and $Y$ is compact because $c_1$ is finite. Also $Y$ is smooth of relative dimension $d$, because $c_1$ is étale.

Second, $Y$ is a finite disjoint union of integral open subsets $W_1, \dots, W_r$, because it is smooth and quasi-compact. Each $W_m$ is closed, since its complement is the union of the others. So the restrictions of $c_1$ and $c_2$ to $W_m$ are finite étale. The fixed points of the restricted pair are the points of $\Phi$ in $W_m$. The cotangent condition is local, so it holds for the restricted pair with the same matrices $A_y$.

Third, by the integral case of the last section, the formula holds for each pair $c_1|_{W_m}, c_2|_{W_m} : W_m \to Z$.

Fourth, the trace along $c_1$ is the sum of the traces along the $c_1|_{W_m}$, and pullback commutes with composition. So $c_{1*} c_2^* = \sum_m (c_1|_{W_m})_* (c_2|_{W_m})^*$, and the left side is the sum over $m$ of the left sides of the third step. Each complex point of $Y$ lies in exactly one $W_m$, so the right side is the sum over $m$ of the sums over $\Phi \cap W_m$. If $Y$ is empty, both sides are $0$, and finite dimension comes from the smoothness and projectivity of $Z$. $\square$

**Lemma 3.7.2 (One diagonal block).** Let $Z$ be smooth of relative dimension $d$ and projective, let $c_1, c_2 : Y \to Z$ be morphisms, let $\Phi$ be the finite set of fixed points, and for $y \in \Phi$ let $A_y$ be a cotangent matrix at $y$ with $\det(1 - A_y) \neq 0$. Let $V \subseteq Z$ be open, closed and integral. Let $W \subseteq Y$ be open, and let $c'_1, c'_2 : W \to V$ be finite étale maps that are the restrictions of $c_1$ and $c_2$. Then for each $a$ and $b$ the space $H^b(V, \Omega^a)$ has finite dimension, and
$$
\sum_{b=0}^{d} (-1)^b \operatorname{tr}\bigl(c'_{1*} c'^{*}_2 \mid H^b(V, \Omega^a)\bigr) = \sum_{y \in \Phi \cap W} \frac{[t^a] \det(1 + t A_y)}{\det(1 - A_y)}.
$$

Lean: `UpperTheory.Core.block_fixed`.

*Proof.* The scheme $V$ is smooth of relative dimension $d$, because an open immersion is smooth of relative dimension $0$. It is projective, because it is closed in $Z$. A complex point $y$ of $W$ is a fixed point of $(c'_1, c'_2)$ if and only if it is a fixed point of $(c_1, c_2)$, because $V \to Z$ is a monomorphism. The cotangent condition for $(c_1, c_2)$ at $y$ is equivalent to the condition for $(c'_1, c'_2)$, since it is local. So the theorem for $Z$ integral, applied to $c'_1, c'_2 : W \to V$, gives the formula with the sum over the fixed points of $W$. The map from complex points of $W$ to complex points of $Y$ is injective, so this is the sum over $\Phi \cap W$. $\square$

**Theorem 3.7.3 (Holomorphic Lefschetz formula for finite étale correspondences).** Let $Z$ be a scheme, smooth of relative dimension $d$ and projective. Let $c_1, c_2 : Y \to Z$ be finite étale. Let $\Phi$ be a finite set of complex points of $Y$ such that $y \in \Phi$ if and only if $c_1(y) = c_2(y)$. For $y \in \Phi$ let $A_y$ be a cotangent matrix at $y$ with $\det(1 - A_y) \neq 0$. Then for each $a$ and $b$ the space $H^b(Z, \Omega^a)$ has finite dimension, and
$$
\sum_{b=0}^{d} (-1)^b \operatorname{tr}\bigl(c_{1*} c_2^* \mid H^b(Z, \Omega^a)\bigr) = \sum_{y \in \Phi} \frac{[t^a] \det(1 + t A_y)}{\det(1 - A_y)}.
$$

Lean: `UpperTheory.Cb.lefschetz_fixedPoint_finite_etale_correspondence`.

*Proof.* We give the proof in four steps.

First, $Z$ is compact. Since it is smooth, it is a finite disjoint union of integral open and closed pieces $V_1, \dots, V_s$.

Second, let $W_{jk} = c_1^{-1}(V_j) \cap c_2^{-1}(V_k)$. These sets are open and closed, and they cover $Y$ without overlap. The map $c_1$ restricts to a finite étale map $W_{jk} \to V_j$, and $c_2$ to a finite étale map $W_{jk} \to V_k$.

Third, restriction gives an isomorphism from $H^b(Z, \Omega^a)$ to the product of the $H^b(V_j, \Omega^a)$. In this product, $c_{1*} c_2^*$ is a block matrix whose $(j, k)$ block is the correspondence given by $W_{jk}$. Its trace is the sum of the traces of the diagonal blocks, and the lemma on one diagonal block, with $V = V_j$ and $W = W_{jj}$, computes each of them.

Fourth, a fixed point $y$ has $c_1(y) = c_2(y)$, so $c_1(y)$ and $c_2(y)$ lie in the same piece $V_j$, and $y$ lies in exactly one diagonal piece $W_{jj}$. So the sum over $\Phi$ is the sum over $j$ of the sums over $\Phi \cap W_{jj}$, and the formula follows. $\square$

**Remark 3.7.4.** The classical theorem is this. Let $X$ be a compact complex manifold of dimension $d$ and $f : X \to X$ a holomorphic map whose fixed points $P$ are nondegenerate, so $\det(1 - df_P) \neq 0$. Then
$$
\sum_{b} (-1)^b \operatorname{tr}\bigl(f^* \mid H^b(X, \Omega^a)\bigr) = \sum_{f(P) = P} \frac{\operatorname{tr} \Lambda^a (df_P)^{\top}}{\det(1 - df_P)}
$$
(M. F. Atiyah and R. Bott, *A Lefschetz fixed point formula for elliptic complexes. II. Applications*, Ann. of Math. 88 (1968), §4). The Lean theorem is the algebraic form for the correspondence $c_{1*} c_2^*$ instead of a map, and with the cotangent matrix $A_y$ in place of $(df_P)^{\top}$. For $a = 0$ it is the [[Lefschetz fixed-point theorem|G44NQXCWT9]] for the structure sheaf. The set $\Phi$ and the matrices $A_y$ are inputs. The theorem does not prove that the fixed points are finite or that a cotangent matrix exists. It asks that every fixed point be nondegenerate.

**Remark 3.7.5.** The name of the theorem for $Z$ integral does not say that $Z$ is integral, and the names do not show which of the two theorems is more general. In the lemma on one diagonal block, the hypotheses that $c'_1$ is finite and étale are instance arguments, and those for $c'_2$ are explicit arguments. The lemma does not ask that $W = c_1^{-1}(V) \cap c_2^{-1}(V)$, but it is used only with that $W$. The general theorem is used through [its parent statement](/entry/t-lefschetz-fixed-point-finite-etale-correspondence/) in [the geometric realization of weight one](/entry/geometric-realization-of-weight-one/), and so in the step [GeoOne holds](/step/geo-one-holds/) of [the Galois row](/proof/galois-row/).
