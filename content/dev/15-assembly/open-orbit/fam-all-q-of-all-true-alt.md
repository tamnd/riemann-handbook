---
id: fam-all-q-of-all-true-alt
title: The family conditions from the package conditions
kind: theorem
decl: GlobalTheory.MiTop.famAllQ_of_allTrue_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.FamAllQOfAllTrue
covers: 9704
status: drafted
drafted_by: writer@claude
---
For a real package $W$, this theorem builds one family character and one bottom datum for each word $u$, with eight properties. Through the relay [`true_geometry_family_row_data_alt`](/entry/true-geometry-family-row-data-alt/) its conclusion goes to [`miStar2_of_allTrue_alt_alt`](/entry/mi-star2-of-all-true-alt-alt/). This subtree is part of the multiplicity condition in branch 3 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/).

## Statement

Let $D$ = `I.rec7 l Z` be the datum of type `D7` given by base data $B$ and tower data $I$, $l$, $Z$. Let $W$ be a real package over $D$ (`RealPackAlt`). Assume `CuspRapidDecay`, `DiscreteSeriesCover`, `HarishChandraModules`, `StrongApproxSU`, `OntoAll D`, $1 \le r_S$ for the integer $r_S$ = `B.R.rS`, and `AllFamilyConditions W` (package hypotheses `pk`, conditions on geometric families, a twist, a level condition and a recursion).

**Theorem.** Then `FamilyAllConditions W` holds. That is, there is an element $z$ of the subgroup `GfC` of the adelic group `GA D (D.sp.Y 0)`, central in that group, such that for each word $u$ there are a family character $f$ and a bottom datum $d$ with:

- `d.Pin z`: an adelic identity at level 0 that ties $d$ to $z$, with side conditions;
- `LawsX f.t`: the place laws for the tuples of $f$;
- `LinkVanishes f d`: at level 0 each column is ramified, and its periods equal the periods of $d$;
- `LinkTailCondition f`: when $2n = m$, the tail at level $2n$ is the column period `perCol` of a vector of the row side;
- `LinkDescends f`: descent to level 0 of a lifted vector is the row form of that vector;
- `LinkSurjective f`: at the base point $\mu_0$, descent to level 0 is onto `BaseRowSpace W`;
- `LinkCommutes f`: for some linear $S$ on `Mu u` with $\|S\varphi\| = r\|\varphi\|$, $r > 0$, and some $s \neq 0$, the tail of the raised column of $\varphi$ is $s$ times the tail of the column of $S\varphi$;
- `FamilyRatioCondition f`: when $2n = m$, $c^{\mathrm{top}}_n(t) \neq 0$, and some power of the ratio of $c^{\mathrm{top}}_n(t)/c^{\mathrm{bot}}(t)$ to its value at $\mu_0$ is a nonzero rational number whose primes lie under `Q t`.

We have not unfolded `GfC`, the fields of `LawsX` or the period maps.

## Proof

1. `exists_botDat_of_placedP_framed` (from `pk` and $1 \le r_S$) gives $z$, and for each placed and framed Bessel datum $\mathcal B$ (`SBes`) a bottom datum $d$ on $\mathcal B$ with `d.Pin z`.
2. Fix $u$. `all_true_family_datum_alt` (from `DiscreteSeriesCover`, `HarishChandraModules` and `StrongApproxSU`) gives a geometric family $a$ with `a.Is`, `a.True`, top matrix $i_A = 1$ and a framed Bessel datum.
3. `exists_pairwise_same_choices_at_geo` (from `CuspRapidDecay`) gives a row choice, each row good and all rows of the same shape.
4. For each choice $k$ of family constants, [`true_geometry_family_invariance_alt`](/entry/true-geometry-family-invariance-alt/) gives a column side. From these, [`true_geometry_family_column_data_alt`](/entry/true-geometry-family-column-data-alt/) gives one column choice with `RowOK`, `LawsX`, the chart at zero condition, and the tail, commutation and ratio conditions.
5. `famCh_is_and_tuples_is_of_colOK` and `placed_p_of_true_geometry` show that the Bessel datum of $a$ is placed. Step 1 then gives $d$.
6. `linkDown_of_famCh` gives `LinkDescends`. `linkOnto_of_ontoAll'` gives `LinkSurjective`; this is the only use of `OntoAll D`. `linkZero_of_chartZero'` gives `LinkVanishes`, with the level identity from the field `bot` of `a.Is`.

## In the Lean code

The theorem is in [FamAllQOfAllTrue.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FamAllQOfAllTrue.lean#L38). The conclusion is in [FamAllQ.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FamAllQ.lean#L29), the link conditions in [NotMemQBase.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/NotMemQBase.lean#L26).

`CuspRapidDecay` is used only in step 3. The lemma `famCh_is_and_tuples_is_of_colOK` takes `RowOK` as its main hypothesis, not `ColOK`; `ColOK` is needed only for its second part. A parallel copy of this theorem for `RealPack`, `famAllQ_of_allTrue`, is in [TrueGeometryFamilyRowData.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/TrueGeometryFamilyRowData.lean#L29).
