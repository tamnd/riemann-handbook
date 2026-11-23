---
id: galois-rep-descends-at-real-places
title: The theta lift is injective on good eigenvectors, restated
kind: theorem
decl: GlobalTheory.T.galoisRep_descends_at_real_places
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.GaloisRepDescendsAtRealPlaces
covers: 882
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`lift_splits_locally`](/entry/at-real-lift-splits-locally/). It is used on the way to [the hypotheses from the unramified exponents](/proof/unitary-hypotheses/), in the [unitary hypotheses chapter](/proof/unitary-hypotheses/). Below this theorem are 882 declarations.

## Statement

**Theorem.** Assume `CuspRapidDecay`, `HoweUnram` and the record `GeometricGaloisRepCompatibility` of twelve named inputs. Let $X$ be a real datum (`RealAt`) over a datum $D$, a character frame, a norm choice and a tied tuple. Then `TypeNZ X.R j t` holds for all $j$ and $t$.

`TypeNZ` says: if $y$ is a good vector that is an eigenvector of a Hecke operator with a given string, and the theta lift `thG` of $y$ is $0$, then $y = 0$.

## Proof

The proof is `exact lift_splits_locally`, inside a `first` tactic that tries three forms of the call. The copy gets `RallisConv D` from `rallisConv_of_siegelWeil`, gets `NonVan` from `nonGalois_downLift_nonvanishing`, and passes both to `liftInj_and_properties_of_rallis_of_nonVan`.

## In the Lean code

Both theorems are in [GaloisRepDescendsAtRealPlaces.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/GaloisRepDescendsAtRealPlaces.lean#L23); the copy is at line 10.

The name does not match the statement: no Galois representation and no real place appear. The route is longer than it must be. `nonGalois_downLift_nonvanishing` is a second name for `nonvanishing_of_down_lift`, which calls [`liftInj_and_nonVan_typeNZ_of_given`](/entry/lift-inj-and-non-van-type-nz-of-given/) and keeps only `NonVan`. That lemma also gives `TypeNZ`, from inputs that the proof already has: `CuspRapidDecay`, `HoweUnram` and the fields `dbl`, `udbl` and `hl` of the record.
