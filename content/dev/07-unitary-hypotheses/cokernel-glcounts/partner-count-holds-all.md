---
id: partner-count-holds-all
title: The local partner count holds for all local data
kind: theorem
decl: Formalism.L2.SG.Pf.PCount.partnerCount_holds_all
module: Formalism.LocalToGlobal.SiegelLatticeTheory.CokernelGLCounts.RankPointCounts.PartnerCountHoldsAll
covers: 1416
status: drafted
drafted_by: writer@claude
---
This theorem proves the partner isomorphism count for all local data. It is a one-line relay to `partnerCount_of_iso`. The real content is in [the local lattice count](/entry/integral-closure-rank-and-residue-trdeg-le/), which gives most of its subtree. Its only user is [the local cut from the deep inputs](/entry/cut-at-of-deep/).

## Statement

Let $D$ be a datum of the unitary setting and let $Z = (\delta, M)$ be local data that agree with $D$ at every finite place (the Lean structure `LocDat`).

**Theorem.** `PartnerIsomorphismCount Z` holds.

This says the following. Fix a finite place $p$, $T, T' \in \mathbb{N}$, points $w, w'$ of the same kind, a local term $t_1$ with invariants $T, T'$, a frame $f_2'$, and isomorphisms $\varphi, \varphi'$ that satisfy the local count hypotheses with first frame $f_2 = t_1.f$. Suppose that the matrix $Z^+(t_1)$ is $u_L \, Y_w \, u_U$ with $u_L$ lower and $u_U$ upper unitriangular, where $Y_w$ is a matrix `modMat` built from $\delta, T, T', p, w$ (we did not unfold it), that the matrix of the new frame pair has the same form at $w'$, and that this second matrix is integral. Then the number of $\mathcal{O}$-lattices $\Lambda_2$ in $V_p$ such that the term $(\Lambda_2, t_1.f, f_2', T, T')$ is generic and respects $t_1$ under $\varphi, \varphi'$ equals $n_{\mathrm{Iso}}(c, c')$, where $c$ and $c'$ are the classes of the two matrices shifted by a corner term. We did not unfold $n_{\mathrm{Iso}}$ or the corner term.

## Proof

Apply `partnerCount_of_iso` to three inputs:

- the local lattice count `T2 D`, from [`integralClosureRank_and_residueTrdegLe`](/entry/integral-closure-rank-and-residue-trdeg-le/);
- the integrality of $Z^+$ at generic terms, `intGenP_holds`;
- the bridge isomorphism, `BI.integralIsomorphism_holds`.

`partnerCount_of_iso` is also one line. It calls `partnerCount_of_integral`, which we did not open.

## In the Lean code

The theorem is in [PartnerCountHoldsAll.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/PartnerCountHoldsAll.lean#L8). `PartnerIsomorphismCount` is in [PartnerCount.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/PartnerCount.lean#L734) and `partnerCount_of_iso` in [PartnerCountOfIso.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/PartnerCountOfIso.lean#L81).

The name of the first input does not match its statement, a count of local lattices.
