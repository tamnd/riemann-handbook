---
id: move-to-base-of-inputs-ser-n
title: Moving a third level datum to an enlarged base, the relay in the namespace T
kind: theorem
decl: GlobalTheory.T.moveToBase_of_inputs_serN
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.MultiplicityBoundOfLocalComponents
covers: 403
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It has the same statement as [moving a third level datum to an enlarged base](/entry/multiplicity-bound-of-local-components-alt/), in the same file, and it proves it by calling that theorem. The real content is one step lower, in [a second level datum after a change of base](/entry/exists-level-b1-carried-of-level-i-same-gal/). The user is [the second nonvanishing statement](/entry/second-no-of-s-mt-s-rat-s-cusp-s-finl/), which uses it as one of nine stage statements that it joins with `Step.and`. Below this theorem are 403 declarations.

## Statement

Assume `PublishedInputsThirdLayerAlt`, `SerN` and $h_L \in$ `RecTExists`. Then `MoveToBase hL` holds: eventually in the context, a third level datum at a stage over a base $B$ gives a stage over an enlargement $B'$ of $B$ with a third level datum, with the twist data carried along and with the list condition kept. [The original](/entry/multiplicity-bound-of-local-components-alt/) states this in full.

## Proof

The proof is

```
first | exact @GlobalTheory.HeightCounting.Up.multiplicity_bound_of_local_components_alt | ...
```

The two statements are the same text, so the first branch closes the goal. The other branches of `first` are fallbacks that are not needed.

## In the Lean code

The theorem is in [MultiplicityBoundOfLocalComponents.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MultiplicityBoundOfLocalComponents.lean#L31), and the original at line 17. It differs from the original only in the namespace (`GlobalTheory.T` here, `GlobalTheory.HeightCounting.Up` for the original) and in the option `maxHeartbeats 1000000`. The caller `secondNo_of_sMt_sRat_sCusp_sFinl` is in [FiniteLevelAndSecond.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FiniteLevelAndSecond.lean#L79).
