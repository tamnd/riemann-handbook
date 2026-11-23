---
id: count-ii-and-count-iii-of-prints-h-of-sp4-in
title: The counts in cases II and III from the printed hypotheses
kind: theorem
decl: UpperTheory.V.HV.DescentVanishingReductions.countII_and_countIII_of_printsH_of_sp4In
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.AdjointLiftingOfCohomology
covers: 808
status: drafted
drafted_by: writer@claude
---
This theorem proves $\mathrm{CountII}$ and $\mathrm{CountIII}$, two of the four counts of the [window bound](/proof/vwin/). It is a pass-through. It gives nine inputs to [`sp4Main_alt`](/entry/sp4-main-alt/). The content is in [`main_big`](/entry/main-big/). Its user [`vwin_of_hypotheses_H_E_alt`](/proof/vwin/) calls it with `SymplecticFourImageDense` from [`sp4In0_alt`](/entry/sp4-in0-alt/).

## Statement

**Theorem.** Assume $\mathrm{HypothesesH'}$, `LemmaK` $C_K$ for some $C_K$, and `SymplecticFourImageDense`. Then $\mathrm{CountII}$ and $\mathrm{CountIII}$ hold.

$\mathrm{CountII}$ says: for each primitive character $\chi$ there is $C$ such that for each host $h$ with character $\chi$ and $h.\mathrm{Big}\ t$, each prime $l \ne 2$, each $0 < e < t$ and each $\psi$ in $h.X\ c\ e$ in case II, the length $V_{\mathrm{len}}(e, \psi)$ is finite and $V_n(e, \psi) \log l \le (l N e)^C$. $\mathrm{CountIII}$ is the same for case III. We have not unfolded `Chr.V'`, which defines $V_{\mathrm{len}}$.

## Proof

The proof applies `sp4Main_alt` to these inputs:

- `SymplecticFourImageDense`, the hypothesis;
- `CohomologyHyp`: the field `.coh` of `adjoint_lift_of_prints hH`;
- `LemmaM`, `LemmaM'` and `LemmaP`, from `Alg.M.main_holds`, `Alg.M.mprime_holds` and `Alg.lemmaP`;
- `NumberSp4Alt`, from `numberSp4_n_alt` on the classical part of $\mathrm{HypothesesH'}$;
- `RigiditySymplecticFour`, from `rigSp4_alt` on `adjoint_lift_of_prints hH` and `adjoint_lifting_of_cohomology hH`;
- `X.CorX`, from `X.corX X.lemmaX X.residual_bernoulli_nonvanishing`;
- `SoV` and `SoFin`, from `X.soBar` and `X.soFin`. Both take `LemmaK` $C_K$, Poitou-Tate duality (`pt_s hN`), local finiteness and local Tate duality.

So Lemma K enters only through `SoV` and `SoFin`.

## In the Lean code

The theorem is in [AdjointLiftingOfCohomology.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/AdjointLiftingOfCohomology.lean#L33). `CountII`, `CountIII` and `CountShape` are in [Counts.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/Counts.lean#L60). `CaseII` and `CaseIII` are in [DirichletPrimeToLPartMulLPowerPart.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/DirichletPrimeToLPartMulLPowerPart.lean#L212).

`adjoint_lift_of_prints` (line 27) builds a full `UnramifiedInputs` structure. This theorem uses only its field `.coh` directly, and passes the whole structure to `rigSp4_alt`.
