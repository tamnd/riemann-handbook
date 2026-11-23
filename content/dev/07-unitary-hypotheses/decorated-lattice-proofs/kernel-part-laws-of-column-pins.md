---
id: kernel-part-laws-of-column-pins
title: The kernel class datum of a pinned column is good, a second name
kind: theorem
decl: GlobalTheory.T.kernelPart_laws_of_columnPins
module: Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs.KernelPartLawsOfColumnPinsStatement
covers: 347
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`clsKL_is`](/entry/cls-kl-is/). It is step 3 of [class data from the column condition](/entry/cls-pin-d-of-fam-col-of-true-w/): for each index $t$, it proves that the kernel class datum `clsKL` built from a pinned column is good. The mathematics, and the full statement, are in [`clsKL_is`](/entry/cls-kl-is/).

## Statement

**Theorem.** Assume `I.Ok`, `TC.Pins`, `PinX` for the lattices and vacua of a geometry $g$ with constants $c_0$, `JetS` for jet scales $s$, and that each lattice datum $g.x_j$ with $j \le m$ satisfies `Is`. Let $A$ be a twist datum and $\iota$ a map from the column characters into the characters of $A$, with `PinChL R g k c₀ A ι w`. Then the kernel class datum `clsKL R g P r k tl s J A ι` satisfies `Is`.

The datum and the five conditions of `Is` are described in [`clsKL_is`](/entry/cls-kl-is/).

## Proof

The proof is one call to `KerLaws.clsKL_is`, with the same arguments in the same order. There is no other step.

## In the Lean code

The theorem is at [KernelPartLawsOfColumnPinsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/KernelPartLawsOfColumnPinsStatement.lean#L9). Its statement is the statement of `clsKL_is`, word for word. The "laws" of the name are the five conditions of `ClsK.Is`.
