---
id: facts-of-galois-preconditions-of-cut-rec
title: The norm choice facts from the Galois preconditions and CutRec
kind: theorem
decl: UpperTheory.GalC.facts_of_galois_preconditions_of_cutRec
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.CFacts
covers: 314
status: drafted
drafted_by: writer@claude
---
This theorem turns the record `GaloisPreconditions` of a datum into the larger record `NormChoiceFacts`, when the datum also satisfies `CutRec`. Its caller is [a good cut with the norm choice facts and the four ties](/entry/exists-good-cut-facts-tie4/), which applies it to the cut datum. That result goes to [the closed link bound](/entry/final-alt-alt/), in branch 1 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). Below this theorem are 314 declarations.

## Statement

`CutRec D` says that the condition `Nc` holds for the local parameter of each automorphic point of $D$ at each place above $g_0$ and $g_1$. We have not unfolded `Nc`.

**Theorem.** Assume the Chebotarev input `TwSys.Cheb` and the three local Galois cohomology inputs `LocalFiniteness`, `LocalTateDuality` and `LocalEulerChar`. Let $D$ be a datum and $x$ a norm choice of $D$. If `GaloisPreconditions D x` and `CutRec D` hold, then `NormChoiceFacts D x` holds.

`GaloisPreconditions` has 18 fields. `NormChoiceFacts` has 21 fields. Seventeen of them are fields of `GaloisPreconditions`. The other four are `Conclusion2`, `g2`, `admJ` and `duties`, and the 18th old field `z` becomes a part of `Conclusion2`.

## Proof

The 17 shared fields are copied. The four new fields are made as follows.

1. `residualRankPartExists_of_jointCondition` gives `RbEx D` from the residual condition in the field `what₂`. The admissibility field `adm` gives `tie0 D` and `adm1 D`.
2. `de_rham_points_weight_jumps_alt`, from `tie0`, `adm1`, the conditions `a2` and `a5` of `what₂`, and `CutRec`, gives `g2`: the de Rham condition at the good points, and the condition `DeRhamJumpsDistinctCondition`.
3. `Conclusion2` is a triple. Its first part, `ConclusionG5`, comes from `prvG5_of_admissible_cutRec`, which uses the three local inputs, `adm`, `RbEx D` and `CutRec`. Its second part, `ConclusionG6`, comes from `prvG6_of_admissible'` with `adm` and `RbEx D`. Its third part is `z`.
4. `admJ` comes from `admJ_of_admPar` for each size datum $L$ with `AdmPar L`. It uses the same inputs as step 2, together with the fields `weight` and `block`.
5. `duties` comes from `duties_of_large_aux41`, from `TwSys.Cheb`, the field `large`, the first part of `Conclusion1`, the second part of `g2`, and the field `rhoBar`.

## In the Lean code

The theorem is in [CFacts.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CFacts.lean#L45). `NormChoiceFacts` and its base `CoreNormFacts` are in [NormChoiceFacts.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/NormChoiceFacts.lean#L13). The lemmas of steps 3 to 5 are in [AdmissibleJOfRestricted.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AdmissibleJOfRestricted.lean#L20), and the lemma of step 2 is in [DeRhamPointsWeightJumps.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/DeRhamPointsWeightJumps.lean#L15).

Every hypothesis is used. `CutRec` is used three times: in steps 2, 3 and 4. Step 4 calls `de_rham_points_weight_jumps_alt` again inside `admJ_of_admPar`, so the proof makes `g2` twice.
