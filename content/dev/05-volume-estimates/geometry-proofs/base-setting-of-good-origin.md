---
id: base-setting-of-good-origin
title: A base degree setting on each component of a good tower
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Cusp.TopBase.base_setting_of_good_origin
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.BaseSettingOfGoodTower
covers: 418
status: drafted
drafted_by: writer@claude
---
For a good root tower, this theorem builds on each component, at each level $B$, an analytic setting: a cusp weight, regularised metrics and the bounds of `NineGeoU`, with an identity that turns the intersection number of the tower into the slope of the setting. Its statement form is [`T.base_setting_of_good_tower`](/entry/base-setting-of-good-tower/). In [the volume theorem](/entry/volume-theorem-x-of-inputs/), `slope_lower_base_settings` turns these settings into the lower bound `SlopeLower` with constant $C_h + C_u/2$.

## Statement

Root towers $T$, good origins $o$ and $\mathrm{PP}_{B,c}$ are as in [the volume theorem](/entry/volume-theorem-x-of-inputs/); component data, cusp weights and regularisations as in [the relay theorem](/entry/relay-cusp-weight-regularisations-tied/). Let $f = \#\mathrm{CMType}(H)$, $N = p + q$, $\mathrm{rd}_E = |d_E|^{1/[E:\mathbb{Q}]}$ and $L_H = \operatorname{Re} L'/L(1, \chi_d)$.

**Theorem.** Let $C_h, C_u$ satisfy `NineGeoU`. Assume the Weil pairing statement `Out.WeilSt`, `PB.AgreementPos`, `PB.Proportional`, `Cmp.CmpSt`, `Top.Given` and `PtsIntegrableStatement`. Let $E$ be an abelian CM field, $Y$ a global integral model, $T$ a root tower for $N$, $o$ a good origin of $Y$ for $T$ with `Extra`, and $II$ a full intersection system. Suppose $1 \leq q \leq p$ and that $T$ has at most $4fN^2$ bad primes. Then for each $B \geq 4fN^2$ and each component $c$ there are a component datum $D$ with $N(D) = N$ and $j(D) = j(T)$ and a component setting $X$ on $D$ (`ComponentSetting`: a Hodge datum, a cusp datum, a model, tied regularisations $S, S'$, and the numbers $\mathrm{rd}_E, L_H$) such that:

- the twisted lines $\overline M_{B,p,q,t'}$ are semipositive, nef on the fibres, ample on the generic fibre and invariant under conjugation for small $t'$ (`CuspBundlePos`, `MUConjInvariant`);
- the height bound of `HtU` with constant $C_h$ holds at points off and on the boundary (`HtInterior`, `HtBoundary`), and the cusp mean bound with $C_u$ (`CuspMean`);
- $\deg_\mu > 0$, the limit $\mathrm{arLim}$ of the arithmetic self-intersections of the regularised line exists, and the Stokes bound `StokesAt` holds;
- $\mathrm{PP}_{B,c}(\mathrm{testPoly}) = \mathrm{sl}(X, B)\,(\dim + 1)\,\mathrm{vol}(c)\,\mathrm{testDeg}$, where $\mathrm{sl}(X, B) = \mathrm{arLim} / ((n+1)\deg_\mu)$.

## Proof

1. `host_numbers` gives $f \geq 1$, so $B \geq 4f + 2$. The helper `genPt_eq_of_factor` shows that the root origin $o.\mathrm{Or}(B, c)$ and the component $c$ have the same generic point.
2. Let $S_1$ be the primes $r \leq B$ outside the bad set. `T.full_intersection_generic_bound` (with `Top.Given`, `Out.WeilSt`) gives $D_c$, $H_d$ and a component origin $O$ with that generic point, with primes $S_1$, $j = p$, and Hodge-Tate freeness at all primes of the bad set and of $S_1$. So $O$ is good and the data are `admitted` at $B$.
3. [`T.cusp_weight_regularisations_tied`](/entry/t-cusp-weight-regularisations-tied/) gives $U, M, S, S'$.
4. `NineGeoU` gives `PosU`, `HtU` and `MeanU`. Then `T.corrected_weight_regularization` builds $X$ with $X.H = H_d$, cusp weight $U$ on $X^o$, and the five properties of the first two items.
5. `T.good_origin_intersection_tower` (with `AgreementPos`, `Proportional`, `CmpSt`, `PtsIntegrableStatement`, `Extra`) gives $\deg_\mu > 0$, the existence of $\mathrm{arLim}$ and the identity for $\mathrm{PP}_{B,c}$.
6. `T.intersection_final_estimate` gives `StokesAt`.

The rest is bookkeeping.

## In the Lean code

The theorem is in [BaseSettingOfGoodTower.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/BaseSettingOfGoodTower.lean#L45), after the helper `genPt_eq_of_factor` (line 30). The conclusion `RootTower.HasBaseDegreeSettingStrict` is in [HasBaseDegreeSettingStrict.lean](lean:Development/AutomorphicSpectrum/Definitions/GlobalGeometry/HasBaseDegreeSettingStrict.lean#L16).

The proof takes `SemiAbelianHomExtension`, `ResKStatement`, `GagaSections`, `PB.Inputs` and `Prov.An` out of `Top.Given` by position (line 100). It calls `full_intersection_generic_bound` with the switch `false`, so the side with $j = p$ is used, and $j' = q \leq j$ needs $q \leq p$. All hypotheses are used. We have not unfolded `CuspData`, `StokesLimit.Hyp`, `testPoly` or `testDeg`.
