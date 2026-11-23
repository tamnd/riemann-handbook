---
id: mi-star2-of-all-true-alt-alt
title: The period identity from the family conditions
kind: theorem
decl: GlobalTheory.Fam.miStar2_of_allTrue_alt_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.MainTheoremFromPublishedResultsAltAltAltAlt
covers: 10205
status: drafted
drafted_by: writer@claude
---
This theorem proves the period identity `MIstar2` for a real pack $W$ over a datum that comes from a base, from the family conditions on $W$ and the nonvanishing of a period map. It joins four lemmas. Its only user is the renaming [main-theorem-from-published-results-alt-alt-alt-alt](/entry/main-theorem-from-published-results-alt-alt-alt-alt/). Through [the period identity for a true pack](/entry/mi-at-of-true-pack-alt-alt/) it serves [the row theorem](/entry/fam-mi-star-row-alt-alt/). Most of its subtree (9,705 of 10,205 declarations) is below [`true_geometry_family_row_data_alt`](/entry/true-geometry-family-row-data-alt/).

## Statement

Let $B$ be a base and `X`, `I : TC B X`, `l : I.Laws`, `Z : TC.Later` data over it. They give a datum $D$ = `I.rec7 l Z`. Let $W$ be a [real pack](/entry/mi-at-of-true-pack-alt-alt/) over an extra datum for $D$, with realisation $Q$.

`AllFamilyConditions W` is a structure of six fields:

- `pk`, the package hypotheses: among them `BottomHypotheses W` and `LevelHypothesis W`;
- `tr`, a validity condition `ValidRealPackage W`;
- `tq`, the geometric family conditions;
- `tw`, a standard twist condition `TwStdAlt W`;
- `lev`, a level condition: the places of the package are of type `IsTypePlaces`, they are the places `vGs` of the primes of $B$, and the characters $\xi_H$ agree with those of $I$;
- `rc`, a recursion of the realisation $Q$ exists.

`PuNZ D` says that for each $u$ the period map $\mathrm{Pu}_u$ is nonzero at some vector. `MIstar2` is the period identity of the [row theorem](/entry/fam-mi-star-row-alt-alt/).

**Theorem.** Assume the thirteen literature hypotheses from `HarishChandraFinite` to `StrongApproxSU`. Assume `AllFamilyConditions W`, $1 \le r_S$ for $B$, and `PuNZ D`. Then `MIstar2` holds for the coefficient space of $W$.

## Proof

1. **Surjectivity.** `ontoAll_of_theta_doubling` takes the first eleven hypotheses (from Harish-Chandra finiteness to `UnramifiedDoublingGL`) and gives `OntoAll` for every datum, here for $D$. We have not unfolded `OntoAll`.
2. **Family data.** [`true_geometry_family_row_data_alt`](/entry/true-geometry-family-row-data-alt/) takes `CuspRapidDecay`, `DiscreteSeriesCover`, `HarishChandraModules`, `StrongApproxSU`, the family conditions, $1 \le r_S$ and `OntoAll D`. It gives `FamilyAllConditions W`: a central element $z$ and, for each $u$, a family character and bottom data with a pin at $z$, the laws `LawsX` and six link conditions (vanishing, tail, descent, surjectivity, commutation, ratio).
3. **Served primes.** `servedQ_of_bot_alt` gives `FamilyServedCondition W`: for each $w$ and each prime $p$ with `qPrime_alt W (μ w) p`, $p$ is not in the ideal of $w$.
4. **The identity.** `mi_star2_of_pu_nz` takes `DiscreteSeriesClassification`, `CuspRapidDecay`, `HarishChandraModules`, the bottom and level hypotheses from `pk`, the results of steps 2 and 3, and `PuNZ D`. It gives `MIstar2`.

## In the Lean code

The theorem is in [MainTheoremFromPublishedResultsAltAltAltAlt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MainTheoremFromPublishedResultsAltAltAltAlt.lean#L23). It calls:

- `GlobalTheory.T.ontoAll_of_theta_doubling`, in [OntoAllOfPrintsAndHecke.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/OntoAllOfPrintsAndHecke.lean#L28), a renaming of `ontoAll_of_hecke_alt` (line 13 of the file);
- [`true_geometry_family_row_data_alt`](/entry/true-geometry-family-row-data-alt/), a renaming of [`famAllQ_of_allTrue_alt`](/entry/fam-all-q-of-all-true-alt/), applied by `apply ... <;> assumption`;
- `GlobalTheory.MiTop.servedQ_of_bot_alt`, in [ServedQOfBot.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ServedQOfBot.lean#L20);
- `GlobalTheory.T.mi_star2_of_pu_nz`, in [MiStar2OfFamiliesStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MiStar2OfFamiliesStatement.lean#L20), a renaming of `miStar2_of_bot_lev_fam_served_puNZ`, which we have not opened.

All thirteen hypotheses are used. `CuspRapidDecay` and `HarishChandraModules` are used three times.

Odd points:

- `servedQ_of_bot_alt` does not use its two hypotheses. Its proof is `served' W`, in [NotMemQBase.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/NotMemQBase.lean#L47), which holds for every pack. So step 3 needs nothing from the family conditions.
- Two names are near copies with different meanings. `AllFamilyConditions` (the hypothesis, [FamilyConstants.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FamilyConstants.lean#L72)) is the six-field structure above. `FamilyAllConditions` (the result of step 2, [FamAllQ.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FamAllQ.lean#L29)) is the statement on family characters and bottom data.
- `MIstar2` is a variant of `MIstar` in [IsometricPeriodsOfHypotheses.lean](lean:Formalism/LocalToGlobal/IndefiniteReal/IsometricPeriodsOfHypotheses.lean#L105). `MIstar` asks that the scalars $\zeta(u,t)$ be roots of unity. `MIstar2` asks only that they be nonzero, with $\zeta(u,\mu(w))$ a unit at $w$ when it lies in the field $K$.
