---
id: global-count-of-split-mode
title: The local lattice count, split by the type of the model
kind: theorem
decl: Formalism.L2.SG.LsDatumA.globalCount_of_split_mode
module: Formalism.LocalToGlobal.SiegelLatticeTheory.CokernelGLCounts.RankPointCounts.GlobalCountOfSplitMode
covers: 503
status: drafted
drafted_by: writer@claude
---
This theorem reduces the local lattice count `T2 D` to two statements about split local models. It proves the non-split case and takes the split case as hypotheses. Its only user is [the local count of partner lattices](/entry/integral-closure-rank-and-residue-trdeg-le/), which supplies the hypotheses and states `T2 D` in full. We use its names.

## Statement

For a local model $M$, ranks $r, n$ and a truth value $b$, let $\mathrm{ModSide}_0(M, r, n, b)$ say: if "$M$ is split" has the value $b$, and $D_\ell = 0$, then the set $\Theta$ of lattice module isomorphisms has $n_{\mathrm{Iso}}(Z_1, Z_2)$ elements. Let $\mathrm{ModSide}_U(M, r, n, b)$ say the same when $D_\ell$ is a unit, with $n_{\mathrm{Iso}}^{BA}$.

**Theorem.** Let $D$ be a datum. Assume $\mathrm{ModSide}_0(M, r, n, \text{true})$ and $\mathrm{ModSide}_U(M, r, n, \text{true})$ for every local model $M$ with $M.\mathrm{OK}$ and all $r, n$. Then `T2 D` holds.

For a model that is not split, the hypotheses say nothing.

## Proof

Split on the type of $M$. If $M$ is not split, the module sides are `modSide0L` and `modSideUL` (that is, `localCountZeroLocal_holds` and `localCountUnitLocal_holds`). If $M$ is split, they are the hypotheses. Then `globalCount_of_module` turns the module sides into `T2 D`, through `localCount_of_module`, which we did not open. The rest is bookkeeping.

## In the Lean code

The theorem is in [GlobalCountOfSplitMode.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/GlobalCountOfSplitMode.lean#L24). `ModSide0` and `ModSideU` are in [LsDatumACut.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/LsDatumACut.lean#L86), and `globalCount_of_module` in [GlobalCountOfModule.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/GlobalCountOfModule.lean#L142).

The name says "global", but every statement here is local. As in the parent, the suffix G means "split" and L means "not split". The hypotheses ask for all $r, n$, but only $r_S$ and $n$ of $D$ are used.
