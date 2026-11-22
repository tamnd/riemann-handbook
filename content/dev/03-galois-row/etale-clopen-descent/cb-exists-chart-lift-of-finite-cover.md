---
id: cb-exists-chart-lift-of-finite-cover
title: The Čech form of the Lefschetz formula, as a name for field0
kind: theorem
decl: UpperTheory.Cb.exists_chart_lift_of_finite_cover
module: Development.AutomorphicArithmetic.Foundations.EtaleClopenDescent.ExistsChartLiftOfFiniteCover
covers: 1193
status: drafted
drafted_by: writer@claude
---
This theorem gives a public name to the private theorem [`field0`](/entry/field0/). It is used by [its restatement](/entry/t-exists-chart-lift-of-finite-cover/), which the [integral case of the Lefschetz formula](/entry/holomorphic-lefschetz-finite-etale-integral/) applies. It has no content of its own.

## Statement

The statement is the [Čech form of the holomorphic Lefschetz formula](/entry/t-exists-chart-lift-of-finite-cover/), word for word. In short: let $F \subset K \subset K'$ be fields over $\mathbb{C}$ with a second map $j_2 \colon K \to K'$, and let $x_0, \dots, x_d$ make $K$ and $K'$ finite covers of $\mathbb{P}^d$ on the standard charts. Suppose that the fixed points of the pair (inclusion, $j_2$) all lie over the origin of chart $0$, that the fibre there is reduced, and that each fixed point $e$ has a matrix $A_e$ with $\det(1 - A_e) \neq 0$. Let $u_p$ act on the Čech group $H^p$ of the $a$-forms as $c_{1*} c_2^*$. Then

$$\sum_{p=0}^{d} (-1)^p \operatorname{tr} u_p = \sum_{e} \frac{[t^a] \det(1 + t A_e)}{\det(1 - A_e)}.$$

The full list of hypotheses is in the [restatement](/entry/t-exists-chart-lift-of-finite-cover/).

## Proof

The proof is the term `field0`. The statement of `field0` is the proposition `Field0`, and this theorem writes out its definition.

## In the Lean code

The theorem is in [ExistsChartLiftOfFiniteCover.lean](lean:Development/AutomorphicArithmetic/Foundations/EtaleClopenDescent/ExistsChartLiftOfFiniteCover.lean#L199), and its proof is the last line of the file. `Field0` is defined in [ResidueOfTraceIsFiberSum.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/LocalMaximality/ResidueOfTraceIsFiberSum.lean#L282). The name says "exists", but the statement is a trace identity. Two hypotheses, the regular parameters on $K$ and the finite dimension of the Čech groups, are not used in the proof.
