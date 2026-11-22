---
id: count-constants-of-siegel-weil
title: Counting constants for each family, from Siegel-Weil
kind: theorem
decl: GlobalTheory.CountConstants.count_constants_of_siegelWeil
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.CountConstantsOfSiegelWeil
covers: 2065
status: drafted
drafted_by: writer@claude
---
This theorem chooses the constants of the counting bound as functions of the family, from the hypothesis `SiegelWeilUnitaryConvergent`. Its users are [`row_counts_of_ties_alt`](/entry/row-counts-of-ties-alt/) and `irr_row_closed`. The proof only picks the constants. The count itself is in [`count_typed_of_volumeStep`](/entry/count-typed-of-volume-step/) and, below it, [`unitaryAutomorphicCounting_of_compactDualVolumeRatio`](/entry/unitary-automorphic-counting-of-compact-dual-volume-ratio/).

## Statement

For the hypothesis, see [`at_choice_alt`](/entry/at-choice-alt/). Under it, there are a map $\ell \mapsto c(\ell)$ from lists of reals to records of counting constants $(C_{res}, n_0, A, C_b, C, c, c_b)$ and a number $c_I > 0$ with these properties, for each family $F$ with output list $\ell_F$:

1. $C(\ell_F) \ge 0$ and $2(C_{YL}(F) + 1) \le A(\ell_F)$.
2. $c_I \le c(\ell_F)$.
3. For each predicate $P$ on (automorphic instance, Haar measure, level, test function), `CountAllPointsClass` holds with the constants of $c(\ell_F)$: $c > 0$, $c_b > 0$, and for each $x$ and $i$ the following. Let $I$ be an automorphic instance of rank $n$ over a field of degree $f$, with a Hida setting of level $n_0$ and constant $A$, the count data and $P$. Assume that the gap at each infinite place is at least $h$, with $C n^{19} f^5 \log(b\, r_d) \le h$, $\log f \le \sqrt n$ and $\log \log b \le c_b\, n f \log n$. Then
$$|D_{count} - D^*| \le e^{-c\, n f \log n}\, D^*.$$
Here $D_{count}$ is a count of the instance and $D^*$ is a main term built from formal degrees. We have not unfolded either.

## Proof

`volumeStep_of_siegelWeil` gives the volume step `VolumeStep` (a relation between the gauge volumes of an instance and of the instance of rank $n - 1$ on the complement of a vector of norm $\pm 1$). `count_typed_of_volumeStep` then gives, for each $A$, an $n_0(A)$ and a $C_0(A) \ge 0$ with the bound for each $n_1 \ge n_0$, $C \ge C_0$, and $c = c_b = 1/16$. The proof takes $A(\ell) = 2(\ell_6 + 1)$, $n_0 = n_0(A)$, $C = C_0(A)$, $c = c_b = c_I = 1/16$ and $C_{res} = C_b = 0$. `count_class_of_count` gives part 3.

## In the Lean code

The theorem is at [CountConstantsOfSiegelWeil.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/CountConstantsOfSiegelWeil.lean#L11). The bound is `PointsLemma` in [PlaceDegreeData.lean](lean:Formalism/SharpRestriction/CuspSpanNormBounds/PlaceDegreeData.lean#L364). The class form is in [BridgeCountE.lean](lean:Formalism/SharpRestriction/CuspSpanNormBounds/BridgeCountE.lean#L45).

The statement is weaker than it looks. `PointsLemma` and `CountIdempotentsClass` do not use their datum argument `_D`, so "for each $x$ and $i$" repeats one statement. The predicate $P$ is only an extra hypothesis, which `count_class_of_count` drops, so the case $P = $ true holds and implies the others. Part 1 holds by `le_refl`, since $C_{YL}(F)$ is entry 6 of $\ell_F$. All the constants are fixed except $n_0$ and $C$.
