---
id: exists-semi-abelian-extension-near-point
title: A semi-abelian extension near each point (statement)
kind: theorem
decl: GlobalTheory.T.exists_semiAbelianExtension_near_point
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsSemiAbelianExtensionNearPointStatement
covers: 646
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`Desc.exists_hasExt_near`](/entry/exists-has-ext-near/), which has the real content (645 of the 646 declarations below this one). It is step 1 of [the semi-abelian extension from complete regular charts](/entry/descent-semi-abelian/): it gives the local extensions that the next step glues.

## Statement

Take $S$, $j \colon X \to S$, $A$, $L$ and the charts as in [the entry above](/entry/descent-semi-abelian/): $S$ noetherian and normal, $j$ a dense open immersion, $A$ an abelian scheme over $X$ with a relatively ample line bundle $L$, and a chart at each point of $S$.

**Theorem.** For each $s \in S$ there is an open $U \subseteq S$ with $s \in U$ such that the restriction of $A$ to $j^{-1}(U)$ extends to a semi-abelian scheme over $U$. That is, there are a semi-abelian scheme $G_U$ over $U$ and a map $A|_{j^{-1}(U)} \to G_U$ that identifies $A|_{j^{-1}(U)}$ with the pullback of $G_U$ to $j^{-1}(U)$, as group schemes.

## Proof

The proof is `GlobalTheory.Desc.exists_hasExt_near`, with no change.

## In the Lean code

The theorem is at [ExistsSemiAbelianExtensionNearPointStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsSemiAbelianExtensionNearPointStatement.lean#L10). Its proof is a `first | exact ...` that applies `exists_hasExt_near`. The two statements are the same, word for word. The condition "extends to a semi-abelian scheme" is `HasExt` in [SubsetSpanBy.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/SubsetSpanBy.lean#L223).
