---
id: local-order
title: The multiplicity of a hyperplane section is the sum of the branch orders
kind: theorem
decl: GlobalTheory.CompanionTheory.Heights.BranchOrder.localOrder
module: Development.AutomorphicSpectrum.Proofs.BlockDecomposition.SliceReducedAwayZariski
covers: 548
status: drafted
drafted_by: writer@claude
---
This theorem computes the algebraic multiplicity of a component of a hyperplane section of an affine variety from the local branches of the variety. It is one of the inputs of the Poincaré-Lelong theorems `poincareLelong` and `poincareLelongInv`. The second reaches the [literature step](/step/every-character-of-literature/) as `poincare_lelong_inv_of_literature`. The proof reduces to curves by a generic linear slice.

## Statement

Let $J \subset \mathbb{C}[x_1, \dots, x_n]$ be a prime ideal with $\dim \mathbb{C}[x]/J = d+1$, and let $\ell_u = \sum_j u_j x_j$ be a linear form with $\ell_u \notin J$. Branches $\gamma \colon B(0, r) \to Z(J)$ are as in [the entry on branches](/entry/branch-proper-at-point/). The *slice* of a branch is the image of $B(0,r) \cap \{t_0 = 0\}$. For a prime $W$, the *local multiplicity* $\operatorname{mult}_W(I)$ is the length of $\mathbb{C}[x]_W / I\,\mathbb{C}[x]_W$ (`localMult`).

**Theorem.** Let $W$ be a minimal prime of $J + (\ell_u)$ and let $p \in Z(W)$. Let $\gamma_1, \dots, \gamma_m$ be branches of $J$ at $p$ of dimension $d+1$, and let $o_1, \dots, o_m \geq 0$. Suppose that

1. near $p$, $Z(J)$ lies in the union of the images of the $\gamma_b$;
2. near $p$, $Z(W)$ lies in the slice of each $\gamma_b$;
3. for $b \neq b'$, the images of $\gamma_b$ and $\gamma_{b'}$ meet only where $\ell_u = 0$;
4. $\ell_u \circ \gamma_b = t_0^{o_b} H_b$ on the ball, with $H_b$ holomorphic and nowhere zero.

Then
$$\operatorname{mult}_W\bigl(J + (\ell_u)\bigr) = \sum_{b=1}^m o_b.$$

## Proof

For a $d \times n$ matrix $L$ and a point $q$, put $J_{L,q} = J + (Lx - Lq)$, the slice of $J$ by the affine subspace through $q$ with direction $\ker L$.

1. **Generic slices** (`SliceLength`). There is an open $U$ with $Z(W) \subseteq \overline{Z(W) \cap U}$. For each $q \in Z(W) \cap U$, the matrices $L$ that satisfy the two conditions below are dense. First, $J_{L,q}$ is radical at $q$. Second, $\operatorname{mult}_W(J + (\ell_u))$ equals the multiplicity of $J_{L,q} + (\ell_u)$ at the maximal ideal of $q$.
2. **Slices of branches** (`SliceBranches`). Given hypotheses 1 to 4, some such $q$ and $L$ have curve branches $c_1, \dots, c_m$ of $J_{L,q}$ at $q$. They satisfy 1, 3 and 4 with the same orders $o_b$.
3. **Curves** (`CurveBranchLength`). For an ideal that is radical at $q$, with curve branches at $q$ that satisfy 1, 3 and 4, the multiplicity of $I + (\ell_u)$ at $q$ is $\sum_b o_b$.

By step 1, the left side equals the multiplicity of the slice at $q$. Steps 2 and 3 show that the slice multiplicity is $\sum_b o_b$.

## In the Lean code

The theorem is at [SliceReducedAwayZariski.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/SliceReducedAwayZariski.lean#L43). It is `LocalOrder.proof` in [PLocalOrder.lean](lean:GroundTheory/HeightsAndTheta/Heights/ComplexAnalyticSets/PLocalOrder.lean#L11), applied to `sliceLength`, `slice_branches_holds` and `curve_branch_length_holds`. `sliceLength` comes from the five other theorems of the same file. The last two are second names for `Ar.SliceBranch.sliceBranches` and `CurveBranch.curveBranchLength`, which we have not unfolded. The statement is in [StatementsCurrent.lean](lean:GroundTheory/HeightsAndTheta/Heights/ComplexAnalyticSets/StatementsCurrent.lean#L131). `localMult` is in [Statements.lean](lean:GroundTheory/HeightsAndTheta/Heights/ArithmeticBezout/Statements.lean#L50). It is 0 when $W$ is not prime, and the length is cast to $\mathbb{N}$ by `toNat`, so an infinite length gives 0.

A second definition named `LocalOrder.Statement`, in the namespace `IndefiniteRowSideFullHecke.ComplexSets`, is in [EqZeroOfMemZeroLocusLineOriginIdeal.lean](lean:GroundTheory/HeightsAndTheta/Heights/ComplexAnalyticSets/EqZeroOfMemZeroLocusLineOriginIdeal.lean#L144). This theorem does not use it.
