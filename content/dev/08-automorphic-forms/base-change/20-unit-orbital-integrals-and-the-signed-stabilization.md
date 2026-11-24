---
title: Unit orbital integrals and the signed stabilization
decls:
  - UpperTheory.ConvolutionTheory.G3.intUniq
  - UpperTheory.ConvolutionTheory.G3.unitAe
  - UpperTheory.ConvolutionTheory.G2.stAA
  - UpperTheory.ConvolutionTheory.G2.termId
  - UpperTheory.ConvolutionTheory.G2.g2s
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Unit orbital integrals and the signed stabilization

The unitary elliptic sum of Section 12 is a sum over pairs of elliptic polynomials of products of $\kappa$-orbital integrals over a section. This section writes it as a combination, with signs $\pm 1$, of stable elliptic sums of the groups $\mathrm{GL}_a \times \mathrm{GL}_{n-a}$. There are three steps: the stable twisted orbital integral of the unit is $1$ at almost every place; the local matching identities multiply to a global one by a product formula for transfer factors; and an identity of archimedean characters turns the character of $\mathrm{U}(n)$ into a signed sum over the blocks. The result is used in the comparison of trace formulas, [the theorem on the run of the trace formula](/entry/run-th/), below the step [EveryCharacter](/step/every-character/).

We keep the notation of Sections 04, 07, 11 and 12. The field $E$ is CM with maximal real subfield $F$, every finite place of $E$ is unramified over $F$, and $\theta_E$ is the involution of $\mathrm{GL}_m(E)$ of Section 11. For a finite place $w$ of $E$ and $m \ge 0$ let $K_m = \mathrm{GL}_m(\mathcal{O}_w)$, let $\theta_w$ be the identity of $\mathrm{GL}_m(E_w)$ if $w$ is split over $F$ and the involution $\theta$ of Section 04 if not, and let $N_w(y) = y$ if $w$ is split and $N_w(y) = y\theta(y)$ if not. For $\delta \in \mathrm{GL}_m(E)$ let $\delta_w \in \mathrm{GL}_m(E_w)$ be as in Section 07 (the image of $\delta\theta_E(\delta)$ if $w$ is split and of $\delta$ if not), and let $P_\delta$ be the characteristic polynomial of $\delta\theta_E(\delta)$. For $y \in \mathrm{GL}_m(E_w)$ let $P_y$ be the characteristic polynomial of $N_w(y)$. Two elements $y, y'$ are twisted conjugate if $y' = g^{-1}y\theta_w(g)$ for some $g \in \mathrm{GL}_m(E_w)$, and $K_m$-twisted conjugate if $g$ can be taken in $K_m$. The stable orbital integrals $SO_{Q_1,Q_2}$ of Section 04 are defined at every finite place with $\theta_w$ in place of $\theta$ and $N_w$ in place of $N$, as in Section 11.

Two facts are direct. The norm of $\delta_w$ has characteristic polynomial the image of $P_\delta$ in $E_w[X]$. And $P_y$ depends only on the twisted class of $y$: if $w$ is not split, $\theta$ is an involution and
$$N_w\big(g^{-1}y\theta(g)\big) = g^{-1}y\theta(g)\,\theta(g)^{-1}\theta(y)\,g = g^{-1}N_w(y)\,g,$$
and if $w$ is split twisted conjugacy is conjugacy.

**Theorem 7.20.1 (Integral uniqueness).** Let $m \ge 0$ and $\delta \in \mathrm{GL}_m(E)$ with $P_\delta$ separable. Then for almost every finite place $w$ of $E$:

1. $\delta_w \in K_m$;
2. every $y \in K_m$ with $P_y$ equal to the image of $P_\delta$ is $K_m$-twisted conjugate to $\delta_w$.

Lean: `UpperTheory.ConvolutionTheory.G3.intUniq`.

*Proof.* Part 1 holds at almost every $w$, since $\delta$ and $\delta\theta_E(\delta)$ have entries and inverse entries in $\mathcal{O}_w$ for almost every $w$. Write $P = P_\delta$. Since $P$ is separable, there are $A, B \in E[X]$ with $AP + BP' = 1$, and for almost every $w$ the coefficients of $A$, $B$ and $P$ are integral at $w$. At such $w$ every monic $Q \in \mathcal{O}_w[X]$ with image $P$ is separable over $\mathcal{O}_w$, that is, its reduction modulo the maximal ideal is separable.

