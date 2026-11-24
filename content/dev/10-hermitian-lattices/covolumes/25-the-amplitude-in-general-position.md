---
title: The amplitude in general position
decls:
  - GlobalTheory.Amp.FibreVolumeGen.fibre_volume
  - GlobalTheory.T.fibreVolume_twoFlags_generalPosition
  - GlobalTheory.Amp.AbsSide.abs_side
  - GlobalTheory.T.amplification_absolute_side_piece_bound
  - GlobalTheory.Amp.AbsConv.abs_core
  - GlobalTheory.T.amplitude_absolutelyConvergent_operatorNorm_le
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The amplitude in general position

Sections 6 and 7 bounded the amplitude of an element $\gamma$ at a real place when the two flags meet in a degenerate way, at a level $j \le r$. This section treats the case of general position: $j = r$, the last leading minor $D_r(\gamma)$ is nonzero, and the Gram number $|D_{r+1}|^2 - T(z) T(z') |D_r|^2$ is nonzero. Then the amplitude integral converges absolutely, and its operator norm is at most an explicit bound that decays like $|D_r(\gamma)|^{-(k-2-r)}$. The proof follows the same three steps as in the degenerate case: a fibre volume, a bound on the side pieces, and a dyadic sum. The difference is that the tail of the Bessel functions is now controlled by moments, and the size has no inverse lengths. The bound feeds the absolutely convergent part of the amplitude estimates in [the step](/step/nonempty-hyps/).

We keep the archimedean setting of [Section 2.6.8](/entry/fibre-normal-fibre-volume/): $n = 2r + k + 1$, $G = U(H)$, the flag unipotent group $N$ with Lebesgue measure $dn$, the vectors $z, z' \in W_b$ with $T(z), T(z') > 0$, the minors $D_l(\gamma)$, the lengths $\lambda_a(z, x)$ for $a \le r$, the Gram volume $Y_r(\gamma, x)$, minor bounds and normal-form stabilizer measures. We also keep the Bessel data on one side and the amplitude operator $J$ of [Section 2.7.6](/entry/deg-core/).

**Definition 2.25.1 (Upper size, general position, moment bound).** Let $x \in G$.

