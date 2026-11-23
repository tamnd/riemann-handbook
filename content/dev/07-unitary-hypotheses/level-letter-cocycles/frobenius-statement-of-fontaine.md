---
id: frobenius-statement-of-fontaine
title: Local lifting theorem B from the Fontaine inequality, a second name
kind: theorem
decl: Formalism.MainNotions.N.Ln17.frobenius_statement_of_fontaine
module: Formalism.SharpRestriction.LevelLetterCocycles.FrobeniusStatementOfFontaine
covers: 863
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`stmt_holds`](/entry/stmt-holds/), with the arguments in another order. Its only user is [`theoremB_of_admitted_inputs`](/entry/theorem-b-of-admitted-inputs/), which is itself a second name used in [local lifting theorem B](/entry/theorem-b-closing/). The mathematics is below `stmt_holds`, in [`thmB_at`](/entry/thm-b-at/).

## Statement

Use the notation of [local lifting theorem B](/entry/theorem-b-closing/): a datum $D$, Wach modules $HW$, Fontaine data $F$ and comparison data $C_m$.

**Theorem.** Let $C, C_R, C_A, C_B, C_K, C_\kappa$ be reals with $C \ge 320$. Assume:

1. `adm22`: `FontaineLe` holds for the period data of $D$ at each prime $\ell$ and each pair $K, L$ of finite extensions of $\mathbb{Q}_\ell$;
2. `adm23`: `coreJumps` holds at each $\ell, K, L$;
3. `LetterConditionGlobal`.

Then `ArcLiftingSetup.Stmt` holds: the 13 conditions `admitted` with the constants $(C_R, C_A, C_B, C_K, C_\kappa)$ imply the bound `aux₃` with the constant $C$.

## Proof

The proof is one call to `stmt_holds`. There is no other step.

## In the Lean code

The theorem is at [FrobeniusStatementOfFontaine.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/FrobeniusStatementOfFontaine.lean#L218). `stmt_holds` is in the same file, at line 211. It takes $C$ after `adm22`, `adm23` and `LetterConditionGlobal`, and states the bound on $C$ as $C_0 \le C$ with $C_0 = 320$ (line 17). This theorem writes $320 \le C$ directly. The two statements are the same up to the order of the arguments. `Stmt` and `admitted` are in [ArcLiftingSetup.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/ArcLiftingSetup.lean#L532), `adm22` and `adm23` in [CrystallineLiftingBounds.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/CrystallineLiftingBounds.lean#L106).

- The name says "of Fontaine". Of the three hypotheses, only `adm22` is about the Fontaine inequality. We have not unfolded `aux₃`.
- The chain `T.theoremB_of_localFilteredHypotheses`, `theoremB_of_admitted_inputs`, `frobenius_statement_of_fontaine`, `stmt_holds` gives four names to one statement.
- The constants $C_R, \dots, C_\kappa$ occur only in `admitted`.
