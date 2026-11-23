---
id: theorem-c-of-admitted-inputs
title: Theorem C with constant 25, from admitted inputs (renaming)
kind: theorem
decl: GlobalTheory.theoremC_of_admitted_inputs
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.TheoremCConst25OfHypotheses
covers: 1284
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [the theorem from literature hypotheses](/entry/theorem-of-literature-hypotheses/), which has the content. Its only user is the renaming [`ramified_coefficient_chains_of_hypotheses`](/entry/ramified-coefficient-chains-of-hypotheses/), and through it [the ramified coefficient bound with constant 25](/entry/ramified-coefficient-chains-prv-twenty-five/).

## Statement

The statement is that of [`ramified_coefficient_chains_of_hypotheses`](/entry/ramified-coefficient-chains-of-hypotheses/). Let $D$, $HW$, $F$, $C_m$ and reals $C_R, C_A, C_B, C_K$ be given. Assume the five local conditions `adm23`, `LetterConditionGlobal`, `HerrClassNaturalExtension`, `adm22` and `LitFont`.

**Theorem.** If the 19 admitted conditions hold with the constants $(C_R, C_A, C_B, C_K)$, then the ramified coefficient bound (local lifting theorem C) holds with $C = 25$.

## Proof

The proof is one term:

```
Formalism.MainNotions.RamifiedCoefficientChains.Asm.theorem_of_literature_hypotheses D HW F Cm CR CA CB CK h23 hC4 hHerr a22 hFont
```

It passes all arguments, in order, to a theorem with the same statement.

## In the Lean code

The theorem is in [TheoremCConst25OfHypotheses.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TheoremCConst25OfHypotheses.lean#L14). The theorem it calls is in [FrobeniusLiftLemmasOfAdmitted.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/FrobeniusLiftLemmasOfAdmitted.lean#L292). There, the proof calls `theorem_of_local_lemmas` with `local_lemmas_of_literature`. That proof uses the Herr class condition, `adm22` and `LitFont` only through `local_lemmas_of_literature`.

So three theorems have one statement: this one, its renaming `ramified_coefficient_chains_of_hypotheses`, and `theorem_of_literature_hypotheses`.

The condition `adm23` here is `LiftingTheory.adm23`. The file [CrystallineLiftingBounds.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/CrystallineLiftingBounds.lean#L109) has a second `adm23` with the same body, and the same holds for `adm22`. The lemma `jumps_exact_adm` proves both copies of `adm23`.
