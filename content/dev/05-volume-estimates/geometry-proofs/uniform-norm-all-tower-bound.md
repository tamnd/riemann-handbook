---
id: uniform-norm-all-tower-bound
title: Small model sections descend to cusp sections (statement form)
kind: theorem
decl: GlobalTheory.T.uniform_norm_all_tower_bound
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.UniformNormAllTowerBoundStatement
covers: 313
status: drafted
drafted_by: writer@claude
---
This theorem is the statement form of [`Plug.descent_small`](/entry/descent-small/), which has the content. It is a second name with the same statement. [The counting lemma](/entry/model-small-encard-le/) uses it in its step 2.

## Statement

We use the notation of [the counting lemma](/entry/model-small-encard-le/). Assume `Top.Given`, `CompLaws`, `Ref.UnifAll` and the norm condition $\|\tau(\xi_0)\| = x$. Fix a good origin $o$ of a root tower, a level $B$, a component $b$, a generic frame, and a reading of a component $Z$ with `GeoRead`. Let $u$ be a weight with strictly decreasing rows, $R \geq 0$, and $s \in \mathcal M(u, R)$. Then there is a cusp section $f$ on $Z$ of weight $u$ with:

1. its value at the generic frame of $Z$ is $\mathrm{tr}_u(s)$;
2. its norm at each frame of $Z$ over each good embedding is at most $d R$, with $d$ the flag degree of the origin;
3. for each prime $p$, each prime $\lambda$ of $F$ above $p$ and each valuation $v$ of `recVals` at $\lambda$, $v(f) \geq -v_\lambda(p)\, e_2(p)\, \|u\|_1$ if $p \in S_B$, and $v(f) \geq 0$ otherwise.

## Proof

The proof is `exact Plug.descent_small`.

## In the Lean code

The theorem is in [UniformNormAllTowerBoundStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/UniformNormAllTowerBoundStatement.lean#L17). The name speaks of a norm bound, but the statement also gives the descent and a valuation bound.
