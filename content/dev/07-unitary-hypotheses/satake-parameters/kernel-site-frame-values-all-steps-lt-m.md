---
id: kernel-site-frame-values-all-steps-lt-m
title: The kernel difference at every level below the top, restated
kind: theorem
decl: GlobalTheory.T.kernelSite_frameValues_all_steps_lt_m
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.KernelSiteFrameValuesAllStepsLtMStatement
covers: 587
status: drafted
drafted_by: writer@claude
---
This theorem is a restatement. Its statement is the statement of `tieDel_all_steps`, and its proof only calls that theorem. The content is in [the kernel difference at every level below the top](/entry/tie-del-all-steps/). Its two users, `del_zero` and `del_of_pos`, specialize it to $j = 0$ and to $j \ge 1$ for [the pending system is admitted at each joint site](/entry/admissible-at-each-site/).

## Statement

Let $S$ be a joint site (`Joint.At`) for a joint $J$ and a standard choice `std` at $w$, as in [the pending system is admitted at each joint site](/entry/admissible-at-each-site/). Let $m$ be the top level `D.R.m`.

**Theorem.** If the dictionary `J.Dict std` holds and the site satisfies `Pair`, `Pos` and `Law`, then `S.Del j` holds for each $j < m$.

`S.Del j` says that for each ring homomorphism $\iota \colon \mathbb{C} \to \mathbb{C}_p$ that agrees with $\lambda$ on $\overline{\mathbb{Q}}$, the kernel difference at level $j$ holds with a constant $c_K \in \mathbb{C}_p$ of norm $1$. [The kernel difference at every level below the top](/entry/tie-del-all-steps/) states it in full.

## Proof

The proof is `tieDel_all_steps`. The tactic tries three forms of the same call.

## In the Lean code

The theorem is in [KernelSiteFrameValuesAllStepsLtMStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/KernelSiteFrameValuesAllStepsLtMStatement.lean#L9), under `set_option maxHeartbeats 1000000`. `tieDel_all_steps` is in [KernelSiteFrameValuesAllStepsLtM.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/KernelSiteFrameValuesAllStepsLtM.lean#L23).

`del_zero` ([KernelSiteFrameValuesStepZero.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/KernelSiteFrameValuesStepZero.lean#L10)) applies this theorem at $j = 0$, with $0 < m$ from `TwU.m_eq`, and `del_of_pos` ([KernelSiteFrameValuesPositiveSteps.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/KernelSiteFrameValuesPositiveSteps.lean#L10)) applies it at $j \ge 1$ and does not use $j \ge 1$. So the split into $j = 0$ and $j > 0$ is not needed.
