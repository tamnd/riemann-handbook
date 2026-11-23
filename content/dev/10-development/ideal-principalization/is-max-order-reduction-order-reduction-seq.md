---
id: is-max-order-reduction-order-reduction-seq
title: The order reduction sequence reduces the maximal order
kind: theorem
decl: FunctorialResolution.EmbeddedResolution.MaxOrderReduction.isMaxOrderReduction_orderReductionSeq
module: Development.ResolutionOfSingularities.EmbeddedResolution.IdealPrincipalization.MarkedOrderReduction.MaxOrderReduction
covers: 639
status: drafted
drafted_by: writer@claude
---
This theorem proves the specification of maximal order reduction for the algorithm `orderReductionSeq`. The theorem [maximal order reduction for the canonical rules](/entry/is-max-order-reduction-canonical-algorithm-rules/) is this theorem with the isomorphism invariance `comapIsoInvariance` put in. That theorem is item 3 of [the rules reduce by dimension, given the hypotheses](/entry/is-correct-canonical-algorithm-rules-of-hypotheses/), whose notation we use: marked ideals $T = (X, I, m, E)$, admissibility, $\delta(T) = \dim X + 1$, and the specifications $\mathrm{Ord}_P$ and $\mathrm{MaxOrd}_P$.

## Statement

Assume the geometry hypotheses (`PrincipalizationGeometryHypotheses`) and invariance under isomorphism (`ComapIsoInvariance`, four fields). Let $n \ge 0$ and let $A$, $L$ be assignments with $\mathrm{Ord}_{\delta \le n}(A, L)$.

**Theorem.** Let $C(T)$ be `orderReductionSeq` of $T$, with $A$ as the recursive call. Then $\mathrm{MaxOrd}_{\delta \le n}(C, A)$. For the canonical rules, $C$ is $\mathcal B^{\max}(A)$.

So for each admissible $T$ with $\delta(T) \le n$: each step of $C(T)$ has a principalization certificate and a centre with nonempty support; $C(T)$ is a resolution; $C(T)$ is empty when the locus $\{x : \operatorname{ord}_x I \ge m\}$ is empty; $C(T)$ is isomorphic to $A(T)$ when $E = \emptyset$ and $\operatorname{ord}_x I \le m$ at all $x$; and $C$ commutes with field extension and with smooth pullback, in the plain and the strict sense.

The algorithm, from [OrderReductionAlgorithm.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/MarkedOrderReduction/OrderReductionAlgorithm.lean#L189): if the locus is empty, the empty sequence. Else write $I = M \cdot N$, after the steps so far, with $M$ monomial and supported on the boundary. Reduce the companion ideal $N^m + I^c$ with mark $mc$, where $c$ is the maximal order of $N$ on the locus. Then principalize the monomial part that is left. Each stage calls $A$ on marked ideals with $\delta \le \delta(T)$.

## Proof

The proof fills the nine fields of `IsMaxOrderReduction` from lemmas on `orderReductionSeq`. First `monomialPrincipalization_spec` gives the hypotheses on monomial principalization from the geometry hypotheses.

- Certificate, nonempty centres, resolution: `certificate_orderReductionSeq`, `center_support_nonempty_orderReductionSeq`, `isResolution_orderReductionSeq`.
- Empty locus: `orderReductionSeq_length_eq_zero_of_orderAtLeastLocus_empty`.
- Isomorphism with $A(T)$: `orderReductionSeq_isomorphic_of_boundary_nil`.
- Field extension and smooth pullback: `orderReductionSeq_isPullbackBlowupSequence_pullbackOverField`, with the compatibility from `baseChangeCompatible_baseChangeProj_of_isOrderReduction` or `baseChangeCompatible_of_smooth`.
- The strict forms: `isStrictPullback_of_surjective`, with the nonempty centres. For field extension, the projection is surjective by `instSurjectivePullbackFstSpecMapField`.

We have not unfolded these lemmas.

## In the Lean code

The theorem is in [MaxOrderReduction.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/MarkedOrderReduction/MaxOrderReduction.lean#L80). The specification is in [OrderReductionProperties.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/OrderReductionProperties.lean#L299).

- $L$ (named `B` in Lean) occurs only through $\mathrm{Ord}_{\delta \le n}(A, L)$. The lemmas use it for the certificates and the base change compatibility.
- The recursive call is `principalizationOfDimLe T A`, which is $A$ itself: the dimension bound is an argument that it does not use.
