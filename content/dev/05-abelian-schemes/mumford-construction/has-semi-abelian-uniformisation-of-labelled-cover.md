---
id: has-semi-abelian-uniformisation-of-labelled-cover
title: A labelled cover gives a uniformisation after a finite extension (statement)
kind: theorem
decl: GlobalTheory.T.hasSemiAbelianUniformisation_of_labelledCover
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.HasSemiAbelianUniformisationOfLabelledCoverStatement
covers: 1085
status: drafted
drafted_by: writer@claude
---
This theorem is a restatement of [`Mum.hasFin_of_labCover`](/entry/has-fin-of-lab-cover/), which has the real content. Its proof only calls that theorem. It is used once, in step 4 of [`Mum.has_of_base`](/entry/has-of-base/), for degeneration data of unitary PEL type.

## Statement

Let $R$ be a local domain that is noetherian, integrally closed, complete for its maximal ideal $\mathfrak{m}$ and of characteristic zero (`Base R`). Let $D$ be degeneration data over $R$ for $\mathfrak{m}$. If $D$ has a labelled cover (`LabCover D`), then `HasFin D` holds: there are a finite injective extension $R \to R'$, with $R'$ again noetherian, normal and complete, and data $D'$ over $R'$ that are the pullback of $D$, such that $D'$ comes from a semi-abelian scheme with a uniformisation (`Has D'`).

The [entry for `hasFin_of_labCover`](/entry/has-fin-of-lab-cover/) unfolds `LabCover`, and the [entry for `has_of_base`](/entry/has-of-base/) unfolds `Has`.

## Proof

The proof is `Mum.hasFin_of_labCover`.

## In the Lean code

The theorem is in [HasSemiAbelianUniformisationOfLabelledCoverStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasSemiAbelianUniformisationOfLabelledCoverStatement.lean#L12). The proof is the tactic `first | exact @GlobalTheory.Mum.hasFin_of_labCover | ...`. The two statements are identical, so `exact` with that theorem closes the goal.
