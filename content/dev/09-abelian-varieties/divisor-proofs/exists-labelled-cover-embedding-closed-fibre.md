---
id: exists-labelled-cover-embedding-closed-fibre
title: A labelled cover with a projective map near the closed fibre (statement)
kind: theorem
decl: GlobalTheory.T.exists_labelledCover_embedding_closedFibre
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsLabelledCoverEmbeddingClosedFibreStatement
covers: 691
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`exists_emb_of_labCover`](/entry/exists-emb-of-lab-cover/). It is step 1 of [`hasFin_of_labCover`](/entry/has-fin-of-lab-cover/). The content is in [`secs_exists`](/entry/secs-exists/), below `exists_emb_of_labCover`.

## Statement

Let $R$ be a local domain with `Base R`, $D$ degeneration data over $R$ for its maximal ideal, and $C$ a labelled cover of $D$, as in [`hasFin_of_labCover`](/entry/has-fin-of-lab-cover/).

**Theorem.** There are a finite injective map $\rho \colon R \to R'$ to a complete normal noetherian local domain (`FinExt ρ`), a pullback $D'$ of $D$ along $\rho$ (`IsPullDeg`), a labelled cover $C'$ of $D'$ and a datum $E$ (`Emb C'.π C'.G`) with `E.Theta` for the line bundle of $C'$.

The datum $E$ is a map of an open neighbourhood $H$ of the closed fibre of $C'.G$ to $\mathbb{P}^N_{R'}$, a smooth group $Y$ over the residue field and an immersion $j \colon Y \to \mathbb{P}^N$, such that the fibre of $C'.G$ at each field-valued point over the closed point is $Y$ after a field extension, compatibly with the two maps. `E.Theta` says that a global section $\theta$ of the line bundle does not vanish at the points of $H$ over the closed point that map to $j(O)$, for a nonempty open $O \subseteq Y$.

## Proof

The proof is the term `GlobalTheory.Mum.exists_emb_of_labCover`, which has the same statement.

## In the Lean code

The theorem is in [ExistsLabelledCoverEmbeddingClosedFibreStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsLabelledCoverEmbeddingClosedFibreStatement.lean#L12). The proof has the usual `first | exact …` form of a second name. `Emb` and `Emb.Theta` are in [TateProductRigidificationTrivial.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/TateProductRigidificationTrivial.lean#L108).
