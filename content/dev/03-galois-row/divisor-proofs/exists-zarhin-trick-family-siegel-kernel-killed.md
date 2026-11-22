---
id: exists-zarhin-trick-family-siegel-kernel-killed
title: Zarhin data for Siegel objects of kernel d (statement form)
kind: theorem
decl: GlobalTheory.T.exists_zarhinTrick_family_siegel_kernelKilled
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsZarhinTrickFamilySiegelKernelKilledStatement
covers: 353
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [the Zarhin data for Siegel objects of kernel $d$](/entry/exists-zarhin-data-sieg-ker-by/), which has the proof. Its one user is [the representability of Siegel moduli with kernel killed by $d$](/entry/sd-rep-of-coprime/), where it is step 1: each Siegel object of kernel $d$ becomes the $e$-part of a principal object of genus $8h$ with an action of an order.

## Statement

Let $h \geq 1$, $M \geq 3$ odd, $d \geq 1$ and $\gcd(M, d) = 1$. Then there are a ring $O$ with an additive map $a \mapsto \bar a$, a spanning family of $O$ with a positive relation, an idempotent $e \in O$, and integer data that link level structures of genus $h$ and $8h$, such that each Siegel object of kernel $d$ over a base on which $d$ is a unit is the $e$-part of a principal object of genus $8h$ with a compatible $O$-action, and this principal object is unique up to isomorphism. The full statement, with each clause, is in [the entry with the proof](/entry/exists-zarhin-data-sieg-ker-by/).

## Proof

The statement is the same as that of `GlobalTheory.UPel.HT.exists_zarhin_data_siegKerBy`, and the proof applies it.

## In the Lean code

The theorem is in [ExistsZarhinTrickFamilySiegelKernelKilledStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsZarhinTrickFamilySiegelKernelKilledStatement.lean#L7). The proof is `first | (exact @GlobalTheory.UPel.HT.exists_zarhin_data_siegKerBy) | ...`, a tactic that tries the alias in three forms. The name says "family", but the statement gives no family over a base: it gives a ring, an additive map on it, and a construction on objects.
