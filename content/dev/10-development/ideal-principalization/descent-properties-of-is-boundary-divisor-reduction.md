---
id: descent-properties-of-is-boundary-divisor-reduction
title: The descent hypotheses for maximal contact, from the divisor reductions
kind: theorem
decl: FunctorialResolution.EmbeddedResolution.OrderReductionProperties.descentProperties_of_isBoundaryDivisorReduction
module: Development.ResolutionOfSingularities.EmbeddedResolution.IdealPrincipalization.OrderReduction.OrderReductionCompatibility
covers: 335
status: drafted
drafted_by: writer@claude
---
This theorem proves the structure `DescentHypotheses` that [maximal contact is an order reduction](/entry/is-order-reduction-max-contact-of-is-boundary-position-invariant/) needs. It fills 17 fields, each with one lemma. Most of the fields do not depend on the hypotheses.

## Statement

We use the notation of the parent entry. Let $\iota$ prove `ComapIsoInvariance`, let $n \in \mathbb N$, let $(A_j)_j$ be a family of assignments and $L$ an assignment. Assume $\mathrm{Div}_{\delta \le n, j}(A_j, L)$ for all $j$ and $\mathrm{Pos}_{\delta \le n}(A)$.

**Theorem.** `DescentHypotheses` holds for $\iota$, the bound $\delta \le n$, $A$ and $L$.

## Proof

The fields fall into four groups.

1. **Field extension.** `maxContact_baseChange_isPullbackBlowupSequence` and `isStrictPullbackBlowupSeq_maxContact_baseChange` show that $\mathcal M_\iota(A)$ commutes with a change of base field. They use the $\mathrm{Div}$ hypothesis.
2. **Smooth pullback.** `maxContact_isPullback_of_smooth_of_orderAt_le_mult` gives the pullback along a smooth map. It uses both hypotheses. For a surjective smooth map the pullback is strict. This needs each centre to differ from the unit ideal, which comes from `CoverSequenceProperties` and `exists_isStrictPullback_cover_dropTrivialBoundary`.
3. **The cover.** The cover map is flat and surjective. The blow-up sequence on the cover has maps that are local isomorphisms, and its schemes are locally Noetherian. Order certificates descend along it (`orderCertificate_of_comap_of_isLocalIsomorphism`).
4. **Marked ideals.** The tuned ideal is marked, and it is $I$ itself when $m = 1$. Deleting the unit ideals from $E$ keeps admissibility and markedness. If $\operatorname{ord} I \le m$, the order stays $\le m$ along every marked sequence (`orderAt_sequenceOfBlowups_ideal_le_mult`). Two admissibility facts treat a closed subscheme of $X$ and a smooth divisor as boundary.

Groups 3 and 4 use neither hypothesis.

## In the Lean code

The theorem is in [OrderReductionCompatibility.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/OrderReduction/OrderReductionCompatibility.lean#L916). The structure is in [DescentHypotheses.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/OrderReduction/DescentHypotheses.lean#L90). We have not read the proofs of the lemmas named above.

The position hypothesis $\mathrm{Pos}$ is used only in the two smooth pullback fields. Some binders are unused: `_hO'` in the strict field extension field, and `_hbd`, `_hq` in the last field.
