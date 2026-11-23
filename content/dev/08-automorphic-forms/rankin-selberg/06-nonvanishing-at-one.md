---
title: Nonvanishing at s = 1
decls:
  - GlobalTheory.RSNonvan.offDiag
  - GlobalTheory.RSNonvan.tendsto_partialL_ne_zero
  - GlobalTheory.T.rankinSelberg_partialL_tendsto_ne_zero_at_one
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Nonvanishing at s = 1

Let $\sigma$ and $\sigma'$ be two different unitary cuspidal representations, of $\mathrm{GL}_a$ and $\mathrm{GL}_b$. This section proves that $L^T(x, \sigma \times \bar\sigma')$ has a finite nonzero limit as $x \to 1^+$. This is the nonvanishing on the line $\operatorname{Re} s = 1$ of Jacquet and Shalika and of Shahidi, at the single point $s = 1$ ([Rankin-Selberg integrals](/learn/trace-formula/#rankin-selberg-integrals)). The proof has two parts. First, [the off-diagonal lemma](/entry/rsnonvan-off-diag/) puts together [the integral for $\mathrm{GL}_n \times \mathrm{GL}_m$](/entry/rs-nm-partial-l-eq-div/) and [the same-degree continuation](/entry/samedeg-continuation/): $L^T(x, \sigma \times \bar\sigma')$ extends to a function that is analytic at each real $x > 0$. Second, a positivity argument of Landau type shows that this function does not vanish at $1$. [The bound on the logarithm](/entry/abs-re-log-rs-bdd/) of the next section uses the result.

We keep the notation of [the first section](/entry/cell-lintegral/): $\ell_w(\sigma, \sigma', x)$ is the local factor at $w$, $p_k$ is the $k$-th power sum, and a set $T$ is good in the sense of [the previous section](/entry/zint-eq-mul-partial-l-smooth/). All the representations are unitary and cuspidal, of degree at least $1$, and unramified outside $T$. "Different" means different as pairs $(a, \sigma)$, so representations of different degrees are always different.

**Lemma 8.6.1 (Good sets are cofinal).** Every finite set $T$ of finite places of $E$ is contained in a good finite set $T'$.

Lean: `GlobalTheory.RSNonvan.exists_isGood_superset_all` (also `GlobalTheory.T.exists_goodRankinSelbergPlaceSet_superset_totallyComplex`, a wrapper).

*Proof.* The character $\psi_w$ has conductor $\mathcal{O}_w$ for all but finitely many $w$. Add these finitely many places to $T$. Then add every place that lies over the same rational prime as a place of the set. Each rational prime has finitely many places above it, so the result is finite, and it is saturated. $\square$

**Lemma 8.6.2 (Strict bound on Satake parameters).** Let $\sigma$ be a unitary cuspidal representation of $\mathrm{GL}_a$, $a \ge 1$, unramified outside $T$. Then $|\alpha|^2 < Nw$ for every $w \notin T$ and every $\alpha \in \mathrm{sat}(\sigma, w)$.

Lean: `GlobalTheory.RSStrict.norm_sq_lt_absNorm` (also `GlobalTheory.T.satakeParameter_normSq_lt_absNorm_unitaryCusp`, a wrapper).

*Proof.* Write $q = Nw$. Let $L_1$ and $L_2$ be the functions that [the pole theorem](/entry/cell-lintegral/) gives for $\sigma \times \bar\sigma$ with the sets $T$ and $T \cup \{w\}$. For $x > 1$ we have $L_1(x) = \ell_w(\sigma, \sigma, x) L_2(x)$, and $L_1, L_2 \ge 1$. The factor $\ell_w(\sigma, \sigma, x)$ contains the pair $(\gamma, \bar\gamma)$ for each $\gamma \in \mathrm{sat}(\sigma, w)$, with the factor $(1 - |\gamma|^2 q^{-x})^{-1}$.

First suppose that $|\gamma|^2 > q$ for some $\gamma$. Put $x_0 = \log |\gamma|^2 / \log q > 1$. Then $1 - |\gamma|^2 q^{-x_0} = 0$, so the local factor at $x_0$ is not a finite nonzero number, while $L_1(x_0)$ and $L_2(x_0)$ are finite and $\ge 1$. This is a contradiction, so $|\gamma|^2 \le q$ for all $\gamma$.

Next suppose that $|\alpha|^2 = q$. Put $t(x) = q^{1 - x} < 1$ for $x > 1$. Every other pair $(\gamma, \bar\delta)$ has $|\gamma\delta| q^{-x} \le t(x) < 1$, so its factor has absolute value at least $1/2$. If $r + 1$ is the number of pairs, then $(1 - t(x))|\ell_w(\sigma, \sigma, x)| \ge 2^{-r}$. But $|\ell_w| = (x - 1)L_1(x) / ((x - 1)L_2(x))$ tends to $c_1 / c_2$ as $x \to 1^+$, with $c_1, c_2 > 0$, and $1 - t(x) \to 0$. So the left side tends to $0$, which is a contradiction. $\square$

**Lemma 8.6.3 (Conjugate symmetry).** For real $x > 1$, $L^T(x, \sigma' \times \bar\sigma) = \overline{L^T(x, \sigma \times \bar\sigma')}$.

Lean: `GlobalTheory.RSConj.partial_conj` (also `GlobalTheory.T.partial_rankinSelberg_product_conj_swap_real`, a wrapper).

*Proof.* For real $x$, the complex conjugate of $(1 - \alpha\bar\beta q^{-x})^{-1}$ is $(1 - \beta\bar\alpha q^{-x})^{-1}$. So $\ell_w(\sigma', \sigma, x) = \overline{\ell_w(\sigma, \sigma', x)}$ for each $w$. Both products converge by [the logarithm lemma](/entry/cell-lintegral/), and conjugation is continuous. $\square$

**Theorem 8.6.4 (Off-diagonal continuation).** Let $T$ be good, and let $\sigma$ on $\mathrm{GL}_a$ and $\sigma'$ on $\mathrm{GL}_b$ be different unitary cuspidal representations, unramified outside $T$. Then there is a function $G$ on $\mathbb{C}$, analytic at each real $x > 0$, such that $\prod_{w \notin T} \ell_w(\sigma, \sigma', x)$ converges to $G(x)$ for every real $x > 1$.

