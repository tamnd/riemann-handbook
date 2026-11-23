---
id: universal-general-statement-holds
title: The universal part in case A, with the inverse-level condition supplied
kind: theorem
decl: Formalism.MainNotions.UnusedSlot80.universal_general_statement_holds
module: Formalism.SharpRestriction.LevelLetterCocycles.UniversalGeneralStatementHolds
covers: 376
status: drafted
drafted_by: writer@claude
---
This theorem is a pass-through. It proves the universal part `adm14` in case A, which [`universalPart_caseA`](/entry/universal-part-case-a/) and [`crystallineUniversalPart_caseA`](/entry/crystalline-universal-part-case-a/) also state. Its only work is to supply one more hypothesis to the lemma that has the content.

## Statement

**Theorem.** Assume `AdmUnivA` (the saturation condition `adm5`, the killer condition at levels, the condition that $\gamma$ keeps the uniformizer, and the arc condition `adm12`), the lattice condition `P9`, the conclusion `ConclusionH`, and `adm15`. Then `UniversalComponentCaseA` holds. This is `adm14`.

## Proof

The lemma `invLevCore_fin` proves from `P9` the condition `InvLevCore` for the Wach module at each $(\ell, K, L)$ in case A with $\ell \ge 5$. It applies `InvW.invLevCore_L`, and at each triple it calls `InvW.levRat_of` with the ring condition `ring_condition_uniformizer_polynomial` and with `toolsAlg_at`. We have not unfolded `InvLevCore`. Then `universal_general_of_level_inverse` gives the result.

## In the Lean code

The theorem is in [UniversalGeneralStatementHolds.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/UniversalGeneralStatementHolds.lean#L38). `invLevCore_fin` is at [line 25](lean:Formalism/SharpRestriction/LevelLetterCocycles/UniversalGeneralStatementHolds.lean#L25).

- The namespace `UnusedSlot80` holds a theorem that is used.
- `toolsAlg_at` (line 12) has the same proof as `tool_algebra_of_ring_condition` in [LemmasUnramifiedOfRingCondition.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/LemmasUnramifiedOfRingCondition.lean#L338).
- `InvLevCore` in [KillWinFromCut.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/KillWinFromCut.lean#L33) has its own hypotheses: case A for the module ($K_0 \to K$ bijective, $s = 1$, $p \ne 2$) and $p \ge 5$. `AtCaseA` already assumes case A for $(K, L)$ and $\ell \ge 5$.
