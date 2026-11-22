---
id: model-st-of-small-frame-gal
title: Hida settings that cover the blocks, from frames and Galois data
kind: theorem
decl: GlobalTheory.ExpModel.modelSt_of_small_frame_gal
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ModelStOfFrames
covers: 1467
status: drafted
drafted_by: writer@claude
---
This theorem proves the model statement: at each good twisted place $w$, Hida settings cover the block subspace at $w$. [`model_statement_of_crystalline_chebotarev_frame_gal`](/entry/model-statement-of-crystalline-chebotarev-frame-gal/) is a copy. It feeds [the exponent bound](/entry/exponent-bound-of-unitary-theta-standard-theorems-alt/). Below this theorem are 1,467 declarations.

## Statement

Each statement below says that the given predicate holds for small $\varepsilon$, large families, eventually at points $p$ with `More p`, for each $j$, each $(P, W)$ with `Dict` and `NumOk`, and each twisted place $w$ with $W$ in range at the residue characteristic $\ell$ of $w$.

- `SmallnessCondition`: $\ell$ is prime, $N_r + 1 < \ell$ ($N_r$ the rank of $P$), $\ell \nmid \operatorname{disc} E$, and the block subspace $Z$ at $w$ is stable under the block operators and lies in their space.
- `FrameStatement'`: there are a good $\ell$-adic frame $F$, a reading $R$ of the block by $F$, embeddings $\iota \colon E \to \overline{\mathbb{Q}}_\ell$ and a tie $T$.
- `GaloisStatement`: for each such $F, R, \iota, T$, `GalSide` holds. It gives, for each eigensystem $\theta$ of $F$, a crystalline representation $G_E \to \mathrm{GL}_{N_r}(\overline{\mathbb{Q}}_\ell)$ with Frobenius polynomials read off $\theta$. In the block, the polynomial is that of a representation of dimension $N_r - t$ times $t$ linear factors from crystalline characters.
- `ModelStatement` (conclusion): there are maps $fr, cj$ and Hida settings $X_i$, $i \in I$, that cover $Z$ at $w$, with $\ell$ not a unit in the coefficient ring of each $X_i$ and `WInputsLink` for each $X_i$. Cover means: if all $X_i$ satisfy the inclusion at level $J$, then $\ell^J$ times the cut lattice of $Z$ lies in a second lattice, localized at $w$.

**Theorem.** `BhattScholzeCrystallineLattices`, `ChebotarevDegreeOne` and the first three statements imply `ModelStatement`.

`ChebotarevDegreeOne` says: for a finite Galois extension $L/F$ of number fields, each $g \in \mathrm{Gal}(L/F)$ and each finite set $S$ of places, there is a place $v \notin S$ of degree 1, unramified in $L$, with Frobenius $g$. This follows from Chebotarev's density theorem (Neukirch, *Algebraic Number Theory*, Chapter VII, §13). `BhattScholzeCrystallineLattices` says: for $K/\mathbb{Q}_\ell$ finite, each crystalline $\mathbb{Z}_\ell$-lattice of $G_K$ comes from an $F$-crystal over $\mathcal{O}_K$, and maps lift uniquely. This has the shape of a result of Bhatt and Scholze (*Prismatic F-crystals and crystalline Galois representations*, Camb. J. Math. 11, 2023). We have not checked the Lean objects against it.

## Proof

Smallness gives that $\ell$ is prime, and with `NumOk` that $\ell \ne 2$. The frame statement gives $F, R, \iota, T$, and the Galois statement `GalSide`.

1. `crystallineLatticeLink_of_blockData` gives $fr, cj$ and a lattice link from the Bhatt-Scholze hypothesis, $\ell \ne 2$ and $\ell \nmid \operatorname{disc} E$.
2. `levelMap_exists` and `HeckeMod.hecke_module` give a level map and a Hecke module.
3. $I$ is the set of maximal ideals $\mathfrak m$ of the Hecke algebra of $F$ such that some $\theta$ that occurs in $Z$ lies over $\mathfrak m$. $X_{\mathfrak m}$ is the setting of $F$ at $\mathfrak m$. `maximalIdeals_meeting_subspace_cover` proves the cover.
4. For each $\mathfrak m$, `frameCoeffRing_prime_not_isUnit` shows that $\ell$ is not a unit, and `hasBlocks_of_system_occurs_in_block_part` puts $\theta$ in the block. Then `winputs_frame` gives `WInputsLink` from the Chebotarev hypothesis, `GalSide` and the lattice link.

## In the Lean code

The theorem is in [ModelStOfFrames.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ModelStOfFrames.lean#L30). The statements are in [SmallnessCondition.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SmallnessCondition.lean#L29) and [ModelStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ModelStatement.lean#L26). `SmallAt`, `FrameAt`, `GalAt` are in [LiftFrameEmbeddingBase.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/LiftFrameEmbeddingBase.lean#L373), `ModelAt` in [SumExpSt.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/SumExpSt.lean#L77), `GalSide` is in [HasBlockOfOccurs.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/HasBlockOfOccurs.lean#L244). We have not unfolded `Frame`, `Reads`, `Tied`, `HidaSetting` or `WInputsLink`.

The proof is line for line that of `modelSt_of_frames` in [ModelStatementOfFrameGalois.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ModelStatementOfFrameGalois.lean#L117). Only the wrapper differs (`AtPtsAlt` here, `AtPts` there).
