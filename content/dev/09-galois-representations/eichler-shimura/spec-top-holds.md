---
id: spec-top-holds
title: The spectral input of the plans
kind: theorem
decl: UpperTheory.Gal.Int.Geo.Pl.specTop_holds
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.IntegralStructures.GeometricFlagBases.PrimeLevelLocalization.SpecTopHolds
covers: 930
status: drafted
drafted_by: writer@claude
---
This theorem proves `SpecTop`, one of the inputs of [planEx_holds](/entry/plan-ex-holds/). It is a renaming. The real content is in [specTopG](/entry/spec-top-g/) and [specData](/entry/spec-data/). Below it are 930 declarations.

## Statement

`SpecTop` is in [PrimeProj.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/PrimeLevelLocalization/PrimeProj.lean#L152). For a CM field $E$, an odd $n$, a prime $p$ and the data `Setup`, `Frame` and `Vec` that meet four side conditions, and for every finite set $X$ of primes, it gives an auxiliary prime $r_0 \notin X$, $r_0 \ne p$. At every level $N$ divisible by $r_0$, every family of Hecke elements $g_j$ with eigenvalues $\theta_j$ that pass the test `Seen` has one Hecke function $f$ with `Spec`. The entry [specTopG](/entry/spec-top-g/) gives the full statement.

## Proof

The proof is in [SpecTopHolds.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/PrimeLevelLocalization/SpecTopHolds.lean#L7):

```lean
theorem specTop_holds : SpecTop := UpperTheory.Gal.Spc.specTopG wtOf_holds
```

`specTopG` proves `WtOf → SpecTopG`. `WtOf` says that a twist of the representation `xi` by the transpose inverse has the weight `V.lam`. It is proved by `wtOf_holds` in `CharConjHolds.lean`.

## In the Lean code

`SpecTopG`, in [ExistsIdempotentHeckeOperatorWithRegularSupportAlt.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ScalarCommutation/ExistsIdempotentHeckeOperatorWithRegularSupportAlt.lean#L139), has the same text as `SpecTop`. Lean accepts the term because the two unfold to the same proposition. The duplicate adds a name and nothing else.
