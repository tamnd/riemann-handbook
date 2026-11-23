---
id: divisor-reduction-properties-of-blowup-preserves-noetherian
title: The divisor reduction properties
kind: theorem
decl: FunctorialResolution.EmbeddedResolution.divisorReductionProperties_of_blowupPreservesNoetherian
module: Development.ResolutionOfSingularities.EmbeddedResolution.IdealPrincipalization.DivisorReduction.BalancedDivisorReduction
covers: 428
status: drafted
drafted_by: writer@claude
---
This theorem proves the fourteen fields of `DivisorReductionProperties`. With six more facts on the subscheme $Z_j$, they give [the step properties of divisor reduction](/entry/divisor-reduction-step-properties-canonical-algorithm-rules/), which feed [the divisor reduction facts for the canonical rules](/entry/divisor-reduction-hypotheses-canonical-algorithm-rules/).

## Statement

Divisor reduction at a boundary divisor $D_j$ of a marked ideal $T = (X, I, m, E)$ works as follows, by `divisorReductionSeq` in [DivisorReductionSequence.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/DivisorReduction/DivisorReductionSequence.lean#L173). Let $Z_j$ be the union of the connected components of $D_j$ that lie in the locus $\{\operatorname{ord} I \ge m\}$. If $Z_j$ is empty, restrict $T$ to $D_j$, run a sequence of blow-ups $s$ on $D_j$, and push $s$ into $X$. If $Z_j$ is not empty, first blow up $Z_j$ (a divisor, so the blow-up is the identity), divide $I$ by $I_{Z_j}^m$, add the exceptional divisor to the boundary, then restrict and push as before.

Call $T$ balanced if $(\mathcal{D}^i I)^m \subseteq I^{m-i}$ for each $i < m$, where $\mathcal{D}^i I$ is the ideal of derivatives of order at most $i$ (`IsDerivBalanced`).

**Theorem.** Let hres say that a strict transform is a blow-up, and let hno say that a blow-up of a noetherian scheme is noetherian. Then for each admissible, balanced $T$ with $\operatorname{ord}_x I \le m$ at all $x$, each $j$, and each sequence $s$ on $D_j$ whose centres contain no component:

- **Marking.** The pushed sequence is marked, in both cases. The twisted restriction is admissible.
- **Order.** The order of the controlled transform of $I$ stays at most $m$ along the pushed sequence. If $s$ ends with an empty order locus, then the final order locus in $X$ does not meet the transform of $D_j$.
- **Restriction.** The controlled transform, pulled back to the transform of $D_j$, is the ideal of $s$ at each stage.
- **Functoriality.** Pushing a sequence commutes with flat pullback, in the plain and the strict sense. $Z_j$ commutes with field extension and with smooth pullback.
- **A degenerate case.** If $m = 1$ and $I$ is the image of an ideal on $D_j$, then $Z_j$ is empty.

## Proof

First `hasStrictNormalCrossingsWith_ker_cons_of_comap` gives `StrictNormalCrossingsLiftFromDivisor`: a subscheme of $D_j$ with normal crossings with $E|_{D_j}$ has normal crossings with $E$ in $X$. Then each field is one lemma:

- marking: `isMarked_ambientBlowupSeq_of_containedComponentsIdeal_eq_top`, `isMarked_prepend_ambientBlowupSeq`, `isAdmissible_restrictTwistedToDivisor`;
- order: `orderAt_controlledTransform_le_of_isMarked`; for the empty locus, `orderAtLeastLocus_inter_support_ker_eq_empty` with the private `goingUpInvariant_length_of_isBalanced` (which calls `goingUpInvariant_of_le`), and in the second case `exists_isClosed_opens_goingUpInvariantOnOpen`;
- restriction: `comap_controlledTransform_of_containedComponentsIdeal_eq_top`, `comap_controlledTransform_prepend_ambientBlowupSeq`;
- functoriality: `isPullbackBlowupSequence_ambientBlowupSequence_of_flat`, `isStrictPullbackBlowupSeq_ambientBlowupSequence_of_flat`, `containedComponentsIdeal_baseChange`, `containedComponentsIdeal_pullbackAlong_of_smooth`;
- degenerate case: `containedComponentsIdeal_eq_top_of_eq_imageIdealSheaf`.

We have not unfolded these lemmas. The marking lemmas and the going-up lemma are the ones that use balance.

## In the Lean code

The theorem is in [BalancedDivisorReduction.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/DivisorReduction/BalancedDivisorReduction.lean#L91). The structure is in [DivisorReductionProperties.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/DivisorReduction/DivisorReductionProperties.lean#L29). The name mentions only hno, but the theorem takes hres too. hno is not an open hypothesis: the caller passes the proved `blowupPreservesNoetherian`. In the Lean code "$Z_j$ is empty" is the statement that `containedComponentsIdeal` is the unit ideal.