Lean: `GlobalTheory.RSNonvan.offDiag`.

*Proof.* We compare $a$ and $b$.

1. If $a > b$, [the theorem for $\mathrm{GL}_n \times \mathrm{GL}_m$](/entry/rs-nm-partial-l-eq-div/) gives entire $F$ and $H$, with $\operatorname{Re} H(x) > 0$ for real $x$, and $L^T(x, \sigma \times \bar\sigma') = F(x)/H(x)$ for $x > 1$. Put $G = F/H$. It is analytic on the open set where $H \neq 0$, which contains the real line.
2. If $a < b$, apply the same theorem to $(\sigma', \sigma)$, which gives $F$ and $H$ with $L^T(x, \sigma' \times \bar\sigma) = F(x)/H(x)$. Put $G(z) = \overline{F(\bar z)/H(\bar z)}$. This function is analytic where $H(\bar z) \neq 0$, so near the real line. By conjugate symmetry, $L^T(x, \sigma \times \bar\sigma') = G(x)$ for $x > 1$.
3. If $a = b$, then $\sigma \neq \sigma'$. [The same-degree continuation](/entry/samedeg-continuation/) gives $F$, analytic at each real $x > 0$, with $F(1) = 0$ and $L^T(x, \sigma \times \bar\sigma') = F(x)/(x - 1)$ for $x > 1$. Let $G$ be the difference quotient of $F$ at $1$: $G(z) = (F(z) - F(1))/(z - 1)$ for $z \neq 1$ and $G(1) = F'(1)$. It is analytic at each point where $F$ is analytic. Since $F(1) = 0$, $G(x) = F(x)/(x - 1)$ for $x > 1$.

In each case the product converges for $x > 1$ by [the logarithm lemma](/entry/cell-lintegral/). $\square$

The analyticity holds only at the real points $x > 0$. This is all that the next lemma needs.

**Lemma 8.6.5 (Landau).** Let $(a_i)$ and $(l_i)$ be families of real numbers $\ge 0$, let $x_0 < x_1$, and let $G$ be analytic at each real $x > x_0$. Suppose that for each $x > x_1$ the series $\sum_i a_i e^{-l_i x}$ converges to a sum $g(x)$ with $G(x) = e^{g(x)}$. Then the same holds for each $x > x_0$.

Lean: `GlobalTheory.landau_exp_hasSum_of_analyticAt`.

*Proof.* First take the case without the exponential: $\sum_i a_i e^{-l_i x}$ converges to $F(x)$ for $x > x_1$, and $F$ is analytic at each $x > x_0$. Let $t$ be the infimum of the points $t' \ge x_0$ such that the series converges to $F$ on $(t', \infty)$, and suppose that $t > x_0$. Then $F$ is analytic on a disc about $t$ of some radius $\rho$. Take $y > t$ with $y - t < \rho/2$. The $k$-th derivative of $F$ at $y$ is $\sum_i a_i (-l_i)^k e^{-l_i y}$. The Taylor series of $F$ at $y$ converges at a point $y - h$ with $y - h < t$. All its terms $\frac{h^k}{k!} \sum_i a_i l_i^k e^{-l_i y}$ are $\ge 0$, so we can interchange the two sums, and the result is $\sum_i a_i e^{-l_i (y - h)}$. So the series converges at $y - h$, hence on $(y - h, \infty)$, since its terms decrease in $x$. Its sum is analytic there and agrees with $F$ near $y$, so it equals $F$ on $(y - h, \infty)$. As $y - h < t$, this contradicts the choice of $t$.

