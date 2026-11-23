---
id: level-i-same-gal-transfer-to-level-b1-list
title: A second level datum after a change of base, the relay in the namespace T
kind: theorem
decl: GlobalTheory.T.levelI_same_gal_transfer_to_levelB1_list
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.MultiplicityBoundTransferOfCmDatum
covers: 397
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It has the same statement as [a second level datum after a change of base](/entry/exists-level-b1-carried-of-level-i-same-gal/), in the same file, and it proves it by calling that theorem. The real content is lower, in the transfer lemmas that [the second level datum on the twisted copy](/entry/multiplicity-lower-bound-of-restricted-copy-alt/) calls. The user is [moving a third level datum to an enlarged base](/entry/multiplicity-bound-of-local-components-alt/), which takes from it the first of its two steps.

## Statement

Assume `PublishedInputsThirdLayerAlt`, `SerN` and $h_L \in$ `RecTExists`. Then, eventually in the context, a third level datum at a stage $x$ over a base $B$, and a stage $x'$ over an enlargement of $B$ with an intermediate level datum and the same Galois data, give a stage $x''$ next to $x'$ with a second level datum, with `Carried` $(D(x), D(x''))$ and with the list condition kept. [Its user](/entry/multiplicity-bound-of-local-components-alt/) states the setting in full.

## Proof

The proof is

```
first | exact @GlobalTheory.HeightCounting.Up.exists_levelB1_carried_of_levelI_same_gal | ...
```

The two statements are the same text, so the first branch closes the goal. The other branches of `first` are fallbacks that are not needed.

## In the Lean code

The theorem is in [MultiplicityBoundTransferOfCmDatum.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MultiplicityBoundTransferOfCmDatum.lean#L48), and the original at line 24. It differs from the original only in the namespace (`GlobalTheory.T` here, `GlobalTheory.HeightCounting.Up` for the original) and in the option `maxHeartbeats 1000000`. The name speaks of a "transfer to level B1 list"; the statement has a second level datum (`SecondIntermediateLevel`) and the list condition `ListSt`.
