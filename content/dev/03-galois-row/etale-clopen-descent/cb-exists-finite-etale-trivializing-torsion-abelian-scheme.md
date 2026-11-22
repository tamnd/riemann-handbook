---
id: cb-exists-finite-etale-trivializing-torsion-abelian-scheme
title: Kernels killed by k form a finite étale scheme
kind: theorem
decl: UpperTheory.Cb.exists_finite_etale_trivializing_torsion_abelianScheme
module: Development.AutomorphicArithmetic.Foundations.EtaleClopenDescent.ExistsFiniteEtaleTrivializingTorsionAbelianSchem
covers: 388
status: drafted
drafted_by: writer@claude
---
This theorem classifies the subgroups of $A[k]$ that occur as kernels of homomorphisms out of $A$, for an abelian scheme $A/S$ and $k$ invertible on $S$, by a finite étale $S$-scheme. [Its second name](/entry/t-exists-finite-etale-trivializing-torsion-abelian-scheme/) states it in full, and [isogeny_rep](/entry/isogeny-rep/) uses it. The proof only puts a group structure on $A[k]$ and calls [`SubRep.core`](/entry/sub-rep-core/), which does the work for any finite étale subgroup $G \subset A$ that contains the $k$-torsion.

## Statement

The statement is that of [the second name](/entry/t-exists-finite-etale-trivializing-torsion-abelian-scheme/). In short: for $S$ locally noetherian, $A/S$ an abelian scheme and $k > 0$ invertible on $S$, there are a finite étale $Y \to S$ and a finite étale subgroup $H \subset A_Y$ killed by $k$, such that each kernel killed by $k$ of a homomorphism from $A_T$ to an abelian scheme is $y^* H$ for a unique $S$-map $y \colon T \to Y$.

## Proof

1. `finiteEtale_mulN_torsion`: since $A$ is an abelian scheme and $k$ is a unit on $S$, the torsion $A[k] = A \times_{[k], A} S$ is finite étale over $S$.
2. The inclusion $\iota \colon A[k] \to A$ is a monomorphism, and products, the unit and inverses of $k$-torsion points are $k$-torsion. Each fact uses the universal property of $A[k]$ (`existsUnique_torsion`). So `exists_grpObj_isMonHom_of_mono_factor` gives $A[k]$ a group structure for which $\iota$ is a homomorphism.
3. [`SubRep.core`](/entry/sub-rep-core/), applied to $G = A[k]$, gives the result. Its two hypotheses are that each point of $A$ killed by $k$ lifts to $G$, and that each point of $G$ is killed by $k$. Both come from the universal property of $A[k]$.

`SubRep.core` builds $Y$ in three steps: a finite étale scheme that classifies the open and closed subsets of $T \times_S G$ (`exists_finite_etale_representing_clopen_subschemes`); the open and closed part of it where the subset is a subgroup (`clopenCond_of_isClosed_subgroupLocus` and `LevCover.exists_sub`); and the fact that the kernel of $f$, intersected with $G$, is such a subset (`exists_closed_locus_of_torsion_abelianScheme`).

## In the Lean code

The theorem is in [ExistsFiniteEtaleTrivializingTorsionAbelianSchem.lean](lean:Development/AutomorphicArithmetic/Foundations/EtaleClopenDescent/ExistsFiniteEtaleTrivializingTorsionAbelianSchem.lean#L203), and `UpperTheory.SubRep.core` is a private theorem at line 36 of the same file. `torsion` and `torsion.ι` are in [SplitTorusAff.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/SemiabelianSchemes/SplitTori/SplitTorusAff.lean#L53), with $A[k]$ defined as the pullback of $[k]$ (`mulN`) along the unit section.

Points to note:

- The hypothesis $0 < k$ is introduced as `hk0` and never used. It is redundant, since $k = 0$ is a unit only on the empty scheme.
- The name says "trivializing torsion", but $Y$ is a scheme of subgroups of $A[k]$, not a cover over which $A[k]$ becomes constant.
- We have not opened the proof of `finiteEtale_mulN_torsion`.
