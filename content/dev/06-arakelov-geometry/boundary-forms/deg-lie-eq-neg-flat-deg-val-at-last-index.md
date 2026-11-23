---
id: deg-lie-eq-neg-flat-deg-val-at-last-index
title: The degree of the Lie frame at a rational point, second name
kind: theorem
decl: GlobalTheory.T.degLie_eq_neg_flatDegVal_at_last_index
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.DegLieCoreStatement
covers: 533
status: drafted
drafted_by: writer@claude
---
This theorem is a second name of [degLie_core_alt](/entry/deg-lie-core-alt/). Its only user is [flatExistsAt_core_alt](/entry/flat-exists-at-core-alt/), which uses it to fix the degree of the flat sections at the last level. Below this theorem are 533 declarations.

## Statement

Use the notation of [flatExistsAt_core_alt](/entry/flat-exists-at-core-alt/). For a component $Z$ of the moduli space at level $i + 1$, point data $P$ on $Z$ (`PtData`) is a rational point of $Z$ with frames $B_w$ at the finite places $w$ of $F$ and $X_\sigma$ at the complex embeddings $\sigma$ of $F$. For an embedding $\tau$ of $E$, $\deg_{\mathrm{Lie}} P(\tau)$ is `detDeg` of the $\tau$-blocks of these frames (`degLie`). We have not unfolded `detDeg`.

**Theorem.** Let $p$ be a point with `RowsTAlt`, let $i + 1 = m$, and assume `GramAt`, `WtNum`, `HostNum` and `FnAlgClosed` at level $i + 1$. Then for each component $Z$, each point data $P$ on $Z$ and each $\tau \in \Psi$,
$$\deg_{\mathrm{Lie}} P(\tau_1) = -\mathrm{flatDegVal} = -\tfrac{p_i - q_i}{2} \log\Omega - q_i(\log d - \mathrm{lrd}(E)),$$
where $\tau_1$ is the embedding of $E$ under $\tau$.

## Proof

The proof is `exact degLie_core_alt`, inside a `first | ...` that tries three forms of the same call.

## In the Lean code

The theorem is at [DegLieCoreStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/DegLieCoreStatement.lean#L13). The file imports `ComponentPointLastIndexStatement`, which holds a parallel theorem `component_point_last_index`: the same statement with `RowsT` in place of `RowsTAlt`, proved by `degLie_core`. The proof here does not use it. At the last level $q_i = 0$, so the right side is $-\tfrac{p_i}{2}\log\Omega$. The real content is in [degLie_core_alt](/entry/deg-lie-core-alt/), which computes the degree from the log period `logOm` of a Kronecker character.
