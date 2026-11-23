---
id: rows-pos-type-p
title: The type bound for pairs of relevant terms
kind: theorem
decl: GlobalTheory.rowsPos_typeP
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.RowsPosTypeP
covers: 2511
status: drafted
drafted_by: writer@claude
---
This theorem proves the type bound `TypeP` with no hypothesis. The theorem [`hypotheses_nonempty_of_unramified_exponents_alt`](/proof/unitary-hypotheses/) passes it to `nonempty_hyps_of_allRows_alt` in its last line, and so it enters the step [HypsAlt is nonempty from the closed bound](/step/nonempty-hyps/). A second user is `degenerate_and_collisions_uncond`. The work is in [`typeBound_of_gap`](/entry/type-bound-of-gap/).

## Statement

The objects are: a datum $D$ (type `D7`), size data with a base $b > 0$, a Hida setting $X$, a choice $Y$ of finite sets of lattices (`Full X`), and a word $u$. We have not unfolded these types. Write $k, r, m, f$ for the integers `D.R.k`, `D.R.rS`, `D.R.m`, `D.R.f`, and $H_b(C) = b^{C m^2 f}$. The operator `Y.tO u u` has terms $t$, each with a vector $v(t)$ in a Hilbert space, a row index $j(t)$ and a label $\delta(t) \colon \mathbb{N} \to E$. Let $d_\pi$ be the complex dimension of the space $V_\pi(u)$, and let $\mathrm{mass}(Y, u) = \sum_{\Lambda} 1/\lvert\mathrm{Aut}(\Lambda)\rvert$ over the lattices of $Y$ at $u$. Here $\lvert\mathrm{Aut}(\Lambda)\rvert$ counts the maps on a quotient space induced by the isometries that fix $\Lambda$ and the flag of $u$. For a row index $j$ and a label $\delta$, let $\Delta(j, \delta) \geq 0$ be the norm of a local ideal attached to $\delta_j$ (`k2Del`) and $\sigma_H(j, \delta) \geq 1$ a product over the places $\tau$ of maxima of normalized absolute values of the $\delta_l$ (`k2S`, with $H = b^{C_H m}$). Put

$$a(j, \delta) = \Bigl(\frac{C}{k}\Bigr)^{j(k-1-j)f} \Delta^{-\frac{k-1-j}{2}} H_b(C)^{C r^4} \sigma_H^{-C_s k}, \qquad e(j, \delta) = \Delta^{k/2} H_b(C_h)^{C_h r^4} \sigma_H^{C_p k}.$$

**Theorem.** For all real $C_g, c_b, C_w, c_T, C_T, C_0$ with $c_b > 0$ and $c_T > 0$, there are $C_H, C_h, C_p \geq 0$ with the following property. For each $C_s \geq C_p + 4$ there is $C_\ast$ such that for each $C \geq C_\ast$ there are thresholds $C'_\ast, C_{l\ast}$, such that for all $C' \geq C'_\ast$, $C_l \geq C_{l\ast}$ and every datum $(D, b, X, Y, u)$ with `Ties D`, `KTwoHypotheses` for these constants and `ConcTie X Y`: for all $j', j'' \in \{1, \dots, r\}$, all labels $\delta', \delta''$, and each finite set $P$ of pairs $(t_1, t_2)$ of relevant terms with $j(t_1) = j'$, $\delta(t_1) = \delta'$, $j(t_2) = j''$, $\delta(t_2) = \delta''$,

$$\sum_{(t_1, t_2) \in P} \lVert v(t_1) \rVert \, \lVert v(t_2) \rVert \leq d_\pi \, \mathrm{mass}(Y, u) \, a(j', \delta') e(j', \delta') \, a(j'', \delta'') e(j'', \delta'').$$

The inner inequality is `TypeAt`. `KTwoHypotheses` is a list of size conditions on $k, r, m, b$ and the field $E$; we have not unfolded `Ties` or `ConcTie` in full.

## Proof

`bessel_multiplicity_one_large_gap_and_whittaker_bessel` gives two facts, `UniqGap` and `BesselOfW`. `UniqGap` says: if $k \geq 1$, $n = 2r + k + 1$, the Harish-Chandra parameter $\lambda$ has $\lvert\lambda_a - \lambda_b\rvert \geq h$ whenever the signs $\varepsilon_a, \varepsilon_b$ differ, and $h \geq 120 n^3$, then, under conditions on the character and on the target representation $\pi$, any two smooth Bessel maps from the discrete series $\sigma$ are linearly dependent on the smooth vectors. `BesselOfW` says that, under a gap condition, an equivariant $W$ with finite nonzero $L^2$ norm, fixed by convolution with a matrix coefficient of $\sigma$, is $W(x) = B(\sigma(x) w)$ for a Bessel map $B$.

`hyp_of_uniqGap` adds three proved facts to `UniqGap` (`hypsG_of_zuck zuckerman_gap`, `factMultOne`, `factDsigHC`) to get the bundle `GapIn.Hyp`. Then [`typeBound_of_largeGap_discreteSeries_bessel`](/entry/type-bound-of-large-gap-discrete-series-bessel/) gives `TypeP`.

## In the Lean code

The theorem is in [RowsPosTypeP.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/RowsPosTypeP.lean#L9). `TypeP` is at [RowsPos.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RowsPos.lean#L18) and `TypeAt` at [DimFormC.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DimFormC.lean#L40).

The definition `TypeP` exists twice with the same text: `Formalism.L2.SG.RowsPos.TypeP` and `GlobalTheory.TypeAsm.TypeP` in [PerRowC.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/PerRowC.lean#L30). Lean identifies them by unfolding, and `degenerate_and_collisions_uncond` uses the second name. The file `RowsPos.lean` has `TypeC`, the same bound without $c_b, c_T > 0$ and without `Ties D`.
