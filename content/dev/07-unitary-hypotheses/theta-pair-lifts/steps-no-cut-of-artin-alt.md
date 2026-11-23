---
id: steps-no-cut-of-artin-alt
title: Sixteen step statements, one of them from Artin reciprocity
kind: theorem
decl: GlobalTheory.Pass.stepsNoCut_of_artin_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.StepsNoCutOfArtin
covers: 382
status: drafted
drafted_by: writer@claude
---
This theorem proves `NoCutStatement` from `GlobalArtinReciprocity`. The proof is a tuple of sixteen terms, one for each part. Fifteen of them are closed theorems that take no hypothesis. Only the last part uses Artin reciprocity. Its second name is [`no_cut_passes_of_artin_reciprocity`](/entry/no-cut-passes-of-artin-reciprocity/), which the [extra facts step](/entry/extra-from-facts-main-alt-alt/) calls. It is part of the [unitary hypotheses chapter](/proof/unitary-hypotheses/).

## Statement

`GlobalArtinReciprocity` implies `NoCutStatement`, the conjunction of these parts. $D$ is a datum `D7`, $i$ a place, $r$ a family of representations, and $w$ a place over $\ell_i$.

1. `CentralIdemCoeff`: for a finite group $\Gamma$, a central idempotent $e$ of $\mathbb C[\Gamma]$ and a primitive $|\Gamma|$-th root of unity $\zeta$, each $|\Gamma| \cdot e(h)$ lies in $\mathbb Z[\zeta]$. This is true. A central idempotent is a sum of the idempotents $e_\chi = \frac{\chi(1)}{|\Gamma|}\sum_g \chi(g^{-1})\, g$ (Serre, *Linear Representations of Finite Groups*, §2.6).
2. `StepCentral`: `CentralIdemCoeff` gives `CentralElt D`.
3. `StepDeg`: at a type prime $\ell_i = g_k$ there are $2f$ places over $\ell_i$, each of degree 1.
4. `StepTypeAlt`: hypotheses on $D$ give `TypeLGC`.
5. to 9. `StepPotDirect`, `StepPotDual`, `StepJumpDirect`, `StepJumpDual`, `StepLift`: the twists or duals of $r$ form families of type `PotFam`, `JumpFam` or `LiftFamW` at $w$.
10. `StepSub`: two families of matrices embed in a twist of $r$ (`SubTw`).
11. `StepCont`: the twists and the duals of $r$ are continuous.
12. and 13. `StepLocDirect`, `StepLocDual`: a local bound `LocBoundP` for each `SubTw`.
14. `StepHfChar`: `HfChar` at type primes other than 2, at places of degree 1.
15. `ResidueStatement`: residual irreducibility and `GaloisFamilyConditions'` give `ResSpan`.
16. `GlobalStatement`: a bound of `vccCut i Xs π` by a sum of local terms.

We have not unfolded `PotFam`, `JumpFam`, `LocBoundP`, `HfChar` or `vccCut`.

## Proof

Each part is a named theorem, such as `centralIdemCoeff` for part 1 and `ResidualSpan.main_alt_alt` for part 15. Part 16 is `globalPass_of_globalArtinReciprocity hA`, a second name of `StepGlobalPf.main_alt_alt`.

## In the Lean code

The theorem is at [StepsNoCutOfArtin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/StepsNoCutOfArtin.lean#L13), and `NoCutStatement` at [StepsNoCut.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/StepsNoCut.lean#L38). Most parts are in [StepJumpDirect.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/StepJumpDirect.lean#L72) and [CentralIdemCoeff.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/CentralIdemCoeff.lean#L158).

`NoCutStatement` is a variant of `StepsNoCut` ([StepJumpDirect.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/StepJumpDirect.lean#L185)). Three parts differ:

- `StepTypeAlt` uses `adm2_alt` where `StepType` uses `adm2`;
- `ResidueStatement` uses `GaloisFamilyConditions'` where `StepRes` uses `GaloisFamilyConditions`;
- `GlobalStatement` is `StepGlobal` without the hypothesis `SetSQ i r`.

The name `StepCont` is also used for an unrelated statement on CM extensions, in the namespace `GlobalTheory.SWLow` ([LowRangeOfSteps.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LowRangeOfSteps.lean#L90)).
