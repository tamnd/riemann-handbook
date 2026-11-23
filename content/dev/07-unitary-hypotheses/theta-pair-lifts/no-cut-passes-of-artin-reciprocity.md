---
id: no-cut-passes-of-artin-reciprocity
title: The step statements without the cut, from Artin reciprocity (second name)
kind: theorem
decl: GlobalTheory.T.no_cut_passes_of_artin_reciprocity
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.StepsNoCutOfArtinStatement
covers: 383
status: drafted
drafted_by: writer@claude
---
This theorem is a second name. It has the same statement as [`stepsNoCut_of_artin_alt`](/entry/steps-no-cut-of-artin-alt/), and its proof only calls that theorem. The real content is in that entry. The [extra facts step](/entry/extra-from-facts-main-alt-alt/) calls this name to get `NoCutStatement` from Artin reciprocity. It is part of the [unitary hypotheses chapter](/proof/unitary-hypotheses/).

## Statement

`GlobalArtinReciprocity` implies `NoCutStatement`.

`GlobalArtinReciprocity` says: for each number field $E$ and each algebraic closure $\Omega$, there is a group map from the ideles of $E$ to the abelianized Galois group that satisfies `IsGlobalArtin`. `NoCutStatement` is a conjunction of sixteen step statements. The entry on [`stepsNoCut_of_artin_alt`](/entry/steps-no-cut-of-artin-alt/) lists them.

## Proof

The proof is `first | exact @stepsNoCut_of_artin_alt | …`. The first branch closes the goal.

## In the Lean code

The theorem is at [StepsNoCutOfArtinStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/StepsNoCutOfArtinStatement.lean#L11). `NoCutStatement` is at [StepsNoCut.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/StepsNoCut.lean#L38). `GlobalArtinReciprocity` is at [ExistsUniqueHcharOfFiniteOrder.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/ExistsUniqueHcharOfFiniteOrder.lean#L70). We have not unfolded `IsGlobalArtin`.

The name says that Artin reciprocity gives the result. In the proof of the target theorem, only one of the sixteen parts uses it.
