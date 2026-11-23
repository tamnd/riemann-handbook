---
id: geometric-parameter-uniform-alt
title: Linked bundles at the parameters of an extension, second name
kind: theorem
decl: GlobalTheory.T.geometric_parameter_uniform_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ExBLIsLinkedPrmRStatement
covers: 781
status: drafted
drafted_by: writer@claude
---
This theorem is a second name of [`exBL_isLinked_prmR_alt`](/entry/ex-bl-is-linked-prm-r-alt/), which has the content. It gives the `ExBL` statement that [the bundles at large unramified exponents](/entry/member-bundles-large-unramified-exponents-alt/) uses, and that entry describes `ExBL` in words.

## Statement

**Theorem.** Assume ten published inputs, from `GreenCuspidal` to `WeberRayFieldSt`, and `RayField`. Let $h_L$ prove `RecTExists`, let $N$ be a norm choice extension, $\Gamma$ a `GeoP` and $p$ the parameters `parametersOfExtension N SExt.none Γ`. Assume that each datum accepted by $N$ has an `extensionWithLaw`, that `PositionMv` $p.s$ holds, and that eventually every point $q$ of the slots of $p.s$ satisfies `MultEq`. Then `ExBL KPx (IsBuiltE p.s) (IsGoodE p.s) (BundleLinkage p)`.

## Proof

The proof is `exact exBL_isLinked_prmR_alt`, tried in three forms by `first`.

## In the Lean code

The theorem is in [ExBLIsLinkedPrmRStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExBLIsLinkedPrmRStatement.lean#L18). Its callers are in [ExistsBaseLatticeOfPrime.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsBaseLatticeOfPrime.lean#L55) and [ExistsWeilBlockNeAtMember.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsWeilBlockNeAtMember.lean#L31).

Odd points:

- The parameters $p$ are a variable with the hypothesis $p = $ `parametersOfExtension N SExt.none Γ`. The callers pass `rfl`.
- The name speaks of a uniform geometric parameter. The statement is about linked bundles, and $\Gamma$ enters only through $p$.
- In ExistsBaseLatticeOfPrime.lean the `PositionMv` hypothesis has the name `intersection_update_fsHerm_neg_one`, at [line 42](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsBaseLatticeOfPrime.lean#L42).
