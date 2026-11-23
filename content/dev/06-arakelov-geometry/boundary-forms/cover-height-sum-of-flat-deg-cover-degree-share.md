---
id: cover-height-sum-of-flat-deg-cover-degree-share
title: The Hilbert-Samuel bound on cover components, second name
kind: theorem
decl: GlobalTheory.T.coverHeightSum_of_flatDeg_coverDegree_share
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.HilbertSamuelLowerBoundOfComponents
covers: 831
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [hilbertSamuel_of_component_estimates_alt](/entry/hilbert-samuel-of-component-estimates-alt/). It proves the cover statement `CoverHeightSum`, a lower bound of Hilbert-Samuel type for the degrees of cusp lattices on the components of a good cover. Its only caller is [the covolume bound](/entry/top-covol-g-alt-alt/), which uses it in step 3, with `sum_c_of_deep_good`, to get a uniform lower bound for a slope on the cover. Below this theorem are 831 declarations.

## Statement

**Theorem.** Assume $\mathsf{HypothesesX}$, `PublishedHodgeBundleTheorems`, `GrothendieckDeformation`, `Quoted`, `SiegelToroidalIntegral`, `ToroidalForFanKS` and `SemiAbelianLieSeminegative`, and the cover statements `DeepGoodness`, `SizeCondition`, `FlatDegreeCondition`, `CoverDegree` and `ShareCondition`. Then `CoverHeightSum` holds.

The inequality inside `CoverHeightSum` (`HSAt`) is stated in [the entry of the theorem with content](/entry/hilbert-samuel-of-component-estimates-alt/).

## Proof

The proof is `first | exact hilbertSamuel_of_component_estimates_alt | ...`. The two statements are the same, hypothesis for hypothesis.

## In the Lean code

The theorem is at [HilbertSamuelLowerBoundOfComponents.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/HilbertSamuelLowerBoundOfComponents.lean#L128), in the same file as the theorem that it renames. The name lists three of the twelve hypotheses (flat degree, cover degree, share). The names of the two theorems describe the same result from two sides: the inputs here, the Hilbert-Samuel bound there. All the content is in [hilbertSamuel_of_component_estimates_alt](/entry/hilbert-samuel-of-component-estimates-alt/).