For the exponential form, expand $e^{g(x)} = \sum_n g(x)^n / n!$ as a series over tuples $(i_1, \dots, i_n)$ with coefficients $a_{i_1} \cdots a_{i_n}/n! \ge 0$ and exponents $l_{i_1} + \dots + l_{i_n} \ge 0$. The first case applies to this series and to $G$. The terms with $n = 1$ form a subseries with nonnegative terms, so $\sum_i a_i e^{-l_i x}$ converges for $x > x_0$. Its exponential equals $G(x)$ by continuation from $x > x_1$. $\square$

**Lemma 8.6.6 (A large power sum).** Let $A$ be a multiset of $N \ge 1$ complex numbers whose product has absolute value $1$. Then $|p_r(A)| \ge 1$ for some $1 \le r \le N$. Consequently, if $A_w$ is such a multiset for each $w \notin T'$ and $0 < x \le 1/N$, then
$$\sum_{w \notin T'} \sum_{r \ge 0} \frac{|p_{r+1}(A_w)|^2\, Nw^{-(r+1)x}}{r + 1} = \infty.$$

Lean: `GlobalTheory.PowerSumDiv.not_summable_psum_sq`.

*Proof.* Let $e_k$ be the elementary symmetric functions of $A$. Suppose that $|p_r| \le c$ for $1 \le r \le N$, with $c \le 1$. Newton's identity $k e_k = \sum_{i=1}^{k} (-1)^{i-1} e_{k-i} p_i$ and induction on $k$ give $|k e_k| \le c + (k - 1)c^2 \le kc$, so $|e_k| \le c$. For $k = N$, $|e_N| = 1$, so $c \ge 1$. This proves the first claim. For the second, choose $r_w \le N$ with $|p_{r_w}(A_w)| \ge 1$. The term with $r + 1 = r_w$ is at least $Nw^{-r_w x}/N \ge Nw^{-1}/N$, since $r_w x \le 1$. And $\sum_w Nw^{-1}$ diverges. $\square$

**Theorem 8.6.7 (Nonvanishing at $s = 1$).** Let $T$ be a finite set of finite places of $E$, and let $\sigma$ on $\mathrm{GL}_a$ and $\sigma'$ on $\mathrm{GL}_b$ be different unitary cuspidal representations, with $a, b \ge 1$, unramified outside $T$. Then there is $z \neq 0$ such that $L^T(x, \sigma \times \bar\sigma') \to z$ as $x \to 1^+$.

Lean: `GlobalTheory.RSNonvan.tendsto_partialL_ne_zero` (also `GlobalTheory.T.rankinSelberg_partialL_tendsto_ne_zero_at_one`, a wrapper).

*Proof.* The steps are as follows.

