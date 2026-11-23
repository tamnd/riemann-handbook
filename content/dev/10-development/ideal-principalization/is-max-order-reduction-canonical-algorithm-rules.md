---
id: is-max-order-reduction-canonical-algorithm-rules
title: The maximal order rule of the canonical rules is a maximal order reduction
kind: theorem
decl: FunctorialResolution.EmbeddedResolution.MaxOrderReduction.isMaxOrderReduction_canonicalAlgorithmRules
module: Development.ResolutionOfSingularities.EmbeddedResolution.IdealPrincipalization.MarkedOrderReduction.MaxOrderReduction
covers: 640
status: drafted
drafted_by: writer@claude
---
This theorem is item 3 of [the rules reduce by dimension, given the hypotheses](/entry/is-correct-canonical-algorithm-rules-of-hypotheses/). It is a second name for [maximal order reduction by the order reduction sequence](/entry/is-max-order-reduction-order-reduction-seq/), which has the content.

## Statement

We use the notation of the parent entry. Let $h_{\mathrm{res}}$ prove `StrictTransformIsBlowupOfClosedSubscheme`, and assume `PrincipalizationGeometryHypotheses`. Let $n \in \mathbb N$ and let $A$, $L$ be assignments.

**Theorem.** If $\mathrm{Ord}_{\delta \le n}(A, L)$, then $\mathrm{MaxOrd}_{\delta \le n}(\mathcal B^{\max}(A), A)$, where $\mathcal B$ are the canonical rules.

## Proof

By definition, $\mathcal B^{\max}(A)(T)$ is `orderReductionSeq` for $T$ with the proved `comapIsoInvariance`, applied to $A$ on the marked ideals of $\delta \le \delta(T)$. So the theorem is `isMaxOrderReduction_orderReductionSeq` with these arguments. Lean checks the match by unfolding `canonicalAlgorithmRules` and `maxOrderFamily`.

## In the Lean code

The theorem is in [MaxOrderReduction.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/MarkedOrderReduction/MaxOrderReduction.lean#L123). The rules are in [CanonicalPrincipalization.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/CanonicalPrincipalization.lean#L26).

The hypothesis $h_{\mathrm{res}}$ appears only to name the canonical rules. It is used there by the divisor rule, not by the maximal order rule. In the canonical rules, the maximal order rule is `orderReductionSeq` and the order rule is the maximal contact `reduceOrder`, so the names cross, as the parent entry says.
