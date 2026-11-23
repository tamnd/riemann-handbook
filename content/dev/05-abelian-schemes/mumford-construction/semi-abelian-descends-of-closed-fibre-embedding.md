---
id: semi-abelian-descends-of-closed-fibre-embedding
title: A semi-abelian scheme on a modification descends to the base (statement)
kind: theorem
decl: GlobalTheory.T.semiAbelian_descends_of_closedFibre_embedding
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.SemiAbelianDescendsOfClosedFibreEmbeddingStatement
covers: 388
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`descend_of_emb`](/entry/descend-of-emb/). It is step 2 of [`hasFin_of_labCover`](/entry/has-fin-of-lab-cover/): the semi-abelian scheme of a labelled cover, on a proper modification of $\operatorname{Spec} R$, comes from one over $\operatorname{Spec} R$. The content is in `descend_of_emb`.

## Statement

Let $R$ be a noetherian, integrally closed local domain, complete for its maximal ideal $\mathfrak{m}$ (`AdmBase R 𝔪`). Let $\pi \colon S \to \operatorname{Spec} R$ be a modification (`Modif R`, see [`hasFin_of_labCover`](/entry/has-fin-of-lab-cover/)). Let $G'$ be a commutative group over $S$ that is semi-abelian (`IsSemiAbelian`: smooth, separated, quasi-compact and geometrically connected, with a `TorusExtension` structure on each geometric fibre, which we have not unfolded). Let $P'$ be a cubical structure on $G'$ (`CP`: a rigidified line bundle $L'$ with a cubical structure and a symmetry). Let $E$ be an `Emb` datum for $G'$ over $\pi$ with `E.Theta` for $L'$, as in [`exists_labelledCover_embedding_closedFibre`](/entry/exists-labelled-cover-embedding-closed-fibre/).

**Theorem.** There are a semi-abelian group $G$ over $\operatorname{Spec} R$ with a cubical structure $P$ (line bundle $L$) and a map $\beta \colon G' \to G$ such that $G'$ is the pullback of $G$ along $\pi$ as a group (`IsGrpPullback`) and $L' \cong \beta^* L$ (`LBIso`).

## Proof

The proof is the term `GlobalTheory.Mum.descend_of_emb`, which has the same statement.

## In the Lean code

The theorem is in [SemiAbelianDescendsOfClosedFibreEmbeddingStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SemiAbelianDescendsOfClosedFibreEmbeddingStatement.lean#L12). The proof is the usual `first | exact … ` form of a second name.

The hypothesis is `AdmBase`, not `Base`: characteristic zero is not assumed. `hasFin_of_labCover` supplies it from `FinExt ρ`. The fact that $G'$ is the semi-abelian scheme of a labelled cover is not used; any semi-abelian $G'$ on a modification with such an `Emb` datum descends.
