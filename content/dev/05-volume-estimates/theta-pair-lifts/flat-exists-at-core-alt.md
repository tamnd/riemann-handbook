---
id: flat-exists-at-core-alt
title: Flat sections of the expected degree at the last level
kind: theorem
decl: GlobalTheory.DefFlat.flatExistsAt_core_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.FlatExistsAtCore
covers: 548
status: drafted
drafted_by: writer@claude
---
This theorem says that at the last level each component of the moduli space carries flat sections, and that each of them has degree $\mathrm{flatDegVal}$. Its only user is its renaming [flatExistsAt_last_index_of_fnAlgClosed](/entry/flat-exists-at-last-index-of-fn-alg-closed/), which is step 3 of [the defect bound at a point](/entry/defect-bound-of-connected-alt/). Below this theorem are 548 declarations.

## Statement

Use the point $p$, the level $i$ and the notation of [the defect bound at a point](/entry/defect-bound-of-connected-alt/). Let $X$ be the moduli space at level $i + 1$ over the coefficient field $F$, and $U$ its family of uniformizations. For a component $Z$ of $X$ and $\tau \in \Psi$, `FlatSec U ξ Z τ` is the type of flat sections on $Z$ at $\tau$, and each such section $s$ has a degree $\deg s$. We have not unfolded `FlatSec`.

**Theorem.** Let $p$ satisfy `RowsTAlt`, let $i + 1 = m$, and assume `GramAt`, `WtNum`, `HostNum` and `FnAlgClosed` at level $i + 1$. Then for each component $Z$ and each $\tau \in \Psi$, a flat section on $Z$ at $\tau$ exists, and each such section $s$ has
$$\deg s = \mathrm{flatDegVal} = \tfrac{p_i - q_i}{2} \log\Omega + q_i(\log d - \mathrm{lrd}(E)).$$

In Lean this is `FlatExistsAt U ξ (-flatDegVal)`, which asks for degree $-(-\mathrm{flatDegVal})$.

## Proof

`finite_nonempty_components_and_dict_mem_dom` gives the definite case `DefCase`.

1. **Existence.** `nonempty_flatSec` builds a flat section from five fields of `DefCase`: $q_i = 0$, $p_i \ge 1$, good reduction at all primes, the condition `IsUnf` on the uniformizations, and `FnAlgClosed`.
2. **Degree.** `nonempty_definiteRationalPointData_component` gives point data $P$ on $Z$: a rational point of $Z$ with local frames at the finite places and the infinite places (`PtData`). It has a degree $\deg_{\mathrm{Lie}} P(\tau)$ (`degLie`). `degree_dualDetLie_eq_neg_flatSection_degree` gives $\deg_{\mathrm{Lie}} P(\tau) = -\deg s$. [degLie_eq_neg_flatDegVal_at_last_index](/entry/deg-lie-eq-neg-flat-deg-val-at-last-index/) gives $\deg_{\mathrm{Lie}} P(\tau) = -\mathrm{flatDegVal}$. So $\deg s = \mathrm{flatDegVal}$.

## In the Lean code

The theorem is at [FlatExistsAtCore.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FlatExistsAtCore.lean#L14). It calls `GlobalTheory.T.finite_nonempty_components_and_dict_mem_dom`, `GlobalTheory.FlatLine.Definite.nonempty_flatSec`, `GlobalTheory.T.nonempty_definiteRationalPointData_component`, `GlobalTheory.T.degree_dualDetLie_eq_neg_flatSection_degree` and `GlobalTheory.T.degLie_eq_neg_flatDegVal_at_last_index`.

The value of the degree comes from the last of these. Its proof, [degLie_core_alt](/entry/deg-lie-core-alt/), itself rewrites $\deg_{\mathrm{Lie}} P(\tau)$ as $-\deg s$ by the same lemma and computes $\deg s$ from a period of a Kronecker character. So the detour through $P$ here only moves the result of `degLie_core_alt` back to flat sections. The real content is in [degLie_core_alt](/entry/deg-lie-core-alt/).
