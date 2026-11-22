---
id: siegel-weil-std-of
title: The Siegel-Weil formula from the transform, the lower rank data and the constant term split
kind: theorem
decl: PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_of
module: Development.WeilBound.CoreStatements.AutomorphicKernels.SiegelWeilFormula.SiegelWeilStandard.SiegelWeilStdOf
covers: 621
status: drafted
drafted_by: writer@claude
---
This theorem proves the [Siegel-Weil formula](/proof/siegel-weil/) `SiegelWeilStd` from eight inputs. It builds the Fourier coefficient statements of the three cases $n < m$, $n = m$ and $m < n$, and gives them to the final assembly `Atop.siegelWeilStd_of`. Its user is [`siegelWeilStd_mid`](/entry/siegel-weil-std-mid/), which supplies the inputs. Below it are 621 declarations.

## Statement

**Theorem.** Suppose that `TAll`, `LocInst`, `GIdil`, `KFinPoly`, `PolyKFin`, `LDEx`, `CTSplit` and `HolLead` hold. Then `SiegelWeilStd` holds.

`SiegelWeilStd` is the formula $E(x, s_0, \Phi) = c\,\mu(D)^{-1}\int_D \theta(\omega(x) S_g \Phi)\,d\mu(g)$ of the [Siegel-Weil chapter](/proof/siegel-weil/), with $s_0 = (m-n)/2$, $c = 1$ for $n < m$ and $c = 2$ for $n \ge m$. Here $E$ is a Siegel [[Eisenstein series|3NZBZXYWAJ]] and $\omega$ a [[Weil representation|H3Q2703KKV]]. `TAll` collects the five properties of the transform $T\Phi$ of the Schrödinger model, `LDEx` says that lower rank data exist for $n \ge 2$, `CTSplit` is the constant term split of [`ctSplit_of`](/entry/ct-split-of/), and `HolLead` says that the Eisenstein series is holomorphic at $s_0$ for $m < n$. We have not unfolded `LocInst`, `GIdil` and `PolyKFin`.

## Proof

The proof first builds some local and global facts: `GSplit`, `VacK` (from `Avac.vacK_of`), `LocOpEx`, and the theorem `thetaCoef` of the same file, which says that the $T$-th Fourier coefficient of the theta integral is an orbit integral. Then it treats the three cases.

1. **$n < m$.** `KWhit.whitK_of` proves `WhitK`: the $T$-th Fourier coefficient of the Eisenstein series is holomorphic at $s_0$ and equals the orbit integral. Its local input is `whitGenLt`, which puts together the local Whittaker integrals at the finite places (`locFin2`, `unrWhit`), at the real places (`realWhit_of`) and the Siegel densities.
2. **$n = m$.** `KWhit.whitEq_of` proves `WhitEq` in the same way, from `whitGenEq` and `Aeis.eisWk`.
3. **$m < n$.** `KWhit.whitLow_of` proves `WhitLow` from `whitGenLow`. Then `AStep.stepOf` proves `Step`, the induction from rank $n-1$ to rank $n$. This is the only place where `CTSplit` and `HolLead` are used. It also uses `Afc.orbRes`, the restriction of orbit integrals to the smaller problem.

Finally `Atop.siegelWeilStd_of` assembles the formula from `AbsSt.absThm` (absolute convergence), `thetaCoef`, `WhitK`, `WhitEq`, `LDEx`, `VacK`, `Step` and the other facts. The chapter describes this assembly in its Steps 3 to 6. The rest is bookkeeping.

## In the Lean code

The theorem is in [SiegelWeilStdOf.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilStandard/SiegelWeilStdOf.lean#L52). The same file proves `tTheta`, `tAll_of`, `thetaCoef`, `whitGenLt`, `whitGenEq` and `whitGenLow` (lines 37 to 50). `CTSplit`, `Step` and `HolLead` are in [LowerRankDatum.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/LowerRankDatum.lean#L155). `Atop.siegelWeilStd_of` is in [SiegelWeilStdLeaves.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/FockVacuumBounds/SiegelWeilStdLeaves.lean#L40).

The theorem `kfour.auxEx` of type `AuxiliaryPrimeFunction` enters `WhitK`, `WhitLow` and `Step`. Its name says nothing about its content, as [`siegelWeilStd_pre`](/entry/siegel-weil-std-pre/) notes. The name `siegelWeilStd_of` is used twice: `Fin.siegelWeilStd_of` here and `Atop.siegelWeilStd_of` are different theorems.
