---
title: Haar measure on the big cell
decls:
  - GlobalTheory.CellDens.bigCell_integral
  - GlobalTheory.T.lintegral_bigCell_haar_density_constant
  - GlobalTheory.DoubleCosetMeasure.isDis_bigCell
  - GlobalTheory.T.besselDoubleCosetMeasure_bigCell_eq
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Haar measure on the big cell

The Hilbert-Schmidt bounds of [Section 2.18.7](/entry/lintegral-hs-norm-sq-amp-j-le/) integrate over the double cosets $U_z N \backslash G / U_{z'} N$. To compute these integrals one needs the Haar measure of $G$ in coordinates adapted to the double cosets. This section gives two such formulas, with exact constants. The first is the Bruhat integration formula: almost all of $G$ is the big cell $N w M N$, and Haar measure is a product of Haar measures on the factors times a power of the torus coordinates. The second refines the first by integrating out the stabilizers of $z$ and $z'$ in the middle group, which leaves a measure on $r + 1$ complex parameters. Both feed the orbital integrals of [Section 2.18.3](/entry/oo-eq-inv-deg-smul-iint/) and through them [the step](/step/nonempty-hyps/).

We keep the archimedean setting of [Section 2.6.8](/entry/fibre-normal-fibre-volume/): $n = 2r + k + 1$, the basis $e_0, \dots, e_{r-1}$ of an isotropic subspace, the dual basis $e^*_a$, the space $W_b$ of dimension $k + 1$ between them, the form $H$ with $G = U(H)$, and the flag unipotent group $N$. Let $H_b = \operatorname{diag}(1, \dots, 1, -1)$ be the form on $W_b$ and $M = U(H_b) \cong U(k, 1)$.

**Definition 2.26.1 (Haar measures normalized by density).** Let $S$ be a closed subgroup of $GL_n(\mathbb{C})$ with real Lie algebra $\mathfrak{s}$, carrying the Hilbert-Schmidt inner product. A measure $\mu$ on $S$ has *density* $c$ at the identity if
$$\lim_{\rho \to 0^+} \frac{\mu\bigl(\exp B_{\mathfrak{s}}(\rho)\bigr)}{\operatorname{vol}\bigl(B_{\mathfrak{s}}(\rho)\bigr)} = c,$$
where $B_{\mathfrak{s}}(\rho)$ is the ball of radius $\rho$ in $\mathfrak{s}$. For $\kappa > 0$ let $\kappa\, dn$ be the image of $\kappa$ times Lebesgue measure on the Lie algebra of $N$ under the exponential map.

A Haar measure is determined by its density, since two Haar measures differ by a scalar and the scalar is the ratio of their densities. On the unipotent group $N$ the exponential map is a diffeomorphism and $\kappa\, dn$ is a Haar measure of density $\kappa$.

**Definition 2.26.2 (Big cell element).** For $x \in (\mathbb{C}^\times)^r$ and $m \in M$ let $w(x, m) \in GL_n(\mathbb{C})$ be the matrix that maps $e_a$ to $x_a e^*_a$, maps $e^*_a$ to $\bar x_a^{-1} e_a$ (with the indexing of the setting), and acts by $m$ on $W_b$. Put $d_a = 2(r - a) + k + 1$ and
$$\omega(x) = \prod_{a < r} |x_a|^{2(d_a - 2)}.$$

So $w(x, m)$ is the long Weyl element of the flag, twisted by the torus element with entries $x_a$, times an element of the middle group. The weight $\omega$ is the modulus of the torus on the Lie algebra of $N$, up to the change from $x$ to the polar coordinates of the torus.

**Theorem 2.26.3 (Haar measure on the big cell).** Let $c, c_b > 0$. Let $\mu_G$ be a Haar measure on $G$ with density $c$ and $\mu_b$ a Haar measure on $M$ with density $c_b$. Then for every measurable $f \ge 0$ on matrices
$$\begin{aligned} \int_G f\, d\mu_G = {} & \frac{c}{c_b}\, 2^r \int_{\mathbb{C}^r} \omega(x) \\ & \cdot \int f\bigl(n^{-1}\, w(x, 1)\, m\, n'\bigr)\, dn\, dn'\, d\mu_b(m)\, dx, \end{aligned}$$
where $dn$ and $dn'$ are the Haar measures of density $1$ on $N$ and $dx$ is Lebesgue measure on $\mathbb{C}^r$.

Lean: `GlobalTheory.CellDens.bigCell_integral` (also `GlobalTheory.T.lintegral_bigCell_haar_density_constant`, a second name).

*Proof.* The proof has two steps. First, an iterated integration formula for $G$ with respect to $N$, the torus and $M$ gives a constant $C \ge 0$ such that, for every measurable $f \ge 0$, $\int f\, d\mu_G$ equals $C$ times the right side without the factor $\tfrac{c}{c_b} 2^r$. This is the Bruhat decomposition of $G$ for the parabolic subgroup of the flag: the map $(n, x, m, n') \mapsto n^{-1} w(x, 1) m n'$ covers the big cell, whose complement has measure $0$, and uniqueness of Haar measure leaves only the constant $C$ free. The factor $\omega(x)$ is the Jacobian of the torus part. Second, we find $C$ by comparing densities. Take a chart of $G$ near the big cell, built from the exponential map, and let $\rho \to 0^+$. The measure $\mu_G$ of the image of a ball of radius $\rho$, divided by the volume of the ball, tends to $c$. The same quotient for the right side tends to $C 2^{-r}$ times the limit of the ball mean of the weight, which is $1$, times the density $c_b$ of $\mu_b$. So $c = C 2^{-r} c_b$, and $C = 2^r c / c_b$. $\square$

**Definition 2.26.4 (Regular double cosets).** The *regular set* is the set of $\gamma \in G$ with $D_l(\gamma) \ne 0$ for all $l \le r$ and
$$|D_{r+1}(\gamma)|^2 - T(z) T(z') |D_r(\gamma)|^2 \ne 0.$$
For measures $\mu_S$, $\mu_S'$ on $G$ and $\nu$ on matrices, the triple *disintegrates* $\mu_G$ on a set $\Omega$ if $\nu$ is $\sigma$-finite, $\nu$ is carried by $\Omega$, and for every measurable $f \ge 0$
$$\int f\, d\mu_G = \int \int f(s\, \gamma\, s'^{-1})\, d\mu_S(s)\, d\mu_S'(s')\, d\nu(\gamma).$$

This is the notion of [Section 2.18.3](/entry/oo-eq-inv-deg-smul-iint/): the measure $\nu$ is a measure on representatives of the double cosets.

**Definition 2.26.5 (Section of the middle group).** For $z \in W_b$ let $z_b$ be its component in $W_b$. A *section* for $(z, z')$ is a family $m(\zeta) \in M$ for $\zeta \in \mathbb{C}$, smooth on $\{|\zeta|^2 > T(z) T(z')\}$, with $h_b(m(\zeta) z'_b, z_b) = \zeta$ there.

By Witt's theorem, $M$ acts transitively on the vectors $z'_b$ of a given norm, and the value $\zeta = h_b(m z'_b, z_b)$ is a complete invariant of the double coset $U_z m U_{z'}$ in $M$ in the region $|\zeta|^2 > T(z) T(z')$. A section picks one element in each such double coset.

Put
$$v(j) = \prod_{i < j} \frac{(2\pi)^{i+1}}{i!},$$
the volume of $U(j)$ for the Haar measure of density $1$, and
$$\beta(x, \zeta) = \begin{cases} \omega(x)\, \bigl(|\zeta|^2 - T(z) T(z')\bigr)^{k-1} & \text{if } T(z) T(z') \le |\zeta|^2, \\ 0 & \text{otherwise.} \end{cases}$$

**Theorem 2.26.6 (The double coset measure on the big cell).** Let $k \ge 1$, let $z, z' \in W_b$ with $T(z), T(z') > 0$, and let $m(\zeta)$ be a section for $(z, z')$. Let $c, \kappa > 0$. Let $\mu_G$ be a Haar measure on $G$ with density $c$, and let $\mu_W$, $\mu_{W'}$ be Haar measures of total mass $1$ on $U_z$ and $U_{z'}$. Let $\nu$ be the image of the measure $\beta(x, \zeta)\, dx\, d\zeta$ on $\mathbb{C}^r \times \mathbb{C}$ under $(x, \zeta) \mapsto w(x, m(\zeta))$, and put
$$C = \frac{c\, 2^{r+1}\, v(k)^2}{v(k-1)\, (T(z) T(z'))^k\, \kappa^2}.$$
Then the map $(x, \zeta) \mapsto w(x, m(\zeta))$ is almost everywhere measurable for $\beta\, dx\, d\zeta$, and $C \nu$ together with the product measures $\mu_W \times \kappa\, dn$ on $U_z N$ and $\mu_{W'} \times \kappa\, dn$ on $U_{z'} N$ disintegrates $\mu_G$ on the regular set.

Lean: `GlobalTheory.DoubleCosetMeasure.isDis_bigCell` (also `GlobalTheory.T.besselDoubleCosetMeasure_bigCell_eq`, a second name).

*Proof.* Start from [Theorem 2.26.3](/entry/big-cell-integral/) with a Haar measure $\mu_b$ on $M$ of density $1$. It writes $\int f\, d\mu_G$ as an integral over $x$, $n$, $n'$ and $m \in M$. The two copies of $N$ match the two factors $\kappa\, dn$ of the product measures, at the cost of a factor $\kappa^{-2}$. For the integral over $M$ we use the rank one integration formula for $U(k, 1)$ with respect to the double cosets of the stabilizers $U_{z_b}$ and $U_{z'_b}$, which are compact groups isomorphic to $U(k)$: for $g \ge 0$ on $M$,
$$\int_M g\, d\mu_b = \frac{2\, v(k)^2}{v(k-1)\, (T(z) T(z'))^k} \int_{|\zeta|^2 > T T'} \bigl(|\zeta|^2 - T T'\bigr)^{k-1} \int\!\!\int g\bigl(u\, m(\zeta)\, u'\bigr)\, du\, du'\, d\zeta,$$
with $T T' = T(z) T(z')$ and $du$, $du'$ the probability Haar measures. The factor $v(k)^2 / v(k-1)$ is the ratio of the volumes of the two stabilizers and of their common subgroup, and $(|\zeta|^2 - T T')^{k-1}$ is the volume of the orbit of $U(k)$ through $m(\zeta) z'_b$. Insert this formula. The group $U_z$ normalizes $N$, and conjugation by an element of $U_z$ preserves the measure $dn$; the same holds for $U_{z'}$. So the factors $u$ and $u'$ can be moved to the outside, next to $n$ and $n'$, and the product measures on $U_z N$ and $U_{z'} N$ appear. The section is first replaced by a measurable section with the same values on the region $|\zeta|^2 > T T'$. This gives the disintegration with constant $C$. The image measure is carried by the regular set. The minors of $w(x, m(\zeta))$ are computed explicitly: the $D_l$ are nonzero when all $x_a$ are nonzero, and the Gram number is nonzero when $T T' < |\zeta|^2$. The remaining points have $\beta = 0$, so they carry no mass. Measurability holds because the section is smooth on the region where $\beta$ is positive. $\square$

**Remark 2.26.7 (Formalization).** The density condition `HasDens` ([UpperOff.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/UpperOff.lean#L113)) is the limit of $\mu(\exp B(\rho)) / \operatorname{vol}(B(\rho))$ as $\rho \to 0^+$, and $v(j)$ is `volUn` in the same file. The big cell element `bigCell` ([StatementBF.lean](lean:Formalism/FormalDegreeBessel/StatementBF.lean#L67)) is defined by its matrix entries, with $\bar x_a^{-1}$ in the last $r$ columns; for $x_a = 0$ it is not invertible, which is harmless since $\omega(x) = 0$ there. The section condition `IsSection` ([StatementRP.lean](lean:Formalism/FormalDegreeBessel/StatementRP.lean#L74)) asks also that $m(\zeta)$ preserve $H_b$. The rank one formula is `rank_one_unitary_integration_formula_exact_constant` ([RankOneUnitaryIntegrationFormulaExactConstantStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/RankOneUnitaryIntegrationFormulaExactConstantStatement.lean#L10)), stated for a Haar measure on $M$ of any density $c_b$ with the constant $2 c_b v(k)^2 / (v(k-1) (T T')^k)$, and with $u^{-1} m(\zeta) u'$ in place of $u\, m(\zeta)\, u'$. The explanation of the factor $v(k)^2 / v(k-1)$ and of the weight given in the last proof is classical background; the formal statement only asserts the formula. The proof of `bigCell_integral` ([LintegralBigCellHaarDensityConstant.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/LintegralBigCellHaarDensityConstant.lean#L303)) takes the constant $C$ from `iterated_integration_formula` and identifies it with `tendsto_measure_image_ball_div_volume` and `tendsto_ball_mean_bigCellWeight`.
