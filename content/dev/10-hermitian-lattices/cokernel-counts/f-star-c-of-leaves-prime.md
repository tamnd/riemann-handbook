---
id: f-star-c-of-leaves-prime
title: The patching statement from its four parts
kind: theorem
decl: Formalism.L2.SG.Pf.FrameGlobalPatching.FStar.fStarC_of_leaves'
module: Formalism.LocalToGlobal.SiegelLatticeTheory.CokernelGLCounts.RankPointCounts.FStarBwdBetaF
covers: 324
status: drafted
drafted_by: writer@claude
---
This theorem proves the patching statement `FStarC`: a bijection between the partner classes of a term and the global lattices with prescribed local components. It takes the context `CtxP`, the local input `LprPart` and the two isometry statements `BetaRat` and `BetaInt` as hypotheses. Its only user is [the patching statement from the two isometries](/entry/f-star-c-of-beta/), which supplies `LprPart`; that entry and [its parent](/entry/f-star-c-of-int/) state the hypotheses.

## Statement

Let $D$ be a datum, $Z_d = (\delta, M)$ local data that agree with $D$, $u, u'$ words, $F_0$ a flag and $\mathcal{W}$ a finite set of lattices.

**Theorem.** If `CtxP`, `LprPart`, `BetaRat` and `BetaInt` hold, then `FStarC` holds.

## Proof

Fix a term $\gamma$ and a matrix $Z$ in the context `Ctx`. A partner of $(\gamma, Z)$ is a flag $F'$ in the set $E_Z$ that represents the class of a term $\gamma'$ with the same scalar as $\gamma$. Its class $\mathrm{cls}(F')$ is the set of flags in $E_Z$ that some element of the group $N_0(F_0, \Lambda_\gamma)$ sends $F'$ to (`NilradicalFlagMoved`). For a flag $F_2'$ and a lattice $\Lambda_2$, write $F' \sim \Lambda_2$ if some unipotent $n$ that fixes $F_0$ moves $F_2'$ to $F'$ and maps $\Lambda_2$ onto $\Lambda_\gamma$.

`fStarC_of_route2` proves `FStarC` from four statements:

1. **Existence** (`starExists2_holds`, from `CtxP`): there are a flag $F_2'$ and local isomorphisms for which the local hypotheses of `FStarC` hold.
2. **Forward** (`fwdC_of_loc`): each partner $F'$ has a global lattice $\Lambda_2$ with the prescribed local components and $F' \sim \Lambda_2$. It uses the row representatives and `LprPart`.
3. **Backward** (`bwdC_of'''`): each such $\Lambda_2$ has a partner $F'$ with $F' \sim \Lambda_2$. It uses `CtxP`, `bwdN_holds`, `bwdTerm'_holds` and `bwdBeta'_of_leaves`. The last is where `BetaRat` and `BetaInt` enter: with `scalarOf_holds` they give `BetaCore`, and with `repG_holds` they give an isometry $\beta$ that satisfies the pair condition `IsPair` for $\Lambda_\gamma$, $F_0$ and the moved flag.
4. **Uniqueness** (`Uniq.uniqC_holds`): if $F' \sim \Lambda_2$ and $F'' \sim \Lambda_3$, then $\Lambda_2 = \Lambda_3$ if and only if $\mathrm{cls}(F') = \mathrm{cls}(F'')$.

The general lemma `equiv_of_corr` turns a relation with the last three properties into a bijection between the set of classes and the set of lattices. `frPart_eq` identifies the set of classes with the partner set of `FStarC`.

## In the Lean code

The theorem is in [FStarBwdBetaF.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FStarBwdBetaF.lean#L27), with `bwdBeta'_of_leaves` at line 23. `fStarC_of_route2`, `equiv_of_corr`, `StarExists2`, `FwdC`, `BwdC` and `UniqC` are in [UnipotentFrameFixers.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/UnipotentFrameFixers.lean#L124). `uniqC_holds` is in [FStarUniq.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FStarUniq.lean#L370).

The proof is one term. We did not open the proofs of the four parts. The uniqueness part `uniqC_holds` takes no context hypothesis. The prime in the name has no unprimed partner: there is no `fStarC_of_leaves` in the code.
