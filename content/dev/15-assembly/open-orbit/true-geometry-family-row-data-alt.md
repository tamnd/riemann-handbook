---
id: true-geometry-family-row-data-alt
title: The family conditions for a real package, the statement form
kind: theorem
decl: GlobalTheory.T.true_geometry_family_row_data_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.FamAllQOfAllTrueStatement
covers: 9705
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It states the result of [the family conditions from the package conditions](/entry/fam-all-q-of-all-true-alt/) and proves it by calling that theorem. The real content is in that entry. Its only user is [`miStar2_of_allTrue_alt_alt`](/entry/mi-star2-of-all-true-alt-alt/), which takes the conclusion `FamilyAllConditions W` and gives it to `mi_star2_of_pu_nz`. This subtree is part of the multiplicity condition of branch 3 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/), below [`main_theorem_published_inputs_third_alt_alt`](/entry/main-theorem-published-inputs-third-alt-alt/).

## Statement

Assume the four named hypotheses `CuspRapidDecay`, `DiscreteSeriesCover`, `HarishChandraModules` and `StrongApproxSU`. Let $W$ be a real package (`RealPackAlt`) over the datum $D$ = `I.rec7 l Z`. Assume `AllFamilyConditions W`, $1 \le r_S$ for the base datum, and `OntoAll D`. Then `FamilyAllConditions W` holds.

[The family conditions from the package conditions](/entry/fam-all-q-of-all-true-alt/) says what each of these predicates means.

## Proof

The proof is `first | exact @GlobalTheory.MiTop.famAllQ_of_allTrue_alt | ...`. It applies that theorem. The two statements are the same, word for word.

## In the Lean code

The theorem is in [FamAllQOfAllTrueStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FamAllQOfAllTrueStatement.lean#L16). It is used once, in [MainTheoremFromPublishedResultsAltAltAltAlt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MainTheoremFromPublishedResultsAltAltAltAlt.lean#L26).

The name says "row data", but the conclusion is the full list of family conditions, not a statement about rows. The file also imports `TrueGeometryFamilyRowDataStatement` from `AbelianVarietyTheory.Proofs.DecoratedLatticeProofs`. That file has a theorem with the same name without `_alt`. It is a parallel copy for the structure `RealPack` in place of `RealPackAlt`, with conclusion `FamAllQ W`.
