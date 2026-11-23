---
id: second-no-of-s-mt-s-rat-s-cusp-s-finl
title: Built points at the origin parameters give good level three points after an enlargement
kind: theorem
decl: GlobalTheory.HeightCounting.Up.secondNo_of_sMt_sRat_sCusp_sFinl
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.FiniteLevelAndSecond
covers: 567
status: drafted
drafted_by: writer@claude
---
This theorem proves `SecondNonvanishing`: each built point at the origin parameters can be carried to an enlarged base, where a column datum with `Start` has a level three point at the geometric parameters. It reaches [membership and bundles at the origin parameters](/entry/exists-base-lattice-of-prime-alt/) through [the pair](/entry/s-fino-and-second-no-of-rat-cusp-finl/) and [its relay](/entry/s-fino-and-second-no-of-s-finl-prime/). There it is the pass hypothesis of [the pair theorem](/entry/exists-base-lattice-of-pair-alt/).

## Statement

The extensions $N_0(c)$ and `FinitenessListStatement` are as in [the pair](/entry/s-fino-and-second-no-of-rat-cusp-finl/). Let $N_g(c) = $ `GeometricNormExtension hL c`, which is $N_0(c)$ with the extra factor `GoodO`. For `S : SExt` and `Γ : GeoP`, let $p_0$ and $p_g$ be the parameters of $N_0(c)$ and $N_g(c)$.

`SecondNonvanishing hL c` says: for all `S`, `Γ`, `Pass KPx (IsBuiltE p₀.s) r` holds, where `r K B f T` says that some column datum $w$ over $B$ has `Start` and a point `Lv3` at $p_g$ (this is `Has3`). `Pass` says: eventually (in the sense of `EvLgG`), for each base $B$ with `KPx` and untwisted $T$, each built point of $p_0$ with `ExportAt`, each finite set of primes to avoid and each finite set of algebraic numbers, there is an enlargement $B'$ of $B$ with the same frame and the same primes, with a twist datum that avoids the given primes, whose coefficient field contains the given numbers, and at which `r` holds.

**Theorem.** Assume `DiscreteSeriesCover`, `CasselmanWallach`, `HarishChandraModules`, `PublishedInputsThirdLayerAlt`, `SerN`, `DatExt`, `WeightCaseCondition`, `DiscreteSeriesExists`, `PhtCmp`, $h_L$ in `RecTExists`, `SMt`, the rationality and cusp statements, and `FinitenessListStatement hL c`. Then `SecondNonvanishing hL c`.

## Proof

1. Collect ten statements. `exists_ext_twisted_places` (from `GreenCuspidal` and `DatExt`) extends a datum on $B$ to a datum on an enlargement. Nine more hold at each $w$ with `Start`: starting choices (`constructionStartingChoices_of_fine_adelicData`), `BareK`, `FirstStageExists`, `SMt`, rationality, cusp, `MoveToBase` ([`moveToBase_of_inputs_serN`](/entry/move-to-base-of-inputs-ser-n/)), `ThirdStageExists` ([`stageCExists_of_casselmanWallach`](/entry/stage-cexists-of-casselman-wallach/)) and `SpectralFiniteness` (`sFino_of_alt`).
2. `pass_of` reduces `Pass` to one task: from a built point, find $B'$ and show that the ten statements at $B'$ give `r`.
3. Fix a built point. `exists_of_position` gives $w$ with `Start`. Its factor `OriginData` gives, by `exists_pre_point_with_henselian_level`, a stage $x$ over $P$ with a `StrictHenselianAcyclicLevel` datum, `ListSt c x` and `SatU P`, and a seed for each set of places.
4. `extend_pinned` gives the primes to avoid and a column datum $w'$ over each enlargement. Choose a seed $\sigma$ that avoids them. `exists_twisted_cohomology_class_lift_alt` gives $B'$ and a twist datum built from $\sigma$. Step 1 gives `Start` for $w'$.
5. At $w'$, the starting choices give a datum $P'$ that extends $P$. `BareK` and `FirstStageExists` give a stage over $P'$ with a same Galois level datum; `SMt`, rationality and cusp make it an intermediate level datum. `MoveToBase` carries the third level of $x$ to a stage $y$ over $P'$, with `Carried` and `ListSt`.
6. `has3_of_carried_levelB2` ends the proof. `ThirdStageExists` gives a character datum at $y$ whose twist indices are those of $\sigma$. `SpectralFiniteness` gives a point `Lv3` at $p_0$. `goodO_of_alt_alt` proves `GoodO` for it, through `goodTwist_of_seed_character_powers` and `rigid_raw_packet_eq_pow_alt`. So it is a point at $p_g$.

## In the Lean code

The theorem is at [FiniteLevelAndSecond.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FiniteLevelAndSecond.lean#L72), with `has3_of_carried_levelB2` (line 52) and `goodO_of_alt_alt` (line 30). `pass_of` and `exists_of_position` are in the other [FiniteLevelAndSecond.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/FiniteLevelAndSecond.lean#L34). The definitions are in [ExtensionWithOrigin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExtensionWithOrigin.lean#L29).

- Each hypothesis is used. `WeilRepresentationUnitaryPair` is not a hypothesis: the proof uses the theorem `GlobalTheory.weilRepresentationUnitaryPair`.
- We have not unfolded `EvLgG`, `Built`, `ExportAt`, `GoodO` or `Lv3`.
- The word "nonvanishing" matches no nonvanishing statement: the conclusion is the existence of points `Lv3`.
