---
id: nine-geo-u-of-given
title: Constants for the positivity, height and mean bounds
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Cusp.TopNine.nineGeoU_of_given
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.ExistsGeometricHeightConstants
covers: 571
status: drafted
drafted_by: writer@claude
---
This theorem gives constants $C_h, C_u$ with `NineGeoU`: on every admitted component, the twisted cusp lines are positive, the heights of points are at least $-C_h$ times an error term, and the mean of the cusp weight is at most $C_u$ times it. It joins three lemmas. Its statement form is [`T.exists_geometric_height_constants`](/entry/exists-geometric-height-constants/). In [the good tower theorem](/entry/good-tower-and-volume/) the constants go to the volume theorem, and [`base_setting_of_good_origin`](/entry/base-setting-of-good-origin/) applies `NineGeoU` to each component.

## Statement

We use the objects of [the relay theorem](/entry/relay-cusp-weight-regularisations-tied/): a component datum $D_c$ on $X$ with $f = \#\mathrm{CMType}(H)$, $N$, $j$, $j' = N - j$, a positive line $\overline A'$ and a constant $K_A$, the Hodge line $\overline\mu$ and a cusp weight $U$. Let $\Lambda_B = \log(B\,\mathrm{rd}_E) + |L_H|$ (`abelian₂`), with $\mathrm{rd}_E$ and $L_H$ as in [the base setting](/entry/base-setting-of-good-origin/). For a bounded regularisation $S'$ with potential $\log h_\mu + U/2$, let $\overline M_{B,p,q,t'}$ be the line of multidegree $q\,(a_\mu + \sum_{r \in S_B} \deg v_r) + p\,a'$ with metric $(h_{\mathrm{ref}}\, e^{\psi_{t'}})^q \prod_{r \in S_B} v_r^q\, h_{A'}^p$ (`MUc`), replaced by a smooth conjugation-invariant line with the same metric on $X$ when one exists (`smoothRepConj`). Here $S_B$ is the primes of $D_c$ up to $B$, $v_r$ the vertical factors, $\psi_{t'}$ the regularised weight of $S'$.

`NineGeoU` $C_h$ $C_u$ says: for all data over an abelian CM field with $II$ full, the component origin admitted at some $B_1$, $U$ a cusp weight and $S'$ tied,

1. (`PosU`) for $B \geq 4f + 2$ and $1 \leq p \leq q$, the line $\overline M_{B,p,q,t'}$ is semipositive, nef on the fibres and ample on the generic fibre for all small $t' > 0$;
2. (`HtU`) for $B \geq 4fN^2$ and $1 \leq p \leq q$, for small $t'$ and each point $P$ of $X$ (a horizontal prime with `IsArithVar P 1`, that is, the closure of an algebraic point), with $II(P; \cdot)$ the intersection number that the system $II$ gives on $P$,
$$\frac{II(P;\, \overline M_{B,p,q,t'})}{q\,\deg P} \geq -C_h\, f\, j'\, \Lambda_B - \frac{p}{q} K_A;$$
3. (`MeanU`) if $1 \leq j'$ and $3j' + 1 \leq N$, then for $B \geq 4fN^2$ the mean of $U$ over $X(\mathbb{C})$ against the measure of $\log h_\mu$ (by the name `maDensity`, a Monge-Ampère density), divided by $\deg_\mu$, is at most $C_u\, f\, j'\, \Lambda_B$.

The admission condition (`admitted`) says that $Y$ is global, the origin is good, $S_0$ is the set of primes dividing $2\,d_E\,M'$, $\#S_0 \leq 4fN^2$, $B_1 \geq 4f + 2$, the primes of $D_c$ are the primes up to $B_1$ outside $S_0$, and $j' \leq j$.

**Theorem.** If `Top.Given`, `Out.WeilSt` and `FlatDegree` hold, then there are $C_h, C_u$ with `NineGeoU` $C_h$ $C_u$.

## Proof

Take $C_h$ from [`T.cusp_height_upper`](/entry/cusp-height-upper/) (with `Top.Given` and `FlatDegree`) and $C_u$ from `T.cusp_volume_sum` (with `Top.Given`). For given data, `T.intersection_degree_lower` (with `Top.Given` and `Out.WeilSt`) gives `PosU`, and the two lemmas give `HtU` and `MeanU`.

## In the Lean code

The theorem is in [ExistsGeometricHeightConstants.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/ExistsGeometricHeightConstants.lean#L17). `NineGeoU`, `PosU`, `HtU`, `MeanU` and `admitted` are in [NineGeoU.lean](lean:Development/AutomorphicSpectrum/Statements/GeometryStatements/NineGeoU.lean#L59).

The constants are chosen before the field and the component. `Out.WeilSt` is used only for `PosU`, which has no constant, and `intersection_degree_lower` does not take the cusp weight hypothesis. `NineGeoU` has three parts, not nine as the name suggests. We have not unfolded `ptsIntegral` beyond its definition as a sum of `maDensity` terms over the sheets of a linear projection.
