---
id: projective-bundle-formula-discrete-space
title: The projective bundle formula on a discrete space, a renaming
kind: theorem
decl: GlobalTheory.T.projectiveBundleFormula_discrete_space
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ProjectiveBundleFormulaDiscreteSpaceStatement
covers: 1195
status: drafted
drafted_by: writer@claude-opus-5-5
---
This theorem is a second name for [pbf_disc](/entry/pbf-disc/), which has the real content. It is the projective bundle formula for a vector bundle on a discrete space. The [general formula](/entry/projective-bundle-formula-vector-bundle-any-space/) uses it as its base case. Below this theorem are 1,195 declarations, all of them below `pbf_disc`.

## Statement

A discrete space is a presheaf of sets $F$ on schemes, seen as a constant simplicial presheaf. The groups $H^n(E, \mathbb{Z}/q(i))$, the vector bundles and the map of the formula are as in [the general entry](/entry/projective-bundle-formula-vector-bundle-any-space/).

**Theorem.** Let $q \geq 1$, let $F$ be a presheaf of sets, let $V$ be a vector bundle of rank $N$ on the discrete space of $F$, and let $q$ be invertible on it. Then for all $n, i$ the map $(a_j) \mapsto \sum_{j<N} \pi^* a_j \cup \xi^j$ from $\bigoplus_{j<N} H^{n-2j}(F, \mathbb{Z}/q(i-j))$ to $H^n(\mathbb{P}(V), \mathbb{Z}/q(i))$ is bijective.

## Proof

The proof is the term `@GlobalTheory.EtC.pbf_disc`, with the same statement. There is no other step.

## In the Lean code

The theorem is in [ProjectiveBundleFormulaDiscreteSpaceStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ProjectiveBundleFormulaDiscreteSpaceStatement.lean#L5), a file of six lines. The proved statement `pbf_disc` is in [ProjectiveBundleFormulaDiscreteSpace.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ProjectiveBundleFormulaDiscreteSpace.lean#L18). The name moves the result from the namespace `GlobalTheory.EtC` to `GlobalTheory.T`. The general formula uses this name and not `pbf_disc`.
