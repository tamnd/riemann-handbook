---
id: tie-chi-of-lab-all-green-chi-cen
title: The two tie conditions for one datum, from the labels and the central action
kind: theorem
decl: GlobalTheory.HeightCounting.Up.PendLayer.tieChi_of_labAll_green_chi_cen
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.PendingLayerConditionAtMember
covers: 545
status: drafted
drafted_by: writer@claude
---
This theorem proves, for one datum $D$, the first two of the four tie conditions `Tie4`: the condition `tieChi`, and a pending datum with `admDZ` and `EigSpan`. Its caller [proves the same at every layer point](/entry/pend-layer-loc-comp-of-is-rc-class-map-d-cen-loc/). It makes three auxiliary facts and passes them to two lemmas. The larger one is [the pending datum of depth zero](/entry/pin-close-loc-comp-of-is-rc-class-map-d-cen-loc/). Below this theorem are 545 declarations.

## Statement

The datum $D$ has a host field $E$ with two auxiliary primes $g_0, g_1$, coefficient rings $\mathcal{O}_i$ over primes $\ell_i$, and characters $\chi_i \colon G_E \to \mathcal{O}_i^\times$. For each type prime place $v$ of index $k$, $D$ fixes a place $w_v$ of $E$ above $g_k$ and a value $\chi_J(i,k,v) \in (\mathbb{Z}/g_k)^\times$. The three conditions are:

- `tieChi`: when $\ell_i = g_k$, there is $u = \chi_J(i,k,v)^{\pm 1}$ such that $\chi_i$ is de Rham at $w_v$ and the polynomial label `items₂` of its Weil-Deligne representation at $w_v$ is $X - u$. At each conjugate place, $\chi_i$ is de Rham with label $X - u^{-1}$.
- A *pending datum* $P$ (`Pend D`) holds local data: for each $k$, primitive central idempotents of $\mathbb{C}[\mathrm{GL}_a(\mathbb{F}_{g_k})]$ with monic polynomial labels, tame inertia characters, an action $z_P$ of the centre of $\mathcal{O}_i[G_0]$ on the modules of $D$, and the types that occur. `admDZ P`: for each type $\tau$ that occurs at $w_v$, with squarefree label $f_\tau$ that has no root $\chi_J^{\pm 1}$, the label of the local parameter at $w_v$ is $f_\tau (X - u)^t$ for some $u = \chi_J^{\pm 1}$, with inverse roots at the conjugate places.
- `EigSpan P`: a central element that acts by a scalar $c$ on the type spaces at a point $x$ acts by $c$, through $z_P$, on the Hecke eigenspace at $x$.

**Theorem.** Assume `PublishedInputsThirdLayerAlt` and `DepthZeroSupport`. Let $P$ be a character choice datum of $D$ and $X$ a real datum that agrees with $P$. Assume `JumpsCard`, `LabAll` (the local labels come from the Weil-Deligne tie of $P$), `GreenLab` (each cuspidal irreducible representation of $\mathrm{GL}_d(\mathbb{F}_{g_k})$ has the cusp label that $P$ gives), `ChiTOk` (the local characters of $P$ at $w_v$ are Teichmüller lifts of $\chi_T^{\pm 1}$), `CenLoc`, `ZLStable`, `CenInt` (the centre of the group algebra acts through a block lift and keeps the rational and integral parts) and `RootsLL`. Then `tieChi` holds, and there is a pending datum with `admDZ` and `EigSpan`.

We have not unfolded `items₂` or the character choice datum.

## Proof

1. For each $i$, `RowModCanon.main_alt_alt` gives a row module (`RowMod`) at the index $j_i$, from Harish-Chandra finiteness and rapid decay of cusp forms.
2. `a_close_main`, from `JumpsCard`, gives the record `RowsAAlt D`. The proof uses its fields `tie0` and `a5`.
3. `rootsOfUnity_and_seriesIdempotent_rational`, from `RootsLL`, gives roots of unity in each $\mathcal{O}_i$ and `SerLL` (the idempotents `eSer` of $D$ have coefficients in the field `LL`).
4. `TieChiPin.locComp_of_isRc_classMapD_cenLoc` gives `tieChi` from step 1, `LabAll` and `ChiTOk`.
5. [`PinClose.locComp_of_isRc_classMapD_cenLoc`](/entry/pin-close-loc-comp-of-is-rc-class-map-d-cen-loc/) gives the pending datum from steps 1 to 3 and the other hypotheses.

## In the Lean code

The theorem is in [PendingLayerConditionAtMember.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PendingLayerConditionAtMember.lean#L31). `tieChi`, `Pend` and `admDZ` are in [PairedCharacterCondition.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/PairedCharacterCondition.lean#L330), and `EigSpan` in [StepJumpDirect.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/StepJumpDirect.lean#L14). Step 1 is in [ImportsBisSide.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ImportsBisSide.lean#L20), step 2 in [SClose.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SClose.lean#L25), and step 4 in [LiftSplitsLocally.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LiftSplitsLocally.lean#L22).

Every hypothesis is used. Of the published inputs, the proof uses only `what₂` (the theta local inputs), `hc` and `decay`.
