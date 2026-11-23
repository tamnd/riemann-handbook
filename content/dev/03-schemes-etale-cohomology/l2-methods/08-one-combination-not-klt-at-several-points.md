---
title: One combination that is not klt at several points
decls:
  - GlobalTheory.LocalHeart.not_klt_at_points
  - GlobalTheory.T.angehrnSiu_not_klt_at_several_points
status: drafted
drafted_by: writer@claude-opus-5-5
---
## One combination that is not klt at several points

This section proves the local heart of the theorem of Angehrn and Siu. Let $Z$ be a subvariety of dimension $k$ of a variety $X$, through points $x_1, \dots, x_c$, and let $f_1, \dots, f_l$ be sections of a line bundle. If $l$ is larger than the number $c\binom{M+k-1}{k}$ of conditions for a section of $Z$ to vanish to order $M$ at $c$ points, then there is one fixed combination $s = \sum_j a_j f_j$, with complex coefficients, such that the pair with the boundary $t\,\mathrm{div}(s)$ added is not klt at any of the points $x_i$, as soon as $tM$ is large compared to $k$. Section 9 uses this to build the divisor of the inductive step. The proof follows the method of Angehrn and Siu: we make the combination vanish to order $M$ at a general point, and then pass to a limit with the result of Section 7.

We keep the notation of Sections 6 and 7. For a ring map $\pi : R \to \kappa$ we say that $\pi$ is a map *over* $\mathbb{C}$ if it is the identity on the constants. A local model $R$ has *rational residues* if each $r \in R$ is a constant $a \in \mathbb{C}$ plus a nonunit of $R$; for the local ring of a closed point of a variety over $\mathbb{C}$ this is the statement that the residue field is $\mathbb{C}$.

The data are the following. The field $K$ is the function field of $X$, and $\kappa$ is the function field of $Z$, of transcendence degree $k$. For each $i$, $R_i \subseteq K$ is the local ring of $X$ at $x_i$, and $\pi_i : R_i \to \kappa$ is the restriction of functions to $Z$, so its image $\pi_i(R_i)$ is the local ring of $Z$ at $x_i$. The elements $w_{ij} \in R_i$ are the sections $f_j$ in a trivialisation at $x_i$. Their restrictions to $Z$ differ only by a factor that does not depend on $j$: $\pi_i(w_{ij}) = \lambda_i \bar w_j$, where $\bar w_j \in \kappa$ is the restriction of $f_j$ in one fixed trivialisation on $Z$.

**Theorem 10.8.1 (One combination not klt at several points).** Assume principalisation. Let $K$ and $\kappa$ be fields over $\mathbb{C}$, and let $n, k, c, l, M$ be natural numbers with $k \ge 1$, $M \ge 1$ and
$$c \binom{M+k-1}{k} < l.$$
Suppose that $K$ has a transcendence basis of size $n$, and $\kappa$ one of size $k$. For $i = 1, \dots, c$ let $R_i \subseteq K$ and $\pi_i : R_i \to \kappa$ be such that:

1. $R_i$ is an integrally closed local model of $K$ with rational residues;
2. $\pi_i$ is a map over $\mathbb{C}$, and each element of $\kappa$ is a quotient of two elements of $\pi_i(R_i)$;
3. $\pi_i(R_i)$ is a local model of $\kappa$ with rational residues.

Let $w_{ij} \in R_i$, $\lambda_i \in \kappa$ and $\bar w_j \in \kappa$ for $j = 1, \dots, l$, with $\lambda_i \neq 0$ and $\pi_i(w_{ij}) = \lambda_i \bar w_j$. Then there is $a \in \mathbb{C}^l$, $a \neq 0$, with the following property. Let $i \le c$, let $\xi$ in $R_i$ be a transcendence basis of $K$, and let $\varphi$ be a finite formal sum of nonzero elements of $R_i$ such that $(d\xi, \varphi)$ is effective at $R_i$. Let $u \in R_i$ with $\pi_i(u) = 0$, let $t \in \mathbb{Q}$ with $t \ge 0$, and suppose
$$s = \sum_{j=1}^l a_j w_{ij} + u \neq 0.$$
Suppose that one of the two conditions holds:

