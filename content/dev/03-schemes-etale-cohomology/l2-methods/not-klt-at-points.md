---
id: not-klt-at-points
title: One combination of sections that is not klt at several points
kind: theorem
decl: GlobalTheory.LocalHeart.not_klt_at_points
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.AngehrnSiuNotKltAtSeveralPoints
covers: 477
status: drafted
drafted_by: writer@claude
---
This theorem is the local part of [the inductive step of Angehrn-Siu](/entry/exists-global-step/): one vector of coefficients $a$ that works at $c$ points at once. Its second name is [`angehrnSiu_not_klt_at_several_points`](/entry/angehrn-siu-not-klt-at-several-points/).

## Statement

A *place* $E$ of $K$ is a discrete valuation ring of $K$, essentially of finite type over $\mathbb{C}$. For a top form $\eta \neq 0$ and a finite sum $\varphi = \sum \varphi_g [g]$ with $\varphi_g \in \mathbb{Q}$, let $\operatorname{disc}_E(\eta, \varphi) = \operatorname{ord}_E \eta - \sum \varphi_g \operatorname{ord}_E g$. $(\eta, \varphi)$ is *klt over* $R$ if $\operatorname{disc}_E > -1$ for every place $E \supseteq R$. It is *effective at* $R$ if $\operatorname{disc}_E \leq 0$ for every place of codimension one over $R$.

Assume principalisation (`Published.Principalisation`). Let $K$ and $\kappa$ be fields over $\mathbb{C}$ of transcendence degree $n$ and $k \geq 1$ (in the parent, function fields of $X$ and $Z$). For $i = 1, \dots, c$ let $R_i \subset K$ be an integrally closed local ring of a point with residue field $\mathbb{C}$. Let $\pi_i \colon R_i \to \kappa$ be a $\mathbb{C}$-linear ring map whose image is a local ring of a point of $\kappa$ with residue field $\mathbb{C}$ and fraction field $\kappa$. Let $w_{ij} \in R_i$, $\lambda_i \in \kappa^\times$ and $\bar w_j \in \kappa$ ($j \leq l$) with $\pi_i(w_{ij}) = \lambda_i \bar w_j$. Suppose $M \geq 1$ and $c \binom{M+k-1}{k} < l$.

**Theorem.** There is a nonzero $a \in \mathbb{C}^l$ with this property. Fix $i$, a transcendence basis $\xi$ of $K$ inside $R_i$, a sum $\varphi$ of nonzero elements of $R_i$ that is effective at $R_i$ for $d\xi_1 \wedge \dots \wedge d\xi_n$, an element $u$ with $\pi_i(u) = 0$, a rational $t \geq 0$, and $s = \sum_j a_j w_{ij} + u \neq 0$. Suppose that either $\pi_i$ is injective and $k \leq tM$, or there is a place $E \supseteq R_i$ with $\pi_i(r) = 0 \iff \operatorname{ord}_E r > 0$ for nonzero $r$, and $k + M(\operatorname{disc}_E + 1) \leq tM$. Then $(d\xi, \varphi + t[s])$ is not klt over $R_i$.

## Proof

1. `CommonPoint.exists_common_field`: a field $\kappa'$, maps $\rho_i \colon \kappa \to \kappa'$ and a point $O'$ dominating each $\rho_i(\pi_i(R_i))$.
2. `count_kernel_nonzero`: a count of dimensions with $c \binom{M+k-1}{k} < l$ gives a nonzero $b \in \kappa'^l$ with $\sum_j \bar w_j \otimes b_j$ in the $M$-th power of the kernel of $\rho_i \otimes \mathrm{id}$ for every $i$.
3. `SmoothNormalise.normalise_at_smooth_point`: a smooth local ring $B$ over $O'$ and $j_0$ with $b_j / b_{j_0} \in B$. Let $a_j$ be the residue of $b_j / b_{j_0}$. Then $a_{j_0} = 1$.
4. Fix $i$; suppose the pair is klt. `FieldPair.TensorTower.exists_isEtTower_tensor` gives a ring $T$ in $\operatorname{Frac}(K \otimes_{\mathbb{C}} \kappa')$ with a retraction $\psi \colon T \to R_i$. Let $\sigma = \sum_j w_{ij} \otimes (b_j/b_{j_0}) + u$, so $\psi(\sigma) = s$. `FieldPair.klt_of_isEtTower` moves the klt property up to $T$. This uses principalisation.
5. `FieldPair.GraphPlace.exists_place` (first case) or `FieldPair.exists_place_weighted_over_place` (second case) gives a place $V$ with $\operatorname{ord}_V(\sigma) \geq M$ and $\operatorname{ord}_V \eta + 1 - \operatorname{ord}_V \varphi \leq tM$. The proof checks $V \supseteq T$.
6. Then $\operatorname{disc}_V \leq tM - 1 - t\operatorname{ord}_V \sigma \leq -1$, a contradiction.

## In the Lean code

The theorem is at [AngehrnSiuNotKltAtSeveralPoints.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/AngehrnSiuNotKltAtSeveralPoints.lean#L63). We did not open the proofs of these lemmas.

Two hypotheses are not used. The transcendence basis of $K$ is only named at [line 84](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/AngehrnSiuNotKltAtSeveralPoints.lean#L84). Only $\pi_i(w_{ij}) = \lambda_i \bar w_j$ is used ([line 274](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/AngehrnSiuNotKltAtSeveralPoints.lean#L274)); $\lambda_i \neq 0$ is not. We have not matched the statement to a lemma of Angehrn and Siu (Invent. Math. 122, 1995).
