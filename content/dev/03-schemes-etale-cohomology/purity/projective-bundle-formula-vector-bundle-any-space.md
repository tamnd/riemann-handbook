---
id: projective-bundle-formula-vector-bundle-any-space
title: The projective bundle formula for a vector bundle on any space
kind: theorem
decl: GlobalTheory.EtC.projectiveBundleFormula_vectorBundle_any_space
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ProjectiveBundleFormulaVectorBundleAnySpace
covers: 1595
status: drafted
drafted_by: writer@claude-opus-5-5
---
This theorem proves the projective bundle formula in étale cohomology with coefficients $\mathbb{Z}/q(i)$, for each vector bundle on each space on which $q$ is invertible. It is the statement $\mathrm{D1}$ that the [power-sum classes](/entry/s57/) need, and [etale_duality_trace_isomorphism](/entry/etale-duality-trace-isomorphism/) gives it to them. Three other results use it, and all four lead to [steps_holds](/entry/steps-holds/). Below this theorem are 1,595 declarations.

## Statement

The spaces $E$, the groups $H^n(E, \mathbb{Z}/q(i))$, the condition "$q$ is invertible on $E$", the vector bundles $V \colon E \to B\mathrm{GL}_N$, the projective bundle $\pi \colon \mathbb{P}(V) \to E$ and the class $\xi \in H^2(\mathbb{P}(V), \mathbb{Z}/q(1))$ are as in [the power-sum entry](/entry/s57/).

**Theorem.** Let $q \geq 1$, let $V$ be a vector bundle of rank $N$ on a space $E$, and let $q$ be invertible on $E$. Then for all integers $n, i$ the map
$$\bigoplus_{j=0}^{N-1} H^{n-2j}(E, \mathbb{Z}/q(i-j)) \to H^n(\mathbb{P}(V), \mathbb{Z}/q(i)), \qquad (a_j) \mapsto \sum_j \pi^* a_j \cup \xi^j$$
is bijective.

For a vector bundle on a scheme this is the classical projective bundle formula (SGA 5, Exposé VII, by Jouanolou). It is also the input of the construction of Chern classes by Grothendieck (La théorie des classes de Chern, Bull. Soc. Math. France 86, 1958).

## Proof

The proof has three steps.

1. `projectiveBundleFormula_of_unitOnEtalePoints` only unfolds the definitions: $\mathrm{D1}$ is the statement `PBF q V` for each $V$ with $q$ invertible.
2. [projectiveBundleFormula_discrete_space](/entry/projective-bundle-formula-discrete-space/) gives the formula for a *discrete* space, that is, a presheaf of sets $F$ seen as a constant simplicial presheaf. Its proof is in [pbf_disc](/entry/pbf-disc/). On a discrete space each vector bundle is equal to the trivial one, and the formula comes from the formula for the trivial bundle on a scheme.
3. `projectiveBundleFormula_of_discrete_spaces`, which is `PBFg.pbf_of_disc`, reduces a general space $E$ to discrete ones. The code writes $\mathbb{P}(V)$ as the diagonal of a simplicial space whose term in degree $p$ is $E_p \times \mathrm{Fib}_N$, with $E_p$ discrete. The class $\xi^j$ comes from a fixed cocycle on a space $\mathrm{lineSp}$ that carries one line bundle and the unit $q$. Its pullbacks to the terms and to the diagonal agree with $\xi^j$ by naturality of $c_1$ and of cup powers. Then `PBFc.pbf_of_model` takes the formula on each term (from step 2) to the formula on the diagonal, through the chains of the diagonal and the total complex of the simplicial space.

We read the statement of `pbf_of_model` but not its proof.

## In the Lean code

The theorem is in [ProjectiveBundleFormulaVectorBundleAnySpace.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ProjectiveBundleFormulaVectorBundleAnySpace.lean#L11). The lemmas:

- `pbfMap`, `PBF` and `projectiveBundleFormula_of_unitOnEtalePoints` are in [ProjectiveBundleFormulaOfUnitOnEtalePoints.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ProjectiveBundleFormulaOfUnitOnEtalePoints.lean#L9).
- `projectiveBundleFormula_of_discrete_spaces` is in [ProjectiveBundleFormulaOfDiscreteSpacesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ProjectiveBundleFormulaOfDiscreteSpacesStatement.lean#L6). Its proof is `first | exact @GlobalTheory.PBFg.pbf_of_disc | ...`, a wrapper.
- `pbf_of_disc` is in [ProjectiveBundleFormulaOfDiscreteSpaces.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ProjectiveBundleFormulaOfDiscreteSpaces.lean#L65).
- `pbf_of_model` is in [ChainsIsStrictlyLE.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ChainsIsStrictlyLE.lean#L62).

The cup product, $c_1$ and the unit class are defined by `pick`, which returns $0$ when no object with the required property exists. So the formula has its expected meaning only because objects with these properties exist. For the pairing behind the cup product, this is `s2` in `AwSpec.lean`.
