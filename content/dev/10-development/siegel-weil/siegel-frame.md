---
id: siegel-frame
title: The Siegel-Weil identity for a represented block matrix
kind: theorem
decl: GlobalTheory.CompanionTheory.WeilSiegel.Frame.siegel_frame
module: Development.WeilBound.RepresentationTheoryGL.SiegelWeil.ArchimedeanSiegelWeil.PlaceIntegrals.SiegelWeilRankCoefficient
covers: 1305
status: drafted
drafted_by: writer@claude
---
This theorem proves the identity $I_\varphi(\beta) = W_\varphi(\beta)$ of the Siegel-Weil formula when $\beta$ is a singular Hermitian matrix in block normal form that is the Gram matrix of a frame of rank $r$. Both sides become integrals of $\varphi$ against the same product of local measures on frames. [`siegel_weil_rank_coefficient`](/entry/siegel-weil-rank-coefficient/) restates it, and [the singular case](/entry/siegel-deg/) uses it.

## Statement

We use the notation $I_\varphi(\beta)$, $W_\varphi(\beta)$ and the hypothesis `Hyp` of [`siegelDeg`](/entry/siegel-deg/).

**Theorem.** Assume `Hyp` for $\varphi$ on $M_{m \times r}(\mathbb{A}_E)$. Let $t < r$ and let $\beta = \begin{pmatrix} \beta_0 & 0 \\ 0 & 0 \end{pmatrix} \in \mathrm{Herm}_r(E)$ with $\beta_0$ an invertible $t \times t$ matrix. Suppose that $\beta = x^* J x$ for some $x \in M_{m \times r}(E)$ of rank $r$. Then $I_\varphi(\beta) = W_\varphi(\beta)$.

Here a frame is an $r$-tuple $X = (X_1, \dots, X_r)$ of vectors of length $m$, and $X^\top$ is the $m \times r$ matrix with columns $X_i$ (`trM`). Let $\mathcal{X}_\beta$ be the set of linearly independent frames over $E$ with Gram matrix $\beta$ (`framesE`). The last hypothesis says $\mathcal{X}_\beta \neq \emptyset$.

## Proof

1. **Setup.** `isCMExt_D` and `isHermND_gram` say that $E/F$ is CM and $J$ is Hermitian and invertible. `fundamentalDomain_adelicUnitary` gives a fundamental domain $\mathcal{F}$ for $\mathrm{U}(V)(F)$ in $\mathrm{U}(V)(\mathbb{A})$. The transpose of $x$ is in $\mathcal{X}_\beta$ (`trM_mem_framesE_iff`).
2. **Local measures.** `exists_tamagawa_measure_normalization` gives a basis of $E$ over $F$, Haar measures on $F_v$ with $\mathcal{O}_v$ of measure $1$, a Haar measure on $F_\infty$ with a fundamental domain of measure $1$ for $\mathcal{O}_F$, and at each place $v$ a family $m_v(T)$ of measures on the frames over $F_v \otimes E$ with Gram matrix $T$. It disintegrates the measure `coordW` on independent frames over `coordHerm` on Hermitian matrices, along $X \mapsto X^* J X$ (`IsGramFibFree`); we have not unfolded these two.
3. **The theta side.** Let $\Theta_\beta$ be the measure $\frac{1}{\nu(\mathcal{F})} \sum_{X \in \mathcal{X}_\beta} (h \mapsto h^{-1}X)_* (\nu|_{\mathcal{F}})$ (`thetaMeas`). By `frame_integral_theta_measure_formula`, $\varphi(X^\top)$ is $\Theta_\beta$-integrable and $I_\varphi(\beta) = \int \varphi(X^\top)\,d\Theta_\beta$.
4. **The product formula.** By `siegelWeil_free_of_block_nonempty_frames` $\Theta_\beta$ is the product of the local measures $m_v(\beta)$ with constant $1$ (`IsEulerProd b Θ 1`). This means: the masses $m_v(\beta)(L_v)$ of the standard lattices are finite with $\sum_v \lvert m_v(\beta)(L_v) - 1 \rvert < \infty$, and for each large finite set $S$ of places the integral of $\varphi_\infty \otimes \bigotimes_{v \in S} \varphi_v \otimes \bigotimes_{v \notin S} 1_{L_v}$ is $\int \varphi_\infty\,dm_\infty(\beta) \prod_{v \in S} \int \varphi_v\,dm_v(\beta) \prod_{v \notin S} m_v(\beta)(L_v)$.
5. **The Fourier side.** By `block_coefficient_local_global_factor`, for each measure $I$ that is such a product of the same $m_v(\beta)$ with constant $1$, and for which $\varphi(X^\top)$ is integrable, $W_\varphi(\beta) = \int \varphi(X^\top)\,dI$.

Steps 3 to 5 with $I = \Theta_\beta$ give $I_\varphi(\beta) = W_\varphi(\beta)$. Step 4 has the form of Siegel's mass formula as [the Learn page](/learn/theta/#the-siegel-weil-formula) states it.

## In the Lean code

The theorem is in [SiegelWeilRankCoefficient.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeil/ArchimedeanSiegelWeil/PlaceIntegrals/SiegelWeilRankCoefficient.lean#L16). `framesE` is in [TrMMemFramesEIff.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/TrMMemFramesEIff.lean#L18), `thetaMeas` and `IsEulerProd` in [IsEulerProd.lean](lean:CompanionTheory/SpectralGeometry/CountingDefinitions/AdelicEulerProducts/IsEulerProd.lean#L84). Four of the lemmas are restatements, proved by `first | exact …`: `exists_tamagawa_measure_normalization` of `Frame.exists_coord_fibres`, `siegelWeil_free_of_block_nonempty_frames` of `Free.swFree_block` ([L531](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeil/ArchimedeanSiegelWeil/PlaceIntegrals/SiegelWeilFreeOfBlockNonemptyFrames.lean#L531)), `frame_integral_theta_measure_formula` of `Frame.glue`, and `block_coefficient_local_global_factor` of `WhitFree.whit_eq_integral` ([L118](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeil/ArchimedeanSiegelWeil/PlaceIntegrals/BlockCoefficientLocalGlobalFactor.lean#L118)). We have not opened their proofs.

The block form of $\beta$ is used only to call `siegelWeil_free_of_block_nonempty_frames` and `block_coefficient_local_global_factor`. The name `exists_tamagawa_measure_normalization` speaks of Tamagawa measures, but its statement gives only the standard local Haar measures and the fibre families. `isCMExt_D` is in the namespace `Formalism.MainNotions.UnusedSlot34`, though this proof uses it.