- (A) $\pi_i$ is injective and $k \le tM$;
- (B) there is a place $E$ that contains $R_i$, with $\pi_i(r) = 0$ if and only if $\operatorname{ord}_E r > 0$ for nonzero $r \in R_i$, and
$$k + M\bigl(\operatorname{disc}_E(d\xi, \varphi) + 1\bigr) \le tM.$$

Then $(d\xi, \varphi + t[s])$ is not klt over $R_i$.

Lean: `GlobalTheory.LocalHeart.not_klt_at_points` (also `GlobalTheory.T.angehrnSiu_not_klt_at_several_points`, a second name).

The vector $a$ does not depend on $i$, $\xi$, $\varphi$, $u$ or $t$. In condition (A) the map $\pi_i$ is injective, so $Z$ is all of $X$ and the condition is the old rule that multiplicity at least the dimension at a point gives a pair that is not klt there. In condition (B) the place $E$ has centre $Z$ on $\operatorname{Spec} R_i$: the functions that vanish on $Z$ are exactly those with positive order along $E$. If $Z$ is a non-klt centre and $E$ computes it, then $\operatorname{disc}_E = -1$, and (B) is again $k \le tM$. The term $M(\operatorname{disc}_E + 1)$ measures how far $Z$ is from being a non-klt centre. Section 9 makes it small by a perturbation of the boundary. The element $u$ is an arbitrary function that vanishes on $Z$. So only the restriction of $s$ to $Z$ matters.

*Proof.* We use four facts, each of which we read as a statement.

