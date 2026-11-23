---
id: exists-analytic-biextension-chart-complex-point
title: An additive analytic chart at a complex point, as a statement
kind: theorem
decl: GlobalTheory.T.exists_analytic_biextension_chart_complex_point
module: Development.AbelianVarietyTheory.Proofs.CuspFormEvaluations.ExistsAnalyticBiextensionChartComplexPointStatement
covers: 326
status: drafted
drafted_by: writer@claude
---
This theorem is a second name. It is used in step 3 of [harm-nab-eq-poly-deriv](/entry/harm-nab-eq-poly-deriv/). Its proof only calls [exists-analytic-chart](/entry/exists-analytic-chart/), which has the same statement and the real proof.

## Statement

Let $y$ be a complex framed point with an analytic uniformization $\Phi$ of dimension $g$ (`AnPt y g ty el`), and assume that `star` on $\mathcal{O}_E$ is the conjugation `H.bar`. Then there is a chart $C$ at $y$ (`ChartAt`) with $C.d = g$ and:

- $C.h = 0$;
- the formal group law of $C$ is additive: $F_i(X_0, X_1) = X_{0,i} + X_{1,i}$;
- the direction vectors are unit vectors: $C.\mathrm{uvec}(\ell)$ is the basis vector of index $\mathrm{el}^{-1}(\ell)$;
- for every $k$, every section $F$ of the $k$-th power and every $\theta$ that reads $F$ in the frame of $\Phi$, the germ of $F$ in $C$ is the Taylor series of $\theta$ at $0$ (`IsGerm ... (tay θ 0)`, up to a renaming of variables by $C.d = g$).

## Proof

The proof is one tactic line: `first | exact @GlobalTheory.AnVal.exists_analytic_chart | ...`. The first branch closes the goal.

## In the Lean code

The theorem is in [ExistsAnalyticBiextensionChartComplexPointStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/ExistsAnalyticBiextensionChartComplexPointStatement.lean#L10). The proof it calls is in [ExistsAnalyticBiextensionChartComplexPoint.lean](lean:Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/ExistsAnalyticBiextensionChartComplexPoint.lean#L73).

The word "biextension" in the name refers to the field `B` of the chart. In the chart that the proof builds, `B` is `anFB ty`, which is `FB.triv (addFGLaw g) (linOAct ty)` in [ComposeLinearAction.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/PullbackSections/HolomorphicFamilies/ComposeLinearAction.lean#L110): the trivial object over the additive formal group law. I have not unfolded `FB.triv`.
