---
title: Division of bounded sections
decls:
  - ReciprocityTheory.ChartRestriction.G.AR.Up.divCoreStatement_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Division of bounded sections

This section proves a division theorem for automorphic sections. Let $s_1, \dots, s_n$ be cusp forms of weight $\ell$ whose common zeros are finitely many orbits, and $f$ a square integrable cusp form of weight $\lambda + T \ell$. If $f$ minus an explicit leading part vanishes to order $T - n$ at the zeros, then it is a sum of monomials of degree $T - n$ in the $s_k$ with bounded coefficients of weight $\lambda + n \ell$. The proof divides in a chart by an $L^2$ estimate and returns with Poincaré series. The theorem serves the [division theorem for one weight](/entry/division-one/) in a later volume.

### Sections and charts

We keep the data of the [short vector bound](/entry/short-vector-bound/): $E$, $\Psi$, $G$, $(p_0, r - p_0)$, $\Gamma$, $\chi_\lambda$, $\mathcal{D}$ and $F_{\xi, \nu}$. Let $B$ be the set of frames $b$ with each $b_\tau$ invertible and upper triangular. For frames $x, b$ let $(x b)_\tau = x_\tau b_\tau$, and for $\gamma \in \Gamma$ let $(\gamma x)_\tau = \tau(\gamma) x_\tau$. We do not unfold the character $\chi_{B, \lambda}$ of $B$. Let $d_{\tau, i}(x)$, for $0 \leq i \leq r$, be the leading principal minor of order $i$ of the Gram matrix of $x_\tau$ for $h_\tau$.

A *section* of weight $\lambda$ is a function $P$ on frames, holomorphic on $\mathcal{D}$, with $P(x b) = \chi_{B, \lambda}(b) P(x)$ and $P(\gamma x) = \chi_\lambda(\gamma) P(x)$ on $\mathcal{D}$. Its *weighted norm* is $\| P \|_\lambda(x) = |P(x)| \, \omega_\lambda(x)$ with
$$\omega_\lambda(x) = \prod_{\tau \in \Psi} \prod_{i = 0}^{r - 1} \Bigl| \frac{d_{\tau, i+1}(x)}{d_{\tau, i}(x)} \Bigr|^{-\lambda_{\tau, i} / 2},$$
and $\varphi_\lambda = -2 \log \omega_\lambda$. A section is *bounded* if $\| P \|_\lambda$ is bounded on $\mathcal{D}$. Let $S_\lambda$ be the set of bounded cusp forms, the bounded sections with $F_{\xi, 0}(P) = 0$ for all isotropic $\xi \in \Lambda$, and $S_\lambda^{+}$ the set of $P \in S_\lambda$ with $F_{\xi, \nu}(P) = 0$ for all isotropic $\xi$ and all $\nu$ with $\sum_\tau \nu_\tau \leq 0$.

Let $n = |\Psi| \, r (r - 1)/2$. For $z = (z_{\tau, a, b})_{b < a} \in \mathbb{C}^n$ let $u(z)_\tau$ be lower unitriangular with entries $z_{\tau, a, b}$. For a frame $x_0$ the *chart* is $c_{x_0}(z) = x_0 u(z)$, on $\Omega_{x_0} = \{ z : c_{x_0}(z) \in \mathcal{D} \}$. On $\Omega_{x_0}$ let
$$\mu_{x_0} = D_{x_0}(z) \, dz, \qquad D_{x_0}(z) = \prod_\tau \prod_{i = 0}^{r - 1} |d_{\tau, i}(c_{x_0}(z))|^{-2}, \qquad \varrho_{x_0}(z) = -\sum_\tau \log |d_{\tau, p_0}(c_{x_0}(z))|.$$
The Levi form of $g$ on $\mathbb{C}^n$ is $\mathcal{L}(g)(z; \zeta) = \operatorname{Re} \sum_{j, k} \partial_j \bar\partial_k g(z) \, \zeta_j \overline{\zeta_k}$, and $\mathcal{L}_{x_0}(\phi) = \mathcal{L}(\phi \circ c_{x_0})$. A frame $x_0$ is *orthonormal* if every Gram matrix of $x_0$ is $\mathrm{diag}(1, \dots, 1, -1, \dots, -1)$ with $p_0$ entries $1$. A *fundamental set* for $x_0$ is a measurable $\mathcal{F} \subseteq \Omega_{x_0}$ such that distinct points of $\mathcal{F}$ have charts in distinct sets $\Gamma x B$, and $c_{x_0}(z) \in \Gamma c_{x_0}(\mathcal{F}) B$ for $\mu_{x_0}$-almost every $z$.

