---
id: closed-of-orthogonal-basis
title: From an orthogonal basis to a good orthogonal family
kind: theorem
decl: Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_orthogonal_basis
module: Formalism.SharpRestriction.GrowthBounds.MonomialFactorials.ClosedOfOrthogonalBasis
covers: 2631
status: drafted
drafted_by: writer@claude
---
This theorem is the fifth link of the chain of reductions that proves the averaged bad-share bound `IntegralityFromMetricForLargeConstants D` (see [`theorem_A_closed_form_holds`](/entry/theorem-a-closed-form-holds/)). [`integralityFromMetric_of_orthBasisLat`](/entry/integrality-from-metric-of-orth-basis-lat/) calls it. It combines `OrthBasisLat` and `GoodLeSmall` into one lattice statement `OrthLat`, and passes the rest on to [`closed_of_orthogonal_lattice`](/entry/closed-of-orthogonal-lattice/).

## Statement

Lattices $L$ and pairings $B$ are as in [`closed_of_minimal_vector`](/entry/closed-of-minimal-vector/). `OrthBasisLat` and `GoodLeSmall` are stated in [`closed_of_orthogonal_splitting`](/entry/closed-of-orthogonal-splitting/) and [`closed_of_splitting_matrix`](/entry/closed-of-splitting-matrix/). Let $\mathrm{bad}(B, L, k) = \operatorname{rk} L - g(B, L, k)$, with the good count $g$ and truncated subtraction in $\mathbb{N}$.

- `OrthLat`: if $p \ne 2$, then for each $k \in \mathbb{Z}$ there are $\mathbb{Z}_p$-linearly independent $e_1, \dots, e_n \in L$ with $B(e_a, e_b) = 0$ for $a \ne b$, $B(e_a, e_a) \ne 0$ and $v_p(B(e_a,e_a)) \le k$ for all $a$, and
$$ n \le \operatorname{rk} L \le n + \mathrm{bad}(B, L, k). $$
- `SymmetryWindowOnAdmissible D`: the window count with the symmetry of the block pairing, stated in [`integralityFromMetric_of_orthBasisLat`](/entry/integrality-from-metric-of-orth-basis-lat/).

**Theorem.** For each datum $D$, `OrthBasisLat`, `GoodLeSmall` and `SymmetryWindowOnAdmissible D` imply `IntegralityFromMetricForLargeConstants D`.

## Proof

The lemma `orthLat_of'` proves `OrthLat` from `OrthBasisLat` and `GoodLeSmall`, through the intermediate statement `OrthCount`. Let $f_1, \dots, f_m$ be an orthogonal basis of $L$ from `OrthBasisLat`, so $\operatorname{rk} L = m$. Let $S$ be the set of $a$ with $B(f_a, f_a) \ne 0$ and $v_p(B(f_a,f_a)) \le k$. Take the family $(f_a)_{a \in S}$. It is orthogonal and linearly independent, and $|S| \le m$. `GoodLeSmall` gives $g(B, L, k) \le |S|$, so $m \le |S| + (m - g(B,L,k))$. Then `closed_of_orthogonal_lattice` is applied to `OrthLat` and `SymmetryWindowOnAdmissible D`.

## In the Lean code

The theorem is in [ClosedOfOrthogonalBasis.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/ClosedOfOrthogonalBasis.lean#L8). Its proof is one term:

```
closed_of_orthogonal_lattice D (orthLat_of' hB hG) h
```

`OrthCount`, `orthCount_of`, `orthLat_of` and `orthLat_of'` are in [OrthCountOf.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/OrthCountOf.lean#L18), lines 18 to 75. `OrthLat` is in [BePhiAddLeft.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/BePhiAddLeft.lean#L9). The family in `orthCount_of` is $f$ composed with the order embedding of $S$, and the last inequality is closed by `omega`.

The hypothesis `h` passes through unchanged. The only content is `orthLat_of'`, a short counting step. `OrthCount` and `GoodLeSmall` have no hypothesis $p \ne 2$; only `OrthBasisLat` needs it.
