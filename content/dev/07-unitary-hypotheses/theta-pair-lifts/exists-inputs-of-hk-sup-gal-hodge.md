---
id: exists-inputs-of-hk-sup-gal-hodge
title: The 21 inputs of the twist theorem from the Galois and series sides
kind: theorem
decl: GlobalTheory.TwInputs.exists_inputs_of_hkSup_galHodge
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.InputsOfSides
covers: 559
status: drafted
drafted_by: writer@claude
---
This theorem builds the record `Inputs D E N0` of 21 facts at one datum $D$. Through its second name [`exists_inputs_of_galHodgeN_roots`](/entry/exists-inputs-of-gal-hodge-n-roots/) it is step 1 of [`exportAt_of_bundles_alt`](/entry/export-at-of-bundles-alt/). Eight fields come from the Galois side, the others from the series side.

## Statement

The three named hypotheses:

- `ChebotarevDegreeOne`: for a finite Galois extension $L/F$, each $g \in \mathrm{Gal}(L/F)$ and each finite set $S$ of finite places of $F$, there is a place $v \notin S$ of degree one, unramified in $L$, with a Frobenius element that restricts to $g$.
- `GlobalArtinReciprocity`, and `ToricDenominator`, a bound on the denominators of toric sums. We have not unfolded the first.

The data: a datum $D$, a real side $X$, an element $E$ of `XD D`, a series side $Y$, and a Galois side $G$ (`GalSideAlt D`). $G$ holds a tie `wd`, the condition `IsGaloisTriple`, and the bounds $r \ge 100$ and $g_k \ge 2r$.

`GalHodgeN D G.wd` has four parts. The main one says: for each prime $\ell$, each $\iota \colon \overline{\mathbb Q}_\ell \cong \mathbb C$ and each conjugate self-dual regular algebraic $\pi$, there is an attached Galois representation that is de Rham above $\ell$, crystalline where $\pi$ is unramified, and potentially crystalline. The other parts are `WildOne D`, a separation condition and tameness for characters.

**Theorem.** Assume the three named hypotheses, the rational rows `RatRow` at each index $i$ with a nonzero index place, `XiBdd`, `HkSupAt` at each $j$, `GalHodgeN D G.wd`, and: each $z \in \mathbb C$ with $z^{g_k(g_k - 1)} = 1$ lies in the image of the field `LL0`. Then there is $N_0$ with `Inputs D E N0`.

## Proof

1. **Galois side.** `galois_inputs_alt` gives `a1`, `a2`, `a8`, `good`, `sig`, $N_0$ with `a9`, `a10`, and `hyp` (the condition `SetHyp`). In it, Chebotarev gives the density of Frobenius elements, `IsGaloisTriple` with `GalHodgeN` gives `a1`, `a2` and `a8`, and `toric_properties` gives $N_0$, `a9` and `a10`.
2. **Laws.** `laws_of_serSide` gives the laws from the rational rows, and `xiType` gives `XiType`.
3. **Hecke support.** `supLaws_of_sides` gives `supG`, `supFull`, `supHk`, `commG` and `comm` from `HkSupAt`. `hkSS_of_sides` gives `ss`.
4. **Series.** From the laws: `rel`, `l3` and `type`. `admT4_of_roots_in_field` gives `t4` from the roots of unity. `univSup_of_xi` gives `univ` from `XiBdd`. The fields `univChar` and `off` are copied from $Y$.

## In the Lean code

The theorem is at [InputsOfSides.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/InputsOfSides.lean#L15). `Inputs` is at [UnivChar.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/UnivChar.lean#L139), `galois_inputs_alt` at [GaloisInputs.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/GaloisInputs.lean#L19), `GalSideAlt` at [GalSide.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/GalSide.lean#L19), and `GalHodgeN` at [IsPotCrysAtOfMono0.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/TypeConditions/IsPotCrysAtOfMono0.lean#L96).

Each hypothesis is used. We have not unfolded the fields of `Inputs`, the laws, `XiBdd` or `HkSupAt`.
