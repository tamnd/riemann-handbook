---
id: loc-jets-all
title: Integral jets of CM theta series at odd primes, at 2, and at the ramified prime
kind: theorem
decl: GlobalTheory.ThLoc.locJets_all
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.LocJetsAll
covers: 734
status: drafted
drafted_by: writer@claude
---
This theorem joins three local facts about CM theta series. Its only user, [`inputs_of_algT`](/entry/inputs-of-alg-t/), copies the parts into the fields `jetsOdd`, `jetsTwo` and `shape` of `ThLoc.Inputs`. The content is in the three theorems that it names. The largest is [`jetsTwo`](/entry/jets-two/), with 616 of the 734 declarations below it.

## Statement

**Theorem.** `IntOpLoc` holds, `IntOpTwoLoc` holds, and `EmbSep` implies `ShapeEigenLoc`.

The three parts share one setting. Let $d \equiv 7 \pmod 8$ be prime and $L$ the CM lattice `cmL` of discriminant $-d$. Let $\theta$ be a theta function in the space `Th` of a lattice $\Lambda$ stable under $\tfrac{b_0 + i\sqrt d}{2}$, and let $\Theta$ (`thetaLin`) be a combination of Taylor series of translates of $\theta$, mapped to $\mathbb C_p$ by $\iota$ in the variables of a frame. A series has *integral jets* (`JetsIntegral`) if each $\kappa!\, a_\kappa$ has norm at most 1.

- `IntOpLoc`: for $p$ odd and prime to $d$, with good reduction of the curve of $L$ and the normalization `LocNorm` of $\theta^{\otimes 4}$, the series $\Theta$ has integral jets, and so has its pairing `jetPair` with integral polynomials.
- `IntOpTwoLoc`: the same at $p = 2$, for a Weierstrass model that uniformizes $L$ (`Unif`). See [`jetsTwo`](/entry/jets-two/).
- `ShapeEigenLoc`: for $p \mid d$ and an eigenframe, $\Theta = \exp(-c\,\beta)\, s$ with $s$ of integral jets, $|c| \le |d|^{-1/2}$ and $\beta$ a quadratic series.
- `EmbSep`: a separation fact for embeddings $E \to \mathbb C_p$ that agree modulo the maximal ideal.

We have not unfolded `kernel4`, `Unif`, `IsEigenFrame` or `betaPair`.

## Proof

The proof is the triple `⟨LocJets.jetsOdd, LocJets.jetsTwo, LocJets.shape⟩`.

## In the Lean code

The theorem is at [LocJetsAll.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/LocJetsAll.lean#L6). The three parts are at [FourthPowerTheta.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/FourthPowerTheta.lean#L299): `jetsOdd` applies `jets_odd_of`, `jetsTwo` applies [`jets_two_of`](/entry/jets-two-of/), and `shape` applies `ShapeEigenLoc_of`.

The statements are in [StatementC.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/GaussianEigenFrames/StatementC.lean#L134) (`IntOpLoc`), [StatementH.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/GaussianEigenFrames/StatementH.lean#L47) (`IntOpTwoLoc`), [StatementJ.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/GaussianEigenFrames/StatementJ.lean#L56) (`ShapeEigenLoc`) and [StatementE.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/GaussianEigenFrames/StatementE.lean#L18) (`EmbSep`). This theorem does not prove `EmbSep`. Since $d$ is prime, the condition $p \mid d$ in `ShapeEigenLoc` means $p = d$.
