---
id: u-pre-of-boundary
title: A tautological chart at each boundary point, first renaming
kind: theorem
decl: GlobalTheory.UChart.uPre_of_boundary
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsTripleChartUnitaryBoundaryPoint
covers: 1050
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [the "pointRigid" statement](/entry/exists-triple-chart-unitary-boundary-point-rigid/). Its only user is [the statement form](/entry/exists-triple-chart-unitary-boundary-point/), which goes to [`rigidForFan_of_uStB`](/entry/rigid-for-fan-of-u-st-b/). The content is in [`uPre_of_boundary_pointRigid`](/entry/u-pre-of-boundary-point-rigid/).

## Statement

**Theorem.** With the data and hypotheses of [`uPre_of_boundary_pointRigid`](/entry/u-pre-of-boundary-point-rigid/) (`UPoinOnX`, `SepB`, $p + q \geq 1$ and the fan conditions on $\varphi$), the chart condition `UPre` holds at each point $x$ of the blow-up $S$ outside $j(X_F)$.

`UPre` at $x$ asks for a formal chart through $x$ with a tautological monomial family, with the boundary given by $t_1 \cdots t_m = 0$ and the divisor $B$ by $\prod_i t_i^{a_i}$. See [`uPre_of_boundary_pointRigid`](/entry/u-pre-of-boundary-point-rigid/) for the full list.

## Proof

The proof is the term `GlobalTheory.T.exists_tripleChart_unitary_boundary_pointRigid`, applied to all the arguments. There is nothing else.

## In the Lean code

The theorem is at [ExistsTripleChartUnitaryBoundaryPoint.lean line 12](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsTripleChartUnitaryBoundaryPoint.lean#L12). It names its arguments (`hpq`, `hφ`, `hns`, `hP`, `hS`, `hx`) and passes each of them on, in the same order.
