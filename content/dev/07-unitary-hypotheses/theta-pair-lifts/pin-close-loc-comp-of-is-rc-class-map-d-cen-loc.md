---
id: pin-close-loc-comp-of-is-rc-class-map-d-cen-loc
title: A pending datum of depth zero, from a character choice datum
kind: theorem
decl: GlobalTheory.PinClose.locComp_of_isRc_classMapD_cenLoc
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ImportsTerSide
covers: 470
status: drafted
drafted_by: writer@claude
---
This theorem gives the second of the four tie conditions `Tie4` for one datum $D$: a pending datum $P'$ with `admDZ P'` and `EigSpan P'`. Its caller is [the two tie conditions for one datum](/entry/tie-chi-of-lab-all-green-chi-cen/), which defines these conditions. The theorem turns the hypotheses on a character choice datum into the list of hypotheses of `exists_pending_objects_depthZero_admissible_eigenSpan`, which builds $P'$. Below this theorem are 470 declarations.

## Statement

Assume the theta local inputs `ThetaLocalInputsAlt` (fifteen named results) and `DepthZeroSupport`. Let $h_L$ be an element of `RecTExists`, $D$ a datum and $P$ a character choice datum of $D$. Assume:

1. for each index $i$, a row module of $P$ at the index $j_i$;
2. `LabAll`, `CenLoc`, `GreenLab` and `ChiTOk` for $P$;
3. `tie0` and `adm5` for $D$;
4. `ZLStable`, `CenInt`, `SerLL`, and a primitive root of unity of the order `restRowsFiniteGroupCard` in each coefficient ring $\mathcal{O}_i$.

Then $D$ has a pending datum $P'$ with `admDZ P'` and `EigSpan P'`.

The [entry of the caller](/entry/tie-chi-of-lab-all-green-chi-cen/) gives these conditions in short form. We have not unfolded the row module, `tie0` or `adm5`.

## Proof

1. `LabTies.main` splits `LabAll` into three facts: `IneRep`, `LabDepth` and `LabGen`.
2. `groupAlgebraCentre_keeps_typeSpaces_at_localisations`, from `CenLoc` and the field `av` of the Hecke data of $P$, gives `OnMtPreservesTypeV`: the centre of the group algebra keeps the type spaces.
3. `depthZ_of_rowMod_labAll_chiTOk` gives `DepthZ D`. This is the one use of `DepthZeroSupport`.
4. `admDepthZero_of_rowMod_labAll_greenLab` gives `AdmDepthZeroTypes`, from the row modules, `LabAll`, `CenLoc`, `GreenLab` and `ChiTOk`.
5. Each parameter $S$ of `ParC D` comes from a parameter of the types of $D$ with the same local parameters. This uses the bijection `eP` in the types of $P$.
6. `exists_pending_objects_depthZero_admissible_eigenSpan` takes the Hecke data of $P$, the facts of steps 1 to 5 and hypotheses 3 and 4, and gives $P'$.

The rest is bookkeeping.

## In the Lean code

The theorem is in [ImportsTerSide.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ImportsTerSide.lean#L18). The lemmas of steps 3 and 4 are in [NonGaloisDepthZeroTame.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/NonGaloisDepthZeroTame.lean#L20) and [NonGaloisDepthZeroEntrywise.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/NonGaloisDepthZeroEntrywise.lean#L74). The lemma of step 6 is in [ExistsPendingObjectsDepthZeroAdmissibleEigenSpanStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsPendingObjectsDepthZeroAdmissibleEigenSpanStatement.lean#L7). It is itself a second name for `PendClose.main`, which we have not opened.

Every hypothesis is used. The name `locComp_of_isRc_classMapD_cenLoc` does not describe the statement: `CenLoc` is one hypothesis of thirteen, and nothing called `isRc` or `classMapD` appears. The module name `ImportsTerSide` describes the imports.
