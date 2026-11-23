---
id: loop-rows-closed-gap
title: The loop row bound, through the families with a gap
kind: theorem
decl: GlobalTheory.LoopRowsCloseGap.loop_rows_closed_gap
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.LoopRowsOfLargeGapDiscreteSeries
covers: 548
status: drafted
drafted_by: writer@claude
---
This theorem proves the loop row statement `LoopRowS 3 𝒞 sel` for a selection of spectral ties. It restricts to the families on which the gap hypothesis holds eventually, builds local Bessel and loop term data, and calls the row bounds of [`loopRowBounds_along_family_largeGaps`](/entry/loop-row-bounds-along-family-large-gaps/). Its only user is the renaming [`loopRows_of_large_gap_discreteSeries`](/entry/loop-rows-of-large-gap-discrete-series/), below [the loop row bound for a selection of spectral ties](/entry/loop-rows-of-rows-fin-dim-alt/).

## Statement

Assume `GapIn.Hyp` (four parts: the branching hypotheses `HypsG`, uniqueness of Bessel maps `UniqGap`, `LowKMultOneG` and `DsigHC`), `BesselOfW`, `ThmBpDS`, `WuDecayOfGap` and `RowsFinDim`. Let $\mathcal C$ be a family class with `TuSize F` for each $F \in \mathcal C$, and let `sel` be a selection of spectral ties. Assume that the rank hypothesis `RanksF` with the constants $(3, C_{YL}+1, \tfrac14, 3, \tfrac12, C_{Tu})$ is [closed](/step/closed-def/) on $\mathcal C$.

**Theorem.** `LoopRowS 3 𝒞 sel` holds. That is: for each function $a_F$ of the constant list, it is closed on $\mathcal C$ that, for all large $x$, all indices $i$ and all word pairs $(u, u')$ that meet the counting hypothesis `Cnt.Hyp`, if the selected ties are concrete and the loop series $t_O(u, u')$ converges absolutely, then the conditions `RowBig` and `RowNotScalar` hold with the bound $\varepsilon_L$.

We have not unfolded `RowBig` and `RowNotScalar`.

## Proof

1. **Gap.** `gapEv_closed_of` uses `TuSize`: it is closed on $\mathcal C$ that the gap hypothesis `GapHyp` holds for $F(x, i)$ for all large $x$. Then `loopRowS_of_sub` reduces the claim to the class `CG 𝒞` of families with this property.
2. **Standing inputs.** `HermRepUnram` and `CoefWeightedLoc` come from theorems with no hypotheses. `DecLow` and `DecInf` are parts of `HypsG`. `finXC_of` gives `FinXC` from `WuDecayOfGap` and `RowsFinDim`. `rMeasEx_all`, `localBesselJFactor_all_words_of_gap` and `CovNFormulaPf.main` give three more inputs with no hypotheses.
3. **Constants.** [`loopRowBounds_along_family_largeGaps`](/entry/loop-row-bounds-along-family-large-gaps/), with the Siegel mass ratio, `GapIn.Hyp` and `ThmBpDS`, gives for each constant list a threshold and a constant $C_0$. `stabiliserCovolume_relevantTerm_le_heightPow` gives covolume constants $c_V$ and the small cell volume bound.
4. **Forms.** For families large enough that the constants $C'$ and $C_l$ exceed the threshold, the first part of step 3 gives `FormAt` for each word. The lemmas `sC'_mem_cLast` and `le_sCl_of` show that the largeness condition gives this.
5. **Rows.** `loopRowS_of_raised` reduces `LoopRowS` to the bounds `RowsND`, `RowsDeg` and `RowsOne` for a family with raised starting point. Its loop ties are built from the local data `BGW` (Bessel data from `wuBessel_ofW`) and `MGW` (loop term data from `loopTermOfN`). The bounds come from the second part of step 3, with the ties `tiesR`, the lattice condition `beta_l_unique` and the cell bound of step 3.

The rest is bookkeeping with constant lists and maxima.

## In the Lean code

The theorem is at [LoopRowsOfLargeGapDiscreteSeries.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/LoopRowsOfLargeGapDiscreteSeries.lean#L121). The file also defines `wuBessel_ofW`, `loopLocDatOfW`, `BGW` and `MGW`, and proves `sC'_mem_cLast` and `le_sCl_of`. The reductions `loopRowS_of_sub` and `loopRowS_of_raised` are in [LoopRowSF.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/LoopRowSF.lean#L66) and [LoopRowSOf.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/LoopRowSOf.lean#L126).

Three inputs enter at one point each: `ThmBpDS` in step 3, `BesselOfW` through `BGW` and `MGW`, and `RowsFinDim` through `finXC_of`. `GapIn.Hyp` enters in steps 2 and 3. The rank hypothesis is used twice, for the forms and for the rows. The constants $3$, $\tfrac14$, $3$, $\tfrac12$ are fixed in the statement and in `LoopRowS`.
