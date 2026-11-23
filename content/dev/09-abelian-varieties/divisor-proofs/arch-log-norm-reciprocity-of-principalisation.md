---
id: arch-log-norm-reciprocity-of-principalisation
title: Archimedean reciprocity from principalisation (statement form)
kind: theorem
decl: GlobalTheory.T.archLogNormReciprocity_of_principalisation
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ArchLogNormReciprocityOfPrincipalisationStatement
covers: 406
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`MixHt.archRecip_of_principalisation`](/entry/arch-recip-of-principalisation/), which has the proof. Its one user is [the proof of the rules of arithmetic intersection](/entry/ar-calc-of-principalisation/), which gives it, together with an integrability statement, to the lemma that builds the intersection functionals.

## Statement

Let $\mathrm{Princ}$ be principalisation of ideals in characteristic $0$, as in [the entry on the Hilbert-Samuel formula](/entry/arith-hilbert-samuel-of-principalisation/). Let $\mathrm{ArchRecip}$ be the reciprocity law for the archimedean terms of two sections $s$, $t$ with no common divisor, stated in full in [the entry with the proof](/entry/arch-recip-of-principalisation/).

**Theorem.** $\mathrm{Princ}$ implies $\mathrm{ArchRecip}$.

## Proof

The statement is the same as that of `GlobalTheory.MixHt.archRecip_of_principalisation`, and the proof applies it.

## In the Lean code

The theorem is in [ArchLogNormReciprocityOfPrincipalisationStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ArchLogNormReciprocityOfPrincipalisationStatement.lean#L16). The proof is `first | exact @GlobalTheory.MixHt.archRecip_of_principalisation | ...`, a tactic that tries the alias in three forms. The type is the same as that of the theorem it calls. The file imports `Mathlib` twice.
