---
id: count-v-of-printed-bound-k-reduced-unitary-lift
title: The case V count from the extended hypotheses
kind: theorem
decl: UpperTheory.V.Z.J.count_v_of_printed_bound_k_reduced_unitary_lift
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.LinkedUnlE
covers: 787
status: drafted
drafted_by: writer@claude
---
This theorem proves the count $\mathrm{CountV}$ for `vwin_of_hypotheses_H_E_alt` (Step 5 of [The window bound VWin](/proof/vwin/)). It is a pass-through. It fills in the thirteen hypotheses of [the case V count from a host frame](/entry/count-v-of-finiteness-duality-euler-host/), which has the real content.

## Statement

**Theorem.** Assume $\mathrm{HypothesesH'}$, $\mathrm{LemmaK}(C_K)$ for some $C_K$, and $\mathrm{ThmS6Core\_s}$. Then $\mathrm{CountV}$ holds.

$\mathrm{CountV}$ is the count shape of the chapter for case V with $R_1(l, \psi) \le 2^{c_2(\psi)}$. $\mathrm{ThmS6Core\_s}$ is an automorphy statement for three-dimensional points of a deformation ring; [the next entry](/entry/count-v-of-finiteness-duality-euler-host/) states it. The chapter gets it from `ends0_alt`.

## Proof

- `unitary_lift_of_reduced_core` turns $\mathrm{ThmS6Core\_s}$ into $\mathrm{ThmS6\_s}$, with `matIrr_open` and `matIrr_cyc` for the two added irreducibility clauses.
- `Alg.M.main_holds` and `Alg.M.mprime_holds` give `LemmaM` and `LemmaM'`.
- The six [[Galois cohomology|9MPCZ3EAJM]] inputs are fields of `hH.litN.coh`.
- `X.So.hostVanE` gives `HostVanE` from Lemma K, and `X.xpp` gives `HostXpp`.
- `hostRigidUE_alt` and `hostNumberUE_alt` give `HostRigid_s` and `HostNumber_s` from `unlEnd3E (linkedUnlE_alt hH)`.

## In the Lean code

The theorem is in [LinkedUnlE.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/LinkedUnlE.lean#L55), and `unitary_lift_of_reduced_core` in [UnitaryLiftTheoremOfReducedForm.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/UnitaryLiftTheoremOfReducedForm.lean#L26). We have not opened `hostVanE`, `xpp`, `hostRigidUE_alt` or `hostNumberUE_alt`.

"Bound K" in the name is Lemma K. [The case I count](/entry/count-i-of-printed-bound-k-kato-automorphy/) in the same file computes `unlEnd3E (linkedUnlE_alt hH)` again.
