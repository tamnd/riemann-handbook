---
id: closed-of-orthogonal-lattice
title: Supplying the coefficient map to the chain
kind: theorem
decl: Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_orthogonal_lattice
module: Formalism.SharpRestriction.GrowthBounds.MonomialFactorials.ClosedOfOrthogonalLattice
covers: 2625
status: drafted
drafted_by: writer@claude
---
This theorem is the sixth link of the chain of reductions that proves the averaged bad-share bound `IntegralityFromMetricForLargeConstants D` (see [`theorem_A_closed_form_holds`](/entry/theorem-a-closed-form-holds/)). [`closed_of_orthogonal_basis`](/entry/closed-of-orthogonal-basis/) calls it. It adds the proved statement `RestFunY` and passes everything to [`closed_of_symmetric_dims`](/entry/closed-of-symmetric-dims/). It has no mathematical content of its own.

## Statement

`OrthLat` is stated in [`closed_of_orthogonal_basis`](/entry/closed-of-orthogonal-basis/), and `SymmetryWindowOnAdmissible D` in [`integralityFromMetric_of_orthBasisLat`](/entry/integrality-from-metric-of-orth-basis-lat/).

**Theorem.** For each datum $D$, `OrthLat` and `SymmetryWindowOnAdmissible D` imply `IntegralityFromMetricForLargeConstants D`.

## Proof

The proof is one term:

```
closed_of_symmetric_dims D restFunY_proved hO h
```

`RestFunY` says the following. Let $O$ be a domain, $K$ its fraction field `KK O` (an `abbrev` for `FractionRing O` in GrowthBounds/ObjPol.lean L23), $\iota \colon \mathbb{Q}_p \to K$ a ring map, and $f \colon K \to \mathbb{Q}_p$ an additive map with $f(\iota(a)x) = a f(x)$. Apply $f$ to each coefficient of a polynomial $y$. If $y$ is in the space `Yjt` over $K$, the result is in the space `Y` over $\mathbb{Q}_p$ for the same letters and conditions. `restFunY_proved` proves it: the map keeps the support condition (`cmap_mem_restrictSupport`) and each of the conditions `YCond` (`cmap_ycond`). We have not unfolded `Yjt`, `Y` or `YCond`.

## In the Lean code

The theorem is in [ClosedOfOrthogonalLattice.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/ClosedOfOrthogonalLattice.lean#L8). `RestFunY` and the coefficient map `cmap` are in [RestDecompProved.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/RestDecompProved.lean#L13), and `restFunY_proved` is in [CmapMemRestrictSupport.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/CmapMemRestrictSupport.lean#L145).

Both hypotheses `hO` and `h` pass through unchanged. The name speaks of an orthogonal lattice, but the only new input is `RestFunY`, which is about coefficient maps. The use of `RestFunY` is further down the chain, below [`closed_of_symmetric_windows`](/entry/closed-of-symmetric-windows/).
