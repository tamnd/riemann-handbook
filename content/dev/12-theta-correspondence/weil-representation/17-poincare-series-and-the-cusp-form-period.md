---
title: Poincaré series and the cusp form period
decls:
  - UpperTheory.Lit.Cusp.fibre_integral_eq_zero
  - UpperTheory.Lit.Cusp.poin_isCuspFun
  - UpperTheory.Lit.Cusp.exists_multT_eq_poin
  - UpperTheory.Lit.Cusp.exists_cusp_form_theta_period_ne_zero
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Poincaré series and the cusp form period

This section constructs cusp forms on a unitary group from Poincaré series of discrete series matrix coefficients, and uses them to prove that a nonzero theta row at the bottom of the tower has a nonzero period against some cusp form. The result is the first half of the [nonzero bottom period](/entry/period-ne-of-eigen/) of the next section, which the step [real functionals separate](/entry/real-functionals-separate-of-hypothesis/) needs. The section has four results: the vanishing of fibre integrals of a coefficient, the cuspidality of the Poincaré series, the realization of the Poincaré series in a space of automorphic forms, and the nonzero period. The analytic inputs are three published results, taken as given.

### Setting

Let $V$ be a Hermitian space of rank $n$ over the CM field $E$, with unitary group $G = \mathrm{U}(V)$. For each real place $\tau$ of $F$ the group $G(F_\tau)$ is a real unitary group $\mathrm{U}(J_\tau)$ of the signature of $V$ at $\tau$. A *model* $M$ is a family of Hilbert spaces $H_\tau$ with irreducible unitary representations $\sigma_\tau$ of $\mathrm{U}(J_\tau)$ that are square integrable, that is, in the discrete series. Let $\Lambda$ be a self-dual lattice of $V$, $\mathfrak m \neq 0$ an ideal of $\mathcal O_E$, and $K = K(\Lambda, \mathfrak m)$ the congruence subgroup of level $\mathfrak m$ of the stabilizer of $\Lambda$ in $G(\mathbb A_{F,\mathrm f})$.

**Definition 1.17.1 (Coefficient and Poincaré series).** For vectors $v = (v_\tau)$ and $a = (a_\tau)$ of the spaces $H_\tau$ put
$$\phi_{v,a}(g) = \begin{cases} \prod_\tau \langle v_\tau, \sigma_\tau(g_\tau)\, a_\tau \rangle & \text{if } g_{\mathrm f} \in K, \\ 0 & \text{otherwise,} \end{cases}$$
for $g \in G(\mathbb A_F)$. For $c \in G(\mathbb A_F)$ the *Poincaré series* is
$$P_{v,c,a}(g) = \sum_{\gamma \in G(F)} \phi_{v,a}(c \gamma g).$$

**Definition 1.17.2 (Decay).** A pair $(v_\tau, a_\tau)$ has *decay of order* $N$ if there is $C$ with
$$|\langle v_\tau, \sigma_\tau(g)\, a_\tau \rangle|\,(1 + |g|)^N \leq C$$
for all $g \in \mathrm{U}(J_\tau)$. A vector $v$ has *$K$-decay* if each $v_\tau$ is $K_\tau$-finite and each pair $(v_\tau, a_\tau)$ with $a_\tau$ a $K_\tau$-finite vector has decay of order $2n^2 + 1$.

An *isotropic frame* of $V$ is a matrix $C$ of size $n \times r$ over $E$ whose columns span a totally isotropic subspace. Its stabilizer is a parabolic subgroup of $G$, and we write $N_C$ for its unipotent radical. A function $\varphi$ on $G(F)\backslash G(\mathbb A_F)$ is *cuspidal* if
$$\int_{N_C(F) \backslash N_C(\mathbb A_F)} \varphi(n g)\, dn = 0$$
for every isotropic frame $C$, every Haar measure and every $g$.

### The published inputs

