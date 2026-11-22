---
id: closed-of-splitting-matrix
title: Counting good vectors by a diagonal rank
kind: theorem
decl: Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_splitting_matrix
module: Formalism.SharpRestriction.GrowthBounds.MonomialFactorials.ClosedOfSplittingMatrix
covers: 2682
status: drafted
drafted_by: writer@claude
---
This theorem is the second link of the chain of reductions that proves the averaged bad-share bound `IntegralityFromMetricForLargeConstants D` (see [`theorem_A_closed_form_holds`](/entry/theorem-a-closed-form-holds/)). [`closed_of_minimal_vector`](/entry/closed-of-minimal-vector/) calls it. It replaces the matrix statement `GoodLeSmallMat` with the lattice statement `GoodLeSmall`, and passes the rest on to [`closed_of_orthogonal_splitting`](/entry/closed-of-orthogonal-splitting/).

## Statement

Lattices $L$ and pairings $B$ are as in [`closed_of_minimal_vector`](/entry/closed-of-minimal-vector/). For an exponent $e \in \mathbb{Z}$, let the *good count* $g(B, L, e)$ be the largest $n$ for which there are $x_1, \dots, x_n, y_1, \dots, y_n \in L$ with $B(x_i, y_j) = p^{e}\delta_{ij}$ (`goodCount`, defined as a supremum).

- `OrthSplit`: under the hypotheses of `OrthMin`, $L = \mathbb{Z}_p x \oplus L'$ with $L'$ orthogonal to $x$ and $\operatorname{rk} L' < \operatorname{rk} L$.
- `GoodLeSmallMat`: if $U, V$ are $n \times m$ matrices over $\mathbb{Z}_p$ and $U \operatorname{diag}(c) V^{T} = p^{e} I_n$, then $n \le \#\{a : c_a \ne 0,\ v_p(c_a) \le e\}$.
- `GoodLeSmall`: if $f_1, \dots, f_m$ is a $\mathbb{Z}_p$-basis of $L$ with $B(f_a, f_b) = 0$ for $a \ne b$, then $g(B, L, e) \le \#\{a : B(f_a,f_a) \ne 0,\ v_p(B(f_a,f_a)) \le e\}$.

**Theorem.** For each datum $D$, `OrthSplit`, `GoodLeSmallMat` and `RestWinE D` imply `IntegralityFromMetricForLargeConstants D`.

## Proof

The lemma `goodLeSmall_of` proves `GoodLeSmall` from `GoodLeSmallMat`. Let $f_1, \dots, f_m$ be an orthogonal basis of $L$, and let $n = g(B, L, e)$. The lemma `goodCount_mem` gives vectors $x_i, y_j$ with $B(x_i, y_j) = p^{e}\delta_{ij}$. Write $x_i = \sum_a U_{ia} f_a$ and $y_j = \sum_a V_{ja} f_a$ with $U_{ia}, V_{ja} \in \mathbb{Z}_p$. By linearity, symmetry and orthogonality of the basis,

$$ B(x_i, y_j) = \sum_a U_{ia}\, B(f_a, f_a)\, V_{ja}. $$

So $U \operatorname{diag}(c) V^{T} = p^{e} I_n$ with $c_a = B(f_a, f_a)$, and `GoodLeSmallMat` gives the bound.

Then `closed_of_orthogonal_splitting` is applied to `OrthSplit`, `GoodLeSmall` and `RestWinE D`.

## In the Lean code

The theorem is in [ClosedOfSplittingMatrix.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/ClosedOfSplittingMatrix.lean#L8). Its proof is one term:

```
closed_of_orthogonal_splitting D hS (goodLeSmall_of hM) h
```

`GoodLeSmallMat` and `goodLeSmall_of` are in [GoodLeSmallMat.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/GoodLeSmallMat.lean#L12). `GoodLeSmall` is in [OrthCountOf.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/OrthCountOf.lean#L32). `goodCount` is in [GoodCount.lean](lean:Formalism/MahlerMeasure/GoodCount.lean#L94), and `goodCount_mem` in [GoodCountMem.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/GoodCountMem.lean#L11).

The hypotheses `hS` and `h` pass through unchanged. The theorem is a reduction step, and its only content is `goodLeSmall_of`. `GoodLeSmall` has no hypothesis $p \ne 2$, and `goodLeSmall_of` does not need one.
