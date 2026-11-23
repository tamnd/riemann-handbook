---
id: lift-inj-and-properties-of-rallis-of-non-van
title: Injectivity of the theta lift and five properties of the lifts (statement)
kind: theorem
decl: GlobalTheory.T.liftInj_and_properties_of_rallis_of_nonVan
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.LiftRowsInjectiveAndTypePropertiesOfNonvanishingStatement
covers: 622
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`liftRows_injective_and_typeProperties_of_nonvanishing`](/entry/lift-rows-injective-and-type-properties-of-nonvanishing/). Its user is [`lift_splits_locally`](/entry/at-real-lift-splits-locally/), which keeps only the fact `TypeNZ` of the conclusion. The statement and its proof are in the entry for `liftRows_injective_and_typeProperties_of_nonvanishing`.

## Statement

The statement is word for word that of [`liftRows_injective_and_typeProperties_of_nonvanishing`](/entry/lift-rows-injective-and-type-properties-of-nonvanishing/). In short: assume `CuspRapidDecay` and `HoweUnram`. Let $R$ be a real datum with a face $F$ that satisfy `Given R F` and `R.FullP`. Assume `RallisConv D` and `NonVan R i t` for all $i$ and $t$. Then at $t = \mu_0$ the theta lift $\theta_G$ is injective on good eigenvectors whose eigensystem also occurs with a nonzero lift (`LiftInj R`), and for all $i$ and $t$ the five facts `TypeNZ`, `GoodMem`, `DownEig`, `UnrCorr` (at all places) and `Saturated` hold.

## Proof

The proof is one line, `exact @GlobalTheory.DownLift.liftRows_injective_and_typeProperties_of_nonvanishing`. It passes all hypotheses along.

## In the Lean code

The theorem is in [LiftRowsInjectiveAndTypePropertiesOfNonvanishingStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LiftRowsInjectiveAndTypePropertiesOfNonvanishingStatement.lean#L17). The proof is the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)` with the name of the proof in each slot, under `maxHeartbeats 1000000`. The hypothesis `RallisConv D` does no logical work in the proof below; see the entry for the proof.
