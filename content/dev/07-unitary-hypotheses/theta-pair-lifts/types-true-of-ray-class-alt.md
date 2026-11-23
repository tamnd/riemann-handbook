---
id: types-true-of-ray-class-alt
title: The host embedding with true types, second name
kind: theorem
decl: GlobalTheory.T.types_true_of_ray_class_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ConclOfGrpStatement
covers: 443
status: drafted
drafted_by: writer@claude
---
This theorem is a second name of [`exists_sideA_alt`](/entry/exists-side-a-alt/), which has the content. It sits in the subtree of [membership and bundles at the origin parameters](/entry/exists-base-lattice-of-prime-alt/). Its callers, in ReductionToLocalLanglandsA.lean and SatakeParametersDeterminedAtUnramifiedPlaces.lean, pass six fields of `PublishedInputsThirdLayerAlt`: `what₂.fin`, `what₂.berger`, `greenC`, `what₂.art`, `ray` and `what₂.cheb`, after $h_L$.

## Statement

**Theorem.** Assume `RecTExists` (as $h_L$), `AutomorphicFormsFiniteGL`, `DeRhamPotSemistable`, `GreenCuspidal`, `GlobalArtinReciprocity`, `RayClassFieldSt` and `ChebotarevDegreeOne`. Let $D$ be a datum whose type `Loc` is empty, with a character frame $cf$, an embedding $j_E$ of the field $E$ of its host into $\overline{\mathbb Q}$ and finite types `rep`. Assume that the exponents `eExp` of $D$ are integers, that `TypesTrue` holds for $D$ and $cf$, that `RowDepth` $D$ `rep` holds, and that each prime $g_k$ of the host is a ray prime (`IsRayPrime`) of the field `KQbar D jE` for the modulus $Q_S \cdot q \cdot d$. Then `ConclAlt` $h_L$ $D$ $cf$ $j_E$ `rep`.

## Proof

The proof is `exact exists_sideA_alt`, tried in three forms by `first`. [That entry](/entry/exists-side-a-alt/) states `ConclAlt` in words.

## In the Lean code

The theorem is in [ConclOfGrpStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ConclOfGrpStatement.lean#L13).

The name says "types true of ray class". `TypesTrue` and the ray class condition are hypotheses. So the name lists inputs, not the output, which is the host embedding of `ConclAlt`.
