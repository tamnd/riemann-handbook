---
id: exists-geometric-height-constants
title: Constants for the positivity, height and mean bounds, restated
kind: theorem
decl: GlobalTheory.T.exists_geometric_height_constants
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.ExistsGeometricHeightConstantsStatement
covers: 572
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`nineGeoU_of_given`](/entry/nine-geo-u-of-given/), which joins the three lemmas that do the work. Its one user is [the good tower theorem](/entry/good-tower-and-volume/). That proof calls it with `FlatDegree_holds` and passes the constants to [the volume theorem from its inputs](/entry/volume-theorem-of-inputs/).

## Statement

The statement is word for word that of [`nineGeoU_of_given`](/entry/nine-geo-u-of-given/), which unfolds `NineGeoU`. In short: if `Top.Given`, the Weil pairing statement `Out.WeilSt` and `FlatDegree` (proved without hypotheses by [`FlatDegree_holds`](/entry/flat-degree-holds/)) hold, then there are real constants $C_h, C_u$ such that on every admitted component of the Shimura variety, for every cusp weight $U$ and tied regularisation $S'$:

- the twisted lines $\overline M_{B,p,q,t'}$ are positive for small $t'$;
- the heights of points for these lines, divided by $q$, are at least $-C_h\, f\, j'\, \Lambda_B - (p/q) K_A$;
- the mean of $U$ is at most $C_u\, f\, j'\, \Lambda_B$ when $1 \leq j'$ and $3j' + 1 \leq N$,

where $\Lambda_B = \log(B\,\mathrm{rd}_E) + |\operatorname{Re} L'/L(1,\chi_d)|$.

## Proof

The proof applies `TopNine.nineGeoU_of_given`. Nothing else happens.

## In the Lean code

The theorem is in [ExistsGeometricHeightConstantsStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/ExistsGeometricHeightConstantsStatement.lean#L14). The proof is

```
first | exact @GlobalTheory.CompanionTheory.Ar.Cusp.TopNine.nineGeoU_of_given | ...
```

The name says "height constants", but only $C_h$ is a height constant; $C_u$ bounds the mean of the cusp weight. Its caller is [GoodTowerVolumeTheorem.lean](lean:Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/GoodTowerVolumeTheorem.lean#L49).
