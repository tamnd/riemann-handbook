---
id: sw-free-singular
title: The theta measure of a represented singular matrix is an Euler product
kind: theorem
decl: GlobalTheory.CompanionTheory.WeilSiegel.Free.swFree_singular
module: Development.WeilBound.RepresentationTheoryGL.SiegelWeil.ArchimedeanSiegelWeil.PlaceIntegrals.SiegelWeilFreeOfBlockNonemptyFrames
covers: 969
status: drafted
drafted_by: writer@claude
---
This theorem says that the theta measure $\Theta_\beta$ of a singular Hermitian matrix $\beta$ is the product of the local measures $m_v(\beta)$ with constant $1$, when $\beta$ is the Gram matrix of a frame and $M$ is large. Its only user is [the block case](/entry/sw-free-block/). The proof is an induction on the size of $\beta$. Each step splits off one vector with a Witt decomposition.

## Statement

We use the names of [`siegel_frame`](/entry/siegel-frame/) and the predicate `SWFree` of [the statement form](/entry/siegel-weil-free-of-block-nonempty-frames/).

**Theorem.** Let $E/F$ be a CM extension and $J$ a nondegenerate Hermitian $M \times M$ matrix over $E$. Let $\beta \in \mathrm{Herm}_n(E)$ with $\det \beta = 0$. If $2n < M$ and $\mathcal{X}_\beta \neq \emptyset$, then `SWFree` holds for $J$ and $\beta$.

## Proof

Induction on $n$, for all $M$ and $J$ at once. Fix $X \in \mathcal{X}_\beta$.

**$n = 0$.** The determinant of the empty matrix is $1$, so there is nothing to prove.

**$\beta = 0$, $n = 1$.** Then $M \ge 3$, and `siegelWeilFree_zero_rank_one_of_three_le` gives the result.

**$\beta = 0$, $n \ge 2$.** The vector $X_1$ is nonzero and isotropic. So there is $g \in \mathrm{GL}_M(E)$ with first column $X_1$ and

$$g^* J g = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & J_1 \end{pmatrix},$$

a hyperbolic plane plus $J_1$ of size $M - 2$ (`split_hyp`). The other vectors of the frame give a frame for $J_1$ with Gram matrix $0$ of size $n - 1$ (`frames_tail_hyp`). Induction gives `SWFree` for $J_1$ and $0_{n-1}$. [`zero_block_coefficient_rank_increase`](/entry/zero-block-coefficient-rank-increase/) lifts this to the matrix above and $0_n$. `siegelWeilFree_of_congruent_form` moves it back to $J$.

**$\beta \neq 0$.** There are $t \in F^\times$ and $x$ with $x^* \beta x = t$ (`exists_value`). So there is $h \in \mathrm{GL}_n(E)$ with $h^* \beta h = \operatorname{diag}(t, \beta_1)$, and $\det \beta_1 = 0$ (`split_herm`). The frame $Y = Xh$ has this Gram matrix. Its first vector $Y_1$ has $Y_1^* J Y_1 = t \neq 0$. So there is $g$ with first column $Y_1$ and $g^* J g = \operatorname{diag}(t, J_1)$ (`split_anisotropic`). The other vectors give a frame for $J_1$ with Gram matrix $\beta_1$ (`frames_tail_aniso`). Induction gives `SWFree` for $J_1$ and $\beta_1$. Then:

1. `siegelWeilFree_extend_by_scalar_block` gives it for $\operatorname{diag}(t, J_1)$ and $\operatorname{diag}(t, \beta_1)$;
2. `siegelWeilFree_of_congruent_form` moves it to $J$;
3. `siegelWeilFree_of_congruent_matrix` moves it to $\beta$.

The bound $2n < M$ passes to the smaller case, since $M$ drops by $2$ or $1$ when $n$ drops by $1$.

## In the Lean code

The theorem is in [SiegelWeilFreeOfBlockNonemptyFrames.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeil/ArchimedeanSiegelWeil/PlaceIntegrals/SiegelWeilFreeOfBlockNonemptyFrames.lean#L457). The helpers `split_herm`, `exists_value`, `split_hyp`, `frames_tail_aniso` and `frames_tail_hyp` are in the same file, at L80, L138, L190, L384 and L419. `split_anisotropic` is in [SplitAnisotropic.lean](lean:CompanionTheory/SpectralGeometry/LocalGlobalProofs/AdelicAnalysis/SplitAnisotropic.lean#L18).

The five lemmas in `GlobalTheory.T` are second names, proved by `first | exact …`: of `SW.OneZero.one_vector_zero`, `HypStep.hyp_step`, `Iso.swFree_of_isometry`, `Aniso.aniso_step` and `Scale.sw_free_scale`. We have not opened their proofs. The proof here does only linear algebra on frames and forms.
