---
id: flat-exists-at-last-index-of-fn-alg-closed
title: Flat sections of the expected degree, second name
kind: theorem
decl: GlobalTheory.T.flatExistsAt_last_index_of_fnAlgClosed
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.FlatExistsAtCoreStatement
covers: 549
status: drafted
drafted_by: writer@claude
---
This theorem is a second name of [flatExistsAt_core_alt](/entry/flat-exists-at-core-alt/). Its only user is [the defect bound at a point](/entry/defect-bound-of-connected-alt/), where it gives the flat sections that the eigenlattice bound needs. Below this theorem are 549 declarations.

## Statement

The statement is that of [flatExistsAt_core_alt](/entry/flat-exists-at-core-alt/), word for word. Let $p$ be a point with `RowsTAlt`, let $i + 1 = m$, and assume `GramAt`, `WtNum`, `HostNum` and `FnAlgClosed` at level $i + 1$. Then each component $Z$ of the moduli space at level $i + 1$ carries, for each $\tau \in \Psi$, a flat section, and each flat section $s$ has
$$\deg s = \mathrm{flatDegVal} = \tfrac{p_i - q_i}{2} \log\Omega + q_i(\log d - \mathrm{lrd}(E)).$$

## Proof

The proof is `exact flatExistsAt_core_alt`, inside a `first | ...` that tries three forms of the same call.

## In the Lean code

The theorem is at [FlatExistsAtCoreStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FlatExistsAtCoreStatement.lean#L13). The file imports `FlatExistsAtLastIndexStatement`, which holds a parallel theorem `flat_exists_at_last_index`: the same statement with `RowsT` in place of `RowsTAlt`, proved by `flatExistsAt_core`. The proof here does not use it. The name "of fnAlgClosed" names one of the five hypotheses at the point. That hypothesis always holds at these points: `fnAlgClosed_core_alt` proves it from `RowsTAlt` (see [the level statement](/entry/lifts-two-mul-def-bound-sub-unit-e-le-mu-core/)). The real content is in [degLie_core_alt](/entry/deg-lie-core-alt/).
