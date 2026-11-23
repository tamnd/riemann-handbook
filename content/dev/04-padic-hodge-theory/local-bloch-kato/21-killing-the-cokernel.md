---
title: Killing the cokernel by a power of the prime
decls:
  - GlobalTheory.CokerL.kills_cokerL
  - GlobalTheory.T.breuilKisin_pow_kills_lattice_cokernel
  - GlobalTheory.Proof.cokernel_latticeMap_killed_by_prime_pow.main
  - GlobalTheory.T.cokernel_latticeMap_killed_by_prime_pow
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Killing the cokernel by a power of the prime

Let $F : D_1 \to D_2$ be a map of Breuil-Kisin data whose cokernel has finite length. A module of finite length over $\mathfrak{S}_{\mathcal{O}}$ is killed by some power $\ell^m$, but $m$ depends on $F$. This section proves that the explicit power $\ell^{\rho}$, with $\rho = 2(N - 1) r(\Sigma)$, already kills the cokernel of $F$ on six lattices, when the tame characters of $D_1$ and $D_2$ lie in $\Sigma$ and the numerical conditions hold. The proof splits a vector into isotypic parts for the descent datum and uses the monodromy operator $N$ on each part. The result is used in the proof of [the lifting theorem for $\varphi$-modules](/entry/lifting-theorem-phi-modules-exact-triple/).

We keep the notation of [the section on lifting](/entry/lift-f-of-is-good/): $\ell$ is a prime, $e + 1 = \ell^a$, $L$ is a finite extension of $\mathbb{Q}_\ell$ with tame descent data, $E = X^e + \ell$, and $N = X \nabla_P$ is the monodromy operator of a $\varphi$-module $P$. The numerical conditions for $(\ell, e, N, \eta, H, \Sigma, U)$ and the period $r = r(\Sigma)$ are as in that section. Put $\rho = 2(N - 1) r$. A *map of Breuil-Kisin data* $F : D_1 \to D_2$ is a map of the $\varphi$-modules, in the sense of [the previous section](/entry/is-exact-triple-of-is-seslat-gen/), that commutes with the descent data. Its cokernel is the cokernel on the lattices $M$.

**Definition 7.21.1 (Killing a cokernel).** Let $F : V_1 \to V_2$ be a map of abelian groups, $W_i \subseteq V_i$ subsets, and $n \ge 1$. The integer $n$ *kills the cokernel* of $F$ from $W_1$ to $W_2$ if for every $y \in W_2$ there is $x \in W_1$ with $F x = n y$.

If $F(W_1) \subseteq W_2$ and the $W_i$ are subgroups, this says that $n$ kills $W_2 / F(W_1)$. On the lattices $M$ it says that $n$ kills the cokernel of $F$.

**Definition 7.21.2 (Six lattices).** Let $D$ be a Breuil-Kisin datum of heights $(\eta, H)$, with $\varphi$-module $P$ and descent datum $\Delta$. Put:

1. $\varphi^* M$, the image lattice, and $M$, the lattice;
2. $M_\eta = \{ y : E^\eta y \in M \}$;
3. $M^\Delta$, the vectors of $M$ fixed by $\Delta$;
4. $Y_\eta = (M_\eta)^\Delta$, the vectors of $M_\eta$ fixed by $\Delta$;
5. $Y'_\eta = X^e\, Y_\eta$.

The lifting theorem of the next section works with $Y'_\eta$ and $M^\Delta$.

The inertia subgroup of the tame Galois group contains a copy of the group $\mu_e$ of $e$-th roots of unity in $L$. For $\zeta \in \mu_e$ and $\tau \in \mathbb{Z}/a$ let $\zeta_\tau \in \mu_e$ be the root by which the inertia element $\zeta$ scales $X$ at the place $\tau$. For $c \in \mathbb{Z}/e$, the *$c$-isotypic part* of the vectors is the set of $v$ with $(\Delta(\zeta) v)_\tau = \zeta_\tau^{c} v_\tau$ for all $\zeta$ and $\tau$. The *isotypic projector* is
$$\pi_c(v)_\tau = \frac{1}{e} \sum_{\zeta \in \mu_e} \zeta_\tau^{-c}\, \big(\Delta(\zeta) v\big)_\tau.$$
It maps into the $c$-isotypic part, the sum of all $\pi_c$ is the identity, it preserves $\varphi^* M$, and it commutes with multiplication by $X^e$ and with maps of Breuil-Kisin data. The order $e$ of $\mu_e$ is prime to $\ell$, so $1/e \in \mathbb{Z}_\ell$.

Heuristically, a vector $X^i d$, with $d$ constant of character $c'$, lies in the $c$-isotypic part when $i \equiv c - c' \pmod e$, and $N(X^i d) = i X^i d$ up to terms of higher degree. This is why the degrees below control $N$ on an isotypic part.

