---
id: quotient-bound-of-kill-detect-constant-room
title: The quotient index bound from killing, detection and room (statement form)
kind: theorem
decl: GlobalTheory.T.quotientBound_of_kill_detect_constantRoom
module: Development.AbelianVarietyTheory.Proofs.ThetaShiftProofs.QuotientBoundOfKillDetectConstantRoomStatement
covers: 812
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`qat_of_kill_detect`](/entry/qat-of-kill-detect/), which has the real content. Its one user is [`qAt_run`](/entry/q-at-run/), which calls it once with fixed constants to get the quotient index bound `QAt`.

## Statement

Use $K$, $S_\kappa$, $M_\kappa$, $\mathcal{K}$, $P(C, A)$ and the bound `QAt` from [the entry for `qAt_run`](/entry/q-at-run/), for the provider `recB h` of a record $T$ with `h : LawsCore T`.

**Theorem.** Assume `Known`. Let $j \in [1, m)$, let $\kappa$ be a weight, and let $C_R, T_t, c, C_k, C_h, A_h, C_0, A_0, C_d, A_d$ be real numbers. Suppose that `GamAt T` holds, $M_\kappa$ is a lattice, `KillQ` and `DetectQ` hold (the functionals of the CM arc family vanish on $\mathcal{K}$ and detect it), $z \ge 1$, $C_0 \ge 0$, $C_d \ge 0$, `RoomAt` holds with $(C_0, A_0)$, and $\log \dim_K S_\kappa \le P(C_d, A_d) |\kappa|$. Then `QAt` holds with $C_c = C_h + 3C_0 + C_d$ and $A_c = \max(A_h, A_0, A_d)$.

[The entry for `qat_of_kill_detect`](/entry/qat-of-kill-detect/) defines `KillQ`, `DetectQ` and `RoomAt`.

## Proof

The statement is the same as that of `GlobalTheory.ArcCM.qat_of_kill_detect`, and the proof applies it.

## In the Lean code

The theorem is in [QuotientBoundOfKillDetectConstantRoomStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/QuotientBoundOfKillDetectConstantRoomStatement.lean#L9). The proof is `first | exact @GlobalTheory.ArcCM.qat_of_kill_detect | ...`, a tactic that tries the alias in three forms. "Constant room" in the name refers to the hypothesis `RoomAt`.
