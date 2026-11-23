---
id: tie-del-all-steps
title: The kernel difference at every level below the top
kind: theorem
decl: GlobalTheory.TwV.DelA.tieDel_all_steps
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.KernelSiteFrameValuesAllStepsLtM
covers: 586
status: drafted
drafted_by: writer@claude
---
This theorem proves the kernel difference tie `Del j` at a joint site, for every level $j$ below the top level $m$. The tie says that a reading of the recursive kernel entry at level $j + 1$ equals a constant of norm $1$ times the kernel difference of the pending element. It is restated as [`kernelSite_frameValues_all_steps_lt_m`](/entry/kernel-site-frame-values-all-steps-lt-m/), and [the pending system is admitted at each joint site](/entry/admissible-at-each-site/) uses it, through that restatement, for the fourth tie at each level.

## Statement

Let $S$ be a joint site for a joint $J$ and a standard choice `std`, with residue characteristic $p$, the embedding $\lambda \colon \overline{\mathbb{Q}} \to \mathbb{C}_p$ and the pending element $Y = S.Y$ of the system `sysS H X std`, as in [the pending system is admitted at each joint site](/entry/admissible-at-each-site/). Assume:

- `J.Dict std`: each chosen adelic point is a global unitary element times the class point times an element of the level group, with the matching lattice and determinant;
- `S.Pair`: at each level $j < m$ the pair of kernel lattices is admitted and local, the kernel theta function is differentiable with algebraic coefficients, a scalar and a nonzero character factor are algebraic, and the frames are invertible and carry the kernel lattices to the local lattices;
- `S.Pos`: $\lambda$, on the embedded elements, matches the twisted embeddings at each place;
- `S.Law`: the transformation law `KapLawLt` of the theta series under the level groups.

**Theorem.** For each $j < m$ and each ring homomorphism $\iota \colon \mathbb{C} \to \mathbb{C}_p$ that agrees with $\lambda$ on $\overline{\mathbb{Q}}$, there is $c_K \in \mathbb{C}_p$ with $\lVert c_K \rVert = 1$ such that

$$\mathrm{Rd}_j(c', L')\bigl(\mathrm{entRec}_j(\mathrm{cls}(L_a), x)\bigr) = c_K \cdot \mathrm{DelF}_j\bigl(\mathrm{cmp}_j(x, L_a),\ \mathrm{Sr}_j(L_a, (c', L'))\bigr)$$

for each representative $L_a$ at level $j$, each lattice vector $x$ at level $j$ and each lattice tuple $(c', L')$ at level $j + 1$. Here $\mathrm{Rd}$ is the reading map `rdJ` through $\iota$, `entRec` the recursive kernel entry, `DelF` the kernel difference of $Y$, `cmp` the comparison map and `Sr` the series of $Y$. We have not unfolded these five maps.

## Proof

Fix $j < m$ and $\iota$. If level $j$ or level $j + 1$ has no component, the condition is empty and $c_K = 1$. Otherwise:

1. `stepDeterminantConstant_unit_independent` (from `Pos`) shows that the constant `cKs` has norm $1$ and does not depend on the components. It is $\iota$ of a ratio of determinant powers, times a power of the constant `ltC` of the datum $g$ of the site. Take it as $c_K$.
2. `exists_adelic_latticeTuple_decomposition` (from `Dict`) gives a decomposition $d_0$.
3. Fix $L_a$, $x$, $(c', L')$. A sharp form $Q$ comes from the joint. `operatorOnFrame_and_classSummand_polynomial` writes the entry $\varphi = \mathrm{entRec}_j(\ldots)$ as a character factor times the frame polynomial of a polynomial $P$, and `wt_polDY_framePol` gives the weight of $P$.
4. For each decomposition $d$, `transportedFramePolynomial_complex_values_at_point` gives a complex polynomial $V$ that realizes $\varphi$ at $(c', L')$. Then `kernelSite_contractionIdentity_operatorHalf` (from `Dict`, `Pair`, `Pos`, `Law`), with three smaller lemmas, shows $\iota(V) = c_K \cdot \mathrm{DelF}_j(\ldots)$.
5. $\iota$ is injective, so $V$ does not depend on $d$. So $V$ realizes $\varphi$ for every decomposition.
6. `latticeTupleReading_eq_of_realising_polynomial` (from `Dict`) gives $\mathrm{Rd}_j(c', L')(\varphi) = \iota(V)$.

## In the Lean code

The theorem is in [KernelSiteFrameValuesAllStepsLtM.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/KernelSiteFrameValuesAllStepsLtM.lean#L23). `Del`, `Dict`, `Pair`, `Pos` and `Law` are in [JointCmpEmbeddingY.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/JointCmpEmbeddingY.lean#L123), `KernelDifferenceAtLevel` in [SecondKernelEntrywiseLastLevel.lean](lean:Formalism/LocalToGlobal/InertKernelTheory/SecondKernelEntrywiseLastLevel.lean#L46), and `cKs` in [RealAt.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/RealAt.lean#L65).

The constant $c_K$ is chosen before $L_a$, $x$ and $(c', L')$, so one constant serves the whole level. `Pair` and `Law` are used only in step 4.
