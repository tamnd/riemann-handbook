---
id: nonempty-hyps-of-all-rows-alt
title: A HypsAlt record from all rows and a selected class
kind: theorem
decl: GlobalTheory.Fc.nonempty_hyps_of_allRows_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.NonemptyHypsOfAllRows
covers: 415
status: drafted
drafted_by: writer@claude
---
This theorem builds a record of type [HypsAlt](/step/hyps-alt-def/) from the rows of `AllRowsAlt` and some global inputs. Its only user is [the proof that HypsAlt is nonempty](/proof/unitary-hypotheses/), in branch 1 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). The rows come from [`allRows_of_open0_alt`](/entry/all-rows-of-open0-alt/). This theorem is bookkeeping: it selects a class of families and moves facts into the fields.

## Statement

Assume `SiegelMassRatioCM`, `LitThin`, `WuDecayOfGap`, `RowsFinDim`, `TypeP`, `RowNGP`, `RowMainEqP`, `MassRatioUnderVolume D` for all $D$ and `GenusMassAt D 2` for all $D$. Let `KP`, `Q`, `Q'`, `Lk`, a predicate `N` on classes of families and a definite side type `DR` be given. Assume that `MinkDiv` implies `BaseCond`, `FirstG`, `ExportF` and `SecondG`, and assume `ExBL` and `AllRowsAlt` for these data. Then `HypsAlt N DR` is nonempty. We have not unfolded the inputs.

## Proof

1. Take the field `c30` of `AllRowsAlt` apart: a constant `c30`, a second constant with a positivity fact, a bound and a row.
2. Make one more row `rTu` from `hTu_cTmin_of_genusMass`, with the two genus mass inputs.
3. Join 27 rows into one row with `RowL.and`: 25 fields of `AllRowsAlt`, the row of `c30` and `rTu`.
4. Apply `UpperTheory.Top.classSel` to this row. It gives a class $\mathcal A$ of families, a selection $\sigma$, an existence fact under `MinkDiv`, `Duty7` and `MtStableF` for each family in $\mathcal A$, the fact `IsSel`, and all the joined conditions for $\mathcal A$ and $\sigma$.
5. `workingFamClass_copies_eq_frozen` gives two inclusions of subclasses into the working classes. `Closed.sub` moves ten closed conditions along these inclusions. `working_classes_frozen` gives the field `hEx`.
6. The other fields take the inputs and the conditions of step 4 directly. The cutoff `cT` is `cTmin`.

## In the Lean code

The theorem is at [NonemptyHypsOfAllRows.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/NonemptyHypsOfAllRows.lean#L19). The record is in [Hyps.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/Hyps.lean#L22), and `classSel` in [ClassSel.lean](lean:Development/AutomorphicArithmetic/CharacterBoxes/ClassSel.lean#L14). The call is at [HypothesesNonemptyOfUnramifiedExponents.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/HypothesesNonemptyOfUnramifiedExponents.lean#L57).

- All inputs are used. Six of them (`LitThin`, `WuDecayOfGap`, `RowsFinDim`, `TypeP`, `RowNGP`, `RowMainEqP`) go into fields with no change.
- The proof drops the fact `IsSel` from `classSel`.
- The fields of `AllRowsAlt` have the type `Lg1`, and the proof reads them as `RowL` by type ascription.
- A near copy `nonempty_hyps_of_allRows` is in [the other NonemptyHypsOfAllRows.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/NonemptyHypsOfAllRows.lean#L14). It uses `AllRows` and `Hyps` in place of `AllRowsAlt` and `HypsAlt`.
