---
title: Orbit interpolation at a free ball
decls:
  - GlobalTheory.T.orbitInterpolation_detWeight_freeBall_indefinite
  - GlobalTheory.OrbitInterpWeight.orbit_interp_deMul
  - GlobalTheory.T.freeBallCentre_interpolation_detWeight_smallSignature
  - GlobalTheory.Up.OrbitInterpSmall.orbit_interp_small
  - GlobalTheory.Up.OrbitInterpSmall.orbitInterp_small
  - GlobalTheory.Up.OrbitInterpSmall.sum_bound
  - GlobalTheory.T.exists_uniform_bound_lintegral_flagDomain_ball_case
  - GlobalTheory.IntBall.intBall
  - GlobalTheory.IntBall.lintegral_lt_top
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Orbit interpolation at a free ball

This section proves the orbit interpolation used by [the interpolation on one component](/entry/comp-interp/) of section 11, in the indefinite case. A cusp form is built that is nonzero at the centre of a free ball and zero at every translate of the centre by the larger group. The large signatures come from the general orbit interpolation. The small signatures, with $p_0 (r - p_0) \leq 3$, need a separate bound for the orbit sum of the potential, and this bound reduces to an integral over a ball.

We keep the notation of section 11: the datum $X$ of rank $r$ over the CM field $E$ with CM type $\Psi$, the frames, the domain, the cusp forms $SS(\lambda)$, the determinant weight $\nabla(s)$, the function $\mathrm{rh}(x_0, x)$ and the free balls. Put $\dim X = |\Psi|\, p_0 (r - p_0)$, the complex dimension of the flag domain.

### The indefinite case

**Theorem 7.12.1 (Orbit interpolation in the indefinite case).** Let $X$ be a datum of rank $r$ over $E$ with $\chi = 1$ on $\Gamma$ and $0 < p_0 < r$. Let $x_0$ be an orthonormal frame and let $(G, x_0)$ be a free ball of radius $1/(49 r^2)$. Let $s$ be even with
$$s \geq 2r + 50 r^2 \dim X + 1.$$
Then there is $P \in SS(\nabla(s))$ with $P(x_0) \neq 0$ and $P(\gamma x_0) = 0$ for every $\gamma \in G$ with $\gamma \notin \Gamma$.

Lean: `GlobalTheory.T.orbitInterpolation_detWeight_freeBall_indefinite` (also `GlobalTheory.OrbitInterpWeight.orbit_interp_deMul`).

*Proof.* There are two cases.

1. Assume $p_0 (r - p_0) \geq 4$. The weight $\nabla(s)$ is constant on the blocks of the signature. Its gaps satisfy the pairing condition with margin $s - 2r + 2$ against the canonical weight: consecutive places in one block have equal entries, and the step across the blocks is $s$, which exceeds the step of the canonical weight by $s - 2r + 2$. So the Levi form of the weight of $\nabla(s)$, minus the Levi form of the density, is at least $(s - 2r + 2)$ times the Levi form of $\mathrm{rh}(x_0, \cdot)$ on the chart at $x_0$.
2. In case 1 the general orbit interpolation applies with the parameters

$$\begin{aligned} b &= 4 |\Psi| r^2 + 1, \\ m &= s - 2r + 2. \end{aligned}$$

Its condition $b + \dim X / \rho_0 < m$ with $\rho_0 = 1/(49 r^2)$ reads $4 |\Psi| r^2 + 1 + 49 r^2 \dim X < s - 2r + 2$. This holds, since $s \geq 2r + 50 r^2 \dim X + 1$ and $\dim X \geq 4 |\Psi|$. Bounded sections of weight $\nabla(s)$ are cusp forms, by the cusp criterion for block constant weights with a positive step. So the general orbit interpolation gives $P$.
3. Assume $p_0 (r - p_0) \leq 3$. Then [the interpolation in small signature](/entry/free-ball-centre-interpolation-det-weight-small-signature/) gives $P$.

This proves the theorem. $\square$

### Small signature

**Theorem 7.12.2 (Interpolation in small signature).** Let $X$, $x_0$, $G$ and $s$ be as in the previous theorem, and assume $p_0 (r - p_0) \leq 3$. Then there is $P \in SS(\nabla(s))$ with $P(x_0) \neq 0$ and $P(\gamma x_0) = 0$ for every $\gamma \in G \setminus \Gamma$.

Lean: `GlobalTheory.T.freeBallCentre_interpolation_detWeight_smallSignature` (also `GlobalTheory.Up.OrbitInterpSmall.orbit_interp_small`).

*Proof.* We have $\dim X \geq 1$, since $0 < p_0 < r$ and $\Psi$ is not empty. Apply [the interpolation with a weight bound](/entry/global-theory-up-orbit-interp-small-orbit-interp-small/) with $\lambda = \nabla(s)$, $\rho_0 = 1/(49 r^2)$ and

$$\begin{aligned} b &= 4(r - 1) + \tfrac{1}{2}, \\ m &= s - 2r + 2. \end{aligned}$$

