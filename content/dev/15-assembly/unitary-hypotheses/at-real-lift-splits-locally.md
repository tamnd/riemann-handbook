---
id: at-real-lift-splits-locally
title: Good eigenvectors with zero theta lift vanish, for a real datum
kind: theorem
decl: GlobalTheory.DownLift.AtReal.lift_splits_locally
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.GaloisRepDescendsAtRealPlaces
covers: 881
status: drafted
drafted_by: writer@claude
---
This theorem proves `TypeNZ` for the real datum of a point: a good Hecke eigenvector with a string of Satake parameters and zero theta lift is zero. Its only user is the second name [`galoisRep_descends_at_real_places`](/entry/galois-rep-descends-at-real-places/), which fills the field `typeNZ` of the named inputs `LinkedDataNamed`. These inputs feed [`theta_conditions_of_inputs_of_jumpsCard`](/entry/theta-conditions-of-inputs-of-jumps-card/), below [the proof that HypsAlt is nonempty](/proof/unitary-hypotheses/) in branch 1 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/).

## Statement

Assume `CuspRapidDecay`, `HoweUnram` and `GeometricGaloisRepCompatibility`. The last is a record of twelve named inputs; the proof uses four of them: the Weil-Siegel formula `WeilSiegelFormulaUnitary`, `DoublingMethodLocalZetaIntegrals`, `UnramifiedDoublingGL` and `HeckeLPartialContinuation`.

Let $D$ be a datum, with a character frame, a norm choice and a tie. Let $X$ be a `RealAt` record over them. It holds a real datum $R$ (hermitian spaces $V_i$, $W_i$, Weil representations and theta maps $\theta_G$), a face $F$, and proofs of `Given R F` and `R.FullP`. Then for all $j$ and $t$, `TypeNZ R j t` holds: if $y$ is an eigenvector of a compatible family of Hecke operators, its eigensystem has a string (as in [the entry on the lifts](/entry/lift-inj-non-van-type-nz-of-hypotheses-alt/)), $y$ is good and $\theta_G(y) = 0$, then $y = 0$.

## Proof

1. `rallisConv_of_siegelWeil` gives `RallisConv D` from `CuspRapidDecay` and the Weil-Siegel formula. `RallisConv D` says that for a positive definite $V$ with $2 \operatorname{rk} W < \operatorname{rk} V$, the theta lifts of two cusp forms on $W$ are integrable, and their inner product is the volume of a fundamental domain times an integral over $W$ of a theta inner product against a matrix coefficient.
2. `nonGalois_downLift_nonvanishing` gives `NonVan R i t` for all $i$ and $t$, from the doubling inputs, `HeckeLPartialContinuation` and `HoweUnram`.
3. [`liftInj_and_properties_of_rallis_of_nonVan`](/entry/lift-inj-and-properties-of-rallis-of-non-van/) takes both facts and gives `LiftInj R` and five facts at each $(i, t)$. The proof keeps `TypeNZ`.

## In the Lean code

The theorem is at [GaloisRepDescendsAtRealPlaces.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/GaloisRepDescendsAtRealPlaces.lean#L10).

- `TypeNZ` is defined in [ParamsEx.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/ParamsEx.lean#L90), and `RealAt` in [ExistsUniqueVec.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/ExistsUniqueVec.lean#L30).
- Step 1 is a detour. Inside `liftRows_injective_and_typeProperties_of_nonvanishing`, `RallisConv` feeds only the fact `Saturated`, and `TypeNZ` comes from `typeNZ_of_nonVan_gen` without it. Step 2 gets `NonVan` from [`liftInj_and_nonVan_typeNZ_of_given`](/entry/lift-inj-and-non-van-type-nz-of-given/), and that theorem already gives `TypeNZ`, with no Weil-Siegel input.
- Eight of the twelve fields of `GeometricGaloisRepCompatibility` are not used.
- The name says "lift splits locally". The statement has no splitting and no local condition. The second name speaks of Galois representations at real places; none appear.
