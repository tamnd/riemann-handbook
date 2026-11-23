---
id: f-star-c-of-int
title: The patching statement from the integral isometry
kind: theorem
decl: Formalism.L2.SG.Pf.FrameGlobalPatching.FStar.fStarC_of_int
module: Formalism.LocalToGlobal.SiegelLatticeTheory.CokernelGLCounts.RankPointCounts.FrGlobPOfInt
covers: 558
status: drafted
drafted_by: writer@claude
---
This theorem proves the patching statement `FStarC` from the context `CtxP` and the hypothesis `BetaInt`. It proves the rational half, `BetaRat`, outright and passes the rest to [the patching statement from the two isometries](/entry/f-star-c-of-beta/). Its only user is [the deep inputs from an integral isometry](/entry/cut-leaves-deep-of-beta-int/), which also states `BetaInt`.

## Statement

Let $D$ be a datum, $Z_d = (\delta, M)$ local data that agree with $D$, $u, u'$ words, $F_0$ a flag and $\mathcal{W}$ a finite set of lattices. `CtxP` says $T_u \equiv T_{u'} \pmod{g_S^2}$, $\mathcal{W}$ is a set of row representatives for $F_0$, and the prime hypothesis holds.

**Theorem.** If `CtxP` and `BetaInt` hold, then `FStarC` holds.

`FStarC` says that the partner classes of a term are in bijection with the global lattices that have prescribed local components, for a suitable choice of flag and local isomorphisms.

## Proof

Apply `fStarC_of_beta` to `CtxP`, `betaRat_holds` and `BetaInt`.

`BetaRat` is the rational form of `BetaInt`: in the context `BHyp`, there is an isometry $\beta_0$ of $V$ that sends the frame of the flag of $\gamma$ to the frame of $F_2'$ and satisfies `W0₂` and `OmB`. `betaRat_holds` proves it outright. Its proof extends a map of frames to an isometry of $V$ (`BRat.isometry_extension_two`), which we did not open.

## In the Lean code

The theorem is in [FrGlobPOfInt.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FrGlobPOfInt.lean#L18). `BetaRat` is in [FStarBwdBetaK.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FStarBwdBetaK.lean#L41), and `betaRat_holds` in [FStarBetaRat.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FStarBetaRat.lean#L27).

The file name says "FrGlobP", but the theorem proves `FStarC`, not `FrGlobP`. `FrGlobP` is a different statement in [PartnerCountP.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/PartnerCountP.lean#L23).
