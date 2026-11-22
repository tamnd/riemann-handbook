---
id: t-exists-chart-lift-of-finite-cover
title: The Lefschetz formula in Čech form on the charts of a finite cover of projective space
kind: theorem
decl: GlobalTheory.T.exists_chart_lift_of_finite_cover
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.ExistsChartLiftOfFiniteCover
covers: 1194
status: drafted
drafted_by: writer@claude
---
This theorem is the holomorphic Lefschetz formula written in algebra: function fields, the charts of $\mathbb{P}^d$ and Čech cocycles of Kähler forms. The [integral case of the formula](/entry/holomorphic-lefschetz-finite-etale-integral/) puts the varieties $Z$ and $Y$ in this form and then applies this theorem. The theorem is a restatement of [its copy in the étale descent files](/entry/cb-exists-chart-lift-of-finite-cover/), whose proof is [`field0`](/entry/field0/).

## Statement

Let $F \subset K \subset K'$ be fields over $\mathbb{C}$, let $x_0, \dots, x_d \in F$, and let $j_2 \colon K \to K'$ be a second $\mathbb{C}$-algebra map. Write $t_m = x_{m+1}/x_0$. For $I \subset \{0, \dots, d\}$ let $B_I \subset K$ and $B'_I \subset K'$ be the integral closures of $\mathbb{C}[x_j/x_i : i \in I]$. A *point* of chart $i$ of $K'$ is a $\mathbb{C}$-algebra map $e \colon B'_i \to \mathbb{C}$. It is *fixed* if for each $b \in B_i$ the element $j_2(b)$ has a value at $e$, and this value is $e(b)$. The set $\mathrm{fib}$ is the set of points of chart $0$ with $e(t_m) = 0$ for all $m$. In geometry: $K$ and $K'$ are the function fields of $Z$ and $Y$, the inclusion is $c_1^*$, $j_2$ is $c_2^*$, and $\mathrm{fib}$ is the fibre of $Y$ over the origin of chart 0.

Suppose that:

1. for $K$ and for $K'$, the ratios $x_j/x_0$ are a transcendence basis that generates $F$, the extension over $F$ is finite and separable, and each $B_{\{i\}}$ is smooth;
2. each point of each chart of $K'$ has a chart $j$ such that every element of the integral closure of $j_2(B_{\{j\}})$ is regular at it;
3. the ring $B'_0/(t_1, \dots, t_d)$ is reduced;
4. no chart $i \neq 0$ has a fixed point, and every fixed point of chart $0$ is in $\mathrm{fib}$;
5. $F_x \subset \mathrm{fib}$ is the finite set of fixed points;
6. at each $e \in F_x$, the $t_l$ generate the maximal ideal of $B_0$ at $e$ locally;
7. at each $e \in F_x$, $j_2(t_m) = \sum_l g_l t_l$ with $g_l$ regular at $e$ and $g_l(e) = (A_e)_{ml}$, and $\det(1 - A_e) \neq 0$;
8. $u_p$ is an endomorphism of the Čech group $H^p$ of the $a$-forms $\Omega^a_{B_I}$ on the charts, with this lift property: each cocycle $b$ has a cocycle $\tilde b$ on the joint cover of $K'$ by the rings $B'_I \cdot B''_J$, where $B''_J$ is the integral closure of $j_2(B_J)$, such that the $J$-part of $\tilde b$ is $j_2 b$ and the trace to $K$ of the $I$-part of $\tilde b$ represents $u_p[b]$;
9. each $H^p$ has finite dimension.

Then

$$\sum_{p=0}^{d} (-1)^p \operatorname{tr} u_p = \sum_{e \in F_x} \frac{[t^a] \det(1 + t A_e)}{\det(1 - A_e)}.$$

Condition 8 says that $u_p$ is $c_{1*} c_2^*$ on Čech cohomology. The trace on forms, `trDR`, is chosen by choice when a trace map exists, and is $0$ otherwise.

## Proof

The proof is one line. It applies `UpperTheory.Cb.exists_chart_lift_of_finite_cover`, which has the same statement. The work is in [`field0`](/entry/field0/).

## In the Lean code

The theorem is in [ExistsChartLiftOfFiniteCover.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/ExistsChartLiftOfFiniteCover.lean#L7). The proof is `first | exact @UpperTheory.Cb.exists_chart_lift_of_finite_cover | exact UpperTheory.Cb.exists_chart_lift_of_finite_cover`.

The name says "exists", but the statement is a trace identity, not an existence statement. Conditions 6 and 9 are not used: `field0_of` in [TraceEqZeroOfBot.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/LocalMaximality/TraceEqZeroOfBot.lean#L52) binds them and never uses them. The conditions are stated with `IsFinCover`, `rB`, `R2`, `RY`, `IsFix`, `fib`, `omB`, `cech`, `pr2L` and `trC`, whose definitions we read.
