---
id: export-at-of-bundles-alt
title: The local export condition from rational rows
kind: theorem
decl: GlobalTheory.ExportClose.exportAt_of_bundles_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ExportAtOfBundles
covers: 2149
status: drafted
drafted_by: writer@claude
---
This theorem proves the local export condition `ExportAt` at one datum. It chooses the integers $N_0$ and the bases $S$ that the condition asks for, and gets the good twists from [the twist theorem for all powers](/entry/twist-all-powers-of-galois-cohomology-class-field/). Its only user is the renaming [realization-of-published-alt](/entry/realization-of-published-alt/). Of the chain of six theorems from [export-f-prm-r-alt-alt](/entry/export-f-prm-r-alt-alt/) down, this one has the content.

## Statement

Let $D$, $n$, $x$ and $E = E(x)$ be as in [export-at-bundles-alt](/entry/export-at-bundles-alt/). Write $\ell_i$ for the prime of a twist index $i$, and $i(w) = n.\mathrm{twI}(w)$ for the twist index of a twisted place $w$.

**Definition.** `ExportAt D n x` holds if there are a function $N_0$ from twist indices to $\mathbb{N}$ and finite sets $S_{i,j,b}$ of data, for $j \in \mathbb{N}$ and $b$ a boolean, with:

1. for each twist index $i$ with a nonzero index place, `goodTwistExistsAllCoprimePowers` holds at $i$: if `SetHyp` holds at $i$, then for each $\varepsilon' > 0$, if the sets $\Sigma_{i,j,b}$ (`SgJ`) have full rank (`FullRk`) for $1 \le j \le m$, then for each family $S$ of bases of them (`BasisOf`) and each finite set $A$ of finite places of the base field of $D$, there are a finite set $Q$ of places, an integer $k'$ and a homomorphism $\psi'$ from the group `RCG i Q` to the units of the ring `Ok i k'`, such that $\psi'^a$ is a good twist (`GoodTw`, not unfolded) for each integer $a$ prime to $\ell_i$;
2. for each twisted place $w$, `SetHyp` holds at $i(w)$, and for $1 \le j \le m$ and each $b$, $\Sigma_{i(w),j,b}$ has full rank and $S_{i(w),j,b}$ is a basis of it. We have not unfolded `FullRk` and `BasisOf`.

`SetHyp` is a conjunction of seven conditions. It includes $r \ge 100$ and $g_k \ge 2r$ for each $k$.

**Theorem.** Under the hypotheses listed in [realization-of-published-alt](/entry/realization-of-published-alt/), `ExportAt D n x` holds.

## Proof

1. `exists_inputs_of_galHodgeN_roots` gives $N_0$ and a record `Inputs D E N0` of 21 facts. It uses `ChebotarevDegreeOne`, `GlobalArtinReciprocity`, `ToricDenominator`, the rows, the bounds, `GalHodgeN` and the roots of unity.
2. `twistedPlaceIndex_mem_firstPair_of_compatibleChoice` shows that $i(w)$ has a nonzero index place for each twisted $w$. It uses `NChTie` and that $L_0$ is Galois.
3. Define $S_{i,j,b}$ as a basis chosen by `exists_basis_averaged_series_of_class_sums` when $i$ has a nonzero index place and $1 \le j \le m$, and as $\emptyset$ otherwise. The lemma uses the field `t4` of the inputs.
4. Clause 1 is `twistAllPowers_of_galoisCohomology_classField`. It uses the 13 hypotheses from `Cheb` to `RayCharacterArtin`, `Conclusion5 D` and 20 fields of the inputs. It covers 1,405 of the 2,149 declarations below this theorem.
5. In clause 2, `SetHyp` is the field `hyp` of the inputs, with step 2. The full rank is `fullRank_thetaSeries_forms_of_rational_scalars`, from `CuspRapidDecay`, `BaseTup` and the rows. The basis property is the choice of step 3.

## In the Lean code

The theorem is at [ExportAtOfBundles.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExportAtOfBundles.lean#L17). Its lemmas are named in the proof above. `exists_inputs_of_galHodgeN_roots` is a renaming of `TwInputs.exists_inputs_of_hkSup_galHodge` ([InputsOfSidesStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/InputsOfSidesStatement.lean#L15)).

`ExportAt` is at [AmbientBaseHeq.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/AmbientBaseHeq.lean#L36), `goodTwistExistsAllCoprimePowers` at [AdmissibleIndexBoundAllPowers.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/AdmissibleIndexBoundAllPowers.lean#L23), `TwIn.Ok` at [TwGood.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/TwGood.lean#L103), and `Inputs` at [UnivChar.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/UnivChar.lean#L139).

Odd points:

- The first conjunct of `SetHyp` is `True` ([BlochKatoPhases.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/BlochKatoPhases.lean#L327)).
- The theorem copies `exportAt_of_bundles` in [RealizationOfPublished.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/RealizationOfPublished.lean#L27), with `GalSideAlt`, `GalHodgeN` and the inputs lemma above in place of `GalSide`, `GalHodge` and `admT4_of_rational_rows`.
- The name says "of bundles", but no bundle appears in the statement.
