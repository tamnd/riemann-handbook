---
id: key-rule-complex-existence-jets-key-value
title: The archimedean property of a key rule, second name
kind: theorem
decl: GlobalTheory.T.keyRule_complex_existence_jets_key_value
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.KeyRuleComplexExistenceJetsKeyValueStatement
covers: 466
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`ArchProof.arch_of_rule4`](/entry/arch-of-rule4/). It has no proof of its own. It is one of the results below [EveryCharacter from the literature and VWin](/step/every-character-of-literature/). Two proofs call it, in [KeyValueUniformisedFourierFrameAbsOne.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KeyValueUniformisedFourierFrameAbsOne.lean#L211) and [ExistsCExtComplex.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsCExtComplex.lean#L239). Both pass its result to `T.archimedeanExistence_of_complex_isomorphic_field`.

## Statement

Let $\kappa$ be a key rule: a function that gives a unit $\kappa(x) \in K^\times$ for each polarized abelian variety $x$ over a field $K$ of characteristic 0, with a rigidification, a theta section and a basis of the Lie algebra. If $\kappa$ satisfies the four conditions `Rule4` (homogeneity, base change, value $1$ on the classical theta function, values in units over normal Noetherian domains), then $\kappa$ satisfies `Arch`: the theta jets of a degenerating family converge near the boundary, and their values are those of a complex abelian variety whose key value is the key value of the abelian part. The entry [`arch_of_rule4`](/entry/arch-of-rule4/) states both conditions in full.

## Proof

The proof is one line: `exact @MBLow.ArchProof.arch_of_rule4`, inside a `first` combinator.

## In the Lean code

The theorem is at [KeyRuleComplexExistenceJetsKeyValueStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KeyRuleComplexExistenceJetsKeyValueStatement.lean#L12). Its statement is `∀ κ : Rule, Rule4 κ → Arch κ`. The name speaks of complex existence, jets and the key value, which are the three parts of the conclusion of `Arch`. The real content is in [`arch_of_rule4`](/entry/arch-of-rule4/).
