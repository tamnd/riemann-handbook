---
id: series-copy-embedding-alt
title: A twist that gives a series datum on the twisted copy of a stage
kind: theorem
decl: GlobalTheory.HeightCounting.SerCopy.series_copy_embedding_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.SeriesCopyEmbeddingOfCmDatum
covers: 350
status: drafted
drafted_by: writer@claude
---
This theorem chooses a new twist of the datum of a stage and proves that the twisted copy of the stage carries a series datum. Through the relay [`series_copy_embedding_of_cmDatum_alt`](/entry/series-copy-embedding-of-cm-datum-alt/) it is the main input of [`sb1l_alt_alt`](/entry/sb1l-alt-alt/), which builds a second level datum from a first one. Its only published input is global Artin reciprocity.

## Statement

The words *stage*, *level* and `SeriesData` are as in [`sb1l_alt_alt`](/entry/sb1l-alt-alt/). For a stage $x$, let $D_x$ be its datum (`Dof x`). A *new twist* $N$ of $D_x$ (type `TwNew`) is a twist datum `tw` with exponent data, theta data and local bridges at the twisting places. The point `oTw x N` is the point of $x$ with its twist replaced by $N$.

**Theorem.** Assume `PublishedInputsThirdLayerAlt`, `SerN` and $h_L$ in `RecTExists`. Let $K$ be over $B$, assume `Forced K B T`, and let $w$ be a column datum with `Start`. Let $x$ be a stage over $P$ and $l$ a first level datum over $x$. Then there is a new twist $N$ of $D_x$ with:

1. each $\lambda$-datum with `IsLamTieFull` for the twist of $D_x$ has `IsLamTieFull` for `N.tw`;
2. let $x'$ be a stage over $P$ with $x'.o = $ `oTw x N`, and $l'$ an intermediate level datum over $x'$. Suppose that the row and the rational data of $l'$ are the twists by $N$ of those of $l$; that $P_q$, the set $S_b$, the Hecke operators, the eigenvalues and the characters $\theta$ of $l'$ and $l$ agree; and that the real data, the group isomorphism and the geometric datum of $x'$ are transported from $x$. Then each `InMt` datum $m$ at $x'$ with identity frames gives `SeriesData` for the geometric datum of $x'$, the data of $l'$ and the frames of $m$.

## Proof

1. `isChoice_of_start_of_over` gives, from `Start` and $K$ over $B$, that for $k = 0, 1$ the $g_k(g_k - 1)$-th roots of unity in $\mathbb C$ lie in the image of the field $L_0$ of $D_x$.
2. `exists_prepared`, with global Artin reciprocity, the side datum $B_s$ of $l$, its valuation datum and step 1, gives a twist $N_1$ with item 1. Each twisting set and prime of $N_1$ is one of $D_x$; $N_1$ satisfies `NoOff` and `IsUnivChar`; and $N_1$ has a side datum with `TauTrue`.
3. The inclusions in `SettingsFormsData` of $l$ give $S_b \subseteq S_0(i)$ and the place condition `OverSet` for the twisting sets of $N_1$.
4. `pre_at_twisted_copy_of_side_b_tau_true` gives a datum $p$ of type `PreTie` on the copy. The twist $N$ is `nP p`: $N_1$ with its exponent and theta data taken from $p$. It has the same `tw`, so item 1 still holds.
5. For item 2, `series_state_b1_twist_alt` gives `SeriesData` from $p$, `TauTrue`, step 3 and the conditions on $x'$ and $l'$.

The rest is bookkeeping with `HEq` and dependent types.

## In the Lean code

The theorem is at [SeriesCopyEmbeddingOfCmDatum.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SeriesCopyEmbeddingOfCmDatum.lean#L35). The lemmas it calls: `isChoice_of_start_of_over` in [FactsStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FactsStatement.lean#L17), `exists_prepared` in [ExistsNewTwistLamFull.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsNewTwistLamFull.lean#L43), `pre_at_twisted_copy_of_side_b_tau_true` and `series_state_b1_twist_alt` in [SeriesStateB1OfGeometry.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SeriesStateB1OfGeometry.lean#L51), and `nP`, `lamT_spec`.

Odd points:

- `SerN` and `Forced K B T` are introduced as `_` and not used. Of `PublishedInputsThirdLayerAlt`, only `hPr.what₂.art` is used.
- In item 2 the hypothesis on `l'.rat.S` is introduced as `_` and not used.
- The field `rootsOfUnityRing_le_wittIntegers` of `SettingsFormsData` is the condition `OverSet`: each place of $S_0(i)$ lies over $\ell_i$ or over a prime of `lowAll`. No ring of roots of unity and no Witt vectors appear.
- The name speaks of an embedding and a CM datum; the statement has neither.
