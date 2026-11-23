---
title: Rank one theta means
decls:
  - GlobalTheory.CompanionTheory.SW.RankOneSiegelWeil.lside
  - GlobalTheory.T.l_function_side_equidistribution
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Rank one theta means

This section applies the [equidistribution theorem](/entry/equi/) to theta series of a unitary group in one variable. We average a theta series over the compact quotient $U(1)(F) \backslash U(1)(\mathbb{A})$ and study the mean as a function of an idele. The result has three parts: the mean is $O(|n|^{-1})$, it vanishes when $|n|$ is large, and along a ray it has the limit given by the volume of the test data. The result is an input of the [base case of the Siegel-Weil formula](/entry/base-one-of/). The background is in [the Weil representation](/learn/theta/#the-weil-representation) and in Weil's paper on the Siegel formula cited at the end of the chapter.

**Setting.** Let $E/F$ be a CM extension of degree $2$, with $d = [F:\mathbb{Q}]$, and let $J = (j)$ be a nonzero Hermitian $1 \times 1$ matrix, so $j \in F^\times$. The unitary group is
$$U(\mathbb{A}) = \{ h \in \mathbb{A}_E^\times : \bar h h = 1 \},$$
a compact abelian group modulo the discrete group $U(F) = \{ h \in E^\times : \bar h h = 1 \}$. Let $\mu$ be a Haar measure on $U(\mathbb{A})$ and $\mathcal{F}$ a measurable fundamental domain for $U(F)$. Fix a basis $b$ of $E$ over $F$. Through $b$, the standard measures of the [previous section](/entry/equi/) give Haar measures on $\mathbb{A}_\infty \otimes_F E$ and on each $E_v$. For $v$ finite, let $\Lambda_v \subset E_v$ be the $\mathcal{O}_v$-span of $b$.

**Definition 3.6.1 (Test data).** Let $S$ be a finite set of finite places. A test datum for $S$ is a pair $(\phi, A)$ where:

1. $\phi : \mathbb{A}_\infty \otimes E \to \mathbb{R}$ is continuous, nonnegative, with compact support contained in the set where the Hermitian norm $\bar X j X$ is invertible;
2. for $v \in S$, $A_v \subset E_v$ is compact and open and contained in $E_v^\times$;
3. for $v \notin S$, $A_v = \Lambda_v$.

Its volume is
$$\operatorname{vol}(\phi, A) = \int_{\mathbb{A}_\infty \otimes E} \phi \, dX \cdot \prod_{v \in S} \operatorname{vol}(A_v).$$

**Definition 3.6.2 (Theta sum and theta mean).** For $y \in \mathbb{A}_E^\times$ put
$$\Theta(y) = \sum_{X \in E^\times} \phi\bigl((yX)_\infty\bigr) \, \mathbf{1}\bigl[ (yX)_v \in A_v \text{ for all finite } v \bigr].$$
The theta mean at $x \in \mathbb{A}_E^\times$ is
$$m(x) = \frac{1}{\mu(\mathcal{F})} \int_{\mathcal{F}} \sum_{X \in E^\times} \phi\bigl((x h^{-1} X)_\infty\bigr)\, \mathbf{1}\bigl[(x h^{-1} X)_v \in A_v \ \forall v\bigr] \, d\mu(h).$$

We say that $n \in \mathbb{A}^\times$ is the norm of $x$ if $n = \bar x x$. A ray is a map $r : (0, \infty) \to \mathbb{A}^\times$ such that $r(\delta)$ has archimedean part $\theta(\delta)$ and finite part $1$, for a continuous ring homomorphism $\theta : \mathbb{R} \to \mathbb{A}_\infty$. So $r(\delta)$ is the idele $\delta$ placed at every archimedean place, and its module is $|r(\delta)| = \delta^{d}$. Note that $r(\varepsilon)^2 = r(\varepsilon^2)$.

We take the following facts as given. They are statements about the theta sum $\Theta$, which is a sum over a lattice coset.

- (Decomposition of ideles.) There is a compact set $K \subset \mathbb{A}_E^\times$ such that every $y$ with norm $n$ can be written $y = q\, k\, r(\varepsilon)$ with $q \in E^\times$, $k \in K$, $\varepsilon > 0$ and $|n| = \varepsilon^{2d}$.
- (Invariance.) $\Theta(qy) = \Theta(y)$ for $q \in E^\times$.
- (Large norms.) There is $R$ such that $\Theta(y) = 0$ whenever the norm $n$ of $y$ has $|n| > R$.
- (Uniform bound.) Assume the [equidistribution theorem](/entry/equi/). For compact $K$ and $\varepsilon_1 > 0$ there is $C$ with $\varepsilon^{2d}\, \Theta(k\, r(\varepsilon)) \le C$ for $k \in K$ and $0 < \varepsilon \le \varepsilon_1$.
- (Limit along the ray.) Assume the equidistribution theorem. If $y$ has norm $n$ and $\Theta(y\, r(\varepsilon))$ is finite for small $\varepsilon$, then $\varepsilon^{2d}\, \Theta(y\, r(\varepsilon)) \to |n|^{-1} \operatorname{vol}(\phi, A)$ as $\varepsilon \to 0^+$.
- (Unfolding.) $m(x) = \mu(\mathcal{F})^{-1} \int_{\mathcal{F}} \Theta(x h^{-1}) \, d\mu(h)$, and the integrand is measurable.
- (Volume.) $U(F)$ is discrete in $U(\mathbb{A})$ and $0 < \mu(\mathcal{F}) < \infty$.

The bound and the limit are where equidistribution enters. With $E \cong F^2$ through $b$, the sum $\Theta(k\, r(\varepsilon))$ is a sum over $X \in F^2$ of $\phi(\varepsilon k_\infty X)$ times local conditions at finitely many places. This is the sum of the equidistribution theorem with $|\iota| = 2$, and the factor $\varepsilon^{2d}$ is the factor $\varepsilon^{d|\iota|}$ there. Scaling by $y$ changes the volume by $|N(y)| = |n|$, which explains the factor $|n|^{-1}$.

**Theorem 3.6.3 (Asymptotics of rank one theta means).** Assume the equidistribution theorem. Let $E/F$ be a CM extension, $J$ a nonzero Hermitian $1 \times 1$ matrix, $\mu$ a Haar measure on $U(\mathbb{A})$, $\mathcal{F}$ a fundamental domain, $b$ a basis of $E/F$, and $\lambda_\infty$, $\lambda_v$ standard measures. Let $r$ be a ray, $S$ a finite set of finite places and $(\phi, A)$ a test datum for $S$. Then:

1. there is $C$ such that $|n|\, m(x) \le C$ for all $x$ with norm $n$;
2. there is $R$ such that $m(x) = 0$ for all $x$ whose norm $n$ has $|n| > R$;
3. for every $x$ with norm $n$,
$$|n\, r(\varepsilon^2)|\; m\bigl(x\, r(\varepsilon)\bigr) \longrightarrow \operatorname{vol}(\phi, A) \qquad (\varepsilon \to 0^+).$$

Lean: `GlobalTheory.CompanionTheory.SW.RankOneSiegelWeil.lside` (also `GlobalTheory.T.l_function_side_equidistribution`, a second name).

*Proof.* First a bound for $\Theta$: there is $C$ with $|n|\,\Theta(y) \le C$ for every $y$ of norm $n$. Write $y = q\, k\, r(\varepsilon)$ with $|n| = \varepsilon^{2d}$. By invariance, $\Theta(y) = \Theta(k\, r(\varepsilon))$. Let $\varepsilon_1 = \max(1, R)$. If $\varepsilon \le \varepsilon_1$, the uniform bound gives $|n|\, \Theta(y) = \varepsilon^{2d}\, \Theta(k\, r(\varepsilon)) \le C$. If $\varepsilon > \varepsilon_1$, then $|n| = \varepsilon^{2d} \ge \varepsilon > R$, and $\Theta(y) = 0$ by the bound for large norms.

Every $h \in U(\mathbb{A})$ has $\bar h h = 1$, so $x h^{-1}$ has the same norm $n$ as $x$. Now:

1. By unfolding, $|n|\, m(x)$ is the average over $\mathcal{F}$ of $|n|\, \Theta(x h^{-1}) \le C$, so it is at most $C$. Here $\mu(\mathcal{F})$ is finite and nonzero.
2. If $|n| > R$, then $\Theta(x h^{-1}) = 0$ for every $h$, so $m(x) = 0$.
3. The idele $x\, r(\varepsilon)$ has norm $n\, r(\varepsilon^2)$, and $|n\, r(\varepsilon^2)| = |n|\, \varepsilon^{2d}$. So
$$|n\, r(\varepsilon^2)|\, m\bigl(x r(\varepsilon)\bigr) = \frac{1}{\mu(\mathcal{F})} \int_{\mathcal{F}} |n|\, \varepsilon^{2d}\, \Theta\bigl(x h^{-1} r(\varepsilon)\bigr) \, d\mu(h).$$
For each $h$ the integrand tends to $|n| \cdot |n|^{-1} \operatorname{vol}(\phi, A) = \operatorname{vol}(\phi, A)$, by the limit along the ray applied to $y = x h^{-1}$; the finiteness it needs follows from the bound for $\Theta$. The integrand is bounded by $C$, and $\mathcal{F}$ has finite measure. By dominated convergence the integral tends to $\mu(\mathcal{F}) \operatorname{vol}(\phi, A)$, and the claim follows. $\square$

The three conclusions control the theta mean as a function of the norm $n$. By the first two, $m(x)$ is bounded by $C|n|^{-1}$ and has support in $|n| \le R$, so an integral of $m(x)\,|n|^{s}$ over ideles of bounded module converges for $\operatorname{Re} s > 1$. By the third, $|n|\, m(x)$ tends to $\operatorname{vol}(\phi, A)$ as the norm shrinks along the ray. This is the behaviour of the integrand of a Tate integral near its pole at $s = 1$.

**Remark 3.6.4 (Formalization).** The theorem is an implication: it assumes the proposition that the equidistribution theorem holds for all totally real fields. That proposition is proved in the [previous section](/entry/equi/), so the hypothesis is discharged in the proof. The facts listed above are statements of the form `GlobalTheory.T.*` (`idele_class_compact_ray_decomposition`, `theta_series_invariant_rational_units`, `theta_test_function_bounded_large_norm`, `rank_one_theta_integral_ray_formula`, `rank_one_theta_integral_ray_limit`, `rank_one_siegel_weil_theta_average`, `unitary_group_finite_volume`, `finite_covolume_unimodular`, `ray_norm_and_module_formula`, `unitary_scalar_has_norm_one`). The bound and the limit along the ray each take the equidistribution theorem as a hypothesis. The measures `mi` and `m` on the fibres of the Hermitian norm are part of the setting but are not used in this theorem. See [LFunctionSideEquidistribution.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/LFunctionSideEquidistribution.lean#L77).
