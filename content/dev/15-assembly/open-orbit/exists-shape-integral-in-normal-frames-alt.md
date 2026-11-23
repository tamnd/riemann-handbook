---
id: exists-shape-integral-in-normal-frames-alt
title: A lattice shape in which the normal frames are integral
kind: theorem
decl: GlobalTheory.Fam.LatShape.exists_shape_integral_in_normal_frames_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ExistsShapeIntegralInNormalFrames
covers: 374
status: drafted
drafted_by: writer@claude
---
This theorem builds global Hermitian lattices for the see-saw data of a real pack, such that the lattice shape condition `ShapeOff` holds and given local frames are integral bases. Its only user is the renaming [`local_component_measure_identity_alt_bis`](/entry/local-component-measure-identity-alt-bis/), in branch 1 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/).

## Statement

Let $W$ be a real pack over a datum $D$ with the package hypotheses, $u$ a word, and $(a, y, m, b_0)$ geometric data, which give a common datum $c$. Let $k$ be a nonarchimedean local field, $v$ level data for $c$ (with finite sets $g_P$ and $t_P$ of places of $F$) and $o$ a shape datum over $k$. Let $P$ be the set of places $\mathfrak P$ of $E$ that are level places of $W$ or lie in a tuple set $Q_t$. For each $\mathfrak P \in P$ let $l_{\mathfrak P}$ be local data: a local field, a split point $q_{\mathfrak P}$ over the place below $\mathfrak P$, and frames. Let $F^Y_{\mathfrak P}$ be *normal* frames of the spaces $Y_j$ (`IsNormalFr`): unit scalars $s_j$ with $s_{j+2} = s_j \xi$, Bessel and Jacobi frame conditions, and one condition on $\tau$.

Assume thirteen compatibility conditions. Among them: $g_P$ is the set of places below the level places of $W$; $t_P$ is the set of primes that divide the integer $T$ of $u$; $g_P \cap t_P = \emptyset$; `PreT v o`; the lattice $L_T$ is self-dual.

**Theorem.** There are lattices $N_j \subset Y_j$, coefficients $d_{T,j}$, lattices $M$ in the Bessel spaces and frames $\beta_0$ with:

1. `ShapeOff` for $v$ with $(N, d_T)$ and $o$ with $(M, \beta_0)$;
2. `CombAt` for each $d_{T,j}$ at the places of $t_P$;
3. $N_j$ self-dual for $j < m$;
4. each $F^Y_{\mathfrak P}$ an integral basis of $N_j$ at the place of $q_{\mathfrak P}$ (`IntIn`).

A lattice $\Lambda$ is self-dual (`IsSelfDualC`) if $y \in \Lambda$ exactly when $h(x, y) \in \mathcal O_E$ for all $x \in \Lambda$.

## Proof

1. `finite_level_places`: $P$ is finite. `level_place_eq_of_under_eq`: distinct places of $P$ lie over distinct places of $F$. Normality gives $s_j \neq 0$ and $\xi \neq 0$.
2. For $j < m$, `exists_selfDual_lattice` gives a self-dual lattice in $Y_j$. `exists_move_selfDual_lattice_split_frames` changes it at the finitely many places to a self-dual $N^1_j$ in which each frame $F^Y_{\mathfrak P}$ is integral. For $j \ge m$ there are no frames.
3. The same method gives self-dual lattices $M^1$ in the Bessel spaces, from `local_component_measure_relation_alt` and the core frames of `normalFrames_and_basePoint_exist`. `coreFrame_beta_eq` says that all core frames have the same matrix.
4. Four lemmas give the local conditions at the places below $P$: they are not in $t_P$, and `GoodBF`, `AdaptFB` and `SplitAt` hold for $(N^1, M^1)$.
5. `seeSawLatticeShapeExists_proof` proves `ShapeEx D` with no hypotheses. With the places below $P$ as level places, it gives $(N, d_T, M, \beta_0)$ with `ShapeOff` and `CombAt`, and self-dual $N_j$ with the same completions as $N^1_j$ at these places. So the frames stay integral. The rest is bookkeeping.

## In the Lean code

The theorem is at [ExistsShapeIntegralInNormalFrames.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsShapeIntegralInNormalFrames.lean#L24). `exists_move_selfDual_lattice_split_frames` is a renaming of `SplitLat.exists_selfDual_frames`. We have not unfolded `GoodBF`, `AdaptFB`, `SplitAt` or `MxAt`.

Odd points:

- The five `local_component_measure_*_alt` lemmas say nothing about measures. They state a self-dual lattice, $\mathfrak P \notin t_P$, `GoodBF`, `AdaptFB` and `SplitAt`.
- The hypotheses on `bas`, $\tau$ and $\zeta_0$ are not used here. They only go to the sub-lemmas.
- `ShapeEx` is applied with a new $g_P$. This works because `ShapeOff` does not mention $g_P$.
