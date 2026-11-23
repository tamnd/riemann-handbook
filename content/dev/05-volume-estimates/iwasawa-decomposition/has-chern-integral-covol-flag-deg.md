---
id: has-chern-integral-covol-flag-deg
title: A Chern integral of the Hodge metric is a covolume times a flag degree
kind: theorem
decl: GlobalTheory.LieBase.hasChernIntegral_covol_flagDeg
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.HodgeMetricChernIntegralEqCovolumeMulFlagDegree
covers: 757
status: drafted
drafted_by: writer@claude
---
This theorem is the analytic core of [Mumford proportionality](/entry/mumford-proportionality-of-good-chern-weil/) in the Lean code. It computes each Chern integral of the metric `lieGram` on the open part of a Lie base: the value is $\operatorname{covol}(U_k)\deg_{\mathrm{Fl}}(\lambda)$. It goes to [its restatement](/entry/hodge-metric-chern-integral-eq-covolume-mul-flag-degree/) and from there to [the good base](/entry/exists-good-base/). The proof multiplies a pointwise identity of forms by one integral.

## Statement

Use the setting and notation of [the good base](/entry/exists-good-base/). Let $(X, j, f, f_0, \mathcal{E}, A_0)$ be a Lie base for the component $Y_k$ (`IsLieBase`), $O = $ `openPart j` and $h = $ `lieGram`. Write $\int_O R = t$ for `HasChernIntegral`: in each holomorphic chart, take the top-degree coefficient of $R$ evaluated on the Chern forms of the curvature of $h$, divided by $\pi^{\dim X}$; its positive part and its negative part have finite mass on $O(\mathbb{C})$, and the positive mass minus the negative mass is $t$.

**Theorem.** Assume `GoodEmb` and `IsUnf`. For each weight $\lambda$ and each real polynomial $R$ in the variables $c_j(\mathcal{E}_\tau)$ with $\operatorname{antisym}(Q_\lambda) = R(e)\,\Delta$, where $Q_\lambda = \bigl(-\sum_{\tau,i} e_\lambda(\tau,i)\,x_{\tau,i}\bigr)^{\dim Y_k}$,

$$\int_O R(h) = \operatorname{covol}(U_k)\cdot\deg_{\mathrm{Fl}}(\lambda).$$

## Proof

Let $P_0$ be the polynomial `pointPoly`,

$$P_0 = \prod_{\tau \in \Psi} \bigl((-1)^{m_\tau} c_{m_\tau}(\mathcal{E}_\tau)\bigr)^{N - m_\tau}, \qquad N = p + q.$$

1. [`hasChernIntegral_pointPoly_covol`](/entry/has-chern-integral-point-poly-covol/): $\int_O P_0(h) = \operatorname{covol}(U_k)$.
2. [`pointwise_hodge`](/entry/pointwise-hodge/): at each point of $O(\mathbb{C})$, in each chart and each frame, the top density of $R(h)$ is $\deg_{\mathrm{Fl}}(\lambda)$ times the top density of $P_0(h)$.
3. `hasChernIntegral_of_eq_mul`: if the density of $R$ is $t$ times the density of $R_0$ at each point of $O$, and $\int_O R_0 = v$, then $\int_O R = t v$. For $t < 0$ the lemma exchanges the positive and the negative parts.

Steps 1 to 3 give $\int_O R = \deg_{\mathrm{Fl}}(\lambda)\operatorname{covol}(U_k)$. The rest is `mul_comm`.

All the geometry is in steps 1 and 2. Step 2 is algebra in the Chern forms at one point, with one relation that is special to the Hodge metric. Step 1 is the volume computation.

## In the Lean code

The theorem is in [HodgeMetricChernIntegralEqCovolumeMulFlagDegree.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/HodgeMetricChernIntegralEqCovolumeMulFlagDegree.lean#L12). The lemmas:

- `GlobalTheory.LieBase.hasChernIntegral_pointPoly_covol`, in [HasChernIntegralPointPolyCovol.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/HasChernIntegralPointPolyCovol.lean#L15).
- `GlobalTheory.PointHodge.pointwise_hodge`, in [PointwiseHodge.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/PointwiseHodge.lean#L32).
- `GlobalTheory.GoodMetric.hasChernIntegral_of_eq_mul`, in [HasChernIntegralOfEqMul.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/HasChernIntegralOfEqMul.lean#L80). It is proved in the same file, from the fact that a glued chart measure scales with its density (`glueMeas_restrict_eq`).
- `pointPoly` is defined in [PointPoly.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/PointPoly.lean#L14).

The proof ends with `convert h using 3`. We have not checked which terms differ. The goodness of the metric (`IsGood`) is not used here: the theorem holds for the metric `lieGram` directly, not for an arbitrary good metric.
