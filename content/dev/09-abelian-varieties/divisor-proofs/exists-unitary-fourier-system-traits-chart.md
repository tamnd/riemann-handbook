---
id: exists-unitary-fourier-system-traits-chart
title: A raw Fourier system with traits and a member, stated
kind: theorem
decl: GlobalTheory.T.exists_unitary_fourier_system_traits_chart
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsUnitaryFourierSystemTraitsChartStatement
covers: 332
status: drafted
drafted_by: writer@claude
---
This theorem is a second name. Its statement is the statement of [`exists_vPre_traitsOn_chart`](/entry/exists-v-pre-traits-on-chart/), and its proof is that theorem. [The normalization step](/entry/exists-system-with-traits-and-family/) calls it in step 1. Below it are 332 declarations.

## Statement

The data are as in [the Fourier system with a member](/entry/exists-unitary-fourier-system-traits-family/): $Z_o$, $\varphi$, $V$ with a monomial family through $\xi$, an odd prime $n$ and $j_0$.

**Theorem.** There are $j \geq j_0$, a theta setup $X_1$ (`GSet`) whose model $M$ maps to $Z_o$, a point $z_1 \in M$ whose local ring is a domain, a nonempty open $U \subseteq M$, a raw Fourier system $\Phi$ over $\mathcal{O}_{M, z_1}$ (`VPre`), an index $y$ and a label $c_0$, such that:

1. $M$ is a normal cover of $Z_o$ at $z_1$ (`IsCov`), and $\Phi$ has the traits through $U$ (`HasTraitsOn`);
2. the monomial family is the member $y$, with theta terms of level $(n^j)^2$ that need not be normalized (`IsMemberP`);
3. $u_{y'}(0, c_0)$ is a unit for every index $y'$, and $y$ is the only index that can have $m_{y'} \neq 1$;
4. $\Phi$ satisfies `Exact` and `ClassSums` at level $(n^j)^2$.

[The proof entry](/entry/exists-v-pre-traits-on-chart/) says what `Exact` and `ClassSums` mean. [The normalization step](/entry/exists-system-with-traits-and-family/) defines the other objects.

## Proof

The proof is the term `GlobalTheory.GSep.exists_vPre_traitsOn_chart`.

## In the Lean code

The theorem is in [ExistsUnitaryFourierSystemTraitsChartStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsUnitaryFourierSystemTraitsChartStatement.lean#L12). The statement repeats the statement of that theorem word for word.
