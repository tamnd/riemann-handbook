---
id: chart-separation-data-defined-over-centre-field
title: Separation at the centre of a chart, stated
kind: theorem
decl: GlobalTheory.T.chartSeparation_data_defined_over_centre_field
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ChartSeparationDataDefinedOverCentreFieldStatement
covers: 798
status: drafted
drafted_by: writer@claude
---
This theorem is a second name. Its statement is $\mathrm{SepSt}$ and its proof is [`sepSt`](/entry/sep-st/), which has the real content. [The smooth blowup with pre-charts](/entry/chart-st5-holds/) uses it twice, for smoothness and for the pre-charts, both times to prove that the centre map of a tautological chart is an étale completion. Below this theorem are 798 declarations.

## Statement

$\mathrm{SepSt}$ is stated in full in [the proof entry](/entry/sep-st/). In short, let $\overline{S}$ be a normalized blowup of a theta compactification $Z$ of a Siegel moduli space, along a boundary ideal with the valuations $d\varphi$. Let $V$ be a local domain with degeneration data that are monomial in elements $s_1, \dots, s_m$ of the maximal ideal, with a $V$-point of $\overline{S}$. Let $\mathrm{ev} \colon V \to K$ be a geometric point over the closed point whose image in $\overline{S}$ is defined over an algebraically closed subfield $k_0$. Then the $\mathrm{ev}(s_k)$ are $0$, the abelian part is defined over $k_0$, and, if the data come from a ring that maps into $k_0$, the unit periods take values in $k_0$.

## Proof

The proof is the term `GlobalTheory.Poinc.Sep.sepSt`.

## In the Lean code

The theorem is in [ChartSeparationDataDefinedOverCentreFieldStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ChartSeparationDataDefinedOverCentreFieldStatement.lean#L12). The proof is `first | exact @GlobalTheory.Poinc.Sep.sepSt | ...`. The two callers are in [ExistsPreChartSiegelNormalizedBlowup.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsPreChartSiegelNormalizedBlowup.lean#L21) and [SmoothOfRelativeDimensionBlowup.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SmoothOfRelativeDimensionBlowup.lean#L168). Inside `tautologicalChart_centre_isCompletedEtaleLocalMap`, $\mathrm{SepSt}$ goes to `quasiFinite_tautologicalChart_of_separation`, which proves that the closed fibre of the centre map is one point and that the residue field extension is finite.
