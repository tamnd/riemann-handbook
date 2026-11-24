---
title: Division at the points of a flat datum
decls:
  - GlobalTheory.DivFreeWeight.division_order_one
  - GlobalTheory.Shares.VanDiv.model_division
  - GlobalTheory.Shares.VanDiv.vanishing_division
  - GlobalTheory.Containment.division_one
  - GlobalTheory.Containment.division_one'
  - GlobalTheory.Containment.division_all
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Division at the points of a flat datum

This section proves the division theorems that [the shares at all indices](/entry/shares-at-all/) of section 18 uses at the definite index $j = m$. A cusp form that vanishes at the points of a flat datum is a combination of the sections of the datum, with cusp form coefficients. A cusp form whose jets at these points agree with a leading polynomial up to a high order differs from it by a combination of high monomials. Both results feed the surjectivity branch of [the unitary hypotheses](/proof/unitary-hypotheses/). The analytic input is an $L^2$ division theorem of order one on the domain.

### Components and flat data

We keep the notation of section 14. Let $X$ be a component: data of rank $r$ over a CM field $E$, with signature $p_0$, the domain $\Omega$ of frames and the flag dimension $n$. For a weight $G$ let $\varphi_G$ be its weight function and $|f|_G(x) = |f(x)|\, e^{-\varphi_G(x)}$ the pointwise norm of a function $f$ on $\Omega$. A *bounded section* of weight $G$ is a holomorphic function with the automorphy rule of weight $G$ and bounded $|f|_G$. Let $SS(G)$ be the cusp forms of weight $G$. For a constant $c_1$, let $SS_{>}(G, c_1)$ be the cusp forms of weight $G$ whose high modes have the decay of margin $c_1$.

An archimedean datum $(L, F, T)$ for $X$ comes with *margins*: a curvature margin for $F$, the positivity of the Levi form of $\varphi_L$, and the fact that bounded sections are cusp forms at each weight $F + a L$. The curvature margin is a pair $b, \mu$ with

$$\begin{aligned} 4 |\Psi| r^2 &< b, \\ b^2\, |\Psi| \min(p_0, r - p_0) + b &< \mu, \end{aligned}$$

such that, at each orthonormal base frame $x_0$ and each point $z$ of its chart,

$$\mu\, \mathrm{Levi}_{\mathrm{ref}} \leq \mathrm{Levi}(\varphi_F) - \mathrm{Levi}_{\mathrm{dens}},$$

where $\mathrm{Levi}_{\mathrm{ref}}$ is the Levi form of the reference metric and $\mathrm{Levi}_{\mathrm{dens}}$ that of the density.

The flat datum holds sections $w_0$ and $s_1, \ldots, s_n$ of weight $L$, a family $(w_k)$ of weight $L$ and points $x_1, \ldots, x_\delta$ of $\Omega$. The common zeros of the $s_q$ are the orbits of the points, $w_0(x_j) \neq 0$, and the coordinate Jacobian of $s/w_0$ at each $x_j$ is nonzero. So $s/w_0$ is a chart at each $x_j$. The section $w_0$ is bounded, and $|w_0|_L^2 \leq K \sum_k |w_k|_L^2$ for a constant $K$. For a multi-index $\alpha$ put $s^\alpha = \prod_q s_q^{\alpha_q}$.

### Division of order one

**Theorem 7.19.1 (Division of order one at a free weight).** Let $G$ be a weight with a curvature margin $b, \mu$ as above, with $\varphi_G$ in place of $\varphi_F$. Assume that the bounded sections of weight $G + (n + 1) L$ are cusp forms, and that these cusp forms span a finite dimensional space on $\Omega$. Let $f$ be a bounded section of weight $G + (n + 1) L$ with $f(x_j) = 0$ for all $j$ and

$$|f|^2_{G + (n + 1) L} \leq C \Bigl( \sum_k |w_k|^2_L \Bigr)^{n + 1}$$

on $\Omega$, for a constant $C$. Then there are bounded sections $h_1, \ldots, h_n$ of weight $G + n L$ with $f = \sum_q s_q h_q$ on $\Omega$.

Lean: `GlobalTheory.DivFreeWeight.division_order_one`.

*Proof.* We take the steps in order.

