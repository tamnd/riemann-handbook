---
id: siegel-weil-free-of-block-nonempty-frames
title: The theta measure of a represented block matrix is an Euler product, statement form
kind: theorem
decl: GlobalTheory.T.siegelWeil_free_of_block_nonempty_frames
module: Development.WeilBound.RepresentationTheoryGL.SiegelWeil.ArchimedeanSiegelWeil.PlaceIntegrals.SiegelWeilFreeOfBlockNonemptyFramesStatement
covers: 973
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the block case](/entry/sw-free-block/). Its only user is [the Siegel-Weil identity for a represented block matrix](/entry/siegel-frame/), in step 4. The real content is in [the singular case](/entry/sw-free-singular/).

## Statement

We use the names of [`siegel_frame`](/entry/siegel-frame/): $\mathcal{X}_\beta$ is the set of linearly independent frames with Gram matrix $\beta$, $\Theta_\beta$ is the theta measure on $\mathcal{X}_\beta$, and $m_v(\beta)$ are the local measures on frames.

**Theorem.** Let $E/F$ be a CM extension and $J$ a nondegenerate Hermitian $M \times M$ matrix over $E$. Let $t < n$ and let $\beta \in \mathrm{Herm}_n(E)$ be $\begin{pmatrix} \beta_0 & 0 \\ 0 & 0 \end{pmatrix}$ with $\beta_0$ an invertible $t \times t$ matrix. Assume $2n < M$ and $\mathcal{X}_\beta \neq \emptyset$. Then, for every choice of standard local Haar measures, every Haar measure on $U_J(\mathbb{A}_F)$ with a fundamental domain, and all fibre families $m_v(\beta)$ of the Gram map, $\Theta_\beta$ is the product of the $m_v(\beta)$ with constant $1$.

The last sentence is the predicate `SWFree`. "Product with constant $1$" means `IsEulerProd b Θ 1`, as step 4 of [`siegel_frame`](/entry/siegel-frame/) spells out.

## Proof

The proof is `swFree_block`, applied to the same arguments.

## In the Lean code

The theorem is in [SiegelWeilFreeOfBlockNonemptyFramesStatement.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeil/ArchimedeanSiegelWeil/PlaceIntegrals/SiegelWeilFreeOfBlockNonemptyFramesStatement.lean#L11). It is proved by `first | exact …`. `framesE`, `IsBlockM` and `SWFree` are in [TrMMemFramesEIff.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/TrMMemFramesEIff.lean#L18).
