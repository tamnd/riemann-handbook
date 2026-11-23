---
id: exists-unitary-group-datum-of-vector-exponent-spectral
title: Plans from the vector, exponent and spectral inputs
kind: theorem
decl: UpperTheory.Gal.Int.Geo.Pl.exists_unitaryGroupDatum_of_vector_exponent_spectral
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.IntegralStructures.GeometricFlagBases.PrimeLevelLocalization.ExistsUnitaryGroupDatumOfVectorExponentSpectral
covers: 545
status: drafted
drafted_by: writer@claude
---
This theorem proves `PlanEx` from three inputs, and [planEx_holds](/entry/plan-ex-holds/) applies it. It is a pass-through: it puts fifteen facts into one structure and calls `planEx_of`. The parent entry describes `planEx_of`. The spectral input has its content in [specTopG](/entry/spec-top-g/) and [specData](/entry/spec-data/). Below this theorem are 545 declarations.

## Statement

```lean
theorem exists_unitaryGroupDatum_of_vector_exponent_spectral
    (h1 : VecEx) (h2 : ExpOf) (h3 : SpecTop) : PlanEx
```

`VecEx` gives a vector datum `Vec x U w₀ Up` for each automorphic space $U$ that meets its hypotheses. `ExpOf` says that each `V.lam τ` is antitone and matches the weight jumps of $U$ with Hodge exponents. `SpecTop` is the statement of [specTop_holds](/entry/spec-top-holds/). All three are in `PrimeProj.lean`.

## Proof

The proof is in [ExistsUnitaryGroupDatumOfVectorExponentSpectral.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/PrimeLevelLocalization/ExistsUnitaryGroupDatumOfVectorExponentSpectral.lean#L37). It builds the structure `All` of [SameKTrans.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/PrimeLevelLocalization/SameKTrans.lean#L21) and applies `planEx_of`. The three inputs fill the fields `vec`, `exp` and `spec`. Twelve proved lemmas fill the other fields, for example `frameEx_holds`, `memEx_holds`, `siteEx_holds`, `congOf_holds`, `datEx_holds`, `rootsAlg_holds` and `satCard`. Five of the twelve (`memEx_holds`, `siteTriv_holds`, `siteEx_holds`, `goodOf_holds` and `congOf_holds`) are proved earlier in the same file.

## In the Lean code

The name says "exists unitary group datum", but the conclusion is `PlanEx`. The words "vector exponent spectral" name the three inputs, not the result.
