---
id: cut-at-of-deep
title: The local cut from three deep inputs
kind: theorem
decl: Formalism.L2.SG.Pf.Coef.cutAt_of_deep
module: Formalism.LocalToGlobal.SiegelLatticeTheory.CokernelGLCounts.RankPointCounts.CoefCutDeep
covers: 2409
status: drafted
drafted_by: writer@claude
---
This theorem proves the local cut `CutAt` for one choice of local data, words and rows. Of the twelve inputs of `cutAt_of_leaves`, it proves nine outright and keeps three as hypotheses: local index ratios, a global approximation and a patching of lattices. Its only user is [the row datum from the deep inputs](/entry/rows-datum-p-of-deep/). The largest part of its subtree is [the partner count](/entry/partner-count-holds-all/).

## Statement

Let $D$ be a datum of the unitary setting, with CM field $E$ over the totally real field $F$. For each finite place $p$ of $F$, let $M_p$ be a local model and $\delta_p$ an element of $F_p$. Let $u, u'$ be words, $F_0$ a flag and $\mathcal{W}$ a finite set of $\mathcal{O}_E$-lattices in the hermitian space $V$ of $D$. Suppose:

1. the signature condition holds for $V$;
2. $(\delta, M)$ agrees with $D$ at every $p$ (`Agree`: the model satisfies its condition `OK`, $\delta_p \neq 0$, and the conjugation, the ring of integers, the character and the split data match those of $D$ at $p$);
3. $T_u \equiv T_{u'} \pmod{g_S^2}$, and the prime hypothesis `PrimeHyp` holds;
4. $\mathcal{W}$ is a set of row representatives for $F_0$;
5. `StepsU`: for each term and each $p$, a local index ratio has the value given by a weight, and a unimodularity condition holds;
6. `StabApprox`: if local lower and upper triangular integral matrices move a matrix at every $p$, then there are global ones that do the same and are integral at all $p$;
7. `FStarC`: for an eligible term $\gamma$ and a point $w'$ of the same kind, the partner set of $\gamma$ is in bijection with a set of global lattices that match prescribed local lattices at almost all $p$.

**Theorem.** Then `CutAt` holds. It is a conjunction of eight parts: the local orbit sums have the stated totals; the scalar kind condition; the coefficient of each term is a finite product of local factors times a number of orbits; the partner count and the fiber count, each a convergent sum equal to a product of local factors; eligibility of normal representatives; a condition `ThSome` on the local classes, which we did not unfold; and a family of local classes $\theta_0$ such that, off a finite set of places, the local orbit functions are the indicator functions of the base point and of $\theta_{0,p}$, and the classes are restricted.

We did not unfold the local factors in these sums.

## Proof

The proof builds the twelve inputs of `cutAt_of_leaves` and applies it.

- The normal representatives exist (`PCount.normRepExists_ctx`) and move correctly (`norm_representative_move`). The second uses the signature condition.
- The local phases come from `local_phase_typed_places`.
- The volume index product comes from `StepsU` through `ProdE.prodE_CZ_of_approxC` and `ZsVolAsm.volIdxProd_of_prodE`.
- `StabApprox` gives the representatives at tuples (`TupFinal.repAtTup_of_stab`). With `FibQ.tupFun_holds`, `TupOrb.orbZT_holds` and the finiteness `ZsVolFin.finR`, this gives the fraction sums (`FibPart.sumFr_of`) and the fiber sums (`FibPart.fibSum_of`).
- `FStarC` gives the global frames (`frGlob_of_fstar`).
- The existence of partners, the integrality, the reduction at $\tau = 1$ and the density statement are proved outright: `PCountEx.exist_holds`, `PCount.intGenP_holds`, `PCount.tau_one_holds` and `densTh_of_ga`.
- The partner isomorphism count is [`partnerCount_holds_all`](/entry/partner-count-holds-all/).

## In the Lean code

The theorem is in [CoefCutDeep.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/CoefCutDeep.lean#L35). `cutAt_of_leaves` is in [CoefCutAt.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/CoefCutAt.lean#L24) and `CutAt` in [LsDatumBCut.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/LsDatumBCut.lean#L135).

Each of the signature condition, `StepsU`, `StabApprox` and `FStarC` has exactly one use, as above. The local space `L` appears only in the conclusion.

The three hypotheses are not real conditions: [the deep inputs, outright](/entry/cut-leaves-deep-outright/) proves them for every datum.
