---
id: multiplicity-lower-bound-of-restricted-copy-alt
title: The second level datum on the twisted copy
kind: theorem
decl: GlobalTheory.HeightCounting.Up.multiplicity_lower_bound_of_restricted_copy_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.MultiplicityPosOfRestrictedEigenformCopy
covers: 369
status: drafted
drafted_by: writer@claude
---
This theorem builds the second level datum at the twisted stage $x''$ in step 4 of [a second level datum after a change of base](/entry/exists-level-b1-carried-of-level-i-same-gal/). It assembles the datum from three transfer lemmas, one for each part of the series data. It reaches its user through [a relay](/entry/multiplicity-pos-of-restricted-eigenform-copy-alt/).

## Statement

The setting is that of [the user](/entry/exists-level-b1-carried-of-level-i-same-gal/), at one fixed context $K$, with all the data of its proof up to step 3 as hypotheses. Assume `PublishedInputsThirdLayerAlt`, `SerN` and $h_L \in$ `RecTExists`. Let $B', f', T', w'$ satisfy `KPx`, `Forced` and `Start`, with $K$ over $B'$, and let every stage family over $K$ satisfy `HostHyp` and $8 f r + 4 \le n_V$. Let $B, w, P, x, P', x'$ be as in `MoveToBase`, with a third level datum $l_b$ at $x$ and an intermediate level datum $l'$ at $x'$. Let $(N, \iota, e)$ satisfy `CopyN` $(D(x), N, \iota, e)$. Let $x''$ be a stage of $P'$ with an intermediate level datum $l''$, whose point is the twist of that of $x'$ by $N$, and whose level characters and seven components of $l''$ match those of $l'$ after the twist.

**Theorem.** Then $x''$ has a second level datum.

## Proof

A second level datum is $l''$ with a `SeriesData` field: a settings forms datum, a real structure `YS`, an equation between two maps `eF`, a fact `fi`, a series datum `ser` of type `SerAt` and a fact `tau` of type `TauTrue`.

1. `hecke_eigenform_copy_transfer_upper_alt` gives units $c_{\mathrm{Hk}}(i, b, P)$ in the rings $O_i$ of the twist data of $D(x'')$. They equal the units of the side datum of $l_b$ at the same indices.
2. [Carrying the series data](/entry/mem-of-series-carry-alt/) takes these units. It gives `YS`, a datum $X$ of type `NExpTied`, the facts `fi`, `ser` and `tau`, and two compatibilities of $X$ and `YS` with $l''$.
3. `side_eigenform_copy_transfer_alt` gives a settings forms datum $b_0$ for $l''$ whose side datum has export part $X$ and map `YS.eF`. Its proof reads the fields `what₂.art`, `what₂.fin`, `what₂.gal` and `what₂.cheb` of the published inputs.
4. These parts fill the structure. The rest is bookkeeping.

## In the Lean code

The theorem is in [MultiplicityPosOfRestrictedEigenformCopy.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MultiplicityPosOfRestrictedEigenformCopy.lean#L22). The level structures are in [SameGaloisLevelExists.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SameGaloisLevelExists.lean#L34) and `SeriesData` in [RootsOfUnityRingLeWittIntegers.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RootsOfUnityRingLeWittIntegers.lean#L52). We have read the statements of the lemmas of steps 1 and 3, not their proofs beyond the first lines.

The hypotheses on $K$ over $B'$ and on the stage families go only to step 2. The names speak of a lower bound or positivity of a multiplicity and of a restricted eigenform. The conclusion is only that a structure is nonempty; no multiplicity appears.
