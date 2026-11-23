---
id: local-theory-of-admitted
title: The local theory from the admitted conditions
kind: theorem
decl: Formalism.MainNotions.LiftingTheory.local_theory_of_admitted
module: Formalism.SharpRestriction.LevelLetterCocycles.BaseChangePreservesUnitaryOf
covers: 539
status: drafted
drafted_by: writer@claude
---
This theorem proves the eight local statements `aux₃` with the constants $10, 23, 32, 32$ from the 23 admitted conditions. Its only caller is [the local lifting statements from the admitted conditions](/entry/frobenius-lifting/). The proof is an assembly of two lemmas, `local_parts_of_admitted` and `lifting_all_parts_of_admitted`. These two lemmas are not in the outline.

## Statement

The data `D`, `HW`, `F`, `Cm` and the condition `admitted` are as in [the parent entry](/entry/frobenius-lifting/). For each prime $\ell$, all finite extensions $K, L$ of $\mathbb{Q}_\ell$ and each $s$ with `Good K s LL`, let $W$ be the object `(HW l).W K s LL h`.

**Theorem.** If `admitted D HW F Cm` holds, then `aux₃ D HW F 10 23 32 32` holds. This is the conjunction of:

1. `ConclusionL`: `coreL` for each $W$;
2. `ConclusionW`: four statements `WachKillsQuotients`, `WachKillsCaseB`, `WachKillsCaseA` and `WachKillsIntermediateField`;
3. `WachAnnihilatorAll` and `WachExponentRecursionAll`;
4. `WachResultConstant 10`: `coreWR` for each $W$ with the constant $10$;
5. `ConclusionH` and `ExistsUnitClasses`: `coreH` and `coreTr` for each $W$;
6. `LiftTheoremAllCases 23 32 32`: the lifting theorem in case A and in case B, `LiftBracketR`, `LiftExponentShapes 23 32 32` and `LiftGaloisDescent`.

We have not unfolded the predicates `coreL`, `coreWR`, `coreH`, `coreTr` and the `coreLift` predicates.

## Proof

1. `local_parts_of_admitted` gives the first seven statements and two more. `lattice_clause_every_situation` proves `ConclusionL` with no hypothesis. `wach_statement_of_admitted` and `wach_first_clause_of_admitted` take all of `admitted`. `opnJumpsQuot_holds` uses `adm22` and `adm23`, and `wach_second_and_result_of_admitted` then gives the exponent recursion and the constant $10$. `gamma_equation_clause_of_uniformizer` and `truncation_of_uniformizer_clause` use only `adm9`. The last two items, `LiftBracketR` and `LiftExponentShapes`, are dropped.
2. `lifting_all_parts_of_admitted` gives the eighth statement. Case B comes from `lifting_case_B_of_hypotheses` with `wach_statement_case_B` (`adm2`, `adm16`). Case A comes from `lifting_case_A_of_admitted` with `wach_statement_case_A` (`adm9`, `adm16`). `lifting_descent_to_subfields` takes both cases and `adm20`. `lifting_bracket_units_times_powers` and `lifting_exponent_shapes` take no hypothesis.

## In the Lean code

The theorem is in [BaseChangePreservesUnitaryOf.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/BaseChangePreservesUnitaryOf.lean#L4837), with `local_parts_of_admitted` at line 4827 and `lifting_all_parts_of_admitted` at line 4818. The statements are in [LiftingTheory.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/LiftingTheory.lean#L589). We have not read the proofs of the lemmas in step 1 and step 2.

`LiftBracketR` and `LiftExponentShapes` are proved twice: once in `local_parts_of_admitted`, where they are dropped, and once in `lifting_all_parts_of_admitted`. The lifting step does not use `adm3`, `adm4` (`ArchimedeanSignatureMatching`), `adm7`, `adm8`, `adm10` or `adm12`; the Wach lemmas in step 1 take all of `admitted`, so we cannot say if these six are used. The namespace `CrystallineLiftingBounds` in the same file has a second `local_theory_of_admitted` at line 4856, with three constants.
