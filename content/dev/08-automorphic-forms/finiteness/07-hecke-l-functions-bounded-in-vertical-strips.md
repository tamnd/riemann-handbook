---
title: Hecke L-functions bounded in vertical strips
decls:
  - GlobalTheory.HeckeStrip.completedLBoundedInStrips
  - GlobalTheory.T.completed_heckePartialLSeries_entire_bounded_strips
  - GlobalTheory.HeckeStrip.completed_pSeries_entire_bounded
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Hecke L-functions bounded in vertical strips

This section proves that the completed L-function of a unitary Hecke character of a totally complex field, with a nontrivial infinity type, is entire and bounded in every vertical strip. The proof is the method of Hecke: split the L-series into partial series over principal ideals in fixed classes, write each partial series as a Mellin transform of a theta function, and use Poisson summation for the theta function. Characters of this kind are the one-dimensional [automorphic representations](/learn/automorphic-forms/#automorphic-representations) of $\mathrm{GL}_1$, and the result is an input to [the step on every character of a row](/step/every-character-of-row/).

### Characters and completed L-functions

Let $E$ be a totally complex number field, with ring of integers $\mathcal{O}_E$ and idele group $\mathbb{A}_E^\times$. A *Hecke character* is a continuous homomorphism $\chi : \mathbb{A}_E^\times \to \mathbb{C}^\times$ that is trivial on the diagonal image of $E^\times$. It is *unitary* if $|\chi(x)| = 1$ for all $x$. It is *unramified* at a finite place $v$ if it is trivial on the units of $E_v$, and then $\chi(\varpi_v)$ is its value at a uniformizer. The *Euler factor* at $v$ is
$$L_v(\chi, s) = (1 - \chi(\varpi_v) \operatorname{N}v^{-s})^{-1}$$
if $\chi$ is unramified at $v$, and $1$ if not.

Let $I$ be a finite set and $\varphi = (\varphi_i)_{i \in I}$ a family of embeddings $E \to \mathbb{C}$. It is a *CM type* if each embedding $\sigma$ is $\varphi_i$ or $\bar\varphi_i$ for exactly one $i$. Let $n \in \mathbb{Z}^I$. We say $\chi$ has *infinity type* $n$ if
$$\chi_\infty(k) = \prod_{i \in I} \Big(\frac{\varphi_i(k)}{|\varphi_i(k)|}\Big)^{n_i} \quad \text{for all } k \in E^\times,$$
where $\chi_\infty$ is the restriction of $\chi$ to the archimedean ideles and $k$ is placed there diagonally. Define the archimedean factor
$$\gamma_n(s) = \prod_{i \in I} 2 (2\pi)^{-(s + |n_i|/2)}\, \Gamma\big(s + |n_i|/2\big).$$
An entire function $\Lambda$ is a *completed L-function* of $(\chi, n)$ if, for $\operatorname{Re} s > 1$, the product $\prod_v L_v(\chi, s)$ over the finite places converges to a number $L$ with $\Lambda(s) = \gamma_n(s) L$. Two such functions agree on a half plane, so they are equal. A function $\Lambda$ is *bounded in vertical strips* if for all real $a < b$ there is $C$ with $|\Lambda(s)| \le C$ when $a \le \operatorname{Re} s \le b$.

### Partial series over principal ideals

For $\alpha \in E^\times$ put
$$\operatorname{wt}(\alpha) = \prod_{i \in I} \Big(\frac{\varphi_i(\alpha)}{|\varphi_i(\alpha)|}\Big)^{-n_i},$$
a number of absolute value $1$ with $\operatorname{wt}(\alpha \beta) = \operatorname{wt}(\alpha) \operatorname{wt}(\beta)$. Let $M \neq 0$ be an ideal of $\mathcal{O}_E$ and $F : \mathcal{O}_E \to \mathbb{C}$ a function with $F(\alpha + \mu) = F(\alpha)$ for $\mu \in M$ and $F(u\alpha)\operatorname{wt}(u\alpha) = F(\alpha)\operatorname{wt}(\alpha)$ for all units $u$. Then $F(\alpha)\operatorname{wt}(\alpha)$ depends only on the ideal $(\alpha)$, and the *partial series* is
$$P_F(s) = \sum_{J} F(\alpha_J)\operatorname{wt}(\alpha_J) \operatorname{N}J^{-s},$$
over the nonzero principal ideals $J = (\alpha_J)$.

For the proof we use theta functions. For $z \in \mathbb{C}$ and $m \in \mathbb{Z}$ let $h_m(z) = \bar z^m$ if $m \ge 0$ and $h_m(z) = z^{-m}$ if $m < 0$. For $w \in \mathbb{C}^I$ let $G_n(w) = \prod_i h_{n_i}(w_i) e^{-2\pi |w_i|^2}$. For $y \in \mathbb{R}^I$ let $y \cdot w = (e^{y_i/2} w_i)_i$. For a family of points $e_j \in \mathbb{C}^I$ and coefficients $a_j$, the theta function is
$$\theta(y) = \sum_j a_j\, G_n(y \cdot e_j).$$
We write $\theta_F$ for the choice $e_\alpha = (\varphi_i(\alpha))_i$ and $a_\alpha = F(\alpha)$, with $\alpha \in \mathcal{O}_E$. Note that $G_n(0) = 0$ when some $n_i \neq 0$.

**Theorem 1.7.1 (Completed partial series).** Let $E$ be totally complex, $\varphi$ a CM type, $n \in \mathbb{Z}^I$ with some $n_i \neq 0$, and $M$, $F$ as above. Then there is an entire function $\Lambda$, bounded in vertical strips, with $\Lambda(s) = \gamma_n(s) P_F(s)$ for $\operatorname{Re} s > 1$.

Lean: `GlobalTheory.HeckeStrip.completed_pSeries_entire_bounded` (also `GlobalTheory.T.completed_heckePartialLSeries_entire_bounded_strips`, a second name).

*Proof.* For a unit $u$ let $\ell(u) = (\log |\varphi_i(u)|^2)_i \in \mathbb{R}^I$. There is a measurable function $p \ge 0$ on $\mathbb{R}^I$ with $\sum_u p(y + \ell(u)) = 1$ for all $y$, and a number $R$ such that $y_i - y_j \le R$ for all $i, j$ when $p(y) \neq 0$. In particular $0 \le p \le 1$. The function $F$ is bounded, since it is periodic modulo $M$, and the Gaussian sums of $|F|$ converge.

Poisson summation for $\theta_F$ gives coefficients $a$ on $\mathbb{C}^I$ and a constant $\kappa$ such that
$$\theta_F(y) = \kappa\, e^{-\sum_i y_i}\, \theta_a(-y),$$
where $\theta_a$ is the theta function with points $v \in \mathbb{C}^I$ and coefficients $a(v)$. The coefficients satisfy $\sum_v |a(v)| e^{-\varepsilon |v|^2} < \infty$ for each $\varepsilon > 0$, and there is $\delta > 0$ with $|v| \ge \delta$ whenever $a(v) \neq 0$ and $v \neq 0$.

Unfolding the sum over units with $p$ gives, for $\operatorname{Re} s > 1$,
$$\gamma_n(s) P_F(s) = 2^{|I|} \int_{\mathbb{R}^I} p(y)\, \theta_F(y)\, e^{s \sum_i y_i}\, dy.$$
Let $S = \{y : \sum_i y_i \ge 0\}$. The functional equation of $\theta_F$ turns the part of the integral outside $S$ into an integral over $S$ in the variable $-y$, and the integral equals $f_1(s) + \kappa f_2(1 - s)$, where
$$f_1(s) = \int_S p(y)\, \theta_F(y)\, e^{s \sum_i y_i}\, dy, \qquad f_2(s) = \int_S p(-y)\, \theta_a(y)\, e^{s \sum_i y_i}\, dy.$$
The terms of $\theta_F$ and $\theta_a$ at the origin are $0$, because $G_n(0) = 0$. The other points stay at distance at least a fixed positive number from the origin, and on the support of $p$ the coordinates $y_i$ differ by at most $R$. So the weighted kernels $|p(y)\theta_F(y)| e^{\sigma \sum_i y_i}$ and $|p(-y)\theta_a(y)| e^{\sigma \sum_i y_i}$ are integrable on $S$ for every real $\sigma$. An integral $\int g(x) e^{s \ell(x)} d\mu(x)$ with $\ell \ge 0$ and $\int |g| e^{\sigma \ell} d\mu < \infty$ for all $\sigma$ is an entire function of $s$, bounded in vertical strips. So $f_1$ and $f_2$ are entire and bounded in vertical strips, and then so is
$$\Lambda(s) = 2^{|I|}\big(f_1(s) + \kappa f_2(1 - s)\big),$$
because $1 - s$ runs over the strip $1 - b \le \operatorname{Re} \le 1 - a$ when $s$ runs over $a \le \operatorname{Re} s \le b$. For $\operatorname{Re} s > 1$, $\Lambda(s) = \gamma_n(s) P_F(s)$ by the two identities above. $\square$

The formula for $\Lambda$ also shows the functional equation of the partial series: it relates $f_1$ at $s$ to $f_2$ at $1 - s$. The theorem keeps only the analytic continuation and the bound.

### The completed L-function

**Theorem 1.7.2 (Completed Hecke L-functions are bounded in vertical strips).** Let $E$ be a totally complex number field, $\varphi$ a CM type of $E$, and $\chi$ a unitary Hecke character of infinity type $n$ with some $n_i \neq 0$. Then $(\chi, n)$ has a completed L-function $\Lambda$, and $\Lambda$ is bounded in vertical strips.

Lean: `GlobalTheory.HeckeStrip.completedLBoundedInStrips`.

*Proof.* Since $\chi$ is unitary, there are a nonzero ideal $m$ and a function $X$ on the ideals of $\mathcal{O}_E$ with these properties: $X(0) = 0$, $X(\mathcal{O}_E) = 1$, $X(ab) = X(a)X(b)$; $|X(a)| = 1$ if $a \neq 0$ is prime to $m$, and $X(a) = 0$ if $a$ is not prime to $m$; $X(P) = \chi(\varpi_P)$ for a prime $P$ at which $\chi$ is unramified, and $X(P) = 0$ for the other primes; and $X((\beta)) = \chi_\infty(\beta)^{-1}$ for $\beta \in \mathcal{O}_E$ with $\beta \equiv 1 \bmod m$. By the infinity type, $X((\beta)) = \operatorname{wt}(\beta)$ for such $\beta \neq 0$, and $|X(a)| \le 1$ for all $a$.

There is a finite family of positive integers $B_k$, constants $c_k$, nonzero ideals $M_k$ and functions $F_k$ as in the previous theorem, with
$$\sum_{a} X(a) \operatorname{N}a^{-s} = \sum_k c_k B_k^{s} P_{F_k}(s) \qquad (\operatorname{Re} s > 1).$$
Let $\Lambda_k$ be the function of the previous theorem for $F_k$, and put $\Lambda(s) = \sum_k c_k B_k^s \Lambda_k(s)$. This is entire, since $B_k \neq 0$.

For $\operatorname{Re} s > 1$, the Dirichlet series of $X$ equals $\exp \sum_P -\log(1 - X(P)\operatorname{N}P^{-s})$, because $X$ is multiplicative and bounded by $1$. The Euler product $\prod_v L_v(\chi, s)$ converges to the same exponential, since $X(P)$ is the coefficient of its factor at $P$. So the product converges to $L = \sum_a X(a)\operatorname{N}a^{-s}$, and
$$\Lambda(s) = \sum_k c_k B_k^s \gamma_n(s) P_{F_k}(s) = \gamma_n(s) L.$$
For the bound, let $a < b$ and let $C_k$ bound $\Lambda_k$ on the strip. Since $B_k \ge 1$, $|B_k^s| = B_k^{\operatorname{Re} s} \le B_k^b$, so $|\Lambda(s)| \le \sum_k |c_k| B_k^b |C_k|$ on the strip. $\square$

The condition that some $n_i \neq 0$ is necessary. For the trivial character and $n = 0$ the completed L-function is that of the Dedekind zeta function of $E$, which has a pole at $s = 1$.

**Remark 1.7.3 (Formalization).** The completed L-function is `GlobalTheory.IndefiniteRowSideFullHecke.CompletedLStripBounds.IsCompletedL`, and the infinity type is `Formalism.L2.Host.HChar.HasInf`; it is stated only for $k \in E^\times$, which is the usual form. We opened the proofs of the two theorems above, but not the proofs of the inputs they use. We read only the statements of `GlobalTheory.T.exists_idealCharacter_of_unitary_heckeChar` (the function $X$), `GlobalTheory.T.heckeLSeries_eq_sum_principalPartialSeries` (the decomposition), `GlobalTheory.tsum_ideal_mul_absNorm_cpow_eq_exp_tsum` and `GlobalTheory.HeckeOne.hasProd_exp` (the Euler product), `GlobalTheory.T.exists_measurable_partitionOfUnity_unitLogTranslates` (the function $p$), `GlobalTheory.T.heckeThetaKernel_poisson_summation`, `GlobalTheory.T.archFactor_mul_pSeries_eq_integral_alt` (the unfolding), `GlobalTheory.T.mellin_integral_split_functional_equation` (the split at $\sum_i y_i = 0$), `GlobalTheory.T.periodic_bounded_gaussian_summable_cmType`, `GlobalTheory.T.integrable_weighted_heckeThetaKernel_halfSpace` and `GlobalTheory.T.laplace_integral_entire_boundedInVerticalStrips`. The explanation of why the weighted kernels are integrable is therefore a reading of the hypotheses of the integrability statement, not of its proof. The second name of the first theorem is proved by `first | exact @...` from the first name.
