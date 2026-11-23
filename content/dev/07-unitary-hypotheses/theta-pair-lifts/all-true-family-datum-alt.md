---
id: all-true-family-datum-alt
title: A true framed geometric family for each word, in statement form
kind: theorem
decl: GlobalTheory.T.all_true_family_datum_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.CoreDataOfPointStatement
covers: 729
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`exists_geoAll_alt`](/entry/exists-geo-all-alt/). Its only user is [`famAllQ_of_allTrue_alt`](/entry/fam-all-q-of-all-true-alt/), which calls it in step 2 of its proof to get, for each word $u$, a geometric family with a framed Bessel datum. That theorem is part of the multiplicity condition in branch 3 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). The real content is in `exists_geoAll_alt` and in [`core_data_of_point`](/entry/core-data-of-point/).

## Statement

The statement is word for word the statement of [`exists_geoAll_alt`](/entry/exists-geo-all-alt/). In short: assume the published inputs `DiscreteSeriesCover`, `HarishChandraModules` and `StrongApproxSU`. Let $W$ be a real package over $D$ = `I.rec7 l Z` with `AllFamilyConditions W`. Then for each word $u$ there is a geometric family $a$ (`GeometricFamily W u`) such that `a.Is` and `a.True` hold, the top matrix $i_A$ of the orthogonal decomposition at the top level $m$ is the identity, and the Bessel datum of the bottom datum of $a$ is framed.

## Proof

The proof applies `exists_geoAll_alt`. Nothing else happens.

## In the Lean code

The theorem is at [CoreDataOfPointStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CoreDataOfPointStatement.lean#L19). The proof is the tactic `first | exact @GlobalTheory.GeoExists.exists_geoAll_alt | ...`, so the theorem only passes its hypotheses along. The file name speaks of `CoreDataOfPoint`, the theorem name of a "family datum", and the conclusion is the existence of a geometric family; the three names refer to one statement.
