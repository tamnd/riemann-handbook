---
id: siegel-weil-std-of-k
title: The Siegel-Weil formula from the transform properties and the local inputs
kind: theorem
decl: PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_of_k
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.ThetaParseval.ThetaKernels.SiegelWeilFinCore
covers: 627
status: drafted
drafted_by: writer@claude
---
This theorem gives the Siegel-Weil formula `SiegelWeilStd_k` from eight hypotheses. Its user is [`siegelWeilStd_mid_k`](/entry/siegel-weil-std-mid-k/), which supplies all eight. The theorem proves the Fourier coefficient statements and the induction step of the [Siegel-Weil chapter](/proof/siegel-weil/), Steps 3 to 5, from lemmas. Then it passes seventeen inputs to `Atop.siegelWeilStd_of_k`, which does the case split. The theorem itself is an assembly. Below it are 627 declarations.

## Statement

**Theorem.** Suppose that `TAll_k`, `LocInst_k`, `GIdil_k`, `KFinPoly_k`, `PolyKFin_k`, `LDEx_k`, `CTSplit_k` and `HolLead` hold. Then `SiegelWeilStd_k` holds.

The [parent entry](/entry/siegel-weil-std-mid-k/) states these hypotheses in words.

## Proof

The proof first makes these inputs, in order.

1. `SiegelWeilDatumProperties` (`auxiliaryExistence_holds`): a covolume measure and a rational Weyl element exist, and $G$ is a locally compact, Hausdorff, second countable group.
2. `FockMem_k`, `LocOpEx_k` and `GSplit_k`. The last one writes each $g$ as $x\,\iota_w(y)$, so that the height and the section are local functions of $y$.
3. `VacK_k` (`Avac.vacK_of_k`): the vacuum space `R.vac` is stable under $K$ and lies in `R.fock`.
4. `WhitK_k`, `WhitEq_k` and `WhitLow_k`, from `KWhit.whitK_of_k`, `whitEq_of_k` and `whitLow_of_k`. These give the Fourier coefficients of the Eisenstein series at $s_0$ in the three cases $n < m$, $n = m$ and $m < n$. The constants are 1, 2 and 0.
5. `Step_k` (`AStep.stepOf_k`): for $m < n$, the formula with constant 2 at rank $n - 1$ gives it at rank $n$. This lemma takes about 25 arguments. Among them are `HolLead`, `CTSplit_k`, `WhitLow_k` and `Afc.orbRes_k`.

Then `Atop.siegelWeilStd_of_k` does the rest. It proves `Main` for $n < m$ and turns it into `SWStdLt_k`. It proves `MainEq` for $n = m$, then `MainLe` for $m \leq n$ from `MainEq`, `Step_k` and `LDEx_k`. Last, `fieldOf_k` joins the two ranges with the meromorphic continuation `EisBL_k` and `SecK_k`.

So `HolLead` and `CTSplit_k` are used only in `Step_k`, and `LDEx_k` only in `MainLe`. We have not opened the proofs of the `KWhit`, `AStep` and `Atop` lemmas.

## In the Lean code

The theorem is in [SiegelWeilFinCore.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/SiegelWeilFinCore.lean#L45). `Atop.siegelWeilStd_of_k` is in [SiegelWeilAtopField.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/SiegelWeilAtopField.lean#L36). The statements `WhitEq_k`, `WhitLow_k`, `VacK_k` and `Step_k` are in [LiftedSchrodingerDatum.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/LiftedSchrodingerDatum.lean#L71).

The theorem is a copy of [`siegelWeilStd_of`](/entry/siegel-weil-std-of/). Some inputs are not `_k` copies: `whitGenLt`, `whitGenEq` and `whitGenLow` of the chain without `_k`, and also `HolLead`, `Holtb.holT`, `AbsSt.absThm` and `AbsSt.vacuum_generates_polynomials`. They are used at [L52 to L60](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/SiegelWeilFinCore.lean#L52).
