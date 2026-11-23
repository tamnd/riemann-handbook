---
id: at-of-true-columns
title: The kernel conditions for an entry over true columns
kind: theorem
decl: GlobalTheory.PdvClose.at_of_true_columns
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.AtOfTrueColumns
covers: 2301
status: drafted
drafted_by: writer@claude
---
This theorem proves the kernel conditions `Pdv.At` for a tied kernel entry over the datum of a true-columns object. It is the content of the chain [`rowAt_of_stdTie`](/entry/row-at-of-std-tie/), [`kernelDatumConditions_at_standardKernelComparison`](/entry/kernel-datum-conditions-at-standard-kernel-comparison/), [`at_of_stdTie`](/entry/at-of-std-tie/). Its direct user is `at_of_stdTie`, which opens a standard tie and calls this theorem. The result goes into the second part of the service row in [`servH_row`](/entry/serv-h-row/).

## Statement

Let $I$ be a true-columns datum (`TC B X`) over a base $B$, with laws $l$, $l_0$ and later data $Z$. Write $D = I.\mathrm{rec7}(l, Z)$ for its datum. Let $L, h_T, G_i, G_l, K, Y, c_X$ and `ex` be size data, ties, instances, constants, division data and extra data over $D$, and let $t$ be a tied kernel entry of `ex`.

**Theorem.** Assume `AlgTAll`, `GenusOneModelExistsLattice`, `CurveDict` and `IntInert` (stated in [`servH_row`](/entry/serv-h-row/)). Assume `I.Ok`, `TC.Pins`, `ColNorm I`, `JetsIn I`, $\mathrm{ex.tw} = I.\mathrm{tw}(l, l_0, Z)$, `I.StdKer l Z t`, `IsEntC t`, `t.Adapted` and `t.TopPinned`. Assume $3 \le$ `splitBound`, $5 \le d_{l1}$, $4 \le d_{l2}$, and for every entry $E$ the condition `Shape` and a bound $\le 2a$ on differences of row values. Then `Pdv.At ex t.ent`.

`Pdv.At` ([IsEntC.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/IsEntC.lean#L19)) has two groups of conditions on the entry $E = t.\mathrm{ent}$:

1. conditions on $E$ and $D$: the values `E.un` have norm 1 at levels below $m$ (`UnUnit`); the kernel maps send rational vectors to rational vectors (`KmapRat`); the kernel maps raise a filtration by one step (`KFi`); the stabilisers at level 0 are trivial (`Stab0`);
2. for some data $\epsilon$, $\beta$, $s$, conditions on the place entry built from $E$ (`ofKer`): even conditions at inert places (`EvenConditionsInert`) and a second set `EvenConditionsAtC`, an orbit lower bound (`OrbitBoundWithoutOperator`), integrality of jets away from $d$, the shape of the theta kernel at the ramified prime $d$, and `Shape`.

We have not unfolded the hypotheses on $I$ and $t$.

## Proof

1. `conditions_at_standardKernelComparison_trueColumns` gives the duties of $t$ (`Duty`): a column side `ColSide`, a rank fact `t.RK` and a second entry $t'$ with `ColSide` and `FormsPin`. `kernelEntries_hyp_of_columnSideProperties` gives `t.Hyp`.
2. `normalisedThetaCMCurveTheorems_of_algebraicTranslates` gives theta inputs from `AlgTAll`. `HostInert.hostAt_inert` gives the host at inert primes from the other three hypotheses.
3. `admissibleKernelSeries_inertPrime_nonConjugateFrobenius` gives $\epsilon$, $\beta$ and the even conditions at inert places, with $s = -1$.
4. The conjuncts: `kernelPairScalars_isUnit_trueColumns` (`UnUnit`), `kmapRat_kerEntC'` (`KmapRat`), `kernelClassSums_carry_chainComplexForms` applied to $t'$ (`KFi`), `stab0_rec7_of_levelData` (`Stab0`), `frobeniusConjugation_conditions_adaptedKernelDatum` (`EvenConditionsAtC`), `orbitBound_standardSeries_inertPlaces` (orbit bound, from the shape hypotheses and $d_{l1}, d_{l2}$), `jetIntegralityBis_ofKer_of_hyp` and `kernelDatum_thetaSeries_shape_at_d_adaptedBases`. The last conjunct `Shape` is the shape hypothesis itself.

## In the Lean code

The theorem is at [AtOfTrueColumns.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/AtOfTrueColumns.lean#L30). All its hypotheses are used. `GenusOneModelExistsLattice`, `CurveDict` and `IntInert` are used only through `hostAt_inert`. The shape hypothesis asks for `Shape` at every entry, not only at the entry built from $t$; the proof uses it at that one entry, and the `Shape` conjunct of `Pdv.At` is copied from it. The conjuncts `KFi` and `Stab0` depend only on $D$ and the twist, not on $t$.
