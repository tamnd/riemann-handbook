---
title: Local indices and pole lengths
decls:
  - Formalism.MainNotions.Gaps.EtaleWeightGaps.localIdx
  - Formalism.MainNotions.Gaps.EtaleWeightGaps.localBound
  - Formalism.MainNotions.Gaps.EtaleWeightGaps.lenPoleL_all
  - length_pole_t0
  - Formalism.MainNotions.Gaps.EtaleWeightGaps.rLa_tsum_le_comb
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Local indices and pole lengths

This section bounds, at one finite place, the length of a lattice of cusp forms modulo a submodule of theta products. The bound is linear in the dimension of the subspace that we cut with, and the constant $r_\lambda$ is a sum of a few local lengths. Then it sums the constants $r_\lambda$ over all finite places with logarithmic weights. One of the local lengths, the length of the poles, is bounded for all data by a theorem of another chapter, and this section states that bound in the form that the local bound uses. The results are used in the theorem that [assembles the four inputs of the net](/entry/inputs4-of-net/). For the background see [rings, ideals and modules](/learn/algebra/#rings-ideals-and-modules) and [places and completions](/learn/number-fields/#places-and-completions).

### The setting

Let $K$ be the number field of the data and let $\lambda$ be a finite place of $K$, that is a height one prime of $\mathcal{O}_K$. Let $\mathcal{O}_\lambda$ and $K_\lambda$ be the local ring and the local field at $\lambda$. Fix an index $j$, two weights $w_L$ and $w_F$, and an integer $T$. Let $\kappa$ be the weight that is built from $w_F$, $w_L$ and $T$. Let $\mathrm{Cusp}_j(\kappa)$ be the $K$-space of cusp forms of weight $\kappa$, with a lattice $M_j(\kappa)$. The data also give two $\mathcal{O}_K$-submodules $\Theta$ and $M^{\sup}$ of $\mathrm{Cusp}_j(\kappa)$. The submodule $\Theta$ is built from the theta forms of the data.

For submodules $A$ and $B$ of a module over a ring $O$, let $\ell(A, B)$ be the length of $A / (A \cap B)$, an element of $\mathbb{N} \cup \{\infty\}$. Put
$$\operatorname{idx}(A, B) = \ell(A, B) - \ell(B, A),$$
where an infinite length is read as $0$.

The local point data at $\lambda$ give a set of points $\zeta$. This set is finite when a curve condition holds. Each point has a ramification index $e_\zeta \geq 1$, a residue degree $f_\zeta$, and a depth $\nu(\zeta)$. The data also give the following.

1. A local length $I_\lambda \in \mathbb{N} \cup \{\infty\}$. It is the length of a ball module $A_0$ modulo the span of a family of sections.
2. An étale term $N_\lambda = \sum_\zeta e_\zeta f_\zeta \, v_\zeta(\eta)$, where $v_\zeta(\eta)$ is the valuation at $\zeta$ of a fixed étale form $\eta$.
3. For an integer $e \geq 0$, the multiplicities $m_\zeta = \max\big(0, \lceil e_\zeta (T \nu(\zeta) - e) \rceil\big)$.
4. Modules $A'_m \supseteq A$ of sections of a fixed weight $a_0$. A section is in $A'_m$ if its Hasse derivatives of order less than $a_0$ are integral and have order at least $-m_\zeta$ at each $\zeta$. We put $A = A'_0$.

Let $d$ be the dimension of the space $Y$ of the index $j$. Let $g_\lambda$ be a local constant of the lattice $M_j(\kappa)$ and of the family $z$ of coefficient vectors. Let $Q_m$ be a quotient module of the lattice that depends on the constants of the data, and let $\theta_1, \dots, \theta_\rho$ be the given theta forms.

### The local index bound

**Lemma 4.9.1 (Local index bound).** Assume the hypotheses of the setting at $\lambda$. These are the lattice condition on $M_j(\kappa)$, the inclusion $\Theta \subseteq M^{\sup}$, $1 \leq T$, $d \leq T$, the memberships of the given forms, the spanning conditions, the nonvanishing of a determinant of the $z$ coefficients, and the basis, curve and tie conditions at $\lambda$. Let $c_p \geq 0$, $\nu_s \in \mathbb{R}$ and $v \geq 0$ be such that $\nu(\zeta) \leq \nu_s + c_p v(\zeta)$ for all $\zeta$ and $T \nu_s \leq e$. Assume
$$\ell(A, A_1) \leq \binom{T-1}{d} I_\lambda, \qquad \ell(A'_m, A) \leq \binom{T-1}{d} \sum_\zeta m_\zeta f_\zeta,$$
where $A_1 \subseteq A$ is a fixed submodule. Let $M_W$ and $\Theta_W$ be the local images of the lattice and of $\Theta$ in the local space $W$. Then for every $K_\lambda$-subspace $U$ of $W$,
$$\operatorname{idx}(M_W \cap U, \Theta_W \cap U) \leq e \dim U + \binom{T-1}{d} T c_p \sum_\zeta e_\zeta f_\zeta v(\zeta) + \binom{T-1}{d} I_\lambda + g_\lambda + \ell_\lambda\big(Q_m / \langle \theta_1, \dots, \theta_\rho \rangle\big).$$

Lean: `Formalism.MainNotions.Gaps.EtaleWeightGaps.localIdx`.

*Proof.* The proof applies a general lemma on the descent of levels. That lemma takes a chain of submodules of $W$ together with the indices $e_\zeta$, the degrees $f_\zeta$, the depths $\nu$ and the weights $v$. Its inputs are proved here one at a time. The generators of the first and zeroth kinds lie in the span of $\Theta$, and that span lies in the integral forms. The theta forms $\theta_i$ map into $\Theta_W$. A reduction map has the expected kernel and image. The two given length bounds hold, and the bound on poles is rewritten as a finite sum over the points. The length of the zeroth module $Z_m$ modulo $Z_l$ is finite. It is at most $g_\lambda$ because the determinant of the $z$ coefficients is not zero. The level lemma then gives the bound with $\ell(Z_m, Z_l)$ in place of $g_\lambda$, and linear arithmetic ends the proof. $\square$

### The bound with the étale weights

For the next theorem put
$$r_\lambda = \binom{T-1}{d} \Big( I_\lambda + [j < m] \, \frac{T \max(0, c)}{2 i} \, N_\lambda \Big) + g_\lambda + \ell_\lambda\big(Q_m / \langle \theta_1, \dots, \theta_\rho \rangle\big),$$
where $m$ is a fixed rank of the setting, $i \geq 1$ is the index of the étale form, $c$ is a real constant, and $[j < m]$ is $1$ when $j < m$ and $0$ otherwise. The integer part of $I_\lambda$ is used, so the term is $0$ when $I_\lambda = \infty$.

**Theorem 4.9.2 (Local bound).** Assume the hypotheses of the lemma, with $\kappa$ built from $w_F$, $w_L$ and $T$, with $\nu(\zeta) \leq \nu_s + \max(0, c) \, v_\eta(\zeta)$ for all $\zeta$, and with $T \nu_s \leq e$. Here $v_\eta(\zeta) = v_\zeta(\eta)/(2i)$ when $j < m$, and $v_\eta(\zeta) = 0$ otherwise. Let $V'$ be a $K_\lambda$-subspace of the local span of $M^{\sup}$. Then the length $\ell_\lambda$ of $M^{\sup}_\lambda \cap V'$ modulo $\Theta_\lambda \cap V'$ is finite, and
$$\ell_\lambda(M^{\sup}_\lambda \cap V', \Theta_\lambda \cap V') \leq e \dim V' + r_\lambda.$$

Lean: `Formalism.MainNotions.Gaps.EtaleWeightGaps.localBound`.

*Proof.* A proved lemma turns a bound on $\operatorname{idx}$ for every subspace $U$ into finiteness and a bound on the length for every $V'$. We apply it with the local index bound, with $c_p = \max(0, c)$ and $v = v_\eta$. An identity for the étale levels rewrites the middle term of the local index bound:
$$T \max(0, c) \sum_\zeta e_\zeta f_\zeta v_\eta(\zeta) = [j < m] \, \frac{T \max(0, c)}{2 i} \, N_\lambda.$$
Then the right side is $e \dim V' + r_\lambda$. $\square$

### The length of the poles

**Theorem 4.9.3 (Length of the poles).** For all global data, every finite place $\lambda$, all local point data, scalars, real constants $C$ and $c$, and integers $T$ and $e$ the following holds. Assume that the local point data satisfy the four conditions of the setting: basis, curve, tie and containment. Assume also the lift condition at $T$, and that every form $w_k$ of the data lies in the given set $W$. Then
$$\ell(A'_m, A) \leq \binom{T-1}{d} \sum_\zeta m_\zeta f_\zeta.$$

Lean: `Formalism.MainNotions.Gaps.EtaleWeightGaps.lenPoleL_all` (also `length_pole_t0`, the same statement with the hypotheses in another order).

*Proof.* This is the pole length bound, a theorem proved in the chapter on period integrals, applied to the same data. Only the order of the hypotheses changes. $\square$

This is the second length hypothesis of the local index bound. The first one, with $I_\lambda$, is supplied in the same place by a bound on the first length.

### Summing over the places

For a finite place $\lambda$ put $\mathrm{lN}(\lambda) = \log N\lambda / [K : \mathbb{Q}]$.

**Theorem 4.9.4 (Sum of the local constants).** Let $1 \leq j \leq m$. Assume the main hypotheses of the setting, the lattice, supremum and $L^2$ conditions at the weight $\kappa$, and the quotient condition when $j < m$. Let the data be tied in the three senses of the setting with constants $G_c$ and $P_{rw}$. Assume the deep Hermitian, submultiplicative and logarithmic derivative conditions with constant $P_d$, the page condition, the polynomial domination, and the height conditions on a family of local point data $Q_\lambda$. Let $c$ be the constant of the setting, and let $|\kappa|$ be the size of $\kappa$. Then $\lambda \mapsto r_\lambda \, \mathrm{lN}(\lambda)$ is summable, and
$$\sum_\lambda r_\lambda \, \mathrm{lN}(\lambda) \leq \binom{T-1}{d} \Big( \sum_\lambda I_\lambda \, \mathrm{lN}(\lambda) + [j < m] \, \frac{T \max(0, c)}{2 i} \sum_\lambda N_\lambda \, \mathrm{lN}(\lambda) \Big) + \rho_z \, B \, |\kappa| + 2 \rho_q P_v |\kappa|,$$
with
$$B = 2 G_c + P_{rw} + P_{0v}(1 + \log |\kappa|) + \tfrac{3}{2}(P_d + P_O).$$
Here $\rho_z$ and $\rho_q$ are the numbers of $z$ vectors and of theta forms, and $P_v$, $P_{0v}$ and $P_O$ are constants of the setting.

Lean: `Formalism.MainNotions.Gaps.EtaleWeightGaps.rLa_tsum_le_comb`.

*Proof.* Three proved bounds are combined. The first bounds the sum of the constants $g_\lambda \, \mathrm{lN}(\lambda)$ by $\rho_z B |\kappa|$. The second bounds the sum of the quotient lengths, weighted by $\mathrm{lN}$, by $2 \rho_q P_v |\kappa|$. The third splits the sum of $r_\lambda \, \mathrm{lN}(\lambda)$ into the sums of its four parts, and shows that each part is summable. Linear arithmetic then gives the bound. $\square$

**Remark 4.9.5 (Formalization).** The pole length theorem asks for the lift condition at $T$, but that condition is not used: an example in [LengthPoleInLift.lean](lean:Formalism/PeriodIntegrals/LengthPoleInLift.lean#L17) derives the statement from the form without it. Its first name only reorders the hypotheses of the second, see [TheoremZeroBundledOfLift.lean](lean:Formalism/SharpRestriction/GenusPolyhedralBounds/RelativeIndexClassSets/TheoremZeroBundledOfLift.lean#L13), and the second is the pole length bound, see [LengthPoleInLift.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/LengthPoleInLift.lean#L4). In the local index lemma and the local bound the two length bounds are hypotheses, and other theorems supply them. In $r_\lambda$ and in the index, $I_\lambda$ and infinite lengths are read as $0$ through the integer part; the sum over places is controlled by a height condition that asks $I_\lambda$ to be finite. The level lemma, the reduction map, the étale level identity and the three summed bounds were not unfolded beyond their statements. We did not unfold the definitions of $\Theta$, $M^{\sup}$, $Q_m$, $g_\lambda$ and the weight $\kappa$. The theorems are in [JWMggWMem.lean](lean:Formalism/SharpRestriction/GenusPolyhedralBounds/RelativeIndexClassSets/JWMggWMem.lean#L70), [JWMggWMem.lean](lean:Formalism/SharpRestriction/GenusPolyhedralBounds/RelativeIndexClassSets/JWMggWMem.lean#L149) and [TheoremZeroSplitOfLocal.lean](lean:Formalism/SharpRestriction/GenusPolyhedralBounds/RelativeIndexClassSets/TheoremZeroSplitOfLocal.lean#L69). The constant $r_\lambda$ is defined in [PublishedIntClosHolds.lean](lean:Formalism/SharpRestriction/GenusPolyhedralBounds/RelativeIndexClassSets/PublishedIntClosHolds.lean#L371).
