---
id: hyp-step
title: Adding a hyperbolic plane to an isotropic frame
kind: theorem
decl: GlobalTheory.CompanionTheory.WeilSiegel.HypStep.hyp_step
module: Development.WeilBound.RepresentationTheoryGL.SiegelWeil.ArchimedeanSiegelWeil.PlaceIntegrals.ZeroBlockCoefficientRankIncrease
covers: 559
status: drafted
drafted_by: writer@claude
---
This theorem proves the Euler product property of the theta measure on isotropic $(n+1)$-frames of $H \oplus J$ from the same property on isotropic $n$-frames of $J$. It proves [`zero_block_coefficient_rank_increase`](/entry/zero-block-coefficient-rank-increase/), the step for the zero Gram matrix in the induction of [`swFree_singular`](/entry/sw-free-singular/).

## Statement

We use the frames $\mathcal{X}_T$, the theta measure $\Theta_T$, the standard lattices $L_v$ and the Euler product property (`IsEulerProd`) of [the represented block case](/entry/siegel-frame/), now for a Hermitian form $J$ on $E^M$. Let $H \oplus J$ be the form $\begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & J \end{pmatrix}$ on $E^{M+2}$ (`hypOne J`), and let $e_0 = (1, 0, \dots, 0)$, an isotropic vector of it.

$\mathrm{SWFree}(J, T)$ says: for each basis of $E$ over $F$, each Haar measure on $F_\infty$ and on each $F_v$ normalized as in [the represented block case](/entry/siegel-frame/), each Haar measure $\mu$ on $\mathrm{U}(J)(\mathbb{A})$ with a fundamental domain $\mathcal{F}$ (`IsFDH`), and each choice of local fibre measures $m_\infty(\cdot)$, $m_v(\cdot)$ of the coordinate measure along the Gram map (`IsGramFibFree`, not unfolded), the measure $\Theta_T$ is the Euler product of $m_\infty(T)$ and the $m_v(T)$ with constant $1$.

**Theorem.** Let $E/F$ be CM, $J$ Hermitian and invertible, $1 \le n$ and $2n < M$. Suppose that $\mathcal{X}_{0_n}(J)$ is not empty and that $\mathrm{SWFree}(J, 0_n)$ holds. Then $\mathrm{SWFree}(H \oplus J, 0_{n+1})$ holds.

## Proof

Write $\Theta^{(k)}$ for the theta measure on isotropic $k$-frames, $m^{(k)}_v$ for the local fibre measure at $0_k$, and put $\tau_v = m^{(n)}_v(L_v)$ for $J$ and $M_v = m^{(n+1)}_v(L_v)$ for $H \oplus J$.

1. **Inputs.** `hyperbolic_sum_nondegenerate_frame`: $H \oplus J$ is Hermitian and invertible, and $e_0 \in \mathcal{X}_{0_1}(H \oplus J)$. `fam_inf` and `fam_fin` give fibre measures for $J$ in rank $n$ and for $H \oplus J$ in rank $1$. `unitary_group_finite_volume` gives a Haar measure and a fundamental domain for $\mathrm{U}(J)$. The hypothesis gives the Euler product for $\Theta^{(n)}$ of $J$. `siegelWeilFree_zero_rank_one_of_three_le` gives it for $\Theta^{(1)}$ of $H \oplus J$.
2. **Masses.** `zero_block_coefficient_induction_right` gives $M_v < \infty$ and $\sum_v \lvert M_v - 1 \rvert < \infty$.
3. **Local unfolding.** Let $c(a, Y)$ be the frame $(e_0, (a_1, 0, Y_1), \dots, (a_n, 0, Y_n))$ (`consA`). At each place, `zero_block_coefficient_induction_left` gives $\Psi_v$ with $\Psi_v(g e_0) = \iint \varphi_v(g\,c(a, Y))\,da\,dm^{(n)}_v(Y)$ and $\int \varphi_v\,dm^{(n+1)}_v = \int \Psi_v\,dm^{(1)}_v$.
4. **Global unfolding.** `hyperbolic_plane_unfolding_integral` writes the integral of $\Phi$ against $\Theta^{(n+1)}$ as an integral against $\Theta^{(1)}$ of $\Psi(h e_0) = \iint \Phi(h\,c(a, Y))\,dA(a)\,d\Theta^{(n)}(Y)$, with $dA$ of covolume $1$ on $\mathbb{A}_E^n$ (`covolume_one_euler_product_measure_exists`).
5. **Factorization.** `euler_product_measure_covolume_one` factors $\Psi$ for a pure tensor $\Phi$. `hyperbolic_rank_one_global_volume` integrates the result against $\Theta^{(1)}$, with factors $p_v = m^{(1)}_v(P_v)$, where $P_v$ is the orbit of $e_0$ under the stabilizer of $L_v$ (`primV`). For almost all $v$, `lattice_stabilizer_volume_almost_all` says that $\Psi_v$ for $\varphi_v = 1_{L_v}$ equals $\tau_v$ on $P_v$. With step 3 this gives $\tau_v p_v \le M_v$.
6. **Limit.** Monotone convergence (`lintegral_iSup_places`) and `iSup_finite_product_tail_limit` turn the supremum over $S' \supseteq S$ of $\prod_{v \in S' \setminus S} M_v \prod_{v \notin S'} \tau_v p_v$ into $\prod_{v \notin S} M_v$.

## In the Lean code

The theorem is in [ZeroBlockCoefficientRankIncrease.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeil/ArchimedeanSiegelWeil/PlaceIntegrals/ZeroBlockCoefficientRankIncrease.lean#L78). `e0`, `consA`, `primV` and `purePr` are in [IsCovolOne.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/IsCovolOne.lean#L12), `hypOne` in [HypOneZeroZero.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/HypOneZeroZero.lean#L8) and `SWFree` in [TrMMemFramesEIff.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/TrMMemFramesEIff.lean#L40). `fam_inf`, `fam_fin` and `lintegral_iSup_places` are proved in the same file. The other lemmas are restatements, proved by `first | exact …`; we have not opened their proofs.

The hypothesis that $\mathcal{X}_{0_n}(J)$ is not empty (`hne`) is never used. The hypotheses `h₀` and `h₁` say that $0$ is Hermitian, which is always true.
