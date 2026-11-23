---
id: rows-all-loc-comp-of-is-rc-class-map-d-cen-loc
title: The point conditions of a datum from linked inputs and a count of jumps
kind: theorem
decl: GlobalTheory.RowsAll.locComp_of_isRc_classMapD_cenLoc
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.GaloisRepIsGeometricAtAllPlaces
covers: 799
status: drafted
drafted_by: writer@claude
---
This theorem proves the record `PointConditions' D` for one datum $D$: five groups of conditions on the data of $D$. Its only user is [`theta_conditions_of_inputs_of_jumpsCard`](/entry/theta-conditions-of-inputs-of-jumps-card/), which two lemmas below [the proof that HypsAlt is nonempty](/proof/unitary-hypotheses/) call, in branch 1 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/).

## Statement

Assume `ThetaLocalInputsAlt` (a record of fifteen named results, among them global Artin reciprocity), `HarishChandraFinite` and `CuspRapidDecay`. Let $h_L$ witness [RecTExists](/step/rect-exists-def/) and let $D$ be a datum. Assume:

- `LinkedInputs hL D`: a character choice $P$, a real datum $X$ (a `RealAt` record) that agrees with $P$, and named facts. One of them is `TypeNZ` for $X$; the callers get it from [`lift_splits_locally`](/entry/at-real-lift-splits-locally/), under its second name. Another is `SphericalInertData.Conclusion1 D`; one caller gets it from [`Conclusion1_alt_alt_alt`](/entry/conclusion1-alt-alt-alt/).
- `JumpsCard`: for each index $i$, each representation $r \colon G_E \to \mathrm{GL}_a(\overline{\mathbb Q}_{\ell_i})$, each place $w$ above $\ell_i$ and each embedding $\tau$ that induces $w$, if $r$ is de Rham at $w$ then the multiset of jumps of $r$ at $\tau$ has $a$ elements. Both notions are fields of the datum, not Mathlib notions.

Then `PointConditions' D` holds. Its fields are `RowsAAlt D` (ten conditions), `RowsB D` (four), `RowsC D` (six), `TypeNZRec` at each local index $i$, and a rank condition `adm3` for each size datum. `TypeNZRec i` says: for each good $x$ and each $F$ in the eigenspace of $x$, if the theta lift $\theta_P(F)$ is $0$ then $F = 0$. We have not unfolded the other conditions.

## Proof

1. `thetaLocal_a_conditions_of_jumpsCard` gives `RowsAAlt D` from `ThetaLocalInputsAlt` and `JumpsCard`.
2. `nonempty_join_of_agree` gives a join of $P$ from `HarishChandraFinite`, `CuspRapidDecay` and the agreement of $X$ with $P$.
3. `thetaLiftSpaces_rank_const_and_localisation_scalars` gives `LamPos` at each $i$ and the rank field.
4. `b_conditions_pairLift_splitBC_repOfLoc_of_a` gives `RowsB D` and, at each $i$, `PairLift`, `SplitBC` and `RepOfLoc`.
5. `provisionFirst D` comes from these rows and `UpperTheory.GalS.Parts.main_alt_alt`, which proves the implication `SummandsSuffice D` with no hypothesis.
6. `c_statement_of_pair_lift_splitBC_repOfLoc` gives `RowsC D`.
7. `type_nonzero_recursion_of_eigen'` gives `TypeNZRec` at each $i$ from `TypeNZ` for $X$, a string condition and a goodness condition.

## In the Lean code

The theorem is at [GaloisRepIsGeometricAtAllPlaces.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/GaloisRepIsGeometricAtAllPlaces.lean#L24). The records are in [PartsGive.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PartsGive.lean#L42), and `JumpsCard` in [DataN.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/DataN.lean#L1353).

- `JumpsCard` is used only in step 1. The proof names its local fact `Conclusion1`, but that fact is `provisionFirst D`, not the `SphericalInertData.Conclusion1 D` of the inputs.
- The name says nothing about the statement, and twenty other theorems in other namespaces have the same last name. The file name speaks of a geometric Galois representation; the conclusion has none.
