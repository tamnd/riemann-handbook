---
id: hodge-metric-chern-integral-eq-covolume-mul-flag-degree
title: The Chern integrals of the Hodge metric, restated
kind: theorem
decl: GlobalTheory.T.hodgeMetric_chernIntegral_eq_covolume_mul_flagDegree
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.HodgeMetricChernIntegralEqCovolumeMulFlagDegreeStatement
covers: 758
status: drafted
drafted_by: writer@claude
---
This theorem is a second name of [`hasChernIntegral_covol_flagDeg`](/entry/has-chern-integral-covol-flag-deg/). It has the same statement and no proof of its own. [The good base](/entry/exists-good-base/) uses it for its property 5: each Chern integral of the Hodge metric on the open part of the base is a covolume times a flag degree. The mathematics is in the entry of `hasChernIntegral_covol_flagDeg` and in the two lemmas below it.

## Statement

Use the setting and notation of [the good base](/entry/exists-good-base/): a Lie base $(X, j, f, f_0, \mathcal{E}, A_0)$ for the component $Y_k$ of a toroidal flag space, the open part $O = $ `openPart j`, and the metric $h = $ `lieGram`.

**Theorem.** For each weight $\lambda$ and each real polynomial $R$ in the Chern classes with $\operatorname{antisym}(Q_\lambda) = R(e)\,\Delta$,

$$\int_O R(h) = \operatorname{covol}(U_k)\cdot \deg_{\mathrm{Fl}}(\lambda).$$

## Proof

The proof is `first | exact @GlobalTheory.LieBase.hasChernIntegral_covol_flagDeg | …`. The first branch closes the goal, so the theorem is the other one under a new name.

## In the Lean code

The theorem is in [HodgeMetricChernIntegralEqCovolumeMulFlagDegreeStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/HodgeMetricChernIntegralEqCovolumeMulFlagDegreeStatement.lean#L8). Its statement is word for word the statement of `hasChernIntegral_covol_flagDeg` in [HodgeMetricChernIntegralEqCovolumeMulFlagDegree.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/HodgeMetricChernIntegralEqCovolumeMulFlagDegree.lean#L12). The name speaks of a "Hodge metric"; in the statement the metric is `lieGram`, which takes its values from the Hodge metric `hodgeMet` ([ExistsIsLieBase.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsIsLieBase.lean#L57)).