1. The action of the group on $\Omega$ is properly discontinuous. The signature gives an orthonormal base frame $x_0$, and there is a fundamental set for the action. From the margin, $0 \leq b \leq \mu$.
2. Consider the singular weight function

$$\psi = \varphi_G + \tfrac{1}{2} \log \sum_k |w_k|^2 + \bigl(n + \tfrac{1}{2}\bigr) \log \sum_q |s_q|^2.$$

The bound on $f$ and its zeros at the points give that $f$ is square integrable for $\psi$ on the fundamental set. The singular metric has the invariant lower bound and smooth curvature at the orders $n + 1$ and $n$.
3. The onto theorem for Poincaré series gives a holomorphic function $P$ on $\Omega$ with $f$ the Poincaré series of $P$, and $P$ equal on the chart of $x_0$ to a function $F$ that is square integrable for $\psi$.
4. The division theorem upstairs at a free weight, with the margin $b \leq \mu$, gives $H_1, \ldots, H_n$ on the chart with $F = \sum_q s_q H_q$ and each $H_q$ square integrable at weight $G + n L$.
5. Each $H_q$ extends to a function $Q_q$ on $\Omega$ with the automorphy rule. The Poincaré series of $Q_q$ converges and is a bounded section of weight $G + n L$.
6. The function $P - \sum_q s_q Q_q$ has the automorphy rule of weight $G + (n + 1) L$ and vanishes on the chart. By the big cell theorem it vanishes on $\Omega$.
7. The sections $s_q$ are invariant of weight $L$. So the Poincaré series of $\sum_q s_q Q_q$ is $\sum_q s_q h_q$, with $h_q$ the Poincaré series of $Q_q$. This is $f$.

This proves the theorem. $\square$

**Lemma 7.19.2 (Division on a model).** Let $(L, F, T)$ have margins, let $k \geq 0$, and assume that the cusp forms of weight $F + (k + n + 1) L$ span a finite dimensional space on $\Omega$. Let $g$ be a bounded section of weight $F + k L$ with $g(x_j) = 0$ for all $j$. Then there are $h_1, \ldots, h_n \in SS(F + (k + n) L)$ with

$$g\, w_0^{n + 1} = \sum_q s_q h_q \quad \text{on } \Omega.$$

Lean: `GlobalTheory.Shares.VanDiv.model_division`.

*Proof.* Put $G = F + k L$ and $f = g\, w_0^{n + 1}$. We check the hypotheses of the division of order one.

1. The Levi form is additive in the weight: $\mathrm{Levi}(\varphi_{G}) = \mathrm{Levi}(\varphi_F) + k\, \mathrm{Levi}(\varphi_L)$. The second term is nonnegative, so the margin of $F$ is a margin of $G$.
2. The weight $G + (n + 1) L$ is $F + (k + n + 1) L$, where bounded sections are cusp forms and the span is finite dimensional.
3. Let $|g|_G \leq C$ and $|w_0|_L \leq B$. Then $|f|^2 = |g|^2_G\, (|w_0|_L^2)^{n + 1} \leq C^2 B^{2(n + 1)}$, so $f$ is bounded. Also $|f|^2 \leq C^2 K^{n + 1} (\sum_k |w_k|^2_L)^{n + 1}$.
4. The section $f$ vanishes at the points, since $g$ does.

The division of order one gives bounded $h_q$ of weight $F + (k + n) L$, and these are cusp forms by the margins. $\square$

### Vanishing at the points of a record

Let $T$ be a record with the laws and $j$ an index in range, and let $N_2$ be a second norm. A *reading* $R$ of $X_j^{+}$ renormed by $N_2$ is a set $\mathcal{Y}$ of points with an evaluation of the forms of each weight. We assume that $\mathcal{Y}$ is in bijection with the pairs $(c, x)$ of a component $c$ and a point $x$ of its domain, so that the evaluation of a form is the value of its restriction to the component. Let $w_1, \ldots, w_N$ be forms of weight $w_L$ and $t$ a matrix of coefficients, which give the sections

$$s_i = \sum_a t(i, a)\, w_a, \qquad 0 \leq i \leq d,$$

