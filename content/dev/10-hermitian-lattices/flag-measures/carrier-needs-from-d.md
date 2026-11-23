---
id: carrier-needs-from-d
title: Three inputs of the carrier bound
kind: theorem
decl: GlobalTheory.carrierNeedsFromD
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.CarrierNeedsFromD
covers: 2946
status: drafted
drafted_by: writer@claude
---
This theorem puts three proved results into one conjunction. Its only user is [`carrierP`](/entry/carrier-p/), which takes it apart at once. It has no content of its own. The content is in [`actual_compact_theorem`](/entry/actual-compact-theorem/), [`model_place_built_holds`](/entry/model-place-built-holds/) and [`pb_builtBounds2Cpt`](/entry/pb-built-bounds2-cpt/).

## Statement

The conjunction of:

1. `ThmPActualCpt`: for real place data, level data and $1 \le l_0 \le k$, there are submodules $K$ of the space `RadSp` with the properties `ThmPOn`, `SliceIn` and `CompositeFormulaLevelZero`. Also, each compactly supported $F$ in all the classes `InCC`, with $G_f \ge \varepsilon$ on its support, has a $\Phi$ in $K(0)$ that equals the restriction of $J_F(D, F)$ on the domain `DomR`.
2. `ModelPlaceBuilt2`: there is $C_c$ such that, for each CM field $E$ and each built place with constant $C_c$ that satisfies the place and word conditions, each place $v$ has a model place (`JC.IsModelPlace`).
3. `BuiltBounds2Cpt`: if `ThmPActualCpt` holds, then for each $C_b$ there are constants $C_c$ and $C_4 \ge 1$ such that each leading form setting satisfies a list of bounds that ends with `SumFormConcrete`.

We have not unfolded the definitions inside these three statements.

## Proof

Each part is one proved theorem: `actual_compact_theorem`, `model_place_built_holds` and `pb_builtBounds2Cpt`.

## In the Lean code

The theorem is at [CarrierNeedsFromD.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/CarrierNeedsFromD.lean#L8). The three statements are in [HerGenC.lean](lean:Formalism/HermitianCurvature/HerGenC.lean#L63), [StatementJCT.lean](lean:Formalism/HermitianCurvature/StatementJCT.lean#L317) and [ArchimedeanUniformConstantsCompactSupport.lean](lean:Formalism/HermitianCurvature/ArchimedeanUniformConstantsCompactSupport.lean#L13).

The statement is `CSTarget4` of [CarrierXAll.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/CarrierXAll.lean#L848), written out, but the theorem does not use that name. Part 3 is an implication from part 1, so with part 1 it is the same as its conclusion. We do not know what "from D" in the name refers to.
