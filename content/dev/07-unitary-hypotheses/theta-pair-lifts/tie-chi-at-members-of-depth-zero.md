---
id: tie-chi-at-members-of-depth-zero
title: Four tie conditions at each layer point (second name)
kind: theorem
decl: GlobalTheory.T.tieChi_at_members_of_depthZero
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.LocalTypeDeterminedAtAllPrimes
covers: 590
status: drafted
drafted_by: writer@claude
---
This theorem is a second name. It has the same statement as [`TypePrimesFinished.locComp_of_isRc_classMapD_cenLoc`](/entry/type-primes-finished-loc-comp-of-is-rc-class-map-d-cen-loc/), and its proof only calls that theorem. The real content is in that entry. Step 2 of [`final_of_alt`](/entry/final-of-alt/) calls this name to get the four tie conditions at every layer point. It is part of the [unitary hypotheses chapter](/proof/unitary-hypotheses/).

## Statement

Assume `HtCard`, `PublishedInputsThirdLayerAlt` and `DepthZeroSupport`. Then for each `hL : RecTExists`, at each layer point (`MemberAtLayerPoint hL`), the datum $D = $ `w.D Z` satisfies:

1. `tieChi D`;
2. there is a pending datum $Q$ with `admDZ Q` and `EigSpan Q`;
3. `TieInePoly D`;
4. `SerLoc D`.

The target entry explains these four conditions.

## Proof

The proof is `first | exact @TypePrimesFinished.locComp_of_isRc_classMapD_cenLoc | …`. The first branch closes the goal.

## In the Lean code

The theorem is at [LocalTypeDeterminedAtAllPrimes.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LocalTypeDeterminedAtAllPrimes.lean#L36). The target is in the same file, at line 22.

Neither name describes the statement well. The name `tieChi_at_members_of_depthZero` names only the first of the four conditions. The target name, `locComp_of_isRc_classMapD_cenLoc`, is the name of theorems in 21 files of the Lean tree, in other namespaces such as `PendLayer` and `SerFinished`, with other statements.
