---
id: lie-gram-is-good
title: The Hodge metric on a Lie base is good at the boundary
kind: theorem
decl: GlobalTheory.LieBaseGood.lieGram_isGood
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.HodgeMetricLieGramIsGoodMumford
covers: 358
status: drafted
drafted_by: writer@claude
---
This theorem proves that the metric `lieGram` on the bundle $\mathcal{E}$ of a Lie base is good, in the sense of Mumford, at the boundary of the open part. Through [its restatement](/entry/hodge-metric-lie-gram-is-good-mumford/) it gives property 4 of [the good base](/entry/exists-good-base/). The proof is local: near a boundary point it writes the metric with a period matrix that has logarithmic growth, and checks the bounds there.

## Statement

Use the setting and notation of [the good base](/entry/exists-good-base/). Let $C$ be a flag component, $(X, j, f, f_0, \mathcal{E}, A_0)$ a Lie base for $C$, $O = $ `openPart j` and $h = $ `lieGram`.

**Theorem.** Assume `GoodEmb` and `IsUnf`. Then $h$ is good on $O$ (`IsGood`). That is, each $y \in X(\mathbb{C}) \setminus O(\mathbb{C})$ has a holomorphic chart $\phi$ with $\phi(y) = 0$ and a set $S$ of coordinates such that near $y$ the boundary is $\{z_a = 0 \text{ for some } a \in S\}$, and a frame $A$ at $y$ with constants $c$, $N$ such that, near $y$ on $O$, the matrices $h_A$, $\det h_A^{-1}$, the connection and the curvature satisfy the growth bounds `GoodBound` in powers of $\sum_{a \in S} |\log|z_a||$ and in the Poincaré weights $|z_a|\,|\log|z_a||$.

These are the good metrics of Mumford, "Hirzebruch's proportionality theorem in the non-compact case" (Invent. Math. 42, 1977).

## Proof

Fix a boundary point $y$.

1. **A period chart.** `exists_hodgeMetric_periodChart_at_boundaryPoint` gives a holomorphic chart $\phi$ at $y$ into the unit polydisc, with $\phi(y) = 0$ and boundary $\{z_1 \cdots z_a = 0\}$; a frame $A$ at $y$; integers $g$ and $r \le g$; a holomorphic symmetric $g \times g$ matrix $\tau_0(z)$ and integer positive semidefinite matrices $B_1, \dots, B_a$ supported on the first $r \times r$ block (`IsPeriodChart`: $\sum_i B_i$ is positive definite on that block and $\operatorname{Im}\tau_0$ on the other block); and holomorphic $m_\tau \times g$ matrices $Q_\tau(z)$ with $\sum_\tau m_\tau = g$ and linearly independent rows at $0$. Let $G(z) = \operatorname{Im}\tau_0(z) - \sum_{i=1}^{a} \frac{\log|z_i|}{2\pi} B_i$ (`hodgeGram`). The lemma gives $h_A(z)_\tau = Q_\tau(z)\,G(z)^{-1} Q_\tau(z)^*$ on $O$, and $Q_\tau G^{-1} Q_{\tau'}^* = 0$ for $\tau \ne \tau'$.
2. **The inverse period is good.** `inv_hodgeMetricGram_mumfordGoodGrowth_boundaryChart`: on a punctured polydisc of radius $\rho \le 1/2$, $G$ is positive definite, $G^{-1}$ is $C^2$, and $G^{-1}$ satisfies `GoodBound` for the first $a$ coordinates.
3. **Frame change.** `mumfordGoodGrowthBound_frameChange_orthogonalSummands`: if $G_0$ is good on an open set $W$ and the $Q_\tau$ are holomorphic, of full rank at $0$ and orthogonal for $G_0$, then each $Q_\tau G_0 Q_\tau^*$ is good near $0$.
4. **Germs.** `mumfordGoodGrowthBound_congr_germ_gram`: `GoodBound` at a point depends only on the germ of the matrix.

Steps 2 and 3 with $G_0 = G^{-1}$ give the bounds for $Q_\tau G^{-1} Q_\tau^*$; step 1 and step 4 move them to $h_A$. The rest is bookkeeping with neighbourhoods.

## In the Lean code

The theorem is in [HodgeMetricLieGramIsGoodMumford.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/HodgeMetricLieGramIsGoodMumford.lean#L19). The four lemmas are second names:

- `exists_hodgeMetric_periodChart_at_boundaryPoint` restates `GlobalTheory.LieBase.HodgeChart.exists_hodge_period_chart`;
- `inv_hodgeMetricGram_mumfordGoodGrowth_boundaryChart` restates `GlobalTheory.HodgeInvGood.inv_hodgeGram_goodBound`;
- `mumfordGoodGrowthBound_frameChange_orthogonalSummands` restates `GlobalTheory.FrameGood.frame_summands_goodBound`;
- `mumfordGoodGrowthBound_congr_germ_gram` restates `GlobalTheory.GoodMetric.goodBound_congr_nhds`.

`hodgeGram`, `punctured` and `IsPeriodChart` are in [HodgePeriodGram.lean](lean:Development/AbelianVarietyTheory/BlockTheory/DivisorBase/HodgePeriodGram.lean#L22). We have not unfolded the proofs of the four lemmas. The geometry is in `exists_hodge_period_chart`, the only one of them that uses the Lie base, `GoodEmb` and `IsUnf`. The other three are statements about matrix functions on a polydisc.
