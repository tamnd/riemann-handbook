---
id: finrank-tangent-pel-family-le-symmetric-domain
title: The tangent space of a PEL family is at most the dimension of the symmetric domain (statement form)
kind: theorem
decl: GlobalTheory.T.finrank_tangent_PEL_family_le_symmetricDomain
module: Development.AbelianVarietyTheory.Proofs.ModuliProofs.FinrankTangentPELFamilyLeSymmetricDomainStatement
covers: 424
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`PelTan.finrank_derivation_le`](/entry/finrank-derivation-le/), with the same type. [`exists_thetaFam_isPEL_smooth`](/entry/exists-theta-fam-is-pel-smooth/) uses it for the tangent bound on each affine chart of the theta family, which gives the smooth generic fibre. Its dominator in the written proof is the step [EveryCharacter from the literature and VWin](/step/every-character-of-literature/).

## Statement

Let $o \to R \to \mathbb{C}$ be ring maps. Let $t$ be a theta level object over $\operatorname{Spec} R$ with a PEL structure of signature $(p, q)$ for the CM field $E$, and suppose that $t$ is unramified on first-order deformations over $\mathbb{C}[\varepsilon]$. Then

$$\dim_{\mathbb{C}} \operatorname{Der}_o(R, \mathbb{C}) \le \tfrac{[E:\mathbb{Q}]}{2}\,pq.$$

The entry [`finrank_derivation_le`](/entry/finrank-derivation-le/) gives all hypotheses and the proof.

## Proof

The proof is the tactic `first | exact @GlobalTheory.PelTan.finrank_derivation_le | ...`. The first branch closes the goal, since the two types are the same.

## In the Lean code

The theorem is in [FinrankTangentPELFamilyLeSymmetricDomainStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/FinrankTangentPELFamilyLeSymmetricDomainStatement.lean#L13). It is a renaming. It carries seven hypotheses that the proof never uses; the entry [`finrank_derivation_le`](/entry/finrank-derivation-le/) lists them.
