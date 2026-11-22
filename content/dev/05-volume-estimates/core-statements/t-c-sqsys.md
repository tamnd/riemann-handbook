---
id: t-c-sqsys
title: Square systems on a flag cover
kind: theorem
decl: PositivityTheory.Xgp.t_c_sqsys
module: Development.WeilBound.CoreStatements.PluriharmonicCharts.XCSqsys
covers: 1107
status: drafted
drafted_by: writer@claude
---
This theorem builds, for each adjacent pair of columns of a flag model, a square system: a variety of pairs of points that differ in one block, with sections and metrics that compare the two points. It is the content of [the relay](/entry/relay-flag-cover-realisation-pullback/) and of [the statement form](/entry/t-flag-cover-realisation-pullback/). Through them it gives the field `sq` of the flag systems that [the swap relation from seven statements](/entry/good-tower-antisymmetry-of/) needs.

## Statement

Let $y$ be coordinates $y_{k,i}$ in a field $\Phi$, one block $\iota_k$ for each $k \in K$. Let $M$ be a flag model over $y$ for a finite set $\Psi$, an integer $N$ and an integer $j$. Let $\mathrm{BM}$ be a base metric on $M$ and $\mathrm{FA}$ analytic flag data over $\mathrm{BM}$ of dimension $d$. Let $M'$ be a second flag model over coordinates $y'$, with a flag cover $M' \to M$ and a realization $\mathrm{CR}$ of $\mathrm{FA}$ along the cover. Let $\xi_{\tau,a}$ be the vector on $\Psi \times \{0, \dots, N-1\}$ with the values $1, -2, 1$ at $(\tau, a-1)$, $(\tau, a)$, $(\tau, a+1)$ and $0$ elsewhere.

**Theorem.** Assume `Inputs`. If the coordinate ideal of $y$ is an arithmetic variety of dimension $d + 2$, then for each $\tau$ and each $a$, $b = a + 1$ with $b < j$ or $j \leq a$, there is a square system for the realization of $\mathrm{CR}$ at $(\tau, a)$ with coefficients $\xi_{\tau,a}$.

A square system (`SqSys`) has a block $k_0$; an analytic square $Q$ with two maps $q_0, q_1$ to the base; an algebraic square: a variety $W$ of dimension $d + 3$ with two block maps $v_0, v_1$ that agree off $k_0$, and multihomogeneous $g, h$ with $\operatorname{div} g = \operatorname{div} h + \Delta$; and a realization of $Q$ on $W$ whose lines are pullbacks by $v_0$ and $v_1$. Off a null set, the log norm of $g/h$ plus the mean of the log norms of the combined line at the two points equals $\log\lVert v \rVert + \mathrm{cst} + \tfrac12 \sum_p \xi_{\tau,a}(p)\,(\varphi_p(q_0) + \varphi_p(q_1))$.

## Proof

1. `t_c_swap` on $M$ and on $M'$ gives the block $k_0$ and columns $c_b = c_a + 1$, with $\sum_p \xi_{\tau,a}(p) \deg_{k_0} = -2$.
2. `flag_adjacent_swap_square_system` gives the analytic square $Q$, a resolution and a norm formula on $M$.
3. `t_c_w_sec` gives $g$ and $h$ on the side of $M'$ with the divisor and degree identities. `mkAlg` makes the algebraic square.
4. `mapsTo_twoFlagFramesOrthogonal_of_isometry` lifts the resolution over the cover, with degree the degree of the cover.
5. The realization is built by pullback by $v_0$ and $v_1$. `varpi_eq` and `pot_pull` check the potentials.
6. `AnResNullForm.proof` shows that the zero set of $gh$ is null. Off it, `norm_pt` and the norm formula of step 2 give the norm equation.

The rest is bookkeeping.

## In the Lean code

The theorem is in [XCSqsys.lean](lean:Development/WeilBound/CoreStatements/PluriharmonicCharts/XCSqsys.lean#L82). `SqSys` and `AnSq` are in [GeometricAbelianConnected.lean](lean:Development/AutomorphicSpectrum/Definitions/MetricPeriods/GeometricAbelianConnected.lean#L131). We have not unfolded `FlagModel`, `CovReal` or the lemmas of steps 1 to 4.