The proofs of this section and the next take three results from the literature as hypotheses. They are fields of the bundle of [published local inputs](/step/published-results-first/).

**Theorem 1.17.3 (Harish-Chandra modules).** Let $\sigma$ be an irreducible unitary representation of a real unitary group $\mathrm{U}(J)$. Then the $K$-finite vectors of $\sigma$ are smooth, they form an admissible irreducible Harish-Chandra module, two such representations with isomorphic Harish-Chandra modules are unitarily equivalent, and the orbit map $g \mapsto \sigma(g) v$ of a $K$-finite vector $v$ is real analytic.

**Theorem 1.17.4 (Casselman-Wallach).** Let $\sigma$ be an irreducible unitary representation of $\mathrm{U}(J)$ and $E$ a smooth representation of moderate growth on a Fréchet space. A map $T_0$ of $(\mathfrak g, K)$-modules from the $K$-finite vectors of $\sigma$ to $E$ extends to a unique continuous $\mathrm{U}(J)$-map $T$ on the smooth vectors, the image of $T$ is closed, and, if $T_0 \neq 0$, each Sobolev norm on the smooth vectors is bounded by a continuous seminorm of $T$.

**Theorem 1.17.5 (Rapid decay of cusp forms).** Let $\varphi$ be an automorphic function on $G(\mathbb A_F)$ that is smooth at infinity, of uniform moderate growth and cuspidal. Then $\varphi$ is rapidly decreasing: for each $N$ there is $C$ with $|\varphi(g)|\, \mathrm{ht}(g)^N \leq C$, where $\mathrm{ht}$ is the height on a Siegel domain.

### The fibre integral of a coefficient

**Theorem 1.17.6 (Fibre integrals of a coefficient vanish).** Let $M$ be a model, $K$ an open subgroup of $G(\mathbb A_{F,\mathrm f})$, and $v, a$ vectors such that $(v_\tau, v_\tau)$ and $(v_\tau, a_\tau)$ have decay of order $2n^2+1$ for every $\tau$. Let $\tau$ be a real place and $C$ an isotropic frame. Then there are closed subgroups $P$ and $Q$ of $N_C(\mathbb A_F)$ that commute elementwise, with $P \cap Q = 1$ and $N_C(\mathbb A_F) = PQ$, such that
$$\int_P \phi_{v,a}(x\, p q\, y)\, d\nu(p) = 0$$
for every Haar measure $\nu$ on $P$, every $q \in Q$ and all $x, y \in G(\mathbb A_F)$.

Lean: `UpperTheory.Lit.Cusp.fibre_integral_eq_zero`.

*Proof.* Take for $P$ the component of $N_C(\mathbb A_F)$ at $\tau$ and for $Q$ the product of the other components. These subgroups are closed, they commute, they meet in $1$, and their product is $N_C(\mathbb A_F)$, since $N_C(\mathbb A_F)$ is a restricted product over the places. For $p \in P$ the components of $x p q y$ away from $\tau$ do not depend on $p$. So
$$\phi_{v,a}(x p q y) = R \cdot \langle v_\tau, \sigma_\tau(x_\tau\, p\, y_\tau)\, a_\tau \rangle,$$
where $R$ is a constant (the product of the other factors, or $0$ if the finite part is not in $K$), and the component of $q$ at $\tau$ is $1$. Through the component at $\tau$, the group $P$ is the unipotent radical of a proper parabolic subgroup of $\mathrm{U}(J_\tau)$, with its Haar measure. The function $p \mapsto \langle \sigma_\tau(x_\tau)^{*} v_\tau, \sigma_\tau(p)\, \sigma_\tau(y_\tau) a_\tau \rangle$ is a matrix coefficient of the square integrable irreducible representation $\sigma_\tau$, and the decay of order $2n^2+1$ makes it integrable on the unipotent radical. By Harish-Chandra's theorem that the matrix coefficients of the discrete series are cusp forms on the real group, its integral over the unipotent radical of a proper parabolic subgroup is $0$. So the integral over $P$ is $R \cdot 0 = 0$. $\square$

