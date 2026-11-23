---
title: The Jacobian of the big cell
decls:
  - Formalism.L2.SG.Pf.BH.sandwich'
  - Formalism.L2.SG.Pf.jacGauge_of_hearts3
  - Formalism.L2.SG.Pf.jacGauge_of_sandwich_rhsWLim
  - Formalism.L2.SG.Pf.jacGauge_of_rhsW
  - Formalism.L2.SG.Pf.jacGauge
  - Formalism.L2.SG.Closed.JacGauge_holds
  - Formalism.L2.SG.Closed.RealBracket_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Jacobian of the big cell

Let $G = \mathrm{U}(r + k, r + 1)$ with its parabolic subgroup $P = M N$ that stabilizes an isotropic flag of dimension $r$. The Bruhat decomposition writes almost every $g \in G$ as $n \, w(c, m) \, n'^{-1}$ with $n, n' \in N$ and $w(c, m)$ in a big cell parametrized by $c \in (\mathbb{C}^\times)^r$ and an element $m$ of the Levi block $\mathrm{U}(k, 1)$. This section computes the Haar measure of $G$ in these coordinates, after a second disintegration of $\mathrm{U}(k, 1)$ along the stabilizers of two negative vectors. The constant is explicit:
$$\frac{2^{r+1} V_k^2}{(T T')^k \, V_{k-1} \, a \, a' \, \kappa^2}.$$
Together with the [orbit constant](/entry/aprime-inf-holds/) it gives the real bracket, the archimedean factor of the [theta local matching](/step/theta-local-matching/), which is used by the [closed form of the tie at the real places](/entry/nc-tie-c-of-closed/).

### The group and the big cell

Fix $k \geq 1$ and $r \geq 0$, and let $n = 2r + k + 1$. Index the basis of $\mathbb{C}^n$ as $e_1, \dots, e_r$, then $k + 1$ middle vectors $b_0, \dots, b_k$, then $e^*_r, \dots, e^*_1$. Let $H$ be the [Hermitian form](/learn/algebra/#hermitian-and-skew-hermitian-forms) with $H(e_a, e^*_b) = \delta_{ab}$, with $H(b_i, b_i) = 1$ for $i < k$ and $H(b_k, b_k) = -1$, and with all other pairings $0$. Its signature is $(r + k, r + 1)$. Let $G = \mathrm{U}(H)$, and:

- $N \subseteq G$ the unipotent radical of the [parabolic subgroup](/learn/groups/#parabolic-subgroups) that stabilizes the flag $\langle e_1 \rangle \subseteq \langle e_1, e_2 \rangle \subseteq \dots$;
- $W_b \subseteq G$ the group of elements that fix every $e_a$ and $e^*_a$; it is the unitary group $\mathrm{U}(k, 1)$ of the middle block;
- for a vector $z$ in the middle block with $T_z = -H(z, z) > 0$, $W_z \subseteq W_b$ the stabilizer of $z$; it is a compact group $\mathrm{U}(k)$.

For $c \in \mathbb{C}^r$ and $\mu \in M_{k+1}(\mathbb{C})$ the *big cell matrix* $w(c, \mu)$ sends $e_a$ to $c_a e^*_a$, acts by $\mu$ on the middle block, and sends $e^*_a$ to $\bar c_a^{-1} e_a$. The *long Weyl element* is $w_0 = w(1, 1)$, and $w_0^2 = 1$. For $a < r$ let $M_a = 2(r - a) + k + 1$, the dimension of the unitary group that the $a$-th step of the flag leaves.

**Definition 5.3.1 (Gauge measure on a subgroup).** Let $S$ be a closed subgroup of $\mathrm{GL}_n(\mathbb{C})$ with Lie algebra $\mathfrak{s}$, a Euclidean space for the Frobenius norm. A measure $\mu$ on $S$ is a *gauge measure* if it is a Haar measure on $S$ and $\mu(\exp B_\rho) / \mathrm{vol}(B_\rho) \to 1$ as $\rho \to 0^+$, where $B_\rho$ is the ball in $\mathfrak{s}$. For $\kappa > 0$ we write $\mathrm{haar}_\kappa(N)$ for the Haar measure on $N$ that is $\kappa$ times the image of Lebesgue measure on its Lie algebra under $\exp$.

Lean: `Formalism.L2.SG.Pf.IsGaugeOn`, `Formalism.MainNotions.S.haarLie`.

This is the normalization of [the first section](/entry/exp-prod-u-holds/): the gauge measure is $\gamma^{-1}$ times any Haar measure. On a unipotent group, $\exp$ is a diffeomorphism from the Lie algebra, so $\mathrm{haar}_\kappa(N)$ is a Haar measure.

**Definition 5.3.2 (Weights).** For $T, T' > 0$, $c \in \mathbb{C}^r$ and $\zeta \in \mathbb{C}$ let
$$\begin{aligned} w(c, \zeta) &= \prod_{a < r} |c_a|^{2(M_a - 2)} \cdot (|\zeta|^2 - T T')^{k-1} \quad \text{if } |\zeta|^2 \geq T T', \\ w(c, \zeta) &= 0 \quad \text{otherwise}. \end{aligned}$$
For two middle vectors $z, z'$ with $T = T_z > 0$, $T' = T_{z'} > 0$, a *section* is a smooth map $\zeta \mapsto \mu(\zeta)$ on $\{ |\zeta|^2 > T T' \}$ with values in $\mathrm{U}(k, 1)$, such that $H(\mu(\zeta) z', z) = \zeta$.

Lean: `Formalism.QuantumDeterminants.bcWeight`, `Formalism.QuantumDeterminants.IsSection`.

The invariant $\zeta = H(m z', z)$ classifies the double cosets $W_z \backslash \mathrm{U}(k, 1) / W_{z'}$ on the open set $|\zeta|^2 > T T'$, and the section picks a representative in each.

**Theorem 5.3.3 (Haar measure on the big cell).** Let $k \geq 1$, $r \geq 0$, and let $z, z'$ be middle vectors with $T = T_z > 0$ and $T' = T_{z'} > 0$. Let $\mu$ be a gauge measure on $G$. Let $\mu_W, \mu_{W'}$ be Haar measures on $W_z, W_{z'}$ with total masses $a, a' > 0$. Let $\kappa > 0$ and let $\zeta \mapsto \mu(\zeta)$ be a section. For $s = n h$ with $n \in N$, $h \in W_z$, let $\mu_S$ be the image of $\mathrm{haar}_\kappa(N) \times \mu_W$ under multiplication, and similarly $\mu_{S'}$. Then for every measurable $\varphi \geq 0$ on $G$,
$$\begin{aligned} \int_G \varphi \, d\mu = {} & \frac{2^{r+1} V_k^2}{(T T')^k V_{k-1} a a' \kappa^2} \\ & \cdot \int_{\mathbb{C}^r \times \mathbb{C}} w(c, \zeta) \int \int \varphi\big(s \, w(c, \mu(\zeta)) \, s'^{-1}\big) \, d\mu_{S'}(s') \, d\mu_S(s) \, dc \, d\zeta. \end{aligned}$$

Lean: `Formalism.L2.SG.Pf.JacGauge`.

### Two inputs

The proof combines a Bruhat disintegration of $\mu$ with a disintegration of the Levi block. Both constants come from limits of small balls. The first input compares a small ball of $G$ with a box in the big cell coordinates.

For $n, n' \in N$, $c \in \mathbb{C}^r$ and $m \in W_b$ let $\Psi(n, c, m, n') = w_0 \, n \, w(c, 1) \, m \, n'^{-1}$; for $c = 1$ and $n, m, n'$ close to $1$ this element is close to $1$, since $w_0^2 = 1$. Let $\rho_S(x)$ be the least norm of an element $Y$ of the Lie algebra of $S$ with $\exp Y = x$, and let
$$Q(n, c, m, n') = \rho_N(n)^2 + 2 \sum_a |c_a - 1|^2 + \rho_{W_b}(m)^2 + \rho_N(n')^2.$$

**Lemma 5.3.4 (Sandwich).** For all $k, r$ and every $0 < \varepsilon < 1$ there is $\delta > 0$ such that for all $0 < \rho < \delta$ and all $n, n' \in N$, $c \in \mathbb{C}^r$, $m \in W_b$:

1. if $\Psi(n, c, m, n') \in \exp B_\rho$, then $Q(n, c, m, n') < ((1 + \varepsilon) \rho)^2$;
2. if $Q(n, c, m, n') < ((1 - \varepsilon) \rho)^2$, then $\Psi(n, c, m, n') \in \exp B_\rho$.

Lean: `Formalism.L2.SG.Pf.BH.sandwich'`.

*Proof.* The map $(Y_N, t, Y_b, Y'_N) \mapsto \Psi(\exp Y_N, 1 + t, \exp Y_b, \exp Y'_N)$ is smooth near $0$, and its differential at $0$ is $(Y_N, t, Y_b, Y'_N) \mapsto \mathrm{Ad}(w_0) Y_N + \dot w(t) + Y_b - Y'_N$, where $\dot w(t)$ is the derivative of $w(1 + t, 1)$. The Lie algebra of $G$ is the orthogonal sum of $\mathrm{Ad}(w_0) \mathfrak{n}$, the torus directions of the big cell, $\mathfrak{w}_b$ and $\mathfrak{n}$, and the differential is an isometry onto when the torus coordinate $t \in \mathbb{C}^r$ has the norm $2 \sum |t_a|^2$. A smooth map whose differential at $0$ is an isometry onto maps the ball of radius $\rho$ into the ball of radius $(1 + \varepsilon)\rho$ and covers the ball of radius $(1 - \varepsilon) \rho$, for $\rho$ small. Pulling back by the logarithms gives both claims. $\square$

The second input is the limit for the Levi block. For a Haar measure $\mu_W$ of total mass $a$ on $W_z$ and $\mu_{W'}$ of mass $a'$ on $W_{z'}$, and a section $\mu(\zeta)$, let
$$R(\varphi) = \int_{\mathbb{C}} (|\zeta|^2 - T T')_+^{k-1} \int \int \varphi(h \, \mu(\zeta) \, h'^{-1}) \, d\mu_{W'}(h') \, d\mu_W(h) \, d\zeta.$$

**Theorem 5.3.5 (Levi limit).** Let $z, z'$ be middle vectors with $T, T' > 0$, with Haar measures of masses $a, a'$ on their stabilizers and a section. Let $m_0 = \mu(\zeta_0)$ be the value of the section at $\zeta_0 = 2 \sqrt{T T'}$, and let $B^b_\rho = m_0 \exp(B_\rho)$ with $B_\rho$ the ball in the Lie algebra of $W_b$. Then
$$\lim_{\rho \to 0^+} \frac{R(\mathbf{1}_{B^b_\rho})}{\mathrm{vol}(B_\rho)} = \frac{(T T')^k V_{k-1} a a'}{2 V_k^2}.$$

Lean: `Formalism.L2.SG.Pf.WB.RhsWLim`.

We take this limit as an input of the proof.

### The proof

**Proposition 5.3.6 (Big cell from the sandwich and three limits).** Assume the sandwich lemma, the Levi limit, the existence of a gauge measure on $\mathrm{U}(r)$ for every $r$ (the case $k = 0$ of $W_b$), and the ball limit $\mu^{\mathrm{g}}_{W_b}(\{x : w_0 x \in \exp B_\rho\}) / \mathrm{vol}(B_\rho) \to 2^{-r}$. Then the theorem on the big cell holds.

Lean: `Formalism.L2.SG.Pf.jacGauge_of_hearts3`.

*Proof.* The sandwich lemma and the ball limit give the Bruhat form of a gauge measure on $G$:
$$\int_G \varphi \, d\mu = 2^r \int_{\mathbb{C}^r} \prod_a |c_a|^{2(M_a - 2)} \int_N \int_{W_b} \int_N \varphi(n \, w(c, 1) \, m \, n'^{-1}) \, dn' \, d\mu_b(m) \, dn \, dc,$$
with gauge measures on $N$ and $W_b$. Indeed both sides are invariant measures on the open cell, so they agree up to a constant, and the constant is read off from small balls: by the sandwich, the ball $\exp B_\rho$ corresponds to the set $Q < \rho^2$ up to the factor $1 \pm \varepsilon$, whose measure in the product coordinates is $\mathrm{vol}(B_\rho)$ times the ball limit. The Levi limit gives in the same way the disintegration of the gauge measure of $W_b = \mathrm{U}(k, 1)$ along $W_z \backslash W_b / W_{z'}$, with the constant $2 V_k^2 / ((T T')^k V_{k-1} a a')$, the inverse of the limit. The existence of gauge measures in every rank makes both sides well defined. Substituting the second disintegration into the first, moving the elements of $W_z$ and $W_{z'}$ through the big cell (they commute with $w(c, 1)$), and replacing the gauge measure on $N$ by $\mathrm{haar}_\kappa(N)$, which divides by $\kappa$ on each side, gives the theorem with the factor $2^r \cdot 2 = 2^{r+1}$ and $\kappa^{-2}$. $\square$

The ball limit and the gauge measures in every rank are proved.

**Corollary 5.3.7 (Big cell from the sandwich and the Levi limit).** If the sandwich lemma and the Levi limit hold, then the theorem on the big cell holds.

Lean: `Formalism.L2.SG.Pf.jacGauge_of_sandwich_rhsWLim`.

*Proof.* This is the [proposition](/entry/jac-gauge-of-hearts3/) applied to the existence of a gauge measure on $\mathrm{U}(r)$ for every $r$. $\square$

**Corollary 5.3.8 (Big cell from the Levi limit).** If the Levi limit holds, then the theorem on the big cell holds.

Lean: `Formalism.L2.SG.Pf.jacGauge_of_rhsW`.

*Proof.* This is the [corollary](/entry/jac-gauge-of-sandwich-rhs-wlim/) applied to the [sandwich lemma](/entry/sandwich-prime/). $\square$

**Theorem 5.3.9 (Haar measure on the big cell, closed form).** Assume the Levi limit. Then the theorem on the big cell holds.

Lean: `Formalism.L2.SG.Pf.jacGauge` (also `Formalism.L2.SG.Closed.JacGauge_holds`, a second name).

*Proof.* This is the [corollary](/entry/jac-gauge-of-rhs-w/) applied to the Levi limit. $\square$

### The real bracket

The two constants of this section and of the [orbit constant](/entry/aprime-inf-holds/) combine into one identity between archimedean volumes. Let $c_X(u, u')$ be the constant with which the Haar measure of $G_\infty$ disintegrates along the double cosets $N H \backslash G_\infty / H' N'$ attached to the frames of $u$ and $u'$. Let $F_N, F_N'$ be fundamental domains for the unipotent radicals, with the product measures $\mu_N, \mu_{N'}$, and let $e = -(8 r^3 + 6 r^2 + 6 k r^2 + r)/3$.

**Theorem 5.3.10 (Real bracket).** Assume the volume of $\mathrm{U}(k)$ for all $k$ and the Levi limit. Assume also that the reference volumes of the fundamental domains satisfy $\mathrm{vol}(F_N) \mathrm{vol}(F_N') = |d_F|^{e}$. Under the standing hypotheses of the setting, if $a' > 0$ is an orbit constant for $u'$, then
$$\begin{aligned} c_X(u, u') \, \mu_H(H_\infty) \, \mu_N(F_N) \, \mu_{N'}(F_N') = {} & a' \, 2^{kd} \left( \frac{\pi^k}{(k-1)!} \right)^{d} \\ & \cdot T_u^{-kd} \, |d_F|^{e}. \end{aligned}$$

Lean: `Formalism.L2.SG.Closed.RealBracket_holds`.

*Proof.* At each infinite place the [theorem on the big cell](/entry/jac-gauge/) disintegrates the gauge measure of $G_v$ along $N H \backslash G_v / H' N'$, with the constant $2^{r+1} V_k^2 / ((T T')^k V_{k-1} a a' \kappa^2)$. With the covolume identity, this splits $c_X(u, u')$ as a product of local constants over the $d$ places. The local disintegrations are exact in the product, so the product of the local identities is the global one. The gauge density exists at every place, and it converts the gauge measure to the fixed Haar measure. The [orbit constant](/entry/aprime-inf-holds/) gives $a' = \gamma V_k^d T_{u'}^{-kd} / \mu_H(H_\infty)$, which removes $\gamma$, the total masses of the stabilizers and the powers of $T_{u'}$. What remains at each place is a ratio of $V_k^2 / V_{k-1}$ to $V_k$, and $V_k / V_{k-1} = (2\pi)^k / (k-1)!$ gives the factor $2^k \pi^k / (k-1)!$ of the right side. $\square$

**Remark 5.3.11 (Formalization).** The Levi limit is assumed through an instance argument `[Fact WB.RhsWLim]`; the closed form `jacGauge` uses `WB.rhsWLim'` ([JacConstFinal.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/JacConstFinal.lean#L8)), and the instance is provided in `Development` (`RhsWLimOfLeaves.lean`, line 49). Likewise the real bracket takes `[Fact GaugeVolUD]` and `[Fact RhsWLim]`, and the covolume identity `CovolRef` as an explicit hypothesis. The disintegration constant $c_X$ (`DisintegrationConstant`) is not unfolded here. The sandwich statement `Sandwich` is defined twice with the same body, in `PeriodIntegrals/SwSand.lean` (line 116) and in `JacConstBHR.lean` (line 25); `w0B`, `gBall` and `WbDataEx` are also defined twice. The proof of the sandwich lemma is `sandwich_of_chart` with ten inputs on the Lie algebra charts.
