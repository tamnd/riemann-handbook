---
id: pointwise-bound-discrete-series
title: The pointwise bound for discrete series coefficients, from the eigenfunction bound
kind: theorem
decl: GlobalTheory.BpDiscreteSeriesTwoInputs.pointwise_bound_discreteSeries
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.PointwiseBoundDiscreteSeriesCoefficients
covers: 1094
status: drafted
drafted_by: writer@claude
---
This theorem proves the bound `ThmBpDS` for matrix coefficients of discrete series from two inputs, `BesselXiIntegrable` and `ThmPActualCpt`. It reduces the bound to the [pointwise bound for Capelli eigenfunctions](/entry/pointwise-bound-capelli-eigenfunction/). The restatement [`T.pointwiseBound_discreteSeries_coefficients`](/entry/pointwise-bound-discrete-series-coefficients/) gives it its public name, and [A pointwise bound for discrete series coefficients](/entry/discrete-series-coef-pointwise-bound/) supplies the two inputs.

## Statement

**Theorem.** $\mathrm{BesselXiIntegrable} \Rightarrow \mathrm{ThmPActualCpt} \Rightarrow \mathrm{ThmBpDS}$.

The three statements are unfolded in [A pointwise bound for discrete series coefficients](/entry/discrete-series-coef-pointwise-bound/) and [its restatement](/entry/pointwise-bound-discrete-series-coefficients/). We keep the notation there, with $n = 2r+k+1$: $\sigma$ is a discrete series of $U(H_{k,r})$ with Harish-Chandra parameter $\lambda'$, $f$ is a translate of a $K$-finite coefficient of $\sigma$, and $\lambda$ is a second parameter that satisfies `StdHyp` and has gaps at least $200\,\|\lambda'-\lambda\|_1$.

## Proof

Fix $C_h$ and $C_0 \ge 0$. The idea: $f$ is a decaying Capelli eigenfunction whose expansion on the big cell has controlled coefficients, and these are the hypotheses of the eigenfunction bound.

1. **Constants.** Apply the [eigenfunction bound](/entry/pointwise-bound-capelli-eigenfunction/) with $C = 2|C_h|$, $C_3 = |C_h| + 6$ and $C_0$. It gives $C_4$ and $C_c$. Three numerical lemmas give thresholds: `BpStdNum.num_of_stdHyp` (with $C_0 + 10$) gives $G_1$, `StdGrid.std_grid` gives $G_2$, and `margin_arith_closing` (with $C_c, C_0$) gives $G_3$. The constants of `ThmBpDS` are $\max(C_4, 0)$ and $C_g^0 = \max(G_1, G_2, G_3)$.
2. **Half-integral types.** `capelliParam_mem_int_add_half` shows that each $u_i$ and $u'_i$ lies in $\mathbb{Z} + \frac{k-1}{2}$. It uses the place condition of $p$ and $T, T' > 0$ (from `StdHyp`).
3. **Integral shift.** `hcParam_sub_integral` writes $\lambda' = \lambda + \nu_0$ with $\nu_0 \in \mathbb{Z}^n$, $\|\nu_0\|_1 = d := \|\lambda' - \lambda\|_1$, and $|\lambda'_s - \lambda_s| \le d$ for each $s$.
4. **Grid conditions.** `std_grid` turns `StdHyp` into `StdNum` with $C = 2|C_h|$ and $c = \tfrac12 \max(C_g(2r+2)^3, 200d)$. It also gives $T, T' \le b^{2|C_h|(2r+2)}$ and the case condition `Cases P n₀`.
5. **Numerical family.** Let $q_0 = \|\nu_0\|_1 + (r+1)(2p_0+n_0) + (r+1)(r+2)$. The third clause of `margin_arith_closing` gives $q_0 \le d + (C_0+10)(2r+2)^3$. With this, `num_of_stdHyp` gives reals $b_v, g_a, h$ with `Num` for $u$ and for $u'$, and $h \ge C_g(2r+2)^{9/2}(3(r+1)n^2 + n^3)$. `NumFam.num_fam` then gives the condition `GapOK` at $h/2$, $b \ge 1$, and gaps of size $h/2$ between entries of $\lambda'$ of different sign.
6. **Arithmetic.** `margin_arith_closing` gives the two inequalities that the eigenfunction bound asks for: the decay margin $C_c(r+1)^4(3(r+1)n^2+n^3) \le A_0 - ((2r+2)p_0 + n_0(r+1))$ with $A_0 = a(r, h/2) - 1$, $a(r,h) = h/(8\sqrt{2(r+1)})$; and $d + (2r+2)p_0 + n_0(r+1) \le c - 1$.
7. **Eigenfunction.** `T.discreteSeries_KFinite_coeff_capelli_eigen_decay` gives `EigDec f A₀ λ'`: $f$ is smooth on $G$, decays to order $A_0$ with all derivatives, and satisfies $\mathcal{C}(y) f = \prod_s (y + \lambda'_s) f$ for the Capelli operator $\mathcal{C}(y)$.
8. **Regularity.** `T.discreteSeries_coefficient_expansion_bound_ball'` gives, for each $a \le 2p_0 + n_0$, functions $f_i$ and complex numbers $c_i$ with $\det M_{r+1}(\mathrm{big}(z))^a\, V_f = \sum_i c_i V_{f_i}$ on the big cell, $\sum_i |c_i| \le b^{(|C_h|+6)(2r+2)^2 a}$, and the big cell norm of each $f_i$ at most that of $f$. Here $V_f$ is the vector `p.V f`. `P.regularity_at_place` turns this into `RegularityBoundBigCell`.

The eigenfunction bound now gives `ThmBpAt` with $C_4$. The lemma `thmBpAt_mono` raises $C_4$ to $\max(C_4, 0)$, since $b \ge 1$. The rest is bookkeeping.

## In the Lean code

The theorem is in [PointwiseBoundDiscreteSeriesCoefficients.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/PointwiseBoundDiscreteSeriesCoefficients.lean#L28). The two inputs are used only by `T.pointwiseBound_capelli_eigenfunction`. We have read the statements of the lemmas named above, not their proofs. `Num`, `GapOK` and the Capelli operator `Q.CV` (a quantum minor operator) are not unfolded here.

The same file proves `thmBpAt_mono` (line 20). Its statement is the same as `BpEigen.pointwise_bound_mono` in [PointwiseBoundCapelliEigenfunction.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/PointwiseBoundCapelliEigenfunction.lean#L14), with a different proof.
