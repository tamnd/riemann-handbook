---
id: f-star-c-of-beta
title: The patching statement from the two isometries
kind: theorem
decl: Formalism.L2.SG.Pf.FrameGlobalPatching.FStar.fStarC_of_beta
module: Formalism.LocalToGlobal.SiegelLatticeTheory.CokernelGLCounts.RankPointCounts.FStarLprClose
covers: 485
status: drafted
drafted_by: writer@claude
---
This theorem proves the patching statement `FStarC` from the context `CtxP` and the two isometry statements `BetaRat` and `BetaInt`. It proves the local input `LprPart` outright and passes everything to [the patching statement from its leaves](/entry/f-star-c-of-leaves-prime/). Its only user is [the patching statement from the integral isometry](/entry/f-star-c-of-int/), which states `FStarC`, `CtxP` and `BetaRat`.

## Statement

Let $D$ be a datum, $Z_d = (\delta, M)$ local data that agree with $D$, $u, u'$ words, $F_0$ a flag and $\mathcal{W}$ a finite set of lattices.

**Theorem.** If `CtxP`, `BetaRat` and `BetaInt` hold, then `FStarC` holds.

## Proof

Apply `fStarC_of_leaves'` to `CtxP`, `lprPart_holds`, `BetaRat` and `BetaInt`.

`LprPart` is a local statement. For a partner flag $F'$ of $\gamma$ and a place $p$, a local isomorphism $\psi$ from the second frame of $\gamma$ to $F'$ that satisfies `Ident` maps the local lattice set of $\gamma$ onto that of $(\Lambda_{\gamma,p}, F')$. If $M_p$ is split, it also maps the graph `iotaGraph`. `lprPart_holds` is `lprPart_of_iota` applied to `iotaStep_holds`. We did not open `lprPart_of_iota`.

## In the Lean code

The theorem is in [FStarLprClose.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FStarLprClose.lean#L22), with `lprPart_holds` at line 19. `LprPart` is in [FStarLocInB.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FStarLocInB.lean#L194) and `lprPart_of_iota` in [FStarLprExist.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FStarLprExist.lean#L73).

The proof is one line that removes a hypothesis. This theorem and its parent together prove `FStarC` from `CtxP` and `BetaInt` alone; the two steps could be one.
