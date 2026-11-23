---
id: cusp-height-upper
title: A uniform lower bound for the heights of points, restated
kind: theorem
decl: GlobalTheory.T.cusp_height_upper
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.CuspHeightUpperStatement
covers: 395
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`htU_of_given`](/entry/ht-u-of-given/), which has the real content. Its one user is [`nineGeoU_of_given`](/entry/nine-geo-u-of-given/), where it gives the constant $C_h$ and the height part `HtU` of `NineGeoU`.

## Statement

**Theorem.** Assume `Top.Given` and `FlatDegree` (proved without hypotheses by [`FlatDegree_holds`](/entry/flat-degree-holds/)). Then there is $C_h \in \mathbb{R}$ with this property. Let $E$ be a CM field, abelian over $\mathbb{Q}$, $II$ a full intersection system, $D_c$, $H_d$, $O$ component data with a component origin that is `admitted` at some $B_1$, $U$ a cusp weight for $O$, $M$ a complex model and $S'$ a tied bounded regularisation with potential $\log h_\mu + U/2$. Then `HtU` holds: for $B \geq 4fN^2$ and $1 \leq p \leq q$ there is $t_0 > 0$ such that for $0 < t' \leq t_0$ and each point $P$ of $X$,
$$\frac{II(P;\, \overline M_{B,p,q,t'})}{q\,\deg P} \geq -C_h\, f\, j'\, \Lambda_B - \frac{p}{q} K_A, \qquad \Lambda_B = \log(B\,\mathrm{rd}_E) + |\operatorname{Re} L'/L(1,\chi_d)|.$$

[The entry for `nineGeoU_of_given`](/entry/nine-geo-u-of-given/) defines the line $\overline M_{B,p,q,t'}$, the constants $f, j', K_A$ and the admission condition. A point $P$ is a horizontal multihomogeneous prime with `IsArithVar P 1` that contains the ideal of $X$, that is, the closure of an algebraic point of $X$. The constant $C_h$ does not depend on the field, the component or $U$.

## Proof

The proof applies `TopHt.htU_of_given`. Nothing else happens.

## In the Lean code

The theorem is in [CuspHeightUpperStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/CuspHeightUpperStatement.lean#L14). The proof is

```
first | exact @GlobalTheory.CompanionTheory.Ar.Cusp.TopHt.htU_of_given | ...
```

`htU_of_given` is in [CuspHeightUpper.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/CuspHeightUpper.lean#L120). It takes $C_h$ from `T.phiDeg_fibLat_le_of_isOFamily_of_isAdapted`, and bounds the height of a point through `T.small_points_over_number_field`, `T.cusp_intersection_height` and `T.cusp_intersection_finite`.

The name says "upper", but the conclusion is a lower bound for heights.
