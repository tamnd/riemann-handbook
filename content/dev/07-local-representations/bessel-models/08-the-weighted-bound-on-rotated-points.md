---
title: The weighted bound on rotated points
decls:
  - CompanionTheory.WaveGrid.weighted_bound_rotated_uniform
  - CompanionTheory.WaveGrid.weighted_bound_rotated_uniform_of_hypsG
  - CompanionTheory.WaveGrid.uniform_bessel_rank_three_of_inputs
  - CompanionTheory.WaveGrid.weighted_bound_rotated_uniform_of_cubic_threshold
  - CompanionTheory.WaveGrid.wave_bessel_period_threshold
  - CompanionTheory.WaveGrid.WGlue.weighted_uniform_rotated_of_expansion_alt_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The weighted bound on rotated points

This section proves the main estimate of the chapter: a weighted sum over global points of products of local orbital integrals of discrete series coefficients is bounded by a power of the size parameter times the product of the local Bessel norms, uniformly in the global datum. The code calls it a form of Theorem B. It is the estimate that the closed bound uses, and through it the step [HypsAlt is nonempty](/step/nonempty-hyps/). The proof puts together the results of the earlier sections: the uniqueness of discrete series with large gaps, the Zuckerman tensoring of [the ingredients](/entry/zuckerman-ingredients/), the moments of [the Pieri section](/entry/moment-first-length/) and the domination of [the normal form](/entry/normal-form-top-domination/). The analysis happens at one place; the global bound is a product of local ones.

### Global points and the statement

