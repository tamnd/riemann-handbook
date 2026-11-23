---
id: tool-statements-hold
title: The tool statements from the extremal projector
kind: theorem
decl: Formalism.MainNotions.G.tool_statements_hold
module: Formalism.SharpRestriction.GrowthBounds.PlaneCountTheoremWithConstants
covers: 631
status: drafted
drafted_by: writer@claude
---
This theorem proves three bundles of tool statements for a datum $D$, from one hypothesis on the extremal projector. Seven theorems of the same file take the bundles apart, among them [the admitted statements in closed form](/entry/first-theorem-admitted-closed/). Through them it lies below the step [EveryCharacter from theta integrals and local matching](/step/theta-local-matching/). The largest part below is [the seven statements on path polynomials](/entry/splitting-package-holds/).

## Statement

Let $K$ be a field of characteristic $0$ and $V$ a finite-dimensional representation of $\mathfrak{gl}_n$ over $K$, with operators $E_{ab}$ (`GLOps`, `IsGLRep`). For a weight $\mu$ and $a < b$, put $h_{ab} = \mu_a - \mu_b + b - a$. For an order of the pairs $a < b$ of the right kind (`NormalOrder`) and $T \in \mathbb{N}$, let $p_\mu$ be the ordered product of the factors
$$\sum_{k=0}^{T} \frac{(-1)^k}{\binom{h_{ab} + k}{k}}\, E_{ba}^{(k)} E_{ab}^{(k)},$$
with divided powers $E^{(k)}$ (`pp`).

The hypothesis `ExtremalProjectorTools` says, for every $D$ (`adm5`): if $h_{ab} \ge 1$ for all $a < b$ and $T \ge \dim V$, then $p_\mu$ maps the $\mu$-weight space to itself, kills the $\mu$-weight vectors in $\sum_{b<a} E_{ab} V$, and fixes the $\mu$-weight vectors killed by all $E_{ab}$ with $a < b$.

**Theorem.** Under this hypothesis, for each $D$:

1. `Conclusion1 D`: five groups of statements, named `ProjectionTheorems`, `ValuationLemmaField`, `ConclusionE`, `UnitProductLemmas` and `DerivativeLemmaField` (not unfolded here);
2. `Conclusion2 D`: [the seven statements on path polynomials](/entry/splitting-package-holds/);
3. `HyperplaneRank D`: over a discrete valuation ring $O$, the polynomials $\Psi(\mu, I)$ for paths $\mu$ of dominant weights and standard tableaux $I$ are linearly independent, and they span the polynomials of multidegree $B$.

## Proof

The proof builds `admitted D`, five statements, from four proved theorems and the hypothesis:

- `positivity_condition_holds`: the alternant of $\lambda + \rho$ times the complete symmetric polynomial $h_b$ is the sum of the alternants of $\mu + \rho$ over $\mu$ that interlace with $\lambda$ and have $|\mu| = |\lambda| + b$. This is Pieri's rule (Macdonald, *Symmetric Functions and Hall Polynomials*, Chapter I, Section 5).
- `weight_condition_from_integral_form`: every invariant subspace of a finite-dimensional representation of $\mathfrak{gl}_n$ in characteristic $0$ has an invariant complement.
- `exponent_condition_holds`: $v_p\binom{m}{k}$ is the number of carries when one adds $k$ and $m - k$ in base $p$ (Kummer's theorem).
- `key_positivity_condition`: if an irreducible $w$ of a factorial domain divides $FG$ in a polynomial ring, it divides $F$ or $G$ (Gauss's lemma).
- the hypothesis, for `adm5 D`.

Then `GLWeightTheory.problem_holds` gives `Conclusion1 D`. `ColumnFamilies.splitting_package_holds` gives `Conclusion2 D`, and `ColumnFamilies.Top.a2` gives `HyperplaneRank D`. Neither of the last two uses the hypothesis.

## In the Lean code

The theorem is in [PlaneCountTheoremWithConstants.lean](lean:Formalism/SharpRestriction/GrowthBounds/PlaneCountTheoremWithConstants.lean#L1009). The five admitted statements are in [CovariantDegrees.lean](lean:Formalism/SharpRestriction/GrowthBounds/CovariantDegrees.lean#L22), `Conclusion2` in [StatementOfDegreeAndBound.lean](lean:Formalism/SharpRestriction/GrowthBounds/StatementOfDegreeAndBound.lean#L437), and `HyperplaneRank` in [ConclusionA2.lean](lean:Formalism/SharpRestriction/GrowthBounds/ConclusionA2.lean#L12).

Odd points:

- `problem_holds` reads only the fifth part of `admitted D` ([GLWeightTheory.lean](lean:Formalism/SharpRestriction/GrowthBounds/GLWeightTheory.lean#L150)). The four proofs of the first four parts are built and then not used.
- The hypothesis is not open. Both places that build `ExtremalProjectorTools` fill it with `extremal_projector_statement` ([TruncatedChains.lean](lean:Formalism/SharpRestriction/GrowthBounds/TruncatedChains.lean#L19)).
- The name `ArchimedeanSignatureMatching` is used for Gauss's lemma.
