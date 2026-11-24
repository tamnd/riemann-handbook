---
title: The Siegel-Weil formula in the convergent range
decls:
  - GlobalTheory.CompanionTheory.WeilSiegel.Frame.siegel_frame
  - GlobalTheory.T.siegel_weil_rank_coefficient
  - GlobalTheory.CompanionTheory.WeilSiegel.Deg.siegelDeg
  - PositivityTheory.Rg.Wsf.weilSiegelFormula
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Siegel-Weil formula in the convergent range

This section proves the Siegel-Weil formula of Weil for a unitary dual pair in the range $2n < m$, where the Eisenstein series and the theta integral both converge absolutely. The proof compares Fourier coefficients. Each coefficient of the theta integral is an integral over the frames of one Hermitian matrix $\beta$, and each coefficient of the Eisenstein series is a Whittaker integral at $\beta$. For singular $\beta$ the comparison uses [the singular case](/entry/sw-free-block/) and [the Euler product form of the Whittaker integral](/entry/whit-eq-integral/). The formula is the input to [the Weil representation of the unitary pair](/entry/weil-unitary/) in the chapter on Howe duality.

We use the notation of the previous section. Let $V$ be a Hermitian space of rank $m$ over $E$, with unitary group $U_V$, and let $r \ge 1$. For an $m \times r$ matrix $x$ over $E$ let $\langle x, x \rangle = {}^t x^\sigma G_V x$ be its Gram matrix. Let $\nu$ be a Haar measure on $U_V(\mathbb{A})$, and write $[U_V] = U_V(F) \backslash U_V(\mathbb{A})$ with the measure induced by $\nu$.

**Definition 4.4.1 (Frame integral).** For a function $\varphi$ on $\mathrm{Mat}_{m \times r}(\mathbb{A}_E)$ and a Hermitian $r \times r$ matrix $\beta$ over $E$, the frame integral is the average
$$I_\beta(\varphi) = \frac{1}{\operatorname{vol}[U_V]} \int_{[U_V]} \sum_{x} \varphi(h^{-1} x) \, dh,$$
where $x$ runs over the $m \times r$ matrices over $E$ of rank $r$ with $\langle x, x \rangle = \beta$.

The columns of such an $x$ form a frame of $\beta$ in the sense of [the section on Gram fibres](/entry/local-stages/). Summing $I_\beta$ over all $\beta$ gives the average of the full theta series over the vectors of rank $r$.

**Theorem 4.4.2 (Siegel-Weil for frames).** Assume the convergent hypotheses for $(r, V, \psi, \mu, \lambda, \nu, \varphi)$. Let $\beta$ be a Hermitian $r \times r$ matrix in block normal form of some rank $t$. If there is an $m \times r$ matrix $x$ of rank $r$ with $\langle x, x \rangle = \beta$, then
$$I_\beta(\varphi) = W_\beta(\varphi).$$

Lean: `GlobalTheory.CompanionTheory.WeilSiegel.Frame.siegel_frame` (also `GlobalTheory.T.siegel_weil_rank_coefficient`, a second name).

*Proof.* The extension $E/F$ is CM and the Gram matrix $G_V$ is Hermitian and nondegenerate. Let $\mathcal{F}$ be a fundamental domain for $U_V(F)$ in $U_V(\mathbb{A})$. The columns of $x$ form a frame of $\beta$, so the set of frames of $\beta$ is not empty. Choose a basis $b$ of $E/F$, a standard system of measures, and free Gram fibre families $m_\infty$, $m_v$; such data exist with the normalisation of the Tamagawa measure. Since $2r < m$, [the block case](/entry/sw-free-block/) gives the free Siegel-Weil property for $(G_V, \beta)$: the theta measure $\Theta$ of the frames of $\beta$ is the Euler product of $(m_\infty(\beta), m_v(\beta))$ with constant 1. By definition of the theta measure, $I_\beta(\varphi) = \int \varphi({}^t X) \, d\Theta(X)$, and the integrand is $\Theta$-integrable because the absolute theta integral is finite. Now [the Whittaker integral theorem](/entry/whit-eq-integral/) gives $W_\beta(\varphi) = \int \varphi({}^t X) \, d\Theta(X)$. $\square$

The general singular matrix reduces to the block case by a change of coordinates.

**Theorem 4.4.3 (Singular coefficients).** Assume the convergent hypotheses for $(r, V, \psi, \mu, \lambda, \nu, \varphi)$, and let $\beta$ be a Hermitian $r \times r$ matrix over $E$ with $\det \beta = 0$. Then $I_\beta(\varphi) = W_\beta(\varphi)$.

Lean: `GlobalTheory.CompanionTheory.WeilSiegel.Deg.siegelDeg`.

