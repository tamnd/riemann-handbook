---
id: t-etale-cohomology-projective-bundle-formula
title: The projective bundle formula on a scheme, a renaming
kind: theorem
decl: GlobalTheory.T.etaleCohomology_projectiveBundle_formula
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.EtaleCohomologyProjectiveBundleFormula
covers: 981
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the formula in `UpperTheory.Cb`](/entry/cb-etale-cohomology-projective-bundle-formula/), and [pbf_all](/entry/pbf-all/) below it has the real content. It is the projective bundle formula for a vector bundle on a scheme. [pbf_disc](/entry/pbf-disc/) uses it for the schemes in its step 3. Below this theorem are 981 declarations.

## Statement

The spaces, $B\mathrm{GL}_N$, $\mathbb{P}(V)$, $L$ and the groups $H^n(E, \mathbb{Z}/q(i))$ are as in [pbf_disc](/entry/pbf-disc/). A scheme $U$ gives the discrete space $\operatorname{sch} U$ of its functor of points.

**Theorem.** Let $q \geq 1$, let $U$ be a scheme on which $q$ is a unit, and let $V \colon \operatorname{sch} U \to B\mathrm{GL}_N$. Then for all $n, i \in \mathbb{Z}$ the map $(a_j) \mapsto \sum_{j<N} \pi^* a_j \cup c_1(L)^j$ from $\bigoplus_{j<N} H^{n-2j}(U, \mathbb{Z}/q(i-j))$ to $H^n(\mathbb{P}(V), \mathbb{Z}/q(i))$ is bijective.

## Proof

The proof is the term `@UpperTheory.Cb.etaleCohomology_projectiveBundle_formula`, with the same statement. That proof has two lines. `eq_triv` shows that $V$ is the trivial bundle, because $\operatorname{sch} U$ is constant and $V$ is natural for the map of each simplex to $[0]$. Then `pbf_all` gives the formula for the trivial bundle.

## In the Lean code

The theorem is in [EtaleCohomologyProjectiveBundleFormula.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/EtaleCohomologyProjectiveBundleFormula.lean#L5). The target is in [the `Cb` file](lean:Development/AutomorphicArithmetic/Foundations/EtaleClopenDescent/EtaleCohomologyProjectiveBundleFormula.lean#L41), with `eq_triv` at line 23 and `pbf_all` at line 30.

`pbf_all` proves the formula for the trivial bundle of rank $N$ on every space $E$ with `Inv q E`, by induction on $N$. The statement here keeps only the case $E = \operatorname{sch} U$.
