---
id: weighted-bound-rotated-uniform-of-hyps-g
title: The weighted bound on rotated points from the representation inputs
kind: theorem
decl: CompanionTheory.WaveGrid.weighted_bound_rotated_uniform_of_hypsG
module: CompanionTheory.AutomorphicTheory.BesselWaveGrids.WeightedBoundRotatedUniformOfHypsG
covers: 1221
status: drafted
drafted_by: writer@claude
---
This theorem proves the [weighted bound on rotated points](/entry/weighted-bound-rotated-uniform/) from one hypothesis, `HypsG`, which the caller proves. The proof only passes the hypothesis to other theorems. The content is in [the bound from the inputs](/entry/uniform-bessel-rank-three-of-inputs/) and in [the bound from a cubic threshold](/entry/weighted-bound-rotated-uniform-of-cubic-threshold/).

## Statement

`HypsG` is the conjunction of seven statements on discrete series of unitary groups in $n = 2r + k + 1$ variables: `InputsG`, `SmoothCyc`, `InfCharG` (the infinitesimal character of a discrete series), `DSExistG` (a discrete series with a given parameter exists when its gaps are large), `ZuckG` (tensor products of a family of discrete series with finite-dimensional representations), `PoulsenG` (invariant forms on smooth vectors) and `HCFdegG` (the formal degree is a positive constant times an explicit function `fdegHC` of the parameter).

**Theorem.** If `HypsG` holds, then `WeightedBoundRotatedUniform` holds.

## Proof

1. `wave_inputs_of_hypotheses_global` turns `HypsG` into `In91`. This is a pair of statements. The first says that a discrete series whose parameter meets the numerical conditions `Num` lies in a family of discrete series at the shifted parameters $\lambda + \nu$, $|\nu|_1 \leq q_0$. The second gives, for a local Bessel datum, an expansion of the Bessel function on the big cell and a bound for its moments.
2. `one_bessel_torus_bound D (le_refl 100)` gives `OneBesselTor D 100` for each datum $D$. It says: for a $K$-finite coefficient $f$ with large gaps and for $\kappa, \tau > 0$, there are a coefficient $f_1$ and a constant $C \neq 0$ such that, after the substitution `cj` in $\kappa, \tau$ (not unfolded), the Bessel function and the orbital integrals of $f_1$ are $C$ times those of $f$.
3. `uniform_bessel_rank_three_of_inputs` takes these two facts and gives the bound.

## In the Lean code

The theorem is in [WeightedBoundRotatedUniformOfHypsG.lean](lean:CompanionTheory/AutomorphicTheory/BesselWaveGrids/WeightedBoundRotatedUniformOfHypsG.lean#L7). The proof is one line.

- `HypsG` is in [IsDSOfIsDG.lean](lean:CompanionTheory/AutomorphicTheory/PieriRules/ThetaBesselIsometries/IsDSOfIsDG.lean#L79).
- `WEnd.wave_inputs_of_hypotheses_global` is in [WaveInputsOfHypothesesGlobal.lean](lean:CompanionTheory/AutomorphicTheory/BesselWaveGrids/WaveInputsOfHypothesesGlobal.lean#L37), and `In91` in [PowFourLeRpowNineHalves.lean](lean:CompanionTheory/AutomorphicTheory/BesselWaveGrids/PowFourLeRpowNineHalves.lean#L70).
- `RankOne.one_bessel_torus_bound` is in [FrameBesselBoundOfLargeConstants.lean](lean:CompanionTheory/AutomorphicTheory/RankOneTori/FrameBesselBoundOfLargeConstants.lean#L223), and `OneBesselTor` in [IsPtRepTrDat.lean](lean:Formalism/SharpRestriction/CuspSpanNormBounds/IsPtRepTrDat.lean#L14).

`HypsG` is used only through `In91`. The proof of `wave_inputs_of_hypotheses_global` passes `HypsG` whole to three lemmas that we have not opened, so we do not know which of the seven parts they use. The constant $100$ in step 2 is the least constant that `one_bessel_torus_bound` accepts.
