---
id: count-i-of-printed-bound-k-kato-automorphy
title: The case I count from the extended hypotheses
kind: theorem
decl: UpperTheory.V.Z.J.count_i_of_printed_bound_k_kato_automorphy
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.LinkedUnlE
covers: 564
status: drafted
drafted_by: writer@claude
---
This theorem proves the count $\mathrm{CountI}$ for `vwin_of_hypotheses_H_E_alt` (Step 5 of [The window bound VWin](/proof/vwin/)). It is a pass-through: it composes four lemmas.

## Statement

**Theorem.** Assume $\mathrm{HypothesesH'}$, $\mathrm{LemmaK}(C_K)$ for some $C_K$, `KatoTwoW` and `AutomorphyUnramifiedCoefficientsAlt`. Then $\mathrm{CountI}$ holds.

$\mathrm{CountI}$ says: for each primitive $\chi$ there are $C$ and primes $r_1, r_2$ such that, for each host $h$ of $\chi$ with $q_1$ and $d$ above $r_1, r_2$, each $t$ with `h.Big t`, $0 < e < t$ and each finite set of odd primes $l$ in case I, $\sum_l \log l \sum_\psi V(\psi)/e_{\mathcal{O}} \le (N t)^C$.

## Proof

1. `cohInp_alt` makes `CohInp` from Lemma K.
2. [`oneCharU_of_katoTwoW_rig_admI_automorphy`](/entry/one-char-u-of-kato-two-w-rig-adm-i-automorphy/) gives `OneCharU_s`: $V(\psi)/e_{\mathcal{O}}$ is at most twice a sum of $v_l(\operatorname{tr} \rho(\sigma) - t)$ over three-dimensional admissible $\rho$. Two of its inputs use `unlEnd3E` of [`linkedUnlE_alt`](/entry/linked-unl-e-alt/).
3. `propGK_of_numberU3U_of_oneCharU` and `numberU3U_of_prints` give a nonzero integer whose $l$-adic valuations bound these sums (`PropGK`).
4. `U3.corGK` sums over $l$ with two primes $p \ne p'$, and `U3.countI` chooses $r_1, r_2$.

## In the Lean code

The theorem is in [LinkedUnlE.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/LinkedUnlE.lean#L49).

`corGK_of` in [CorGKOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/SmallClassNumbers/CorGKOf.lean#L10) builds the same chain from $\mathrm{HypothesesH'}$ alone, with [`lemmaK_litN_alt`](/entry/lemma-k-lit-n-alt/) and [`katoTwoW_of_printsH`](/entry/kato-two-w-of-prints-h/). So the last three hypotheses here are not needed.
