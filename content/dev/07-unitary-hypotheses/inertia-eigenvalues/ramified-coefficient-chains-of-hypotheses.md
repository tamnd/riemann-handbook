---
id: ramified-coefficient-chains-of-hypotheses
title: The ramified coefficient bound from five local hypotheses (renaming)
kind: theorem
decl: GlobalTheory.T.ramified_coefficient_chains_of_hypotheses
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.TheoremCConst25OfHypothesesStatement
covers: 1286
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [`theoremC_of_admitted_inputs`](/entry/theorem-c-of-admitted-inputs/), which is itself a renaming of [the theorem from literature hypotheses](/entry/theorem-of-literature-hypotheses/). That last entry has the content. The user is [the ramified coefficient bound with constant 25](/entry/ramified-coefficient-chains-prv-twenty-five/).

## Statement

Let $D$ be a datum with Wach modules $HW$, Fontaine data $F$ and comparison data $C_m$, and let $C_R, C_A, C_B, C_K$ be reals. Assume five local conditions, each for all primes $\ell$ and finite extensions $K, L$ of $\mathbb{Q}_\ell$:

- `adm23`: the condition `coreJumps` on the period data;
- `LetterConditionGlobal`: the local letter condition for each Wach module;
- `HerrClassNaturalExtension`: naturality conditions on Herr classes of the Wach modules;
- `adm22`: the condition `FontaineLe`;
- `LitFont`: the condition `FontCore` for each Wach module in case A.

We have not unfolded `coreJumps`, `FontaineLe` or `FontCore`.

**Theorem.** If the 19 admitted conditions hold with the constants $(C_R, C_A, C_B, C_K)$, then the ramified coefficient bound holds with $C = 25$.

The bound is stated in full in [the ramified coefficient bound with constant 25](/entry/ramified-coefficient-chains-prv-twenty-five/).

## Proof

The proof is `exact @GlobalTheory.theoremC_of_admitted_inputs`. The statement is the same, with the same hypotheses in the same order.

## In the Lean code

The theorem is in [TheoremCConst25OfHypothesesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TheoremCConst25OfHypothesesStatement.lean#L12). Its proof is the tactic `first | exact @X | exact X | (intros; apply X <;> assumption)` with `X = theoremC_of_admitted_inputs`, so it adds nothing. The conclusion is `RamifiedCoefficientChains.Stmt D HW F Cm 25 CR CA CB CK`, that is `admitted` implies `aux₃` with $C = 25$.

The constants $C_R, C_A, C_B, C_K$ appear only in the premise `admitted`, not in the bound.
