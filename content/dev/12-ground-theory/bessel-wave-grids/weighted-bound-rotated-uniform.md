---
id: weighted-bound-rotated-uniform
title: The weighted bound on rotated points, uniform in the data
kind: theorem
decl: CompanionTheory.WaveGrid.weighted_bound_rotated_uniform
module: CompanionTheory.AutomorphicTheory.BesselWaveGrids.ThmBFinal
covers: 1222
status: drafted
drafted_by: writer@claude
---
This theorem bounds a weighted sum, over global points, of products of local orbital integrals of discrete series coefficients, uniformly in the global datum. It has no hypotheses. The code calls it a form of Theorem B. Its result goes to `analytic_pinnedTheoremB_uniform` and `bDat_theoremB_global`, which lie below the last node of the trunk, [HypsAlt is nonempty from the closed bound](/step/nonempty-hyps/). Below this theorem are 1,222 declarations.

## Statement

A global datum $D$ (the structure `D7`) gives, among other data, two ranks $k$ and $r$, with $n = 2r + k + 1$; a CM field $E$; a finite set $\mathcal{T}$ with a ring embedding $\iota_v \colon E \to \mathbb{C}$ for each $v \in \mathcal{T}$; and a Harish-Chandra parameter $\lambda_v^0 \in \mathbb{R}^n$ for each $v$.

A *point* $\gamma$ of size $r+1$ is a list of blocks $(t_i, s_i)$ with $t_i \in E^\times$, $s_i \geq 1$ and $\sum s_i = r + 1$. Its matrix is block diagonal, and the block $i$ is $t_i$ times the antidiagonal matrix of ones of size $s_i$. Let $\Delta_l$ be the leading $l \times l$ minor of this matrix. For natural numbers $T, T'$ put $G(\gamma) = \Delta_{r+1}\bar\Delta_{r+1} - TT'\Delta_r\bar\Delta_r$. The point is *admissible* if $G(\gamma)$ is a nonzero algebraic integer and $L\gamma U$ is integral for some lower and some upper unitriangular $L, U$ over $E$. Its norm weight is $N(\gamma) = \prod_v |\iota_v G(\gamma)| \cdot \prod_l \prod_v |\iota_v \Delta_l|^2$, with $l$ over the ends of the blocks.

A *Bessel datum* $X$ (the structure `BData` with distance $0$) gives, at each $v$, a local datum $L_v$: a discrete series $\sigma_v$ of a unitary group in $n$ variables with parameter $\lambda_v = \lambda_v^0$, two finite-dimensional representations, and a Bessel function. It also gives a $K$-finite matrix coefficient $f_v$ of $\sigma_v$ and a section $\mu_v$. The data meet size conditions in a real number $b$ and constants $C_h, C_g$. The local point $\gamma_v$ has the blocks $(\rho_i\,\iota_v(t_i), s_i)$, with $\rho_i$ a power of `Host.rdE` (not unfolded). The rotated point $\tilde\gamma_v$ has the entries $(-1)^r(-i)^{a+b}(\gamma_v)_{ab}$. Let $O_v(\gamma)$ be the supremum of the squared Hilbert-Schmidt norms of the orbital integrals of $f_v$ at $\tilde\gamma_v$. Let $J_v$ be a weighted $L^2$ norm of the Bessel function of $f_v$ on the big cell.

**Theorem.** For all $A_w \geq 0$ and $C_h$ there are $C_b$ and $C_{g,0}$ such that the following holds for all $C_g \geq C_{g,0}$, all $D$ and all $X$. Suppose that $|\lambda_v(s) - \lambda_v(s')| \geq C_g(2r+2)^4$ for all $v$ and $s \neq s'$. Then

$$\sum_{\gamma \text{ admissible}} w(\gamma)\,\omega(\gamma)\,N(\gamma)^{A_w(r+1)^2} \prod_{v} O_v(\gamma) \;\leq\; b^{\,C_b (2r+2)^5 |\mathcal{T}|} \prod_{v} J_v.$$

Here $w(\gamma) = \prod_l \prod_v (1 + |\iota_v \Delta_l|^2)^2$ and $\omega(\gamma)$ is a second weight from the local blocks, which we have not unfolded.

## Proof

1. `zuckerman_gap` proves `ZuckG`, a statement on tensor products of a family of discrete series with finite-dimensional representations.
2. `hypsG_of_zuck` adds six proved facts and gives `HypsG`.
3. [The bound from HypsG](/entry/weighted-bound-rotated-uniform-of-hyps-g/) gives the theorem.

The proof only connects these.

## In the Lean code

The theorem is in [ThmBFinal.lean](lean:CompanionTheory/AutomorphicTheory/BesselWaveGrids/ThmBFinal.lean#L7). The statement is the proposition `WeightedBoundRotatedUniform` of [WeightedUniformRotatedOfExpansion.lean](lean:Formalism/SharpRestriction/CuspSpanNormBounds/WeightedUniformRotatedOfExpansion.lean#L156), built from `theoremBRotated` and `BSumR` in the same file and from `normWt`, `BData` and `jSqG` in [LeadMinorK.lean](lean:Formalism/SharpRestriction/CuspSpanNormBounds/LeadMinorK.lean#L164). The right side is written as $\exp(C_b (2r+2)^5 |\mathcal{T}| \log b)$. We have not unfolded `IsDSHpk`, `orbSq` beyond its supremum, or `jNormSq`.

It calls `Zuck.zuckerman_gap` in [ZuckermanGapSmall.lean](lean:CompanionTheory/AutomorphicTheory/ZuckermanCommutation/ZuckermanFunctors/ZuckermanGapSmall.lean#L9) and `PieriExpansion.hypsG_of_zuck` in [InfinitesimalCharacterDiscreteSeries.lean](lean:CompanionTheory/AutomorphicTheory/PieriRules/InfinitesimalCharacterDiscreteSeries.lean#L51).

The caller `ThmBChain.theoremB_uniform_rotated` turns the result into `JointNormBoundRotatedUniform` with the proof `exact h`. That proposition, in [ThmBUseR.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmBUseR.lean#L38), is a word-for-word copy of `WeightedBoundRotatedUniform`.
