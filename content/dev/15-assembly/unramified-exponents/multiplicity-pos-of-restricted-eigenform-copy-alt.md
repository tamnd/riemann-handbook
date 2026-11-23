---
id: multiplicity-pos-of-restricted-eigenform-copy-alt
title: The second level datum on the twisted copy, the relay in the namespace T
kind: theorem
decl: GlobalTheory.T.multiplicity_pos_of_restricted_eigenform_copy_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.MultiplicityPosOfRestrictedEigenformCopy
covers: 370
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It has the same statement as [the second level datum on the twisted copy](/entry/multiplicity-lower-bound-of-restricted-copy-alt/), in the same file, and it proves it by calling that theorem. The real content is lower, in the transfer lemmas that the original calls, such as [the restaging of the series data](/entry/series-restage-of-carry-alt/). The user is [a second level datum after a change of base](/entry/exists-level-b1-carried-of-level-i-same-gal/), in its step 4.

## Statement

Assume `PublishedInputsThirdLayerAlt`, `SerN` and $h_L \in$ `RecTExists`, and the data of a change of base at one context, up to a stage $x''$ whose intermediate level datum is the twist by a copy $N$ of the one at $x'$. Then $x''$ has a second level datum. [The original](/entry/multiplicity-lower-bound-of-restricted-copy-alt/) lists the hypotheses.

## Proof

The proof is

```
first | exact @GlobalTheory.HeightCounting.Up.multiplicity_lower_bound_of_restricted_copy_alt | ...
```

The two statements are the same text, so the first branch closes the goal. The other branches of `first` are fallbacks that are not needed.

## In the Lean code

The theorem is in [MultiplicityPosOfRestrictedEigenformCopy.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MultiplicityPosOfRestrictedEigenformCopy.lean#L35), and the original at line 22. It differs from the original only in the namespace (`GlobalTheory.T` here, `GlobalTheory.HeightCounting.Up` for the original) and in the option `maxHeartbeats 1000000`. The name says "multiplicity pos"; the conclusion is that a structure is nonempty, and no multiplicity appears.