- (a) *A common point.* There are a field $\kappa'$ over $\mathbb{C}$, maps $\rho_i : \kappa \to \kappa'$ over $\mathbb{C}$, and a local model $O' \subseteq \kappa'$ with rational residues that dominates $\rho_i(\pi_i(R_i))$ for each $i$; also $\kappa'$ has a finite transcendence basis. Geometrically, $\kappa'$ is the function field of a variety $Z'$ with dominant maps $\rho_i : Z' \to Z$, and a point $o' \in Z'$ with $\rho_i(o') = x_i$ for each $i$. One can take $Z' = Z^c$ with the $c$ projections.
- (b) *Counting conditions.* There is $b \in (\kappa')^l$, $b \neq 0$, such that for each $i$
$$\sum_{j=1}^l \bar w_j \otimes b_j \in \bigl(\ker(\rho_i \otimes \mathrm{id} : \kappa \otimes_{\mathbb{C}} \kappa' \to \kappa')\bigr)^M.$$
The kernel of $\rho_i \otimes \mathrm{id}$ is the ideal of the graph of $\rho_i$ in $Z \times Z'$. So the section $\sum_j b_j(z')\, \bar w_j$ of $Z$, with coefficients that are functions of a parameter $z' \in Z'$, vanishes to order $M$ at the point $\rho_i(z')$, for each $i$ and a general $z'$. This is linear algebra over the field $\kappa'$: vanishing to order $M$ at a smooth point of the $k$-dimensional $Z$ is $\binom{M+k-1}{k}$ linear conditions, there are $c$ points, and $l$ unknowns.
- (c) *Normalisation at a smooth point.* There are a local model $B \subseteq \kappa'$ with rational residues that dominates $O'$, elements $\tau_1, \dots, \tau_r$ of $B$ that generate its maximal ideal, with $\mathbb{C}[X_1, \dots, X_r] \to B$, $X_q \mapsto \tau_q$, formally étale and $\tau$ a transcendence basis of $\kappa'$, and an index $j_0$ with $b_{j_0} \neq 0$ and $b_j / b_{j_0} \in B$ for all $j$. So $B$ is the local ring of a smooth point $o''$ of a model of $Z'$ over $o'$, with coordinates $\tau$, at which the ratios of the $b_j$ are regular.
- (d) *The tower of the product.* Let $L$ be the fraction field of $K \otimes_{\mathbb{C}} \kappa'$, the function field of $X \times Z'$. There are a subring $T \subseteq L$ and maps $\iota : R_i \to T$, $\psi : T \to R_i$ and $j : B \to T$ such that $(R_i, T, \iota, \psi, j(\tau))$ is an étale tower of length $r$ in the sense of Section 7, $\iota(g) = g \otimes 1$ and $j(\beta) = 1 \otimes \beta$, and $\psi(j(\beta))$ is the constant $\beta(o'')$ for $\beta \in B$. Also each element of $T$ is a quotient of two elements of the ring generated by $\iota(R_i)$ and $j(B)$, with a denominator whose image under $\psi$ is a unit. So $T$ is the local ring of $X \times Z'$ at $(x_i, o'')$, and $\psi$ is the restriction to the slice $X \times \{o''\}$.

Now let $b$ be as in (b) and $B$, $\tau$, $j_0$ as in (c). For each $j$ the ratio $b_j / b_{j_0}$ lies in $B$, and by rational residues $b_j/b_{j_0} = a_j + m_j$ with $a_j \in \mathbb{C}$ and $m_j$ in the maximal ideal of $B$. So $a_j$ is the value of $b_j/b_{j_0}$ at $o''$. Since $b_{j_0}/b_{j_0} = 1$ is a unit, $a_{j_0} = 1$, and $a \neq 0$. This $a$ depends only on the data before the choice of $i$.

Fix $i$, $\xi$, $\varphi$, $u$, $s$ and $t$ as in the theorem, and suppose that $(d\xi, \varphi + t[s])$ is klt over $R_i$. We derive a contradiction. Let $T$, $\iota$, $\psi$, $j$ be as in (d) for $R_i$, and put
$$\sigma = \sum_{j=1}^l \iota(w_{ij})\, j\bigl(b_j / b_{j_0}\bigr) + \iota(u) \in T.$$
This is the family of combinations $\sum_j (b_j/b_{j_0})(z') f_j + u$ over the parameter space. By (d), $\psi(\sigma) = \sum_j a_j w_{ij} + u = s$. So $\psi(\sigma) \neq 0$.

*The pair upstairs is klt.* Apply the theorem on klt up an étale tower ([Theorem 10.7.2](/entry/klt-of-is-et-tower/)) to the tower of (d), the transcendence basis $\xi$, the sum $\varphi$ and $\theta = t[\sigma]$. The support of $\theta$ is $\{\sigma\}$ or empty, with $\psi(\sigma) \neq 0$ and $t \ge 0$. The pair $(d\xi, \varphi)$ is effective at $R_i$, and $\varphi + \psi_*\theta = \varphi + t[s]$, so the pair downstairs is klt. Hence
$$\bigl(d\tau \wedge d\xi,\ \varphi + t[\sigma]\bigr)$$
is klt over $T$, where we write $\tau$ for $1 \otimes \tau$ and $\xi$ for $\xi \otimes 1$.

*A place of large order.* We next need a place $V$ of $L$ with these properties:

1. $V$ contains $g \otimes 1$ for $g \in R_i$, and $\operatorname{ord}_V(1 \otimes \beta) = 0$ for nonzero $\beta \in \kappa'$;
2. if $\sum_q \rho_i(\pi_i(a_q))\, \beta_q \neq 0$, then $\sum_q a_q \otimes \beta_q$ is nonzero of order $0$ along $V$;
3. if $\sum_q a_q \otimes \beta_q \neq 0$ and $\sum_q \pi_i(a_q) \otimes \beta_q$ lies in the $M$-th power of the kernel of $\rho_i \otimes \mathrm{id}$, then $\operatorname{ord}_V \sum_q a_q \otimes \beta_q \ge M$;
4. $\operatorname{ord}_V(d\tau \wedge d\xi) + 1 - \operatorname{ord}_V \varphi \le tM$.

Here $\operatorname{ord}_V \varphi = \sum_g \varphi_g \operatorname{ord}_V g$. Geometrically, $V$ is a place of $X \times Z'$ with centre the graph $\Gamma_i$ of $Z' \to Z \subseteq X$, with weight $M$ in the directions normal to $\Gamma_i$ inside $Z \times Z'$. Its existence is one of two facts that we read as statements:

- (e) in case (A), a place $V$ with 1 to 3, $\operatorname{ord}_V(g \otimes 1) = 0$ for nonzero $g \in K$ and $\operatorname{ord}_V(d\tau \wedge d\xi) + 1 \le k$;
- (f) in case (B), a place $V$ with 1 to 3, $\operatorname{ord}_V(g \otimes 1) = M \operatorname{ord}_E g$ for nonzero $g \in K$ and $\operatorname{ord}_V(d\tau \wedge d\xi) + 1 \le M(\operatorname{ord}_E d\xi + 1) + k$.

In case (A), $\operatorname{ord}_V \varphi = 0$, so 4 follows from $k \le tM$. In case (B), $\operatorname{ord}_V \varphi = M \operatorname{ord}_E \varphi$, so
$$\operatorname{ord}_V(d\tau \wedge d\xi) + 1 - \operatorname{ord}_V \varphi \le M\bigl(\operatorname{ord}_E d\xi - \operatorname{ord}_E\varphi + 1\bigr) + k = M\bigl(\operatorname{disc}_E(d\xi,\varphi) + 1\bigr) + k \le tM.$$

*The place contains $T$.* By 1, the generators $\iota(R_i)$ and $j(B)$ of $T$ lie in $\mathcal{O}_V$, so the ring they generate does. Let $y$ be an element of that ring with $\psi(y)$ a unit, and write $y = \sum_q \iota(a_q) j(\beta_q)$. Then $\psi(y) = \sum_q a_q c_q$ with $c_q = \beta_q(o'')$ the constants of (d). If $\sum_q \rho_i\pi_i(a_q)\, \beta_q$ were $0$, then
$$\rho_i\pi_i\bigl(\psi(y)\bigr) = \sum_q \rho_i\pi_i(a_q)\,(c_q - \beta_q)$$
would lie in the maximal ideal of $B$, since each $\beta_q - c_q$ does and $\rho_i\pi_i(R_i) \subseteq B$ by (a) and (c). But $\psi(y)$ is a unit of $R_i$, so its image is a unit of $B$, a contradiction. So by 2, $y \neq 0$ and $\operatorname{ord}_V y = 0$. By (d), each element of $T$ is $y_1 / y_2$ with $y_1$, $y_2$ of this kind and $\psi(y_2)$ a unit. So it has order $\operatorname{ord}_V y_1 \ge 0$, and $V$ contains $T$.

*The order of $\sigma$.* Write $\sigma = \iota(u) + \sum_j \iota(w_{ij})\, j(b_j/b_{j_0})$, a sum of the form in 3 with $l + 1$ terms. Its image under $\pi_i \otimes \mathrm{id}$ is
$$\pi_i(u) \otimes 1 + \sum_j \lambda_i \bar w_j \otimes \frac{b_j}{b_{j_0}} = (\lambda_i \otimes b_{j_0}^{-1}) \sum_j \bar w_j \otimes b_j,$$
since $\pi_i(u) = 0$. By (b) it lies in the $M$-th power of the kernel. Since $\sigma \neq 0$, 3 gives $\operatorname{ord}_V \sigma \ge M$.

*The contradiction.* Since the pair upstairs is klt over $T$ and $V$ contains $T$,
$$-1 < \operatorname{disc}_V\bigl(d\tau \wedge d\xi, \varphi + t[\sigma]\bigr) = \operatorname{ord}_V(d\tau \wedge d\xi) - \operatorname{ord}_V\varphi - t \operatorname{ord}_V\sigma.$$
By 4 and $t \operatorname{ord}_V \sigma \ge tM$, the right side is at most $tM - 1 - tM = -1$. This is a contradiction. $\square$

The proof does not use $\lambda_i \neq 0$: the factor $\lambda_i$ is absorbed into the ideal in the step on the order of $\sigma$ in any case. It also does not use the transcendence basis of $K$ of size $n$ in the hypotheses, since the theorem gives $\xi$ again in the conclusion.

**Remark 10.8.2 (Formalization).** The facts (a) to (d) are `CommonPoint.exists_common_field`, `count_kernel_nonzero`, `SmoothNormalise.normalise_at_smooth_point` and `TensorTower.exists_isEtTower_tensor`, and (e) and (f) are `GraphPlace.exists_place` and `exists_place_weighted_over_place`. We read their statements, not their proofs, and the geometric readings given for them are ours. Rational residues is `RatRes`. The field $L$ is `FractionRing (K ⊗[ℂ] κ')`. In the file AngehrnSiuNotKltAtSeveralPoints.lean the hypothesis that $K$ has a transcendence basis of size $n$ is named `hxK` on line 84 and is not used afterwards. Of the hypothesis `hw`, only the second part $\pi_i(w_{ij}) = \lambda_i \bar w_j$ is used, as `(hw i).2` on line 274, so $\lambda_i \neq 0$ is not needed. The second name is a wrapper of the first with the same statement.