$\Gamma$ is *properly discontinuous* if all $x, x' \in \mathcal{D}$ have neighbourhoods $U, U'$ such that only finitely many $\gamma \in \Gamma$ have $\gamma u = u' b$ with $u \in U$, $u' \in U'$, $b \in B$. The *finite volume* condition is that some orthonormal $x_0$ has a fundamental set of finite $\mu_{x_0}$-measure.

### The division data

The *archimedean datum* contains weights $\ell$ and $\lambda$, an integer $T$, and sections $w_1, \dots, w_N \in S_\ell^{+}$ with no common zero on $\mathcal{D}$, with $n \geq 2$ and $T \geq 11 n^2$. We do not list its other fields, which the statement does not use.

The *flat datum* contains $w_0 \in S_\ell^{+}$, sections $s_1, \dots, s_n \in S_\ell^{+}$ and points $x_1, \dots, x_q \in \mathcal{D}$, such that the common zeros of the $s_k$ in $\mathcal{D}$ are the distinct sets $\Gamma x_j B$, $w_0(x_j) \neq 0$, and $z \mapsto (s_k / w_0)(c_{x_j}(z))_k$ has an invertible derivative at $0$. We do not list its comparison bounds between weighted norms.

For $\alpha \in \mathbb{N}^n$ let $s^\alpha = \prod_k s_k^{\alpha_k}$ and $|\alpha| = \sum_k \alpha_k$. For sections $t_1, \dots, t_\delta$ and coefficients $\theta = (\theta_{\alpha, k})$ the *leading part* is
$$\mathrm{lead}_\theta(x) = \sum_{|\alpha| < T - n} \ \sum_{k = 1}^{\delta} \theta_{\alpha, k} \, s^\alpha(x) \, w_0(x)^{T - |\alpha|} \, t_k(x).$$
The family $t$ is an *evaluation basis* if $a \mapsto \bigl( \sum_k a_k t_k(x_j) \bigr)_j$ is a bijection $\mathbb{C}^\delta \to \mathbb{C}^q$.

**Definition 1.17.1 (Vanishing to order a).** A function $g$ on frames *vanishes to order $a$* at the points $x_j$ if for each $j$ there is $\rho > 0$ with
$$\int_{|z| < \rho} |g(c_{x_j}(z))|^2 \Bigl( \sum_k |s_k(c_{x_j}(z))|^2 \Bigr)^{-(a + n - 1/2)} dz < \infty.$$

Lean: `ReciprocityTheory.ChartRestriction.G.AR.Up.VanS`.

For a frame $x$ let $\Sigma_w(x) = \sum_k \| w_k \|_\ell^2(x)$.

### The theorem

**Theorem 1.17.2 (Division of bounded sections).** Let $\Gamma$ be properly discontinuous with the finite volume condition, and fix an archimedean and a flat datum. Assume:

1. there are $\beta, \kappa$ with $4 |\Psi| r^2 < \beta$, $\beta^2 |\Psi| \min(p_0, r - p_0) + \beta < \kappa$, and $\kappa \, \mathcal{L}(\varrho_{x_0}) \leq \mathcal{L}_{x_0}(\varphi_\lambda) - \mathcal{L}(\log D_{x_0})$ at all $z \in \Omega_{x_0}$ and $\zeta$, for all orthonormal $x_0$;
2. $\mathcal{L}_{x_0}(\varphi_\ell) \geq 0$ on $\Omega_{x_0}$ for all orthonormal $x_0$;
3. for $\eta = \lambda + n \ell$, $\lambda$ and $\lambda + T \ell$, every bounded section of weight $\eta$ is in $S_\eta$;
4. there are sections $g_1, \dots, g_K$ such that every $f \in S_{\lambda + T \ell}$ is a linear combination of them on $\mathcal{D}$.