Let $w$ be split. Then $\theta_w$ is the identity, $\delta_w$ is the image of $\delta\theta_E(\delta)$, and $y$ and $\delta_w$ are two matrices in $K_m$ with the same characteristic polynomial, which is separable over $\mathcal{O}_w$. A matrix over a local ring whose characteristic polynomial is separable has a cyclic vector, so it is conjugate over the ring to the companion matrix of its characteristic polynomial. So $y$ and $\delta_w$ are conjugate by an element of $K_m$.

Let $w$ be inert. Write $\theta_E(g) = u\,{}^{\mathsf T}\bar g^{-1}u^{-1}$ with $u \in \mathrm{GL}_m(E)$ and $u\,{}^{\mathsf T}\bar u^{-1} = 1$; such a $u$ exists, and the same formula describes $\theta_w$ at every nonsplit $w$. For almost every $w$ the matrix $u$ lies in $K_m$. At such a place, with $\delta_w \in K_m$ and the integral model of $P$ separable, the companion development proves part 2 directly: an element $y \in K_m$ whose norm $y\theta(y)$ has the same separable characteristic polynomial as $\delta_w\theta(\delta_w)$ is $K_m$-twisted conjugate to $\delta_w$. The proof uses the local Galois data of the unramified quadratic extension $E_w/F_v$. $\square$

**Theorem 7.20.2 (Unit orbital integrals).** Let $a, b \ge 0$, and let $\delta_1 \in \mathrm{GL}_a(E)$ and $\delta_2 \in \mathrm{GL}_b(E)$ with $P_{\delta_1}$ and $P_{\delta_2}$ separable. Then for almost every finite place $w$ the following holds. Let $y_1 \in \mathrm{GL}_a(E_w)$ and $y_2 \in \mathrm{GL}_b(E_w)$ with $P_{y_i}$ equal to the image of $P_{\delta_i}$. Then, with $K = K_a \times K_b$ and $\theta_w$ on both factors,
$$O^\theta_{(y_1, y_2)}(\mathbf{1}_K) = \begin{cases}1 & \text{if } y_i \text{ is twisted conjugate to } \delta_{i,w} \text{ for } i = 1, 2,\\ 0 & \text{otherwise.}\end{cases}$$

Lean: `UpperTheory.ConvolutionTheory.G3.unitAe`.

*Proof.* Take $w$ such that the [integral uniqueness theorem](/entry/int-uniq/) holds for $\delta_1$ and for $\delta_2$, and such that for $i = 1, 2$ the compact part $C$ of the twisted centralizer of $\delta_{i,w}$ is its intersection with $K$; the companion development proves this last property for almost every $w$ when $P_{\delta_i}$ is separable. Write $\delta_w = (\delta_{1,w}, \delta_{2,w})$. The subgroup $K$ is $\theta_w$-stable.

Assume that $y_i$ is twisted conjugate to $\delta_{i,w}$ for both $i$. The twisted orbital integral depends only on the twisted class, so $O^\theta_y(\mathbf{1}_K) = O^\theta_{\delta_w}(\mathbf{1}_K)$. In the sum over double cosets $H_{\delta_w}gK$ that defines it, a term is nonzero only if $z = (gk)^{-1}\delta_w\theta_w(gk)$ lies in $K$ for some $k \in K$. Such a $z$ is twisted conjugate to $\delta_w$ and has the norm polynomials of $\delta_w$, so by part 2 of integral uniqueness $z = k'^{-1}\delta_w\theta_w(k')$ with $k' \in K$. Then $gkk'^{-1}$ lies in the twisted centralizer, so $g \in H_{\delta_w}K$, and only the trivial double coset contributes. Its term is $[C : C \cap K]$ times the average of $\mathbf{1}_K$ over $k^{-1}\delta_w\theta_w(k)$, $k \in K$. The index is $1$ since $C = H_{\delta_w} \cap K$, and the average is $1$ since $\delta_w \in K$. So the integral is $1$.

Assume now that some $y_i$ is not twisted conjugate to $\delta_{i,w}$. Let $z$ be a twisted conjugate of $y$. If $z \in K$, then $P_{z_i} = P_{y_i}$ is the image of $P_{\delta_i}$, and integral uniqueness makes $z_i$ twisted conjugate to $\delta_{i,w}$ for both $i$, hence $y_i$ too, which is false. So $\mathbf{1}_K$ vanishes on the twisted class of $y$, and every term of the orbital integral is $0$. $\square$

**Theorem 7.20.3 (Stable unit integrals).** Let $a, b \ge 0$ and let $P_1$, $P_2$ be elliptic polynomials over $E$ of degrees $a$ and $b$. Then for almost every finite place $w$,
$$SO_{P_1,P_2}(\mathbf{1}_{K_a \times K_b}) = 1.$$

