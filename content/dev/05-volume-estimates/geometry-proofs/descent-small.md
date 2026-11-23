---
id: descent-small
title: A small model section gives a small cusp section on the component
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Plug.descent_small
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.UniformNormAllTowerBound
covers: 312
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement of [`T.uniform_norm_all_tower_bound`](/entry/uniform-norm-all-tower-bound/), which states it in full. From a small section $s$ on a root model it makes a cusp section $f$ on the component $Z$ whose value at the generic frame is the trace of $s$, and it bounds the norms and the valuations of $f$. [The counting lemma](/entry/model-small-encard-le/) uses it through the statement form. The proof joins four lemmas: one for each of existence, the norm bound, membership in the cusp space and the valuation bound.

## Statement

The statement is that of [`T.uniform_norm_all_tower_bound`](/entry/uniform-norm-all-tower-bound/). Recall that $s \in \mathcal M(u, R)$ means two things: $s$ is in the chart lattice of degree $u$, and $s$ satisfies the Hodge bound `HodgeLe` of size $R$.

## Proof

1. The tower has $j = p$ and $1 \leq j < p + q$, so $p, q \geq 1$.
2. `T.comp_laws_tower_bound` (from `Top.Given` and `CompLaws`) uses the chart lattice condition. It gives $f$ in the space `secZ` of sections of weight $u$, supported on $Z$, with value $\mathrm{tr}_u(s)$ at the generic frame.
3. `T.uniform_norm_tower_bound` (with the norm condition on $\xi_0$) uses the Hodge bound. It bounds the norm of $f$ by $d R$ at each frame of $Z$ over each good embedding.
4. `bdd_mem_cuspOn` uses $p, q \geq 1$, the strictly decreasing rows of $u$, and the bound of step 3. It shows that $f$ is a cusp section on $Z$.
5. `T.uniform_all_tower_bound` (with `Ref.UnifAll`) gives the lower bound for the valuations of $f$.

## In the Lean code

The theorem is in [UniformNormAllTowerBound.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/UniformNormAllTowerBound.lean#L22). The lemmas are in their statement files, and `bdd_mem_cuspOn` is in [WeightZeroSectionMembership.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/WeightZeroSectionMembership.lean#L23).

Each hypothesis is used by one of the four lemmas. The valuation bound of step 5 does not need the Hodge bound or the norm condition: `uniform_all_tower_bound` takes only the chart lattice condition. The name `descent_small` describes the result better than the name of its statement form.