Let $t_1, \dots, t_\delta$ be bounded sections of weight $\lambda$ that form an evaluation basis, $x_0$ orthonormal, $\mathcal{F}$ a fundamental set for $x_0$, and $f \in S_{\lambda + T \ell}$ with
$$\int_{\mathcal{F}} \| f \|_{\lambda + T \ell}^2 \, \Sigma_w^{-T} \circ c_{x_0} \, d\mu_{x_0} < \infty.$$
Let $\theta$ be such that $f - \mathrm{lead}_\theta$ vanishes to order $T - n$ at the points $x_j$. Then there are bounded sections $h_\alpha$ of weight $\lambda + n \ell$, for $|\alpha| = T - n$, with
$$f - \mathrm{lead}_\theta = \sum_{|\alpha| = T - n} s^\alpha \, h_\alpha \quad \text{on } \mathcal{D}.$$

Lean: `ReciprocityTheory.ChartRestriction.G.AR.Up.divCoreStatement_holds`.

*Proof.* Write $\lambda' = \lambda + T \ell$, $\lambda'' = \lambda + n \ell$, $c = c_{x_0}$, $g = f - \mathrm{lead}_\theta$ and $k_\beta = e^{-\beta \varrho_{x_0}}$. Let $W = 0$ outside $\mathcal{D}$ and on $\mathcal{D}$
$$W = e^{-\varphi_{\lambda'}} \, \Sigma_w^{-T} \Bigl( \sum_k \| s_k \|_\ell^2 / \Sigma_w \Bigr)^{-(T - 1/2)}.$$
A *metric weight* for a weight $\eta$ is a measurable $W' \geq 0$ with $W'(x b) = W'(x) / |\chi_{B, \eta}(b)|^2$ and $W'(\gamma x) = W'(x)$; it has a *lower bound* if $W' \geq a \, e^{-\varphi_\eta}$ on $\mathcal{D}$ for some $a > 0$. Let $\pi_\eta(P) = \sum_{\gamma \in \Gamma} \chi_\eta(\gamma)^{-1} P(\gamma x)$. We use these facts from another part of the development, whose statements we have opened.

1. $g$ is a bounded section of weight $\lambda'$ with $\int_{\mathcal{F}} \| g \|_{\lambda'}^2 \Sigma_w^{-T} \circ c \, d\mu_{x_0} < \infty$.
2. *The weight.* Under hypotheses 1 and 2, $W$ is a metric weight for $\lambda'$ with a lower bound, and there are a real $\psi_0$ and a holomorphic $g_1 \not\equiv 0$ on $\Omega_{x_0}$ such that, where $g_1 \neq 0$, $\psi_0 \circ c$ is smooth, $W \circ c = e^{-\psi_0 \circ c}$ and $\kappa \mathcal{L}(\varrho_{x_0}) \leq \mathcal{L}(\psi_0 \circ c - \log D_{x_0})$. Each $g' \in S_{\lambda'}$ with the integral of fact 1 finite that vanishes to order $T - n$ has $\int_{\mathcal{F}} |g' \circ c|^2 \, W \circ c \, d\mu_{x_0} < \infty$.
3. *Onto.* With these data and hypotheses 3 and 4, each such $g'$ is $\pi_{\lambda'}(P)$ for a holomorphic $P$ on $\mathcal{D}$ with $P(x b) = \chi_{B, \lambda'}(b) P(x)$, such that $F = P \circ c$ is holomorphic on $\Omega_{x_0}$ with $\int |F|^2 k_\beta^{-1} \, W \circ c \, d\mu_{x_0} < \infty$.
4. *Division in the chart.* Under hypotheses 1 and 2, each such $F$ is $\sum_{|\alpha| = T - n} (s^\alpha \circ c) H_\alpha$ on $\Omega_{x_0}$, with $H_\alpha$ holomorphic and $\int |H_\alpha|^2 k_\beta^{-1} e^{-\varphi_{\lambda''}} \circ c \, d\mu_{x_0} < \infty$.
5. *Extension.* If $H$ is holomorphic on $\Omega_{x_0}$ and $\int |H|^2 e^{-\varphi_\eta} \circ c \, d\mu_{x_0}$ over $\{z : c(z) \in C B\}$ is finite for every compact $C \subseteq \mathcal{D}$, then $H = P' \circ c$ with $P'$ holomorphic on $\mathcal{D}$ and $P'(x b) = \chi_{B, \eta}(b) P'(x)$.
6. *Poincaré series.* If $W'$ is a metric weight for $\eta$ with a lower bound, and $P'$ is as in fact 5 with $\int |P' \circ c|^2 k_\beta^{-1} W' \circ c \, d\mu_{x_0} < \infty$, then $\pi_\eta(P')$ converges absolutely on $\mathcal{D}$, it is a bounded section of weight $\eta$, and $\pi_{\eta + \eta'}(g' P') = g' \, \pi_\eta(P')$ for each section $g'$ of a weight $\eta'$.
7. *Dense chart.* There is a holomorphic $\Delta$ such that $\{ \Delta \neq 0 \}$ meets every ball around a point of $\mathcal{D}$, and each $x \in \mathcal{D}$ with $\Delta(x) \neq 0$ is $c(z) b$ with $z \in \Omega_{x_0}$, $b \in B$.
8. $s^\alpha$ is a section of weight $|\alpha| \ell$, $\chi_{B, \eta + \eta'} = \chi_{B, \eta} \chi_{B, \eta'}$, $|\chi_\eta(\gamma)| = 1$, $e^{-\varphi_\eta}$ is a metric weight for $\eta$ with a lower bound, and $\varrho_{x_0} \geq 0$ almost everywhere on $\Omega_{x_0}$.

By fact 1 and hypothesis 3, $g \in S_{\lambda'}$. Facts 2 and 3 give $P$ and $F$ with $\pi_{\lambda'}(P) = g$, and fact 4 gives the $H_\alpha$. Since $\beta > 0$, fact 8 gives $k_\beta \leq 1$, so fact 5 applies to $H_\alpha$ with $\eta = \lambda''$ and gives $P_\alpha$ with $P_\alpha \circ c = H_\alpha$. By facts 8 and 6, $h_\alpha = \pi_{\lambda''}(P_\alpha)$ is a bounded section of weight $\lambda''$.

From $n \geq 2$ and $T \geq 11 n^2$ we get $n \leq T$, so $\lambda' = \lambda'' + (T - n) \ell$. Let $Q = \sum_{|\alpha| = T - n} s^\alpha P_\alpha$, holomorphic on $\mathcal{D}$. If $x = c(z) b$ as in fact 7, then by fact 8
$$P(x) = \chi_{B, \lambda'}(b) \sum_\alpha s^\alpha(c(z)) H_\alpha(z) = \sum_\alpha s^\alpha(x) P_\alpha(x) = Q(x).$$
Since $\mathcal{D}$ is open and $P, Q$ are continuous, fact 7 gives $P = Q$ on $\mathcal{D}$. Let $x \in \mathcal{D}$. As $\mathcal{D}$ is stable under $\Gamma$, $g(x) = \pi_{\lambda'}(Q)(x)$. Each series $\pi_{\lambda'}(s^\alpha P_\alpha)$ converges absolutely, since $|s^\alpha(\gamma x)| = |s^\alpha(x)|$, so the finite sum and the series commute, and by fact 6
$$g(x) = \sum_\alpha \pi_{\lambda'}(s^\alpha P_\alpha)(x) = \sum_\alpha s^\alpha(x) \, h_\alpha(x). \qquad \square$$

**Remark 1.17.3 (Classical form).** Fact 4 is of the type of Skoda's theorem. Let $\Omega \subseteq \mathbb{C}^n$ be pseudoconvex, $\varphi$ plurisubharmonic, $g_1, \dots, g_p$ holomorphic, $\alpha > 1$ and $m = \min(n, p - 1)$. If $f$ is holomorphic with $I = \int_\Omega |f|^2 |g|^{-2 \alpha m - 2} e^{-\varphi} < \infty$, then $f = \sum_k g_k h_k$ with $\int_\Omega |h|^2 |g|^{-2 \alpha m} e^{-\varphi} \leq \frac{\alpha}{\alpha - 1} I$ (Skoda, 1972, with the $L^2$ estimates of Hörmander, 1965). The theorem here divides by the monomials of degree $T - n$, and Poincaré series carry the division from a chart to $\mathcal{D}$. We have not opened the proof of fact 4, so we do not claim which form of Skoda's theorem it uses.

**Remark 1.17.4 (Formalization).** The theorem proves the proposition `DivCoreStatement` in [WeightFunctionOnFrames.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/ArakelovVolumes/UpperBounds/WeightFunctionOnFrames.lean#L118). Its proof in [LocalUnfoldBStatementHolds.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/ArakelovVolumes/UpperBounds/LocalUnfoldBStatementHolds.lean#L21) is one line: `divCore_up_of`, the argument above in [DivCoreUpPf.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/ArakelovVolumes/UpperBounds/DivCoreUpPf.lean#L99), applied to `ontoWeightStatement_holds`, `upDiv_holds` and `DivStartStatement_holds` (facts 2, 4 and 1). Facts 3, 5, 6 and 7 are `ontoStatement_holds`, `extFStatement_holds`, `poin_holds` and `lu_holds`; fact 8 is `mono_sec`, `bchar_add`, `PoinPf.norm_chi`, `metricW_exp`, `wLower_exp` and `ExF.rhF_nonneg`. The data are `ArchInM` and `FlatM`, $W$ is `WSk`, and $\lambda$, $\ell$ are `Fp`, `L`. In the intro at [line 101](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/ArakelovVolumes/UpperBounds/DivCoreUpPf.lean#L101) the hypotheses `hcF` and `hcFp`, the first two cases of hypothesis 3, and `hval`, the evaluation basis, are named but not used, so the statement could drop them. The numbers $\delta$ and $q$ are separate parameters, which the evaluation basis forces to be equal. The vanishing to order $a$ uses $|s_k|$, not $\| s_k \|_\ell$.

## Notes and references

This chapter proves the finiteness of class numbers of linear algebraic groups over number fields. The theorem of this section is used by the [theorem on the geometric realization of weight one](/entry/geometric-realization-of-weight-one/), which serves the step [GeoOne](/step/geo-one-def/) of [the Galois row](/proof/galois-row/). It is also used to show that the centraliser torus of a similitude group has finitely many classes.

The theorem is due to Borel. In its classical form: let $G$ be a linear algebraic group over a number field $F$ and $U$ an open compact subgroup of $G(\mathbb{A}_{F,f})$; then $G(F) \backslash G(\mathbb{A}_{F,f}) / U$ is finite. The form here is the same, with $G$ given by equations inside $\mathrm{GL}_n$. The treatment of a reductive group, by a rational tensor with a closed orbit and the reduction theory of $\mathrm{SL}_I$, is the method of Borel and Harish-Chandra. The treatment here differs in three points. All results over $\mathbb{Q}$ are proved over an arbitrary adelic pair $(R, R_0)$, of which $(\mathbb{A}_{\mathbb{Q},f}, \widehat{\mathbb{Z}})$ is the main example. A group is given by its complex points and its rational ideal, not as a scheme; the hypothesis on a reductive group is replaced by the complete reducibility of the natural representation. The unipotent part is removed by an induction on the dimension of the linear span of the group, with the block-diagonal part for a rational flag, and not by a Levi decomposition.

- A. Borel, "Some finiteness properties of adele groups over number fields", *Publ. Math. IHÉS* 16 (1963), Theorem 5.1.
- A. Borel and Harish-Chandra, "Arithmetic subgroups of algebraic groups", *Ann. of Math.* 75 (1962).
- V. Platonov and A. Rapinchuk, *Algebraic Groups and Number Theory*: Chapter 2, §2.1 (restriction of scalars), Chapter 4 (reduction theory and Siegel sets), Chapter 5, §5.1 (Theorem 5.1, finiteness of the class number), Chapter 7 (strong approximation), Chapter 8 (class numbers).
- J. E. Humphreys, *Linear Algebraic Groups*, §11.2 (Chevalley's theorem: a closed subgroup is the stabiliser of a line in a representation).

The later sections prove inputs for unitary groups over CM fields: the Hasse norm principle, finite volume and theta functions, the theta measure of a box, strong approximation for special unitary groups, an inert local frame, short vectors and reduced frames near a cusp, and an $L^2$ division theorem.

- J. Neukirch, *Algebraic Number Theory*, Chapter VI, §4.
- J. Tate, "Fourier analysis in number fields and Hecke's zeta-functions", in Cassels and Fröhlich, *Algebraic Number Theory*.
- C. L. Siegel, "Indefinite quadratische Formen und Funktionentheorie I", *Math. Ann.* 124 (1951).
- A. Weil, *Acta Math.* 111 (1964) and 113 (1965).
- A. Borel, *Introduction aux groupes arithmétiques*, Hermann, 1969.
- M. Kneser, *J. reine angew. Math.* 218 (1965).
- J. Voight, *Quaternion Algebras*, Graduate Texts in Mathematics 288.
- R. Jacobowitz, "Hermitian forms over local fields", *Amer. J. Math.* 84 (1962).
- W. Banaszczyk, *Math. Ann.* 296 (1993).
- H. Skoda, *Ann. Sci. École Norm. Sup.* (4) 5 (1972).
- L. Hörmander, *Acta Math.* 113 (1965).
