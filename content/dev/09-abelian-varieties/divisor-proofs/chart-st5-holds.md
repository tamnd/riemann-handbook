---
id: chart-st5-holds
title: The normalized blowup is smooth and has local semi-abelian charts
kind: theorem
decl: GlobalTheory.SiegJoin.chartSt5_holds
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.MinimalBlowupSmoothWithSemiAbelianCharts
covers: 2260
status: drafted
drafted_by: writer@claude
---
This theorem proves $\mathrm{ChartSt5}$: a normalized blowup of the minimal compactification of the Siegel moduli space, along an ideal with the right valuations, is smooth of relative dimension $g(g+1)/2$ and has a pre-chart at each point. It is step 4 of the construction in [`siegelToroidalPolCharts`](/entry/siegel-toroidal-pol-charts/), and it reaches that theorem through the wrapper [`minimalBlowup_smooth_with_semiAbelianCharts`](/entry/minimal-blowup-smooth-with-semi-abelian-charts/).

## Statement

Let $\Lambda_n = \mathbb{Z}[\zeta_n, 1/n]$, let $g \ge 1$, let $\varphi$ be a polarization function for $g$ with no self-intersections, and let $n \ge 3$ be odd. Let $\mathcal{A}$ be a Siegel family of genus $g$ and level $n$ over a base $X$. Let $z \colon Z \to \operatorname{Spec} \Lambda_n$, $i \colon X \to Z$ and a line bundle $\mathcal{O}_Z(1)$ satisfy `MinAt5`: $Z$ is normal and projective over $\Lambda_n$, $i$ is a dense open immersion over $\Lambda_n$ (`IsThetaCompact`), $\mathcal{O}_Z(1)$ is ample, and a proper surjective normal cover of $Z$ carries a semi-abelian scheme whose Hodge bundle to a power $N \ge 1$ is the pullback of $\mathcal{O}_Z(1)$. Let $\pi \colon \overline{S} \to Z$, an open immersion $j \colon X \to \overline{S}$, an effective Cartier divisor $B$ on $\overline{S}$ and $d$ satisfy `BlowAt`: there is an ideal sheaf $J$ on $Z$ with

- $d \ge 1$, $J$ supported off $i(X)$, and $J$ with valuation $d\,\varphi(\beta)$ along each degeneration of period $\varpi^\beta$ over a discrete valuation ring (`ValOn`);
- $\pi$ a normalized blowup of $J$ (`IsNormBl`), with $\overline{S}$ projective over $\Lambda_n$;
- $j$ dense, $\pi \circ j = i$ and $\pi^{-1}(i(X)) = j(X)$;
- $B$ the divisor of $\pi^{-1}J$, again with `ValOn` for $\varphi$ and $d$.

**Theorem.** Then $\overline{S}$ is smooth of relative dimension $g(g+1)/2$ over $\Lambda_n$, and each point $x$ of $\overline{S}$ has a pre-chart (the predicate `PreChart`).

A pre-chart at $x$ is the polarized chart of [`siegelToroidalPolCharts`](/entry/siegel-toroidal-pol-charts/) with a semi-abelian scheme over the local ring $R$ in place of a global one. That scheme is abelian exactly where $t_1 \cdots t_m$ is a unit, and its generic fibre maps to $X$.

## Proof

The two halves have separate proofs, and both start from a tautological chart.

1. **Charts.** `exists_tautological_chart_at_siegel_blowup_point` gives, at each point $x$, a tautological chart $C$ (`Taut`) with a local semi-abelian scheme and a map $\xi$ to $\overline{S}$ with centre $x$. Then `tautologicalChart_centre_isCompletedEtaleLocalMap` says that $\xi$ is an étale completion at $x$.
2. **Smoothness** (`smoothOfRelativeDimension_blowAt_comp`). $\overline{S}$ is proper over $\Lambda_n$, since it is projective. At each $x$, the ring of $C$ is regular with relative parameters (`Taut.isRegularLocalRing_and_isRelParam`), so the local ring of $\overline{S}$ at $x$ is formally smooth over $\Lambda_n$ (`formallySmooth_stalkMap`). So $\overline{S}$ is smooth. Its relative dimension is that of $X$, which is dense in it (`smoothOfRelativeDimension_of_dense`).
3. **Pre-charts** (`exists_preChart_siegel_normalizedBlowup`). `preChart_of_tautologicalChart_etaleCompletion` turns the chart $C$ and the étale completion into a pre-chart at $x$.

## In the Lean code

The theorem is in [MinimalBlowupSmoothWithSemiAbelianCharts.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/MinimalBlowupSmoothWithSemiAbelianCharts.lean#L9). The statement `ChartSt5` is in [MinSt5OfMinSt4.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/MinSt5OfMinSt4.lean#L40).

- `smoothOfRelativeDimension_blowAt_comp` is a wrapper of `BlowSmooth.smoothOfRelativeDimension_blowup` ([L148](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SmoothOfRelativeDimensionBlowup.lean#L148)).
- `exists_preChart_siegel_normalizedBlowup` is a wrapper of `AllChart.preChart_all` ([L15](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsPreChartSiegelNormalizedBlowup.lean#L15)).
- Both call [`exists_tautological_chart_at_siegel_blowup_point`](/entry/exists-tautological-chart-at-siegel-blowup-point/), which holds 1,213 of the 2,260 declarations below this theorem.

`ChartSt5` has the same conclusion as `ChartSt` in [ExistsMinAt.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ExistsMinAt.lean#L42), but its hypothesis `MinAt5` is weaker than `MinAt`. It drops the preimage of $i(X)$ in the cover, the abelian locus of the semi-abelian scheme on the cover, a line bundle on that scheme, and a condition on abelian parts at geometric points. We have not unfolded `Taut`, `IsEtaleCompletion` or the degeneration data.
