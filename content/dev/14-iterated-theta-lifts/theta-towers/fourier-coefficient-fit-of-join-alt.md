---
id: fourier-coefficient-fit-of-join-alt
title: The constant function fits, from the joined inputs
kind: theorem
decl: GlobalTheory.BigTop.Fun.Close.fourier_coefficient_fit_of_join_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.FourierCoefficientFitOfJoin
covers: 4155
status: drafted
drafted_by: writer@claude
---
This theorem supplies the statement `ConstantFunctionFits Fld` to the last node of the trunk, [HypsAlt is nonempty from the closed bound](/step/nonempty-hyps/), in item 3 of its proof. It unpacks one hypothesis, converts another, and calls [the fitted function theorem](/entry/fitted-function-at-zero-close-alt/). That theorem has the real content. Below it are 4,155 declarations.

## Statement

Assume:

1. the record [`ThetaLocalInputs`](/step/theta-local-inputs-def/) of 53 named inputs;
2. `JoinOut`, the conjunction of the five propositions `ToricDenominator`, `Transport`, `TwistedTransport`, `ZetaDenominators` and `Refl`;
3. `HeckeTateFunctionalEquation`: for a unitary Hecke character $\chi$ of a field $E$ with a CM type and nonzero infinity type $n$, there are completed L-functions $\Lambda$ of $\chi$ and $\Lambda'$ of $\chi^{-1}$ with $\Lambda(s) = \varepsilon_\infty(n)\,\varepsilon_f(\chi, s)\,\Lambda'(1-s)$;
4. [`ThetaIntegralsAgree`](/step/theta-integrals-agree-def/) and [`LocalMatching`](/step/local-matching-def/);
5. `FunctionalsSeparate`;
6. `LambdaLowerBound₂`.

Then `ConstantFunctionFits Fld` holds. The [next entry](/entry/fitted-function-at-zero-close-alt/) states it.

Item 3 is the functional equation of Hecke L-functions, proved in Tate's thesis (J. Tate, *Fourier analysis in number fields and Hecke's zeta-functions*, 1950; in Cassels and Fröhlich, *Algebraic Number Theory*, 1967). We have not unfolded the factors `archEps` and `finEps`.

## Proof

The proof splits `JoinOut` into its five parts. `HeckeTateFunctionalEquation.abs` converts item 3 to the form $\Lambda(s) = \varepsilon\, N^{1/2 - s}\, \Lambda'(1-s)$ with $|\varepsilon| = 1$, where $N$ is $|d_E|$ times the norm of the conductor. Then it calls `fittedFunction_at_zero_close_alt` with all the inputs.

## In the Lean code

The theorem is in [FourierCoefficientFitOfJoin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FourierCoefficientFitOfJoin.lean#L12). It calls:

- `fittedFunction_at_zero_close_alt`, in [FittedFunctionAtZeroClose.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FittedFunctionAtZeroClose.lean#L42);
- `HeckeTateFunctionalEquation.abs`, in [AbsNormDifferentEqProd.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/AbsNormDifferentEqProd.lean#L130).

The proof only passes hypotheses along. `JoinOut` is defined in [HypothesisBundleConversions.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/HypothesisBundleConversions.lean#L7). The name speaks of a Fourier coefficient fit. No Fourier coefficient occurs in the statement: the conclusion is `ConstantFunctionFits`, and "join" refers to the hypothesis `JoinOut`.
