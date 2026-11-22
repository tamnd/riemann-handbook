---
id: u-st-b
title: The separation statement (second name)
kind: theorem
decl: GlobalTheory.UPoincTop.uStB
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.UnitaryToroidalSeparationOfBase
covers: 1390
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement `UStB`. It is the theorem [the normalized blowup with separation](/entry/u-poin-st-x-sep/) under the name of its statement, and that entry has the content. [The citation in the statement file](/entry/unitary-toroidal-separation-of-base/) passes it on to [rigid boundary charts for a fan](/entry/rigid-for-fan-holds/). Below it are 1,390 declarations of the proof.

## Statement

`UStB` holds. This is the statement of [the normalized blowup with separation](/entry/u-poin-st-x-sep/), word for word: the projective normal compactification $Z$ of $X_F$, the normalized blowup $\pi \colon S \to Z$ along a boundary ideal, the open immersion $j \colon X_F \to S$, the conditions `UPoinOnX`, and the separation property `SepB` of $j$.

## Proof

The proof term is `uPoinStX_sep`. The type of `uPoinStX_sep` is the body of the definition of `UStB`, so Lean accepts the term after it unfolds `UStB`. There is nothing more.

## In the Lean code

The theorem is at [UnitaryToroidalSeparationOfBase.lean#L90](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UnitaryToroidalSeparationOfBase.lean#L90), in the same file as `uPoinStX_sep` (line 23). The definition `UStB` is in [FromBaseAlt.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/FromBaseAlt.lean#L57). Its first part, `UPoinOnX`, is the body of the definition `UPoinStX` in [SpecializesGenericImage.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/SpecializesGenericImage.lean#L168). So `UStB` is `UPoinStX` with the clause `SepB` added inside the existential. The name `uPoinStX_sep` says this.
