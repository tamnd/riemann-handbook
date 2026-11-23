---
id: type-bound-of-gap
title: The type bound from an amplitude bound and a pair count
kind: theorem
decl: GlobalTheory.TypeAsm.TopGap.typeBound_of_gap
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.TypePOfLargeGapDiscreteSeriesBessel
covers: 2509
status: drafted
drafted_by: writer@claude
---
This theorem proves the type bound `TypeP` from the gap bundle `GapIn.Hyp` and the Bessel realization `BesselOfW`. It splits the bound into a bound for each term (the amplitude bound) and a bound for the weighted number of pairs of terms (the pair count). Its statement form is [`typeBound_of_largeGap_discreteSeries_bessel`](/entry/type-bound-of-large-gap-discrete-series-bessel/), and the result goes to [`rowsPos_typeP`](/entry/rows-pos-type-p/).

## Statement

**Theorem.** $\mathrm{GapIn.Hyp} \wedge \mathrm{BesselOfW} \implies \mathrm{TypeP}$.

`TypeP` and the notation $v(t)$, $j(t)$, $\delta(t)$, $d_\pi$, $\mathrm{mass}(Y, u)$, $a(j, \delta)$, $e(j, \delta)$ are in [the entry for `rowsPos_typeP`](/entry/rows-pos-type-p/). The two intermediate bounds are as follows. Both have the same pattern of constants as `TypeP`.

- **Amplitude bound** (`AmpP`, with `AmpAt`). For each relevant term $t$, $\lVert v(t) \rVert \leq w(t) \sqrt{d_\pi} \, \omega(t) \, a(j(t), \delta(t))$. Here $w(t) = \sqrt{w(\Lambda) w(\Lambda')}$, with $w(\Lambda) = 1/\lvert\mathrm{Aut}(\Lambda)\rvert$ for the two lattices $\Lambda, \Lambda'$ of $t$, and $\omega(t)$ is a weight (`omT`) that we have not unfolded.
- **Pair count** (`PairsP`, with `PairsAt`). For all $C_H \geq 0$ there are $C_h, C_p \geq 0$ and thresholds such that, for $P$ as in `TypeP`, $\sum_{(t_1, t_2) \in P} w(t_1) w(t_2) \, \omega(t_1) \omega(t_2) \leq \mathrm{mass}(Y, u) \, e(j', \delta') \, e(j'', \delta'')$.

## Proof

1. **Amplitude.** `locDatC_of_besselOfW` turns `BesselOfW` into `LocDatC`: for each datum with a word, under `GapHyp D` and `dsigTie D`, there is a choice of local data with good local properties (`GoodLoc`). `localDataTailBound_closedForm_largeGaps` turns `GapIn.Hyp` into a tail bound `TailP`. Then `amplitudeBound_at_terms_of_localData` gives `AmpP`.
2. **Pairs.** [`termPairCountBound_of_siegelMassRatios`](/entry/term-pair-count-bound-of-siegel-mass-ratios/) gives `PairsP` from two proved facts on [[Hermitian forms|48P4A1CX85]] over CM fields: the mass formula for maximal lattices `MaxFormula.main` and the mass ratio `siegelMassRatio_holds`.
3. **Product.** `typeBound_of_amplitude_pairs` combines them. Take the constants $C_H$ of `AmpP`, then $C_h, C_p$ of `PairsP` at this $C_H$, and the maxima of the two pairs of thresholds. For a pair $(t_1, t_2) \in P$, multiply the amplitude bounds:
$$\lVert v(t_1) \rVert \lVert v(t_2) \rVert \leq d_\pi \, a(j', \delta') a(j'', \delta'') \cdot w(t_1) w(t_2) \, \omega(t_1) \omega(t_2),$$
since $\sqrt{d_\pi}^{\,2} = d_\pi$. Sum over $P$ and apply the pair count. The factor $d_\pi \, a \, a$ is nonnegative by `termAmplitudeFactor_nonneg`. This is `TypeAt`.

The hypothesis $C_s \geq C_p + 4$ of `TypeP` is used only to get $C_s \geq 0$ for `AmpP`.

## In the Lean code

The theorem is in [TypePOfLargeGapDiscreteSeriesBessel.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/TypePOfLargeGapDiscreteSeriesBessel.lean#L15). It calls:

- `GlobalTheory.T.amplitudeBound_at_terms_of_localData`, `GlobalTheory.TypeAsm.locDatC_of_besselOfW` and `GlobalTheory.T.localDataTailBound_closedForm_largeGaps`;
- `GlobalTheory.T.termPairCountBound_of_siegelMassRatios`, `GlobalTheory.Mass.MaxFormula.main` and `GlobalTheory.Mass.siegelMassRatio_holds`;
- `GlobalTheory.TypeAsm.typeBound_of_amplitude_pairs` in [TermAmplitudeFactorNonneg.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/TermAmplitudeFactorNonneg.lean#L22).

`AmpP`, `PairsP`, `AmpAt` and `PairsAt` are in [PerRowC.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/PerRowC.lean#L19). `typeBound_of_amplitude_pairs` proves `GlobalTheory.TypeAsm.TypeP`, while this theorem states `Formalism.L2.SG.RowsPos.TypeP`. The two definitions have the same text, so the `exact` closes the goal. `GapIn.Hyp` enters only the tail bound, and `BesselOfW` only the local data. `PairsP` asks neither $c_b, c_T > 0$ nor `Ties D`.
