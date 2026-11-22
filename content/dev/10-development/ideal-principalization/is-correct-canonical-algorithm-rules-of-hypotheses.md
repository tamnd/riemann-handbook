---
id: is-correct-canonical-algorithm-rules-of-hypotheses
title: The principalization rules reduce by dimension, given the divisor and geometry hypotheses
kind: theorem
decl: FunctorialResolution.EmbeddedResolution.isCorrect_canonicalAlgorithmRules_of_hypotheses
module: Development.ResolutionOfSingularities.EmbeddedResolution.IdealPrincipalization.CanonicalRulesCorrect
covers: 2363
status: drafted
drafted_by: writer@claude
---
This theorem is the inductive step of the principalization algorithm: the canonical rules satisfy the four fields of `ReducesInductivelyOnDimension`. Its only user, [the rules reduce by dimension](/entry/is-correct-canonical-algorithm-rules/), proves its two structure hypotheses.

## Statement

**Marked ideals.** A marked ideal $T = (X, I, m, E)$ is a scheme $X$ over a field $k$, an ideal sheaf $I$, an integer $m$ and a boundary list $E$ of ideal sheaves. It is *admissible* if $\operatorname{char} k = 0$, $X$ is smooth over $k$, quasi-compact and locally of finite type, $I$ is nonzero on each component, $m \geq 1$ and $E$ is in strict normal crossing position. Let $\delta(T) = \dim X + 1$. A *marked sequence* is a sequence of [[blow-ups|4SFS82N88K]] $X = X_0 \leftarrow \dots \leftarrow X_r$ with ideals $I_i$ and boundaries $E_i$. It *resolves* $T$ if $\operatorname{ord} I_r < m$ everywhere on $X_r$. An *assignment* $L$ gives a marked sequence $L(T)$ for each $T$.

**The rules.** Rules $\mathcal{B}$ make a marked sequence for $T$ in three ways: divisor reduction $\mathcal{B}^{\mathrm{div}}(L, j)$, from an assignment $L$ on $\delta < \delta(T)$ and an index $j$; maximal order reduction $\mathcal{B}^{\max}(A)$, from an assignment $A$ on $\delta \leq \delta(T)$; order reduction $\mathcal{B}^{\mathrm{ord}}(D)$, from a family $(D_j)_j$ on $\delta \leq \delta(T)$.

**The four specifications.** Each applies to admissible $T$ with $P(\delta(T))$, for a bound $P$.

- $\mathrm{MaxOrd}_P(A, B)$: $A(T)$ resolves $T$; its centres are nonempty with certificates; it is empty when no point has order $\geq m$; it commutes with field extension and smooth pullback; it is isomorphic to $B(T)$ when $E$ is empty and $\operatorname{ord} I \leq m$.
- $\mathrm{Ord}_P(A, B)$: for $T$ with $\operatorname{ord} I \leq m$, the first four clauses of $\mathrm{MaxOrd}$ hold and the order stays $\leq m$. If also $E$ is empty, $m = 1$ and $I$ is the image of an ideal $J$ on a smooth divisor $Y \subset X$, then $A(T)$ is the pushforward of $B$ applied to $(Y, J)$.
- $\mathrm{Div}_{P,j}(A, B)$: for balanced $T$ with $\operatorname{ord} I \leq m$ and $j < |E|$, the clauses of $\mathrm{Ord}$ other than resolution and certificates hold, with the $j$-th boundary divisor in the role of $Y$. Also its strict transforms $F_t$ stay smooth divisors that contain the centres, and no point of the last $F_r$ has order $\geq m$.
- $\mathrm{Pos}_P(A)$ for a family $(A_j)_j$: for balanced $T$ with $\operatorname{ord} I \leq m$, $A_{|E_1|}$ on the boundary $E_1, F, E_2$ stays the same up to isomorphism when $E_1$, $E_2$ change only in unit ideal entries.

**Theorem.** Assume $h_{\mathrm{res}}$ : `StrictTransformIsBlowupOfClosedSubscheme`, `DivisorReductionHypotheses` $h_{\mathrm{res}}$ and `PrincipalizationGeometryHypotheses`. Then for each $n$, with $P_{<} = (\delta < n)$ and $P_{\leq} = (\delta \leq n)$:

1. if $\mathrm{MaxOrd}_{P_<}(L, O)$, then $\mathrm{Div}_{P_\leq, j}(\mathcal{B}^{\mathrm{div}}(L, j), L)$ for each $j$;
2. if $\mathrm{MaxOrd}_{P_<}(L, O)$, then $\mathrm{Pos}_{P_\leq}(j \mapsto \mathcal{B}^{\mathrm{div}}(L, j))$;
3. if $\mathrm{Ord}_{P_\leq}(A, L)$, then $\mathrm{MaxOrd}_{P_\leq}(\mathcal{B}^{\max}(A), A)$;
4. if $\mathrm{MaxOrd}_{P_<}(L, O)$, $\mathrm{Div}_{P_\leq, j}(D_j, L)$ for all $j$ and $\mathrm{Pos}_{P_\leq}(D)$, then $\mathrm{Ord}_{P_\leq}(\mathcal{B}^{\mathrm{ord}}(D), L)$.

`nextLevel` runs divisor, order, then maximal order reduction.

## Proof

Items 1 and 2 are `isBoundaryDivisorReduction_divisorFamily_canonicalAlgorithmRules` and `isBoundaryPositionInvariant_divisorFamily_canonicalAlgorithmRules`, from $h_{\mathrm{res}}$ and the divisor hypotheses. Item 3 is `MaxOrderReduction.isMaxOrderReduction_canonicalAlgorithmRules`, from the geometry hypotheses. Item 4 is [order reduction for the canonical rules](/entry/is-order-reduction-order-family-of-strict-transform-is-blowup/).

## In the Lean code

The theorem is in [CanonicalRulesCorrect.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/CanonicalRulesCorrect.lean#L20).

- `ReducesInductivelyOnDimension`, `PrincipalizationRules` and `nextLevel`: [DimensionRecursion.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/DimensionRecursion.lean#L79).
- `canonicalAlgorithmRules`: [CanonicalPrincipalization.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/CanonicalPrincipalization.lean#L26). The rules are `divisorReductionSeq`, `orderReductionSeq` for maximal order and the maximal contact `MaxContactReduction.reduceOrder` for order. The names cross.
- $\mathrm{MaxOrd}$, $\mathrm{Ord}$, $\mathrm{Div}$, $\mathrm{Pos}$ are `IsMaxOrderReduction`, `IsOrderReduction`, `IsBoundaryDivisorReduction`, `IsBoundaryPositionInvariant` in [OrderReductionProperties.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/OrderReductionProperties.lean#L299).
- `MarkedIdealWithBoundary` and `IsResolution`: [MarkedSequenceOfBlowups.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/MarkedBlowupSequence/MarkedSequenceOfBlowups.lean#L59).

We have not unfolded "balanced" (`IsDerivBalanced`) or the pullback relations.

The types `PrincipalizationCertificate` and `OrderCertificate` ([PrincipalizationCertificate.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/PrincipalizationCertificate.lean#L19)) have a constructor `large` that accepts any centre when $m \geq 2$. So the certificate clauses only have content for $m = 1$.
