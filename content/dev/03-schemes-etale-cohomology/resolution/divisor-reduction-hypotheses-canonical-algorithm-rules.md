---
id: divisor-reduction-hypotheses-canonical-algorithm-rules
title: The divisor reduction facts for the canonical rules
kind: theorem
decl: FunctorialResolution.EmbeddedResolution.divisorReductionHypotheses_canonicalAlgorithmRules
module: Development.ResolutionOfSingularities.EmbeddedResolution.IdealPrincipalization.DivisorReduction.CanonicalDivisorReduction
covers: 667
status: drafted
drafted_by: writer@claude
---
This theorem proves the structure `DivisorReductionHypotheses`, the list of facts on divisor reduction that [the correctness of the canonical rules](/entry/is-correct-canonical-algorithm-rules/) needs. The name says "hypotheses", but nothing here is assumed: each of the nine fields is proved. The only input is $\mathrm{hres}$, the statement that a strict transform is a blow-up, which the parent also takes.

## Statement

Let $\mathrm{hres}$ be `StrictTransformIsBlowupOfClosedSubscheme`. Then `DivisorReductionHypotheses hres` holds. Its nine fields, grouped by purpose:

- **The steps of divisor reduction.** `divisorReduction`, the twenty properties of one step (see [the step properties](/entry/divisor-reduction-step-properties-canonical-algorithm-rules/)), and `pushedBlowupSequenceProperties`, thirteen facts on the blow-up sequences that are built on $D_j$ and pushed into $X$, which we have not unfolded.
- **Compatibility with base change.** `baseChange` (smooth pullback), `fieldBaseChangeCompatibility` and `fieldLower` (field extension, the second one for the restriction to a divisor), and `smoothImpliesFlat` (a smooth morphism is flat). We have not unfolded the first three.
- **Degenerate cases.** `degenerateTransversal`: if the ideal of the components of $D_j$ in the order locus pulls back to the unit ideal, then the two ways to form the lower ideal and the lower boundary agree after pullback. `boundaryReindexingInvariance`: the lower ideal and boundary depend on the divisor $D_j$ and not on its index in the list. `trivial_of_coSupport_empty`: if the order locus of $T$ is nonempty but its smooth pullback has an empty order locus, then a sequence of length $0$ is a pullback of the divisor reduction sequence of $T$.

## Proof

First the step properties come from [`divisorReductionStepProperties_canonicalAlgorithmRules`](/entry/divisor-reduction-step-properties-canonical-algorithm-rules/). From them, `toDivisorReductionTerminationProperties` gives the facts that the two compatibility helpers need. Then each field is one lemma:

- `smoothPullbackCompatibility_of_divisorReductionTermination` and `fieldBaseChangeCompatibility_of_divisorReductionTermination`, private, in the same file;
- `divisorRestrictionFieldBaseChange`, `emptyPulledBackCenterCompatibility` and `pushedBlowupSequenceProperties_canonicalAlgorithmRules`, private, in the same file;
- `DivisorReduction.boundaryReindexingInvariance`;
- `divisorFamily_isPullbackSequenceOfBlowups_of_orderAtLeastLocus_empty`, for the empty case;
- `infer_instance`, for flatness.

We have not unfolded the proofs of the helpers.

## In the Lean code

The theorem is in [CanonicalDivisorReduction.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/DivisorReduction/CanonicalDivisorReduction.lean#L155). The structure is in [DivisorReductionHypotheses.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/DivisorReduction/DivisorReductionHypotheses.lean#L35). Two fields, `divisorReduction` and `pushedBlowupSequenceProperties`, fix the noetherian input to the proved fact `blowupPreservesNoetherian`. The field `smoothImpliesFlat` is a standard fact that Mathlib supplies as an instance.
