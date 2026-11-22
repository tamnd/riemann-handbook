---
id: model-place-built2-of-chart-eqs
title: Model places from the chart equations
kind: theorem
decl: Formalism.FourierDecayAlt.P.CutMP.modelPlaceBuilt2_of_chartEqs
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.ModelPlaceBuilt2OfChartEqs
covers: 1930
status: drafted
drafted_by: writer@claude
---
This theorem is a relay. It proves `ModelPlaceBuilt2` from the hypothesis `ChartEqs`, and it adds one fact on the way: elliptic regularity. Its only user is [each place of a built setting is a model place](/entry/model-place-built-holds/), which proves `ChartEqs` and so removes the hypothesis. That entry states `ModelPlaceBuilt2` and `ChartEqs` in words.

## Statement

**Theorem.** If `ChartEqs` holds, then `ModelPlaceBuilt2` holds.

## Proof

1. `jfSmoothBuilt_of_chartEqs`, in the same file, proves `JfSmoothBuilt` from `ChartEqs`. It calls `jfSmoothBuilt_of_chart` with `elliptic_regularity_weighted`. `JfSmoothBuilt` is an `abbrev` for `JfSmoothDS`: there is $C_c$ such that at each built place with constant $C_c$, the transfer `B.JF` of $f_v$ lies in the function space `Q.FFl` on the domain `OmP`. We have not unfolded `Q.FFl`.
2. [`modelPlaceBuilt2_of_jf`](/entry/model-place-built2-of-jf/) turns `JfSmoothDS` into `ModelPlaceBuilt2`.

The fact `elliptic_regularity_weighted` proves `EllRegW`. Let $P_j$ be finitely many differential operators with smooth coefficients on an open set $U \subseteq \mathbb{R}^d$. Let $u$ be continuous on $U$ with $P_j u = 0$ in the weak sense for each $j$. Assume that for each $x \in U$ and $\xi \ne 0$ some principal symbol $p_j(x, \xi)$ is nonzero. Then $u$ is smooth on $U$. This follows from the bound $\operatorname{WF}(u) \subseteq \operatorname{Char}(P) \cup \operatorname{WF}(Pu)$ of Hörmander, *The Analysis of Linear Partial Differential Operators I*, Theorem 8.3.1, applied to each $P_j$. `ChartEqs` supplies the operators $P_j$ in each chart. Its conclusion turns a common characteristic direction into a nilpotent element; `jfSmoothBuilt_of_leaves` handles that element with `JfS.symbol_nilpotent_holds` and `lie_stabilizer_splitting`, which we have not unfolded.

## In the Lean code

The theorem is in [ModelPlaceBuilt2OfChartEqs.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/ModelPlaceBuilt2OfChartEqs.lean#L9). It calls:

- `jfSmoothBuilt_of_chartEqs`, at [line 6](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/ModelPlaceBuilt2OfChartEqs.lean#L6);
- `jfSmoothBuilt_of_chart` in [ModelPlaceBuilt2OfPublished.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/ModelPlaceBuilt2OfPublished.lean#L11), which calls `jfSmoothBuilt_of_rest` with `nilpotent_derivative`, `group_equations_post_holds` and `smooth_of_coefficients_holds`;
- `elliptic_regularity_weighted` in [CutEllRegW.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutEllRegW.lean#L6), with `EllRegW` in [TransferSmoothOfRegularity.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/TransferSmoothOfRegularity.lean#L37);
- [`modelPlaceBuilt2_of_jf`](/entry/model-place-built2-of-jf/).

The file named `ModelPlaceBuilt2OfPublished` does not contain a theorem with that name, and it has an empty namespace block at the end.