where $d = \dim Y$ as in section 18. Let $A$ be an archimedean datum at $(w, w_F, T_n, c_1)$ and $\Phi$ a flat datum with $w_0 = s_0$ and $s_1, \ldots, s_d$ on each component. Let $x_1, \ldots, x_\delta \in \mathcal{Y}$ be the points of all the flat data. For a weight $u$ let $\mathrm{sp}(u)$ be the span of the readings of the forms of weight $u$. Put

$$\mathrm{deep}(u, a) = \operatorname{span} \{\, s^\alpha h : |\alpha| = a,\ h \in \mathrm{sp}(u) \,\}.$$

The readings are *onto* at $u$ if every family of cusp forms on the components of the right weights is the restriction of a form of weight $u$.

**Theorem 7.19.3 (Vanishing division at a record).** Let the readings be onto at every weight $w_F + k w_L$. Let $k \geq 0$ and $g \in \mathrm{sp}(w_F + k w_L)$ with $g(x_q) = 0$ for all $q$. Then there is $m \geq 0$ with

$$s_0^{m + 1}\, g \in \mathrm{deep}(w_F + (k + m) w_L, 1).$$

Lean: `GlobalTheory.Shares.VanDiv.vanishing_division`.

*Proof.* We take the steps in order.

1. By the dictionary of weights, the weight $w_F + a w_L$ is $F_c + a L_c$ on the component $c$, where $(L_c, F_c)$ are the weights of $A$ there.
2. The readings of weight $u$ are the families of restrictions to the components. So $g$ is given by cusp forms $f_c$ of weight $F_c + k L_c$, with $f_c(x_q) = 0$ at the points of $\Phi$ on $c$.
3. The cusp forms of each weight are finite over $K$. Since the readings are onto, the cusp forms on each component span a finite dimensional space at each weight.
4. [The division on a model](/entry/model-division/) on each component $c$ gives $H_{c, 1}, \ldots, H_{c, d}$ in $SS(F_c + (k + d) L_c)$ with $f_c\, w_0^{d + 1} = \sum_q s_q H_{c, q}$.
5. Since the readings are onto at $w_F + (k + d) w_L$, the family $(H_{c, q})_c$ is a reading $h_q \in \mathrm{sp}(w_F + (k + d) w_L)$. So $s_0^{d + 1} g = \sum_q s_q h_q$, and each term has $|\alpha| = 1$.

Take $m = d$. $\square$

### Division of high order

Let $t_1, \ldots, t_m$ be bounded sections of weight $F$. For coefficients $c_{\alpha, i}$, indexed by multi-indices $\alpha$ with $|\alpha| < T - n$ and by $i$, put

$$\mathrm{lead}_c = \sum_{|\alpha| < T - n} \sum_i c_{\alpha, i}\, s^\alpha\, w_0^{T - |\alpha|}\, t_i.$$

It has weight $F + T L$.

**Lemma 7.19.4 (Division of high order on one component).** Let $(L, F, T)$ have margins, and let the cusp forms of weight $F + T L$ span a finite dimensional space on $\Omega$. Assume that the vectors $(t_i(x_j))_j$ span $\mathbb{C}^\delta$. Let $f \in SS_{>}(F + T L, c_1)$, and let $c$ be coefficients such that, in the chart coordinates $z$ at each $x_j$,

$$f - \mathrm{lead}_c = O\bigl(|z|^{T - n}\bigr) \quad (z \to 0).$$

Then there are $h_\alpha \in SS(F + n L)$ for $|\alpha| = T - n$ with $f - \mathrm{lead}_c = \sum_{|\alpha| = T - n} s^\alpha h_\alpha$ on $\Omega$.

Lean: `GlobalTheory.Containment.division_one'` (also `GlobalTheory.Containment.division_one`).

*Proof.* We take the steps in order.

1. The action is properly discontinuous and the quotient has finite measure. This gives a base frame $x_0$ and a fundamental set.
2. The start of the division gives that $f - \mathrm{lead}_c$ is bounded and integrable at the order $T - n$. It uses the bound for the high modes of $f$, which holds since $f$ has margin $c_1$.
3. Since the values of the $t_i$ at the points span $\mathbb{C}^\delta$, there are bounded sections $t'_1, \ldots, t'_\delta$ of weight $F$ with $t'_i(x_j) = 1$ if $i = j$ and $0$ otherwise. Take the combinations $t'_i = \sum_k a_{ik} t_k$ with the values of the unit vectors.
4. The estimate in the charts gives that $f - \mathrm{lead}_c$ vanishes to order $T - n$ at the points.
5. The division core theorem, with the dual family $t'$ and the zero leading term, gives bounded sections $h_\alpha$ of weight $F + n L$ with the identity. By the margins they are cusp forms.

