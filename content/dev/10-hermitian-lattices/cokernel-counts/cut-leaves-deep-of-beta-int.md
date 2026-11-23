---
id: cut-leaves-deep-of-beta-int
title: The deep inputs of the local cut from an integral isometry
kind: theorem
decl: Formalism.L2.SG.Pf.FrameGlobalPatching.FStar.cutLeavesDeep_of_betaInt
module: Formalism.LocalToGlobal.SiegelLatticeTheory.CokernelGLCounts.RankPointCounts.FStarCut
covers: 870
status: drafted
drafted_by: writer@claude
---
This theorem proves $\mathrm{CutLeavesDeep}(D)$ from one hypothesis, `BetaInt`. Two of its three parts are proved outright. The third, `FStarC`, comes from [the patching statement from the integral isometry](/entry/f-star-c-of-int/). Its only user is [the deep inputs hold outright](/entry/cut-leaves-deep-outright/), which supplies `BetaInt` by `betaInt_holds` and states $\mathrm{CutLeavesDeep}(D)$.

## Statement

Let $D$ be a datum. Assume `BetaInt` for all local data $(\delta, M)$ that agree with $D$, all words $u, u'$, every flag $F_0$ and every finite set $\mathcal{W}$ of lattices.

`BetaInt` says: let $\gamma$ be a term, $F_2'$ a flag and $\Lambda_2$ a global lattice in the context `BHyp`. In particular $\Lambda_2$ has the prescribed local components, and a unipotent element that fixes $F_0$ maps $\Lambda_2$ onto the lattice $\Lambda_\gamma$ of $\gamma$. Let $\beta_0$ be an isometry of $V$ that sends the frame of the representative flag of $\gamma$ to the frame of $F_2'$ and satisfies `W0₂` and `OmB`. Then there is an isometry $v$ of $V$ that fixes the frame of $F_2'$, satisfies $v y - y \in X$ for each $y \perp X$ (with $X$ the subspace `Xsp` of $F_2'$), maps $\Lambda_\gamma$ onto $\Lambda_2$ after $\beta_0$, and satisfies a condition `IotaC₂` that we did not unfold.

**Theorem.** Then $\mathrm{CutLeavesDeep}(D)$ holds.

## Proof

1. `StepsU` comes from `CountAt.countAt_holds` and `ProdEP2Uni.unimodAt_holds`.
2. `StabApprox` comes from `TupGlobApprox.stabApprox`.
3. The congruence, the row representatives and the prime hypothesis form the context `CtxP`. With `BetaInt`, `fStarC_of_int` gives `FStarC`.

The rest is bookkeeping.

## In the Lean code

The theorem is in [FStarCut.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FStarCut.lean#L16). `BetaInt` and `BHyp` are in [FStarBwdBetaK.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FStarBwdBetaK.lean#L59).

The signature condition and the local space are not used, as the parent entry notes. The hypothesis asks for `BetaInt` for every $F_0$ and $\mathcal{W}$, but the proof uses it only for the given ones. Since `betaInt_holds` needs no hypothesis, this does not matter.
