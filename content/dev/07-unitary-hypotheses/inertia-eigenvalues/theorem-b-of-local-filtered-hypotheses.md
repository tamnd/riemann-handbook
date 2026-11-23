---
id: theorem-b-of-local-filtered-hypotheses
title: Local lifting theorem B from the Fontaine and jump conditions (second name)
kind: theorem
decl: GlobalTheory.T.theoremB_of_localFilteredHypotheses
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.TheoremBOfLocalFilteredHypothesesStatement
covers: 866
status: drafted
drafted_by: writer@claude
---
This theorem is a second name of [`theoremB_of_admitted_inputs`](/entry/theorem-b-of-admitted-inputs/). It is step 4 of [local lifting theorem B](/entry/theorem-b-closing/). The proof is a chain of second names, and the mathematics is in [`thmB_at`](/entry/thm-b-at/). Below this theorem are 866 declarations of the proof.

## Statement

Use the notation of [local lifting theorem B](/entry/theorem-b-closing/): a datum $D$, Wach modules $HW$, Fontaine data $F$ and comparison data $C_m$.

**Theorem.** Let $C, C_R, C_A, C_B, C_K, C_\kappa$ be reals with $C \ge 320$. Assume `adm22` (the Fontaine inequality at each $\ell, K, L$), `adm23` (the jump condition at each $\ell, K, L$) and `LetterConditionGlobal`. Then the 13 conditions `admitted` with the constants $C_R, C_A, C_B, C_K, C_\kappa$ imply the bound `aux₃ D HW F C`, which is local lifting theorem B with the constant $C$.

## Proof

The proof is `exact @theoremB_of_admitted_inputs`. The chain below it is:

1. [`theoremB_of_admitted_inputs`](/entry/theorem-b-of-admitted-inputs/) calls [`frobenius_statement_of_fontaine`](/entry/frobenius-statement-of-fontaine/) with the same arguments.
2. `frobenius_statement_of_fontaine` calls [`stmt_holds`](/entry/stmt-holds/), with the arguments in another order.
3. `stmt_holds` takes the 13 conditions, regroups them with `admBoundsB_of_adm` and passes them to `frobenius_statement_of_inputs`.
4. `frobenius_statement_of_inputs` takes $\ell$, $K$ and $L$, gets $\ell \ge 11$ and calls [`thmB_at`](/entry/thm-b-at/).

## In the Lean code

The theorem is in [TheoremBOfLocalFilteredHypothesesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TheoremBOfLocalFilteredHypothesesStatement.lean#L10). Steps 2 to 4 are in [FrobeniusStatementOfFontaine.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/FrobeniusStatementOfFontaine.lean#L197).

- The name "local filtered hypotheses" names no object of the statement.
- The constants $C_R, C_A, C_B, C_K, C_\kappa$ and the data $C_m$ enter only through `admitted`. The bound `aux₃` does not depend on them.