Lean: `UpperTheory.ConvolutionTheory.G2.stAA`.

*Proof.* Every elliptic polynomial is a norm polynomial: the companion development gives $\delta_1 \in \mathrm{GL}_a(E)$ and $\delta_2 \in \mathrm{GL}_b(E)$ with $P_{\delta_i} = P_i$. Elliptic polynomials are separable, so the [theorem on unit orbital integrals](/entry/unit-ae/) applies at almost every $w$. At such $w$, $SO_{P_1,P_2}(\mathbf{1}_K)$ is the sum of $O^\theta_y(\mathbf{1}_K)$ over the twisted classes of pairs $y$ with $P_{y_i}$ the image of $P_i$. The class of $\delta_w$ is one of them, by the first direct fact above, and its term is $1$. Every other class has term $0$. $\square$

For the next result we need the transfer factor at a split place. Let $w$ be split, $\mu_w$ a character of $E_w^\times$, and $Q_1$, $Q_2$ monic of degrees $a$ and $b$ with $R = \mathrm{Res}(Q_1, Q_2) \ne 0$. Put
$$d = \big((-1)^aQ_1(0)\big)^b\big((-1)^bQ_2(0)\big)^a, \qquad \Delta_\mu(Q_1, Q_2) = \mu_w\big((-1)^{ab}d\big)\,\big|R^2/d\big|_w^{1/2}.$$
At a nonsplit place $\Delta_\mu = \Delta$ is the factor of Section 04 and does not depend on $\mu$. Matching with the character $\mu_w$ is the identity $SO_{Q_1,Q_2}(\varphi) = \Delta_\mu(Q_1,Q_2)\,\kappa O_{Q_1,Q_2}(f)$ for the pairs of Section 04; at a split place the condition of being conjugate self-reciprocal is empty. For an archimedean place $v$, an integer $e_v$ and $R \in E^\times$ put
$$\epsilon_v(R) = \Big(\frac{v(R)}{|v(R)|}\Big)^{e_v}|v(R)|,$$
with $v(R) \in \mathbb{C}$ the image of $R$ and $|\cdot|$ the usual absolute value.

**Theorem 7.20.4 (Product of $\kappa$-orbital integrals).** Let $(\mu, e)$ be admissible, let $S$ be a section, and let $n, a, b \ge 0$. Let $f = (f_w)$ be a family of functions on the unitary groups $U_w$ of rank $n$, and $\varphi = (\varphi_w)$ a family of functions on $\mathrm{GL}_a(E_w) \times \mathrm{GL}_b(E_w)$ with $\varphi_w = \mathbf{1}_{K_a \times K_b}$ for almost every $w$, such that $f_w$ matches $\varphi_w$ with the character $\mu_w$ at every $w \in S$. Let $P_1$, $P_2$ be coprime elliptic polynomials of degrees $a$ and $b$, and $R = \mathrm{Res}(P_1, P_2)$. Then $SO_{P_1,P_2}(\varphi_w) = 1$ for all but finitely many $w \in S$, and
$$\prod_{w \in S}\kappa O_{P_1,P_2}(f_w) = \Big(\prod_v\epsilon_v(R)\Big)\prod_{w \in S}SO_{P_1,P_2}(\varphi_w).$$

Lean: `UpperTheory.ConvolutionTheory.G2.termId`.

*Proof.* The first claim follows from the [theorem on stable unit integrals](/entry/st-aa/), since $\varphi_w$ is the unit at almost every $w$. Next, at every $w$ the images of $P_1$ and $P_2$ are monic of degrees $a$ and $b$, their product is separable since $P_1P_2$ is, and they are conjugate self-reciprocal, since the roots of an elliptic polynomial have absolute value $1$ under every embedding. So matching gives $SO_{P_1,P_2}(\varphi_w) = \Delta_{\mu}(P_1, P_2)_w\,\kappa O_{P_1,P_2}(f_w)$ for $w \in S$.