### Cuspidality of the Poincaré series

**Theorem 1.17.7 (The Poincaré series is cuspidal).** Let $M$ be a model, $\Lambda$ a self-dual lattice, $\mathfrak m \neq 0$, $v$ a vector with $K$-decay, $c \in G(\mathbb A_F)$, and $a$ a vector of $K_\tau$-finite vectors. Then $P_{v,c,a}$ is cuspidal.

Lean: `UpperTheory.Lit.Cusp.poin_isCuspFun`.

*Proof.* Fix an isotropic frame $C$, a Haar measure on $N = N_C(\mathbb A_F)$, a fundamental domain for $N_C(F)$ in $N$, and $g$. Put $f(y) = \phi_{v,a}(c y g)$. Write each $\gamma \in G(F)$ as $\gamma = \delta \beta$ with $\beta \in N_C(F)$ and $\delta$ in a set of representatives of $G(F)/N_C(F)$. Then
$$\int_{N_C(F) \backslash N} P_{v,c,a}(n g)\, dn = \int_{N_C(F)\backslash N} \sum_\delta \sum_{\beta \in N_C(F)} f(\delta \beta n)\, dn = \sum_\delta \int_N f(\delta n)\, dn.$$
The exchange of sum and integral needs absolute convergence. The quotient $N_C(F) \backslash N$ is compact, so a compact set covers it under translation by $N_C(F)$. The partial sums of the Poincaré series of $|\phi_{v,a}|$ are bounded on compact sets, by the decay of order $2n^2+1$. The unfolding inequality then bounds the integral of the sum of absolute values over the fundamental domain, and the sum over $N_C(F)$ is integrable on the fundamental domain and sums to the integral over $N$.

Each term $\int_N f(\delta n)\, dn$ is $0$. Choose a real place $\tau$ and take $P$ and $Q$ from the theorem on fibre integrals, applied to $v$ and $a$. The pair $(v_\tau, v_\tau)$ has decay since $v_\tau$ is $K_\tau$-finite and $v$ has $K$-decay. Since $N = PQ$ with $P \cap Q = 1$, the Haar measure of $N$ is the product of Haar measures of $P$ and $Q$, and
$$\int_N f(\delta n)\, dn = \int_Q \int_P \phi_{v,a}(c \delta\, p q\, g)\, d\nu(p)\, dq = 0,$$
since each inner integral is $0$. So the constant term along $N_C$ is $0$ for every $C$. $\square$

### Realization as automorphic forms

Write $\mathrm{Mult}(M, K)$ for the space of linear maps $y$ from the smooth vectors of $\bigotimes_\tau \sigma_\tau$ to smooth functions on $G(F) \backslash G(\mathbb A_F)/K$ that intertwine the real group action with right translation and that take values in square integrable cuspidal automorphic functions.

**Theorem 1.17.8 (Poincaré series are automorphic forms).** Assume the theorems on Harish-Chandra modules, Casselman-Wallach and rapid decay. Let $M$ be a model, $\Lambda$ a self-dual lattice, $\mathfrak m \neq 0$, $v$ a vector with $K$-decay and $c \in G(\mathbb A_F)$, and let $K = K(\Lambda, \mathfrak m)$. Then there is $y \in \mathrm{Mult}(M, K)$ with
$$y(\otimes_\tau a_\tau) = P_{v,c,a}$$
for every family $a$ of $K_\tau$-finite vectors.

Lean: `UpperTheory.Lit.Cusp.exists_multT_eq_poin`.

