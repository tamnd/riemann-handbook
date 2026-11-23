---
id: exists-hw-of-fon-of-cmp-of-prime
title: Statement of the Wach and étale families at every prime
kind: theorem
decl: GlobalTheory.T.exists_hwOf_fonOf_cmpOf'
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.ExistsHwOfFonOfCmpOfStatement
covers: 405
status: drafted
drafted_by: writer@claude
---
This theorem is a second name. It has the same statement as [the theorem with the content](/entry/exists-hw-of-fon-of-cmp-of/), and its proof only points to that theorem. [The Bhatt-Scholze assembly](/entry/exists-hw-fon-cmp-ties/) calls it under this name.

## Statement

Let $L$ be a local theory and $A$ an $A_{\mathrm{inf}}$ datum at each prime $l$. Assume two things at every $l$:

1. `LocTied`: the abstract period rings of $L$ are isomorphic to $B_{\mathrm{cris}}$ and $B_{\mathrm{dR}}$, compatibly with their structure.
2. `WachEx`: every étale layer of $A$ has a Wach lattice.

**Theorem.** There are a family $H$ of Wach modules at every prime (`HWOf L`), a family $F$ of étale modules over it (`FonOf L A H`), and a comparison between them (`CmpOf L A H F`).

## Proof

The proof is the tactic `first | exact @GlobalTheory.HWL.exists_hwOf_fonOf_cmpOf | ...`. The first branch closes the goal: the two statements are the same term. No mathematics happens here.

## In the Lean code

The theorem is at [ExistsHwOfFonOfCmpOfStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsHwOfFonOfCmpOfStatement.lean#L7). The target is at [ExistsHwOfFonOfCmpOf.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsHwOfFonOfCmpOf.lean#L10). The size of this entry, 405, is one more than the size of the target, 404. `WachEx` is in [ConvZero.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/ConvZero.lean#L29).
