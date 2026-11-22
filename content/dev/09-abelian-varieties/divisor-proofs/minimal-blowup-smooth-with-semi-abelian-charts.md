---
id: minimal-blowup-smooth-with-semi-abelian-charts
title: The blowup of the minimal compactification is smooth with semi-abelian charts (a wrapper)
kind: theorem
decl: GlobalTheory.T.minimalBlowup_smooth_with_semiAbelianCharts
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.MinimalBlowupSmoothWithSemiAbelianChartsStatement
covers: 2261
status: drafted
drafted_by: writer@claude
---
This theorem states $\mathrm{ChartSt5}$ under a second name. Its one caller is [`siegelToroidalPolCharts`](/entry/siegel-toroidal-pol-charts/), where it is step 4: the smoothness of the toroidal compactification and its local charts. The real content is in [`chartSt5_holds`](/entry/chart-st5-holds/). Its 2,261 declarations are itself and the 2,260 below that theorem.

## Statement

**Theorem.** $\mathrm{ChartSt5}$ holds.

In short: let $Z$ be a minimal compactification of the Siegel moduli space of genus $g$ and odd level $n \ge 3$ over $\mathbb{Z}[\zeta_n, 1/n]$, in the sense of `MinAt5`, and let $\pi \colon \overline{S} \to Z$ be a normalized blowup along an ideal whose valuations along degenerations are given by a polarization function $\varphi$ with no self-intersections (the predicate `BlowAt`). Then $\overline{S}$ is smooth of relative dimension $g(g+1)/2$, and each point of $\overline{S}$ has a pre-chart with a local semi-abelian scheme. The entry [`chartSt5_holds`](/entry/chart-st5-holds/) states it in full.

## Proof

Apply `SiegJoin.chartSt5_holds`. The two statements are the same.

## In the Lean code

The theorem is in [MinimalBlowupSmoothWithSemiAbelianChartsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/MinimalBlowupSmoothWithSemiAbelianChartsStatement.lean#L6). Its proof is the tactic `first | exact @X | exact X | (intros; apply X <;> assumption)` with `X = SiegJoin.chartSt5_holds`, under `maxHeartbeats 1000000`. The two types are the same constant, so the first branch is enough. The name is accurate: the conclusion is smoothness and local charts with semi-abelian schemes.
