---
id: idempotent-image-uniformised-by-factor-data
title: The image of an idempotent on a uniformised group is uniformised (statement form)
kind: theorem
decl: GlobalTheory.T.idempotent_image_uniformised_by_factor_data
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.IdempotentImageUniformisedByFactorDataStatement
covers: 329
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`MumDesc.image_unif`](/entry/image-unif/), which has the real content. It has two users, `Mum.CanonFam.exists_unif_refines` and `Mum.canon_pull_unif`, which build canonical Mumford families; both are below [`exists_chart_at`](/entry/exists-chart-at/) in the spine.

## Statement

Use the notation of [`image_unif`](/entry/image-unif/): a local domain $R$ with `Base R`, degeneration data $D, D'$ over $R$, a factor $F$ of $D$ in $D'$ with `F.Alg`, built from a ring $O$ with involution and elements $e, f \in O$.

**Theorem.** Let $G'$ be semi-abelian over $R$ with an $O$-linear uniformisation by $D'$. Let $G$ be semi-abelian with homomorphisms $i_G \colon G \to G'$ and $p_G \colon G' \to G$ such that $p_G i_G = 1$ and $i_G p_G = e$. Then $G$ has a uniformisation by $D$ whose bundle satisfies $\Lambda(L_G) \cong (i_G \times f i_G)^* \Lambda(L_{G'})$.

## Proof

The statement is the same as that of `GlobalTheory.MumDesc.image_unif`, and the proof applies it.

## In the Lean code

The theorem is in [IdempotentImageUniformisedByFactorDataStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IdempotentImageUniformisedByFactorDataStatement.lean#L12). The proof is `first | exact @GlobalTheory.MumDesc.image_unif | ...`. The type is copied word for word from [IdempotentImageUniformisedByFactorData.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IdempotentImageUniformisedByFactorData.lean#L18). The users call it in [CanonicalMumfordFamilyUniformisesRefinements.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CanonicalMumfordFamilyUniformisesRefinements.lean#L91) and [CanonicalMumfordFamilyPullbackLocalUniformised.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CanonicalMumfordFamilyPullbackLocalUniformised.lean#L48).
