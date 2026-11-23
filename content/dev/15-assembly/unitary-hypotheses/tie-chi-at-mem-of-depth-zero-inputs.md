---
id: tie-chi-at-mem-of-depth-zero-inputs
title: The first two tie conditions at every layer point, restated
kind: theorem
decl: GlobalTheory.T.tieChi_at_mem_of_depth_zero_inputs
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.PendingLayerConditionAtMember
covers: 550
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the first two tie conditions at every layer point](/entry/pend-layer-loc-comp-of-is-rc-class-map-d-cen-loc/). Its only user is [the four tie conditions at every layer point](/entry/type-primes-finished-loc-comp-of-is-rc-class-map-d-cen-loc/), which adds the other two parts of `Tie4`. That result goes to [the closed link bound, given a cut](/entry/final-of-alt/), in branch 1 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). Below this theorem are 550 declarations, one more than below the copy.

## Statement

The statement is that of the copy, word for word. Assume `HtCard`, the record `PublishedInputsThirdLayerAlt` of fourteen named inputs, and `DepthZeroSupport`. Let $h_L$ be an element of `RecTExists`. Then at every layer point for $h_L$, the datum $D$ of the point satisfies `tieChi`, and there is a pending datum $P$ of $D$ with `admDZ P` and `EigSpan P`. The [entry of the copy](/entry/pend-layer-loc-comp-of-is-rc-class-map-d-cen-loc/) says what a layer point is, and [the entry below it](/entry/tie-chi-of-lab-all-green-chi-cen/) says what the three conditions are.

## Proof

The proof is `exact PendLayer.locComp_of_isRc_classMapD_cenLoc`, inside a `first` tactic that tries three forms of the call.

## In the Lean code

The theorem is in [PendingLayerConditionAtMember.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PendingLayerConditionAtMember.lean#L62), in the namespace `GlobalTheory.T`. The copy is at line 46 of the same file, in `GlobalTheory.HeightCounting.Up.PendLayer`.

The name speaks of depth zero inputs. Of the hypotheses, only `DepthZeroSupport` matches it. The name does not say that the conclusion also contains the pending datum.
