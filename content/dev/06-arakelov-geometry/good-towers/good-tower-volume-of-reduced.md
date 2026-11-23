---
id: good-tower-volume-of-reduced
title: The good tower and volume theorem, assembled from seventeen inputs
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Top.goodTower_volume_of_reduced
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.FinalTheoremOfInputsRight
covers: 21073
status: drafted
drafted_by: writer@claude-opus-5-5
---
This theorem assembles the pair `GoodTowerExistsX` and `VolumeTheoremX` from seventeen inputs. It builds the six inputs of [`good_tower_volume_theorem`](/entry/good-tower-volume-theorem/) and applies it. It is restated as [`final_theorem_of_inputs_right`](/entry/final-theorem-of-inputs-right/), which [`good_tower_volume_theorem_bis`](/entry/good-tower-volume-theorem-bis/) calls. That entry states the two conclusions. Of the 21,073 declarations below this theorem, `good_tower_volume_theorem` holds 17,797 and [`family_pos_of_hodge_tate_inputs`](/entry/family-pos-of-hodge-tate-inputs/) holds 1,619.

## Statement

**Theorem.** Assume the following seventeen statements. Then `GoodTowerExistsX` and `VolumeTheoremX` hold.

1. A model clause: `PartI`, `N1ab`, `N1c`, and for each CM field $E$, host $H$ and datum $D$ the toroidal level and Hecke compatibilities.
2. `KeyFormula`: there is a rule `ka` with `IsKeyRule ka`.
3. `SemiAbelianHomExtension`, `NumericalSegre.Statement`, `ResKStatement`, `FarguesHodgeTate` and `GagaSections`.
4. The Siegel lemma `LineOfLargeDegree.Statement` (see [its proof](/entry/line-of-large-degree-of-use/)).
5. `PB.Inputs`, `Prov.HS`, `Prov.An` and `Prov.ZhangDimensionPushDownGrassmannianHeightBounds`.
6. `PtsIntegrableStatement` and `I2.AvoidStatement`.
7. `QuotientByFiniteFlatStatement`, `ZarhinStatement` and `ThetaUnifAV`.

We have not unfolded these statements, except the Siegel lemma.

## Proof

The proof builds the six inputs of `good_tower_volume_theorem` and applies it.

1. **The bundle `Top.Given`.** [`final_theorem_of_inputs_left`](/entry/final-theorem-of-inputs-left/) takes inputs 1 to 5 (twelve statements) and gives `Top.Given`. It adds three statements that the code proves: `SAStatement`, the slope bound `SlopeBoundSt` (from the Siegel lemma) and `AntisymPerturbation.Statement`.
2. **Weil pairings.** `Out.WeilSt` is the theorem `Link.weilSt`, with no hypothesis.
3. **The family.** `family_pos_of_hodge_tate_inputs` gives `Num.FamilyExistsPos` from `FarguesHodgeTate`, `QuotientByFiniteFlatStatement`, `ZarhinStatement` and two proved statements, `HodgeTateDatumStatement` (the theorem `GR.Top.main`) and `OrdinaryCurveStatement` (`ordinary_curve_statement_holds`). `FamilyExistsPos` gives Hodge-Tate lattice data over each place above $p$; see [`model_on_hodge_of_family_pos`](/entry/model-on-hodge-of-family-pos/) for its use.
4. **The comparison pair.** `comparison_of_inputs_avoidance` gives `Cmp.CmpSt` from `PB.Inputs`, `AvoidStatement` and `ResKStatement`. The theorem `CmpHodgeTied_holds` gives `HodgeComparisonCompatibility`. Then `cmpPair_of_inputs` gives `Cmp.CmpPair` from `PB.Inputs`, `CmpSt`, this compatibility and `ThetaUnifAV`.
5. **The volume theorem.** `good_tower_volume_theorem` takes `Top.Given`, `PtsIntegrableStatement`, `AvoidStatement`, `WeilSt`, `FamilyExistsPos` and `CmpPair`, and gives the conclusion. It is a restatement of [`goodTower_and_volume`](/entry/good-tower-and-volume/), which does the work: it builds the root tower with `exists_good_root_tower`, and gets `VolumeTheoremX` from [`volume_theorem_of_inputs`](/entry/volume-theorem-of-inputs/).

## In the Lean code

The theorem is in [FinalTheoremOfInputsRight.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/FinalTheoremOfInputsRight.lean#L28). The proof is nine lines. It calls:

- `GlobalTheory.T.final_theorem_of_inputs_left`, a restatement of `given_of_inputs`.
- `Link.weilSt`, `GR.Top.main`, `ordinary_curve_statement_holds` and `CmpHodgeTied_holds`, all with no hypotheses.
- `family_pos_of_hodge_tate_inputs`, `comparison_of_inputs_avoidance` and `cmpPair_of_inputs`.
- `GlobalTheory.T.good_tower_volume_theorem`, a restatement of `goodTower_and_volume`.

All seventeen hypotheses are used. `PB.Inputs` is used three times; `FarguesHodgeTate`, `ResKStatement` and `AvoidStatement` twice. At the call site, six of the seventeen are theorems with no hypotheses: the model clause (`modelClause_holds`), `KeyFormula`, `NumericalSegre.Statement`, `Prov.An`, `AvoidStatement` (`topAvoid`) and `ThetaUnifAV` (`thetaUnifAV_closed`). The others come from the ten hypotheses of the caller.

The word "reduced" in the name does not refer to anything in the statement that we could find. The caller unpacks `Top.Given` into its parts and passes them here, and this proof packs them into `Top.Given` again.
