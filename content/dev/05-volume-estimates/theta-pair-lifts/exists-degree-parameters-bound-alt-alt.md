---
id: exists-degree-parameters-bound-alt-alt
title: Degree parameters for the Hilbert-Samuel claim, second name
kind: theorem
decl: GlobalTheory.T.exists_degree_parameters_bound_alt_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ExistsDegreeParametersBound
covers: 812
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [hsClaim_short_alt_alt](/entry/hs-claim-short-alt-alt/). It gives, on each component of a good cover, numbers $n, \Lambda, \beta, \Lambda_D, \Lambda_T, J$ with explicit bounds, for which the inequality `HSClaimS` holds at the top weight. Its only user is [hilbertSamuel_of_component_estimates_alt](/entry/hilbert-samuel-of-component-estimates-alt/), which uses it in step 1. Below this theorem are 812 declarations.

## Statement

**Theorem.** Assume $\mathsf{HypothesesX}$, `PublishedHodgeBundleTheorems`, `GrothendieckDeformation`, `Quoted`, `SiegelToroidalIntegral`, `ToroidalForFanKS`, `SemiAbelianLieSeminegative`, and the cover statements `DeepGoodness`, `SizeCondition` and `FlatDegreeCondition`. Then the cover statement of [hsClaim_short_alt_alt](/entry/hs-claim-short-alt-alt/) holds.

The bounds on the six numbers and the form of `HSClaimS` are stated in that entry and in [the estimate at one level](/entry/hilbert-samuel-estimate-at-level/).

## Proof

The proof is `first | exact hsClaim_short_alt_alt | ...`. The two statements are the same, hypothesis for hypothesis.

## In the Lean code

The theorem is at [ExistsDegreeParametersBound.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsDegreeParametersBound.lean#L84), in the same file as the theorem that it renames. The statement is copied in full, on one line of about 1800 characters. There is a second pair with the same statement in the folder `HodgeBundleWeights`: `exists_degree_parameters_bound_alt` renames `hsClaim_short_alt`. All the content is in [hsClaim_short_alt_alt](/entry/hs-claim-short-alt-alt/).
