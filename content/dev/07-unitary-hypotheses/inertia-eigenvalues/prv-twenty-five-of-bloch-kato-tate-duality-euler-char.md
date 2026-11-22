---
id: prv-twenty-five-of-bloch-kato-tate-duality-euler-char
title: The ramified coefficient bound with constant 25, from three local Galois statements (renaming)
kind: theorem
decl: GlobalTheory.T.prv_twenty_five_of_blochKato_tateDuality_eulerChar
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.RamifiedCoefficientChainsPrvTwentyFiveStatement
covers: 1336
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [the ramified coefficient bound with constant 25](/entry/ramified-coefficient-chains-prv-twenty-five/). That entry has the content. [The admissibility conditions at twisted inert primes](/entry/inert-step-main-alt-alt/) use it, together with local lifting theorem B at 320, in the case where $\ell_i$ is not a row B prime.

## Statement

Assume three published statements: `BlochKatoLocal`, local Tate duality (`LocalTateDualityK`) and the local Euler characteristic formula (`LocalEulerCharK`). For the last two, see Serre, *Galois Cohomology*, Chapter II, Section 5.

**Theorem.** For each datum $D$, each choice of Wach modules $HW$, Fontaine data $F$ and comparison data $C_m$, the bound `RamifiedCoefficientChains.aux₃ D HW F 25` holds.

This is a local bound on the cokernel length of a map of lattices, at each prime $\ell$ and each good pair of local fields, with the constants $(32, 4, 10, 4, 3/2)$ and $C = 25$. It is stated in full in [the ramified coefficient bound](/entry/ramified-coefficient-chains-prv-twenty-five/).

## Proof

The proof is `exact @GlobalTheory.ramifiedCoefficientChains_prv_twenty_five`. The statement is the same, with the same hypotheses in the same order.

## In the Lean code

The theorem is in [RamifiedCoefficientChainsPrvTwentyFiveStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/RamifiedCoefficientChainsPrvTwentyFiveStatement.lean#L8). Its proof is the tactic `first | exact @X | exact X | (intros; apply X <;> assumption)` with `X = ramifiedCoefficientChains_prv_twenty_five`. Each branch uses only that theorem, so this theorem gives a second name to it and adds nothing.

The name says "prv twenty five". The 25 is the constant $C$ in the bound; the letters "prv" are not explained in the file. The data $C_m$ do not appear in the conclusion.
