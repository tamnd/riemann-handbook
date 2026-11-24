---
title: Group sums over a row and a double coset
decls:
  - GlobalTheory.HL.RowCoset.row_coset_sum_norm_sq
  - GlobalTheory.T.row_doubleCoset_sum_norm_sq_bound
  - GlobalTheory.FamilyNormRational.squaredGroupSum_classDoubleCoset_eq_rowWeight
  - GlobalTheory.FamilyNormRational.familyGroupSumFactorsRowWeightAmplitude
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Group sums over a row and a double coset

This section sums the term vectors of the double coset sum over one row and one rational double coset. The result is an exact formula: the squared norm of the sum is the squared row weight, times the squared norm of a global amplitude, times an archimedean factor. The global amplitude is a sum over the orbits of global terms with one datum, and it factors into local amplitudes at the finite places. The proof matches the terms of the row and the coset one to one with these orbits, with the results of [the previous section](/entry/exists-term-of-global/). Then we group the terms by classes of a family, and we choose a rescaling of the archimedean measures that removes the archimedean factor. The last theorem is used in the step [HypsAlt is nonempty from the closed bound](/step/nonempty-hyps/).

We keep the setting of [the previous section](/entry/exists-term-of-global/): a datum $D$, words $u$ and $u'$ with the standing hypotheses and $4r + 7 \le k$, a point $w$, base flags $F_{00}$ and $F'_0$, local frame pairs, global frames $(S_p)$ with global coordinates $\operatorname{lat}$, a term $t_0$ and an isometry $\rho$ that moves the frame of $t_0$ to the base flags. Let $d_0$ be the datum of $\operatorname{lat}(\rho, \lambda_{t_0})$. Each term $t$ has its vector $a_t$, its row weight $\mathrm{wt}(t)$, its rational double coset $N(F_u)\, \ell_t\, N(F_{u'})$, and it is *generic* or not.

**Definition 2.12.1 (Global amplitude).** Two lattices $\Gamma$ and $\Gamma'$ in the frame space are *related* if $\Gamma' = x \Gamma$ for some $x$ in the common unipotent group $N \cap N'$. For a lattice $\Gamma$ let $\mu(\Gamma)$ be the inverse of the covolume of the stabilizer of $\Gamma$ in $N \cap N'$, relative to a fixed compact subgroup. A global term $(d, \Gamma)$ is *generic* if a local condition holds at every place. For a datum $d$ and a property $P$ of lattices, the *global amplitude* is
$$\operatorname{amp}(d, P) = \sum_{o} \mu(\Gamma_o)\, \omega(d, \Gamma_o),$$
where $o$ runs over the classes of related lattices, $\Gamma_o$ is a representative of $o$, and the sum is restricted to the $o$ such that $(d, \Gamma_o)$ is a global term and $P(\Gamma_o)$ holds. Here $\omega$ is the [global phase](/entry/global-witnesses/).

We use a selector $Q$, a map from propositions to propositions, to pick the generic terms, the nongeneric terms, or all terms. For instance $Q(\phi) = \phi$ keeps the terms where "not generic" holds.

Let $\nu$ be a pinned family of measures on the archimedean group, and let $J(\nu, w)$ be the archimedean operator of the point $w$, with its Hilbert-Schmidt norm $\|J(\nu, w)\|_{\mathrm{HS}}$. Let $g$ be the integer of the setting, $f$ the number of infinite places, and $\Phi(w)$ the set of free indices of $w$. Put
$$\kappa(w) = g^{-f\, \#\Phi(w)}.$$

**Theorem 2.12.2 (Sum over a row and a double coset).** In this setting, let $\nu$ be pinned, let $t_0$ be relevant with point $w$, and let $Q$ be a selector. Let $\Sigma$ be the sum of $a_t$ over the terms $t$ with the row of $t_0$, the double coset of $t_0$, and $Q(t \text{ not generic})$. Then
$$\|\Sigma\|^2 = \mathrm{wt}(t_0)^2\, |\operatorname{amp}(d_0, P_Q)|^2\, \kappa(w)^2\, \|J(\nu, w)\|_{\mathrm{HS}}^2,$$
where $P_Q(\Gamma)$ is $Q((d_0, \Gamma) \text{ not generic})$.

Lean: `GlobalTheory.HL.RowCoset.row_coset_sum_norm_sq` (also `GlobalTheory.T.row_doubleCoset_sum_norm_sq_bound`, a second name).

*Proof.* We use six facts of the term setting.

1. A term $t$ has the double coset of $t_0$ if and only if $\ell_t = n^{-1} \ell_{t_0} m$ for some $n \in N(F_u)$ and $m \in N(F_{u'})$. Then $\rho n$ moves the frame of $t$ to the base flags.
2. If $t$ also has the row of $t_0$, then $\lambda_t = \lambda_{t_0}$, $\lambda'_t = \lambda'_{t_0}$, the datum of $\operatorname{lat}(\rho n, \lambda_t)$ is $d_0$, and $(d_0, \operatorname{lat}(\rho n, \lambda_t))$ is a global term.
3. In this position, $t$ is generic if and only if the global term $(d_0, \operatorname{lat}(\rho n, \lambda_t))$ is generic.
4. Two such terms $t, t'$ with elements $(n, m)$ and $(n', m')$ are equal if and only if $\operatorname{lat}(\rho n, \lambda_t)$ and $\operatorname{lat}(\rho n', \lambda_{t'})$ are related.
5. Relation is an equivalence on lattices, it preserves global terms with datum $d_0$, and there are only finitely many classes of related lattices $o$ such that $(d_0, \Gamma_o)$ is a global term.
6. There is an operator $T$ with $\|T\| = \|J(\nu, w)\|_{\mathrm{HS}}$ such that, for every term $t$ in the position of the first two facts, $a_t$ is the vector with the single component
$$\mathrm{wt}(t_0)\, \kappa(w)\, \mu(\Gamma)\, \omega(d_0, \Gamma)\, T, \qquad \Gamma = \operatorname{lat}(\rho n, \lambda_t),$$
at the pair of lattices $(\lambda_{t_0}, \lambda'_{t_0})$, and $0$ at the other pairs.

The last fact is the unfolding of the archimedean orbital integral of a term; it uses that $\nu$ is pinned and $t_0$ is relevant. The row weight of $t$ equals $\mathrm{wt}(t_0)$, since it depends only on the two lattices.

Let $C$ be the finite set of classes $o$ such that $(d_0, \Gamma_o)$ is a global term and $P_Q(\Gamma_o)$ holds. For $o \in C$, the theorem on [global terms in the row](/entry/exists-term-of-global/) gives a term $\tau(o)$ with the row of $t_0$, elements $(n, m)$ as in the first fact, and $\Gamma_o = \operatorname{lat}(\rho n, \lambda_{\tau(o)})$. By the third fact, $\tau(o)$ satisfies $Q(\tau(o) \text{ not generic})$, so $\tau(o)$ is a term of $\Sigma$. The map $\tau$ is injective on $C$ by the fourth fact. It is onto the terms of $\Sigma$: for such a term $t$, the first two facts give a global term $\Gamma = \operatorname{lat}(\rho n, \lambda_t)$ with datum $d_0$, its class $o$ lies in $C$ by the fifth and third facts, and $\tau(o) = t$ by the fourth fact. So $\Sigma = \sum_{o \in C} a_{\tau(o)}$.

By the sixth fact, all these vectors sit in the same component, so
$$\Sigma = \mathrm{wt}(t_0)\, \kappa(w) \Big(\sum_{o \in C} \mu(\Gamma_o)\, \omega(d_0, \Gamma_o)\Big) T = \mathrm{wt}(t_0)\, \kappa(w) \operatorname{amp}(d_0, P_Q)\, T$$
in that component. The norm of a vector with a single component is the norm of the component. Take the squared norm. $\square$

Now we group the terms by classes. Let $S$ be a selector and let $T_S$ be the set of terms $t$ with nonzero $G$-value and $S(t \text{ not generic})$. A *family* consists of a map $\mathrm{cls}$ on terms with values in a set of classes, a point $\gamma$, and local data, with these properties:

1. inside each double coset, the terms of $T_S$ in one class lie in one row;
2. some term $t_1 \in T_S$ has point $\gamma$ and $a_{t_1} \ne 0$;
3. the local data consist of finite sets $\Omega \subseteq P$ of finite places, a weight $\mathrm{rw}(c) \ge 0$ for each class $c$, and a partial map $\mathrm{dat}$ from pairs $(c, \eta)$ of a class and a double coset to families $d = (d_p)_{p \in P}$ of local data;
4. $\mathrm{dat}(c, \eta)$ is defined if and only if some $t \in T_S$ has class $c$, point $\gamma$ and double coset $\eta$; then every such $t$ lies over the local orbits of $d$, and $\mathrm{wt}(t)^2 = \mathrm{rw}(c)$.

For local amplitudes $a^N_p$ and $a^Z_p$ at the places of $P$, the *local amplitude* of $d$ is
$$A_S(d) = \sum_{B} \prod_{p \in B} a^N_p(d_p) \prod_{p \in P \setminus B} a^Z_p(d_p),$$
where $B$ runs over the subsets of $\Omega$ with $S(B \ne \emptyset)$.

For a class $c$ and a double coset $\eta$ let $\Sigma(c, \eta)$ be the sum of $a_t$ over the $t \in T_S$ with class $c$, point $\gamma$ and double coset $\eta$. For a family $\nu'$ of measures let $J^2(\nu', \gamma) = \|J(\nu', z)\|_{\mathrm{HS}}^2$ for a point $z$ over $\gamma$ that has a representative, and $0$ if there is none.

**Theorem 2.12.3 (Squared group sum of a class and a double coset).** Assume the standing hypotheses, $4r + 7 \le k$ and the concentration tie. Let $\nu$ be pinned and let $s > 0$ be a function on the archimedean group with $s(\gamma_z) = \kappa(z)$ at the archimedean point $\gamma_z$ of each point $z$ that has a representative. Then for every family, every class $c$ and every double coset $\eta$,
$$\frac{\|\Sigma(c, \eta)\|^2}{J^2(s \nu, \gamma)} = \begin{cases} 0 & \text{if } \mathrm{dat}(c, \eta) \text{ is undefined}, \\ \mathrm{rw}(c)\, |A_S(d)|^2 & \text{if } \mathrm{dat}(c, \eta) = d. \end{cases}$$

Lean: `GlobalTheory.FamilyNormRational.squaredGroupSum_classDoubleCoset_eq_rowWeight`.

*Proof.* If $\mathrm{dat}(c, \eta)$ is undefined, no term of $T_S$ has class $c$, point $\gamma$ and double coset $\eta$. So $\Sigma(c, \eta) = 0$ and both sides are $0$.

Let $\mathrm{dat}(c, \eta) = d$, and take a term $t_0$ of $\Sigma(c, \eta)$, with the base flags and point $z$ that the local data give. The nongeneric classes determine rows, so $t_1$ is relevant, and all terms with point $\gamma$ have the same point $z$. The base flags have nonzero $G$-value, and the local frame pairs are relevant. There are global frames with coordinates for the base flags, and an isometry $\rho$ moves the frame of $t_0$ to them up to unitriangular matrices.

The terms of $\Sigma(c, \eta)$ are exactly the terms with the row of $t_0$, the double coset of $t_0$ and $S(t \text{ not generic})$: the first property of the family puts them in one row, and the invariants of a term are constant on a rational double coset. So the theorem on the sum over a row and a double coset applies with $Q = S$:
$$\|\Sigma(c, \eta)\|^2 = \mathrm{wt}(t_0)^2\, |\operatorname{amp}(d_0, P_S)|^2\, \kappa(z)^2\, \|J(\nu, z)\|_{\mathrm{HS}}^2.$$
The global amplitude factors over the places: $|\operatorname{amp}(d_0, P_S)| = |A_S(d)|$. The rescaling gives
$$J^2(s\nu, \gamma) = s(\gamma_z)^2\, \|J(\nu, z)\|_{\mathrm{HS}}^2 = \kappa(z)^2\, \|J(\nu, z)\|_{\mathrm{HS}}^2.$$
This is not $0$: else the sixth fact of the previous proof gives $a_{t_1} = 0$. Divide, and use $\mathrm{wt}(t_0)^2 = \mathrm{rw}(c)$. $\square$

**Theorem 2.12.4 (Group sums factor as row weight times local amplitude).** For all constants $C_g, c_b, C_w, c_T, C_T, C_0$ there are $C_{\mathrm{St}} \ge 0$ and thresholds $C'_\ast, C_{l\ast}$ with this property. Let $C' \ge C'_\ast$ and $C_l \ge C_{l\ast}$, let $D$, size data with parameter $b$, $X$, $Y$, $u$, $u'$ satisfy the standing context for these constants, take mass data, and let $\nu$ be pinned. Then there is a function $s \ge 0$ on the archimedean group such that:

1. $s(\gamma) = 1$ at each regular $\gamma$;
2. $s(\gamma) > 0$ for every $\gamma$;
3. $s(\gamma)^2 \le b^{C_{\mathrm{St}} (2r+2)^3 f}$ for every $\gamma$;
4. for every family, class $c$ and double coset $\eta$, the identity of the previous theorem holds for $s\nu$.

Lean: `GlobalTheory.FamilyNormRational.familyGroupSumFactorsRowWeightAmplitude`.

*Proof.* Take $C_{\mathrm{St}} = 0$ and both thresholds $0$. The standing context contains the standing hypotheses and the concentration tie, and it gives $4r + 7 \le k$. A normalization lemma for the local readings gives $s$ with the first two properties, with $s \le 1$, and with $s(\gamma_z) = \kappa(z)$ at the archimedean point of each point $z$ that has a representative. The third property with $C_{\mathrm{St}} = 0$ reads $s(\gamma)^2 \le 1$, which holds since $0 \le s \le 1$. The fourth property is the previous theorem with this $s$. $\square$

**Remark 2.12.5.** The third property is stated with a constant $C_{\mathrm{St}}$ so that a rescaling that grows with $b$ would be allowed. The proof needs none: the normalized rescaling is at most $1$.

**Remark 2.12.6 (Formalization).** The global amplitude is `GFrames.amp`, a `tsum` over `Quot G.LRel`, and $\mu$ is `GFrames.mu`, defined with `invVol` ([GFrames.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/GFrames.lean#L112)). The name `row_doubleCoset_sum_norm_sq_bound` says "bound", but the statement is an equality ([RowDoubleCosetSumNormSqBound.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/RowDoubleCosetSumNormSqBound.lean#L52)). The six facts of its proof are `doubleCoset_eq_iff_isometry_unipotent_translate`, `termRow_eq_iff_movedLatticeInnerData_eq` with `movedTermLattice_isGlobalTerm_phase`, `generic_iff_zero_defectGroup_coordinates`, `doubleCoset_term_eq_iff_stabiliserOrbit`, `hermitian_amplitude_mass_product_structure` with `globalHermitianFrames_terms_orbits_local`, and `rowTerm_amplitude_eq_mass_mul_phase`; the single-component embedding is the local map `V` into a `WithLp 2` product. In the squared group sum, the quotient $\|\Sigma\|^2 / J^2$ is the real division `a2F`, and the right side is `a2W` with `ampQ`; the factorization of the global amplitude is `globalAmplitude_eq_localAmplitudes`. In `familyGroupSumFactorsRowWeightAmplitude` ([FamilyGroupSumFactorsRowWeightAmplitudeProof.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/FamilyGroupSumFactorsRowWeightAmplitudeProof.lean#L183)) the constant $C_{\mathrm{St}}$ is $0$, and most hypotheses are introduced and not used: the mass data (`hb`, `X0`, `ψ`, `hT`, `sd`, `C`, `Th`, `F0`, `vR`, `Q`, `i0`, `i0'`, `νq`, `Irat`, `Ire`, `hBk`) and the first half of the pinning; the constants enter only through `four_rank_add_seven_le_k`. The rescaling comes from `exists_scale_normalised_localReading`. The proposition it proves is `GlobalTheory.SnFam.FamilyGroupSumFactorsWeightAmplitude`.
