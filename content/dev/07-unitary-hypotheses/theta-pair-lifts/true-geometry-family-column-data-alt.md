---
id: true-geometry-family-column-data-alt
title: The column data of a true geometric family, in statement form
kind: theorem
decl: GlobalTheory.T.true_geometry_family_column_data_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.LawsLinksOfGeoRowsColsStatement
covers: 2657
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`lawsLinks_of_geo_rows_cols_alt`](/entry/laws-links-of-geo-rows-cols-alt/). Its only user is [`famAllQ_of_allTrue_alt`](/entry/fam-all-q-of-all-true-alt/), which takes from it one column choice with the place laws and the tail, commutation and ratio conditions, in step 4 of its proof. That theorem is part of the multiplicity condition in branch 3 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). The real content is in `lawsLinks_of_geo_rows_cols_alt`.

## Statement

The statement is word for word the statement of [`lawsLinks_of_geo_rows_cols_alt`](/entry/laws-links-of-geo-rows-cols-alt/). In short: assume `DiscreteSeriesCover`, `HarishChandraModules` and `StrongApproxSU`. Let $W$ be a real package with `AllFamilyConditions W`, $u$ a word and $a$ a geometric family with `a.Is` and `a.True`. Let `row` be a row choice whose rows are good and pairwise of the same shape. Suppose that for each record $k$ of family constants there is a column choice with the column condition and the column output condition for $k$. Then there is a column choice `col` such that the family character `a.fam row col` satisfies `RowOK`, `LawsX`, `ChartAtZeroCondition`, `LinkTailCondition`, `LinkCommutes` and `FamilyRatioCondition`.

## Proof

The proof applies `lawsLinks_of_geo_rows_cols_alt`. Nothing else happens.

## In the Lean code

The theorem is at [LawsLinksOfGeoRowsColsStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LawsLinksOfGeoRowsColsStatement.lean#L22). The proof is the tactic `first | exact @GlobalTheory.Fam.lawsLinks_of_geo_rows_cols_alt | ...`, so the theorem only passes its hypotheses along. The hypothesis `StrongApproxSU` and the hypothesis `a.True` are not used in the proof of `lawsLinks_of_geo_rows_cols_alt` (see that entry).
