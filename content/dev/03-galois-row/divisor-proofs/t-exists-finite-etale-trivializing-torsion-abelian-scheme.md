---
id: t-exists-finite-etale-trivializing-torsion-abelian-scheme
title: Kernels killed by k form a finite étale scheme, a renaming
kind: theorem
decl: GlobalTheory.T.exists_finite_etale_trivializing_torsion_abelianScheme
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsFiniteEtaleTrivializingTorsionAbelianSchem
covers: 389
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the theorem in `UpperTheory.Cb`](/entry/cb-exists-finite-etale-trivializing-torsion-abelian-scheme/), and [the lemma `SubRep.core`](/entry/sub-rep-core/) below it has the real content. It classifies kernels killed by $k$ of maps out of an abelian scheme $A/S$, for $k$ invertible on $S$. Step 1 of [isogeny_rep](/entry/isogeny-rep/) uses it. Below this theorem are 389 declarations.

## Statement

Group pullbacks are as in [isogeny_rep](/entry/isogeny-rep/).

**Theorem.** Let $S$ be locally noetherian, $A/S$ an abelian scheme, and $k > 0$ invertible on $S$. There is a finite étale $Y \to S$ and, in each group pullback $A_0$ of $A$ to $Y$, a finite étale subgroup $H$ killed by $k$, such that: for each $S$-scheme $T$, group pullback $A_1$ of $A$ to $T$, and homomorphism $f \colon A_1 \to B_1$ to an abelian scheme with kernel killed by $k$, there is a unique $S$-map $y \colon T \to Y$ with $\ker f = y^* H$.

## Proof

The proof is `exact @UpperTheory.Cb.exists_finite_etale_trivializing_torsion_abelianScheme`, a term with the same statement, inside a `first` with one fallback.

## In the Lean code

The theorem is in [ExistsFiniteEtaleTrivializingTorsionAbelianSchem.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsFiniteEtaleTrivializingTorsionAbelianSchem.lean#L8). The name is misleading: $Y$ does not trivialize $A[k]$. In the proof of [`SubRep.core`](/entry/sub-rep-core/) it is the scheme of open and closed subgroups of $A[k]$, with $H$ the universal subgroup. The equality $\ker f = y^* H$ is stated on points: $f \circ g = 0$ if and only if the image of $g$ in $A$ lifts to $H$ over $y$.
