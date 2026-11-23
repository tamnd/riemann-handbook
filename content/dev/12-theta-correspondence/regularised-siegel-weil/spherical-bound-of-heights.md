---
id: spherical-bound-of-heights
title: The edge bound for spherical Eisenstein series, given heights, under its statement name
kind: theorem
decl: GlobalTheory.T.spherical_bound_of_heights
module: Development.AutomorphicSpectrum.Proofs.BlockDecomposition.SphericalBoundOfHeightsStatement
covers: 418
status: drafted
drafted_by: writer@claude
---
This theorem is a second name of [`sphBound_of_htExist`](/entry/sph-bound-of-ht-exist/). Its only user is [`sphBound`](/entry/sph-bound/), which applies it to `htExist` and gives the bound to [`resCore`](/entry/res-core/). The entry [`sphBound_of_htExist`](/entry/sph-bound-of-ht-exist/) has the mathematics.

## Statement

**Theorem.** `HtExist` implies `SphBound`.

`HtExist` says: for each datum and each $n$, there is a height on $G = U(n,n)(\mathbb{A}_F)$, and there is a compact $C_0 \subset G$ with $G = P \cdot C_0$, where $P$ is the Siegel parabolic. `SphBound` is the bound of the [entry for `sphBound`](/entry/sph-bound/): for $p \ge 1$, a height $H$ and a compact $C$, the sums $(\sigma - p/2) \sum_{\gamma \in P(F) \backslash G(F)} H(\gamma h)^{\sigma + p/2}$ converge and are bounded for $\sigma \in (p/2, p/2 + 1]$ and $h \in C$.

## Proof

The proof is the tactic

```
first | exact @GlobalTheory.CompanionTheory.SphPole.sphBound_of_htExist | ...
```

Each branch applies `sphBound_of_htExist`, and the two types are the same. So the theorem is that lemma.

## In the Lean code

The theorem is in [SphericalBoundOfHeightsStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/SphericalBoundOfHeightsStatement.lean#L6). The file imports the file of `sphBound_of_htExist`, [SphericalBoundOfHeights.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/SphericalBoundOfHeights.lean#L360), and states the same type in the namespace `GlobalTheory.T`. The same pattern, a statement file with a `first | exact ...` proof, is also used for `split_place_rank_cut_of_alternative` and `section_eigenfunction_maximal_compact` (see [the entry for `jPos_of_idemEx`](/entry/j-pos-of-idem-ex/)). The option `maxHeartbeats 1000000` has no visible purpose for a one-step proof.
