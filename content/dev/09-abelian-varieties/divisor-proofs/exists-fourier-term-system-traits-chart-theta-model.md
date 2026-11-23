---
id: exists-fourier-term-system-traits-chart-theta-model
title: A raw Fourier system with traits and a chart member, stated
kind: theorem
decl: GlobalTheory.T.exists_fourierTermSystem_traits_chart_thetaModel
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsFourierTermSystemTraitsChartThetaModelStatement
covers: 501
status: drafted
drafted_by: writer@claude
---
This theorem is a second name. Its statement is the statement of [`exists_vPre_traits_chart`](/entry/exists-v-pre-traits-chart/), and its proof is that theorem. [The normalization step](/entry/exists-chart-member-traits-r/) calls it in step 1. Below it are 501 declarations.

## Statement

The data are those of [the regular traits statement](/entry/exists-fourier-term-system-regular-traits-given-chart/): a Siegel family over $X$, a theta compactification $i \colon X \to Z$ with a matrix $W$, a monomial family $(V, Q, t, \delta)$ at $\xi \colon \operatorname{Spec} V \to Z$, a prime $l$ that divides $n$, and $j_0 \in \mathbb{N}$.

**Theorem.** There are $j \geq j_0$, a theta setup $X_1$ with a point $z_1$ whose stalk $A$ is a domain, a raw Fourier system $\Phi$ over $A$ (`VPre`), an index $y$, a map $\rho \colon V \to V_y$, identifications $e$, $h$ and a label $c_0$, such that, with $N_1 = l^{2j}$:

1. $\Phi$ has the traits (`HasTraitsR`);
2. $(\rho, e, h)$ makes the family a member at $y$ whose theta terms need not be normalized (`IsChartMemberP`);
3. $u_{y'}(0, c_0)$ is a unit for each index $y'$;
4. $y$ is the only index that can have $m_{y'} \neq 1$;
5. `Exact` and `ClassSums` hold at level $N_1$.

## Proof

The proof is the term `GlobalTheory.Poinc.Sep.exists_vPre_traits_chart`.

## In the Lean code

The theorem is in [ExistsFourierTermSystemTraitsChartThetaModelStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsFourierTermSystemTraitsChartThetaModelStatement.lean#L12). The proof is `first | exact @GlobalTheory.Poinc.Sep.exists_vPre_traits_chart | ...`. The statement repeats the statement of that theorem.
