---
id: herm-frame-pair-om-sum-same-datum-le
title: The weight of the terms with one datum and fixed indices, statement form
kind: theorem
decl: GlobalTheory.T.hermFramePair_omSum_same_datum_le
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.HermFramePairOmSumSameDatumLeStatement
covers: 369
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [`OmCount.main`](/entry/om-count-main/). Its only user is [`omSum_sameDat_le`](/entry/om-sum-same-dat-le/), in step 3 of its proof, where it bounds the weight for each value of the pair of indices $(i_I, b_I)$. The content is in [`OmCount.main`](/entry/om-count-main/).

## Statement

The notation is that of [`FixedForm.main`](/entry/fixed-form-main/) and [`omSum_sameDat_le`](/entry/om-sum-same-dat-le/).

**Theorem.** Let $K$ satisfy `IsCMUnram`, $N$ a normal form of length $r$, $g \geq 1$, and $\Lambda$ a term of level $g$. Let $i, b \in \mathbb{N}$. Let $Q(\Lambda')$ say that $\Lambda'$ is a term of level $g$ with the same datum as $\Lambda$, with $i_I(\Lambda') = i$ and $b_I(\Lambda') = b$. Then
$$\Omega(Q) \leq (ib)^{k}\, i^{c_K}\, (\Delta_b \Delta N_T)^{10000 (r+1)^3}, \qquad k = \dim W_t.$$

The bound does not depend on $g_I(\Lambda)$; the parent entry brings $g_I$ in through the condition $g_I\, i^2 b^2 \leq \Delta$.

## Proof

The proof is the term `GlobalTheory.DegCnt.OmCount.main`. There is nothing else.

## In the Lean code

The theorem is in [HermFramePairOmSumSameDatumLeStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/HermFramePairOmSumSameDatumLeStatement.lean#L11). The proof is the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)` with `maxHeartbeats` set to 1,000,000. The two statements are the same, so the first alternative fits. For $i = 0$ the right side is $0$, since $c_K \geq 1$. This is consistent: each term has $i_I \geq 1$ and $b_I \geq 1$, by the lemmas in step 1 of the proof of [`omSum_sameDat_le`](/entry/om-sum-same-dat-le/).
