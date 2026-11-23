---
id: fam-joint-bcd-closed-alt
title: Joint hub conditions along a family, from closed jump conditions
kind: theorem
decl: GlobalTheory.HTW.RecS.fam_jointBCD_closed_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.FamJointBCDClosed
covers: 331
status: drafted
drafted_by: writer@claude
---
This theorem gives a threshold $x_0$ along a family, past which the joint hub conditions hold at each member. It is [`fam_jointBCD`](/entry/fam-joint-bcd/) with two hypotheses removed. One comes from a closure hypothesis on jumps, and the other from a lemma on places away from the type primes. The [closing step of the link argument](/entry/nlink-close-main-alt-alt/) uses it for the thresholds of the joint hub conditions. It is part of the [unitary hypotheses chapter](/proof/unitary-hypotheses/).

## Statement

Assume:

1. `FontaineBcris`: for each prime $\ell$ and each core $C$, a list of properties of $B_{\mathrm{cris}}$, such as that $\varphi - 1$ maps the elements in $\mathrm{Fil}^0$ onto $B_{\mathrm{cris}}$;
2. `adm7 D` for each datum $D$;
3. `FontaineAtPlacesOverL` at each place $i$ of each $D$;
4. `JumpClosed D` for each $D$: each parameter $L$ with `AdmJAlt L` satisfies `JumpConditions L`.

Let `Fm : FamP eps` be a family and $R$ a `RowK` datum. Then there is $x_0$ with this property. For $x \ge x_0$ with $x > x_1$, each index $j$, each `HW`, and each hub datum $X$ of $D = $ `Fm.D x j`: if `AdmJAlt (Fm.L x j)` and `PtFam D X.r X.ρ` hold, then `JointParametersHubConditions (Fm.L x j) HW X R` holds.

## Proof

`fam_jointBCD Fm R` takes hypotheses 2 and 3 and gives $x_0$. At each member it needs two more facts.

1. `ConclusionJa D`. This is the first part of `JumpConditions`, so it comes from hypothesis 4 and `AdmJAlt`.
2. `PtIn` at each good $\pi$, at each place $i$ with $\ell_i$ inert (`InertK`). `ptIn_of_ptFam_deRham_away` gives this from hypothesis 1, `PtFam`, the first part of `AdmJAlt` (`DeRhamFamilyAwayAlt`), and $\ell_i \notin$ `gset D` $= \{g_0, g_1\}$. The last fact is `inert_prime_ne_typePrime` for $k = 0$ and $k = 1$: an inert prime is not a type prime.

## In the Lean code

The theorem is at [FamJointBCDClosed.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FamJointBCDClosed.lean#L13). `fam_jointBCD` is at [FamJointBCD.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/FamJointBCD.lean#L18). `ptIn_of_ptFam_deRham_away` is a second name of `pointInputAwayFromTypePrimes_alt`, at [PointInputAwayFromTypePrimesStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PointInputAwayFromTypePrimesStatement.lean#L11). `AdmJAlt` and `JumpClosed` are at [DeRhamFamilyAway.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/DeRhamFamilyAway.lean#L28). `FontaineBcris` is at [OneSubPhiOntoOfFilZero.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/GaloisCohomology₂/OneSubPhiOntoOfFilZero.lean#L18). We have not unfolded `ConclusionJa`, `PtIn` beyond its field names, or `JointParametersHubConditions` beyond its two local conditions.

The hypothesis `TwLoc` that `fam_jointBCD` gives at each place is not used: the proof only needs `InertK`.
