---
id: pow-k-ne-zero
title: The top power of the de Rham first Chern class is not zero
kind: theorem
decl: CrystallineSemistableComparison.Pb.powK_ne_zero
module: Development.WeilBound.CoreStatements.PadicHodgeComparison.EtaleCohomologyComparison.PerfectoidPullbacks.ConeSectionRestriction.IsFirstChernDeRhamUnique
covers: 667
status: drafted
drafted_by: writer@claude
---
This theorem says that on a connected smooth variety of dimension $d$ with a tautological line, the $d$-th cup power of the de Rham first Chern class is not zero. It is a second name for [the main form](/entry/pow-k-ne-zero-main/), with the same statement, and its proof is one application of it. The real argument is in [the residue argument](/entry/pow-k-ne-zero-of/). It sits below [the geometric steps](/entry/steps-holds/): [`pmap`](/entry/pmap/) uses it to find a linear form $\varphi$ with $\varphi(c^d) = 1$, and `HT.kTop` also uses it. Below it are 667 declarations.

## Statement

Let $K$ be a field of characteristic $0$, and $X$ a connected scheme, smooth of relative dimension $d$ over $K$ by $q$. Let $D$ be line data on $X$ with `IsTautologicalLine q D`: there is a closed immersion $i \colon X \to \mathbb{P}^N_K$ over $K$, and $D$ has transition units $x_k/x_j$ on the charts $i^{-1}D_+(x_j)$. Let $c$ be a class in `HdR q 2`, the degree $2$ cohomology of the structure sheaf on the site of thickenings of $X$ over $K$. We have not unfolded the site. Assume that $c$ is a first Chern class of $D$ in the sense of `IsFirstChernDeRham q D c`: locally it is given by a Čech cocycle of truncated logarithms of the transition units. Then
$$c^d = \mathrm{powK}\ q\ c\ d \neq 0.$$

There is no properness hypothesis. The closed immersion into $\mathbb{P}^N_K$ makes $X$ projective.

## Proof

Apply `powK_ne_zero_main q d D hD c hc`.

## In the Lean code

The theorem is in [IsFirstChernDeRhamUnique.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/PerfectoidPullbacks/ConeSectionRestriction/IsFirstChernDeRhamUnique.lean#L45). The same file holds other facts on the tautological line, such as `isO1_exists` and `isFirstChernDeRham_exists`. The statements of `powK_ne_zero` and `powK_ne_zero_main` are the same text. The size 667 is almost all below `powK_ne_zero_main`.
