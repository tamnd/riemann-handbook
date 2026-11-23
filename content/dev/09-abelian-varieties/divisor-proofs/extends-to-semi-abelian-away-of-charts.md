---
id: extends-to-semi-abelian-away-of-charts
title: Extension over Spec R from charts, statement form
kind: theorem
decl: GlobalTheory.T.extendsToSemiAbelian_away_of_charts
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExtendsToSemiAbelianAwayOfChartsStatement
covers: 636
status: drafted
drafted_by: writer@claude
---
This theorem is the statement form of [`hasExt_awayMap_of_charts`](/entry/has-ext-away-map-of-charts/). It has the same statement, and its proof applies that theorem. Its only user is [`hasExt_opensRange`](/entry/has-ext-opens-range/), which reduces the extension over an affine open of a general base to this case.

## Statement

Let $R$ be a noetherian integrally closed domain and $f \in R$ with $f \neq 0$. Let $A$ be an abelian scheme over $\operatorname{Spec} R_f$ with a relatively ample line bundle $L$. Suppose that $A$ has a chart at each point $x$ of $\operatorname{Spec} R$, relative to the open immersion $\operatorname{Spec} R_f \to \operatorname{Spec} R$.

**Theorem.** Then $A$ extends to a semi-abelian scheme over $\operatorname{Spec} R$: there are a semi-abelian scheme $G$ over $\operatorname{Spec} R$ and a map $A \to G$ that identifies $A$ with $G \times_{\operatorname{Spec} R} \operatorname{Spec} R_f$ as group schemes.

Charts, semi-abelian schemes and the predicate `HasExt` are defined in [the entry above](/entry/has-ext-opens-range/).

## Proof

The proof is `GlobalTheory.Desc.hasExt_awayMap_of_charts`, applied to all the arguments. There is nothing else. The content is in [`hasExt_awayMap_of_charts`](/entry/has-ext-away-map-of-charts/).

## In the Lean code

The theorem is at [ExtendsToSemiAbelianAwayOfChartsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExtendsToSemiAbelianAwayOfChartsStatement.lean#L10). The proof is the tactic `first | exact @GlobalTheory.Desc.hasExt_awayMap_of_charts | ...`. The two statements are written in the same words, so the first branch fits.
