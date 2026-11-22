---
id: theorem-s-leaves-of-carrier-g
title: The nineteen hypotheses of Theorem S
kind: theorem
decl: GlobalTheory.CarrierGap.theoremS_leaves_of_carrierG
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.OffK0Closed
covers: 6030
status: drafted
drafted_by: writer@claude
---
This theorem collects the 19 hypotheses of Theorem S into one statement. [`offDiag`](/entry/carrier-gap-off-diag/) feeds its result to `theoremS_of_conj`, which gives Theorem S and then the off-diagonal bound. The proof only assembles results that are proved elsewhere. The real content is in the leaves that it calls, mainly [`rowsDatumP_of_deep`](/entry/rows-datum-p-of-deep/), [`CutLeavesDeep_outright`](/entry/cut-leaves-deep-outright/) and [`carrierP`](/entry/carrier-p/), and in the proof of Theorem S itself (`theoremS_closedP`).

## Statement

Assume `CarrierP` (a carrier bound, see [`carrierP`](/entry/carrier-p/)), `RowNGP` (a bound on the rows), `RowsFinDim` (finite dimension of the spaces that the operator integrals give), `UniqGap` (two smooth Bessel maps of a discrete series with a large gap, $h \ge 120 n^3$, are proportional) and `SWXS` (a Siegel-Weil condition at each Hida setting). Then `TheoremSClosedHypotheses` holds. This is the conjunction of 19 conditions: a local model, density inputs, row inputs for each datum, `RowNGP`, `KppOffC`, `CarrierP`, agreement of the kernel exponents, `FoldOKC`, `OOIntAllC`, absolute convergence, `FinXC`, `WuDecayOfGap`, choices, the formula `FormulaC`, `RowsSumC`, `RowFormAllP`, mass data, `LinkAll` and `SplitAll`. We have not unfolded most of these.

## Proof

Each conjunct comes from one lemma. Thirteen are proved with no hypothesis, for example `localModelAt_holds`, `densInputT_holds`, `KppOffC_holds`, `kExpTiedS_holds` and `formulaCT_holds`. The row inputs come from `CutLeavesDeep_outright D`, then `rowsDatumP_of_deep`, `rowsInputP_of_normProd` and `rowsInputP_of_dataCut`. The other six use the hypotheses. `UniqGap` gives `WuDecayOfGap` (by `wuDecayOfGap_of_uniqGap`) and, with `KFinDense`, the independence `VIndepAtAllP` (by `vIndepAtAllP_ofG`). `SWXS` gives the normalizing constants and the mass data. `RowsFinDim` and `WuDecayOfGap` give `FinXC`. `CarrierP` and `RowNGP` are conjuncts as they are.

## In the Lean code

The theorem is at [OffK0Closed.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/OffK0Closed.lean#L633). The conjunction is in [TheoremSConclusion.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/TheoremSConclusion.lean#L58).

Two hypotheses are proved outright: `CarrierP` by `carrierP` in the same file, and `UniqGap` by `uniqGap_holds`. Its only user, `offDiag`, passes exactly these. The nine `Fact` instances of the section (for example `HermRepUnram`, `KFinDense`, `CoefCapAll`) are all supplied by global instances. Another definition with the same name, `ThmSOwn.TheoremSClosedHypotheses` in [ThmSOwn.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmSOwn.lean#L983), is a conclusion (bounds on $K_0$ and on a Hilbert-Schmidt sum), not a list of hypotheses. We do not know what the suffix "carrierG" means.
