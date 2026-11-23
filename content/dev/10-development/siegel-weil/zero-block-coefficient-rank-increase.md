---
id: zero-block-coefficient-rank-increase
title: The mass formula for isotropic frames, from rank n to rank n+1
kind: theorem
decl: GlobalTheory.T.zero_block_coefficient_rank_increase
module: Development.WeilBound.RepresentationTheoryGL.SiegelWeil.ArchimedeanSiegelWeil.PlaceIntegrals.ZeroBlockCoefficientRankIncreaseStatement
covers: 560
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`hyp_step`](/entry/hyp-step/). It is the inductive step for the zero Gram matrix in [`swFree_singular`](/entry/sw-free-singular/), which proves the Euler product property of the theta measure for each singular Gram matrix. All the content is in [`hyp_step`](/entry/hyp-step/).

## Statement

Let $E/F$ be a CM extension with conjugation $\sigma$. Let $J$ be an invertible Hermitian $M \times M$ matrix over $E$, and let $H \oplus J$ be the $(M+2) \times (M+2)$ matrix $\begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & J \end{pmatrix}$ (`hypOne J`). For a Hermitian matrix $T$, let $\mathrm{SWFree}(J, T)$ say that the theta measure on the frames with Gram matrix $T$ is the Euler product of the local fibre measures at $T$, with constant $1$. [`hyp_step`](/entry/hyp-step/) states this property in full.

**Theorem.** Let $1 \le n$ and $2n < M$. If there is an isotropic $n$-frame for $J$ and $\mathrm{SWFree}(J, 0_n)$ holds, then $\mathrm{SWFree}(H \oplus J, 0_{n+1})$ holds.

## Proof

The proof is `first | exact @hyp_step | exact hyp_step`. The statement is the same as that of `hyp_step`, word for word.

## In the Lean code

The theorem is in [ZeroBlockCoefficientRankIncreaseStatement.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeil/ArchimedeanSiegelWeil/PlaceIntegrals/ZeroBlockCoefficientRankIncreaseStatement.lean#L7). `swFree_singular` calls it at [L492](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeil/ArchimedeanSiegelWeil/PlaceIntegrals/SiegelWeilFreeOfBlockNonemptyFrames.lean#L492), after it moves the first vector of an isotropic frame to the first basis vector of a hyperbolic plane. The two hypotheses `h₀` and `h₁` say that the zero matrix is Hermitian. They always hold, and the code needs them only as arguments of `hermOf`. The name speaks of a "zero block coefficient", but the statement is about Euler products of measures on isotropic frames, not about Fourier coefficients.
