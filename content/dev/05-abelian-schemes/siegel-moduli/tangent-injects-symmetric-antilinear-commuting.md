---
id: tangent-injects-symmetric-antilinear-commuting
title: The Kodaira-Spencer map injects tangent vectors (statement form)
kind: theorem
decl: GlobalTheory.T.tangent_injects_symmetric_antilinear_commuting
module: Development.AbelianVarietyTheory.Proofs.ModuliProofs.TangentInjectsSymmetricAntilinearCommutingStatement
covers: 405
status: drafted
drafted_by: writer@claude
---
This theorem is the statement form of [`KS.tangent_injects_symm_antilinear`](/entry/tangent-injects-symm-antilinear/), with the same type. Its only caller is [`PelTan.finrank_derivation_le`](/entry/finrank-derivation-le/), which bounds the dimension of the tangent space of a PEL family by the dimension of a symmetric domain.

## Statement

**Theorem.** Assume `Out.Laws`, `Out.Laws2` and `ThetaUnifAV`. Let $t$ be a theta-level abelian scheme over $\operatorname{Spec} R$, with $R$ an $o$-algebra and a point $R \to \mathbb{C}$. Assume that a first-order deformation of the point along which $t$ is constant is trivial. Then there is a linear map $\kappa$ from the $o$-derivations $R \to \mathbb{C}$ to complex $g \times g$ matrices. It is injective, and each $\kappa(D)$ is symmetric for the Hermitian form of the complex fibre and commutes with the endomorphisms of $t$.

The entry [`tangent_injects_symm_antilinear`](/entry/tangent-injects-symm-antilinear/) gives each object and hypothesis in full.

## Proof

The proof is the tactic `first | exact @GlobalTheory.KS.tangent_injects_symm_antilinear | ...`. The two types agree, so the first branch closes the goal.

## In the Lean code

The theorem is in [TangentInjectsSymmetricAntilinearCommutingStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/TangentInjectsSymmetricAntilinearCommutingStatement.lean#L14). It is a renaming, with no content of its own. The real proof is in [`tangent_injects_symm_antilinear`](/entry/tangent-injects-symm-antilinear/). The file sets `maxHeartbeats` to 1,000,000 for this one-line proof.
