---
id: unitary-toroidal-separation-of-base
title: The separation statement from the base (citation)
kind: theorem
decl: GlobalTheory.T.unitaryToroidalSeparation_of_base
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.UnitaryToroidalSeparationOfBaseStatement
covers: 1391
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement `UStB`. It is a second name for [the theorem of the same statement](/entry/u-st-b/), which is itself a second name for [the normalized blowup with separation](/entry/u-poin-st-x-sep/). That last entry has the content. [Rigid boundary charts for a fan](/entry/rigid-for-fan-holds/) uses this theorem as one of its two inputs. Below it are 1,391 declarations of the proof.

## Statement

`UStB` holds. In words: for each unitary moduli scheme $X$ with $p + q \geq 1$, each invariant function $\varphi$ with `IsPolFan` and `NoSelfInt`, and each coefficient field $F$, there are a projective normal compactification $Z$ of $X_F$, a normalized blowup $\pi \colon S \to Z$ along a boundary ideal, an open immersion $j \colon X_F \to S$ and further data, such that `UPoinOnX` and the separation property `SepB` hold. The entry [the normalized blowup with separation](/entry/u-poin-st-x-sep/) states it in full.

## Proof

The proof is the tactic

```
first | exact @GlobalTheory.UPoincTop.uStB | exact GlobalTheory.UPoincTop.uStB | (intros; apply GlobalTheory.UPoincTop.uStB <;> assumption)
```

The first branch succeeds, since `uStB` has the type `UStB`. So this theorem is `uStB` under another name.

## In the Lean code

The theorem is in [UnitaryToroidalSeparationOfBaseStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UnitaryToroidalSeparationOfBaseStatement.lean#L6). It calls only `GlobalTheory.UPoincTop.uStB`, in [UnitaryToroidalSeparationOfBase.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UnitaryToroidalSeparationOfBase.lean#L90). The statement `UStB` is in [FromBaseAlt.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/FromBaseAlt.lean#L57).

The name says "of base", as if the theorem took a hypothesis about a base. It takes none. The words "from base" in `UStB` and in `FromBase` refer to a condition inside `SepB`: degeneration data that descend from a smaller ring.
