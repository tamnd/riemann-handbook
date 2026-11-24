---
title: The type bound
decls:
  - GlobalTheory.TypeAsm.pair_count_bound_of_siegel_mass
  - GlobalTheory.T.termPairCountBound_of_siegelMassRatios
  - GlobalTheory.TypeAsm.TopGap.typeBound_of_gap
  - GlobalTheory.T.typeBound_of_largeGap_discreteSeries_bessel
  - GlobalTheory.rowsPos_typeP
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The type bound

This section proves the type bound. Fix two row indices and two labels, and take a finite set of pairs of relevant terms with these indices and labels. The type bound says that the sum over the pairs of the products of the norms of the two term vectors is at most the local Bessel dimension times the row mass times an explicit product of factors. The proof has two halves. The first half is the [amplitude bound at terms](/entry/amplitude-bound-of-local-data-of-tail-bound/): each norm is at most a weight times an amplitude factor. The second half is a pair count: the weighted number of pairs is at most the row mass times a second factor. We prove the pair count here from two mass formulas for Hermitian lattices and the counts of the earlier sections. The type bound is used in the step [HypsAlt is nonempty from the closed bound](/step/nonempty-hyps/).

We keep the setting of the [previous section](/entry/amplitude-bound-of-local-data-of-tail-bound/): a datum $D$ with host field $E$, the ranks $k$, $r$, $m = 2r + 2$ and the number $f$ of infinite places, size data with the parameter $b$, a setting $X$, a family $Y$ and a word $u$. Each relevant term $t$ has a vector $a_t$, a weight $\mathrm{wt}(t)$, a row index $j(t)$, a label $\delta(t)$ and the weight $\omega(t)$ of [the frame class section](/entry/sum-cls-om-le-dat-bd/). Let $d_\pi(u)$ be the Bessel dimension and let $m_{\mathrm{row}}(u)$ be the row mass of [the genus mean section](/entry/rows-mean/).

For a row index $j$ and a label $\delta$, let $\Delta(j, \delta) \ge 0$ be the norm of the local ideal of $\delta_j$, as in [the frame class section](/entry/sum-cls-om-le-dat-bd/). For $H_1 > 0$ and an infinite place $\tau$ let $\sigma_\tau(j, \delta)$ be the maximum of $1$ and of the numbers $|\delta_l|_\tau / (2H_1)^{2r}$ over the indices $1 \le l \le j$ with $\delta_l \ne 0$, and let $\sigma(j, \delta) = \prod_\tau \sigma_\tau(j, \delta) \ge 1$. In the type bound $H_1 = b^{C_H m}$ for a constant $C_H$. Put $H_b(C) = b^{C m^2 f}$.

**Definition 2.10.1 (Amplitude and pair factors).** For constants $C_H, C_s, C, C_h, C_p$ put
$$A(C_H, C_s, C; j, \delta) = \Big(\frac{C}{k}\Big)^{j(k-1-j)f}\, \Delta^{-\frac{k-1-j}{2}}\, H_b(C)^{C r^4}\, \sigma^{-C_s k},$$
$$E(C_H, C_h, C_p; j, \delta) = \Delta^{k/2}\, H_b(C_h)^{C_h r^4}\, \sigma^{C_p k},$$
with $\Delta = \Delta(j, \delta)$ and $\sigma = \sigma(j, \delta)$ computed with $H_1 = b^{C_H m}$.

In a product $A \cdot E$ the powers of $\Delta$ nearly cancel, and the power of $\sigma$ is $\sigma^{-(C_s - C_p)k}$. This is why the type bound asks $C_s \ge C_p + 4$.

