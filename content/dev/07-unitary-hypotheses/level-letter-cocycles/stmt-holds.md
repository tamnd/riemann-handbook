---
id: stmt-holds
title: Local lifting theorem B from the admitted conditions, the unpacking step
kind: theorem
decl: Formalism.MainNotions.N.Ln17.stmt_holds
module: Formalism.SharpRestriction.LevelLetterCocycles.FrobeniusStatementOfFontaine
covers: 862
status: drafted
drafted_by: writer@claude
---
This theorem is a pass-through. It is the proof of [`frobenius_statement_of_fontaine`](/entry/frobenius-statement-of-fontaine/), a second name below [`theoremB_of_admitted_inputs`](/entry/theorem-b-of-admitted-inputs/). It takes the 13 admitted conditions apart and hands the pieces to [`frobenius_statement_of_inputs`](/entry/frobenius-statement-of-inputs/). The mathematics is in [`thmB_at`](/entry/thm-b-at/).

## Statement

Use the notation of [local lifting theorem B](/entry/theorem-b-closing/).

**Theorem.** Assume `adm22` (a Fontaine inequality), `adm23` (a jump condition) and the global letter condition `LetterConditionGlobal`. Let $C \ge 320$ and let $C_R, C_A, C_B, C_K, C_\kappa$ be reals. If the conditions `admitted` hold with the constants $(C_R, C_A, C_B, C_K, C_\kappa)$, then local lifting theorem B holds with the constant $C$.

## Proof

Assume `admitted`. The lemma `admBoundsB_of_adm` picks 17 pieces out of it and puts them in the record `AdmBoundsB`. It passes them, with `adm22`, `adm23` and the letter condition, to `frobenius_statement_of_inputs`.

## In the Lean code

The theorem is in [FrobeniusStatementOfFontaine.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/FrobeniusStatementOfFontaine.lean#L211). The record and `admBoundsB_of_adm` are in [AdmBoundsBOfAdm.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/AdmBoundsBOfAdm.lean#L67).

- `frobenius_statement_of_fontaine` ([line 218](lean:Formalism/SharpRestriction/LevelLetterCocycles/FrobeniusStatementOfFontaine.lean#L218)) has the same statement with the arguments reordered and $320$ in place of $C_0 = 320$.
- `admBoundsB_of_adm` drops `adm16`, three of the four parts of `adm1`, and three of the five parts of `adm8`. One of these is `KillerKap`, the only place where $C_\kappa$ occurs, so $C_\kappa$ plays no role.
- `stmtF_holds` in the same file also calls `stmt_holds`, once for each datum of a family.
