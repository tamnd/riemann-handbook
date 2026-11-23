---
id: mem-of-series-carry-alt
title: Carrying the series data to the twisted copy, the relay in the namespace T
kind: theorem
decl: GlobalTheory.T.mem_of_series_carry_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.SeriesRestageOfCarry
covers: 310
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It has the same statement as `series_restage_of_carry_alt`, the [restaging of the series data](/entry/series-restage-of-carry-alt/), in the same file, and it proves it by calling that theorem. The real content is there. The user is [the second level datum on the twisted copy](/entry/multiplicity-lower-bound-of-restricted-copy-alt/), in its step 2.

## Statement

Take the hypotheses of [the user](/entry/multiplicity-lower-bound-of-restricted-copy-alt/). Add a family of units $c_{\mathrm{Hk}}(i, b, P)$ of the rings $O_i$ of the twist data of $D(x'')$, one for each twist index $i$, boolean $b$ and place $P$, equal to the units of the side datum at $x$ at the same indices. Then there are a real structure `YS` and a datum $X$ of type `NExpTied` for $D(x'')$ with:

1. the components `QP` and `DP` of $X$ are the values of `qpOf` at the place choice $P_q$ of $x''$;
2. at each split place $P$ outside the set $S_0(i)$ and each $k \le r$, the map `YS.eF` turns the Hecke operator of $D(x'')$ into $c_{\mathrm{Hk}}(i, b, P)^k$ times the Hecke operator `hkF` of the rational datum of $l''$;
3. the maps `(YS.fi i).e` are the identity;
4. there is a series datum of type `SerAt`;
5. `TauTrue X`: the values `tauG` of $X$ are the images, under the side embedding, of homomorphisms from the units of $\mathbb{Z}/g$ to the units of the ring `LL0`.

We have not unfolded `NExpRealS`, `NExpTied`, `qpOf` or `hkF`.

## Proof

The proof is `exact series_restage_of_carry_alt`, inside a `first | … | …` tactic that tries three forms of the same call. There is no other content.

## In the Lean code

The theorem is in [SeriesRestageOfCarry.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SeriesRestageOfCarry.lean#L39), and the original at line 22. It differs from the original only in the namespace (`GlobalTheory.T` here, `GlobalTheory.HeightCounting.SerCarry` for the original) and in the option `maxHeartbeats 1000000`.

The proof of the original names the published inputs and `SerN` but never uses them, and it drops the eight matching hypotheses on $x''$ and $l''$. It calls `exists_move_alt`, `st_facts_alt` (twice), `sideB_facts` and `series_move`, whose proofs we have not read. The name says "mem"; no membership appears in the conclusion.
