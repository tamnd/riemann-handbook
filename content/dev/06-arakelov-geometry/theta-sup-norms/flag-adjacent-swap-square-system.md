---
id: flag-adjacent-swap-square-system
title: The analytic square of an adjacent swap, the statement form
kind: theorem
decl: GlobalTheory.T.flag_adjacent_swap_square_system
module: Development.AutomorphicSpectrum.Proofs.MetricProofs.FlagAdjacentSwapSquareSystemStatement
covers: 578
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. Its proof calls [the analytic square of an adjacent swap](/entry/ansq-exists/), which holds the content. Its one user is [square systems on a flag cover](/entry/t-c-sqsys/), where it is step 2: it gives the analytic square $Q$, the resolution of the swap variety and the norm formula on the flag model $M$.

## Statement

The statement is the same as in [the analytic square of an adjacent swap](/entry/ansq-exists/). For a flag model $M$ with base metric $\mathrm{BM}$ and analytic data $\mathrm{FA}$, and an adjacent pair of rows $a, b = a + 1$ in one block $k_0$, it gives an analytic square $Q$ at $(\tau, a)$ with coefficients $\xi_{\tau,a}$, a log resolution $R_W$ of the swap variety, a map $e \colon R_W \to W$ of degree one, and the norm formula.

## Proof

The proof is `first | exact @GlobalTheory.CompanionTheory.Ar.PB.WSq.ansq_exists | ...`.

## In the Lean code

The theorem is in [FlagAdjacentSwapSquareSystemStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/MetricProofs/FlagAdjacentSwapSquareSystemStatement.lean#L8). Its user is in [XCSqsys.lean](lean:Development/WeilBound/CoreStatements/PluriharmonicCharts/XCSqsys.lean#L92).

The name says "square system", but the conclusion gives only the analytic square `AnSq`, not the structure `SqSys`. The full square system, with its algebraic square and realization, is built in [square systems on a flag cover](/entry/t-c-sqsys/).
