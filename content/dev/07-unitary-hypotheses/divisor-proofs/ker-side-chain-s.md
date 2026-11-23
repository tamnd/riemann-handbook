---
id: ker-side-chain-s
title: The kernel side of the chain bound
kind: theorem
decl: GlobalTheory.KernelHalfS.kerSide_chainS
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.KernelHalfChainNumbersAnyLevelPrime
covers: 876
status: drafted
drafted_by: writer@claude
---
This theorem proves [the bound on the kernel chain](/entry/kernel-half-chain-numbers-any-level-prime/), which is a second name for it, and which [the body of the column rows](/entry/rows-body-col-face/) uses in step 1. It bounds each step map of the kernel chain $Q$ at each infinite place by explicit numbers. The analytic input comes from bounds on theta vectors over a number field $M$ that contains their coefficients; the proof averages these bounds over the embeddings of $M$.

## Statement

The statement is that of [the second name](/entry/kernel-half-chain-numbers-any-level-prime/), with the notation of [the parent entry](/entry/rows-body-col-face/). Here is the conclusion in full. Let $R$ be the record of numbers that the member reads: $f$, $m$, $N$, $L$, $L_a$, $\log T$, the mean $\log \Omega$, and weights $\nu_{j,\tau,i}$, with $j$ in an index set $J \cong \{0, \dots, m-1\}$. `KerSide` $R$ $C$ says that there are numbers $g_0(j)$, $A(j, v)$, $\log\Omega(\tau, v)$, $\log\theta_0(v)$, $\log h(j)$, $\log h'(j)$, $\mathrm{vv}$ and $\log g$ such that:

- the mean of $\log \Omega(\tau, \cdot)$ over the places is $R.\log\Omega$, and the mean of $\log\theta_0$ is at most $C L$;
- $A(j,v) \le C f m^2 N^2 (\log g + \log T) + C f N^2 \log g$;
- $\log h(j), \log h'(j) \le C f N^2 (L + \log T + \log g)$, and $\log g \le C L$;
- $0 \le g_0(j) \le N^2$, $\log(8 + 32\, |P|\, g_0(j)\, \mathrm{vv}) \le C L_a$, and $\log(2 \sum_i \nu_{j,\tau,i} + 2) \le C L_a$;
- `FactorBounds` holds for the number $t(j, v)$ that `liftedMapLogSize` builds from all of these: for each step $i < n$ and each $v$, $\operatorname{Re}\langle \mathrm{step}\,\varphi, \mathrm{step}\,\varphi\rangle_v \le e^{t_i(v)} \operatorname{Re}\langle \varphi, \varphi \rangle_v$, where $t_i(v)$ is the sum of $t(j, v)$ over the $j$ that map to step $i$; the same holds for the last map to $S_1$, with the sum over the remaining $j$.

## Proof

The constant is $C = C_K + 2(C_c + C_i + C_y) + 2\max(C_t, 0) + 20 + 2\max(C_Y, 0)$, where each piece comes from one lemma named below.

1. `ChainClassNumbersS.classNumbers_leS` ($C_c$), `T.card_matrixStep_indices_le_exp` ($C_i$) and `CouplingCosetsS.ncard_ybSet_le` ($C_y$) bound the class numbers and index counts at each level by $\exp((C_c + C_i + C_y) E)$, with $E = f m^2 N_m^2 \log(g_0 g_1 T)$ (`errUnit`).
2. `T.exists_numberField_containing_coefficientData` gives a number field $M$ that contains the coefficients of the theta data. `PlaceWeights.exists_weights` gives weights on the embeddings of $M$ over each infinite place of $K$, with sum 1 and the right mean.
3. `T.log_norm_conj_vacuum_eq_rank_product_mul` gives log norms $\ell_t(\rho)$ of the vacuum vector at each embedding $\rho$, with mean at most $2\max(C_t, 0) f L$ by `T.normalisedFamily_normBound_absoluteConstant`.
4. `T.mean_logMetric_generator_eq_meanPeriod` gives the mean of $\log\Omega$.
5. `kerSide_of_meansS` packs these numbers into `KerSide`. Its size bounds use `SizeRowsS` through `log_eight_leS` and `log_nu_leS`.
6. `T.norms_matrixSteps_coupledFactor_bounded_anyLevelPrime` ($C_K$, fed by six lemmas on the normalized theta family) bounds the step maps at each $\rho$. `factorBounds_of_weights` averages these bounds with the weights of step 2 and gives `FactorBounds`.

The rest is bookkeeping.

## In the Lean code

The theorem is in [KernelHalfChainNumbersAnyLevelPrime.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KernelHalfChainNumbersAnyLevelPrime.lean#L219). `kerSide_of_meansS` is at [L104](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KernelHalfChainNumbersAnyLevelPrime.lean#L104). `KerSide` and `FactorBounds` are in [FactorBounds.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/FactorBounds.lean#L50), `StepBound_sq` in [TopPlaceLogTheta.lean](lean:Development/AbelianVarietyTheory/BlockTheory/DivisorBase/TopPlaceLogTheta.lean#L101), and `liftedMapLogSize` in [DivIneqExplicit6.lean](lean:Formalism/ThetaSupremumBounds/DivIneqExplicit6.lean#L15).

The ties, the conditions at $\mu_0$ and the size conditions are packed into one record `Core.Ht2.HypS`, except `FieldOfDefinition`, which goes only to the factor bound. The hypothesis `SizeRowsS` has `True` as its third conjunct ([ColHeightSharpWith.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/ColHeightSharpWith.lean#L16)). We have not unfolded the statements of the six theta lemmas behind $C_K$, among them `T.meanLogPeriod_chowlaSelberg`.
