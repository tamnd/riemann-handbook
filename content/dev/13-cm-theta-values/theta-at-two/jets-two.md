---
id: jets-two
title: Integral jets of CM theta series at the prime 2 (instance)
kind: theorem
decl: GlobalTheory.ThLoc.LocJets.jetsTwo
module: Development.AbelianVarietyTheory.Definitions.GaloisGeometry.FourthPowerTheta
covers: 616
status: drafted
drafted_by: writer@claude
---
This theorem proves `IntOpTwoLoc`, the 2-adic integrality of the jets of translated CM theta series. It is the second part of [the three local jet statements](/entry/loc-jets-all/). The proof only applies [`jets_two_of`](/entry/jets-two-of/) to four proved inputs, so the content is in that entry.

## Statement

**Theorem.** `IntOpTwoLoc` holds.

`IntOpTwoLoc` is stated in [the parent entry](/entry/loc-jets-all/) and in more detail in [the entry for `jets_two_of`](/entry/jets-two-of/). In short: for a CM lattice $L$ with $d \equiv 7 \pmod 8$, a theta function $\theta$ for a self-dual lattice $\Lambda$, and a Weierstrass model of $L$ over $\mathbb{C}_2$ with good reduction and $|a_1| = 1$, each sum of odd translates of $\theta$ in an integral frame has 2-adically integral jets.

## Proof

The proof is the term `jets_two_of fourth_power_theta gram_transfer FrameCompose_proof jets_linear`. The four inputs are:

- `fourth_power_theta`: the form `TensZ` of the fourth tensor power of a translate as a product of one-variable theta series;
- `gram_transfer`: the Gram relation `GramTransfer`;
- `FrameCompose_proof`: the frame relation `FrameCompose`;
- `jets_linear`: the transfer `JetsLinZ` of integral jets from the fourth tensor power to the series itself.

## In the Lean code

The theorem is at [FourthPowerTheta.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/FourthPowerTheta.lean#L301). `fourth_power_theta` (line 239), `jets_linear` (line 252) and `gram_transfer` (line 295) are in the same file. `FrameCompose_proof` is in [JetsLin.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/GaussianEigenFrames/GramFrameComposition/JetsLin.lean#L96); we did not open its proof. The odd-prime analogue `jetsOdd` is at line 299.

The module is in a folder named `Definitions`, but it holds only theorems.
