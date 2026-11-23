---
id: om-sum-same-dat-le
title: The weight of the terms with one datum
kind: theorem
decl: GlobalTheory.DegCnt.omSum_sameDat_le
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.HermFrameWeightSumSameDatumLe
covers: 373
status: drafted
drafted_by: writer@claude
---
This theorem bounds the total weight of the $R$-orbits of terms that have one datum. Its statement form is [`hermFrame_weightSum_sameDatum_le`](/entry/herm-frame-weight-sum-same-datum-le/), which [`FixedForm.main`](/entry/fixed-form-main/) uses for each class of terms. The proof sorts the terms by two integer indices and calls a bound for each value of the indices, [`hermFramePair_omSum_same_datum_le`](/entry/herm-frame-pair-om-sum-same-datum-le/).

## Statement

The notation is that of [`FixedForm.main`](/entry/fixed-form-main/) and [the statement form](/entry/herm-frame-weight-sum-same-datum-le/). The statement is the same as there: for a term $\Lambda$ of level $g \geq 1$ and $Q(\Lambda')$ = "$\Lambda'$ is a term of level $g$ with the same datum as $\Lambda$",
$$\Omega(Q) \leq \Bigl(\frac{\Delta}{g_I(\Lambda)}\Bigr)^{k/2} \Delta^{c_K + 2} X, \qquad X = (\Delta_b \Delta N_T)^{10000 (r+1)^3},$$
with $c_K = 1 + \log_2 [K : \mathbb{Q}]$ and $k = \dim W_t$.

Two more indices of a lattice $\Lambda'$ enter the proof: $i_I(\Lambda') = [L_g(\Lambda') : L_\theta(\Lambda')]$ (`iI`), where $L_\theta$ is the lattice `latTh`, and an integer $b_I(\Lambda')$ (`bI`, defined by `bOne`), which we have not unfolded.

## Proof

1. By `flagPairDefiniteThetaLattice_le_fixed_index_bound`, each term $\Lambda'$ has $g_I, i_I \geq 1$ and $g_I\, i_I^2\, b_I^2 \leq \Delta$ and $g_I\, i_I \leq \Delta$. So $\Delta \geq 1$. By `normal_form_terminal_determinant`, $b_I(\Lambda') \neq 0$.
2. A term $\Lambda'$ with the same datum as $\Lambda$ has $g_I(\Lambda') = g_I(\Lambda)$, since $g_I$ depends only on $L$ and $\Gamma_g$. So the pair $(i_I(\Lambda'), b_I(\Lambda'))$ is in
$$S = \{(i, b) \in [1, \lfloor \Delta \rfloor]^2 : g_I(\Lambda)\, i^2 b^2 \leq \Delta\},$$
and $|S| \leq \lfloor \Delta \rfloor^2 \leq \Delta^2$.
3. Split $\Omega(Q)$ by the value of the pair (`tsum_ite_le_sum_fibres`). For each $(i, b) \in S$, [`hermFramePair_omSum_same_datum_le`](/entry/herm-frame-pair-om-sum-same-datum-le/) bounds the part by $(ib)^k\, i^{c_K} X$.
4. For $(i, b) \in S$, $(ib)^2 \leq \Delta / g_I(\Lambda)$ and $i \leq \Delta$. So $(ib)^k i^{c_K} X \leq (\Delta / g_I(\Lambda))^{k/2} \Delta^{c_K} X$ (`index_pair_bound`).
5. Sum over $S$: the factor $|S| \leq \Delta^2$ turns $\Delta^{c_K}$ into $\Delta^{c_K + 2}$.

The rest is bookkeeping with nonnegativity ($c_K \geq 0$ by `cf_nonneg_of_numberField`).

## In the Lean code

The theorem is in [HermFrameWeightSumSameDatumLe.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/HermFrameWeightSumSameDatumLe.lean#L48). It calls:

- `GlobalTheory.T.flagPairDefiniteThetaLattice_le_fixed_index_bound` and `GlobalTheory.T.normal_form_terminal_determinant`, for the index inequalities;
- `GlobalTheory.T.hermFramePair_omSum_same_datum_le`, for each pair $(i, b)$;
- `tsum_ite_le_sum_fibres`, `cf_nonneg_of_numberField` and `index_pair_bound`, elementary lemmas in the same file.

The real content is below, in [`OmCount.main`](/entry/om-count-main/). The bound loses a factor $\Delta^2$ for the count of pairs; no attempt is made to sharpen it.
