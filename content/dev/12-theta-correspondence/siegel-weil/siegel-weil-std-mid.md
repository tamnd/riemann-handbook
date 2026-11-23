---
id: siegel-weil-std-mid
title: The Siegel-Weil formula from four inputs
kind: theorem
decl: PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_mid
module: Development.WeilBound.CoreStatements.AutomorphicKernels.SiegelWeilFormula.SiegelWeilStandard.SiegelWeilStdMid
covers: 798
status: drafted
drafted_by: writer@claude
---
This theorem gives the [Siegel-Weil formula](/proof/siegel-weil/) `SiegelWeilStd` from four inputs. Its user is [`siegelWeilStd_pre`](/entry/siegel-weil-std-pre/), which proves three of them. The theorem only builds four more inputs and passes everything to [`siegelWeilStd_of`](/entry/siegel-weil-std-of/), which has the real content. Below it are 798 declarations.

## Statement

**Theorem.** If `TWeyl`, `KFinPoly`, `LDEx` and `CTSplit` hold, then `SiegelWeilStd` holds.

`TWeyl` (the action of the Weyl element on the transform $T\Phi$), `KFinPoly` and `LDEx` (lower rank data exist for $n \ge 2$) are stated in [the entry above](/entry/siegel-weil-std-pre/). `CTSplit` is stated in [`siegelWeilStd_of_ct`](/entry/siegel-weil-std-of-ct/).

## Proof

1. `tAll_of` adds the four other properties of $T$ to `TWeyl` and gives `TAll`.
2. `locInst_of` gives `LocInst` from `TAll`, `kfour.auxEx`, `KFock.fockMem` and `KFock.liftEx`.
3. `Kdil.gIdil_full` gives `GIdil`, and `KK.polyKFin_of` gives `PolyKFin`.
4. `HSt.holLeadB` gives `HolLead`, the holomorphy of the Eisenstein series at $s_0$ for $m < n$.

Then `siegelWeilStd_of` gives the formula. We have not unfolded `LocInst`, `GIdil` and `PolyKFin`.

## In the Lean code

The theorem is in [SiegelWeilStdMid.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilStandard/SiegelWeilStdMid.lean#L16), and `locInst_of` in the same file at [L14](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilStandard/SiegelWeilStdMid.lean#L14). The proof writes `locInst_of hT` twice, once for `siegelWeilStd_of` and once inside `gIdil_full`. It is a pass-through.