Then $4(r - 1) \leq b$ and $b > 0$. The condition $b + \dim X/\rho_0 < m$ reads $4r - \tfrac{7}{2} + 49 r^2 \dim X < s - 2r + 2$, which follows from the bound on $s$. The curvature inequality comes from the gaps of $\nabla(s)$, as in step 1 of the previous proof. Bounded sections of weight $\nabla(s)$ are cusp forms. $\square$

The hypothesis $\chi = 1$ is not used in this proof. Only $|\chi| = 1$ enters, through the norm of the Poincaré series terms.

**Lemma 7.12.3 (Interpolation with a weight bound).** Let $X$ be a datum with $0 < p_0 < r$, $p_0 (r - p_0) \leq 3$ and a properly discontinuous action of $\Gamma$. Let $x_0$ be orthonormal and let $(G, x_0)$ be a free ball of radius $\rho_0 > 0$. Let $\lambda$ be a block constant weight, and let $b, m$ be real with

$$\begin{aligned} 4(r - 1) &\leq b, \quad 0 < b, \\ b + \dim X/\rho_0 &< m. \end{aligned}$$

Assume that on the chart at $x_0$ the Levi form of the weight of $\lambda$, minus the Levi form of the density, is at least $m$ times the Levi form of $\mathrm{rh}(x_0, \cdot)$. Assume that bounded sections of weight $\lambda$ are cusp forms. Then there is $u_0 \in SS(\lambda)$ with $u_0(x_0) = 1$ and $u_0(\gamma x_0) = 0$ for every $\gamma \in G \setminus \Gamma$.

Lean: `GlobalTheory.Up.OrbitInterpSmall.orbitInterp_small`.

*Proof.* We take the steps in order.

1. There is a measurable cutoff $\kappa$ on frames with $0 < \kappa \leq 1$ on the domain, invariant under the Borel group, equal to the model cutoff of exponent $b$ on the chart at $x_0$. The sums $\sum_{\gamma \in \Gamma} \kappa(\gamma x)$ are bounded by a finite constant $C_s$ on the domain.
2. [The orbit sum bound](/entry/sum-bound/) at exponent $b/2$ applies, since $b/2 \geq 2(r - 1)$.
3. Let $\eta > 0$ and put $\eta' = \eta / (C_s + 1)$. The solution of the $\bar\partial$ equation with a pole at $x_0$, in $L^2$ with the singular weight of exponent $m$, gives a smooth section $F$ and a holomorphic section $P$ with $|P(x_0) - 1| \leq \eta'$ and $|P(\gamma x_0)| \leq \eta'$ for every $\gamma \in G$ with $\gamma \neq 1$. The free ball property keeps the pole of $\gamma x_0$ outside the support of the cutoff at $x_0$.
4. The Poincaré series

$$\mathrm{poin}(P)(x) = \sum_{\gamma \in \Gamma} \chi(\gamma)^{-1} P(\gamma x)$$

converges and is a bounded section of weight $\lambda$, so it lies in $SS(\lambda)$. At $x_0$ its term at $\gamma = 1$ is $P(x_0)$, and the other terms have norm at most $\eta'$ times $\kappa$. So $|\mathrm{poin}(P)(x_0) - 1| \leq \eta' + \eta' C_s = \eta$. In the same way $|\mathrm{poin}(P)(\sigma^{-1} x_0)| \leq \eta$ for each $\sigma$ with $\sigma^{-1} \in G \setminus \Gamma$.
5. The group $\Gamma$ has finite index in the unitary stabiliser of the lattice, with a finite set $T$ of coset representatives. The points $\sigma^{-1} x_0$ with $\sigma \in T$ and $\sigma^{-1} \in G \setminus \Gamma$ are finite in number. The space $SS(\lambda)$ is a complex vector space. Approximate solutions for all $\eta > 0$ give an exact solution $u_0 \in SS(\lambda)$ of the finite linear problem with value $1$ at $x_0$ and $0$ at these points.
6. Let $\gamma \in G \setminus \Gamma$. Write $\gamma^{-1} = \sigma \delta$ with $\sigma \in T$ and $\delta \in \Gamma$. Then $\sigma^{-1} = \delta \gamma \in G$ and $\sigma^{-1} \notin \Gamma$. Since $\gamma = \delta^{-1} \sigma^{-1}$, we get $u_0(\gamma x_0) = \chi(\delta^{-1})\, u_0(\sigma^{-1} x_0) = 0$.

This proves the lemma. $\square$

### The orbit sum of the potential

**Lemma 7.12.4 (Orbit sum bound).** Let $X$ be a datum with $0 < p_0 < r$, $p_0 (r - p_0) \leq 3$ and a properly discontinuous action of $\Gamma$. Let $x_0$ be orthonormal and let $s \geq 2(r - 1)$. Then there is a finite constant $C$ such that for every orthonormal frame $x$,

$$\sum_{\gamma \in \Gamma} \exp\bigl(-s\, \mathrm{rh}(x_0, \gamma x)\bigr) \leq C.$$

Lean: `GlobalTheory.Up.OrbitInterpSmall.sum_bound`.