*Proof.* Let $T_0$ be the map $\otimes a_\tau \mapsto P_{v,c,a}$ on the $K$-finite vectors. Each value is an automorphic function of level $K$, and $T_0$ is linear in each $a_\tau$, so $T_0$ is defined on the tensor product. By the theorem on Harish-Chandra modules each value is smooth at infinity and of uniform moderate growth, with the same bounds for its derivatives, since $K$-finite vectors are smooth and their orbit maps are analytic. By the previous theorem each value is cuspidal. By the theorem on rapid decay each value is rapidly decreasing, so bounded and square integrable on a fundamental domain. A derivative in the Lie algebra moves $a_\tau$ to $d\sigma_\tau(X) a_\tau$, and an element $k$ of the maximal compact subgroup moves it to $\sigma_\tau(k) a_\tau$, so $T_0$ is a map of $(\mathfrak g, K)$-modules. By the theorem of Casselman-Wallach, $T_0$ extends to a continuous intertwining map $y$ on the smooth vectors. $\square$

### The nonzero period

At the bottom of the tower there is a row group $\mathrm U(Y_0)$, a core space $V_0$ and a stabilizer embedding $\iota_0$ of $\mathrm U(Y_0)$ into $\mathrm U(V_0)$. Write $\mathrm{Rows}(M_0)$ for the space of maps from the smooth vectors of a model $M_0$ of $\mathrm U(Y_0)$ to automorphic functions of the row level, and $\mathrm{Core}(M_P)$ for $\mathrm{Mult}(M_P, K_0)$ at the core level $K_0$. The *bottom period* of a form $F$ on $\mathrm U(V_0)$ and a function $u$ on $\mathrm U(Y_0)$ is
$$P_0(F, u) = \int_{\mathcal F} F(\iota_0(h))\, u(h)\, dh,$$
an integral over a fundamental domain of the row grid. *For large data* means: for each $\varepsilon$ and each $C_F \geq 6510$ there is $x_0$ such that the claim holds for all data of the tower with parameter $x \geq x_0$.

Two further hypotheses carry the real analysis. A *pack* is a choice of frames $A$ of $Y_0$ and $B$ of $V_0$, a $K$-finite vector $v_0$ with decay, a real point $g_0$ and a vector $w \neq 0$ of $M_0$, with the property that the integral of the coefficient of $v = \sigma(g_0) v_0$ against the coefficient of $w$ over the real row group is $c\langle b, w\rangle$ with $c \neq 0$, together with a bound of size $e^{Q}|c|$ for the far part of the integral and a Lipschitz bound. *Packs exist* if there is $C \geq 0$ such that for large data and all models there is a pack with $Q = C\,|\mathrm{Tau}|\,(r+1)^4 \log b$. *Depth pays* if for each $C \geq 0$ and large data there is a parameter $s$ that pays this loss against the norm of the level.

**Theorem 1.17.9 (A cusp form with a nonzero theta period).** Assume the theorems on Harish-Chandra modules, Casselman-Wallach and rapid decay, and assume that packs exist and depth pays. Then for large data the following holds. Let $M_0$ and $M_P$ be models, and let $t \in \mathrm{Rows}(M_0)$ be nonzero. Then there are $y \in \mathrm{Core}(M_P)$ and smooth vectors $v'$ and $w'$ with
$$P_0\big(y(v'), t(w')\big) \neq 0.$$

Lean: `UpperTheory.Lit.Cusp.exists_cusp_form_theta_period_ne_zero`.

*Proof.* Take a pack $p$ with frames $A, B$, vectors $v_0, w$ and point $g_0$, and a parameter $s$ that pays the loss. At the bottom of the grid the lattices of $Y_0$ and $V_0$ are self-dual, and the level of the row group maps into the core level under $\iota_0$.

