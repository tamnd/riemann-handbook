---
id: s-fino-and-second-no-of-rat-cusp-finl
title: Spectral finiteness and second nonvanishing as one pair
kind: theorem
decl: GlobalTheory.HeightCounting.Up.sFino_and_secondNo_of_rat_cusp_finl
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.FiniteLevelAndSecond
covers: 569
status: drafted
drafted_by: writer@claude
---
This theorem puts two results side by side: a short repackaging lemma, and [`secondNo_of_sMt_sRat_sCusp_sFinl`](/entry/second-no-of-s-mt-s-rat-s-cusp-s-finl/), which has the real content. It reaches [membership and bundles at the origin parameters](/entry/exists-base-lattice-of-prime-alt/) through the relay [`sFino_and_secondNo_of_sFinl'`](/entry/s-fino-and-second-no-of-s-finl-prime/).

## Statement

Stages, the `StrictHenselianAcyclicLevel` data and the level three points `Lv3` are as in [the stage statements](/entry/all-stages-of-specializations-alt/). For $c \in \mathbb R$, let $N_L(c) = $ `extensionWithList hL c` and $N_0(c) = $ `extensionWithOrigin hL c`. The extension $N_0(c)$ is $N_L(c)$ with one more factor, `OriginData`: there are a datum $P$, a stage $x$ over $P$ and a `StrictHenselianAcyclicLevel` datum $l$ over $x$ with `ListSt c x` and `SatU P`, with the set $W_t$ of $P$, and with a norm choice kept by $l$.

- `FinitenessListStatement hL c`: at every stage $x$ with `ListSt c x`, each $l$ and each `S`, `Γ` give a point `Lv3` at the parameters of $N_L(c)$, with the set $W_t$ of $P$ and a norm choice kept by $l$.
- `SpectralFiniteness hL c`: the same, for stages with `ListSt c x` and `SatU P`, at the parameters of $N_0(c)$.
- `SecondNonvanishing hL c`: as in [`secondNo_of_sMt_sRat_sCusp_sFinl`](/entry/second-no-of-s-mt-s-rat-s-cusp-s-finl/).

**Theorem.** Under the hypotheses of [the relay](/entry/s-fino-and-second-no-of-s-finl-prime/), `SpectralFiniteness hL c` and `SecondNonvanishing hL c` hold.

## Proof

The first half is `sFino_of_alt`. Take the point $v$ that `FinitenessListStatement` gives. Keep each field of $v$ and add to its extension the factor `OriginData`, with the stage $x$, the datum $l$ and the facts at hand as witnesses. This is a point at the parameters of $N_0(c)$. The second half is `secondNo_of_sMt_sRat_sCusp_sFinl` with the same hypotheses.

## In the Lean code

The theorem is at [FiniteLevelAndSecond.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FiniteLevelAndSecond.lean#L116). The proof is a term, a pair of the two lemmas. `sFino_of_alt` is in [ExistsSeed.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsSeed.lean#L21); `extensionWithOrigin` and `OriginData` are in [ExtensionWithOrigin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExtensionWithOrigin.lean#L24).

`SpectralFiniteness` is close to a restatement of `FinitenessListStatement`: the extra factor `OriginData` only records that the point came from a stage of the right kind. The proof of `SecondNonvanishing` also calls `sFino_of_alt` itself.
