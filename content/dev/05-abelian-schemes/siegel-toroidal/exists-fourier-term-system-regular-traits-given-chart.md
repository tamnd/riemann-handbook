---
id: exists-fourier-term-system-regular-traits-given-chart
title: A Fourier system with traits and a chart member, stated
kind: theorem
decl: GlobalTheory.T.exists_fourierTermSystem_regular_traits_given_chart
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsFourierTermSystemRegularTraitsGivenChartStatement
covers: 503
status: drafted
drafted_by: writer@claude
---
This theorem is a second name. Its statement is the statement of [`exists_chartMember_traitsR`](/entry/exists-chart-member-traits-r/), and its proof is that theorem. [Separation at the centre of a chart](/entry/sep-st/) calls it in step 3. Below it are 503 declarations.

## Statement

Let $g \geq 1$, let $n \geq 3$ be odd, and let $\mathcal{A}$ be a Siegel family of genus $g$ and level $n$ over $X$. Let $i \colon X \to Z$ be a dense open immersion over $\mathbb{Z}[\zeta_n, 1/n]$ into a normal projective $Z$, with a matrix $W$ such that `IsE8 W` and `ThetaInt` hold. Let $V$ be a local domain with degeneration data $Q$ of rank at most $g$, monomial (`IsMonomialTau`) in nonzero $t_1, \dots, t_m$ of the maximal ideal with forms $\delta_k$ as in [the proof entry](/entry/exists-chart-member-traits-r/). Let $\xi \colon \operatorname{Spec} V \to Z$ satisfy `UnifOver`. Let $l$ be a prime that divides $n$, and let $j_0 \in \mathbb{N}$.

**Theorem.** There are $j \geq j_0$, a theta setup $X_1$ (`Setup`) with a point $z_1$ of its model $M$, a Fourier system $\Phi$ of level $l^{2j}$ over $\mathcal{O}_{M, z_1}$ (`VSys`), an index $y$, a map $\rho \colon V \to V_y$ and identifications $e$, $h$ such that $\Phi$ has the traits (`HasTraitsR`) and $(\rho, e, h)$ makes the family a member of $\Phi$ at $y$ (`IsChartMember`).

## Proof

The proof is the term `GlobalTheory.Poinc.Sep.exists_chartMember_traitsR`.

## In the Lean code

The theorem is in [ExistsFourierTermSystemRegularTraitsGivenChartStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsFourierTermSystemRegularTraitsGivenChartStatement.lean#L12). The proof is `first | exact @GlobalTheory.Poinc.Sep.exists_chartMember_traitsR | ...`. The statement repeats the statement of that theorem.
