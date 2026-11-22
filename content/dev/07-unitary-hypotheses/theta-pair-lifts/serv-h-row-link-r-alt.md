---
id: serv-h-row-link-r-alt
title: The service row for the reciprocity linkage, from Artin reciprocity
kind: theorem
decl: GlobalTheory.Svd.servH_row_linkR_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ServHRowLinkR
covers: 10819
status: drafted
drafted_by: writer@claude
---
This theorem gives the service row for the bundles of the reciprocity linkage. It is a special case of the general service row [`servH_row_of_artin`](/entry/serv-h-row-of-artin/), which holds the real content (10,811 of the 10,819 declarations below this theorem). Its user is the renaming [`reciprocity_kernel_of_artin`](/entry/reciprocity-kernel-of-artin/), and through it [`row_hServ_of_link_alt`](/entry/row-h-serv-of-link-alt/). That theorem gives the field `hServ` of the record `AllRowsAlt` in branch 1 of [the unitary hypotheses node](/proof/unitary-hypotheses/). See also the field `hServ` of [HypsAlt](/step/hyps-alt-def/).

## Statement

The hypothesis `GlobalArtinReciprocity` says: for each number field $E$ and each algebraic closure $\Omega$ of $E$, there is a homomorphism from the ideles of $E$ to the abelianized Galois group of $\Omega/E$, with five properties. It is an open quotient map. Its kernel is the closure of $E^\times$ times the identity component of the units of the infinite ideles, so it factors through the [[idele class group|9GHD9MXNYV]]. Local units at a finite place $v$ map onto the image of inertia. Uniformizers at $v$ map to the inverses of Frobenius elements. The closure of the image of the local ideles at $v$ is the image of the decomposition group. This is global Artin reciprocity, as in Cassels and Fröhlich, *Algebraic Number Theory*, Chapter VII (Tate, Global class field theory).

The conclusion uses these notions:

- `BoundaryReciprocity` gives, at each point with data $O$, the type `RecTAlt O.ex` of reciprocity records.
- `ReciprocityLinkage p` links a record $R$ at a point $q$ of slot `p.s` when `RecordCompatibleExtended q R` holds. This structure has the fields of `RecordCompatible` (spectral data, a pin of the kernel, unit coordinates) and three more: `entC`, `std` and `rd`.
- `ServH ker 𝒜 σ` is the conjunction of `Closed 𝒜 RowTwU` and of `Pdv.At` for the kernel entry `ker b` at every selected bundle $b = \sigma(\dots)$ past a threshold. I did not unfold `RowTwU` or `Pdv.At`.

**Theorem.** Assume `GlobalArtinReciprocity`. For parameters $p$, the [row](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/ValidForConstructedPointClassesEventuallyWorking.lean#L268) `Row (IsGoodE p.s) (ReciprocityLinkage p) (ServH ker)` holds, with `ker R = R.T.ker`.

## Proof

Apply `servH_row_of_artin` (through its renaming `bundle_bothParts_of_standardKernel_of_globalArtinReciprocity`). That theorem gives `Row Q Lk (ServH ker)` for any slot $Q$, linkage $L_k$ and kernel map, from Artin reciprocity and two side conditions.

1. Every point of $Q$ has `HasPart`. A point in `IsGoodE p.s` is in `IsBuiltE p.s`, so it is built. Then `builtC_hasPart` gives `HasPart`.
2. Eventually, every bundle linked by $L_k$ has `StdTie` for its kernel. `linkR_stdTie_entry` proves this for all points. A linked record satisfies `RecordCompatibleExtended`, and its field `std` gives `StdTie` through `stdTie_of_eq_alt`.

Artin reciprocity is only passed along.

## In the Lean code

The theorem is at [ServHRowLinkR.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ServHRowLinkR.lean#L14). The general theorem is at [BundleBothPartsOfStandardKernelOfGlobalArtinReci.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/BundleBothPartsOfStandardKernelOfGlobalArtinReci.lean#L15). The side lemma is at [LinkRStdTie.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkRStdTie.lean#L20). The linkage is defined at [CoreAltAltBis.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CoreAltAltBis.lean#L60), and the hypothesis at [ExistsUniqueHcharOfFiniteOrder.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/ExistsUniqueHcharOfFiniteOrder.lean#L70).

The second side condition holds by the definition of the linkage: the field `std` of [RecordCompatibleExtended](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CoreAltAltBis.lean#L56) is the needed tie. The first conjunct of [ServH](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/HasPartAnd.lean#L45) does not depend on the selection $\sigma$ or on the kernel map.
