---
id: onto-x-of-hypotheses-alt-alt
title: The surjectivity statement from twelve published inputs
kind: theorem
decl: GlobalTheory.BigOn.ontoX_of_hypotheses_alt_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.OntoXOfPrints
covers: 19069
status: drafted
drafted_by: writer@claude
---
This theorem proves `SurjectiveOntoX`, the statement that at almost all points of a family a certain map is onto. It takes twelve published inputs and assembles six estimates: export, twist, share, bad places, exponent and rank. Its only user is [`ontoX_and_lamLow_of_unitaryGroupHypotheses'`](/proof/unitary-hypotheses/), branch 2 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/), which passes it twelve fields of its bundle. Below this theorem are 19,069 declarations. The largest parts are [`runHolds_of_parOK`](/entry/run-holds-of-par-ok/) (5,710), [`geoSt_of_pageSt_alt`](/entry/geo-st-of-page-st-alt/) (5,131) and [`expSt_of_base_change_and_crystalline_lattices`](/entry/exp-st-of-base-change-and-crystalline-lattices/) (3,719).

## Statement

Assume the following twelve inputs. We give them by their Lean names and have not unfolded them here.

- Automorphic inputs: `GreenCuspidal`, `ClozelCohomological`, `CuspRapidDecay`, `DiscreteSeriesCover`, `CasselmanWallach`.
- Galois inputs: `HeckeLAdicCharacter` and `HeckeLAdicCharacterAbove` ($\ell$-adic characters attached to Hecke characters), `ChebotarevDegreeOne`, `CuspUAlt` (the caller passes its field for Galois representations of polarized cuspidal representations), `BaseChangeDefiniteUnitaryGroup` and `BhattScholzeCrystallineLattices`.
- `RecTExists`: a local Langlands correspondence. The caller builds it from the field `litN.loc.llc` by `llOf_alt`, as in the step [RecTExists](/step/rect-exists-def/).

Then `SurjectiveOntoX` holds. It says: for each closed family hypothesis and each family $F_m$ in it with `DIVinN` $F_m$, there is $C_0 \ge 0$ such that at all but finitely many points $p$ of $F_m$ with `More p`, and for all $C \ge C_0$, the map `p.S false` is onto the target `p.N C CH`. We have not unfolded `FamHyp`, `ON` or the objects at a point.

## Proof

1. `HeckeLAdicCharacter.globalArtin` takes the global Artin map out of `HeckeLAdicCharacter`. It gives the ray class field statement and the rational series statement `SeriesRatS`.
2. `exportSt_of_reciprocity_and_casselman_wallach` gives the export statement from the facts of step 1 and from `CuspRapidDecay`, `DiscreteSeriesCover` and `CasselmanWallach`. It is a second name for `exportSt_of_reading_alt`. The Lean proof finds its arguments by `with_reducible assumption`.
3. `pageSt_alt` proves the page statement with no input. [`geoSt_of_pageSt_alt`](/entry/geo-st-of-page-st-alt/) turns it into the geometric statement (bounds on leaves, spans, indices and depths).
4. `rankLocSt_of_max_geo_runs` gives the rank statement from the geometric one. `twistSt_of_alt` then gives the twist bound from the export, geometric and rank statements.
5. `modelSt_alt` proves a model statement. From it come the share statement and, with `GreenCuspidal`, the bad places statement.
6. [`expSt_of_base_change_and_crystalline_lattices`](/entry/exp-st-of-base-change-and-crystalline-lattices/) gives the exponent bound from the six Galois inputs, `ClozelCohomological` and `RecTExists`.
7. `ontoX_of_twist_shares_exp_alt` combines the twist, share, bad places and exponent statements.

All twelve inputs are used. [`runHolds_of_parOK`](/entry/run-holds-of-par-ok/) is not called here. Several lemmas below this theorem use it, and so it sits directly below this theorem in the tree.

## In the Lean code

The theorem is at [OntoXOfPrints.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OntoXOfPrints.lean#L28). The statements are defined in [ExportSt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExportSt.lean#L33).

- `ontoX_of_twist_shares_exp_alt` ([OntoXOfTwistSharesExp.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OntoXOfTwistSharesExp.lean#L22)) ignores its export argument. It proves the page and geometric statements again with other lemmas. So the export statement enters only through the twist bound.
- The words "hypotheses alt alt" in the name and "prints" in the file name say nothing about the statement.
