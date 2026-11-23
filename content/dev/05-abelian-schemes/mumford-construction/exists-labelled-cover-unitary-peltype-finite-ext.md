---
id: exists-labelled-cover-unitary-peltype-finite-ext
title: Degeneration data of unitary PEL type have a labelled cover after a finite extension (statement)
kind: theorem
decl: GlobalTheory.T.exists_labelledCover_unitaryPELType_finiteExt
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsLabelledCoverUnitaryPELTypeFiniteExtStatement
covers: 425
status: drafted
drafted_by: writer@claude
---
This theorem is a restatement of [`Mum.exists_labCover_of_pelOK`](/entry/exists-lab-cover-of-pel-ok/), which has the real content. Its proof only calls that theorem. It is used once, in step 3 of [`Mum.has_of_base`](/entry/has-of-base/).

## Statement

Let $R$ be a local domain with `Base R` (noetherian, integrally closed, complete, characteristic zero). Let $E$ be a CM field with a host datum $H$ (`Host`) and a PEL datum `Dm : Datum H`. Let $D$ be degeneration data over $R$ whose lattice $X$ is a nonzero $\mathcal{O}_E$-module, with an action $o$ of $\mathcal{O}_E$ on $D$, such that `PelOK Dm D o` holds. The [entry for `exists_labCover_of_pelOK`](/entry/exists-lab-cover-of-pel-ok/) unfolds `Host`, `Datum` and `PelOK`.

**Theorem.** There are a local domain $R'$, a finite injective map $\rho \colon R \to R'$ with $R'$ again noetherian, normal and complete (`FinExt ρ`), and data $D'$ over $R'$ that are a pullback of $D$, such that $D'$ has a labelled cover (`LabCover D'`).

The [entry for `hasFin_of_labCover`](/entry/has-fin-of-lab-cover/) unfolds `LabCover`.

## Proof

The proof is `Mum.exists_labCover_of_pelOK`.

## In the Lean code

The theorem is in [ExistsLabelledCoverUnitaryPELTypeFiniteExtStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsLabelledCoverUnitaryPELTypeFiniteExtStatement.lean#L12). The proof is the tactic `first | exact @GlobalTheory.Mum.exists_labCover_of_pelOK | ...`. The two statements are identical, so `exact` with that theorem closes the goal.
