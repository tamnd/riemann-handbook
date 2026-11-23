---
id: closed-of-orthogonal-splitting
title: An orthogonal basis from repeated splitting
kind: theorem
decl: Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_orthogonal_splitting
module: Formalism.SharpRestriction.GrowthBounds.MonomialFactorials.ClosedOfOrthogonalSplitting
covers: 2677
status: drafted
drafted_by: writer@claude
---
This theorem is the third link of the chain of reductions that proves the averaged bad-share bound `IntegralityFromMetricForLargeConstants D` (see [`theorem_A_closed_form_holds`](/entry/theorem-a-closed-form-holds/)). [`closed_of_splitting_matrix`](/entry/closed-of-splitting-matrix/) calls it. It turns the splitting statement `OrthSplit` into the statement `OrthBasisLat` that each lattice has an orthogonal basis, and passes the rest on to [`integralityFromMetric_of_orthBasisLat`](/entry/integrality-from-metric-of-orth-basis-lat/).

## Statement

Lattices $L$ and pairings $B$ are as in [`closed_of_minimal_vector`](/entry/closed-of-minimal-vector/): $L$ is a finitely generated $\mathbb{Z}_p$-submodule of a finite-dimensional $\mathbb{Q}_p$-subspace of $\mathbb{Q}_p[x_i : i \in \sigma]$, and $B$ is $\mathbb{Q}_p$-linear in the first variable and symmetric on $L$.

- `OrthSplit`: if $p \ne 2$ and $B \ne 0$ on $L \times L$, then $L = \mathbb{Z}_p x \oplus L'$ with $B(x, L') = 0$ and $\operatorname{rk} L' < \operatorname{rk} L$.
- `GoodLeSmall`: the bound on the good count by an orthogonal basis, stated in [`closed_of_splitting_matrix`](/entry/closed-of-splitting-matrix/).
- `OrthBasisLat`: if $p \ne 2$, then $L$ has a $\mathbb{Z}_p$-basis $f_1, \dots, f_m$ with $B(f_a, f_b) = 0$ for $a \ne b$.

**Theorem.** For each datum $D$, `OrthSplit`, `GoodLeSmall` and `RestWinE D` imply `IntegralityFromMetricForLargeConstants D`.

## Proof

The lemma `orthBasisLat_of` proves `OrthBasisLat` from `OrthSplit` and `FreeLat`. `FreeLat` says that each such $L$ is free, with a basis inside $L$. This is the structure theorem for finitely generated torsion-free modules over the principal ideal domain $\mathbb{Z}_p$ (Lang, *Algebra*, Chapter III, §7), and `freeLat_proved` proves it.

The proof of `orthBasisLat_of` is strong induction on $\operatorname{rk} L$.

1. If $B = 0$ on $L \times L$, any basis from `FreeLat` is orthogonal.
2. Otherwise `OrthSplit` gives $L = \mathbb{Z}_p x \oplus L'$ with $L'$ orthogonal to $x$ and of smaller rank. By induction $L'$ has an orthogonal basis $f_1, \dots, f_k$. Then $x, f_1, \dots, f_k$ is an orthogonal basis of $L$: it spans $L$, it is linearly independent because the sum is direct, and $B(x, f_b) = B(f_b, x) = 0$ by symmetry.

This is the usual existence of an orthogonal basis for a lattice with a symmetric form over $\mathbb{Z}_p$, $p$ odd (O'Meara, *Introduction to Quadratic Forms*, Chapter IX). Then `integralityFromMetric_of_orthBasisLat` is applied to `OrthBasisLat`, `GoodLeSmall` and `RestWinE D`.

## In the Lean code

The theorem is in [ClosedOfOrthogonalSplitting.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/ClosedOfOrthogonalSplitting.lean#L8). Its proof is one term:

```
integralityFromMetric_of_orthBasisLat D (orthBasisLat_of freeLat_proved hS) hG h
```

`FreeLat`, `OrthSplit`, `freeLat_proved` and `orthBasisLat_of` are in [OrthBasisLatOf.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/OrthBasisLatOf.lean#L10). `OrthBasisLat` is in [OrthCountOf.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/OrthCountOf.lean#L9).

The hypotheses `hG` and `h` pass through unchanged. The theorem is a reduction step, and its only content is `orthBasisLat_of`. The proof of `freeLat_proved` (line 29) is a chain of six tactic alternatives (`first | ... | ...`) that all try to apply `Bl.FreeLattices.goal1`. We have not opened `Bl.FreeLattices.goal1`.
