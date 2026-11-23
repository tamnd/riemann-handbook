---
id: idempotent-image-iso-uniformised-factor-with-adjoint-pair
title: The image of an idempotent is isomorphic to any group uniformised by its data (statement form)
kind: theorem
decl: GlobalTheory.T.idempotent_image_iso_uniformised_factor_with_adjoint_pair
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.IdempotentImageIsoUniformisedFactorOfAdjointPairStatement
covers: 311
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`MumIsoAdj.iso_of_factor_adj`](/entry/iso-of-factor-adj/), which has the real content. Its one user is [`MumDesc.image_unif`](/entry/image-unif/), as step 2 of its proof.

## Statement

Use the notation of [`image_unif`](/entry/image-unif/): $R$, $D$, $D'$, a factor $F$ with `F.Alg` and elements $e, f \in O$, an $O$-linear uniformised $G'$, and the retract $G$ with $i_G$, $p_G$.

**Theorem.** Let $G_0$ be semi-abelian over $R$ with a uniformisation by $D$. Then there are homomorphisms $\varepsilon \colon G \to G_0$ (an isomorphism), $u \colon G' \to G_0$ and $u' \colon G_0 \to G'$ such that $\varepsilon = u \, i_G$, $u' u = e^* f e$, and $u, u'$ are adjoint for the bundles $L_{G'}$ and $L_{G_0}$ (`GAdj`).

## Proof

The statement is the same as that of `GlobalTheory.MumIsoAdj.iso_of_factor_adj`, and the proof applies it.

## In the Lean code

The theorem is in [IdempotentImageIsoUniformisedFactorOfAdjointPairStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IdempotentImageIsoUniformisedFactorOfAdjointPairStatement.lean#L13). The proof is `first | exact @GlobalTheory.MumIsoAdj.iso_of_factor_adj | ...`. The type is copied word for word from [IdempotentImageIsoUniformisedFactorOfAdjointPair.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IdempotentImageIsoUniformisedFactorOfAdjointPair.lean#L32).
