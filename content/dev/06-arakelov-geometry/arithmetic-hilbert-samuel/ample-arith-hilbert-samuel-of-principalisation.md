---
id: ample-arith-hilbert-samuel-of-principalisation
title: The ample Hilbert-Samuel limit from principalisation (statement form)
kind: theorem
decl: GlobalTheory.T.ampleArithHilbertSamuel_of_principalisation
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.AmpleArithHilbertSamuelOfPrincipalisationStatement
covers: 544
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`HSNef.ampleHS_of_principalisation`](/entry/ample-hs-of-principalisation/), which has the proof. Its one user is [the arithmetic Hilbert-Samuel formula from principalisation](/entry/arith-hilbert-samuel-of-principalisation/), which uses it as the ample case before it passes to nef bundles.

## Statement

Let $\mathrm{Princ}$ be principalisation of ideals in characteristic $0$, as in [the parent entry](/entry/arith-hilbert-samuel-of-principalisation/). Let $\mathrm{AmpleHS}$ be the statement: for an ample line bundle $L$ with a semipositive metric and self-intersection $a$ on an arithmetic variety of dimension $D+1$, the logarithm of the number of sections of $L^m \otimes A$ of sup norm at most $e^{tm}$, divided by $m^{D+1}$, tends to $(a + (D+1)\, t \deg L)/(D+1)!$ for all large $t$. It is stated in full in [the entry with the proof](/entry/ample-hs-of-principalisation/).

**Theorem.** $\mathrm{Princ}$ implies $\mathrm{AmpleHS}$.

## Proof

The statement is the same as that of `GlobalTheory.HSNef.ampleHS_of_principalisation`, and the proof applies it.

## In the Lean code

The theorem is in [AmpleArithHilbertSamuelOfPrincipalisationStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/AmpleArithHilbertSamuelOfPrincipalisationStatement.lean#L7). The proof is `first | exact @GlobalTheory.HSNef.ampleHS_of_principalisation | ...`, a tactic that tries the alias in three forms. The type is the same as that of the theorem it calls.
