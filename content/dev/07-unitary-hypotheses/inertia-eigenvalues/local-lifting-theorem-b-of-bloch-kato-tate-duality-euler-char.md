---
id: local-lifting-theorem-b-of-bloch-kato-tate-duality-euler-char
title: Local lifting theorem B from three local Galois statements (renaming)
kind: theorem
decl: GlobalTheory.T.localLiftingTheoremB_of_blochKato_tateDuality_eulerChar
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.LocalLiftingTheoremBOfBlochKatoTateDualityEulerCStatement
covers: 1838
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [the closing of theorem B](/entry/theorem-b-closing/). That entry has the content. [The admissibility conditions at twisted inert primes](/entry/inert-step-main-alt-alt/) use it with $C = 320$, in the case where $\ell_i$ is not a row B prime.

## Statement

Assume three published statements: `BlochKatoLocal`, local Tate duality (`LocalTateDualityK`) and the local Euler characteristic formula (`LocalEulerCharK`). For local Tate duality and the Euler characteristic formula, see Serre, *Galois Cohomology*, Chapter II, Section 5.

**Theorem.** For each datum $D$, each choice of Wach modules $HW$, Fontaine data $F$ and comparison data $C_m$, and each real $C \ge 320$, the local lifting bound `ArcLiftingSetup.aux₃ D HW F C` holds.

The bound is local lifting theorem B at each prime $\ell$. It is stated in full in [the closing of theorem B](/entry/theorem-b-closing/).

## Proof

The proof is `exact @GlobalTheory.theoremB_closing`. The statement is the same, with the same hypotheses in the same order.

## In the Lean code

The theorem is in [LocalLiftingTheoremBOfBlochKatoTateDualityEulerCStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocalLiftingTheoremBOfBlochKatoTateDualityEulerCStatement.lean#L8). Its proof is the tactic `first | exact @X | exact X | (intros; apply X <;> assumption)` with `X = theoremB_closing`. Each branch uses only `theoremB_closing`, so the theorem gives a second name to it and adds nothing.

The data $C_m$ do not appear in the conclusion. The quantifier over $C_m$ is harmless but has no use.