**Definition 7.21.3 (Degrees and polynomials).** For $\Sigma \subseteq \mathbb{Z}/e$, $c \in \mathbb{Z}/e$ and $m \le m'$ let
$$\deg(\Sigma, c, m, m') = \{ \overline{c - c'} + n e : c' \in \Sigma,\ m \le n < m' \} \subseteq \mathbb{N},$$
where $\overline{x} \in [0, e)$ is the representative of $x$. For $A' \ge 1$ put
$$P_1 = \prod_{i \in \deg(\Sigma, c, 0, A')} (X - i), \qquad P_2 = \prod_{i \in \deg(\Sigma, c, A', 2A')} (X - i).$$

**Definition 7.21.4 (High part).** Let $\mathcal{S}^{\mathrm{high}}$ be the ideal of the series in $\mathcal{S}$ that are divisible by $X^{\ell e}$ in $L[[X]]$, and $\mathcal{M}^{\mathrm{high}} = \mathcal{S}^{\mathrm{high}} \mathcal{M}$. For a map $F : D_1 \to D_2$ and $A', b \ge 0$ put
$$T(A', b) = X^{e A'} F(\varphi^* M_1) + \ell^b\, \varphi^* M_2 + \mathcal{M}_2^{\mathrm{high}}.$$

We take the following results as given.

1. *Numerics.* Under the numerical conditions, $1 \le r$ and $4 r \le N^2$; and if $4r \le N^2$ with the other numerical conditions, then $2(H + \eta + 2(N - 1) r + 1) + 2 < \ell$.
2. *Lagrange.* If $|\Sigma| \le N$ and $2A' + 2 < \ell$, there are $\alpha, \beta \in \mathbb{Z}_\ell[X]$ with $\ell^{\rho} = \alpha P_1 + \beta P_2$.
3. *Image up to $\ell^b$.* If the cokernel of $F$ has finite length, $1 \le b$ and $H + \eta + b \le \ell$, then for every $x \in \varphi^* M_2$ there are $y \in \varphi^* M_1$ and $z \in \varphi^* M_2$ with $X^{e(H + \eta + b)} x = F y + \ell^b z$.
4. *Reduction.* For every Breuil-Kisin datum: $N$ preserves $\mathcal{M}$; $\mathcal{M} = \varphi^* M + \mathcal{M}^{\mathrm{high}}$; and $\varphi^* M \cap \mathcal{M}^{\mathrm{high}} = X^{e\ell}\, \varphi^* M$. For every map $F$, $N$ preserves $T(A', b)$.
5. *Degrees.* Let $2A' \le \ell$, and let the characters of $D$ lie in $\Sigma$. Then $P_1(N)$ maps the $c$-isotypic part of $\varphi^* M$ into $X^{eA'} \varphi^* M + \mathcal{M}^{\mathrm{high}}$, and $P_2(N)$ maps the $c$-isotypic part of $X^{eA'} \varphi^* M$ into $X^{2eA'} \varphi^* M + \mathcal{M}^{\mathrm{high}}$.
6. *Division by $X$.* If $w, z \in \varphi^* M$ and $X^{en} w = \ell^b z$, then $w = \ell^b z'$ with $z' \in \varphi^* M$.
7. *Finite length.* An $\mathfrak{S}_{\mathcal{O}}$-module of finite length is killed by some $\ell^m$.
8. *From $\varphi^* M$ to all six.* If $\ell^s$ kills the cokernel of $F$ from $\varphi^* M_1$ to $\varphi^* M_2$, then $\ell^s$ kills the cokernel of $F$ on each of the six lattices.

Part 1 is elementary arithmetic. Part 7 holds because $\ell$ lies in the maximal ideal of $\mathfrak{S}_{\mathcal{O}}$, and a module of finite length over a local ring is killed by a power of the maximal ideal.

**Lemma 7.21.5 (Isotypic step).** Assume the numerical conditions, that the characters of $D_1$ and $D_2$ lie in $\Sigma$, and that the cokernel of $F$ has finite length. Put $b = \rho + 1$ and $A' = H + \eta + b$. Then for every $c \in \mathbb{Z}/e$ and $x \in \varphi^* M_2$,
$$\ell^{\rho}\, \pi_c\big(X^{eA'} x\big) \in T(A', b).$$

*Proof.* By part 1, $2A' + 2 < \ell$. So part 2 gives $\alpha, \beta$, and part 5 applies. Put $y = \pi_c(X^{eA'} x)$. Then
$$\ell^\rho y = \alpha(N)\, P_1(N) y + \beta(N)\, P_2(N) y.$$
The coefficients of $\alpha$ and $\beta$ lie in $\mathbb{Z}_\ell \subseteq \mathcal{O}$, and $N$ preserves $T = T(A', b)$ by part 4. So it is enough to show $P_1(N) y \in T$ and $P_2(N) y \in T$.

*$P_1$.* By part 3, $X^{eA'} x = F y_0 + \ell^b z_0$ with $y_0 \in \varphi^* M_1$, $z_0 \in \varphi^* M_2$. Apply $\pi_c$, which commutes with $F$:
$$y = F \pi_c(y_0) + \ell^b \pi_c(z_0).$$
Since $F$ commutes with $N$, $P_1(N) F \pi_c(y_0) = F P_1(N) \pi_c(y_0)$. By part 5 for $D_1$, $P_1(N) \pi_c(y_0) \in X^{eA'} \varphi^* M_1 + \mathcal{M}_1^{\mathrm{high}}$, and $F$ maps $\mathcal{M}_1^{\mathrm{high}}$ into $\mathcal{M}_2^{\mathrm{high}}$. So the first term lies in $T$. Next, $\pi_c(z_0) \in \varphi^* M_2 \subseteq \mathcal{M}_2$. The polynomial $P_1$ has integer coefficients and $N$ preserves $\mathcal{M}_2$, so $P_1(N) \pi_c(z_0) \in \mathcal{M}_2 = \varphi^* M_2 + \mathcal{M}_2^{\mathrm{high}}$ by part 4. Multiplied by $\ell^b$, it lies in $\ell^b \varphi^* M_2 + \mathcal{M}_2^{\mathrm{high}} \subseteq T$.

*$P_2$.* The vector $y = X^{eA'} \pi_c(x)$ lies in the $c$-isotypic part of $X^{eA'} \varphi^* M_2$. By part 5 for $D_2$, $P_2(N) y = X^{2eA'} w + h$ with $w \in \varphi^* M_2$ and $h \in \mathcal{M}_2^{\mathrm{high}}$. By part 3, $X^{eA'} w = F y' + \ell^b z'$, so
$$X^{2eA'} w = X^{eA'} F y' + \ell^b X^{eA'} z' \in T. \qquad \square$$

**Theorem 7.21.6 (The cokernel on the image lattice).** Let $\ell$, $e$, $a$, $L$ be as above, and let $(N, \eta, H, \Sigma, U)$ satisfy the numerical conditions. Let $D_1$ and $D_2$ be Breuil-Kisin data of heights $(\eta, H)$ whose characters lie in $\Sigma$ at every $\tau$, and let $F : D_1 \to D_2$ be a map of Breuil-Kisin data whose cokernel has finite length. Then $\ell^{\rho}$ kills the cokernel of $F$ from $\varphi^* M_1$ to $\varphi^* M_2$.

Lean: `GlobalTheory.CokerL.kills_cokerL` (also `GlobalTheory.T.breuilKisin_pow_kills_lattice_cokernel`, a second name).

*Proof.* Let $b$ and $A'$ be as in the lemma. From $2A' + 2 < \ell$ we get $2A' \le \ell$.

*Step 1: one step.* We show: for $x \in \varphi^* M_2$ there are $y \in \varphi^* M_1$ and $z \in \varphi^* M_2$ with $\ell^\rho x = F y + \ell^b z$. Sum the lemma over $c$. Since $\sum_c \pi_c$ is the identity,
$$\ell^\rho X^{eA'} x = X^{eA'} F y' + \ell^b z' + h$$
with $y' \in \varphi^* M_1$, $z' \in \varphi^* M_2$ and $h \in \mathcal{M}_2^{\mathrm{high}}$. All other terms lie in $\varphi^* M_2$, so $h$ does too. By part 4, $h = X^{e\ell} h_0$ with $h_0 \in \varphi^* M_2$. Put
$$w = \ell^\rho x - F y' - X^{e(\ell - A')} h_0 \in \varphi^* M_2.$$
Then $X^{eA'} w = \ell^b z'$, so by part 6, $w = \ell^b z''$ with $z'' \in \varphi^* M_2$. Next, $X^{e(\ell - A')} h_0 = X^{eA'} \big(X^{e(\ell - 2A')} h_0\big)$, and part 3 gives $X^{e(\ell - A')} h_0 = F y_2 + \ell^b z_2$. So
$$\ell^\rho x = F(y' + y_2) + \ell^b (z'' + z_2).$$

*Step 2: iteration.* By induction on $k$, for every $x \in \varphi^* M_2$ there are $y$ and $z$ with $\ell^\rho x = F y + \ell^{\rho + k} z$. For $k = 0$ take $y = 0$ and $z = x$. For the step, write $\ell^\rho x = F y + \ell^{\rho + k} z$ and apply Step 1 to $z$: $\ell^{\rho} z = F y_2 + \ell^{b} z_2$. Then $\ell^{\rho + k} z = \ell^k F y_2 + \ell^{\rho + k + 1} z_2$.

*Step 3: the cokernel on $M$.* By part 7, $\ell^m$ kills the cokernel of $F$ on $M$ for some $m$. The lattice $\varphi^* M$ is the $\mathfrak{S}_{\mathcal{O}}$-span of $\varphi(M)$, and $F \varphi = \varphi F$. If $F y_0 = \ell^m w$ with $w \in M_2$, then $F \varphi(y_0) = \ell^m \varphi(w)$, and $\varphi(y_0) \in \varphi^* M_1$. Sums and multiples by $\mathfrak{S}_{\mathcal{O}}$ follow. So $\ell^m$ kills the cokernel from $\varphi^* M_1$ to $\varphi^* M_2$.

*Step 4: conclusion.* Take $k = m$ in Step 2: $\ell^\rho x = F y + \ell^{\rho} \ell^{m} z$. By Step 3, $\ell^m z = F y_3$. So $\ell^\rho x = F(y + \ell^\rho y_3)$. $\square$

Step 3 alone gives $\ell^m$ with an unknown $m$. The isotypic step turns this into the explicit exponent $\rho$: it moves $\ell^\rho x$ into the image modulo $\ell^{\rho + 1}$, and the iteration pushes the error into $\ell^{\rho + m}$, where $\ell^m$ absorbs it.

**Theorem 7.21.7 (The cokernel on six lattices).** Let $\ell$, $e$, $a$, $L$ be as above, and let $(N, \eta, H, \Sigma, U)$ satisfy the numerical conditions. Let $D_1$ and $D_2$ be Breuil-Kisin data of heights $(\eta, H)$, with $D_1$ of type $(\Sigma, U)$ (its characters lie in $\Sigma$ and its jumps lie in $U$, as for packs in Section 14) and the characters of $D_2$ in $\Sigma$. Let $F : D_1 \to D_2$ be a map of Breuil-Kisin data whose cokernel has finite length. Then $\ell^{\rho}$ kills the cokernel of $F$ on each of the six lattices: from $\varphi^* M_1$ to $\varphi^* M_2$, from $M_1$ to $M_2$, from $(M_1)_\eta$ to $(M_2)_\eta$, from $M_1^\Delta$ to $M_2^\Delta$, from $Y_{1,\eta}$ to $Y_{2,\eta}$, and from $Y'_{1,\eta}$ to $Y'_{2,\eta}$.

Lean: `GlobalTheory.Proof.cokernel_latticeMap_killed_by_prime_pow.main` (also `GlobalTheory.T.cokernel_latticeMap_killed_by_prime_pow`, a second name).

*Proof.* Since $D_1$ is of type $(\Sigma, U)$, its characters lie in $\Sigma$. The field $L$ is finite over $\mathbb{Q}_\ell$, hence complete. So the [Theorem 7.21.6](/entry/kills-coker-l/) on the image lattice applies, and part 8 carries the result to the six lattices. $\square$

**Example 7.21.8.** If $\Sigma = \{0\}$, then $r = 1$ and $\rho = 2(N - 1)$.

**Remark 7.21.9 (Formalization).** The given results are, in order, `maxFrobeniusOrbitLengthDiff_bounds_zmod` and `numerical_conditions_theorem_T_large_prime`, `lagrange_prime_pow_mem_isotypicDegreePoly_span`, `vPow_lattice_le_image_add_lPow_of_finite_cokernel`, `monodromy_reduction_modulo_high_degree` with `eulerDerivation_preserves_breuilKisin_sum_submodule`, `isotypic_monodromy_polynomials_raise_degree`, `mem_prime_pow_lattice_of_X_pow_smul_mem`, `exists_prime_pow_kills_finiteLength_integralPowerSeries` and `killsCoker_all_of_killsCoker_phiModuleLattice`, with the facts on `isoProj`. We read their statements, not their proofs, and we did not unfold the characters of a descent datum. The lemma is `isotypic_step` ([BreuilKisinPowKillsLatticeCokernel.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/BreuilKisinPowKillsLatticeCokernel.lean#L75)). The set $U$ is a hypothesis of both theorems but is never used: the proofs use only the characters, and the second theorem uses only the part of "of type $(\Sigma, U)$" that concerns characters ([CokernelLatticeMapKilledByPrimePow.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CokernelLatticeMapKilledByPrimePow.lean#L14)). No theorem of Fontaine or of Bhatt and Scholze enters. Both second names are wrappers that set `maxHeartbeats` to 1000000.