The second form of the lemma names $n$ and $T$ by given numbers. $\square$

**Theorem 7.19.5 (Division on all components).** Let $(X_k)$ be a family of components with archimedean data $(L_k, F_k, T)$ with margins and flat data, all with the same flag dimension $n$ and the same $T$. Assume that the cusp forms of weight $F_k + T L_k$ span a finite dimensional space on each domain. Let $t_1, \ldots, t_m$ be families of bounded sections of weight $F_k$ on each $X_k$, such that the vectors of values at all the points of all the flat data span. Let $f_k \in SS_{>}(F_k + T L_k, c_1)$ for each $k$. Then there are coefficients $c$, the same for all $k$, and $h_{k, \alpha} \in SS(F_k + n L_k)$ for $|\alpha| = T - n$, with

$$f_k - \mathrm{lead}_{k, c} = \sum_{|\alpha| = T - n} s_k^\alpha\, h_{k, \alpha} \quad \text{on the domain of } X_k.$$

Lean: `GlobalTheory.Containment.division_all`.

*Proof.* We take the steps in order.

1. Each $s_{k, q}$ vanishes at the points of the flat datum of $X_k$, since these points lie in the common zero set. Also $w_{k, 0} \neq 0$ there, and the Jacobian of $s_k / w_{k, 0}$ is nonzero.
2. All the functions are holomorphic near each point. So in the chart coordinates the functions $s_k / w_{k, 0}$ are coordinates at each point.
3. The theorem on pure jets, applied at all the points at once, gives coefficients $c$ such that $f_k - \mathrm{lead}_{k, c} = O(|z|^{T - n})$ at each point of each $X_k$. It uses the span of the values of the $t_i$.
4. For each $k$, the values of the $t_i$ at the points of $X_k$ span. Indeed, extend a vector on these points by zero to all the points, and use the span hypothesis.
5. The division of high order on $X_k$, with the coefficients $c$, gives the $h_{k, \alpha}$.

This proves the theorem. $\square$

In the definite case, the theorem is applied to the restrictions of a form of weight $w_F + T_n w_L$ with growth margin, and the sections $t_i$ are the readings of the forms $\theta'$ of section 18. The result is the containment of these forms in the span of the leading monomials plus the deep module.

**Remark 7.19.6 (Formalization).** The division of order one is `division_order_one` at line 22 of [DivisionOrderOne.lean](lean:Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/DivisionOrderOne.lean#L22); its margin uses $\min(p_0, r - p_0)$. The lemma `model_division` is at line 45 and `vanishing_division` at line 95 of [CuspFormVanishingAtPointsMulPowMemSpan.lean](lean:Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/CuspFormVanishingAtPointsMulPowMemSpan.lean#L45), with the additivity `leviO_phla_add_nsmul` at line 25 and the norm identity `pnorm_mul_pow_sq` at line 39. The existential $m$ of `vanishing_division` is always $d$, `WeightFamilies.dimY D j`. The lemmas `division_one`, `division_one'` and `division_all` are at lines 48, 75 and 104 of [CuspFormVanishingLowCoeffMemLeadingAddDeepSpan.lean](lean:Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/CuspFormVanishingLowCoeffMemLeadingAddDeepSpan.lean#L48), with the dual family `exists_valBasis` at line 31; `division_one'` is `subst` and `division_one`. The record theorem `main` at line 159 of that file binds its hypothesis on $c_1$ to `_` at line 161, and its proof is repeated in `containment_any` at line 74 of [CuspFormBasisSharesDefiniteLiftIndex.lean](lean:Development/AbelianVarietyTheory/Proofs/TorusHaarMeasure/CuspFormBasisSharesDefiniteLiftIndex.lean#L74), which calls `division_all` at line 122 instead of `main`. The same file calls `vanishing_division` at line 162. The indefinite case uses the statement forms `T.cuspForm_vanishing_at_points_mul_pow_mem_span` and `T.cuspForm_vanishing_low_coeff_mem_leading_add_deep_span`, which are `first | exact` wrappers.
