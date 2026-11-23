---
id: herm-frame-weight-sum-same-datum-le
title: The weight of the terms with one datum, statement form
kind: theorem
decl: GlobalTheory.T.hermFrame_weightSum_sameDatum_le
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.HermFrameWeightSumSameDatumLeStatement
covers: 374
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [`omSum_sameDat_le`](/entry/om-sum-same-dat-le/). Its only user is [`FixedForm.main`](/entry/fixed-form-main/), in step 3 of its proof, where it bounds the weight of one class of terms. The content is in [`omSum_sameDat_le`](/entry/om-sum-same-dat-le/) and below it.

## Statement

The notation is that of [`FixedForm.main`](/entry/fixed-form-main/). For a property $Q$ of $\mathcal{O}_K$-lattices, let
$$\Omega(Q) = \sum_{o \in R \backslash \{\text{lattices}\}} \mathbf{1}_{Q(\Lambda_o)}\, \omega(\Lambda_o) \in [0, \infty],$$
where $\Lambda_o$ is a chosen lattice in the $R$-orbit $o$ (`NF.omSum`). Two lattices have the *same datum* at level $g$ (`SameDat`) if they have equal $L$, equal $L'$ and equal graph $\Gamma_g$.

**Theorem.** Let $K$ satisfy `IsCMUnram`, $N$ a normal form of length $r$, $g \geq 1$, and $\Lambda$ a term of level $g$. Let $Q(\Lambda')$ say that $\Lambda'$ is a term of level $g$ with the same datum as $\Lambda$. Then
$$\Omega(Q) \leq \Bigl(\frac{\Delta}{g_I(\Lambda)}\Bigr)^{k/2} \Delta^{c_K + 2} (\Delta_b \Delta N_T)^{10000 (r+1)^3}.$$

## Proof

The proof is the term `GlobalTheory.DegCnt.omSum_sameDat_le`. There is nothing else.

## In the Lean code

The theorem is in [HermFrameWeightSumSameDatumLeStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/HermFrameWeightSumSameDatumLeStatement.lean#L11). The proof is the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)` with `maxHeartbeats` set to 1,000,000. The two statements are the same, so the first alternative fits. The right side is a real number put into $[0, \infty]$ with `ENNReal.ofReal`. `omSum` and `SameDat` are in [NormalFormDualOrthogonalLast.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/NormalFormDualOrthogonalLast.lean#L112). The file imports `Mathlib` twice.
