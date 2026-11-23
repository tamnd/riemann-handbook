---
id: closed-of-minimal-vector
title: Splitting off a vector of minimal norm
kind: theorem
decl: Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_minimal_vector
module: Formalism.SharpRestriction.GrowthBounds.MonomialFactorials.ClosedOfMinimalVector
covers: 2691
status: drafted
drafted_by: writer@claude
---
This theorem is the first link of a chain of reductions that proves the averaged bad-share bound `IntegralityFromMetricForLargeConstants D`. The theorem [`theorem_A_closed_form_holds`](/entry/theorem-a-closed-form-holds/) applies it to three proved inputs. The step here replaces the minimal vector statement `OrthMin` with the splitting statement `OrthSplit` and passes the rest on to [`closed_of_splitting_matrix`](/entry/closed-of-splitting-matrix/). The bound itself is proved further down the chain.

## Statement

All lattices here are finitely generated $\mathbb{Z}_p$-submodules $L$ of a finite-dimensional $\mathbb{Q}_p$-subspace of a polynomial ring $\mathbb{Q}_p[x_i : i \in \sigma]$. The pairing $B$ takes values in $\mathbb{Q}_p$. It is additive and $\mathbb{Q}_p$-linear in the first variable, and symmetric on $L$.

- `OrthMin`: if $p \ne 2$ and $B$ is not zero on $L \times L$, then there is $x \in L$ with $B(x,x) \ne 0$ and $B(u,x) \in \mathbb{Z}_p\, B(x,x)$ for all $u \in L$.
- `GoodLeSmallMat`: if $U, V$ are $n \times m$ matrices over $\mathbb{Z}_p$, $c \in \mathbb{Q}_p^m$ and $U \operatorname{diag}(c) V^{T} = p^{e} I_n$, then $n \le \#\{a : c_a \ne 0,\ v_p(c_a) \le e\}$.
- `RestWinE D`: the window count, stated in [`theorem_A_closed_form_holds`](/entry/theorem-a-closed-form-holds/).

**Theorem.** For each datum $D$, `OrthMin`, `GoodLeSmallMat` and `RestWinE D` imply `IntegralityFromMetricForLargeConstants D`.

## Proof

The lemma `orthSplit_of_min` turns `OrthMin` into `OrthSplit`: under the same hypotheses, $L = \mathbb{Z}_p x \oplus L'$ with $L'$ orthogonal to $x$ and of smaller rank. Its proof takes the $x$ of `OrthMin` and sets

$$ L' = \{u \in L : B(u,x) = 0\}. $$

Each $u \in L$ is $c\,x + (u - c\,x)$, where $c \in \mathbb{Z}_p$ is the quotient $B(u,x)/B(x,x)$. So $L = \mathbb{Z}_p x + L'$. If $c\,x + y = 0$ with $y \in L'$, pair with $x$: then $c\,B(x,x) = 0$, so $c = 0$. The lemma `splitRank_proved` gives $\operatorname{rk} L' < \operatorname{rk} L$ from this direct sum and $x \ne 0$. Orthogonality $B(x,u) = 0$ for $u \in L'$ is symmetry. This is the first step of the usual proof that a lattice with a symmetric form over $\mathbb{Z}_p$, $p$ odd, has an orthogonal basis (O'Meara, *Introduction to Quadratic Forms*, Chapter IX).

Then `closed_of_splitting_matrix` is applied to `OrthSplit`, `GoodLeSmallMat` and `RestWinE D`.

## In the Lean code

The theorem is in [ClosedOfMinimalVector.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/ClosedOfMinimalVector.lean#L8). Its proof is one term:

```
closed_of_splitting_matrix D (orthSplit_of_min hO) hM h
```

`OrthMin`, `orthSplit_of`, `splitRank_proved` and `orthSplit_of_min` are in [OrthSplitOfMin.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/OrthSplitOfMin.lean#L9). `OrthSplit` is in [OrthBasisLatOf.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/OrthBasisLatOf.lean#L17).

The hypotheses `hM` and `h` pass through unchanged. All three hypotheses are proved statements in the code, so the theorem is a reduction step and its only content is `orthSplit_of_min`. A second, unrelated definition named `OrthSplit` (about matrices) is in [ArchimedeanUnitaryGroupStabilisersUnimodular.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/ArchimedeanUnitaryGroupStabilisersUnimodular.lean#L21), in another namespace.
