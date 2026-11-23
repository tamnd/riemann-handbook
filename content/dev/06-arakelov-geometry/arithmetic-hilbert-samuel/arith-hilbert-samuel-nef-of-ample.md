---
id: arith-hilbert-samuel-nef-of-ample
title: From the ample case to the nef Hilbert-Samuel formula (statement form)
kind: theorem
decl: GlobalTheory.T.arithHilbertSamuel_nef_of_ample
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ArithHilbertSamuelNefOfAmpleStatement
covers: 347
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`HSNef.arithHilbertSamuel_of_ampleHS`](/entry/arith-hilbert-samuel-of-ample-hs/), which has the proof. Its one user is [the arithmetic Hilbert-Samuel formula from principalisation](/entry/arith-hilbert-samuel-of-principalisation/), which gives it the three statements that it proves from principalisation.

## Statement

Use the statements of [the parent entry](/entry/arith-hilbert-samuel-of-principalisation/): $\mathrm{ArCalc}$, the rules of [arithmetic intersection](/entry/ar-calc-of-principalisation/); $\mathrm{AmpleHS}$, the counting limit for [ample bundles with a semipositive metric](/entry/ample-hs-of-principalisation/); $\mathrm{SemiPull}$, the statement that the pull-back of a semipositive hermitian line bundle is semipositive; and $\mathrm{ArithHilbertSamuel}$, the formula $\log \# \widehat{H}^0(\overline{L}^m \otimes \overline{N}) = \frac{a}{(D+1)!} m^{D+1} + o(m^{D+1})$ for a nef $\overline{L}$ with self-intersection $a$.

**Theorem.** $\mathrm{ArCalc}$, $\mathrm{AmpleHS}$ and $\mathrm{SemiPull}$ imply $\mathrm{ArithHilbertSamuel}$.

## Proof

The statement is the same as that of `GlobalTheory.HSNef.arithHilbertSamuel_of_ampleHS`, and the proof applies it. The parent entry outlines that proof: finiteness of the small sections, an upper bound from all three statements and a lower bound from $\mathrm{ArCalc}$ and $\mathrm{AmpleHS}$.

## In the Lean code

The theorem is in [ArithHilbertSamuelNefOfAmpleStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ArithHilbertSamuelNefOfAmpleStatement.lean#L10). The proof is `first | exact @GlobalTheory.HSNef.arithHilbertSamuel_of_ampleHS | ...`, a tactic that tries the alias in three forms. The type is the same as that of the theorem it calls, in [ArithHilbertSamuelNefOfAmple.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ArithHilbertSamuelNefOfAmple.lean#L16).
