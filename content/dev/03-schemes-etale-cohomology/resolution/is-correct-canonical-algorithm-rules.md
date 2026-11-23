---
id: is-correct-canonical-algorithm-rules
title: The canonical principalization rules reduce by dimension, for each strict transform law
kind: theorem
decl: FunctorialResolution.EmbeddedResolution.isCorrect_canonicalAlgorithmRules
module: Development.ResolutionOfSingularities.EmbeddedResolution.IdealPrincipalization.CanonicalRulesCorrect
covers: 3838
status: drafted
drafted_by: writer@claude
---
This theorem removes two of the three hypotheses of [the rules reduce by dimension, given the hypotheses](/entry/is-correct-canonical-algorithm-rules-of-hypotheses/). It proves both of them. The one hypothesis left is the strict transform law $h_{\mathrm{res}}$. The entry [the canonical rules reduce by dimension](/entry/canonical-algorithm-rules-is-correct/) supplies $h_{\mathrm{res}}$ and is the only user of this theorem.

## Statement

Let $h_{\mathrm{res}}$ be a proof of `StrictTransformIsBlowupOfClosedSubscheme`: under a [[blow-up|4SFS82N88K]] of a locally noetherian scheme, the strict transform of a closed subscheme is the blow-up of that subscheme. Let $\mathcal{B}(h_{\mathrm{res}})$ be the canonical principalization rules built from $h_{\mathrm{res}}$. Then $\mathcal{B}(h_{\mathrm{res}})$ reduces inductively on dimension.

The rules and the four properties of "reduces inductively on dimension" are stated in [the rules reduce by dimension, given the hypotheses](/entry/is-correct-canonical-algorithm-rules-of-hypotheses/).

## Proof

Apply `isCorrect_canonicalAlgorithmRules_of_hypotheses` to $h_{\mathrm{res}}$ and to two proved results.

1. `divisorReductionHypotheses_canonicalAlgorithmRules` proves `DivisorReductionHypotheses` $h_{\mathrm{res}}$. This structure has nine fields. One says: if a marked ideal $(X, I, m, E)$ has a point where $I$ has order at least $m$, and its pullback along a smooth map $h$ has none, then the empty sequence of blow-ups is the pullback along $h$ of the divisor reduction sequence of that marked ideal. The others are named compatibilities: smooth pullback, flatness of smooth maps, field base change, invariance under a new order of the boundary, and two groups of properties of the divisor reduction step. We have not unfolded the eight named compatibility statements.
2. `principalizationGeometryHypotheses` proves `PrincipalizationGeometryHypotheses`. Its fields are facts on blow-ups in smooth centres with normal crossings with the boundary. Among them: after such a blow-up, the controlled transform of an ideal of constant order $c$ on the centre has order at most $c$ on the exceptional divisor, and no component of the exceptional divisor lies in its support. Other fields say that the order and monomial splittings are stable under field extension and smooth pullback. We have not read all fields.

## In the Lean code

The theorem is in [CanonicalRulesCorrect.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/CanonicalRulesCorrect.lean#L31). The proof is one term:

```
isCorrect_canonicalAlgorithmRules_of_hypotheses hres
  (divisorReductionHypotheses_canonicalAlgorithmRules hres) principalizationGeometryHypotheses
```

- `divisorReductionHypotheses_canonicalAlgorithmRules`, in [CanonicalDivisorReduction.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/DivisorReduction/CanonicalDivisorReduction.lean#L155). The structure is in [DivisorReductionHypotheses.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/DivisorReduction/DivisorReductionHypotheses.lean#L35).
- `principalizationGeometryHypotheses`, in [GeometricPrincipalization.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/MarkedOrderReduction/GeometricPrincipalization.lean#L27). The structure is in [GeometryHypotheses.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/MarkedOrderReduction/GeometryHypotheses.lean#L24).

The words "Hypotheses" in these two names are labels. Both structures are proved here, so they are not assumptions of the final proof. Of the 3,838 declarations below this theorem, the assembly step `isCorrect_canonicalAlgorithmRules_of_hypotheses` holds 2,363.
