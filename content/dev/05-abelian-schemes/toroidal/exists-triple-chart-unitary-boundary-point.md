---
id: exists-triple-chart-unitary-boundary-point
title: A tautological chart at each boundary point, the statement
kind: theorem
decl: GlobalTheory.T.exists_tripleChart_unitary_boundary_point
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsTripleChartUnitaryBoundaryPointStatement
covers: 1051
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [`uPre_of_boundary`](/entry/u-pre-of-boundary/), which is itself a renaming. Its only user is [`rigidForFan_of_uStB`](/entry/rigid-for-fan-of-u-st-b/), where it is the main step: it gives the chart condition `UPre` at each boundary point of the blow-up $S$. The content is in [`uPre_of_boundary_pointRigid`](/entry/u-pre-of-boundary-point-rigid/).

## Statement

Use the data and the hypotheses `UPoinOnX` and `SepB` of [`uPre_of_boundary_pointRigid`](/entry/u-pre-of-boundary-point-rigid/).

**Theorem.** Assume $p + q \geq 1$, `IsPolFan` and `NoSelfInt` for $\varphi$, `UPoinOnX` and `SepB`. Then `UPre` holds at each $x \in S$ outside $j(X_F)$: there is a formal chart $\operatorname{Spec} k[[t_1, \dots, t_m, u_1, \dots, u_e]] \to S$ through $x$ that carries a tautological monomial family, in which the boundary is $t_1 \cdots t_m = 0$ and the divisor $B$ is $\prod_i t_i^{a_i}$ with $a_i = d\,\varphi(M'\delta_i)$.

## Proof

The proof is the term `GlobalTheory.UChart.uPre_of_boundary`. There is nothing else.

## In the Lean code

The theorem is at [ExistsTripleChartUnitaryBoundaryPointStatement.lean line 10](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsTripleChartUnitaryBoundaryPointStatement.lean#L10). The proof is a `first | exact … | …` block that tries the same lemma in three forms. The statement is word for word that of [the "pointRigid" statement](/entry/exists-triple-chart-unitary-boundary-point-rigid/), except that one writes `EffCartierData` with its namespace. The word "triple" in the name does not match a triple in the statement; we do not know what it refers to.
