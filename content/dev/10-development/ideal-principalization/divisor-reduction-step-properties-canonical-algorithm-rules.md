---
id: divisor-reduction-step-properties-canonical-algorithm-rules
title: The step properties of divisor reduction
kind: theorem
decl: FunctorialResolution.EmbeddedResolution.divisorReductionStepProperties_canonicalAlgorithmRules
module: Development.ResolutionOfSingularities.EmbeddedResolution.IdealPrincipalization.DivisorReduction.CanonicalDivisorReduction
covers: 429
status: drafted
drafted_by: writer@claude
---
This private theorem supplies the field `divisorReduction` of [the divisor reduction facts for the canonical rules](/entry/divisor-reduction-hypotheses-canonical-algorithm-rules/). It is a pass-through. The real content is in [the divisor reduction properties](/entry/divisor-reduction-properties-of-blowup-preserves-noetherian/).

## Statement

Let $\mathrm{hres}$ be the statement that a strict transform is a blow-up. Then `DivisorReductionStepProperties hres blowupPreservesNoetherian` holds. This structure has twenty fields on one step of divisor reduction at a boundary divisor $D_j$ of an admissible marked ideal $(X, I, m, E)$. Let $Z_j$ be the subscheme cut out by `containedComponentsIdeal`. Six fields are these: $I = I_{Z_j}^m \cdot J$ for some ideal $J$ when $\operatorname{ord}_x I \le m$ at all $x$; the identity of $X$ is a blow-up along $I_{Z_j}$; $Z_j$ is smooth over the base; $Z_j$ has strict normal crossings with $E$; $Z_j$ lies in the locus where $\operatorname{ord} I \ge m$; and the restriction of $T$ to $D_j$ is admissible when $Z_j$ is empty, the order is at most $m$ and $T$ is balanced. The other fourteen are the fields of `DivisorReductionProperties`.

## Proof

The proof is one line:

```
(divisorReductionProperties_of_blowupPreservesNoetherian hres blowupPreservesNoetherian).toDivisorReductionStepProperties
```

The conversion `toDivisorReductionStepProperties` copies the fourteen fields. It fills the six others with lemmas on $Z_j$: `exists_mul_pow_containedComponentsIdeal_eq_ideal`, `isBlowupAlongIdealSheaf_id_containedComponentsIdeal`, `smooth_subschemeι_containedComponentsIdeal_comp`, `hasStrictNormalCrossingsWith_containedComponentsIdeal`, `support_containedComponentsIdeal_subset_orderAtLeastLocus` and `DivisorReduction.isAdmissible_restrictToDivisor`. We have not unfolded their proofs.

## In the Lean code

The theorem is in [CanonicalDivisorReduction.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/DivisorReduction/CanonicalDivisorReduction.lean#L151) and is `private`. The conversion is in [DivisorReductionProperties.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/DivisorReduction/DivisorReductionProperties.lean#L231).