*Proof.* We have $s \geq 2(r - 1) \geq 2$, since $r \geq 2$. The uniform bound for orbit sums of the potential reduces the claim to a uniform bound, over orthonormal base frames $x_1$, for the integral of $\exp(-s\, \mathrm{rh})$ on the chart at $x_1$. [The integral over the ball](/entry/exists-uniform-bound-lintegral-flag-domain-ball-case/) gives this bound. $\square$

**Theorem 7.12.5 (Integral over the ball).** Let $X$ be a datum with $0 < p_0 < r$ and $p_0 (r - p_0) \leq 3$, and let $s \geq 2(r - 1)$. Then there is a finite constant $I$ such that for every orthonormal frame $x_1$,

$$\int \exp\bigl(-s\, \mathrm{rh}_{x_1}(z)\bigr)\, d\mu_{x_1}(z) \leq I,$$

where $\mathrm{rh}_{x_1}$ and $\mu_{x_1}$ are the potential and the invariant measure on the chart at $x_1$.

Lean: `GlobalTheory.T.exists_uniform_bound_lintegral_flagDomain_ball_case` (also `GlobalTheory.IntBall.intBall`).

*Proof.* Let $x^{\ast}$ be the standard orthonormal frame. The potential and the measure on the chart at an orthonormal frame $x_1$ are the images of those at $x^{\ast}$ under a unitary change of chart. So the integral at $x_1$ is equal to the integral at $x^{\ast}$. Take $I$ to be this integral, which is finite by [the finiteness on the ball](/entry/lintegral-lt-top/). $\square$

**Lemma 7.12.6 (Finiteness on the ball).** In the setting of the previous theorem, the integral of $\exp(-s\, \mathrm{rh})$ on the chart at an orthonormal base frame is finite.

Lean: `GlobalTheory.IntBall.lintegral_lt_top`.

*Proof.* We take the steps in order.

1. From $0 < p_0 < r$ and $p_0 (r - p_0) \leq 3$ we get $p_0 = 1$ or $p_0 + 1 = r$. So each factor of the domain is a complex ball, of dimension at most $3$.
2. On the chart $Z = (Z_\tau)$ of the unit ball domain $\Omega$, the integral is

$$\int_{\Omega} \delta(Z)\, e^{-s \rho(Z)}\, dZ, \qquad \rho(Z) = -\sum_{\tau} \log \det(1 - Z_\tau^{\ast} Z_\tau),$$

where the density $\delta(Z)$ is the product of the inverse squares $|d_i|^{-2}$ of the leading Gram minors.
3. Each Gram minor is at least $t$ times a cutoff factor $g_i$, where $t = e^{-\rho} \in (0, 1]$. For $s \geq 2q$, with $q$ the number of minors, we get

$$\Bigl(\prod_i d_i^{-2}\Bigr) t^{s} \leq \prod_i g_i^{-2}.$$

Here $q \leq r - 1$, so $s \geq 2(r - 1)$ suffices. So the integrand is at most a product over $\tau$ of a cutoff bound $h(Z_\tau)$ for the block.
4. The integral of the product over the chart coordinates is the product of the integrals over $\tau$.
5. The cases $p_0 \in \{1, 2, 3\}$ with $r - p_0 - 1 \leq 2$ and $p_0 (r - p_0) \leq 3$ leave the blocks of rank $2$, $3$ and $4$. For each of them the integral of $h$ is finite by a direct computation.

So the integral is finite. $\square$

**Remark 7.12.7 (Formalization).** The indefinite theorem `T.orbitInterpolation_detWeight_freeBall_indefinite`, the small signature theorem `T.freeBallCentre_interpolation_detWeight_smallSignature` and the integral `T.exists_uniform_bound_lintegral_flagDomain_ball_case` are `first | exact` wrappers under `maxHeartbeats 1000000`. The case split `orbit_interp_deMul` is at line 89 of [OrbitInterpolationDetWeightFreeBallIndefinite.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/OrbitInterpolationDetWeightFreeBallIndefinite.lean#L89). The large case `large` at line 47 has no hypothesis on $\chi$; the gap pairing is `gapsPairing_deMul` at line 28 and the block constancy is `blockConst_deMul` at line 25. In [FreeBallCentreInterpolationDetWeightSmallSignatu.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/FreeBallCentreInterpolationDetWeightSmallSignatu.lean#L160) the proof `orbit_interp_small` at line 160 binds the $\chi$ hypothesis to `_`. The lemma `orbitInterp_small` is at line 61, with the cutoff `kappa_exists` at line 40 and `sum_bound` at line 33. The lemma `gapsPairing_deMul'` at line 140 repeats `gapsPairing_deMul`. The ball integral is `intBall` at line 136 of [ExistsUniformBoundLintegralFlagDomainBallCase.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsUniformBoundLintegralFlagDomainBallCase.lean#L136), with `lintegral_lt_top` at line 119, `ball_cases` at line 58, `density_mul_exp_le` at line 75, `prod_inv_sq_mul_rpow_le` at line 26 and the case check `block_fin` at line 106, which runs `interval_cases` over $p_0$ and the corank.
