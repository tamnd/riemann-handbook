---
id: laws-links-of-geo-rows-cols-alt
title: The column data of a true geometric family
kind: theorem
decl: GlobalTheory.Fam.lawsLinks_of_geo_rows_cols_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.LawsLinksOfGeoRowsCols
covers: 2656
status: drafted
drafted_by: writer@claude
---
For a geometric family $a$ and a good row choice, this theorem picks the family constants and then one column choice for which the family character has the place laws `LawsX` and four link conditions. Its only user is the restatement [`true_geometry_family_column_data_alt`](/entry/true-geometry-family-column-data-alt/), which [`famAllQ_of_allTrue_alt`](/entry/fam-all-q-of-all-true-alt/) calls in step 4 of its proof. That theorem is part of the multiplicity condition in branch 3 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). About half of the size (1,356 of 2,656) is below [`seeSaw_latticeFramePins_finiteIntegralLaws`](/entry/see-saw-lattice-frame-pins-finite-integral-laws/).

## Statement

Let $D$ = `I.rec7 l Z` be the datum of type `D7` made from base data $B$ and tower data $I, l, Z$. Let $W$ be a real package over $D$ (`RealPackAlt`) with `AllFamilyConditions W` (package hypotheses `pk`, validity `tr`, family conditions, a standard twist `tw`, a level condition and a recursion). Let $u$ be a word. A geometric family $a$ (`GeometricFamily W u`) consists of a geometry $g$, a linear map $j$, a nonarchimedean local field $k$, vector data $v$, type data $o$, local groups $G_1, \dots, G_n$ with a bijection to the places `Pg`, data at the places of `Q`, a bottom datum and a sequence $c_0$. `a.Is` has twelve fields (measures, volumes, shape, ties, a top reading and others); `a.True` has four (pins, a standard form, an embedding and the vector at zero).

A record of family constants $k$ has units $\varepsilon$ of the residue field of $k$, bilinear operators, reals $r$, integers $e$, complex numbers $c_G$ and scalars $\mathrm{sc}(t, j)$.

**Theorem.** Assume `DiscreteSeriesCover`, `HarishChandraModules` and `StrongApproxSU`, and `a.Is`, `a.True`. Let `row` be a row choice with each `(row t).Is` and all rows pairwise `Same`. Suppose that for each $k$ there are a column choice `col`, vector tuples $w_0, w$ and families $F$ with `FamilyColumnCondition` and `ColumnOutputCondition k w₀ w F`. Then for some `col` the family character $f$ = `a.fam row col` satisfies:

- `RowOK` and `LawsX f.t` (nine laws: the commutation datum and tuples are good, local finiteness, real equality, `ValX`, `ValLastX`, `KerX`, `PerX`, `RdX`);
- `ChartAtZeroCondition`: at level 0 there is exactly one index $\alpha_0$, and the ramified columns are exactly the twisted columns `col0_alt`, with the readings of the chart at zero;
- `LinkTailCondition` and `LinkCommutes`, as in [`famAllQ_of_allTrue_alt`](/entry/fam-all-q-of-all-true-alt/);
- `FamilyRatioCondition`: when $2n = m$, $c^{\mathrm{top}}_n(t) \neq 0$, and the ratio of $c^{\mathrm{top}}_n(t)/c^{\mathrm{bot}}(t)$ to its value at $\mu_0$ is a unit ratio. Here `UnitRatio S x y` means: $y \neq 0$ and $(x/y)^N = r$ for some $N > 0$ and some rational $r \neq 0$ whose primes are in $S$.

## Proof

1. `RowOK` holds for every column choice: its fields come from `a.Is` and the two row hypotheses.
2. `famCh_is_and_tuples_is_of_colOK` shows that the commutation datum is good. It needs some column choice, so the proof first applies the column hypothesis to a dummy record of constants.
3. `seeSaw_latticeFramePins_finiteIntegralLaws` gives $\varepsilon$, operators, $r > 0$, $e$ and $c_G \neq 0$. It also gives local finiteness, `ValX` and `ValLastX` for every tuple family that meets twelve conditions.
4. `nonzero_scalars_roots_of_unity_alt` gives scalars $s_j \neq 0$ and roots of unity $\zeta(t, j)$. Put $\mathrm{sc}(t,j) = s_j \zeta(t,j)$. This fixes $k$. The column hypothesis at $k$ gives `col`, $w_0$, $w$, $F$.
5. The twelve conditions of step 3 come from `weilOK_of_rank_one_gram'`, `quadratic_family_level_identity_alt` and the fields of the column output condition.
6. `cls_pin_d_of_true_family` gives the class data `ClsPinD`. Three see-saw lemmas turn it into `KerX`, `PerX` and `RdX`. `realEq_of_colOK'` gives the real equality. This completes `LawsX`.
7. `ChartAtZeroCondition` is the field `zero` of the column output condition. `linkTail_of_topReadAt_alt` gives the tail condition from the top reading of `a.Is` and the fact that `col0_alt` at the base twist $\mu_0$ is the untwisted column. `type_data_unit_shift_relation_alt` gives `LinkCommutes`.
8. `seeSaw_totalConstant_ratio_of_factor_ratios` gives the ratio condition. The ratio of scalars is a unit ratio because $(s_j\zeta(t,j))^N = (s_j\zeta(\mu_0,j))^N$ for a common order $N$ of the roots of unity.

The rest is bookkeeping.

## In the Lean code

The theorem is at [LawsLinksOfGeoRowsCols.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LawsLinksOfGeoRowsCols.lean#L36). The structures are in [GeoAll.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/GeoAll.lean#L28) and [FamilyConstants.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FamilyConstants.lean#L27). `LawsX` is in [ValLastX.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/ValLastX.lean#L212), and `UnitRatio` in [UnitRatio.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/UnitRatio.lean#L22). We have not unfolded the twelve conditions of step 3 or the periods in `ValX`.

Odd points:

- The hypotheses `StrongApproxSU` and `a.True` are introduced (line 37) and never used.
- `ChartAtZeroCondition` in the conclusion is the field `zero` of the hypothesis, and the unit ratios of `cK` and `cP` in step 8 are also fields of the hypothesis. So part of the conclusion is assumed.
- The dummy call in step 2 (line 40) uses constants $1$ and $0$, and only its column choice is kept.
