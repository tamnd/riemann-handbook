---
id: exists-triple-chart-unitary-boundary-point-rigid
title: A tautological chart at each boundary point, the rigid statement
kind: theorem
decl: GlobalTheory.T.exists_tripleChart_unitary_boundary_pointRigid
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsTripleChartUnitaryBoundaryPointRigidStatement
covers: 1049
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [`uPre_of_boundary_pointRigid`](/entry/u-pre-of-boundary-point-rigid/), which has the content. Its only user is [`uPre_of_boundary`](/entry/u-pre-of-boundary/), which goes through [the statement form](/entry/exists-triple-chart-unitary-boundary-point/) to [`rigidForFan_of_uStB`](/entry/rigid-for-fan-of-u-st-b/).

## Statement

**Theorem.** With the data and hypotheses of [`uPre_of_boundary_pointRigid`](/entry/u-pre-of-boundary-point-rigid/) (`UPoinOnX`, `SepB`, $p + q \geq 1$ and the fan conditions on $\varphi$), the chart condition `UPre` holds at each point $x$ of the blow-up $S$ outside $j(X_F)$.

## Proof

The proof is the term `GlobalTheory.UCanon.uPre_of_boundary_pointRigid`. There is nothing else.

## In the Lean code

The theorem is at [ExistsTripleChartUnitaryBoundaryPointRigidStatement.lean line 10](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsTripleChartUnitaryBoundaryPointRigidStatement.lean#L10). The proof is a `first | exact … | …` block that tries the same lemma in three forms.

The statement is the same as that of [the statement form](/entry/exists-triple-chart-unitary-boundary-point/), word for word up to a namespace. So four theorems carry one statement, and only the last, `uPre_of_boundary_pointRigid`, has a proof with content. The suffix "Rigid" does not change the statement. Its proof passes the point rigidity in `IsTautB` to two lemmas, and then drops it.
