---
id: is-order-reduction-order-family-of-strict-transform-is-blowup
title: Order reduction for the canonical rules
kind: theorem
decl: FunctorialResolution.EmbeddedResolution.OrderReductionProperties.isOrderReduction_orderFamily_of_strictTransformIsBlowup
module: Development.ResolutionOfSingularities.EmbeddedResolution.IdealPrincipalization.OrderReduction.OrderReductionCompatibility
covers: 1293
status: drafted
drafted_by: writer@claude
---
This theorem is item 4 of [the rules reduce by dimension, given the hypotheses](/entry/is-correct-canonical-algorithm-rules-of-hypotheses/): the field `orderSpec` of `ReducesInductivelyOnDimension` for the canonical rules. It is a restatement of [order reduction by maximal contact](/entry/is-order-reduction-max-contact-of-is-boundary-position-invariant/), which has the real content. The only step here is that the order reduction rule of the canonical rules is the maximal contact assignment by definition.

## Statement

We use the notation of [the rules reduce by dimension, given the hypotheses](/entry/is-correct-canonical-algorithm-rules-of-hypotheses/). Let $h_{\mathrm{res}}$ prove `StrictTransformIsBlowupOfClosedSubscheme`. Let $n \in \mathbb{N}$, let $(A_j)_{j \in \mathbb{N}}$ be a family of assignments and let $L, L'$ be assignments. Assume

1. $\mathrm{MaxOrd}_{\delta < n}(L, L')$;
2. $\mathrm{Div}_{\delta \leq n, j}(A_j, L)$ for all $j$;
3. $\mathrm{Pos}_{\delta \leq n}(A)$.

Then $\mathrm{Ord}_{\delta \leq n}(\mathcal{B}(h_{\mathrm{res}})^{\mathrm{ord}}(A), L)$: the order reduction assignment of the canonical rules, fed with the family $A$, is an order reduction up to dimension $n$ relative to $L$.

## Proof

Let $\mathcal{M}(A)$ be the maximal contact assignment `maxContactPrincipalization comapIsoInvariance A`. By [order reduction by maximal contact](/entry/is-order-reduction-max-contact-of-is-boundary-position-invariant/), applied with the proved invariance `comapIsoInvariance`, $\mathcal{M}(A)$ satisfies the conclusion. The two assignments $\mathcal{B}(h_{\mathrm{res}})^{\mathrm{ord}}(A)$ and $\mathcal{M}(A)$ are equal: for each $T$ both unfold to `MaxContactReduction.reduceOrder comapIsoInvariance T (fun S _ j => A j S)`. Rewrite with this equality.

## In the Lean code

The theorem is in [OrderReductionCompatibility.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/OrderReduction/OrderReductionCompatibility.lean#L1011). The proof calls `isOrderReduction_maxContact_of_isBoundaryPositionInvariant`, proves the equality by `funext T; rfl`, and rewrites.

The hypothesis $h_{\mathrm{res}}$ does no work. It enters only through the name $\mathcal{B}(h_{\mathrm{res}})$, and the order rule of `canonicalAlgorithmRules` ([CanonicalPrincipalization.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/CanonicalPrincipalization.lean#L30)) does not use it: only the divisor rule does. So the name part "of strict transform is blowup" names an idle hypothesis.