A global datum $D$ gives two ranks $k, r$, with $n = 2r + k + 1$; a CM field $E$; a finite set $\mathcal{T}$ of places with embeddings $\iota_v : E \to \mathbb{C}$; and a Harish-Chandra parameter $\lambda^0_v \in \mathbb{R}^n$ for each $v \in \mathcal{T}$. The local groups are unitary groups in $n$ variables at real places ([unitary groups](/learn/groups/#unitary-groups)).

**Definition 6.8.1 (Points).** A *point* $\gamma$ of size $r+1$ is a list of blocks $(t_i, s_i)$ with $t_i \in E^\times$, $s_i \geq 1$ and $\sum s_i = r+1$. Its matrix is block diagonal; the block $i$ is $t_i$ times the antidiagonal matrix of ones of size $s_i$. Let $\Delta_l$ be the leading $l \times l$ minor. For natural numbers $T, T'$ put
$$G(\gamma) = \Delta_{r+1} \bar\Delta_{r+1} - T T' \, \Delta_r \bar\Delta_r .$$
The point is *admissible* if $G(\gamma)$ is a nonzero algebraic integer and $L \gamma U$ is integral for some lower and some upper unitriangular matrices $L, U$ over $E$. Its *norm weight* is $N(\gamma) = \prod_v |\iota_v G(\gamma)| \cdot \prod_l \prod_v |\iota_v \Delta_l|^2$, with $l$ over the ends of the blocks.

At a place $v$, the local point $\gamma_v$ has blocks $(\alpha_i \iota_v(t_i), s_i)$ with fixed positive scalars $\alpha_i$, and the *rotated point* $\tilde\gamma_v$ has the entries $(-1)^r (-i)^{a+b} (\gamma_v)_{ab}$.

**Definition 6.8.2 (Bessel data).** A *Bessel datum* $X$ with constants $C_h, C_g$ and size $b$ gives, at each $v$, a local datum $L_v$: a discrete series $\sigma_v$ of $\mathrm{U}(p_v, q_v)$ with parameter $\lambda_v = \lambda^0_v$ ([discrete series](/learn/representations/#discrete-series)), two finite-dimensional representations, vectors $z, z'$ with $T_z = T$ and $T_{z'} = T'$, a $K$-finite matrix coefficient $f_v$ of $\sigma_v$, and a section $\mu_v$. The data meet size conditions in $b$; among them $b \geq C_g n^7$, and a scaling constant $\kappa$ with $\kappa, \kappa^{-1} \leq b^{C_h}$.

Let $O_v(\gamma)$ be the supremum of the squared Hilbert-Schmidt norms of the orbital integrals of $f_v$ at $\tilde\gamma_v$. Let $J_v$ be the weighted $L^2$ norm of the Bessel function of $f_v$ on the big cell, denoted $j_{N2}$ in the local statements. We have not unfolded the orbital integral or $J_v$ beyond this description.

**Theorem 6.8.3 (Weighted bound on rotated points).** For all $A_w \geq 0$ and $C_h$ there are $C_b$ and $C_{g,0}$ such that the following holds for all $C_g \geq C_{g,0}$, all data $D$ and all Bessel data $X$. If $|\lambda_v(s) - \lambda_v(s')| \geq C_g (2r+2)^4$ for all $v$ and $s \neq s'$, then
$$\sum_{\gamma \text{ admissible}} w(\gamma) \, \omega(\gamma) \, N(\gamma)^{A_w (r+1)^2} \prod_v O_v(\gamma) \leq b^{C_b (2r+2)^5 |\mathcal{T}|} \prod_v J_v .$$
Here $w(\gamma) = \prod_l \prod_v (1 + |\iota_v \Delta_l|^2)^2$, and $\omega(\gamma)$ is a second weight from the local blocks, which we have not unfolded.

Lean: `CompanionTheory.WaveGrid.weighted_bound_rotated_uniform` (also `CompanionTheory.WaveGrid.weighted_bound_rotated_uniform_of_hypsG`).

The proof is at the end of the section, after the local estimate and the assembly.

### The weighted one-place bound

At one place the statement is a pointwise bound. Write $G_p(\gamma)$ for the local value of $G$ at a local point $\gamma$.

**Definition 6.8.4 (Weighted one-place bound).** For a real $C_b$, the *weighted one-place bound* says: for all $C \geq 0$ and $C_a$ there are $C_5 \geq 0$ and $C_{g0}$ with the following property. Let $C_g \geq C_{g0}$, and let $f$ be a $K$-finite coefficient of a discrete series with parameter $\lambda$ at a local Bessel datum with types $u, u'$. Assume that $\lambda$ has gaps at least $C_g (2r+2)^4$, that $|\lambda_s| \leq b$, that $\lambda$ meets the sign and size conditions in $b$ and in an auxiliary $b_v \geq C_g n^7$, and that $1 \leq T, T' \leq b^{C(2r+2)}$. Assume one of two cases: either $|u_{l_0} - u'_{l_0}| \geq 30(r+1)^2 + 6$ and the decomposition condition at level $C_b$ of [the normal form section](/entry/normal-form-top-domination/) holds, or $u = u'$ and $u_l - u_{l+1} \geq 2(30(r+1)^2 + 6) + 1$ for some $l$. Then for every $j \leq r$, every $a \leq C_a (2r+2)^3$ and every local point $\gamma$ with $G_p(\gamma) > 0$,
$$|m_j(\gamma)|^{2a} \, E(\gamma) \leq b^{C_5 (2r+2)^5} \max\big(1, 1/G_p(\gamma)\big)^{40 (r+1)^2} \, j_{N2},$$
where $E(\gamma)$ is the local term of $f$ at $\gamma$ for the empty word and $m_j(\gamma)$ is a minor of size $j$.

The estimate needs a threshold. A *threshold* is a function $t(n, \varepsilon)$ of $n$ and a signature $\varepsilon : \{1, \dots, n\} \to \{\pm\}$. It is *good* if, for parameters $\mu$ whose gaps between entries of different sign exceed $t(n, \varepsilon) + 1$, the tensor product of the discrete series at $\mu$ with the standard representation (and with its dual) splits into inequivalent discrete series at $\mu + e_s$ (and $\mu - e_s$), in the sense of [the Zuckerman ingredients](/entry/zuckerman-ingredients/): products of coefficients with matrix coefficients of the standard representation are finite sums of coefficients of the summands, and conversely.

**Theorem 6.8.5 (Weighted one-place bound).** Let $t$ be a good threshold with $t(n, \varepsilon) \leq C_t n^3$ for $n \geq 1$, where $C_t \geq 0$. Assume the two family and moment statements below. Then the weighted one-place bound holds for every $C_b$.

The two statements are: (i) a discrete series whose parameter satisfies the numerical conditions of [the Pieri section](/entry/family-setup-cayley-moment/) lies in a family of discrete series at the shifted parameters $\lambda + \nu$ with $|\nu|_1 \leq q_0$; (ii) for a local Bessel datum, the Bessel function has an expansion on the big cell, and its moments satisfy $\mathrm{mom} \leq b^{(C+12)(2r+2)^2 a} \, j_{N2}$.

Lean: `CompanionTheory.WaveGrid.wave_bessel_period_threshold`.

*Proof.* The proof fills the inputs of a long proved lemma. The inputs are:

1. seven facts on coefficients of discrete series, from the theorem on the infinitesimal character of discrete series;
2. $K$-finite vectors are smooth;
3. the endpoint bound for two different types $u \neq u'$ at the extreme index $l_0$, with $|u_{l_0} - u'_{l_0}| \geq 30(r+1)^2 + 6$, and $n_0 = 0$;
4. the endpoint bound for equal types, with a gap of $2n_0 + 1$ at some index and $n_0 = 30(r+1)^2 + 6$;
5. smoothness of the Bessel function of a smooth coefficient;
6. uniqueness: two discrete series with the same parameter and gaps above $n^3 + 1$ are unitarily equivalent.

The endpoint bound reads: at a local point $\gamma$ with $G_p(\gamma) > 0$,
$$E_w(\gamma) \leq b^{C_4 (2r+2)^4} \, G_p(\gamma)^{-(2p_0 + n_0)} \, j_{N2}.$$
Both endpoint bounds come from the asymptotics of the coefficients on the big cell and from the domination of the normal form, which allows the passage to the limit in the cutoff. Item 6 comes from the uniqueness of discrete series with a given parameter under a gap condition with threshold $npq + 1$, together with $p, q \leq n$, so $npq + 1 \leq n^3 + 1$. This has the shape of the uniqueness part of the classification of Harish-Chandra (Acta Math. 116 (1966)); see [discrete series and formal degrees](/learn/real-groups/#discrete-series-and-formal-degrees).

Inside the lemma, the endpoint bounds give constants $C_1, C_A$ and $C_2, C'_A$, and a weighting lemma gives $c_3$. Put
$$C_5 = 4|C_a| + \max(C_1, C_2, 0) + (C+12)|C_a|, \qquad C_{g0} = 10^6 + C_t + |C_A| + |C'_A| + |c_3| + 100 |C_a| .$$
Statement (i) puts the discrete series in a family around $\lambda$. For each shift $\nu$, item 3 or item 4 bounds the local term; the case is the one assumed in the definition. The weighting lemma sums these bounds against $|m_j(\gamma)|^{2a}$, and statement (ii) bounds the resulting moment by $b^{(C+12)(2r+2)^2 a} j_{N2}$. With $a \leq C_a (2r+2)^3$ the exponents combine into $b^{C_5 (2r+2)^5}$. $\square$

### Reduction to one place

**Theorem 6.8.6 (Reduction to one place).** Assume the weighted one-place bound for every $C_b$. Assume the regularity statement with a constant $C_{gc}$: every $K$-finite coefficient whose gaps are at least $C_{gc} (2r+2)^{9/2} \big(3(r+1) n^2 + n^3\big)$ lies in the decay class of [the normal form section](/entry/normal-form-top-domination/) of the fixed order $A_0(k, r)$, for one derivative. Assume a frame bound from the Bessel torus with constant $C_{gf}$ for every datum $D$. Then the weighted bound on rotated points holds.

Lean: `CompanionTheory.WaveGrid.WGlue.weighted_uniform_rotated_of_expansion_alt_alt`.

*Proof.* Fix $A_w \geq 0$ and $C_h$. The first two assumptions give constants $C$ and $C_{g0}$ and a local inequality at every place: for $a \leq 2(1 + A_w + 10)(2r+2)^3$ and every point $\gamma$ with $G_p(\gamma) \neq 0$, the weighted orbital integral times $|m_l(\gamma)|^{2a}$, for a leading minor $m_l$, is at most $b^{C (2r+2)^5} \max(1, 1/G_p)^{40(r+1)^2} j_{N2}$. A proved reduction to one place shows that the global bound with constant $C_K + 6$ follows from a bound at each place $v$ and each admissible $\gamma$:
$$w_v(\gamma)^2 (1 + d_v(\gamma))^A \, n_v(\gamma) \, W_v(\gamma)^{A_w (r+1)^2} \, O_v(\gamma) \leq b^{C_K (2r+2)^5} \max\big(1, 1/|\iota_v G(\gamma)|\big)^A J_v,$$
with an exponent $A$ fixed by $D$, and local weights $w_v, d_v, n_v, W_v$ that we have not unfolded.

Fix $v$ and $\gamma$. If $O_v(\gamma) = 0$ there is nothing to prove. Otherwise there is a group element that represents the orbit, and this forces $G_p(\tilde\gamma_v) \geq 0$. Since $G$ is a nonzero algebraic integer, the real number $x = \iota_v G(\gamma)$ is nonzero, and $G_p(\tilde\gamma_v)$ is a positive multiple of $x$. The size conditions give $b \geq 2$ and $\kappa, \kappa^{-1} \leq b^{C_h}$. A weighting lemma picks an index $l$ and an exponent $a$, at most twice the sum of the multiplicities, with
$$\Big( \prod_l (1 + s_l |m_l|^2)^{N_l} \Big)^2 \leq (2\sigma)^{2 \sum N_l} |m_l|^{2a}$$
for weights $s_l \leq \sigma$, where $\sigma = b^{(3 + C_h)(2r+2)^2}$. A count of weighted points bounds the multiplicities by $(1 + A_w + 10)(2r+2)^3$, so $a$ is in the range of the local inequality. The frame bound moves the point by the scaling $\kappa$; this changes each minor by at most $b^{C_h (2r+2)^2}$. The local inequality then bounds the left side, and the remaining factors are powers of $b$ with exponents at most a constant times $(2r+2)^5$. The constant is
$$C_K = (4 + |C_h|) \cdot 2(1 + A_w + 10) + |C_h| \cdot 4(1 + A_w + 10) + 4|C_h| + C + 10(3 + 3|C_h|),$$
and $C_{g,0} = \max(C_{g0}, C_{gf}, 2)$. $\square$

### Assembly

**Theorem 6.8.7 (Bound from a cubic threshold).** Let $t$ be a good threshold with $t(n, \varepsilon) \leq C_t n^3$ for $n \geq 1$ and $C_t \geq 0$. Assume statements (i) and (ii) and the frame bound with constant $C_{gf}$ for every datum. Then the weighted bound on rotated points holds.

Lean: `CompanionTheory.WaveGrid.weighted_bound_rotated_uniform_of_cubic_threshold` (also `CompanionTheory.WaveGrid.uniform_bessel_rank_three_of_inputs`).

*Proof.* The theorem on the weighted one-place bound gives the first input of the reduction to one place. A proved regularity lemma gives the second: from the cubic bound, the tensoring up, the smoothness of $K$-finite vectors and the continuity of coefficients under Capelli operators, the regularity statement holds with $C_{gc} = C_t + |c_3| + 2$. The reduction to one place gives the bound.

For the explicit version, let $p, q$ be the numbers of plus and minus signs of $\varepsilon$, $q_0 = \min(p, q)$, and
$$t(n, \varepsilon) = \max\big(2n, \; 16 n q_0 + 8 \sqrt{2 q_0}\big).$$
Since $q_0 \leq n$ and $\sqrt{2 q_0} \leq 2n$, we get $t(n, \varepsilon) + 1 < 43 n^2 \leq 43 n^3$ for $n \geq 1$. The Zuckerman tensoring theorems show that $t$ is good, for the standard representation and for its dual. So the first part applies with $C_t = 43$. $\square$

*Proof of the theorem on the weighted bound.* The Zuckerman gap statement is proved, and with six further proved facts it gives a package of seven statements on discrete series of unitary groups: the inputs on families, smooth cyclic vectors, the infinitesimal character, the existence of a discrete series with a given parameter when the gaps are large, Zuckerman tensoring, invariant forms on smooth vectors (Poulsen), and the formula for the formal degree. A proved lemma turns this package into statements (i) and (ii). The frame bound from the Bessel torus is proved with constant $100$ for every datum. The explicit version of the bound from a cubic threshold gives the theorem. $\square$

**Remark 6.8.8 (Formalization).** The statement is `WeightedBoundRotatedUniform` in [WeightedUniformRotatedOfExpansion.lean](lean:Formalism/SharpRestriction/CuspSpanNormBounds/WeightedUniformRotatedOfExpansion.lean#L156); its right side is written $\exp(C_b (2r+2)^5 |\mathcal{T}| \log b)$. The caller `theoremB_uniform_rotated` turns it into `JointNormBoundRotatedUniform` with `exact h`; that proposition, in [ThmBUseR.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmBUseR.lean#L38), is a word-for-word copy. The objects `orbSq`, `jNorm2`, `Ew`, `InCC`, `IsDS` and the weights `wLoc`, `dLoc`, `nLoc`, `WLoc` were not unfolded. The package `HypsG` is passed whole to `wave_inputs_of_hypotheses_global`, so we do not know which of the seven parts are used. The constant $100$ in [WeightedBoundRotatedUniformOfHypsG.lean](lean:CompanionTheory/AutomorphicTheory/BesselWaveGrids/WeightedBoundRotatedUniformOfHypsG.lean#L7) is the least that `one_bessel_torus_bound` accepts. The name `uniform_bessel_rank_three_of_inputs` ([WeightedBoundRotatedUniformOfCubicThreshold.lean](lean:CompanionTheory/AutomorphicTheory/BesselWaveGrids/WeightedBoundRotatedUniformOfCubicThreshold.lean#L54)) has no rank three condition, and the threshold `thrS` sits in a namespace `G2` in [Transported.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/ExceptionalGroupG2/TensorProductsG2/Transported.lean#L10), although nothing is about $G_2$. The lemma `thrS_lt` proves a quadratic bound but only the cubic `thrS_le` is used. In [EndpointDifferentTypesThreshold.lean](lean:CompanionTheory/AutomorphicTheory/BesselWaveGrids/EndpointDifferentTypesThreshold.lean#L11) the endpoint theorems discard hypotheses with `_`. The lemmas `wBp_of` ([PowFourLeRpowNineHalves.lean](lean:CompanionTheory/AutomorphicTheory/BesselWaveGrids/PowFourLeRpowNineHalves.lean#L106)) and `wLoc1N_of` raise `maxHeartbeats` to 1,600,000.