1. The function $u = t(w)$ is bounded: there are $b \geq 0$ and a point $x$ with $|u| \leq b$ everywhere and $|u(x)| > b/2$. By the theorem on rapid decay, $u$ is automorphic, smooth, cuspidal and rapidly decreasing.
2. The unipotent periods of $u$ along a real one-parameter subgroup are Lipschitz with a constant $e^{Q} b$ given by the pack.
3. The line through $x$ in the direction of the frame $A$ is *long*. If it were short, the bound for cusp forms of level $\Lambda$ on short lines would give $|u(x)| \leq b/2$, by the Lipschitz bound and the bound on $s$. This contradicts the choice of $x$.
4. The real clauses of the pack give the adelic clauses of the unipotent period: a constant $c$ that controls the integral against $u$.
5. Since the line is long and the level norm is large, the pairing of the Poincaré series with $u$ is not zero:
$$\int_{\mathcal F} P_{v_0, c', v}(\iota_0(h))\, u(h)\, dh \neq 0,$$
where $v = \sigma(g_0) v_0$ and $c' = g_0^{-1}\iota_0(x^{-1})$.
6. By the theorem on Harish-Chandra modules, $v_0$ has $K$-decay. The previous theorem gives $y \in \mathrm{Mult}(M_P, K_0)$ with $y(\otimes a) = P_{v_0, c', a}$ for $K$-finite $a$.
7. Put $a' = \sigma(g_0) v_0$, a smooth vector. Since $y$ intertwines the real action with right translation, $y(a')(g) = y(v_0)(g g_0)$, and moving the real point $g_0$ through the Poincaré series gives $y(a') = P_{v, c', v}$ on the core.
8. The core level is the level of the self-dual lattice at the bottom, so $y \in \mathrm{Core}(M_P)$, and by step 5, $P_0(y(a'), t(w)) \neq 0$. $\square$

**Remark 1.17.10.** The vanishing of the integrals of discrete series matrix coefficients over unipotent radicals is Harish-Chandra's theorem that integrable matrix coefficients are cusp forms on the real group; see Harish-Chandra, *Automorphic forms on semisimple Lie groups*, Lecture Notes in Math. 62 (1968), Chapter I. The results taken as given are Harish-Chandra's theory of $(\mathfrak g, K)$-modules, from Harish-Chandra, *Representations of a semisimple Lie group on a Banach space I*, Trans. Amer. Math. Soc. 75 (1953), 185 to 243; the globalization theorem of W. Casselman, *Canonical extensions of Harish-Chandra modules to representations of G*, Canad. J. Math. 41 (1989), 385 to 438, with N. Wallach, *Real reductive groups II* (1992), Chapter 11; and the rapid decay of cusp forms, for which see C. Mœglin and J.-L. Waldspurger, *Spectral decomposition and Eisenstein series* (1995), Section I.2.

**Remark 1.17.11 (Formalization).** The four results are in the folder RealBands: `fibre_integral_eq_zero` ([FibreIntegralEqZero.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/RealBands/FibreIntegralEqZero.lean#L58)), `poin_isCuspFun` and `exists_multT_eq_poin` (ExistsMultTEqPoin.lean, lines 15 and 75), and `exists_cusp_form_theta_period_ne_zero` (Period.lean, line 18). The model is `DSModel` (ScalarOnPartsFull.lean, line 51), whose field `ds` gives the square integrability, and the coefficient, the Poincaré series and the decay conditions are `coefR`, `coef`, `poin`, `DecayAt` and `KDecay` in DepthPays.lean (lines 48 to 61). The three published inputs are the propositions `HarishChandraModules` (HarishChandraModulesOn.lean, line 43), `CasselmanWallach` (HasDRepIffHasDerivAt.lean, line 98) and `CuspRapidDecay` (ExistsNormLeHeightPow.lean, line 28). In the fibre integral the vanishing on the real unipotent radical is `integral_coef_eq_zero`, which the proof cites. The proof of the period theorem is a chain of cited results, among them `norm_cuspForm_le_of_shortLine` (in a `by_contra` that gives `Long`) and `poincareSeries_pairing_ne_zero_of_large_level`; we state what they give and not their proofs. The theorem gives the nonzero period for one pair $(v', w')$ only, and the vector $v'$ need not be $K$-finite; the next section removes both limits. The hypothesis `CasselmanWallach` enters only through `exists_multT_eq_poin`.
