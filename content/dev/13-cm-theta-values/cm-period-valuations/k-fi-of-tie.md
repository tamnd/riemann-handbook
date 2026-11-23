---
id: k-fi-of-tie
title: The kernel maps raise the filtration of member forms, from a pinned tie
kind: theorem
decl: GlobalTheory.KFiClose.kFi_of_tie
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.KernelClassSumsCarryChainComplexForms
covers: 339
status: drafted
drafted_by: writer@claude
---
This theorem proves the condition `KFi` of [`Pdv.At`](/entry/at-of-true-columns/) from a tied kernel entry. It is used through its second name [`kernelClassSums_carry_chainComplexForms`](/entry/kernel-class-sums-carry-chain-complex-forms/), which [`at_of_true_columns`](/entry/at-of-true-columns/) calls. The idea: a kernel map whose theta kernel moves by a scalar under a stabiliser sends forms with the matching law to forms with the same law.

## Statement

Let $D$, the data over $D$, `ex` and the tied kernel entry $t$ be as in [`kernelClassSums_carry_chainComplexForms`](/entry/kernel-class-sums-carry-chain-complex-forms/).

**Theorem.** Assume `ColSide t` and `FormsPin t`. Then for each word $u$ and each level $i < m$, the kernel map $K_i$ sends the member forms $F_i$ into $F_{i+1}$, both for the forms of $D$ and for the twisted forms of each used tuple $\mu$ (`OrbitPlaces.KFi D ex.tw`).

A tuple is *used* (`DV.Used`) if it is $\mu_0$, $\mu^*$, $\mu^{*\prime}$ or $\mu_w$ for a place $w$.

`ColSide t` is a structure of eight facts, among them: the fields of $t$ are good, the selection is valid, the bad primes are in the set $S$ of $t$, the characters are tied, and depth and sharpness conditions hold. `FormsPin t` says: for each $u$ and each used $\mu$ there is a stabiliser datum $G$ such that `FormsAre` and `StabPin` hold. `FormsAre` describes $F_i$ for $1 \le i \le m$: a family $\varphi$ is in $F_i$ if and only if each $\varphi(c)$ is a value of the frame map (`IsVal`) and satisfies the law of each $g \in G_i(c)$, that is $f(y) = g_2\, f(y')$ whenever the frame of $y$ is $g_1$ times the frame of $y'$. `StabPin` identifies $G$ with explicit stabiliser sets of the tie. We have not unfolded `IsVal` or `StabPin` in full.

## Proof

1. Fix $u$ and a used $\mu$. `FormsPin` gives $G$ with `FormsAre` and `StabPin`.
2. `kernelOperator_maps_stabiliserEquivariant_forms` (a second name for `FiCore.K_mem_Fi`) proves $K_i(F_i) \subseteq F_{i+1}$ from four inputs: `FormsAre`; the unfolding condition `UnfIs` (the field `t.unf`); the differentiability of the theta kernels of $t$ (`kerTie_entire`); and the term law (`TermLaw`): each $g \in G_{i+1}(c')$ has $\det g_1 \neq 0$ and moves the theta kernel by a scalar $k$ with $g_2 = k \prod_\tau \tau(\det g_1)^{-s_{i,\tau}}$. The term law comes from `classSum_term_law_stabiliser_target` (a second name for `term_law`), which uses `ColSide` and `StabPin`.
3. Inside `K_mem_Fi`, $K_i\varphi(c') = \sum_c w(c)\, K(c, c')(\varphi(c))$. Each term keeps the value property and the law, and so does the sum.
4. For the forms of $D$ itself: $\mu_0$ is used, so step 2 holds at $\mu_0$. `memberForms_stable_of_reference_tuple` carries it to the forms of $D$ by the isomorphisms `eMu0` of the twist.

## In the Lean code

The theorem is at [KernelClassSumsCarryChainComplexForms.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/KernelClassSumsCarryChainComplexForms.lean#L13). The lemmas:

- `K_mem_Fi` at [KernelOperatorMapsStabiliserEquivariantForms.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/KernelOperatorMapsStabiliserEquivariantForms.lean#L29);
- `kerTie_entire` at [KerTieEntire.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/KerTieEntire.lean#L12);
- `term_law` at [ClassSumTermLawStabiliserTarget.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/ClassSumTermLawStabiliserTarget.lean#L25);
- `memberForms_stable_of_reference_tuple` at [MemberFormsStableOfReferenceTuple.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/MemberFormsStableOfReferenceTuple.lean#L43).

`FormsAre`, `TermLaw` and `LawAt` are in [FormsAre.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/FormsAre.lean#L19), `FormsPin` and `ColSide` in [FormsPin.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/FormsPin.lean#L37). `ColSide` is used only in the term law. The conclusion depends on $D$ and `ex.tw`, not on $t$.