1. Choose a good $T' \supseteq T$, by the first lemma. Both representations are unramified outside $T'$.
2. Apply the off-diagonal theorem to $(\sigma, \sigma')$ and to $(\sigma', \sigma)$ on $T'$. This gives $G$ and $G'$. Apply the same-degree continuation to $(\sigma, \sigma)$ and to $(\sigma', \sigma')$. This gives $D$ and $D'$, analytic at each real $x > 0$, with $L^{T'}(x, \sigma \times \bar\sigma) = D(x)/(x - 1)$ and $L^{T'}(x, \sigma' \times \bar\sigma') = D'(x)/(x - 1)$ for $x > 1$. Since $G$ is analytic at $1$, $L^{T'}(x, \sigma \times \bar\sigma') \to G(1)$.
3. Suppose that $G(1) = 0$. By conjugate symmetry, $G'(x) = \overline{G(x)}$ for $x > 1$, so $G'(1) = 0$ too. Let $P = D \cdot D' \cdot \tilde G \cdot \tilde G'$, where $\tilde G$ and $\tilde G'$ are the difference quotients of $G$ and $G'$ at $1$. Then $P$ is analytic at each real $x > 0$, and $P(x)$ is the product of the four partial L-functions of $(\sigma, \sigma)$, $(\sigma', \sigma')$, $(\sigma, \sigma')$ and $(\sigma', \sigma)$ for $x > 1$.
4. By part (1) of [the logarithm lemma](/entry/cell-lintegral/), the sum of the four logarithms at $w$ has the coefficient
$$p_k \bar p_k + p'_k \bar p'_k + p_k \bar p'_k + p'_k \bar p_k = |p_k + p'_k|^2$$
at $Nw^{-kx}/k$, where $p_k = p_k(\mathrm{sat}(\sigma, w))$ and $p'_k = p_k(\mathrm{sat}(\sigma', w))$. So $P(x) = \exp \sum_{w \notin T'} \sum_{r \ge 0} c_{w,r} e^{-(r+1) x \log Nw}$ with $c_{w,r} = |p_{r+1} + p'_{r+1}|^2/(r+1) \ge 0$, for all $x > 1$.
5. Landau's lemma with $x_0 = 0$ and $x_1 = 1$ shows that this series converges at $x = 1/(a + b)$.
6. Let $A_w = \mathrm{sat}(\sigma, w) + \mathrm{sat}(\sigma', w)$. It has $a + b$ elements, and its product has absolute value $1$, because the central character of a unitary representation is unitary. So $p_k(A_w) = p_k + p'_k$, and the lemma on a large power sum says that the series of step 5 diverges at $1/(a + b)$. This contradiction shows that $G(1) \neq 0$.
7. Now return to $T$. For $x > 1$, $L^T = \prod_{w \in T' \setminus T} \ell_w \cdot L^{T'}$. By the strict bound, every $\alpha \in \mathrm{sat}(\sigma, w)$ and $\beta \in \mathrm{sat}(\sigma', w)$ have $|\alpha\beta| < Nw$, so each factor $\ell_w(\sigma, \sigma', x)$ is continuous at $x = 1$ and $\ell_w(\sigma, \sigma', 1) \neq 0$. Thus $z = \prod_{w \in T' \setminus T} \ell_w(\sigma, \sigma', 1) \cdot G(1) \neq 0$. $\square$

For unitary $\sigma'$ the conjugate parameters are those of the contragredient, so the limit is the value $L^T(1, \sigma \times \tilde\sigma') \neq 0$.

**Remark 8.6.8 (Formalization).** The two theorems are in [RankinSelbergPartialLTendstoNeZeroAtOne.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/RankinSelbergPartialLTendstoNeZeroAtOne.lean#L66), at lines 66 and 117. The local factor `lfac`, the predicate `IsGood` and the coefficients `dcoef` and exponents `dexp` of the positive series are in [IsGoodEmptyIff.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/IsGoodEmptyIff.lean#L13). The off-diagonal theorem gives analyticity only at real points. In the two cases $a \neq b$ it passes only the conductor half of `IsGood` to the theorem for $\mathrm{GL}_n \times \mathrm{GL}_m$. The difference quotient is Mathlib's `dslope`, and `analyticAt_dslope'` at line 23 proves that it keeps analyticity. The nonvanishing theorem takes an arbitrary finite $T$, while its inputs need a good set; step 1 bridges the two. The four-product identity is `fourProd_eq_exp` in [DirichletSeriesExponentialSumConverges.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/DirichletSeriesExponentialSumConverges.lean#L46). Landau's lemma is in [GenDirichletHasSumIteratedDeriv.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/GenDirichletHasSumIteratedDeriv.lean#L267), and the power-sum lemma is in [ExistsOneLeNormPsumMultiset.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsOneLeNormPsumMultiset.lean#L123). In the proof of the strict bound, the case $|\gamma|^2 > q$ uses the Lean convention $0^{-1} = 0$: the factor at $x_0$ is $0$, so the product would be $0$, against $L_1 \ge 1$ ([SatakeParameterNormSqLtAbsNormUnitaryCusp.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/SatakeParameterNormSqLtAbsNormUnitaryCusp.lean#L109)). The wrappers in the `GlobalTheory.T` namespace are `...Statement` files whose proof tries three forms of `exact` with `first`, under `set_option maxHeartbeats 1000000`.
