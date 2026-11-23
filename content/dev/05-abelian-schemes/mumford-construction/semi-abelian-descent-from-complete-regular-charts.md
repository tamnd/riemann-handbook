---
id: semi-abelian-descent-from-complete-regular-charts
title: Semi-abelian extension from complete regular charts (statement)
kind: theorem
decl: GlobalTheory.T.semiAbelian_descent_from_complete_regular_charts
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.SemiAbelianDescentFromCompleteRegularChartsStatement
covers: 659
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`Desc.descent_semiAbelian`](/entry/descent-semi-abelian/), which has the real content (658 of the 659 declarations below this one). It lies below the [literature step](/step/every-character-of-literature/). Its users apply it to universal abelian schemes over moduli schemes, to extend them over a larger normal base.

## Statement

Let $S$ be a noetherian normal scheme, $j \colon X \to S$ a dense open immersion, and $A$ an abelian scheme over $X$ with a relatively ample line bundle. Suppose that each point $x \in S$ has a chart: a complete regular local ring $R$ of characteristic $0$ over the local ring at $x$, with a semi-abelian scheme over $R$ whose generic fibre is $A$ at the generic point of $\operatorname{Spec} R$. Then $A$ extends to a semi-abelian scheme $G$ over $S$, and each chart is the pullback of $G$.

The [entry for the proof](/entry/descent-semi-abelian/) gives every hypothesis in full.

## Proof

The proof is `GlobalTheory.Desc.descent_semiAbelian`, with no change.

## In the Lean code

The theorem is at [SemiAbelianDescentFromCompleteRegularChartsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SemiAbelianDescentFromCompleteRegularChartsStatement.lean#L10). Its proof is a `first | exact ...` that applies `descent_semiAbelian`. The two statements are the same, word for word.

It is used in `descSt` in [DescSt.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/DescSt.lean#L41), in `descSt5` in [DescSt5.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/DescSt5.lean#L34), and in `exists_semiAbelian_of_charts` in [ExistsSemiAbelianDescentOfToricChartsCorrectedSe.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsSemiAbelianDescentOfToricChartsCorrectedSe.lean#L70).
