---
id: om-count-main
title: The weight of the terms with one datum and fixed indices
kind: theorem
decl: GlobalTheory.DegCnt.OmCount.main
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.HermFramePairOmSumSameDatumLe
covers: 368
status: drafted
drafted_by: writer@claude
---
This theorem bounds the total weight of the $R$-orbits of terms with one datum and fixed indices $i_I = i$, $b_I = b$. Its statement form is [`hermFramePair_omSum_same_datum_le`](/entry/herm-frame-pair-om-sum-same-datum-le/), which [`omSum_sameDat_le`](/entry/om-sum-same-dat-le/) sums over the pairs $(i, b)$. The proof bounds the weight of one orbit and counts the orbits, and here the exponent $10000(r+1)^3$ of [`FixedForm.main`](/entry/fixed-form-main/) appears.

## Statement

The notation is that of [`FixedForm.main`](/entry/fixed-form-main/) and [`omSum_sameDat_le`](/entry/om-sum-same-dat-le/). Let $\Lambda$ be a term of level $g \geq 1$ and $i, b \in \mathbb{N}$. Let $Q(\Lambda')$ say that $\Lambda'$ is a term of level $g$ with the same datum as $\Lambda$, $i_I(\Lambda') = i$ and $b_I(\Lambda') = b$. Then
$$\Omega(Q) \leq (ib)^{k}\, i^{c_K}\, M^{10000 (r+1)^3}, \qquad M = \Delta_b \Delta N_T, \quad k = \dim W_t.$$

## Proof

Let $\Pi = W_t^\perp$; it has dimension $2r + 1$. A lattice $\Lambda'$ is *split* (`Split`) if $L_\theta(\Lambda') = (\Lambda' \cap W_t) + I$, where $I$ is the span `II` of the common part of the two flags. For an ideal $\mathfrak{m}$, $\Lambda'$ is *near* the reference lattice $P_0 \subset \Pi$ (`Near`) if $\mathfrak{m} P_0 \subseteq \Lambda' \cap \Pi$ and $\mathfrak{m}(\Lambda' \cap \Pi) \subseteq P_0$.

1. **An ideal.** By `exists_star_stable_ideal_absorbing_minors`, there is a nonzero ideal $\mathfrak{c}$, stable under the involution, divisible by $T$, that clears the denominators of the minors of $N$, with $\mathrm{N}\mathfrak{c} \leq (\Delta_b N_T)^2$. The same lemma gives $\Delta, \Delta_b \geq 1$. Put $e = 12r + 50$.
2. **A good representative in each orbit.** $R$ preserves $Q$ (`commonUnipotent_stabiliser_preserves_terms_and_datum`). By `hermFramePair_exists_unipotent_split_lattice`, each orbit has a split lattice. By `hermFramePairNormalForm_exists_conj_near_reference`, a further element of $R$ makes it also near $P_0$ for $\mathfrak{c}^e$. Let $S$ be the set of lattices with $Q$ that are split and near.
3. **The weight of one orbit.** The weight is $R$-invariant (`om_smul`). For $\Lambda' \in S$, `splitTermWeight_le_near_referenceLattice` gives $\omega(\Lambda') \leq b^k \Delta^r\, \mathrm{N}\mathfrak{c}^{2(3e+11)(2r+1)^2}$. So $\Omega(Q) \leq |S|$ times this bound (`tsum_orbits_le`).
4. **The count of $S$.** Map $\Lambda' \in S$ to the pair $(L_\theta(\Lambda'), \Lambda' \cap \Pi)$.
   - $L_\theta(\Lambda')$ lies between $I$ and $L_g(\Lambda)$ with index $i$. By `card_sublattices_definiteQuotient_normalForm_le`, there are at most $i^{k + c_K}$ such lattices.
   - $\Lambda' \cap \Pi$ is near $P_0$. By `encard_lattices_near_reference_lattice_le`, there are at most $\mathrm{N}\mathfrak{c}^{2e(2r+1)^2}$ such lattices.
   - In a fibre, $\Lambda'$ is unimodular with fixed $\Lambda' \cap W_t$ (it is $L_\theta \cap W_t$, by splitness) and fixed $\Lambda' \cap \Pi$. By `encard_unimodular_hermGluings_le`, there are at most $[A^\# : A]^{2r+1}$ such lattices, with $A = \Lambda' \cap W_t$. By `idx_dual_le`, $[A^\# : A] \leq (\Delta N_T)^2$.
5. **Arithmetic.** With $\mathrm{N}\mathfrak{c} \leq M^2$, $\Delta N_T \leq M$ and $M \geq 1$, the lemma `numeric` collects all powers of $M$ into $M^{10000(r+1)^3}$. If $S$ is empty, the bound is trivial; else $i \geq 1$.

## In the Lean code

The theorem is in [HermFramePairOmSumSameDatumLe.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/HermFramePairOmSumSameDatumLe.lean#L237). The lemmas `encard_le_of_fibres`, `tsum_orbits_le`, `idx_dual_sup`, `numeric`, `om_smul`, `isLatMod_latLa`, `inf_Wt_of_split` and `idx_dual_le` are in the same file. The other lemmas named above are `GlobalTheory.T.*` statement forms; we have not opened their proofs. `idx_dual_le` also uses `hermFramePairNormalForm_geometry_summary` and `DelScale.main`.

The existence of $\mathfrak{c}$ is stated in continuation form: "for each $Q$, if the properties of $\mathfrak{c}$ imply $Q$, then $Q$". That lemma also returns $1 \leq \Delta_b$ and $1 \leq \Delta$, which have nothing to do with $\mathfrak{c}$. The exponent $10000(r+1)^3$ is a crude upper bound for the true exponent $4e(2r+1)^2 + 2(2r+1) + r + 4(3e+11)(2r+1)^2$; `nlinarith` checks the inequality.