*Proof.* A singular Hermitian matrix is congruent to one in block normal form: there are an invertible $a$ over $E$ and a $\gamma$ in block normal form of some rank $t < r$ with $\beta = {}^t a^\sigma \gamma a$. Let $\varphi_a(y) = \varphi(y a^{-1})$ be the pullback. The map $x \mapsto x a$ is a bijection from the rank $r$ matrices with Gram matrix $\gamma$ to those with Gram matrix $\beta$, so $I_\beta(\varphi) = I_\gamma(\varphi_a)$. A change of variables in $y$ and in $b$, which uses that $\mu$ and $\lambda$ are Haar measures of covolume 1, gives $W_\beta(\varphi) = W_\gamma(\varphi_a)$. The convergent hypotheses hold for $\varphi_a$. If $\gamma$ is represented by a matrix of rank $r$, apply [Siegel-Weil for frames](/entry/siegel-frame/) to $\varphi_a$ and $\gamma$. If not, $I_\gamma(\varphi_a)$ is an empty sum, and [the theorem on nonrepresented coefficients](/entry/frame-integral-eq-coefficient-nonrepresented/) shows that $W_\gamma(\varphi_a) = 0$ as well. $\square$

Now we state the formula. Let $G_n = U(n, n)$ be the quasi-split unitary group of rank $2n$ over $F$ attached to $E/F$, and $P_n$ its Siegel parabolic subgroup, see [parabolic subgroups](/learn/groups/#parabolic-subgroups). Let $\chi$ be a [[Hecke character|KPYFGB342X]] of $\mathbb{A}_E^\times$ whose restriction to $\mathbb{A}^\times$ is $\eta^m$, where $\eta$ is the quadratic character of $E/F$, see [Hecke characters](/learn/class-field-theory/#hecke-characters). Let $\omega$ be the [[Weil representation|H3Q2703KKV]] of $G_n(\mathbb{A})$ on the adelic Schwartz space of $\mathrm{Mat}_{m \times n}(\mathbb{A}_E)$ in the Schrödinger model attached to $\psi$, $\chi$ and $V$, see [the Weil representation](/learn/theta/#the-weil-representation).

**Theorem 4.4.4 (Siegel-Weil formula, convergent range).** Let $1 \le n$ with $2n < m$. Let $\psi$ be a standard character, $\chi$ a Hecke character with restriction $\eta^m$ to $\mathbb{A}^\times$, $\mu$ a Haar measure of covolume 1 on $\mathrm{Mat}_{m \times n}(\mathbb{A}_E)$, $\omega$ the Weil representation, and $\nu$ a Haar measure on $U_V(\mathbb{A})$. Then for each adelic Schwartz function $\Phi$ of the given archimedean type,
$$\begin{aligned} &\sum_{\gamma \in P_n(F) \backslash G_n(F)} (\omega(\gamma) \Phi)(0) \\ &\quad = \frac{1}{\operatorname{vol}[U_V]} \int_{[U_V]} \sum_{\xi} \Phi(h^{-1} \xi) \, dh, \end{aligned}$$
where $\xi$ runs over all $m \times n$ matrices over $E$.

Lean: `PositivityTheory.Rg.Wsf.weilSiegelFormula`.

The left side is the value at $g = 1$ of the [[Siegel Eisenstein series|3NZBZXYWAJ]] of the section $g \mapsto (\omega(g) \Phi)(0)$, see [Eisenstein series](/learn/automorphic-forms/#eisenstein-series). The right side is the average of the theta function of $\Phi$ over $[U_V]$. This is Weil's form of the Siegel-Weil formula, see [the Siegel-Weil formula](/learn/theta/#the-siegel-weil-formula).

*Proof.* We compare the $\beta$-th Fourier coefficients of both sides along the unipotent radical of $P_n$, and then sum. On the theta side, split the sum over $\xi$ by the rank and the Gram matrix of $\xi$. For vectors of full rank $n$ the contribution of a Gram matrix $\beta$ is the frame integral $I_\beta(\Phi)$. These terms sum to the full theta integral, since the absolute theta integral converges. On the Eisenstein side, the Bruhat decomposition of $P_n(F) \backslash G_n(F)$ into cells, together with Poisson summation on the Hermitian matrices, writes the sum over the big cell as $\sum_\beta W_\beta(\Phi)$. The two sides then agree term by term: for $\det \beta \ne 0$ by the nondegenerate case of the Siegel-Weil comparison, and for $\det \beta = 0$ by [the theorem on singular coefficients](/entry/siegel-deg/). The smaller cells match the vectors of lower rank in the same way. The assembly of the cells, the orbit decomposition of the theta series and the convergence of both sides are proved in [the assembly of the formula](/entry/head-of-deg/). $\square$

**Remark 4.4.5 (Formalization).** The formula is stated only at $g = 1$, and the section is $\gamma \mapsto (\omega(\gamma)\Phi)(0)$ with no height factor, so there is no complex parameter ([WeilSiegelFormula.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/WeilSiegelFormula.lean#L18)). The proof of the theorem on frames takes the CM property of the host data from a lemma placed in a namespace named for an unused slot ([SiegelWeilRankCoefficient.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeil/ArchimedeanSiegelWeil/PlaceIntegrals/SiegelWeilRankCoefficient.lean#L16)). The second name of that theorem is stated with `first | exact`; it speaks of a rank coefficient, but the statement is the identity for frames. In the theorem on singular coefficients, the change of variables uses only the covolume parts of the convergent hypotheses. The main formula is proved by passing the theorem on singular coefficients to one assembly result, which supplies the nondegenerate case, Poisson summation and the cell decomposition.
