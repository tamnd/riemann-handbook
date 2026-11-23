---
id: weighted-bound-rotated-uniform-of-cubic-threshold
title: The weighted bound on rotated points from a cubic tensoring threshold
kind: theorem
decl: CompanionTheory.WaveGrid.weighted_bound_rotated_uniform_of_cubic_threshold
module: CompanionTheory.AutomorphicTheory.BesselWaveGrids.WeightedBoundRotatedUniformOfCubicThreshold
covers: 1158
status: drafted
drafted_by: writer@claude
---
This theorem proves the [weighted bound on rotated points](/entry/weighted-bound-rotated-uniform/) for any threshold function $t$ that grows at most like $n^3$ and above which discrete series can be tensored with the standard representation and its dual. It is the last assembly step before the local estimates. Its caller, [the bound with the cubic threshold filled in](/entry/uniform-bessel-rank-three-of-inputs/), gives one such $t$.

## Statement

Let $t(n, \varepsilon)$ be a real function of $n$ and a signature $\varepsilon$ of size $n$. Let $C_t \geq 0$ and $C_{gf}$ be real. Assume:

1. $t(n, \varepsilon) \leq C_t n^3$ for all $n \geq 1$ and all $\varepsilon$;
2. `ZuckT t` and `ZuckDualT t`: a discrete series with parameter $\mu$ whose gaps between entries of different sign exceed $t(n, \varepsilon) + 1$ tensors with the standard representation, and with its dual, into inequivalent discrete series at $\mu \pm e_s$ (see the [caller](/entry/uniform-bessel-rank-three-of-inputs/) for the precise form);
3. `In91`, the pair of statements on families of discrete series and on local Bessel expansions and moments;
4. `OneBesselTor D C_gf` for every datum $D$.

Then `WeightedBoundRotatedUniform` holds.

## Proof

The proof makes two local facts and then calls one theorem.

1. **The weighted one-place bound.** `wave_bessel_period_threshold`, in the same file, proves `WBp C_b` for every $C_b$. `WBp` says: for a local Bessel datum whose parameter has gaps at least $C_g(2r+2)^4$ and meets further size conditions in $b$, and for $a \leq C_a(2r+2)^3$, the local term `TBB.Ew` at a point $\gamma$ times $\|m(\gamma)\|^{2a}$ is at most $b^{C_5 (2r+2)^5} \max(1, 1/G(\gamma))^{40(r+1)^2}$ times the Bessel norm `TBB.jN2`. Here $m(\gamma)$ is a minor of $\gamma$ (`mnr`); we have not unfolded `Ew`. The proof is `wBp_of`. It takes $C_t$, hypotheses 1, 2 and 3, and these proved inputs: `LimSteps` (from `discrete_series_infinitesimal_character`), `k_finite_smooth`, `EndDiffW t` and `EndEqW t` (from `asymptotic_different_types`, `asymptotic_equal_types`, `wigExists` and `smooth_coefficient_bessel`), and `uniqueness_global`.
2. **Regularity of coefficients.** `Tied.coefCC1_of` takes $C_t$, hypothesis 1, `ZuckT t`, `k_finite_smooth` and `capelli_coefficient_continuity`. It gives `CoefCC1` with the constant $C_t + |c_3| + 2$: each $K$-finite coefficient with large gaps lies in the class `InCC`, which we have not unfolded.
3. **Assembly.** `WGlue.weighted_uniform_rotated_of_expansion_alt_alt` takes these two facts and hypothesis 4. It reduces the global bound to a bound at each place $v$ and each point $\gamma$ through `weighted_bound_rotated_of_one_place`, and proves that bound from `WBp`, `CoefCC1` and the frame bound that `OneBesselTor` gives.

`uniqueness_global` proves `UniqG`: two discrete series with the same parameter and gaps above $n^3 + 1$ are unitarily equivalent. It comes from `discrete_series_unique_large_gap`, whose threshold is $npq + 1$, and from $p, q \leq n$. This has the shape of the uniqueness part of Harish-Chandra's classification of the discrete series (Acta Math. 116, 1966), under an extra gap condition.

## In the Lean code

The theorem is in [WeightedBoundRotatedUniformOfCubicThreshold.lean](lean:CompanionTheory/AutomorphicTheory/BesselWaveGrids/WeightedBoundRotatedUniformOfCubicThreshold.lean#L30), with `wave_bessel_period_threshold` at line 23 and `uniqueness_global` at line 11. The lemmas it calls:

- `WEnd.wBp_of` and `WBp` in [PowFourLeRpowNineHalves.lean](lean:CompanionTheory/AutomorphicTheory/BesselWaveGrids/PowFourLeRpowNineHalves.lean#L106).
- `Tied.coefCC1_of` in [TiedNum.lean](lean:CompanionTheory/AutomorphicTheory/BesselWaveGrids/TiedNum.lean#L167).
- `WGlue.weighted_uniform_rotated_of_expansion_alt_alt` in [WeightedUniformRotatedOfExpansion.lean](lean:CompanionTheory/AutomorphicTheory/BesselWaveGrids/WeightedUniformRotatedOfExpansion.lean#L295).

The analysis is in `wBp_of` and in `weighted_uniform_rotated_of_expansion_alt_alt`, which are long proofs (both raise `maxHeartbeats` to 1,600,000). This theorem only connects them. Each hypothesis is used. `ZuckDualT t` is used only in step 1; the other hypotheses on $t$ are used in steps 1 and 2.
