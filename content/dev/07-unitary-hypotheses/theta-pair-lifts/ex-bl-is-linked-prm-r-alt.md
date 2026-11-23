---
id: ex-bl-is-linked-prm-r-alt
title: Bundles at good points, for parameters with no S-extension
kind: theorem
decl: GlobalTheory.Mem.Top.Bl.exBL_isLinked_prmR_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ExBLIsLinkedPrmR
covers: 780
status: drafted
drafted_by: writer@claude
---
This theorem proves the bundle statement `ExBL` for parameters of the form $p(N, \Gamma) = $ `parametersOfExtension N SExt.none Γ`. Its second name [`geometric_parameter_uniform_alt`](/entry/geometric-parameter-uniform-alt/) has the same statement and calls it. The result goes up to [membership and bundles at the stronger parameters](/entry/member-bundles-large-unramified-exponents-alt/), in branch 1 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/).

## Statement

Let $N$ be a norm choice extension for `hL : RecTExists`, let $\Gamma$ be a geometric predicate, and let $p = p(N, \Gamma)$, with slots $s = p.s$. Assume eleven named inputs: `GreenCuspidal`, `DiscreteSeriesCover`, `HarishChandraModules`, `CasselmanWallach`, `WeilRepresentationUnitaryPair`, `DiscreteSeriesExists`, `HarishChandraFinite`, `CuspRapidDecay`, `GlobalArtinReciprocity`, `WeberRayFieldSt` and `RayField`. Assume also:

1. each datum of $N$ gives an element of `extensionWithLaw` (the law part);
2. `PositionMv s`: a point with a witness keeps rows with the slot data when its lattices and heights are replaced;
3. eventually (`EvP`), at each weighted point $q$ of $s$, `MultEq` holds: two models linked by a finite isomorphism $\Phi$ give the same cusp multiplicity to each irreducible, admissible, good representation.

Then `ExBL KPx (IsBuiltE s) (IsGoodE s) (BundleLinkage p)` holds: there is a slot $R$ such that, eventually, each built core at a large base with `KPx` lies in $R$ (`LargeBaseCondition`), and each good point $\beta$ in $R$ has, for each $c \in \mathbb R$, a bundle `BundleCondition` with a `BundleWitness` (`ExB`). We have not unfolded `BundleCondition` and `ZetaCompatible`.

## Proof

1. `zeta_uniform_of_extension'` uses five of the inputs and hypothesis 1, and gives `ZeU s`: `ZetaCompatible` holds at the datum of each weighted point.
2. `witnesses_pass_along_set_division` turns `PositionMv s` into `WitMv s`. Then `witExE_of_witMv` gives `WitExE s`: each good point carries a weighted point whose kernel satisfies `EntC`.
3. `local_langlands_prm_reduction_alt` uses ten inputs, hypothesis 1 and hypothesis 3. It gives, eventually, a bundle with a witness for each compatible record at each weighted point.
4. `eta_size_recursion_alt` takes `GlobalArtinReciprocity`, `WeberRayFieldSt`, `RayField`, and the results of steps 1 to 3, and gives `ExBL`. `EvP.of_all` makes step 1 an `EvP` statement.

## In the Lean code

The theorem is at [ExBLIsLinkedPrmR.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExBLIsLinkedPrmR.lean#L21). `ExBL` is at [EventuallyAllScaleContextsAndOfBoth.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/EventuallyAllScaleContextsAndOfBoth.lean#L71) and `ExB` at [ValidForConstructedPointClassesEventuallyWorking.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/ValidForConstructedPointClassesEventuallyWorking.lean#L259). The lemmas it calls:

- `zeta_uniform_of_extension'` ([ZeUPrmRNEbStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ZeUPrmRNEbStatement.lean#L16)), a second name of `ze_u_prm_of_extension_with_law`;
- `witnesses_pass_along_set_division` and `witExE_of_witMv`;
- `local_langlands_prm_reduction_alt` ([BwitExistsStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BwitExistsStatement.lean#L19)), a second name of `bwit_exists_alt`;
- `eta_size_recursion_alt` ([ExistsLinkedOfEqStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsLinkedOfEqStatement.lean#L17)), a second name of `exBL_isLinked_alt`.

We have not opened their proofs. All eleven inputs are used; `WeberRayFieldSt` goes only to step 4, `DiscreteSeriesExists` only to step 3. The second names do not describe their statements: `local_langlands_prm_reduction_alt` concludes that bundles with witnesses exist, and `eta_size_recursion_alt` concludes `ExBL`. Neither mentions local Langlands or a recursion on sizes.
