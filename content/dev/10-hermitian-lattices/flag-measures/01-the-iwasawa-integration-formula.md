---
title: The Iwasawa integration formula on U(p,q)
decls:
  - GlobalTheory.IwConst.iwasawa_constant
  - GlobalTheory.T.iwasawa_integration_formula_constant
  - GlobalTheory.FlagMeas.iwasawaFormula
  - GlobalTheory.T.unitary_iwasawa_integration_formula_real_place
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Iwasawa integration formula on U(p,q)

This section proves an integration formula on the real group $U(p,q)$ for the decomposition $g = umk$ along an isotropic flag. Here $u$ is in the unipotent radical $N$ of the flag, $m$ is in a Levi factor $M$ and $k$ is in the maximal compact subgroup $K$. The Haar measure of $U(p,q)$ is the product of gauge measures on $N$, $M$ and $K$, times the inverse modulus of $M$ on $N$ and an explicit constant $c_{\mathrm{Iw}}(p,q,j)$. The formula is used at each real place in the bound for the measure of one flag class (the third section), which is the base of the flag measure bound of the counting theorem.

### Gauge measures

Let $n = p + q$ and let $\varepsilon \colon \{1, \dots, n\} \to \{\pm 1\}$ take the value $+1$ exactly $p$ times. Let $J_\varepsilon$ be the diagonal matrix with entries $\varepsilon(1), \dots, \varepsilon(n)$, a [[Hermitian form|8NJ7XY6F1S]] on $\mathbb{C}^n$ of signature $(p,q)$ (see [Hermitian forms](/learn/algebra/#hermitian-and-skew-hermitian-forms)). Let $G = U(J_\varepsilon) \cong U(p,q)$ be its [unitary group](/learn/groups/#unitary-groups), with a fixed [Haar measure](/learn/analysis/#haar-measure) $\mu_G$. For $g \in G$ and $r > 0$ put
$$B_r = \{ g \in G : \|g - 1\|_{\mathrm{HS}} \le r \},$$
where $\|X\|_{\mathrm{HS}}^2 = \operatorname{tr}(X^* X)$ is the Hilbert-Schmidt norm. For $d \ge 0$ let $\omega_d$ be the volume of the unit ball of $\mathbb{R}^d$.

**Definition 3.1.1 (Gauge constant).** A real number $c$ is a *gauge constant* for $G$ if
$$\lim_{r \to 0^+} \frac{c\, \mu_G(B_r)}{r^{n^2}} = \omega_{n^2}.$$

So $c\,\mu_G$ is the Haar measure that gives small balls around $1$ their Euclidean volume in the real vector space of dimension $n^2 = \dim_{\mathbb{R}} G$.

**Definition 3.1.2 (Gauge measure on a subset).** Let $S \subseteq G$ and $d \ge 0$. A measure $\nu$ on $G$ is a *gauge measure on $S$ of dimension $d$* if $\nu(G \setminus S) = 0$, the left translate of $\nu$ by each $s \in S$ is $\nu$, and
$$\lim_{r \to 0^+} \frac{\nu(B_r)}{r^d} = \omega_d.$$

### Isotropic flags and their groups

**Definition 3.1.3 (Isotropic flag).** Let $a \ge 0$ and $j_1, \dots, j_a \ge 1$, and put $s = j_1 + \dots + j_a$. An *isotropic flag of type $j$* is a chain of complex subspaces $0 = W_0 \subseteq W_1 \subseteq \dots \subseteq W_a$ of $\mathbb{C}^n$ with $\dim W_i = \dim W_{i-1} + j_i$, such that $y^* J_\varepsilon x = 0$ for all $x, y \in W_a$.

For such a flag let $W_a^\perp$ be the orthogonal space of $W_a$ for $J_\varepsilon$. We use three subsets of $G$:

1. $N = N(W)$, the set of $g$ with $gy - y \in W_{i-1}$ for $y \in W_i$ and each $i$, and $gy - y \in W_a$ for $y \in W_a^\perp$;
2. $M = M(W)$, the set of $g$ with $g W_i \subseteq W_i$ and $g^* W_i \subseteq W_i$ for each $i$;
3. $K$, the set of $g$ with $g^* g = 1$.

So $N$ is the unipotent radical of the [parabolic subgroup](/learn/groups/#parabolic-subgroups) that fixes the flag, $M$ is a Levi factor of it, and $K \cong U(p) \times U(q)$ is a [maximal compact subgroup](/learn/groups/#reductive-groups-and-maximal-compact-subgroups). The real dimensions are
$$d_N = 4 \sum_{i < k} j_i j_k + 2 s (n - 2s) + \sum_i j_i^2, \qquad d_M = (n - 2s)^2 + 2 \sum_i j_i^2.$$

For a matrix $m$ that preserves each $W_i$, let $\det(m|W_i)$ be the determinant of its restriction to $W_i$. The *local sizes* of $m$ are
$$\tau_i(m) = \Bigl( \frac{|\det(m|W_i)|}{|\det(m|W_{i-1})|} \Bigr)^{-1/j_i}, \qquad 1 \le i \le a.$$

**Definition 3.1.4 (Layer product).** For $n, f \ge 0$, a type $j$ of length $a$, $\tau \in \mathbb{R}^a$ and a function $\Gamma \colon \mathbb{R} \to \mathbb{R}$ put
$$
\begin{aligned}
\Pi_{n,f,j}(\tau; \Gamma) = {}& \prod_{i < k} \Gamma(\tau_i/\tau_k)^{2 j_i j_k f}\, \Gamma(\tau_i \tau_k)^{2 j_i j_k f} \\
& \cdot \prod_i \Gamma(\tau_i)^{2 j_i (n - 2s) f}\, \Gamma(\tau_i^2)^{j_i^2 f}.
\end{aligned}
$$

We write $\delta(m) = \Pi_{n,1,j}(\tau(m); \mathrm{id})$. This is the inverse of the modulus of $m$ acting on $N$ by conjugation: the factors list the blocks of the Lie algebra of $N$, the pairs $(i,k)$ with their two blocks of size $j_i \times j_k$, the blocks between $W_i$ and the anisotropic part, and the skew-Hermitian blocks of size $j_i$.

### The constant

For $i \ge 0$ put
$$\sigma(i) = \prod_{l=1}^{i} \frac{2 \pi^l}{(l-1)!}, \qquad V(i) = \sigma(i)\, 2^{i(i-1)/2}.$$
The product $\sigma(i)$ is the product of the volumes of the unit spheres $S^1, S^3, \dots, S^{2i-1}$, and $V(i)$ has the form of the volume of the compact group $U(i)$ for a Riemannian metric given by the Hilbert-Schmidt norm. The *Iwasawa constant* is
$$c_{\mathrm{Iw}}(p,q,j) = \frac{2^{-d_N/2}\, V(p)\, V(q)}{\prod_i \bigl(V(j_i)\, 2^{j_i^2/2}\bigr) \cdot V(p-s)\, V(q-s)}.$$

**Theorem 3.1.5 (Iwasawa constant).** Let $W$ be an isotropic flag of type $j$ with all $j_i \ge 1$. Let $\mu_N$ be a gauge measure on $N$ of dimension $d_N$, $\mu_M$ a gauge measure on $M$ of dimension $d_M$, and $\mu_K$ a measure with $\mu_K(G \setminus K) = 0$, $\mu_K(G) = 1$ and invariant under left translation by $K$. Let $c$ be a gauge constant for $G$ and $\kappa \in [0, \infty]$. Assume that for every measurable $\varphi \colon G \to [0, \infty]$
$$\int_G \varphi \, d\mu_G = \kappa \int_N \int_M \delta(m) \int_K \varphi(umk)\, d\mu_K(k)\, d\mu_M(m)\, d\mu_N(u).$$
Then $c \kappa = c_{\mathrm{Iw}}(p,q,j)$.

Lean: `GlobalTheory.IwConst.iwasawa_constant` (also `GlobalTheory.T.iwasawa_integration_formula_constant`, a second name).

*Proof.* The proof compares the measures of the small balls $B_r$ on both sides as $r \to 0$.

1. *Dimensions.* Let $L = K \cap M$ and $d_L = (p-s)^2 + (q-s)^2 + \sum_i j_i^2$. Then $n^2 = 2 d_N + d_M$ and $p^2 + q^2 = d_N + d_L$.
2. *Lie algebras.* The sets $N$, $M$, $K$ and $L$ are the sets of $g$ with $g - 1$ in real subspaces $\mathfrak{n}$, $\mathfrak{m}$, $\mathfrak{k}$, $\mathfrak{l}$ of the matrices, each with an orthonormal basis for the real part of the Hilbert-Schmidt inner product. These four spaces are in a fixed relative position. In the coordinates of the bases, the gauge function on $\mathfrak{n} \times \mathfrak{m} \times \mathfrak{k}$ that measures $\|umk - 1\|_{\mathrm{HS}}$ to first order is definite, and the volume of its unit body is $2^{d_N/2}\, \omega_{2 d_N + d_M}\, \omega_{d_L}$.
3. *Compact volumes.* There are gauge measures $\mu_0$ on $K$ of dimension $p^2 + q^2$ and $\nu_L$ on $L$ of dimension $d_L$. Their total masses are $\mu_0(K) = V(p) V(q)$ and
$$\nu_L(L) = \prod_i \bigl(V(j_i)\, 2^{j_i^2/2}\bigr) \cdot V(p-s)\, V(q-s).$$
4. *Right invariance.* For a unitary $U$ the map $X \mapsto U^* X U$ keeps the Hilbert-Schmidt norm. So a gauge measure on a subgroup that is closed under such conjugation is also right invariant under its unitary elements. This applies to $\mu_0$ under $K$, and to $\mu_M$ and $\nu_L$ under $L$. A right $K$-invariant measure of finite mass is a multiple of the left invariant probability measure on the compact group, so $\mu_0 = V(p) V(q)\, \mu_K$.
5. *Small balls.* The integral of the indicator of $B_r$ over $N \times M \times K$, with the weight $\delta$, is unfolded over the compact Levi part $L$. Its quotient by $r^{2 d_N + d_M + p^2 + q^2}$ has a limit given by the unit body volume of step 2. The ball $B_r$ is squeezed between slabs of radius $r/(1+\eta)$ and $(1+\eta)r$ for each $\eta > 0$, so both sides have the same limit.
6. *Comparison.* By the hypothesis with $\varphi = \mathbf 1_{B_r}$ and the gauge property of $c$, the limit of $c\, \mu_G(B_r)/r^{n^2}$ is $\omega_{n^2}$ and also $c \kappa$ times the limit of step 5. The dimension count of step 1 makes the powers of $r$ agree. Uniqueness of limits, with the masses of step 3 and the factor $2^{d_N/2}$ of step 2, gives $c \kappa = c_{\mathrm{Iw}}(p,q,j)$. $\square$

**Theorem 3.1.6 (Iwasawa integration formula).** Let $W$, $\mu_N$, $\mu_M$, $\mu_K$ be as in the theorem above and let $c$ be a gauge constant for $G$. Then for every measurable $\varphi \colon G \to [0,\infty]$
$$
\begin{aligned}
c \int_G \varphi \, d\mu_G = c_{\mathrm{Iw}}(p,q,j) \int_N \int_M & \delta(m) \\
& \cdot \int_K \varphi(umk)\, d\mu_K\, d\mu_M\, d\mu_N.
\end{aligned}
$$

Lean: `GlobalTheory.FlagMeas.iwasawaFormula` (also `GlobalTheory.T.unitary_iwasawa_integration_formula_real_place`, a second name).

*Proof.* The formula up to a constant gives $\kappa \in (0, \infty)$ such that the hypothesis of the theorem on the Iwasawa constant holds. That theorem gives $c\kappa = c_{\mathrm{Iw}}(p,q,j)$. Multiply the identity for $\kappa$ by $c$. $\square$

The formula up to a constant is the decomposition of Haar measure along a parabolic subgroup and a maximal compact subgroup (Knapp, *Lie Groups Beyond an Introduction*, second edition, Chapter VIII): the map $(u,m,k) \mapsto umk$ is onto $G$, its fibres are the sets $\{(u, ml, l^{-1}k) : l \in L\}$, and the pushed product measure with the weight $\delta$ is a Haar measure. Its proof is below the results of this section and is not reproduced here.

**Remark 3.1.7 (Formalization).** The formula up to a constant, `GlobalTheory.FlagMeas.iwasawa_shape` in IwasawaIntegrationFormulaUpToConstant.lean, is not unfolded here. The statement of the Iwasawa constant allows $\kappa = \infty$; the conclusion $c\kappa = c_{\mathrm{Iw}}$ then shows $\kappa < \infty$. The steps of its proof use results not unfolded here: `isotropicFlag_dimension_count`, `exists_nilpotentAlgebra_isotropicFlagUnipotentRadical`, `iwasawa_lieAlgebras_relative_position`, `iwasawaGauge_definite_and_unitBody_volume`, `volume_unitaryMaximalCompact_eq_prod`, `volume_maximalCompact_inter_isotropicFlagLevi`, `localisedIwasawaIntegral_smallBall_asymptotics` and `slab_measure_squeeze'`. The right invariance of step 4 is the private lemma `map_mul_right_eq_of_isGaugeSub` (IwasawaIntegrationFormulaConstant.lean, line 97). The Haar measure $\mu_G$ (`Formalism.REAL.muG`) and the group $U(J_\varepsilon)$ (`Formalism.REAL.UJ`) are not unfolded. The two second names are proved by a `first | exact ...` combinator under `set_option maxHeartbeats 1000000`.