1. The *upper size* of $x$ is $S^+_z(x) = \max\bigl(1, \max_{a \le r} \lambda_a(z, x)\bigr)$.
2. The element $\gamma$ is in *general position* for $(z, z')$ if $z, z' \in W_b$, $T(z) > 0$, $T(z') > 0$, $\gamma \in G$, $D_r(\gamma) \ne 0$ and
$$|D_{r+1}(\gamma)|^2 - T(z) T(z')\, |D_r(\gamma)|^2 \ne 0.$$
3. Let $q \in \mathbb{N}$ and $H_1 > 0$. A function $\Phi$ has a *moment bound* of order $q$ and scale $H_1$ for $(z, \nu_S)$ if for every $a \le r$
$$\int \lambda_a(z, x)^{2q}\, \|\Phi(x)\|^2\, d\nu_S(x) \le H_1^{2q} \int \|\Phi\|^2\, d\nu_S.$$
4. For $R_0, y > 0$ the *upper fibre set* $E^+(\gamma; R_0, y)$ is the set of $x \in G$ with $S^+_{z'}(x) \le R_0$, $S^+_z(\gamma x) \le R_0$ and $y < Y_r(\gamma, x) \le 2y$.

By Chebyshev's inequality, a moment bound gives a tail bound: the mass of $\Phi$ where $\lambda_a > \lambda H_1$ is at most $\lambda^{-2q}$ times the total mass. For $k \ge r + 3$ and $R_0, D_e, y > 0$ put
$$\begin{aligned} V^+(R_0, D_e, y) = {} & (4r)^{11 r^2}\, R_0^{20 r^3}\, D_e^{12 r^2} \\ & \cdot \Bigl(\frac{\pi e}{k - 2 - r}\Bigr)^{r(k-2-r)} (2y)^{2(k-2-r)}, \end{aligned}$$
and for $H_1, D_e, D > 0$
$$\begin{aligned} A(H_1, D_e, D) = {} & (4r)^{44 r^3}\, H_1^{24 r^3}\, D_e^{14 r^2} \\ & \cdot \Bigl(\frac{8 \pi e}{k}\Bigr)^{r(k-2-r)} D^{-(k-2-r)}. \end{aligned}$$

**Theorem 2.25.2 (Fibre volume in general position).** Let $1 \le r$ and $2r + 6 \le k$. Let $\gamma$ be in general position for $(z, z')$, let $D_e$ be a minor bound for $\gamma$, let $s > 0$, and let $\mu_R$ be a normal-form stabilizer measure for $\gamma$ with scale $s$. Let $g_1 \in G$. Then:

1. the set of $n \in N$ with $Y_r(\gamma, n g_1) = 0$ has $dn$-measure $0$;
2. for every cutoff $\varphi$ for $(G, \mu_R)$ and all $R_0 \ge 1$, $y > 0$,
$$\int_N \varphi(n g_1)\, \mathbf{1}_{E^+(\gamma; R_0, y)}(n g_1)\, dn \le \frac{V^+(R_0, D_e, y)}{s}.$$

Lean: `GlobalTheory.Amp.FibreVolumeGen.fibre_volume` (also `GlobalTheory.T.fibreVolume_twoFlags_generalPosition`, a second name).

*Proof.* Write $\gamma = n_1 g_0 n_2$ with $g_0$ normal and $\mu_R$ the image of $s \mu^0_\beta$ under conjugation by $n_2^{-1}$. The Gram volume, the sizes and the fibre set are compatible with this factorization: left translation by $n_1$ does not change $S^+_z$, and the substitution $x \mapsto n_2 x$ carries $E^+(\gamma; R_0, y)$ to the fibre set of $g_0$ and $\varphi$ to a cutoff for $(G, s\mu^0_\beta)$. The measure $dn$ is invariant under left translation by $n_2$. Next write $g_1 = n' t k_1$ by the Iwasawa decomposition, with $t$ in the torus and Levi part and $k_1$ in the maximal compact subgroup; the lengths $\lambda_a$ are unchanged by $k_1$ on the right. So both claims reduce to the normal element $g_0$ and an element $t$, and the factor $1/s$ comes from the scale of $\mu_R$. For a normal element with $j = r$ we use the normal case, which is the general position form of [Theorem 2.6.8](/entry/fibre-normal-fibre-volume/): the set of $n$ with $Y_r(g_0, n t) = 0$ is null, and the cutoff integral over the upper fibre set is at most $V^+(R_0, D_e, y)$. The constant $(\pi e/(k-2-r))^{r(k-2-r)}$ is a bound for the volume of a ball of dimension $2r(k - 2 - r)$, and $(2y)^{2(k-2-r)}$ comes from the condition $Y_r \le 2y$ in each of the $k - 2 - r$ free directions. $\square$

**Theorem 2.25.3 (Side pieces in general position).** Let $1 \le r$, $2r + 6 \le k$, $\kappa > 0$, $s > 0$, $H_1 \ge 1$ and $q \in \mathbb{N}$. Let $\Phi'$ be a Bessel function for $z'$, with Haar measure $\kappa\, dn$ on $N$, constant $c$ and quotient measure $\nu_S'$, and with a moment bound of order $q$ and scale $H_1$. Let $\gamma$ be in general position for $(z, z')$, let $D_e$ be a minor bound for $\gamma$, let $\mu_R$ be a normal-form stabilizer measure with scale $s$, and let $\nu_R$ be the quotient measure of $\mu_G$ by $\mu_R$. Then:

1. the set of $x$ that are not in $G$ or have $Y_r(\gamma, x) = 0$ is $\nu_R$-null;
2. for every unit vector $w \in W_q$, every $i \in \mathbb{N}$ and all $R_0 \ge 1$, $y > 0$,
$$\int_{Q_i} |\langle w, \Phi'(x) \rangle|^2\, d\nu_R(x) \le \frac{\kappa}{s}\, V^+(R_0, D_e, y)\, \frac{(r+1)\, 4^q}{2^{2iq}}\, c,$$
where $Q_i$ is the set of $x \in E^+(\gamma; R_0, y)$ such that $i = 0$ or $2^i H_1 / 2 < S^+_{z'}(x)$.

Lean: `GlobalTheory.Amp.AbsSide.abs_side` (also `GlobalTheory.T.amplification_absolute_side_piece_bound`, a second name).

*Proof.* Unfold $\mu_G$ in two ways. As $\nu_R$ is the quotient of $\mu_G$ by $\mu_R$, a cutoff $\varphi$ for $(G, \mu_R)$ turns a $\nu_R$-integral into a $\mu_G$-integral:
$$\int f\, d\nu_R \le \int \varphi\, f\, d\mu_G$$
for functions $f \ge 0$ that are left $\mu_R$-invariant. Then unfold $\mu_G$ along $U_{z'} N$: the $\mu_G$-integral is a $\nu_S'$-integral of an integral over $U_{z'} \times N$ for $\mu_{W'} \times \kappa\, dn$. On the $N$ part, the factor $\varphi \cdot \mathbf{1}_{Q_i}$ is bounded by the last Theorem, which gives $\kappa\, V^+/s$. The null set of claim 1 is null for $\nu_R$ for the same reason, by claim 1 of the last Theorem. On the $U_{z'}$ part, $|\langle w, \Phi'(u x)\rangle|^2 = |\langle \pi'(u)^{-1} w, \Phi'(x)\rangle|^2$, and the Schur orthogonality relations for the irreducible representation $\pi'$ on the probability space $U_{z'}$ give
$$\int_{U_{z'}} |\langle w, \pi'(u) v\rangle|^2\, d\mu_{W'}(u) = \frac{\|v\|^2}{\dim W_q}.$$
On the $\nu_S'$ part, the condition $2^i H_1/2 < S^+_{z'}(x)$ with $i \ge 1$ means that $\lambda_a(z', x) > 2^{i-1} H_1$ for some $a \le r$. So
$$\mathbf{1}_{Q_i}(x) \le \sum_{a \le r} \Bigl(\frac{\lambda_a(z', x)}{2^{i-1} H_1}\Bigr)^{2q},$$
and for $i = 0$ the same bound holds with the factor $1 \le (r+1)4^q$. The moment bound gives at most $(r+1)\, 4^q\, 2^{-2iq} \int \|\Phi'\|^2\, d\nu_S'$, and $\int \|\Phi'\|^2\, d\nu_S' = c \dim W_q$. The dimensions cancel. $\square$

**Theorem 2.25.4 (Absolute convergence of the amplitude).** Let $1 \le r$, $2r + 6 \le k$, $\kappa > 0$, $s > 0$ and $H_1 \ge 1$. Let $\Phi$ and $\Phi'$ be Bessel functions for $z$ and for $z'$, both with Haar measure $\kappa\, dn$ on $N$ and constant $c$, with quotient measures $\nu_S$ and $\nu_S'$, and both with a moment bound of order $q = 24 r^3 + 1$ and scale $H_1$. Let $\gamma$ be in general position for $(z, z')$, let $D_e$ be a minor bound for $\gamma$, let $\mu_R$ be a normal-form stabilizer measure for $\gamma$ with scale $s$, and let $\nu_R$ be the quotient measure of $\mu_G$ by $\mu_R$. Then the function $x \mapsto \langle \Phi'(x), \cdot\, \rangle\, \Phi(\gamma x)$ is $\nu_R$-integrable, and
$$\|J\| \le \frac{\kappa}{s}\, A\bigl(H_1, D_e, |D_r(\gamma)|\bigr).$$

Lean: `GlobalTheory.Amp.AbsConv.abs_core` (also `GlobalTheory.T.amplitude_absolutelyConvergent_operatorNorm_le`, a second name).

*Proof.* Fix unit vectors $w \in W_q$ and $v \in W_p$. We bound $\int |\langle w, \Phi'(x)\rangle|\, |\langle v, \Phi(\gamma x)\rangle|\, d\nu_R(x)$. Away from a $\nu_R$-null set, $x \in G$ and $Y_r(\gamma, x) > 0$. Cut the rest into dyadic pieces: for $i, i' \ge 0$ the piece where $S^+_{z'}(x)$ and $S^+_z(\gamma x)$ lie in the dyadic ranges of $2^i H_1$ and $2^{i'} H_1$, and for each $l \in \mathbb{Z}$ the range $y_l < Y_r \le 2 y_l$ with $y_l = 2^l$. The Gram volume is a projected volume of $r$ vectors whose lengths are bounded in terms of $R_0$, divided by $|D_r(\gamma)|$; so on a piece with given $R_0$ only the $l$ with $y_l$ at most a power of $R_0$ times $|D_r(\gamma)|^{-1}$ occur. On each piece apply the Cauchy-Schwarz inequality and the last Theorem to both sides, once for $\Phi'$ and once, with the roles of $z$ and $z'$ exchanged, for $\Phi$ at $\gamma x$. This gives a bound
$$\frac{\kappa}{s}\, c\, V^+(R_0, D_e, y_l)\, (r+1)\, 4^q\, 2^{-(i + i') q},$$
with $R_0 = 2^{\max(i, i')} H_1$. The factor $R_0^{20 r^3}$ of $V^+$ is beaten by $2^{-(i+i')q}$ since $q = 24 r^3 + 1$, so the sum over $i, i'$ converges. The factor $(2y_l)^{2(k-2-r)}$ makes the sum over $l$ a geometric series dominated by its largest term, which is a power of $R_0$ times $|D_r(\gamma)|^{-2(k-2-r)}$; the square root from Cauchy-Schwarz turns this into $|D_r(\gamma)|^{-(k-2-r)}$. Since $2r + 6 \le k$ gives $k - 2 - r \ge k/2$, we have $\pi e/(k - 2 - r) \le 8 \pi e / k$. Collecting the constants gives the bound $A(H_1, D_e, |D_r(\gamma)|)$ for the integral, and the factor $c^{-1}$ in $J$ cancels $c$. The integrability follows from the same bound. $\square$

**Remark 2.25.5.** The bound $A$ decays in $|D_r(\gamma)|$ with exponent $k - 2 - r$, which is large when $k \ge 2r + 6$. In the degenerate case of [Section 2.7.6](/entry/deg-core/) the decay is in the last nonzero minor $D_j(\gamma)$ and is weaker.

**Remark 2.25.6 (Formalization).** The size `Sg` ([UpperOff.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/UpperOff.lean#L90)) is $\max(1, \max_a \lambda_a)$, without the inverse lengths of the size of Section 6; this is why the moment bound `MomBd` ([BlockAnti.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/BlockAnti.lean#L38)) asks only for positive moments. The threshold in the side pieces is $2^i H_1/2$, not $2^i H_1$ as in Section 7. The order is fixed at $q = 24 r^3 + 1$ in `abs_core`. In `fibVol` the integer $k - 2 - r$ is a natural number subtraction, which is harmless under $2r + 6 \le k$. The general position condition is `TwoFl` and the minor bound is `DeOK`. The second names are wrappers of the form `first | exact @X | exact X | ...`. The proof of the fibre volume cites the normal case `fibre_gramNumber_null_and_cutoff_integral_bound`, which is not unfolded here; the account of the dyadic sum above follows the shape of the constants. In [AmplitudeAbsolutelyConvergentOperatorNormLe.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/AmplitudeAbsolutelyConvergentOperatorNormLe.lean#L85) the extension by zero `ext0` has a lemma named `cochainExtendByZeroSubgroup_of_mem` (line 87), a name unrelated to its content. The Iwasawa step is `Amp.Iwa.iwasawa`.
