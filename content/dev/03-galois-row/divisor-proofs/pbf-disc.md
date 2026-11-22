---
id: pbf-disc
title: The projective bundle formula on discrete spaces
kind: theorem
decl: GlobalTheory.EtC.pbf_disc
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ProjectiveBundleFormulaDiscreteSpace
covers: 1194
status: drafted
drafted_by: writer@claude
---
This theorem proves the projective bundle formula for étale cohomology with coefficients $\mathbb{Z}/q(i)$ over a discrete space. The statement `GlobalTheory.T.projectiveBundleFormula_discrete_space` ([its entry](/entry/projective-bundle-formula-discrete-space/)) repeats it. [The formula on an arbitrary space](/entry/projective-bundle-formula-vector-bundle-any-space/) uses it, and goes into the [local steps](/entry/steps-holds/) of the Galois row.

## Statement

A *space* is a simplicial presheaf of sets on schemes. A presheaf $F$ gives the constant simplicial object $\operatorname{disc} F$; a scheme gives the discrete space of its functor of points. The space $B\mathrm{GL}_N$ sends $U$ to the nerve of $\mathrm{GL}_N(\Gamma(U, \mathcal{O}))$ as a one-object category, and a map $V \colon E \to B\mathrm{GL}_N$ plays the role of a vector bundle of rank $N$. The space $P_N$ sends $U$ to the nerve of the category of vectors $v \in \Gamma(U, \mathcal{O})^N$ whose entries generate the unit ideal, with morphisms $(g, \lambda) \in \mathrm{GL}_N \times \mathbb{G}_m$ such that $g v = \lambda w$. Then $\mathbb{P}(V) = E \times_{B\mathrm{GL}_N} P_N$, with projection $\pi$ and the line bundle $L$ given by $\lambda$.

$H^n(E, \mathbb{Z}/q(i))$ is the group of homotopy classes of degree $n$ from the complex of free étale $\mathbb{Z}/q$-sheaves on the simplices of $E$ to an injective resolution of $\mathbb{Z}/q(i)$. There is a cup product and a Chern class $c_1(L) \in H^2(\mathbb{P}(V), \mathbb{Z}/q(1))$, fixed by Kummer conditions on cocycles.

**Theorem.** Let $q \geq 1$, $N \geq 0$, and let $F$ be a presheaf such that $q$ is a unit on each scheme $U$ with $F(U) \neq \emptyset$. Let $V \colon \operatorname{disc} F \to B\mathrm{GL}_N$. Then for all $n, i \in \mathbb{Z}$ the map

$$\bigoplus_{j=0}^{N-1} H^{n-2j}(\operatorname{disc} F, \mathbb{Z}/q(i-j)) \to H^n(\mathbb{P}(V), \mathbb{Z}/q(i)), \qquad (a_j) \mapsto \sum_{j} \pi^* a_j \cup c_1(L)^j$$

is bijective.

This is the projective bundle formula (SGA 5, Exposé VII), for a trivial bundle (step 1).

## Proof

1. `discrete_glBundle_eq_trivialGLBundle`: each map $\operatorname{disc} F \to B\mathrm{GL}_N$ is constant at the identity, since every simplex of $\operatorname{disc} F$ is degenerate. So $V$ is trivial.
2. `exists_injective_cochainModel_trivialProjectiveBundle` gives, for fixed $q, N, i$, a complex $J$ of injective sheaves and cocycles $\psi_j$ of degree $2j$ from the resolution of $\mathbb{Z}/q(i-j)$ to $J$. For each $F$ and $n$ there is an isomorphism that carries $\sum_j \psi_j \circ a_j$ to $\sum_j \pi^* a_j \cup c_1(L)^j$. As $J$ and $\psi_j$ do not depend on $F$, the theorem for $F$ becomes the bijectivity of one map $\Psi_F \colon (a_j) \mapsto \sum_j \psi_j \circ a_j$.
3. For a scheme $U$ on which $q$ is a unit, `etaleCohomology_projectiveBundle_formula` and step 2 make $\Psi_U$ bijective.
4. `injectiveComplexMap_quasiIso_of_unit_schemes` passes from all such $U$ to $F$. Its proof makes one map $f$ of complexes of injectives from the $\psi_j$, turns bijectivity into the vanishing of classes into the mapping cone of $f$, gets from step 3 that the cone is exact étale-locally on each $U$ with $F(U) \neq \emptyset$, and concludes.

The rest is bookkeeping.

## In the Lean code

The theorem is in [ProjectiveBundleFormulaDiscreteSpace.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ProjectiveBundleFormulaDiscreteSpace.lean#L18). `pbfMap` and `PBF` are in [ProjectiveBundleFormulaOfUnitOnEtalePoints.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ProjectiveBundleFormulaOfUnitOnEtalePoints.lean#L9). The lemmas, each an alias:

- `GlobalTheory.T.discrete_glBundle_eq_trivialGLBundle`, of `disc_eq_trivV`;
- `GlobalTheory.T.exists_injective_cochainModel_trivialProjectiveBundle`, of `pbf_disc_model`;
- `GlobalTheory.T.injectiveComplexMap_quasiIso_of_unit_schemes`, of `DiscSupp.bijective_disc`;
- `GlobalTheory.T.etaleCohomology_projectiveBundle_formula`, of `UpperTheory.Cb.etaleCohomology_projectiveBundle_formula`.

A scheme is a discrete space, so the scheme input also starts with `UpperTheory.Pbf.eq_triv` and then calls `UpperTheory.Pbf.pbf_all`, which we have not opened. So the theorem covers only $\operatorname{disc} F \times P_N$, where $P_N$ is a model of $\mathbb{P}^{N-1}$ as the groupoid of unimodular vectors up to a unit. Nontrivial bundles occur only on spaces that are not discrete; the entry above reaches them through `GlobalTheory.T.projectiveBundleFormula_of_discrete_spaces`, which we have not opened.
