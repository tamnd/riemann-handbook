---
id: member-bundles-large-unramified-exponents-alt
title: Membership and bundles at the stronger parameters
kind: theorem
decl: GlobalTheory.Fc.StageOneU.member_bundles_large_unramified_exponents_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.MemberBundlesLargeUnramifiedExponents
covers: 19958
status: drafted
drafted_by: writer@claude
---
This theorem gives the first step of [`hypotheses_nonempty_of_unramified_exponents_alt`](/entry/hypotheses-nonempty-of-unramified-exponents-alt/), the first branch of the [unitary hypotheses node](/proof/unitary-hypotheses/). It turns the record of literature hypotheses into three facts at the stronger parameters: a Siegel mass ratio, the membership statement `MemberE`, and the existence of bundles `ExBL`. It reaches its caller through the second name [`large_unramified_exponent_bundles_exist_alt`](/entry/large-unramified-exponent-bundles-exist-alt/). Most of its work is in [`member_exists_baseLattice_alt`](/entry/member-exists-base-lattice-alt/).

## Statement

A *parameter* $p$ in this part of the code is a record $(R, N, S, \Gamma)$: a position, a norm choice extension $N$ (for each norm choice datum at a base, a type of extra data), an `SExt` and a geometric predicate. For a norm choice extension $N$, let $p(N)$ be the parameter $(\mathrm{RX}, N, \mathrm{none}, \mathrm{geoCl}(\mathrm{any}))$ (`parametersOfExtension N SExt.none (geoCl anyGeometry)`), and let $p(N).s$ be its slots. Let $N_0 = $ `extensionWithOrigin hL cDep`; it pairs the data of `extensionWithList` with an origin datum. For a property $A$ of bases, let $N_0 \times A$ be `extensionWithAtProperty hL N_0 A`: the data of $N_0$ together with a proof that $A$ holds at the base.

**Theorem.** Assume `UnitaryGroupThirdPlaceHypotheses` (the sixty literature hypotheses of the [chapter](/proof/unitary-hypotheses/)) and `RowRat`. Let `hL : RecTExists`, $c_{\mathrm{Dep}} \in \mathbb R$, and let $A$ be a property of bases with `EvLgG A` (eventually in the context, $A$ holds at all large bases). Then:

1. `SiegelMassRatioCM`: for each number field $K$ with a star ring structure that satisfies `IsCMUnram`, and each $M \ge 3$, the ratio of the masses of the standard hermitian lattices of ranks $M$ and $M - 1$ over $K$ equals `massRatioRightSide K M`;
2. `MemberE` $p(N_0 \times A).s$: four conditions on the slot of built points (`BaseCond`, `FirstG`, `ExportF`, `SecondG`), which say that bases of the right kind exist eventually, that untwisted large bases carry a built core, that built cores export, and that they pass to enlarged bases with good cores;
3. `ExBL KPx (IsBuiltE s) (IsGoodE s) (BundleLinkage p)` for $p = p(N_0 \times A)$: there is a slot $R$ such that, eventually, built cores at large bases lie in $R$, and every good point in $R$ carries, for each $c \in \mathbb R$, a bundle linked by `BundleLinkage p`.

We have not unfolded `Built`, `EntC`, `ExportAt`, `BundleLinkage` or `massRatioRightSide`.

## Proof

1. `compatibleSystem_member_hypotheses` makes the record `HypAAlt` (21 fields) from eleven fields of the input. It is a second name of `compatibleSystem_hypotheses_of_localInputs`, which fills three fields with proved theorems: `weilRepresentationUnitaryPair`, `rowsFinDim_link` and `massRatio_all_unramified_cmFields`.
2. Ten fields of the input form the record `MemberHypotheses`. With ten more fields and `RowRat`, `compatibleSystem_member_rationalWeights` gives the record `MultiplicityCoverHypotheses`.
3. `compatibleSystem_weightOne_saturated` gives `ExistsUnlocalizedSaturatedState` from these two records.
4. `member_multiplicatively_closed_alt` gives `MultiplicityCondition` $p(N_0)$ from ten fields of the input.
5. [`hyps_e_third_layer_ser_n_of_geometric_galois`](/entry/hyps-e-third-layer-ser-n-of-geometric-galois/) gives the record `EllipticHypothesis` and a `LocalLanglandsHypothesis` from the fields `litN` and `toHypothesesX`.
6. Part 1 is the field `a18` of `HypAAlt`. So it comes from the theorem `massRatio_all_unramified_cmFields`, with no hypothesis.
7. Part 2: [`member_exists_baseLattice_alt`](/entry/member-exists-base-lattice-alt/) gives `MemberE` $p(N_0).s$. Then `memberE_extensionWithAtProperty_of_evLgG` uses `EvLgG A` to pass from $N_0$ to $N_0 \times A$.
8. Part 3: `compatibleSystem_weilBlock_ne_alt` gives `ExBL` directly for $N_0 \times A$, from the three records, a projection from $N_0$ to `extensionWithLaw`, and `slot_mv_extension_with_origin_geo_cl` (the condition `PositionMv` at $p(N_0)$).

## In the Lean code

The theorem is in [MemberBundlesLargeUnramifiedExponents.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MemberBundlesLargeUnramifiedExponents.lean#L34). The lemmas it calls:

- `compatibleSystem_member_hypotheses`, `compatibleSystem_member_rationalWeights`, `compatibleSystem_weightOne_saturated` (in LocalTypeDictionary);
- `member_multiplicatively_closed_alt`, `memberE_extensionWithAtProperty_of_evLgG`, `compatibleSystem_weilBlock_ne_alt`, `slot_mv_extension_with_origin_geo_cl`;
- [`hyps_e_third_layer_ser_n_of_geometric_galois`](/entry/hyps-e-third-layer-ser-n-of-geometric-galois/) and [`member_exists_baseLattice_alt`](/entry/member-exists-base-lattice-alt/).

Odd points:

- `member_exists_baseLattice_alt` proves `MemberE` and `ExBL` at $p(N_0)$, but the proof keeps only the first half (`.1`). The `ExBL` of part 3 comes from `compatibleSystem_weilBlock_ne_alt` instead. So the `ExBL` half of that theorem is not used here, its only caller.
- Part 1 needs no hypothesis. It is the theorem `massRatio_all_unramified_cmFields`, passed through `HypAAlt`.
- `EvLgG A` is used only for part 2.
- The pattern `obtain ⟨hE, -, -, hL', hN⟩` takes a new proof `hL'` of `RecTExists` from an existential, and `hN` is stated for `hL'`. The proof then uses `hN` with the given `hL`. This type checks because `RecTExists` is a `Prop`, so any two proofs are equal.
- One of the fields passed to `compatibleSystem_member_rationalWeights` is `siegelEisensteinSimplePole`, whose type `UnusedSlot72` is `True`.
- "Large unramified exponents" names no object in the statement.
