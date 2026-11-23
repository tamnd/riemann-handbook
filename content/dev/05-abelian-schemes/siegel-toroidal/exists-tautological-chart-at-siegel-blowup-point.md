---
id: exists-tautological-chart-at-siegel-blowup-point
title: A tautological chart at each point of the Siegel blowup (statement)
kind: theorem
decl: GlobalTheory.T.exists_tautological_chart_at_siegel_blowup_point
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsTautologicalChartAtSiegelBlowupPointStatement
covers: 1213
status: drafted
drafted_by: writer@claude
---
This theorem is a restatement. Its statement is the statement of [`TChart.exists_chart_at`](/entry/exists-chart-at/), word for word, and its proof only calls that theorem. The real content is in that entry. Two lemmas use this theorem: `smoothOfRelativeDimension_blowAt_comp` and `exists_preChart_siegel_normalizedBlowup`. These are the two halves of [`chartSt5_holds`](/entry/chart-st5-holds/): the blowup is smooth of relative dimension $g(g+1)/2$, and each of its points has a chart.

## Statement

Let $g \geq 1$. Let $\varphi$ be a polarisation function that is a fan in genus $g$ (`IsPolFan`) and has no self-intersection (`NoSelfInt`). Let $n \geq 3$ be odd. Let $F$ be a Siegel family of genus $g$ and level $n$ over $\mathbb{Z}[\zeta_n, 1/n]$. Let $(Z, z, i, \mathcal{O}_Z)$ be a compactification of $F$ of the type of the minimal compactification, in the sense of `MinAt5`. Let $\pi \colon S \to Z$ with the open immersion $j \colon F.X \to S$ and the Cartier divisor $BD$ be a normalised blowup in the sense of `BlowAt`. Then for each point $x \in S$ there are a tautological chart $C$ with complete local ring $R$, a semi-abelian scheme $G_1$ over $\operatorname{Spec} R$ with a map $y \colon \operatorname{Spec} \operatorname{Frac}(R) \to F.X$, and a map $\xi \colon \operatorname{Spec} R \to S$, such that $(G_1, y)$ is a Mumford family for $C$, $j \circ y = \xi \circ \iota$ for the generic point $\iota \colon \operatorname{Spec} \operatorname{Frac}(R) \to \operatorname{Spec} R$, and $\xi$ sends the closed point to $x$. The [entry for `exists_chart_at`](/entry/exists-chart-at/) unfolds each condition.

## Proof

The proof is `exists_chart_at`.

## In the Lean code

The theorem is in [ExistsTautologicalChartAtSiegelBlowupPointStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsTautologicalChartAtSiegelBlowupPointStatement.lean#L12). The proof is the tactic `first | exact @GlobalTheory.TChart.exists_chart_at | ...`. The two statements are identical, so `exact` with that theorem closes the goal. Other files of this chapter follow the same pattern: a file `...Statement.lean` restates, in the namespace `GlobalTheory.T`, a theorem that is proved in another namespace.