The transfer factors satisfy a product formula: only finitely many $\Delta_\mu(P_1,P_2)_w$ differ from $1$, and
$$\Big(\prod_{w \in S}\Delta_\mu(P_1, P_2)_w\Big)\prod_v\epsilon_v(R) = 1.$$
To see this, the companion development computes each local factor as a product over the places $u$ of $E$ above the place of $F$ under $w$:
$$\Delta_\mu(P_1, P_2)_w = \prod_{u}\mu_u(R)\,|R|_u^{1/2}.$$
Since $S$ contains exactly one place above each finite place of $F$, the product over $w \in S$ is the product of $\mu_u(R)|R|_u^{1/2}$ over all finite places $u$ of $E$. The character $\mu$ is trivial on $E^\times$ and its archimedean component is $z \mapsto \prod_v(z_v/|z_v|)^{e_v}$ (part 4 of admissibility), so $\prod_u\mu_u(R)\prod_v(v(R)/|v(R)|)^{e_v} = 1$. The product formula for $R$, with the normalized absolute value $|v(R)|^2$ at a complex place, gives $\prod_u|R|_u^{1/2}\prod_v|v(R)| = 1$. Multiplying the two identities gives the product formula.

Now the products over $S$ are finite products up to factors $1$, and every $\Delta_\mu(P_1,P_2)_w$ is nonzero. So $\prod_{w \in S}\kappa O(f_w) = \prod_{w \in S}SO(\varphi_w)\big/\prod_{w \in S}\Delta_\mu(P_1,P_2)_w$, which is the claim by the product formula. $\square$

The last input is an identity of archimedean characters. Recall from Section 07 that $\mathrm{ch}_l(P) = \prod_v\overline{\mathrm{ch}_{l_v}(v(P))}$, and from Section 12 the multisets $\chi(l)$.

**Theorem 7.20.5 (Signed character identity).** Let $a + b = n$, let $e = (e_v)$ be a family of odd integers, and $\lambda = (\lambda_v)$ a family of dominant weights of $\mathrm{GL}_n$. There are a finite set $J$, families $l_{1,j}$, $l_{2,j}$ of dominant weights of $\mathrm{GL}_a$ and $\mathrm{GL}_b$, and signs $s_j \in \{\pm 1\}$, such that
$$\big(\chi(l_{1,j,v}) + \tfrac{be_v}{2}\big) + \big(\chi(l_{2,j,v}) + \tfrac{ae_v}{2}\big) = \chi(\lambda_v)$$
for all $j$ and $v$, and such that for all coprime elliptic $P_1$, $P_2$ of degrees $a$ and $b$, with $R = \mathrm{Res}(P_1, P_2)$,
$$\Big(\prod_v\epsilon_v(R)\Big)\mathrm{ch}_\lambda(P_1P_2) = \sum_{j \in J}s_j\,\mathrm{ch}_{l_{1,j}}(P_1)\,\mathrm{ch}_{l_{2,j}}(P_2).$$
If $a = 0$ or $b = 0$, one can take $J$ with one element and sign $1$.

This is proved in the companion development, place by place: at one archimedean place, for $\lambda_v$ and $e_v$ odd, the index set is the set of $a$-element subsets of $\{1, \dots, n\}$ and the signs are $\pm 1$. If $a = 0$, then $P_1 = 1$, $R = 1$, every $\epsilon_v(R)$ is $1$, and one takes $l_2 = \lambda$; the case $b = 0$ is the same.

**Theorem 7.20.6 (Signed stabilization).** Let $n \ge 1$, $(\mu, e)$ admissible and $\lambda$ a family of dominant weights of $\mathrm{GL}_n$. There are a finite set $I$, integers $0 \le a_i \le n$, families of dominant weights $l_{1,i}$, $l_{2,i}$ of $\mathrm{GL}_{a_i}$ and $\mathrm{GL}_{n-a_i}$ with
$$\big(\chi(l_{1,i,v}) + \tfrac{(n - a_i)e_v}{2}\big) + \big(\chi(l_{2,i,v}) + \tfrac{a_ie_v}{2}\big) = \chi(\lambda_v)$$
for all $i$ and $v$, and signs $s_i \in \{\pm 1\}$, with the following properties. There is exactly one $i$ with $a_i = n$, and its sign is $1$; there is exactly one $i$ with $a_i = 0$, and its sign is $1$. Let $S$ be a section, $K'$ a level family of $\mathrm{U}(n)$ and $f$ a test function of level $K'$. For every $a \le n$ let $\varphi_a$ be a local test family on $\mathrm{GL}_a \times \mathrm{GL}_{n-a}$ such that $f_w$ matches $\varphi_{a,w}$ with the character $\mu_w$ at every $w \in S$. Then
$$\mathcal{G}_U(S, \lambda, f) = \sum_{i \in I}s_i\,\mathcal{G}_{\mathrm{st}}(S, l_{1,i}, l_{2,i}, \varphi_{a_i}).$$

Lean: `UpperTheory.ConvolutionTheory.G2.g2s`.

