---
id: lift-restriction-bijective-low-degrees
title: Restriction along a smooth lift is bijective in degrees 1 and 2 (statement form)
kind: theorem
decl: GlobalTheory.T.lift_restriction_bijective_low_degrees
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.LiftRestrictionBijectiveLowDegreesStatement
covers: 315
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`Lift.resMap_lift_pullbackBijectiveDegreesOneTwo`](/entry/res-map-lift-pullback-bijective-degrees-one-two/), which has the real content. It is fact (b) in the proof of [`rel_total_zero`](/entry/rel-total-zero/).

## Statement

We use the notation of [`rel_total_zero`](/entry/rel-total-zero/). Let $D$ be a datum and $\Lambda$ a lift of $D$. The functor $\Lambda.L$ sends each affine open $U$ of $X$ to a PD thickening in $\mathrm{Thick}(D)$. Restriction of cochains along $\Lambda.L$ is a map of complexes from the total complex of $\mathrm{KK}$ to the total complex of $\mathrm{KK} \circ \Lambda.L$.

**Theorem.** For each $D$ and each $\Lambda$, this restriction map induces bijections
$$H^1(\mathrm{KK}) \to H^1(\mathrm{KK} \circ \Lambda.L), \qquad H^2(\mathrm{KK}) \to H^2(\mathrm{KK} \circ \Lambda.L).$$

## Proof

The proof is the term `GlobalTheory.PDForm.Lift.resMap_lift_pullbackBijectiveDegreesOneTwo`.

## In the Lean code

The theorem is in [LiftRestrictionBijectiveLowDegreesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LiftRestrictionBijectiveLowDegreesStatement.lean#L7). The proof is a `first` tactic whose first branch, `exact @GlobalTheory.PDForm.Lift.resMap_lift_pullbackBijectiveDegreesOneTwo`, closes the goal. The statement repeats the type of that lemma word for word. The lemma is in [LiftRestrictionBijectiveLowDegrees.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LiftRestrictionBijectiveLowDegrees.lean#L64). It writes $\Lambda.L$ as the composite of $\Lambda.\mathrm{toE}$ and a projection `pE`, and proves the two bijections separately. The property `PullbackBijectiveDegreesOneTwo` is the conjunction of the two bijections, in [PullbackBijectiveDegreesOneTwo.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/PullbackBijectiveDegreesOneTwo.lean#L277).
