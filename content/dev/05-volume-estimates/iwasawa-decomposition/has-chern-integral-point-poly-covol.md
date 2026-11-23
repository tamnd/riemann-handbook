---
id: has-chern-integral-point-poly-covol
title: The Chern integral of the point polynomial is the covolume
kind: theorem
decl: GlobalTheory.LieBase.hasChernIntegral_pointPoly_covol
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.HasChernIntegralPointPolyCovol
covers: 353
status: drafted
drafted_by: writer@claude
---
This theorem computes one Chern integral of the metric `lieGram` on the open part of a Lie base: the integral of the polynomial $P_0$ = `pointPoly` is the covolume $\operatorname{covol}(U_k)$. It is step 1 of [the Chern integrals of the Hodge metric](/entry/has-chern-integral-covol-flag-deg/), which multiplies it by the pointwise factor $\deg_{\mathrm{Fl}}(\lambda)$ of [`pointwise_hodge`](/entry/pointwise-hodge/). The proof joins two lemmas: the form is nonnegative, and its mass is the covolume.

## Statement

Use the setting and notation of [the Chern integrals of the Hodge metric](/entry/has-chern-integral-covol-flag-deg/): a Lie base $(X, j, f, f_0, \mathcal{E}, A_0)$ for $Y_k$, $O = $ `openPart j`, $h = $ `lieGram`, and

$$P_0 = \prod_{\tau \in \Psi} \bigl((-1)^{m_\tau} c_{m_\tau}(\mathcal{E}_\tau)\bigr)^{N - m_\tau}.$$

**Theorem.** Assume `GoodEmb` and `IsUnf`. Then $\int_O P_0(h) = \operatorname{covol}(U_k)$ in the sense of `HasChernIntegral`.

## Proof

1. `chernTop_pointClass_hodge_metric_lie_nonneg`: at each point $y$ of $O(\mathbb{C})$, in each chart at $y$ and each frame at $y$, the top density of $P_0(h)$ is $\ge 0$.
2. `chernTopForm_negativePart_eq_zero_of_nonneg_on_open`: a density that is $\ge 0$ on $O$ has a negative part of mass $0$ on $O$.
3. `hodgeMetric_pointClassForm_mass_eq_covolume`: the positive part has mass $\operatorname{covol}(U_k)$ on $O$.
4. `covol_pos`: $\operatorname{covol}(U_k) > 0$.

So both masses are finite, and the signed integral is $\operatorname{covol}(U_k) - 0$. The rest is bookkeeping with `ENNReal.toReal_ofReal`.

## In the Lean code

The theorem is in [HasChernIntegralPointPolyCovol.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/HasChernIntegralPointPolyCovol.lean#L15). The three lemmas of steps 1 to 3 are second names:

- `GlobalTheory.T.chernTop_pointClass_hodge_metric_lie_nonneg` restates `GlobalTheory.PointFormSign.chernTop_pointPoly_lieGram_nonneg` ([statement](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ChernTopPointClassHodgeMetricLieNonnegStatement.lean#L9)).
- `GlobalTheory.T.chernTopForm_negativePart_eq_zero_of_nonneg_on_open` restates `GlobalTheory.chernTopPart_neg_eq_zero_of_nonneg` ([statement](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ChernTopFormNegativePartEqZeroOfNonnegOnOpenStatement.lean#L8)). It holds for any metric and any polynomial.
- `GlobalTheory.T.hodgeMetric_pointClassForm_mass_eq_covolume` restates `GlobalTheory.BaseVolume.mass_openPart_eq_covol` ([statement](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/HodgeMetricPointClassFormMassEqCovolumeStatement.lean#L9)).
- `GlobalTheory.TrueCx.covol_pos`.

We have not unfolded the proofs of `chernTop_pointPoly_lieGram_nonneg` and `mass_openPart_eq_covol`. They hold the content: the sign of the form $P_0(h)$ and the computation of its mass as a covolume. The lemma names call $P_0$ the "point class". We have not checked this in Lean; the statement only says what is above.
