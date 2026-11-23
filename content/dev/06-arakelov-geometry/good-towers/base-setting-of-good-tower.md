---
id: base-setting-of-good-tower
title: A base degree setting on each component of a good tower, restated
kind: theorem
decl: GlobalTheory.T.base_setting_of_good_tower
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.BaseSettingOfGoodTowerStatement
covers: 419
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`base_setting_of_good_origin`](/entry/base-setting-of-good-origin/), which has the real content. Its one user is [the volume theorem](/entry/volume-theorem-x-of-inputs/). There it is passed, for each $B$ and each component, to `slope_lower_base_settings`, which gives the lower bound `SlopeLower` with constant $C_h + C_u/2$.

## Statement

The statement is word for word that of [`base_setting_of_good_origin`](/entry/base-setting-of-good-origin/). In short: let $C_h, C_u$ satisfy `NineGeoU`, and assume `Out.WeilSt`, `PB.AgreementPos`, `PB.Proportional`, `Cmp.CmpSt`, `Top.Given` and `PtsIntegrableStatement`. Let $T$ be a root tower with a good origin with `Extra` over an abelian CM field, with $1 \leq q \leq p$ and at most $4fN^2$ bad primes, and $II$ a full intersection system. Then for each $B \geq 4fN^2$ and each component $c$, the tower has a strict base degree setting at $(B, c)$: a component setting with the positivity, height, mean and Stokes bounds, whose slope gives $\mathrm{PP}_{B,c}$ of the test polynomial.

## Proof

The proof applies `TopBase.base_setting_of_good_origin`. Nothing else happens.

## In the Lean code

The theorem is in [BaseSettingOfGoodTowerStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/BaseSettingOfGoodTowerStatement.lean#L24). The proof is

```
first | exact @GlobalTheory.CompanionTheory.Ar.Cusp.TopBase.base_setting_of_good_origin | ...
```

The caller, [VolumeTheoremOfInputs.lean](lean:Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/VolumeTheoremOfInputs.lean#L115), supplies `PB.Proportional` by `T.proportional'`.
