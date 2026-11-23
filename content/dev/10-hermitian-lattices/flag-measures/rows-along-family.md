---
id: rows-along-family
title: The row bounds along a family with large gaps
kind: theorem
decl: GlobalTheory.LoopRowBoundsGap.rows_along_family
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.LoopRowBoundsAlongFamilyLargeGaps
covers: 363
status: drafted
drafted_by: writer@claude
---
This theorem gives uniform constants for the three row bounds `RowsND`, `RowsDeg` and `RowsOne` along a family. It collects the constants of four earlier results into one admissibility package and applies the row estimate for admissible families. Its only user is the renaming [`loopRowBounds_along_family_largeGaps`](/entry/loop-row-bounds-along-family-large-gaps/), which serves [`loop_rows_closed_gap`](/entry/loop-rows-closed-gap/).

## Statement

The statement is in the [entry of the renaming](/entry/loop-row-bounds-along-family-large-gaps/). In short: from `SiegelMassRatio`, `GapIn.Hyp` and `ThmBpDS`, for each list of constants there are $C_0'$ and a threshold $t$. For each family $F$ with constant $C_\Gamma$, with $t \le C'(F)$, $t \le C_l(F)$ and the rank hypothesis, two things hold eventually: `FormAt` for each word, and the three row bounds with each $C \ge C_0'$ for ties $X, Y$ that meet four conditions.

## Proof

1. **Count constants.** `rowCounts_uniform_constants_families`, from the Siegel mass ratio, gives $c_3, c_H, c_S, c_4$ and a threshold $t_1$. Above $t_1$ the count conditions `adm20`, `HerrCocycleExtensionClass`, `ArchimedeanSignatureMatching` and `adm21` hold eventually.
2. **Amplitude constants.** `amplitude_bounds_uniform_large_gap_families`, from all three inputs, gives $C_a \ge 0$, $C_2$, $C_h \ge 0$ and a threshold $t_2$. Above $t_2$ and with the rank hypothesis, the amplitude bounds hold eventually for each $C_{pr}$ and $\delta > 0$.
3. **Choice.** Let $U$ be the package $(c_3, c_H, c_V, c_S, c_4, C_a, C_2, C_h)$. Put $C_0' = $ `c0U CT A C0 CGam U`, the maximum of three constants, and $t = \max(40, t_1, t_2)$.
4. **Forms.** `rows_raw_mass_and_genus_mass` has no hypotheses and gives `Conclusion3Family F`. Then `along_family`, with the part `DsigHC` of `GapIn.Hyp`, $40 \le C_l(F)$ and the rank hypothesis, gives the first conclusion and five family conditions: `FamilyRowsExist`, `admF6`, `admF7`, `admF8` and `FamilyWeylDimensionVandermondeQuotient`.
5. **Rows.** Steps 1 and 2, with the given cell bound for $c_V$, prove `UAdm` for $U$. `admissible_family_satisfies_row_estimates` takes the five family conditions, the four tie conditions and `UAdm`. It gives the three row bounds for each $C \ge$ `c0U CT A C0 F.CGam U`. Since $F$ has constant $C_\Gamma$, this is the bound $C \ge C_0'$.

## In the Lean code

The theorem is at [LoopRowBoundsAlongFamilyLargeGaps.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/LoopRowBoundsAlongFamilyLargeGaps.lean#L25). `along_family` is in [TcritLowOfDsig.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/TcritLowOfDsig.lean#L97). `UC`, `UAdm` and `c0U` are in [DegenerateConstant.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/DegenerateConstant.lean#L18). The four results of steps 1, 2, 4 and 5 are renamings of `RowCounts.uniform_counts`, `GapAmpUniform.amplitude_bounds_uniform_gap`, `Mass.RowsRawMass.main` and `RowsFive.rows_three_bounds`. We have not opened these originals, and we have not unfolded the row bounds.

`UC` lets the amplitude constants depend on $C_{pr}$, but here they are constant. The proof gives the name `LocalHeightDeterminant` to the `adm20` part of step 1.
