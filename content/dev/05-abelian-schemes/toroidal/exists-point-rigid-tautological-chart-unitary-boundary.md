---
id: exists-point-rigid-tautological-chart-unitary-boundary
title: A rigid tautological chart through each boundary point (statement form)
kind: theorem
decl: GlobalTheory.T.exists_pointRigid_tautological_chart_unitary_boundary
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsPointRigidTautologicalChartUnitaryBoundaryStatement
covers: 1009
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`exists_tautB_chart_at`](/entry/exists-taut-b-chart-at/), which has the real content. Its one user is [`uPre_of_boundary_pointRigid`](/entry/u-pre-of-boundary-point-rigid/). That theorem applies it at a boundary point $x$, then adds the étale completion and the boundary equations of the chart, and so gets the chart condition `UPre` at $x$.

## Statement

Use the moduli scheme $X^\circ_F$, the fan function $\varphi$, the data $Z, i, \pi, S, j, B$ and the hypotheses `UPoinOnX` and `SepB` from [the entry with the proof](/entry/exists-taut-b-chart-at/).

**Theorem.** Assume $p + q \geq 1$, `IsPolFan` and `NoSelfInt` for $\varphi$ in rank $\min(p, q)$, `UPoinOnX` and `SepB`. Then for each $x \in S$ outside the image of $j$ there are a field $k$, integers $m, e$, a monomial family $C$ over $R = k[[s_1, \dots, s_m, u_1, \dots, u_e]]$ with `IsTautB`, and a map $\xi \colon \operatorname{Spec} R \to S$, such that the generic point of $C$ followed by $j$ factors through $\xi$, and $\xi$ sends the closed point of $\operatorname{Spec} R$ to $x$.

## Proof

The statement is the same as that of `GlobalTheory.UCanon.exists_tautB_chart_at`, and the proof applies it.

## In the Lean code

The theorem is in [ExistsPointRigidTautologicalChartUnitaryBoundaryStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsPointRigidTautologicalChartUnitaryBoundaryStatement.lean#L10). The proof is `first | exact @GlobalTheory.UCanon.exists_tautB_chart_at | ...`, a tactic that tries the alias in three forms. The type is copied word for word from the theorem it calls.
