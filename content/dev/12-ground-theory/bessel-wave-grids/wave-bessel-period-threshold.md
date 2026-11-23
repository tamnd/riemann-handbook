---
id: wave-bessel-period-threshold
title: The weighted one-place Bessel bound for a cubic threshold
kind: theorem
decl: CompanionTheory.WaveGrid.wave_bessel_period_threshold
module: CompanionTheory.AutomorphicTheory.BesselWaveGrids.WeightedBoundRotatedUniformOfCubicThreshold
covers: 955
status: drafted
drafted_by: writer@claude
---
This theorem proves the weighted one-place Bessel bound `WBp` for every constant $C_b$. It is step 1 of the proof of [the weighted bound from a cubic threshold](/entry/weighted-bound-rotated-uniform-of-cubic-threshold/), and that entry states `WBp`. Here we show how the endpoint estimates at one place give it. The proof fills the inputs of the lemma `wBp_of` and calls it.

## Statement

Let $t$ be a threshold function with $t(n, \varepsilon) \leq C_t n^3$ for $n \geq 1$, where $C_t \geq 0$. Assume `ZuckT t`, `ZuckDualT t` and `In91`. Then `WBp` $C_b$ holds for every real $C_b$.

## Proof

The proof supplies six inputs to `wBp_of`.

1. `LimSteps`, a conjunction of seven facts on coefficients of discrete series, from `discrete_series_infinitesimal_character`.
2. `k_finite_smooth`: $K$-finite vectors are smooth.
3. `EndDiffW t`, the endpoint bound for two different types $u \neq u'$. It is `endDiffW_of` applied to `asymptotic_different_types`. Given a coefficient $f$ in the space `Wsp` at a parameter $\lambda'$ near $\lambda$, a gap above $t(n, \varepsilon)$ plus a margin, the condition $|u_{l_0} - u'_{l_0}| \geq 30(r+1)^2 + 6$ and a big-cell expansion of $f$, it gives `ThmBpAt` with $n_0 = 0$. That bound reads: at a local point $\gamma$ with $G_p(\gamma) > 0$, $E_w(\gamma) \leq b^{C_4 (2r+2)^4} G_p(\gamma)^{-(2p_0 + n_0)}\, j_{N2}$.
4. `EndEqW t`, the same bound for equal types $u = u'$ with a gap of $2n_0 + 1$ at some $l$, and $n_0 = 30(r+1)^2 + 6$. It is `endEqW_of` applied to `asymptotic_equal_types` and `wigExists`.
5. `smooth_coefficient_bessel`, used by items 3 and 4.
6. `uniqueness_global`, proved in the same file.

Inside `wBp_of`, the two endpoint bounds give constants $C_1, C_A$ and $C_2, C'_A$. The lemma `weighted` gives $c_3$. Then
$$C_5 = 4|C_a| + \max(C_1, C_2, 0) + (C + 12)|C_a|, \qquad C_{g0} = 10^6 + C_t + |C_{A}| + |C'_{A}| + |c_3| + 100|C_a|.$$
The first part of `In91` gives a family of discrete series around $\lambda$. For each shift $\nu$ in a ball, item 3 or item 4 bounds $E_w$; the case hypothesis of `WBp` selects which one. `weighted` sums these bounds against the minor $m(\gamma)^{2a}$. The second part of `In91` bounds the moment `momL` by $b^{(C+12)(2r+2)^2 a} j_{N2}$. The rest is the arithmetic of exponents, which ends in $b^{C_5 (2r+2)^5}$.

The constant $C_b$ goes only to `EndDiffW` and to the condition `InDDplus2` in the case $u \neq u'$.

## In the Lean code

The theorem is in [WeightedBoundRotatedUniformOfCubicThreshold.lean](lean:CompanionTheory/AutomorphicTheory/BesselWaveGrids/WeightedBoundRotatedUniformOfCubicThreshold.lean#L23). `In91`, `WBp` and `wBp_of` are in [PowFourLeRpowNineHalves.lean](lean:CompanionTheory/AutomorphicTheory/BesselWaveGrids/PowFourLeRpowNineHalves.lean#L106). `EndDiffW` and `EndEqW` are in [EigStrOfMem.lean](lean:CompanionTheory/AutomorphicTheory/BesselWaveGrids/EigStrOfMem.lean#L128). We have not unfolded `Ew`, `Gp` or `jN2`.

The endpoint inputs come from [normal-form domination](/entry/normal-form-top-domination/) through `thmBpAt_top` and `thmBpAt_eqR_top`. In [EndpointDifferentTypesThreshold.lean](lean:CompanionTheory/AutomorphicTheory/BesselWaveGrids/EndpointDifferentTypesThreshold.lean#L11), `asymptotic_different_types` discards one hypothesis of `AsmDiff` (the membership `JF ∈ FFKB`) with `_`, and `asymptotic_equal_types` discards two of `AsmEq`. These hypotheses are not needed.
