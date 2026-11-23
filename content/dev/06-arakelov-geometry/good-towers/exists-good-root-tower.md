---
id: exists-good-root-tower
title: A good root tower exists (statement form)
kind: theorem
decl: GlobalTheory.T.exists_good_root_tower
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.ExistsGoodRootTowerStatement
covers: 517
status: drafted
drafted_by: writer@claude
---
This theorem is the statement form of [`TopTower.exists_good_tower`](/entry/exists-good-tower/), which has the real content. It is a second name with the same statement. [The good tower theorem](/entry/good-tower-and-volume/) uses it for its first conclusion, `GoodTowerExistsX`.

## Statement

Assume `Top.Given` ([the inputs](/entry/given-of-inputs/)), `Out.WeilSt` (the Weil pairing statement), `FlatLineGenerator` and `FlatLineGeneratorComponent` (flat generators of a line, on the model and on each component). Let $E$ be a CM field with a host $H$, a datum $D$ with $p, q \geq 1$, a level $l$, coefficients $c$ and an integral model $Y$ that is global (`Top.IsGlobal`) and has split components. Then there are a root tower $T$ for the CM types of $H$ and $N = p + q$, and a good origin $o$ of $Y$ for $T$, with the two conditions of `Extra`:

1. on each component $a$, each point of the analytic space has an open neighbourhood with holomorphic lifts $\lambda$ of the point map of $o$ (up to a nonzero scalar), and the affine charts of $\lambda$ have injective differential;
2. for each $B$, each $a$ and each prime $p$ of the set $S_B$ of $o$, the number $R(p)$ of the origin at level $B$ is $4$.

## Proof

The proof is `exact TopTower.exists_good_tower`.

## In the Lean code

The theorem is in [ExistsGoodRootTowerStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/ExistsGoodRootTowerStatement.lean#L12). The statement is copied word for word from `exists_good_tower`.
