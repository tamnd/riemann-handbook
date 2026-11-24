---
title: Orbit sums of weights over one datum
decls:
  - GlobalTheory.DegCnt.OmCount.main
  - GlobalTheory.T.hermFramePair_omSum_same_datum_le
  - GlobalTheory.DegCnt.omSum_sameDat_le
  - GlobalTheory.T.hermFrame_weightSum_sameDatum_le
  - GlobalTheory.DegAsm.FixedForm.main
  - GlobalTheory.T.sum_weights_inequivalent_hermFrameTerms_le
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Orbit sums of weights over one datum

This section sums the weights of the previous section over the orbits of $R$ on terms that share a datum. The first result fixes the two indices $i_I$ and $b_I$ and counts the orbits near the reference lattice. The second sums over all values of the indices. The third passes from orbit sums to finite families of terms that are pairwise inequivalent under $R$. The bounds are polynomial in $\Delta$, $D_b$ and $N_T$, with exponents that depend only on $r$, $\dim \widetilde W$ and $c_f$. They are used for the weights of frame classes in the next section, and so for the pair count of the [type bound](/entry/rows-pos-type-p/).

We keep the notation of [the weight of a split term](/entry/om-le/). Let $N$ be a normal form of length $r$ and let $g \ge 1$.

**Definition 2.2.1 (Same datum).** Two lattices $\Lambda_0$ and $\Lambda$ have the *same datum* at level $g$ if $L(\Lambda) = L(\Lambda_0)$, if the lattice $L'(\Lambda) = (X + X')^\perp \cap (\Lambda + X')$ built from the second flag agrees with $L'(\Lambda_0)$, and if the gluing graphs of $\Lambda$ and $\Lambda_0$ modulo $g$ agree.

The weight is constant on $R$-orbits, so it makes sense on the orbit space.

**Definition 2.2.2 (Orbit sum).** For a property $Q$ of lattices let
$$\Omega(Q) = \sum_{o \in R \backslash \{\text{lattices}\}} \mathbf{1}_{Q}(\Lambda_o)\, \omega(\Lambda_o) \in [0, \infty],$$
where $\Lambda_o$ is a chosen representative of the orbit $o$.

### Orbits with fixed indices

**Proposition 2.2.3 (Orbit sum with fixed indices).** Let $K$ be an unramified CM field, let $N$ be a normal form of length $r$, let $g \ge 1$ and let $\Lambda$ be a term of level $g$. For natural numbers $i$ and $b$ let $Q_{i,b}$ hold for the terms $\Lambda'$ of level $g$ with the same datum as $\Lambda$, $i_I(\Lambda') = i$ and $b_I(\Lambda') = b$. Then
$$\Omega(Q_{i,b}) \le (i b)^{\dim \widetilde W}\, i^{c_f}\, (D_b\, \Delta\, N_T)^{10000 (r+1)^3}.$$

Lean: `GlobalTheory.DegCnt.OmCount.main` (also `GlobalTheory.T.hermFramePair_omSum_same_datum_le`, a second name).

*Proof.* Choose an ideal $\mathfrak{c}$ that absorbs the minors and has $N\mathfrak{c} \le (D_b N_T)^2$. Such an ideal exists by a lemma on ideals that absorb the minors. We also have $D_b \ge 1$ and $\Delta \ge 1$. Put $e = 12r + 50$.

The sum over orbits is at most the sum over any set of lattices that meets every orbit with $Q_{i,b}$. Each such orbit contains a split term. By [the lemma on moving a term](/entry/normal-pos-exists-near/), it then contains a split term that is near $P_0$ at $\mathfrak{c}^e$. So $\Omega(Q_{i,b})$ is at most the number of such near split terms with the given datum and indices, times the largest weight among them.

The weight of each of them is at most $b^{\dim \widetilde W} \Delta^r N\mathfrak{c}^{2(3e+11)(2r+1)^2}$ by [the weight bound](/entry/om-le/). We count the near split terms in three steps:

1. the sublattices of the definite part with index $i$ number at most $i^{\dim \widetilde W + c_f}$;
2. the lattices on $\Pi$ that are near $P_0$ at $\mathfrak{c}^e$ number at most $N\mathfrak{m}^{2(2r+1)^2}$, for an ideal $\mathfrak{m}$ built from $\mathfrak{c}^e$;
3. the gluings of the two pieces number at most $x^{\dim U^\perp}$, where $U$ is the glued subspace and $x \le (\Delta N_T)^2$ is the index of a lattice in its dual.

The product of the weight bound and the three counts is a product of powers of $i$, $b$, $D_b$, $\Delta$ and $N_T$. With $N\mathfrak{c} \le (D_b N_T)^2$ and $e = 12r+50$, all exponents of $D_b$, $\Delta$ and $N_T$ are at most $10000(r+1)^3$. $\square$

### Orbits of one datum

**Theorem 2.2.4 (Orbit sum over one datum).** Let $K$ be an unramified CM field, let $N$ be a normal form of length $r$, let $g \ge 1$ and let $\Lambda$ be a term of level $g$. Let $Q$ hold for the terms of level $g$ with the same datum as $\Lambda$. Then
$$\Omega(Q) \le \Big(\frac{\Delta}{g_I(\Lambda)}\Big)^{\dim \widetilde W / 2} \Delta^{c_f + 2}\, (D_b\, \Delta\, N_T)^{10000 (r+1)^3}.$$

Lean: `GlobalTheory.DegCnt.omSum_sameDat_le` (also `GlobalTheory.T.hermFrame_weightSum_sameDatum_le`, a second name).

*Proof.* The index $g_I$ depends only on the datum, so $g_I(\Lambda') = g_I(\Lambda)$ for every $\Lambda'$ with $Q$. For such $\Lambda'$ the indices satisfy
$$g_I(\Lambda)\, i_I(\Lambda')^2\, b_I(\Lambda')^2 \le \Delta,$$
by a bound on the index pair of a term. So the pairs $(i, b)$ that occur lie in the finite set $S$ of pairs in $[1, \lfloor \Delta \rfloor]^2$ with $g_I i^2 b^2 \le \Delta$, and $|S| \le \Delta^2$.

Split $\Omega(Q)$ as the sum over $(i,b) \in S$ of $\Omega(Q_{i,b})$ and apply the previous proposition to each term. For $(i,b) \in S$ we have $(i b)^{\dim \widetilde W} \le (\Delta / g_I)^{\dim \widetilde W/2}$ and $i^{c_f} \le \Delta^{c_f}$. Multiplying by $|S| \le \Delta^2$ gives the claim. $\square$

### Inequivalent families

**Corollary 2.2.5 (Weights of inequivalent terms).** Let $K$ be an unramified CM field, let $N$ be a normal form of length $r$, let $g \ge 1$ and let $\Lambda_0$ be a term of level $g$. Let $(\Lambda_i)_{i \in s}$ be a finite family of terms of level $g$ such that for each $i \in s$:

1. $L(\Lambda_i) = L(\Lambda_0)$;
2. the definite part of $\Lambda_i$ for the pair $(F', F)$ equals that of $\Lambda_0$;
3. the gluing graph of $\Lambda_i$ modulo $g$ equals that of $\Lambda_0$;

and such that $\rho \Lambda_i = \Lambda_{i'}$ with $\rho \in R$ implies $i = i'$. Then
$$\sum_{i \in s} \omega(\Lambda_i) \le N_T^2 \Big(\frac{\Delta}{g_I(\Lambda_0)}\Big)^{\dim \widetilde W / 2} \Delta^{c_f + 2} (D_b\, \Delta\, N_T)^{10000 (r+1)^3}.$$

Lean: `GlobalTheory.DegAsm.FixedForm.main` (also `GlobalTheory.T.sum_weights_inequivalent_hermFrameTerms_le`, a second name).

*Proof.* Sort the family by the lattice $L'(\Lambda_i)$. Each $L'(\Lambda_i)$ is an inner lattice whose definite part is fixed by condition 2. A count of inner lattices with a given definite part and trace gives at most $N_T^2$ values of $L'(\Lambda_i)$.

Fix one value and pick $\Lambda_{i_0}$ in its fibre. Every $\Lambda_i$ in the fibre has the same datum as $\Lambda_{i_0}$, and the $\Lambda_i$ in the fibre lie in distinct $R$-orbits. The weight is constant on $R$-orbits, so the sum over the fibre is at most $\Omega(Q)$ for the datum of $\Lambda_{i_0}$. The index $g_I(\Lambda_{i_0})$ equals $g_I(\Lambda_0)$, since it depends only on $L$ and on the gluing graph. The theorem bounds each fibre, and the number of fibres is at most $N_T^2$. $\square$

**Remark 2.2.6 (Formalization).** The orbit sum is `GlobalTheory.DegCnt.NF.omSum`, a `tsum` over `MulAction.orbitRel.Quotient` with values in `ℝ≥0∞`; the representative is `Quotient.out`. Same datum is `NF.SameDat`, and $L'$ is `latL N.F' N.F`. The proof of the proposition ([HermFramePairOmSumSameDatumLe.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/HermFramePairOmSumSameDatumLe.lean#L237)) obtains $\mathfrak{c}$ from `exists_star_stable_ideal_absorbing_minors`, which is stated in continuation form: it takes the goal as a function of the ideal. It uses `tsum_orbits_le` and the dual index bound `idx_dual_le`, and it ends with a long arithmetic lemma `numeric`. The exponent $10000(r+1)^3$ is a crude common bound and is not tight. The proof of the theorem uses `index_pair_bound` ([HermFrameWeightSumSameDatumLe.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/HermFrameWeightSumSameDatumLe.lean#L48)); there $\Delta^{c_f+2}$ is a real power. The corollary uses `card_innerLattices_with_definite_trace_le_norm`, `sum_le_orbit`, the invariance `StabInv.main` and `WeightInf.main`. The second names are proved by a `first | exact ...` combinator under `set_option maxHeartbeats 1000000`.
