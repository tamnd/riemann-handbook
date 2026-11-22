---
id: is-order-reduction-max-contact-of-is-boundary-position-invariant
title: Order reduction by maximal contact
kind: theorem
decl: FunctorialResolution.EmbeddedResolution.OrderReductionProperties.isOrderReduction_maxContact_of_isBoundaryPositionInvariant
module: Development.ResolutionOfSingularities.EmbeddedResolution.IdealPrincipalization.OrderReduction.OrderReductionCompatibility
covers: 1290
status: drafted
drafted_by: writer@claude
---
This theorem says that the maximal contact construction is an order reduction, once the divisor reductions in the boundary behave well. Its only user is [order reduction for the canonical rules](/entry/is-order-reduction-order-family-of-strict-transform-is-blowup/), which rewrites the order rule of the canonical rules into this construction. The method of reducing the order of a marked ideal through a hypersurface of maximal contact is the core of Włodarczyk, *Simple Hironaka resolution in characteristic zero* (J. Amer. Math. Soc. 18, 2005). The Lean statement is a formal specification of that step. We do not claim that it matches a theorem of that paper.

## Statement

We use the notation of [the rules reduce by dimension, given the hypotheses](/entry/is-correct-canonical-algorithm-rules-of-hypotheses/): marked ideals $T = (X, I, m, E)$, $\delta(T) = \dim X + 1$, assignments, and the specifications $\mathrm{MaxOrd}$, $\mathrm{Ord}$, $\mathrm{Div}$, $\mathrm{Pos}$.

Let $\iota$ prove `ComapIsoInvariance`: four facts saying that the locus of order $\geq m$, strict normal crossings, smoothness of a centre and strict transforms are compatible with pullback along an isomorphism of schemes. Let $n \in \mathbb{N}$, let $(A_j)_j$ be a family of assignments and let $L, L'$ be assignments. Assume

1. $\mathrm{MaxOrd}_{\delta < n}(L, L')$;
2. $\mathrm{Div}_{\delta \leq n, j}(A_j, L)$ for all $j$;
3. $\mathrm{Pos}_{\delta \leq n}(A)$.

Then $\mathrm{Ord}_{\delta \leq n}(\mathcal{M}_\iota(A), L)$, where $\mathcal{M}_\iota(A)$ is the maximal contact assignment.

**The assignment $\mathcal{M}_\iota(A)$.** For $T$ not admissible, or with no point of order $\geq m$, it is the empty sequence. Otherwise it deletes the unit ideals from $E$, forms a tuned ideal $W$ and a tuned exponent $\mu$, takes a maximal contact cover of $X$, reduces along the hypersurface with the family $A$, and descends the result to $X$ by strict pullback. If the descent fails, it is the empty sequence. We have not unfolded the tuned ideal, the cover or the descent.

## Proof

Two structures of properties come from the hypotheses on $A$.

1. `coverSequenceProperties_of_isBoundaryDivisorReduction` proves `CoverSequenceProperties` from hypothesis 2 alone. Its five fields say, for the sequence on the cover: the centres are not the unit ideal; they carry order certificates when $m = 1$; the sequence descends to $X$; for $E$ empty and $m = 1$ it is the strict pullback of $A_0$ applied to the smooth divisor; and it resolves the tuned marked ideal.
2. `descentProperties_of_isBoundaryDivisorReduction` proves `DescentHypotheses`, a structure of 17 fields, from hypotheses 2 and 3. They concern descent of certificates, field extension, smooth pullback, the bound $\operatorname{ord} \leq m$, flatness and surjectivity of the cover map, and admissibility after the unit ideals are deleted.

Then `MaxContactFunctoriality.isOrderReduction_maxContact_dim_le_of_descentHypotheses` takes $\iota$, hypotheses 1 and 2 and the two structures, and gives the conclusion. It is the general `isOrderReduction_maxContact_of_descentHypotheses` with the bounds $\delta \leq n$ and $\delta < n$.

## In the Lean code

The theorem is in [OrderReductionCompatibility.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/OrderReduction/OrderReductionCompatibility.lean#L1001). The proof is one term with the three lemmas above.

- `coverSequenceProperties_of_isBoundaryDivisorReduction` ([L405](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/OrderReduction/OrderReductionCompatibility.lean#L405)) and `descentProperties_of_isBoundaryDivisorReduction` ([L916](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/OrderReduction/OrderReductionCompatibility.lean#L916)), in the same file. The file also holds the lemmas that they use, for example `maxContact_isPullback_of_smooth_of_orderAt_le_mult` and `isStrictPullbackBlowupSeq_maxContact_baseChange`.
- `isOrderReduction_maxContact_dim_le_of_descentHypotheses`, in [MaxContactOrderReduction.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/OrderReduction/MaxContactOrderReduction.lean#L90).
- `maxContactPrincipalization` and the two structures, in [DescentHypotheses.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/OrderReduction/DescentHypotheses.lean#L31). The construction `reduceOrder` is in [MaxContactReduction.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/OrderReduction/MaxContactReduction.lean#L220).
- `ComapIsoInvariance` is in [Append.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/MarkedBlowupSequence/Append.lean#L268). The caller passes the proved `comapIsoInvariance`.

The assignment $L'$ appears only in hypothesis 1. The name refers to hypothesis 3. Only the descent structure uses it.
