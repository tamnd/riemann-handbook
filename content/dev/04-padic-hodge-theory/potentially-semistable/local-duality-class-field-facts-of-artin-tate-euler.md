---
id: local-duality-class-field-facts-of-artin-tate-euler
title: Thirteen facts of class field theory and local duality, a second name
kind: theorem
decl: GlobalTheory.T.local_duality_class_field_facts_of_artin_tate_euler
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.LocalDualityClassFieldFactsOfArtinTateEulerStatement
covers: 382
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the thirteen facts from Artin reciprocity, Tate duality and the Euler characteristic](/entry/lang-rec-core-of-artin-reciprocity/). That entry has the content. Its user is [the Selmer bound at a point](/entry/selmer-bound-at-point-main/), which applies it in step 1 of its proof to get the instance `T2.Core`.

## Statement

**Theorem.** Assume global Artin reciprocity (`GlobalArtinReciprocity`), local Tate duality (`LocalTateDualityK`) and Tate's local Euler characteristic formula (`LocalEulerCharK`). Then `T2.Core` holds.

`T2.Core` is a list of thirteen statements of local and global Galois cohomology. They are described in [the entry with the content](/entry/lang-rec-core-of-artin-reciprocity/).

## Proof

The proof applies `GlobalTheory.langRecCore_of_artinReciprocity`, which has the same statement. Nothing else happens.

## In the Lean code

The theorem is in [LocalDualityClassFieldFactsOfArtinTateEulerStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocalDualityClassFieldFactsOfArtinTateEulerStatement.lean#L8). The proof is a `first | exact ... | ...` combinator with three tries. Each try applies the same lemma. The file has `set_option maxHeartbeats 1000000` (line 7), which a one-line proof does not need. The file is named as a statement file, but it imports the proof module (line 2) and only renames it.
