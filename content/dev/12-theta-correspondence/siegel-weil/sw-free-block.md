---
id: sw-free-block
title: The theta measure of a block matrix is an Euler product
kind: theorem
decl: GlobalTheory.CompanionTheory.WeilSiegel.Free.swFree_block
module: Development.WeilBound.RepresentationTheoryGL.SiegelWeil.ArchimedeanSiegelWeil.PlaceIntegrals.SiegelWeilFreeOfBlockNonemptyFrames
covers: 970
status: drafted
drafted_by: writer@claude
---
This theorem proves [the statement form](/entry/siegel-weil-free-of-block-nonempty-frames/) for a block matrix $\beta = \begin{pmatrix} \beta_0 & 0 \\ 0 & 0 \end{pmatrix}$ with $t < n$. It is a short reduction: such a $\beta$ is singular, and [the singular case](/entry/sw-free-singular/) has the real content.

## Statement

The statement is the one of [the statement form](/entry/siegel-weil-free-of-block-nonempty-frames/): if $2n < M$ and $\mathcal{X}_\beta \neq \emptyset$, then $\Theta_\beta$ is the product of the local measures $m_v(\beta)$ with constant $1$.

## Proof

1. The hypothesis on $\beta$ says that $t < n$ and that $\beta_{ij} = 0$ when $i \ge t$ or $j \ge t$.
2. So row $t$ of $\beta$ is $0$, and $\det \beta = 0$.
3. [The singular case](/entry/sw-free-singular/) applies to $\beta$, with the same $J$, frames and bound $2n < M$.

## In the Lean code

The theorem is in [SiegelWeilFreeOfBlockNonemptyFrames.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeil/ArchimedeanSiegelWeil/PlaceIntegrals/SiegelWeilFreeOfBlockNonemptyFrames.lean#L531). Step 2 is `Matrix.det_eq_zero_of_row_eq_zero`. The proof discards the third part of `IsBlockM`, which says that $\beta_0$ is invertible. The same proof works for every Hermitian $\beta$ with a zero row. `IsBlockM` is in [TrMMemFramesEIff.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/TrMMemFramesEIff.lean#L22).
