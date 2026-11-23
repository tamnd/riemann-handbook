---
id: series-restage-of-carry-alt
title: Carrying the series datum to the twisted stage
kind: theorem
decl: GlobalTheory.HeightCounting.SerCarry.series_restage_of_carry_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.SeriesRestageOfCarry
covers: 309
status: drafted
drafted_by: writer@claude
---
This theorem moves the series part of a third level datum at a stage $x$ to the twisted stage $x''$ after a change of base. It is step 2 of [the second level datum on the twisted copy](/entry/multiplicity-lower-bound-of-restricted-copy-alt/), which it reaches through the second name [`mem_of_series_carry_alt`](/entry/mem-of-series-carry-alt/).

## Statement

The setting is that of the parent entry: the published inputs, `SerN`, $h_L$, the bases $B'$ and $B$, the stages $x$, $x'$, $x''$ with a third level datum $l_b$ at $x$ and intermediate level data $l'$, $l''$, the copy $(N, \iota, e)$, and the matching of $l''$ with $l'$ after the twist. In addition, let $c_{\mathrm{Hk}}(i, b, P)$ be units of the rings $O_i$ of the twist data of $D(x'')$ that equal the units of the side datum of $l_b$ at the same indices.

**Theorem.** There are a real structure `YS` over the real datum of $x''$ and a datum $X$ of type `NExpTied` for $D(x'')$ with these properties:

1. `PqLaw`: the two place components `QP` and `DP` of each matrix part of $X$ are given by the place map $P_q$ of $l''$;
2. at each split place $P$ outside the excluded set $S_0(i)$ and each $k \le r$, the map `YS.eF` turns the map `hkF` at $(k, P)$ of $D(x'')$ into $c_{\mathrm{Hk}}(i, b, P)^k$ times the map `hkF` at $(k, P)$ built from the rational datum of $l''$;
3. the maps `YS.fi i` are the identity;
4. there is a series datum `SerAt` for `YS`, $X$ and the data of $l''$;
5. `TauTrue` $X$.

## Proof

1. `exists_move_alt` gives a copy `CopyAll` of $D(x)$ onto $D(x'')$, the same character frame at both stages, equal place maps $P_q$, geometric halves at $x$ and $x''$, and a real move `RealMove` between the real sides.
2. `st_facts_alt`, used for $l_b$ and for $l''$, gives the Hecke condition `HkAd` and the matrix condition `KeepsMat` at both stages.
3. `sideB_facts` gives `HkLaw`, `LowIn` and `PqLaw` for the side datum of $l_b$.
4. `series_move` carries the series datum and `TauTrue` of $l_b$ along the move. With `PqLaw` and `HkLaw` unfolded, this is the conclusion.

## In the Lean code

The theorem is in [SeriesRestageOfCarry.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SeriesRestageOfCarry.lean#L22). The lemmas: `exists_move_alt` in [ExistsMove.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsMove.lean#L18), `st_facts_alt` in [StFacts.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/StFacts.lean#L16), `sideB_facts` in [Lb1OfRestagingBound.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/Lb1OfRestagingBound.lean#L21) and `series_move` in [ExportTieMove.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExportTieMove.lean#L98).

Odd points:

- The proof introduces `PublishedInputsThirdLayerAlt` and `SerN` as `hPr` and `hSer` and does not use them.
- The eight `HEq` hypotheses that match $l''$ with $l'$ are introduced as `_` and not used. So $l'$ plays no role.
- The same file has the second name `mem_of_series_carry_alt` at [line 39](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SeriesRestageOfCarry.lean#L39). `Lb1OfRestagingBound.lean` has an older copy, `series_restage`, with `PrN` and `LocalLanglandsGL` in place of the published inputs and $h_L$.
- No restaging or carry object appears in the statement.
