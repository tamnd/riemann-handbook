---
id: cb-etale-cohomology-projective-bundle-formula
title: The projective bundle formula on a scheme
kind: theorem
decl: UpperTheory.Cb.etaleCohomology_projectiveBundle_formula
module: Development.AutomorphicArithmetic.Foundations.EtaleClopenDescent.EtaleCohomologyProjectiveBundleFormula
covers: 980
status: drafted
drafted_by: writer@claude
---
This theorem proves the projective bundle formula in étale cohomology with coefficients $\mathbb{Z}/q(i)$ for a vector bundle on a scheme. Its second name is [etaleCohomology_projectiveBundle_formula](/entry/t-etale-cohomology-projective-bundle-formula/), which [pbf_disc](/entry/pbf-disc/) uses in its step 3. The proof reduces to the trivial bundle, and [pbf_all](/entry/pbf-all/) proves the formula for the trivial bundle. That lemma has the real content.

## Statement

Spaces, $B\mathrm{GL}_N$, $\mathbb{P}(V)$, $L$ and the groups $H^n(E, \mathbb{Z}/q(i))$ are as in [pbf_disc](/entry/pbf-disc/). A scheme $U$ gives the discrete space $\operatorname{sch} U$.

**Theorem.** Let $q \geq 1$, $U$ a scheme, $N \geq 0$ and $V \colon \operatorname{sch} U \to B\mathrm{GL}_N$. Assume `Inv q (sch U)`: $q$ is a unit on each scheme $T$ over which $\operatorname{sch} U$ has a $0$-simplex. Then for all $n, i \in \mathbb{Z}$ the map

$$\bigoplus_{j=0}^{N-1} H^{n-2j}(U, \mathbb{Z}/q(i-j)) \to H^n(\mathbb{P}(V), \mathbb{Z}/q(i)), \qquad (a_j) \mapsto \sum_j \pi^* a_j \cup c_1(L)^j$$

is bijective.

## Proof

1. `eq_triv`: $V$ is the trivial bundle `triv`. Each $k$-simplex of $\operatorname{sch} U$ is the image of a $0$-simplex under the map $[k] \to [0]$. A functor from the one-point category to $B\mathrm{GL}_N$, composed with $[k] \to [0]$, is constant at the base object. So naturality of $V$ along $[k] \to [0]$ forces $V$ to be constant.
2. [pbf_all](/entry/pbf-all/) at $E = \operatorname{sch} U$ gives the formula for the trivial bundle of rank $N$.

## In the Lean code

The theorem is in [EtaleCohomologyProjectiveBundleFormula.lean](lean:Development/AutomorphicArithmetic/Foundations/EtaleClopenDescent/EtaleCohomologyProjectiveBundleFormula.lean#L41). The private lemmas `eq_triv` (line 23) and `pbf_all` (line 30) are in the same file, and `triv` is in [ConstCompSingle.lean](lean:Development/AutomorphicArithmetic/CupPullbacks/ConstCompSingle.lean#L13).

The theorem has the form of the projective bundle formula for any bundle, but on a discrete space every bundle is trivial. So it only says that $H^\ast(U \times \mathbb{P}^{N-1})$ is free over $H^\ast(U)$ on the powers of $c_1(L)$, for the model of $\mathbb{P}^{N-1}$ in [pbf_disc](/entry/pbf-disc/). We have not unfolded `sch`, or the simplices `Sx` in the definition of `Inv` ([GalMapMul.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/GalMapMul.lean#L250)).
