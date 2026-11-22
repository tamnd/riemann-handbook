---
id: integral-closure-rank-and-residue-trdeg-le
title: The local count of partner lattices
kind: theorem
decl: Formalism.L2.SG.LsDatumA.integralClosureRank_and_residueTrdegLe
module: Formalism.LocalToGlobal.SiegelLatticeTheory.CokernelGLCounts.RankPointCounts.IntegralClosureRankAndResidueTrdegLe
covers: 1293
status: drafted
drafted_by: writer@claude
---
This theorem counts local lattices. For every local model that satisfies its condition `OK`, it gives the number of lattices that complete a generic local term to a partner term. Its name speaks of an integral closure and a residue transcendence degree, but its statement has neither. Its only user is [the local partner count](/entry/partner-count-holds-all/).

## Statement

Let $D$ be a datum of the unitary setting, with ranks $r = r_S$ and $n$ (the Lean fields `D.R.rS` and `D.R.r`).

**Theorem.** `T2 D` holds.

`T2 D` says: for every field $F$ with a valuation and a topology, every $F$-algebra $E$ and every local model $M$ over $(F, E)$ that satisfies its condition `OK`, `FamilyLocalModel M r n` holds. This means: let $V$ be an $E$-module of rank $n$ with a hermitian structure $H$ over $M$. Let $t_1$ be a generic term, with lattice, frames $f, f'$ and invariants $T, T'$. Let $f_2, f_2'$ be frames and let $\varphi \colon W(f) \to W(f_2)$ and $\varphi' \colon W(f') \to W(f_2')$ be $E$-linear isomorphisms of the modules that the frames define (the Lean `Wb`, which we did not unfold), such that:

- $f_2$ and $f_2'$ satisfy the frame condition `FrameK` for $T$ and $T'$;
- $\varphi, \varphi'$ satisfy the identity condition `Ident`;
- $\varphi$ sends the last vector of $f$ to the last vector of $f_2$, and $\varphi'$ does the same for $f'$ and $f_2'$.

Let $S$ be the set of $\mathcal{O}$-lattices $\Lambda_2$ in $V$ such that $(\Lambda_2, f_2, f_2', T, T')$ is generic and respects $t_1$ under $\varphi, \varphi'$. Let $P_1 = Z^+(t_1)$ and let $P_2$ be the matrix of the frame pair $(f_2, f_2')$. Then:

1. if the invariant $D_\ell(f, f', r)$ is $0$, then $|S| = n_{\mathrm{Iso}}(Z_1, Z_2)$ for the integral matrices $Z_1, Z_2$ with entries $P_1, P_2$;
2. if $D_\ell(f, f', r)$ is a unit, then $|S| = n_{\mathrm{Iso}}^{BA}(Y_1, Y_2, \beta_1, \beta_2, \alpha_1, \alpha_2)$, where $Y_i$ is the upper left $r \times r$ block of $P_i$, $\beta_i$ is its last column and $\alpha_i$ its last row.

We did not unfold $D_\ell$, $n_{\mathrm{Iso}}$ or $n_{\mathrm{Iso}}^{BA}$. The statement depends on $D$ only through $r$ and $n$.

## Proof

The proof is `globalCount_of_split_mode D modSide0G modSideUG`, in two steps.

1. A model is split or not split. In the non-split case the module sides are proved outright (`modSide0L`, `modSideUL`). In the split case they come from `modSide0G` and `modSideUG`, which are `localCountZeroGlobal_holds` and `localCountUnitGlobal_holds`. A module side says that the set $\Theta$ of $\mathcal{O}$-isomorphisms between the two lattice modules, with a unit invariant and compatible with the given graphs, has $n_{\mathrm{Iso}}$ or $n_{\mathrm{Iso}}^{BA}$ elements.
2. `globalCount_of_module` and `localCount_of_glue` prove $|S| = |\Theta|$ (`latSide_at'`). The inputs are `glueEta_holds`, `glueConv_holds`, `genOfPrim_holds` and `claimR_at`. With step 1 this gives both cases.

## In the Lean code

The theorem is in [IntegralClosureRankAndResidueTrdegLe.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/IntegralClosureRankAndResidueTrdegLe.lean#L11). `T2` is in [ThinScalesBound.lean](lean:Formalism/SharpRestriction/CuspSpanNormBounds/ThinScalesBound.lean#L199) and `FamilyLocalModel` at line 152 of that file. The module sides and $\Theta$ are in [LsDatumACut.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/LsDatumACut.lean#L55). The split is in [GlobalCountOfSplitMode.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/GlobalCountOfSplitMode.lean#L24).

Odd points:

- The name does not match the statement. A file with the same name, [IntegralClosureRankAndResidueTrdegLe.lean](lean:ReciprocityTheory/SemistableReduction/IntegralClosureRankAndResidueTrdegLe.lean#L6), proves a real result on the rank of an integral closure over a discrete valuation ring. This theorem may have taken its name from that file.
- `T2` is defined three times with the same text: also in [ChainLength.lean](lean:Formalism/SharpRestriction/CuspSpanNormBounds/ChainLength.lean#L195) and [LocalBesselAndTopKernel.lean](lean:Formalism/SharpRestriction/CuspSpanNormBounds/LocalBesselAndTopKernel.lean#L162).
- In `modSide0G` and `localCountZeroGlobal_holds`, "global" means the split case and "local" the non-split case.
