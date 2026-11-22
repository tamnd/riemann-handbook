---
id: b-odd-zk
title: The rank bound for the homology of GL_n, moved between two copies of the definitions
kind: theorem
decl: PositivityTheory.KB.bOdd_zk
module: Development.AutomorphicArithmetic.AutomorphicVarieties.LiteratureResults.KTheoryStability.ReductionBoundsTorsion.TorsionIntegers.Bridge
covers: 1787
status: drafted
drafted_by: writer@claude
---
This theorem only moves [the rank bound of `bStarOdd`](/entry/b-star-odd/) from one namespace to another. Under the name `UpperTheory.V.ZK.bOdd` it becomes [the input `BOdd`](/entry/b-odd/) of the bound on $H^2$. All the mathematics is in [`bStarOdd`](/entry/b-star-odd/).

## Statement

Let $L$ be a totally complex number field with $r_2$ complex places, $k$ an even number with $k + 1 < r_2$, $\ell \geq 1$ and $n \geq 2(k+1) + 4$. For $x \in H_{k+1}(\mathrm{GL}_n(\mathcal{O}_L), \mathbb{Z})$ (group homology with trivial coefficients) put $z_0 = x$ and
$$z_{t+1} = \psi_{\ell *}(z_t) - \ell^{t+2}\, \mathrm{st}_*(z_t) \in H_{k+1}(\mathrm{GL}_{\ell^{t+1} n}(\mathcal{O}_L), \mathbb{Z}).$$
Here $\psi_\ell(A) = 1_\ell \otimes A$ is the block diagonal map $\mathrm{GL}_m \to \mathrm{GL}_{\ell m}$, and $\mathrm{st}$ is the inclusion $\mathrm{GL}_m \to \mathrm{GL}_{\ell m}$ in the upper left corner.

**Theorem.** The subgroup of $H_{k+1}(\mathrm{GL}_{\ell^k n}(\mathcal{O}_L), \mathbb{Z})$ spanned by all $z_k$ has rank at most $r_2$.

## Proof

The definitions `zSeq`, `lev` and `psi` exist twice, in `UpperTheory.V.ZK` and in `PositivityTheory.KB`, with the same bodies. The lemma `lev_zk` shows that the two level functions agree, by induction. The lemma `zSeq_zk` shows that the two sequences agree, as a heterogeneous equality because the groups depend on the level. The lemma `rank_heq` then gives equal ranks, and `bStarOdd` gives the bound.

## In the Lean code

The theorem is at [line 34 of Bridge.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/KTheoryStability/ReductionBoundsTorsion/TorsionIntegers/Bridge.lean#L34). The statement `BOdd` is in [LemmaKOfSteps.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ClassCounting/LemmaKOfSteps.lean#L11), and `zSeq` is in [HasVal.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ClassCounting/HasVal.lean#L56). The proof is a pure transport. The declaration exists only because the definitions were duplicated. The next step up, `UpperTheory.V.ZK.bOdd`, is a second renaming of this one.
