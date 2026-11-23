---
id: theorem-b-of-admitted-inputs
title: Local lifting theorem B from the admitted conditions, a second name
kind: theorem
decl: GlobalTheory.theoremB_of_admitted_inputs
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.TheoremBOfLocalFilteredHypotheses
covers: 864
status: drafted
drafted_by: writer@claude
---
This theorem is a second name. It is the proof of [`theoremB_of_localFilteredHypotheses`](/entry/theorem-b-of-local-filtered-hypotheses/), which is step 4 of [local lifting theorem B](/entry/theorem-b-closing/). Its proof is one call to [`frobenius_statement_of_fontaine`](/entry/frobenius-statement-of-fontaine/), which is again one call to [`stmt_holds`](/entry/stmt-holds/). The mathematics is below `stmt_holds`, in [`thmB_at`](/entry/thm-b-at/).

## Statement

Use the notation of [local lifting theorem B](/entry/theorem-b-closing/): a datum $D$, Wach modules $HW$, Fontaine data $F$ and comparison data $C_m$.

**Theorem.** Let $C, C_R, C_A, C_B, C_K, C_\kappa$ be reals with $C \ge 320$. Assume:

1. `adm22`: the Fontaine inequality `FontaineLe` holds at each prime $\ell$ and each pair $K, L$ of finite extensions of $\mathbb{Q}_\ell$;
2. `adm23`: the jump condition `coreJumps` holds at each $\ell, K, L$;
3. the global letter condition `LetterConditionGlobal`.

Then the 13 conditions `admitted` with the constants $(C_R, C_A, C_B, C_K, C_\kappa)$ imply local lifting theorem B with the constant $C$.

## Proof

The proof passes all arguments to `frobenius_statement_of_fontaine`. There is no other step.

## In the Lean code

The theorem is in [TheoremBOfLocalFilteredHypotheses.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TheoremBOfLocalFilteredHypotheses.lean#L12). The conclusion is `ArcLiftingSetup.Stmt` in [ArcLiftingSetup.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/ArcLiftingSetup.lean#L532), which is `admitted D HW F Cm CR CA CB CK Ckap → aux₃ D HW F C`. The callee is in [FrobeniusStatementOfFontaine.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/FrobeniusStatementOfFontaine.lean#L218).

- The name says "of admitted inputs", but `admitted` is not a hypothesis of the theorem. It is the premise of the implication in the conclusion.
- The five constants $C_R, \dots, C_\kappa$ occur only in `admitted`. The bound `aux₃` does not depend on them.
- The chain `T.theoremB_of_localFilteredHypotheses`, `theoremB_of_admitted_inputs`, `frobenius_statement_of_fontaine` has three names for one statement.