*Proof.* For each $a \in \{0, \dots, n\}$ take the data $J_a$, $l_{1,j}$, $l_{2,j}$, $s_j$ of the signed character identity for $(a, n - a)$; it applies since every $e_v$ is odd (part 3 of admissibility). Let $I$ be the disjoint union of the $J_a$, with $a_i = a$ for $i \in J_a$. Since $J_0$ and $J_n$ have one element each, with sign $1$, the uniqueness claims hold.

Fix $S$, $K'$, $f$ and the $\varphi_a$. By definition, $\mathcal{G}_U(S, \lambda, f)$ is the sum over $a$ of the sum over coprime elliptic pairs $(P_1, P_2)$ of degrees $a$ and $n - a$ of $\mathfrak{m}(P_1P_2)\,\mathrm{ch}_\lambda(P_1P_2)\prod_{w \in S}\kappa O_{P_1,P_2}(f_w)$. Fix $a$ and such a pair. The companion development proves $\mathfrak{m}(P_1P_2) = \mathfrak{m}(P_1)\,\mathfrak{m}(P_2)$ for coprime elliptic polynomials. The [theorem on products of $\kappa$-orbital integrals](/entry/term-id/), applied to $\varphi_a$, replaces the product of $\kappa$-orbital integrals by $\prod_v\epsilon_v(R)$ times the product of stable integrals. The signed character identity then turns $\prod_v\epsilon_v(R)\,\mathrm{ch}_\lambda(P_1P_2)$ into $\sum_j s_j\,\mathrm{ch}_{l_{1,j}}(P_1)\,\mathrm{ch}_{l_{2,j}}(P_2)$. So the term of $(P_1, P_2)$ is
$$\sum_{j \in J_a}s_j\,\mathfrak{m}(P_1)\,\mathfrak{m}(P_2)\,\mathrm{ch}_{l_{1,j}}(P_1)\,\mathrm{ch}_{l_{2,j}}(P_2)\prod_{w \in S}SO_{P_1,P_2}(\varphi_{a,w}).$$

It remains to exchange the sum over $j$ with the sum over pairs. The companion development proves that only finitely many elliptic pairs $(P_1, P_2)$ of degrees $a$ and $n - a$ have $SO_{P_1,P_2}(\varphi_{a,w}) \ne 0$ for all $w \in S$, for a family $\varphi_a$ of compactly supported functions equal to the unit almost everywhere. If the product over $S$ of these integrals is nonzero, then each factor is nonzero, since only finitely many factors differ from $1$. So all the sums run over one finite set of pairs, the exchange is allowed, and the sum over the pairs of degrees $(a, n-a)$ is $\sum_{j \in J_a}s_j\,\mathcal{G}_{\mathrm{st}}(S, l_{1,j}, l_{2,j}, \varphi_a)$. Summing over $a$ gives the claim. $\square$

**Remark 7.20.7.** The theorem has the shape of the [stabilization of Section 12](/entry/chain-existence-of-global-character/), with signs $\pm 1$ in place of nonzero coefficients.

**Remark 7.20.8 (Formalization).** Integral uniqueness is [IntUniq.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/OrbitNormCounting/IntUniq.lean#L36); the split case uses `conjSep` and `eventually_separable_of_integral_model`, the nonsplit case uses `transl` and `unitary_involution_stabilizes_integral_at_nonsplit`, whose proof we did not unfold. The statements `IntUniq`, `CptInt`, `OrbUnit` and `UnitAe` are in OrbitNormCounting/NormCount.lean (lines 33 to 51), and the unit integral is [UnitAe.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/OrbitNormCounting/UnitAe.lean#L71); its hypotheses on $P_{y_i}$ are used only in the vanishing case. The stable unit integral is [LpolTwist.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/WeightRankUnits/LpolTwist.lean#L46). The statement `TermId` ([DeltaProdAlt.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/WeightRankUnits/DeltaProdAlt.lean#L73)) takes $n$, $a$ and $b$ without the condition $a + b = n$; the proof (TermId.lean, line 24) does not need it. We did not open the proof of `deltaLoc`. The signed character identity is `realProdS` (RealProdS.lean, line 31). The statement `G2s` is in GlobalTraceComparison/StableBlock.lean (line 21) and the proof `g2s` in [NeZeroOfFinprod.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/WeightRankUnits/NeZeroOfFinprod.lean#L40). Of the admissibility of $(\mu, e)$, the proof of `g2s` uses directly only that every $e_v$ is odd; the rest enters through `termId`.
