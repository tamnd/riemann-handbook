---
id: projective-bundle-formula-of-discrete-spaces
title: From discrete spaces to all spaces, a renaming
kind: theorem
decl: GlobalTheory.T.projectiveBundleFormula_of_discrete_spaces
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ProjectiveBundleFormulaOfDiscreteSpacesStatement
covers: 395
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [pbf_of_disc](/entry/pbf-of-disc/), which has the real content. It says that the projective bundle formula on all discrete spaces gives it on all spaces. [The general formula](/entry/projective-bundle-formula-vector-bundle-any-space/) uses it as its step 3. Below this theorem are 395 declarations, all of them below `pbf_of_disc`.

## Statement

Spaces, discrete spaces $\operatorname{disc} F$, vector bundles $V \colon E \to B\mathrm{GL}_N$ and the condition `Inv q E` ($q$ is a unit on each scheme $U$ with a point of $E$ over $U$) are as in [pbf_disc](/entry/pbf-disc/). `PBF q V` says that for all $n, i \in \mathbb{Z}$ the map $(a_j) \mapsto \sum_{j<N} \pi^* a_j \cup c_1(L)^j$ to $H^n(\mathbb{P}(V), \mathbb{Z}/q(i))$ is bijective.

**Theorem.** Let $q \geq 1$ and $N \geq 0$. Suppose that `PBF q V` holds for each presheaf $F$ and each $V \colon \operatorname{disc} F \to B\mathrm{GL}_N$ with `Inv q (disc F)`. Then `PBF q V` holds for each space $E$ and each $V \colon E \to B\mathrm{GL}_N$ with `Inv q E`.

The rank $N$ is the same in the hypothesis and in the result.

## Proof

The proof is `first | exact @GlobalTheory.PBFg.pbf_of_disc | ...`, and the statement of `pbf_of_disc` is the same, so the term fits as it is. There is no other step.

## In the Lean code

The theorem is in [ProjectiveBundleFormulaOfDiscreteSpacesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ProjectiveBundleFormulaOfDiscreteSpacesStatement.lean#L6), a file of seven lines. It sets `maxHeartbeats` to 1000000 for a proof that is one term. `PBF` and `pbfMap` are in [ProjectiveBundleFormulaOfUnitOnEtalePoints.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ProjectiveBundleFormulaOfUnitOnEtalePoints.lean#L9). The name moves the result from `GlobalTheory.PBFg` to `GlobalTheory.T`.
