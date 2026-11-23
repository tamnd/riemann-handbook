---
id: exists-tautological-chart-versality
title: A versal tautological chart through a degenerating family (statement form)
kind: theorem
decl: GlobalTheory.T.exists_tautological_chart_versality
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsTautologicalChartVersalityStatement
covers: 931
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`exists_taut_through`](/entry/exists-taut-through/), which has the real content. Its one user is [`exists_tautB_chart_at`](/entry/exists-taut-b-chart-at/), as step 2 of its proof. That theorem drops the map $\theta$ and keeps only the fact that the chart passes through the given boundary point.

## Statement

Use the notation, the hypotheses, monomial families (`MonoFam`) and `IsTautB` of [`exists_tautB_chart_at`](/entry/exists-taut-b-chart-at/).

**Theorem.** Assume $p + q \geq 1$, `IsPolFan` and `NoSelfInt` for $\varphi$ in rank $\min(p, q)$, `UPoinOnX` and `SepB`. Let $V$ be a local domain with `Mum.Base` and an algebraically closed residue field, $C$ a monomial family over $V$ whose character lattice is nonzero, and $\xi_V \colon \operatorname{Spec} V \to S$ such that the generic point of $C$ followed by $j$ is $\operatorname{Spec}\operatorname{Frac}(V) \to \operatorname{Spec} V \xrightarrow{\xi_V} S$. Then there are a field $k$, integers $m, e$, a monomial family $C_1$ over $R = k[[s_1, \dots, s_m, u_1, \dots, u_e]]$, a map $\xi \colon \operatorname{Spec} R \to S$ and a ring map $\theta \colon R \to V$ such that

1. $C_1$ satisfies `IsTautB`;
2. the generic point of $C_1$ followed by $j$ is $\operatorname{Spec}\operatorname{Frac}(R) \to \operatorname{Spec} R \xrightarrow{\xi} S$;
3. $\theta$ is a local homomorphism and $\xi \circ \operatorname{Spec}\theta = \xi_V$.

## Proof

The statement is the same as that of `GlobalTheory.UCanon.exists_taut_through`, and the proof applies it.

## In the Lean code

The theorem is in [ExistsTautologicalChartVersalityStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsTautologicalChartVersalityStatement.lean#L10). The proof is `first | exact @GlobalTheory.UCanon.exists_taut_through | ...`, a tactic that tries the alias in three forms. The type is copied word for word from [ExistsTautologicalChartVersality.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsTautologicalChartVersality.lean#L38). The name says "versality", but the chart $C_1$ depends on $C$. The statement does not say that one chart receives every family through the point, nor that $\theta$ is unique.
