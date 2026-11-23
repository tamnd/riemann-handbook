---
title: Chern integrals of the Hodge metric
decls:
  - GlobalTheory.LieBase.hasChernIntegral_pointPoly_covol
  - GlobalTheory.LieBase.hasChernIntegral_covol_flagDeg
  - GlobalTheory.T.hodgeMetric_chernIntegral_eq_covolume_mul_flagDegree
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Chern integrals of the Hodge metric

This section puts the two previous sections together. It defines the Chern integral of a polynomial over an open set, as a difference of two finite masses, and proves that the Chern integral of $R$ for the Hodge metric over the open part of a Lie base is $\operatorname{covol}(U_k) \cdot \deg_{\mathrm{Fl}}(\lambda)$. This is the analytic half of the main theorem. The other half, that Chern integrals of good metrics are intersection numbers, is the hypothesis of [the proportionality theorem](/entry/mumford-proportionality-of-good-chern-weil/), and the bridge is [the good base](/entry/exists-good-base/).

**Definition 7.4.1 (Chern integral).** Let $h$ be a Hermitian metric on a framed family $\mathcal{E}$ over $X$, let $O \subseteq X$ be open, let $R \in \mathbb{R}[c_{\tau,k}]$ and $t \in \mathbb{R}$. We say that *$R$ has Chern integral $t$ on $O$*, and write $\int_O R(c(h)) = t$, if the [Chern measures](/entry/mass-open-part-eq-covol/) satisfy
$$\mu_R^+\bigl(O(\mathbb{C})\bigr) < \infty, \qquad \mu_R^-\bigl(O(\mathbb{C})\bigr) < \infty, \qquad \mu_R^+\bigl(O(\mathbb{C})\bigr) - \mu_R^-\bigl(O(\mathbb{C})\bigr) = t.$$

The value $t$ is determined by $R$, $h$ and $O$: if $\int_O R(c(h)) = t$ and $\int_O R(c(h)) = t'$, then $t = t'$. The definition asks for absolute convergence. On a non-compact $O(\mathbb{C})$ this is the point of the growth conditions of Mumford: a good metric has Chern forms of finite mass.

**Lemma 7.4.2 (Proportional densities).** Let $R, R_0 \in \mathbb{R}[c_{\tau,k}]$ and $s \in \mathbb{R}$. Suppose that for each $y \in O(\mathbb{C})$, each algebraic chart $\phi$ at $y$ and each frame $A \in S(y)$,
$$\rho_R(h_A \circ \phi^{-1})(\phi(y)) = s\, \rho_{R_0}(h_A \circ \phi^{-1})(\phi(y)).$$
If $\int_O R_0(c(h)) = t$, then $\int_O R(c(h)) = s\,t$.

*Proof.* If $s \geq 0$, the densities give $\mu_R^\pm = s\,\mu_{R_0}^\pm$ on $O(\mathbb{C})$. If $s < 0$, they give $\mu_R^\pm = |s|\,\mu_{R_0}^\mp$. In both cases the masses are finite and their difference is $s\,t$. $\square$

**Theorem 7.4.3 (Chern integral of the point class).** Let $X, j, f, \mathcal{E}, A_0$ be a Lie base for $Y_k$, with open part $O$ and Hodge metric $h$. Then
$$\int_O P_0(c(h)) = \operatorname{covol}(U_k).$$

Lean: `GlobalTheory.LieBase.hasChernIntegral_pointPoly_covol`.

*Proof.* The top density of $P_0$ for the Hodge metric is nonnegative at each point of $O(\mathbb{C})$, in each algebraic chart and each frame: in the coordinates of the bounded domain it is the positive function of [the density on the domain](/entry/chern-top-domain/), and a holomorphic change of chart multiplies it by $|\det|^2 \geq 0$. So $\mu_{P_0}^-(O(\mathbb{C})) = 0$. The [mass of the point class](/entry/mass-open-part-eq-covol/) gives $\mu_{P_0}^+(O(\mathbb{C})) = \operatorname{covol}(U_k)$, which is finite. The covolume is positive, so the difference is $\operatorname{covol}(U_k)$. $\square$

**Theorem 7.4.4 (Chern integrals of the Hodge metric).** Let $X, j, f, \mathcal{E}, A_0$ be a Lie base for $Y_k$, with open part $O$ and Hodge metric $h$. Let $\lambda$ be a weight and $R \in \mathbb{R}[c_{\tau,k}]$ with $\operatorname{antisym}(Q_{\lambda, \dim Y_k}) = \chi(R)\,\Delta$. Then
$$\int_O R(c(h)) = \operatorname{covol}(U_k) \cdot \deg_{\mathrm{Fl}}(\lambda).$$

Lean: `GlobalTheory.LieBase.hasChernIntegral_covol_flagDeg` (also `GlobalTheory.T.hodgeMetric_chernIntegral_eq_covolume_mul_flagDegree`, a second name).

*Proof.* By [pointwise proportionality](/entry/pointwise-hodge/), the densities of $R$ and $P_0$ satisfy the hypothesis of the lemma on proportional densities with $s = \deg_{\mathrm{Fl}}(\lambda)$. The [Chern integral of the point class](/entry/has-chern-integral-point-poly-covol/) is $\operatorname{covol}(U_k)$. The lemma gives $\int_O R(c(h)) = \deg_{\mathrm{Fl}}(\lambda) \cdot \operatorname{covol}(U_k)$. $\square$

The theorem does not ask that the Hodge metric be good. The growth conditions enter only through the hypothesis of the main theorem, which converts Chern integrals of good metrics into intersection numbers. Here the finiteness of the masses comes from the exact computation of the volume.

**Remark 7.4.5.** In Mumford's paper the two halves are the theorem that the Chern forms of a good metric represent, as currents, the Chern classes of the canonical extension, and the volume computation through the compact dual (D. Mumford, "Hirzebruch's proportionality theorem in the non-compact case", Invent. Math. 42 (1977), 239 to 272). Here the second half is proved, and the first half is taken as a hypothesis.

**Remark 7.4.6 (Formalization).** The Chern integral is `HasChernIntegral` in [InterPolyProdSum.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/InterPolyProdSum.lean#L134). Its value is part of the definition, so uniqueness is immediate. The lemma on proportional densities is `GoodMetric.hasChernIntegral_of_eq_mul` in [HasChernIntegralOfEqMul.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/HasChernIntegralOfEqMul.lean#L80); we did not read its proof, and the proof above is ours. The nonnegativity of the density of $P_0$ is the lemma `chernTop_pointClass_hodge_metric_lie_nonneg`, whose proof we did not open. The proof of the second theorem ends with `convert … using 3` ([HodgeMetricChernIntegralEqCovolumeMulFlagDegree.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/HodgeMetricChernIntegralEqCovolumeMulFlagDegree.lean#L20)); we did not check which terms it identifies.
