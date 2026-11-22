---
id: true-geometry-family-invariance-alt
title: The column side of a geometric family, the statement form
kind: theorem
decl: GlobalTheory.T.true_geometry_family_invariance_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ColSideStatement
covers: 3233
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It states the result of [the column side of a geometric family](/entry/col-side-alt/) and proves it by calling that theorem. The real content is in that entry. Its only user is [the family conditions from the package conditions](/entry/fam-all-q-of-all-true-alt/), which applies it once for each choice of family constants and gives the result to [`true_geometry_family_column_data_alt`](/entry/true-geometry-family-column-data-alt/).

## Statement

Assume `DiscreteSeriesCover` and `HarishChandraModules`. Let $W$ be a real package with `AllFamilyConditions W`, $u$ a word, and $a$ a geometric family for $W$ and $u$ with `a.Is`, `a.True` and top matrix $i_A$ equal to the identity. Let $k$ be family constants for $a$, and let a row choice be given with each row good and all rows of the same shape. Then there are a column choice, two tuples $w_0$, $w$ and local families $F$ with `FamilyColumnCondition` and `ColumnOutputCondition k w₀ w F`.

[The column side of a geometric family](/entry/col-side-alt/) says what these predicates mean.

## Proof

The proof is `first | exact @GlobalTheory.Fam.colSide_alt | ...`. It applies that theorem. The two statements are the same, word for word.

## In the Lean code

The theorem is in [ColSideStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ColSideStatement.lean#L18). It is used once, in [FamAllQOfAllTrue.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FamAllQOfAllTrue.lean#L45).

The name says "invariance", but the statement is an existence statement for column data. No invariance is stated. A copy without `_alt`, `true_geometry_family_invariance`, wraps `GlobalTheory.Fam.colSide` in `AbelianVarietyTheory.Proofs.DecoratedLatticeProofs`.
