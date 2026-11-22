---
id: siegel-weil-std-of-ct
title: The Siegel-Weil formula from the constant term split
kind: theorem
decl: PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_of_ct
module: Development.WeilBound.CoreStatements.AutomorphicKernels.SiegelWeilFormula.SiegelWeilStandard.SiegelWeilStdOfCt
covers: 1172
status: drafted
drafted_by: writer@claude
---
This theorem gives the Siegel-Weil formula `SiegelWeilStd` from one hypothesis, the constant term split `CTSplit`. It fills the other hypothesis of [`siegelWeilStd_pre`](/entry/siegel-weil-std-pre/), a Poisson summation formula, with a theorem. Its user is [the Siegel-Weil formula](/proof/siegel-weil/), which proves `CTSplit`. The real content is in `siegelWeilStd_pre`. Below this theorem are 1,172 declarations.

## Statement

**Theorem.** If `CTSplit` holds, then `SiegelWeilStd` holds.

`SiegelWeilStd` is the formula of the [Siegel-Weil chapter](/proof/siegel-weil/). `CTSplit` is the induction step on the rank $n$. For a lower rank datum, which embeds the problem of size $n - 1$ into the problem of size $n$, it says: the integral over a unipotent group of a Fourier coefficient of the Siegel [[Eisenstein series|3NZBZXYWAJ]] is a Fourier coefficient of the lower rank coset sum, plus a term $c_2$. This $c_2$ satisfies $c_2(\iota(y)x) = e^{\tau(n-2z)} c_2(x)$ for each $y$ with `IsDil` of parameter $\tau$. We have not unfolded `IsDil`.

## Proof

Apply `siegelWeilStd_pre` to the theorem `TW.Twp.poisson` and the hypothesis. The theorem `poisson` proves `Poisson`, which is stated in [the entry on `siegelWeilStd_pre`](/entry/siegel-weil-std-pre/). Its proof changes coordinates and then calls `theta_four`: the theta sum of the adelic Fourier transform of a Schwartz-Bruhat function equals the theta sum of the function.

## In the Lean code

The theorem is in [SiegelWeilStdOfCt.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilStandard/SiegelWeilStdOfCt.lean#L8). Its proof is `siegelWeilStd_pre TW.Twp.poisson hCT`. `CTSplit` is defined in [LowerRankDatum.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/LowerRankDatum.lean#L155). `poisson` is in [IntEqFour.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/WeylIntegralCovariance/IntEqFour.lean#L27), and `theta_four` is in [AdelicFourierRealisesWeylElement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/AdelicFourierRealisesWeylElement.lean#L129).

The theorem only passes its hypothesis along. The copy [`siegelWeilStd_of_ct_k`](/entry/siegel-weil-std-of-ct-k/) has the same form.
