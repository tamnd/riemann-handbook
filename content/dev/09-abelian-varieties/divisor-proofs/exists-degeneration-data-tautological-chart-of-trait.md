---
id: exists-degeneration-data-tautological-chart-of-trait
title: Degeneration data from a tautological chart along a trait (statement)
kind: theorem
decl: GlobalTheory.T.exists_degeneration_data_tautologicalChart_of_trait
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsDegenerationDataTautologicalChartOfTraitStatement
covers: 407
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`TChart.exists_degFrom_of_trait`](/entry/exists-deg-from-of-trait/), which has the proof. Its one user is [`TChart.exists_chart_at`](/entry/exists-chart-at/), where it is step 3: after a finite extension of a trait, the family has degeneration data that come from a lower Siegel family, a basis of forms and values $s_k$.

## Statement

Let $F$ be a Siegel family over $\Lambda = \mathbb{Z}[\zeta_n, 1/n]$ with a polarisation fan $\varphi$, let $T$ be a trait of $F$ over a complete discrete valuation ring $V$, and let $b \colon \Lambda \to V$ be compatible with $y$. Then after a finite extension $V \to V'$ there are a lower base $L$, a basis $\varepsilon_k$ of the symmetric forms adapted to a cone of $\varphi$, values $s_k \in V'$, and degeneration data $D'$ of the pullback of $G$ that come from $L$ (`DegFrom`). The full list of conditions is in [the entry with the proof](/entry/exists-deg-from-of-trait/).

## Proof

The statement is the same as that of `GlobalTheory.TChart.exists_degFrom_of_trait`, and the proof applies it.

## In the Lean code

The theorem is in [ExistsDegenerationDataTautologicalChartOfTraitStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsDegenerationDataTautologicalChartOfTraitStatement.lean#L12). The proof is `first | exact @GlobalTheory.TChart.exists_degFrom_of_trait | ...`, and the type is copied word for word.

The hypothesis that $b$ is compatible with $y$ is never used in the proof. See [the entry with the proof](/entry/exists-deg-from-of-trait/).
