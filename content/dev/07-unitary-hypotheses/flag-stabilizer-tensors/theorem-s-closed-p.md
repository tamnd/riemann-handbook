---
id: theorem-s-closed-p
title: Theorem S, with the per-pair inputs supplied
kind: theorem
decl: Formalism.L2.SG.PoincareAmplitudeLowerBounds.theoremS_closedP
module: Formalism.LocalToGlobal.SiegelLatticeTheory.FlagStabilizerTensors.TheoremSClosedP
covers: 920
status: drafted
drafted_by: writer@claude
---
This theorem is Theorem S: a bound on the off-diagonal entries $K_0(u, u')$ of the spectral ties, and on a Hilbert-Schmidt norm, by $(1 + b^{-6})\, d(u) d(u') / D^*$. It takes 19 global hypotheses. [`theoremS_of_conj`](/entry/theorem-s-of-conj/) calls it with the hypotheses as one conjunction. Its proof makes the inputs for one pair of words that [`theoremS_rec3P`](/entry/theorem-s-rec3-p/) needs.

## Statement

The 19 hypotheses are `LocalModelAt`, `DensInputAt` and `RowsInputP` for each datum, `RowNGP`, `KppOffC`, `CarrierP`, `KernelExponentAgreement`, `FoldOKC`, `OOIntAllC`, `AbsConvC`, `FinXC`, `WuDecayOfGap`, `ChoicesC`, `FormulaC`, `RowsSumC`, `RowFormAllP`, `MassDataHypAll`, `LinkAll` and `SplitAll`. We have not unfolded most of them. [`theoremS_leaves_of_carrierG`](/entry/theorem-s-leaves-of-carrier-g/) proves all 19.

**Theorem.** Assume the 19 hypotheses. For each real $C_{\mathrm{thr}}$ there are $C_4 \ge 1$, $C_A \ge \max(C_{\mathrm{thr}}, 1)$ and $0 \le C \le C_A$ with the following property. For all $C_0 \ge 1$, $C_G \ge 0$, $C_\Delta > 4$ and $c_T, C_b > 0$ with $c_T C_b > 1$ there is $k_0$ such that, for all $C_g, c_b, C_w, c_{Tf}, C_T, C_{0f}$ with $c_b, c_{Tf} > 0$, there are $C_n \ge 0$, $C'_0$ and $C_{l,0}$ with this property: for all $C' \ge C'_0$ and $C_l \ge C_{l,0}$, each datum $D$, size data $L$ with scale $b \ge 0$, tie package $T$ (`STies`) and words $u \neq u'$, if

1. `Ties D`, the size condition `SizesAt` with these constants and $k_0$, `Hyp0`, `Stand`, `KTwoHypotheses`, the gap hypothesis `GapHyp`, `LocTied` and `TFrameAt` hold, and
2. the loop pairs are small: `RowBig` and `RowNotScalar` hold with $\varepsilon_L = \exp(-\tfrac13 k f \log k)$ and $d = d(u) d(u') / D^*$,

then
$$\|K_0(u,u')\|^2 \le (1 + b^{-6})\, \frac{d(u)\, d(u')}{D^*}, \qquad \|K_D(u,u')\|_{\mathrm{HS}}^2 \le (1 + b^{-6})\, \frac{d(u)\, d(u')}{D^*}.$$

Here $K_0(u, u')$ is the sum of the identity, generic and non-generic parts of the term series $t_O(u, u')$ (see [`pbApplied`](/entry/pb-applied/)), and $K_D(u, u')$ is the operator `KD D u u'`.

## Proof

Fix the constants from `theoremS_rec3P`, which takes the first four hypotheses and `CarrierP`. Enlarge $C'_0$ and $C_{l,0}$ to cover the constants of `KppOffC` and `RowFormAllP`. Then, for one pair $(u, u')$:

1. Unpack `SizesAt`.
2. `FinXC` and `GapHyp` give finiteness `FinX`; `WuDecayOfGap` gives the decay; with `LocTied` and `TFrameAt`, `STies.concTie` gives the concrete tie `ConcTie`.
3. `ChoicesC` chooses the auxiliary data, with uniformizers $\varpi$ and a row label $\kappa$. `FormulaC` gives the formula with $n_c$ = `cExpl`.
4. From `SizeNumbers`, $k \ge 32$, $b \ge 16$ and $(kb)^8 \le g_i$, so $g_i \ge 3$.
5. `absConvTied_of_full` gives absolute convergence. `KppOffC` and `kppOff_of_termZero` show that the degenerate part of $t_O(u, u')$ is zero.
6. `RowsSumC`, `RowFormAllP`, `MassDataHypAll`, `LinkAll`, `SplitAll` and `KernelExponentAgreement` give the remaining inputs, and `idDegenerate_tO` gives `IdDegenerate`.

Then `theoremS_rec3P` gives the bound.

## In the Lean code

The theorem is at [TheoremSClosedP.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/TheoremSClosedP.lean#L256). Most of the hypotheses and `SizesAt` are defined in [TheoremSRecursion.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/TheoremSRecursion.lean#L28).

All 19 hypotheses are used. The fact $T_h > 0$, which `MassDataHypAll` needs, is the 18th of the 19 conjuncts of `SzHyp`. The number of infinite places of $F$ is matched to $f$ by `cardC_holds`, with no hypothesis.
