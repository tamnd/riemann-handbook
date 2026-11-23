---
id: sp4-in-alt
title: Symplectic four-dimensional automorphy from five inputs
kind: theorem
decl: UpperTheory.V.Cu.sp4In_alt
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.Sp4In
covers: 1047
status: drafted
drafted_by: writer@claude
---
This theorem proves `SymplecticFourImageDense`, the symplectic four-dimensional automorphy statement that feeds the counts $\mathrm{CountII}$ and $\mathrm{CountIII}$ of the [window bound](/proof/vwin/). It is a pass-through. The content is in [`main4_alt`](/entry/main4-alt/).

## Statement

**Theorem.** Assume `CohomologyHyp` (the Galois cohomology inputs: Poitou-Tate, the global Euler characteristic formula and the Greenberg-Wiles formula), `FerreroWashington`, `SeedIIAlt`, `SeedIVAlt` and `PMExAlt`. Then `SymplecticFourImageDense` holds.

`SymplecticFourImageDense` says: for a host datum $h$, a prime $l \neq 2$, an exponent $0 < e < t$, a character $\psi$ and good raw data $D$ in case II or case III of $(h, e, \psi)$, the data $D$ is finite, has no end (we have not unfolded `Fin0` or `NoEnd`), and there is $\iota$ such that each irreducible piece of $D$ is automorphic in the sense of `IsAut4Alt`. See [`main4_alt`](/entry/main4-alt/) for more.

## Proof

The proof is `main4_alt hC hF hFit s2 s4 hP`. The theorem [`main4_alt`](/entry/main4-alt/) proves `AutomorphyRankFourDense`, which is the implication from six inputs to `SymplecticFourImageDense`. This theorem passes on its five hypotheses and adds the sixth, `HFit`. The proof of `HFit` is `hFit`, and it holds by definition: a `Four` datum carries the fields of `Three0`, and `Fit` asks for `Ok` and, in case III, `Three0`.

## In the Lean code

The theorem is in [Sp4In.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/Sp4In.lean#L13). `hFit` is in [CuspidalTwists/Sp4In.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/CuspidalTwists/Sp4In.lean#L42). The only user is [`sp4In0_alt`](/entry/sp4-in0-alt/), which supplies the five hypotheses from the printed hypotheses `hH`. It takes `SeedIIAlt` from [`seedIIs_alt`](/entry/seed-iis-alt/) and `FerreroWashington` from `FW.ferreroWashington`.

`HFit` is a hypothesis of `AutomorphyRankFourDense`, but it is true by definition. So `AutomorphyRankFourDense` has one hypothesis that it does not need.