**Definition 2.10.2 (Type bound).** The type bound is the following statement. For all constants $C_g, c_b, C_w, c_T, C_T, C_0$ with $c_b > 0$ and $c_T > 0$ there are $C_H, C_h, C_p \ge 0$ such that for every $C_s \ge C_p + 4$ there is $C_\ast$ such that for every $C \ge C_\ast$ there are thresholds $C'_\ast, C_{l\ast}$ with this property. Let $C' \ge C'_\ast$ and $C_l \ge C_{l\ast}$. Let $D$ be a datum with ties, with size data that satisfy the $k_2$ hypotheses for $(C', C_l, C_g, c_b, C_w, c_T, C_T, C_0)$, and let $X$, $Y$, $u$ be as above, with the concentration tie. Let $1 \le j', j'' \le r$, let $\delta', \delta''$ be labels, and let $S$ be a finite set of pairs $(t_1, t_2)$ of relevant terms with $j(t_1) = j'$, $\delta(t_1) = \delta'$, $j(t_2) = j''$ and $\delta(t_2) = \delta''$. Then
$$\sum_{(t_1, t_2) \in S} \|a_{t_1}\|\, \|a_{t_2}\| \le d_\pi(u)\, m_{\mathrm{row}}(u)\, (A' E')\, (A'' E''),$$
where $A' = A(C_H, C_s, C; j', \delta')$, $E' = E(C_H, C_h, C_p; j', \delta')$, and $A''$, $E''$ are the same with $(j'', \delta'')$.

**Definition 2.10.3 (Pair count bound).** The pair count bound is the following statement. For all constants $C_g, c_b, C_w, c_T, C_T, C_0$ and every $C_H \ge 0$ there are $C_h, C_p \ge 0$ and thresholds $C'_\ast, C_{l\ast}$ such that for all $C' \ge C'_\ast$ and $C_l \ge C_{l\ast}$ the following holds. For every datum $D$ with size data that satisfy the $k_2$ hypotheses for these constants, every $X$, $Y$ with the concentration tie and every word $u$, and for $j', j'', \delta', \delta'', S$ as in the type bound,
$$\sum_{(t_1, t_2) \in S} \mathrm{wt}(t_1)\, \mathrm{wt}(t_2)\, \omega(t_1)\, \omega(t_2) \le m_{\mathrm{row}}(u)\, E'\, E''.$$

