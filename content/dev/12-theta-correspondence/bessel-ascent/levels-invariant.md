---
id: levels-invariant
title: The pairing of points is invariant under the level groups at every vertex
kind: theorem
decl: GlobalTheory.ExpansionInvariance.levels_invariant
module: Development.AbelianVarietyTheory.Proofs.TwistedOperators.NormalisedKernelExpansionSumLevelInvariant
covers: 617
status: drafted
drafted_by: writer@claude
---
This theorem puts four invariance lemmas into one conjunction: the pairing of points of an expansion does not change when one point of the grid moves by an element of its level group. The renaming [`normalisedKernelExpansionSum_levelInvariant`](/entry/normalised-kernel-expansion-sum-level-invariant/) gives it a second name, and [`twisted_pairing_identity`](/entry/twisted-pairing-identity/) gives the four parts to `JetsOne.glue`. The content is in the four lemmas.

## Statement

Fix a grid datum with $m \ge 2$, a grid choice $S$, an index $t \in U$, a datum $\Phi$, a family of cosets $\beta$ in the support `S.supp t Φ`, and a finite expansion $\tau$ of the product of the local unfolded terms at $\beta$ (`S.IsExpansion t Φ β τ`). Assume that each datum $d$ in the support of $\tau$ has vectors (`S.Z.HasVec`), and three arithmetic conditions: `L.Is μ₀`, a coprimality condition on `pde` and `pde'`, and a condition on the norm of `ccK`.

Let $x = (x_j)_{j \le m}$ be points of the top vertices and $y = (y_i)_{i \le m}$ points of the row vertices. Let $P_\tau(x, y)$ be the bilinear form `pairPts S τ x y`: the sum over $d$ of $\tau(d)$ times the bracket of the column chain of theta kernels of $d$ at $x$ and the row chain at $y$. Let $\Psi$ and $F$ be vector-valued functions on the points of the vertices $0$. Then:

1. For $0 < j < m$ and $k$ in the top level group $K^{\mathrm{top}}_j$ (`S.levTop`), $P_\tau(x_j \mapsto x_j k, y)(\Psi(x_0), F(y_0)) = P_\tau(x, y)(\Psi(x_0), F(y_0))$.
2. If $\Psi(xk) = \Psi(x)$ for all $k \in K^{+}$, the same holds for a move of $x_0$ by $k \in K^{\mathrm{top}}_0$, with $\Psi(x_0 k)$ in place of $\Psi(x_0)$. By definition $K^{\mathrm{top}}_0 = K^{+}$.
3. For $0 < i < m$ and $k$ in the row level group $K^{\mathrm{row}}_i$ (`S.levRow`), the same holds for a move of $y_i$.
4. If $x_m = \iota(y_m)$, where $\iota$ is the embedding `finEmb G.sp.topDec`, then the same holds when $y_m$ moves to $y_m k$ with $k \in K^{\mathrm{row}}_m$ and $x_m$ moves to $\iota(y_m k)$ together.

## Proof

Each part is one lemma:

1. [`expansionPairing_invariant_inner_vertex_level`](/entry/expansion-pairing-invariant-inner-vertex-level/), the inner top vertices.
2. `expansionPairing_invariant_parabolic_basePoint`, the base point.
3. `expansionPairing_invariant_innerVertex_level`, the inner row vertices.
4. `expansion_pairing_invariant_last_vertex_level`, the last vertex.

## In the Lean code

The theorem is in [NormalisedKernelExpansionSumLevelInvariant.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/NormalisedKernelExpansionSumLevelInvariant.lean#L19). The proof is an anonymous constructor of the four lemmas, with the same arguments. The names of parts 1 and 3 differ only in `inner_vertex` against `innerVertex`, but part 1 is about the column (top) vertices and part 3 about the row vertices.
