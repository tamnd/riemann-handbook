---
id: hermitian-theta-series-span-bounded-forms
title: Hermitian theta series span the bounded forms (statement)
kind: theorem
decl: GlobalTheory.T.hermitianTheta_series_span_bounded_forms
module: Development.AbelianVarietyTheory.Proofs.SiegelThetaTransformation.HermitianThetaSeriesSpanBoundedFormsStatement
covers: 976
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`SpanMain.theta_span`](/entry/theta-span/), which has the real content. Its proof only calls that theorem. Its user is [`level_theta_span`](/entry/level-theta-span/), which applies it to the theta system of a level.

## Statement

Let $E$ be a CM field, let `X : Data E r` be a hermitian space of signature $(p_0, q_0)$ with a symplectic basis `bas` of its lattice, and let $n$ be even with $4r < n$. Let $\Delta$ be a group of unitary matrices, $\mathcal{L}$ a set of lattices, $\Phi$ a family of test functions and $\mu$ a multiplier, and let $M > 0$. Suppose that $(\Delta, \mathcal{L}, \Phi, \mu)$ is a theta system (`IsSystem`). Then each form $F$ of weight `wtOf c c' n` for $(\Delta, \mathcal{L}, \mu)$ (`IsForm`: holomorphic, equivariant and bounded) is a finite sum
$$F(L, x) = \sum_i a_i\, \theta_{P_i}\big(\Phi(L, \Lambda_i)\big)(x)$$
with $\Lambda_i$ in the genus `Vset` and $P_i$ row-highest harmonic polynomials of type $(c, c')$ (`InSpan`). The [entry for `theta_span`](/entry/theta-span/) explains the terms.

## Proof

The proof is `SpanMain.theta_span`.

## In the Lean code

The theorem is in [HermitianThetaSeriesSpanBoundedFormsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation/HermitianThetaSeriesSpanBoundedFormsStatement.lean#L8). The proof is the tactic `first | exact @GlobalTheory.SW.SpanMain.theta_span | ...`. The two statements are identical, so the first `exact` closes the goal.