The pair count rests on two statements about masses of Hermitian lattices over a CM field. Let $K$ be a number field with an involution. We say that $K$ is an *unramified CM field* if $K$ is totally complex, every embedding $K \to \mathbb{C}$ carries the involution to complex conjugation, and for every maximal ideal $P$ there is $\theta \in \mathcal{O}_K$ with $\theta - \bar\theta \notin P$. For a [Hermitian form](/learn/algebra/#hermitian-and-skew-hermitian-forms) $h$ and an $\mathcal{O}_K$-lattice $L$, the mass $\mathrm{mass}(h, L)$ is the sum of $1/\#\operatorname{Aut}(M)$ over representatives $M$ of the classes in the genus of $L$ (see [genus and class](/learn/hermitian-lattices/#genus-class-and-spinor-genus) and [the mass formula](/learn/hermitian-lattices/#the-mass-formula-for-unitary-groups)). Let $v = |d_K|^{1/(2f)}/2$, where $f$ is the number of infinite places of $K$.

**Definition 2.10.4 (Maximal mass formula).** The maximal mass formula is the statement: for every unramified CM field $K$ and every $n \ge 1$ there is a constant $c$ such that for every [[positive definite|0KX66CZMBB]] Hermitian space $(V, h)$ over $K$ of dimension $n$ and every maximal integral lattice $M$ in $V$,
$$\mathrm{mass}(h, M) = c \prod_{P} \frac{q_P^{\,n} - (-1)^n}{q_P + 1},$$
where $P$ runs over the maximal ideals at which $M$ is not unimodular, and $q_P = \lfloor \sqrt{N P} \rfloor$.

**Definition 2.10.5 (Siegel mass ratio).** The Siegel mass ratio is the statement: for every unramified CM field $K$, every $M \ge 3$, and Hermitian lattices $L$ and $L'$ with orthonormal bases of sizes $M$ and $M - 1$,
$$\frac{\mathrm{mass}(h, L)}{\mathrm{mass}(h', L')} = \frac{\big((M-1)!\,(v/\pi)^M\big)^f}{\sqrt{(2v)^f}} \prod_P \varepsilon_P(M),$$
where the product is over the maximal ideals $P$, with $\varepsilon_P(M) = \big(1 - (-1)^M N P^{-M/2}\big)^{-1}$ if $\bar P = P$, and $\varepsilon_P(M) = (1 - N P^{-M})^{-1/2}$ otherwise.

Both statements are forms of the classical mass formula for unitary groups. In the pair count we take them as hypotheses. Both are proved elsewhere in the development, and the last theorem of this section uses these proofs.

**Theorem 2.10.6 (Pair count from the mass formulas).** The maximal mass formula and the Siegel mass ratio imply the pair count bound.

Lean: `GlobalTheory.TypeAsm.pair_count_bound_of_siegel_mass` (also `GlobalTheory.T.termPairCountBound_of_siegelMassRatios`, a second name).

*Proof.* Fix the constants and $C_H \ge 0$. Put $C_a = \max(1, 2(C_H + 1), C_T)$. An arithmetic lemma, described in the third step below, gives for this $C_a$ constants $C_h \ge 0$ and $C_{l1}$. We take this $C_h$, $C_p = 16$, $C'_\ast = 1$ and $C_{l\ast} = \max(1, C_{l1})$. Fix $C' \ge C'_\ast$, $C_l \ge C_{l\ast}$, the data $D, X, Y, u$, the indices, the labels and the set $S$. If $S$ is empty, the left side is $0$, and the right side is nonnegative since the row mass and the pair factors are nonnegative. So let $S$ be nonempty.

First, the sizes. The arithmetic conditions on the host field give that $f$ is the number of infinite places of $E$. The $k_2$ hypotheses give the size relations: $m = 2r + 2$, $C_l \le m$, $m^4 \le f$, $m^5 f \le k$, $C_l m^2 \log b \le k$, $\log f \le \sqrt r$, $2 \le b$, $1 \le v$, $2v \le b$, $(kb)^8 \le g$ for the integer $g$ of the setting, and $1 \le T_u \le b^{C_a m}$ for the prime $T_u$ of the word.

Second, the sizes of the norms. For each relevant term $t$ with index $j$ and label $\delta$, a lemma on relevant terms gives $\Delta(j, \delta) \ge 1$ and $1 \le D_b(j, \delta)$, where $D_b$ is the product of the norms of the local ideals of the nonzero $\delta_l$, and
$$\Delta(j, \delta) \le H_b(2(C_H + 1))\, \sigma(j, \delta)^2, \qquad D_b(j, \delta) \le \big(H_b(2(C_H + 1))\, \sigma(j, \delta)^2\big)^r.$$
Since $2(C_H + 1) \le C_a$, both bounds hold with $H_b(C_a)$ in place of $H_b(2(C_H + 1))$. We apply this to the first term of a pair in $S$ and to its second term. So the bounds hold for $(j', \delta')$ and for $(j'', \delta'')$.

Third, the arithmetic lemma. Let $B$ be the datum bound of [the frame class section](/entry/sum-cls-om-le-dat-bd/) and $P$ the pair bound of [the pairs over one row lattice](/entry/per-row-c/). Write $\Delta' = \Delta(j', \delta')$, $D'_b = D_b(j', \delta')$, $\sigma' = \sigma(j', \delta')$, and the same with two primes. The lemma says: for $C_a \ge 1$ there are $C_h \ge 0$ and $C_{l1}$ such that under the size relations of the first step and the bounds of the second step,
$$\begin{aligned}
\sum_{x=1}^{\lfloor \Delta' \rfloor} \sum_{x'=1}^{\lfloor \Delta'' \rfloor} {}& P(k, g, r, T_u, x, x')\, B(k, r, \Delta', D'_b, N_T, x)\, B(k, r, \Delta'', D''_b, N_T, x') \\
&\le E'\, E'',
\end{aligned}$$
where $N_T = T_u^f$, and $E'$, $E''$ are the pair factors with $C_p = 16$. The proof is a direct estimate. Each factor of $P$ and of $B$ is a power of $b$, of $\Delta$ or of $\sigma$, and the size relations bound each exponent. The factors $(x x')^{k/2}$ of $P$ and $(\Delta'/x)^{k/2}$, $(\Delta''/x')^{k/2}$ of the two datum bounds combine to $(\Delta' \Delta'')^{k/2}$.

Fourth, the definite space. The setting gives a Hermitian subspace $W$ of dimension $k$ whose inclusion is an embedding along the first flag $F_0$, with $H_W$ positive definite.

Fifth, the counts. The [term pairs over a row lattice](/entry/term-pairs-row-lattice-counted-via-embeddings/) bound the weighted sum over the pairs that share a row lattice by a sum over $x, x'$ of the numbers of pair triples times the two datum bounds. The [genus mean in the term setting](/entry/genus-mean-embedded-pairs-le-mass-mul-pair-bound/) bounds the orbit sum of the numbers of pair triples over the genus of each base lattice by the mass of the genus times $P(k, g, r, T_u, x, x')$. This is the only step that uses the maximal mass formula and the Siegel mass ratio. The [rows mean bound](/entry/rows-mean-c-holds/) turns these genus bounds into a bound by the row mass. Together, in $[0, \infty]$,
$$\begin{aligned}
\sum_{(t_1, t_2) \in S} {}& \mathrm{wt}(t_1)\, \mathrm{wt}(t_2)\, \omega(t_1)\, \omega(t_2) \\
&\le m_{\mathrm{row}}(u) \sum_{x, x'} P(\dots, x, x')\, B(\dots, x)\, B(\dots, x'),
\end{aligned}$$
with the sums and arguments of the third step. All terms are finite and nonnegative, so the inequality holds in $\mathbb{R}$.

Finally, the third step bounds the double sum by $E' E''$. Multiply by $m_{\mathrm{row}}(u) \ge 0$. $\square$

**Theorem 2.10.7 (Type bound from the gap hypotheses).** Assume the gap hypotheses at the infinite places and the Bessel realization of Whittaker functions. Then the type bound holds.

Lean: `GlobalTheory.TypeAsm.TopGap.typeBound_of_gap` (also `GlobalTheory.T.typeBound_of_largeGap_discreteSeries_bessel`, a second name).

The gap hypotheses are a bundle of four facts on [discrete series](/learn/representations/#discrete-series) representations of a [unitary group](/learn/groups/#unitary-groups) $U(p, q)$ with a large gap in the Harish-Chandra parameter: a branching support fact, uniqueness of Bessel models, a multiplicity one fact for the lowest $K$-type, and a fact on the formal degree. The Bessel realization says that, under a gap condition, a square integrable equivariant function $W$ that is fixed by convolution with a matrix coefficient of a discrete series $\sigma$ has the form $W(x) = \ell(\sigma(x) w)$ for a Bessel functional $\ell$ and a vector $w$.

*Proof.* The Bessel realization gives the local data statement of the [amplitude bound at terms](/entry/amplitude-bound-of-local-data-of-tail-bound/). The gap hypotheses give the tail statement, in closed form for large gaps. So that theorem gives the amplitude bound. The maximal mass formula and the Siegel mass ratio are proved in the development, so the previous theorem gives the pair count bound.

Now combine the two bounds. Fix the constants. The amplitude bound gives $C_H \ge 0$. The pair count bound at this $C_H$ gives $C_h, C_p \ge 0$ and thresholds $C'_2, C_{l2}$. Let $C_s \ge C_p + 4$. Then $C_s \ge 0$, and the amplitude bound gives $C_\ast$. For $C \ge C_\ast$ it gives thresholds $C'_1, C_{l1}$. Put $C'_\ast = \max(C'_1, C'_2)$ and $C_{l\ast} = \max(C_{l1}, C_{l2})$. Fix the data and a set $S$ as in the type bound. For a pair $(t_1, t_2) \in S$, the amplitude bound at both terms gives
$$\|a_{t_1}\|\, \|a_{t_2}\| \le d_\pi(u)\, A' A'' \cdot \mathrm{wt}(t_1)\, \mathrm{wt}(t_2)\, \omega(t_1)\, \omega(t_2),$$
since $\sqrt{d_\pi(u)}^{\,2} = d_\pi(u)$ and the indices and labels of $t_1$ and $t_2$ are $(j', \delta')$ and $(j'', \delta'')$. The factor $d_\pi(u) A' A''$ is nonnegative. Sum over $S$ and apply the pair count bound:
$$\sum_{(t_1, t_2) \in S} \|a_{t_1}\|\, \|a_{t_2}\| \le d_\pi(u)\, A' A''\, m_{\mathrm{row}}(u)\, E' E''.$$
This is the type bound. $\square$

**Theorem 2.10.8 (Type bound).** The type bound holds.

Lean: `GlobalTheory.rowsPos_typeP`.

*Proof.* Uniqueness of Bessel models for discrete series with a large gap, and the Bessel realization of Whittaker functions, are proved in the development. Uniqueness, together with three further proved facts (the branching support fact from the Zuckerman gap, the multiplicity one fact and the formal degree fact), gives the gap hypotheses. The previous theorem gives the type bound. $\square$

**Remark 2.10.9.** The constant $C_p = 16$ of the pair count comes from the arithmetic lemma. The condition $C_s \ge C_p + 4$ is not used in the proof of the type bound beyond $C_s \ge 0$. The users of the type bound need it: there $A' E'$ has the factor $\sigma(j', \delta')^{-(C_s - C_p)k} \le \sigma(j', \delta')^{-4k}$. We have not checked how they use it.

**Remark 2.10.10 (Formalization).** The type bound is `TypeP` with the inner inequality `TypeAt`, the pair count bound is `PairsP` with `PairsAt`, and the amplitude and pair factors are `k2a` and `k2e` (KappaEndpoints.lean, lines 2965 and 2969). `TypeP` is defined twice with the same body: as `Formalism.L2.SG.RowsPos.TypeP` ([RowsPos.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RowsPos.lean#L18)) and as `GlobalTheory.TypeAsm.TypeP` ([PerRowC.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/PerRowC.lean#L30)); `typeBound_of_amplitude_pairs` proves the second, and `typeBound_of_gap` states the first, so the final `exact` unfolds one into the other. In `pair_count_bound_of_siegel_mass` the concentration tie is introduced as `_` and not used ([TermPairCountBoundOfSiegelMassRatios.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/TermPairCountBoundOfSiegelMassRatios.lean#L81)); the pair count also asks neither $c_b, c_T > 0$ nor the ties of $D$. The steps of the proof are `parameter_size_constraints`, `relevantTerm_norms_ge_one_and_bounded`, `sum_pairBd_mul_datBd_le` (with $C_h = 300000\, C_a$ and $C_{l1} = 42\, C_a$), `definite_quotient_model_exists` and `weightedTermPairs_sum_le_via_rows_genusMeans`; the passage from `ℝ≥0∞` to `ℝ` is the private lemma `le_mul_sum_sum_of_ofReal_le_ennreal_sum`. The maximal mass formula is `GlobalTheory.Mass.MaxMass` ([MaxMass.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/DiscreteSeriesUnitary₂/MaxMass.lean#L10)), with the product written as `lamMax` and $q_P$ as `Nat.sqrt` of the absolute norm, so $q_P$ is a floor for primes of odd norm exponent. The Siegel mass ratio is `Formalism.HermitianLatticesTheory.SiegelMassRatio` ([StatementMass.lean](lean:Formalism/HermitianLattices/StatementMass.lean#L67)); it asks only that the forms be Hermitian, not definite, and its Euler product is a `tprod`. Their proofs used here are `GlobalTheory.Mass.MaxFormula.main` and `GlobalTheory.Mass.siegelMassRatio_holds`. The gap hypotheses are `GlobalTheory.GapIn.Hyp`, built by `hyp_of_uniqGap` from `UniqGap`, and the Bessel realization is `BesselOfW`; the local data and tail statements come from `locDatC_of_besselOfW` and `localDataTailBound_closedForm_largeGaps`. The second names are wrappers of the form `first | exact @X | exact X | ...`.
