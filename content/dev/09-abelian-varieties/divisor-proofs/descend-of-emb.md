---
id: descend-of-emb
title: A semi-abelian scheme on a modification descends to the base
kind: theorem
decl: GlobalTheory.Mum.descend_of_emb
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.SemiAbelianDescendsOfClosedFibreEmbedding
covers: 387
status: drafted
drafted_by: writer@claude
---
This theorem takes a semi-abelian scheme $G'$ over a proper modification $S \to \operatorname{Spec} R$ and shows that it is the pullback of a semi-abelian scheme $G$ over $\operatorname{Spec} R$, with its cubical line bundle. The input is a map of a neighbourhood of the closed fibre to projective space and a theta section that does not vanish there. Its restatement is [`semiAbelian_descends_of_closedFibre_embedding`](/entry/semi-abelian-descends-of-closed-fibre-embedding/), which is step 2 of [`hasFin_of_labCover`](/entry/has-fin-of-lab-cover/).

## Statement

Let $R$ be a local domain with maximal ideal $\mathfrak{m}$ that is noetherian, integrally closed and $\mathfrak{m}$-adically complete (`AdmBase R 𝔪`). Let $M$ be a modification of $\operatorname{Spec} R$: an integral scheme $S$ with a proper map $\pi \colon S \to \operatorname{Spec} R$ and a dominant point $\operatorname{Spec} K \to S$ over $\operatorname{Spec} R$, where $K = \operatorname{Frac} R$ (`Modif`). Let $G'$ be a commutative semi-abelian scheme over $S$ with a cubical line bundle $P'$ (`CP`: a rigidified line bundle $L'$ with a cubical structure and a symmetry). Let $E$ be an embedding datum (`Emb`):

- an open $H \subseteq G'$ that contains every point over the closed point of $\operatorname{Spec} R$, and a map $f \colon H \to \mathbb{P}^N_R$ over $\operatorname{Spec} R$;
- a smooth group $Y$ over the residue field $k$ with an immersion $j \colon Y \to \mathbb{P}^N_R$ over $\operatorname{Spec} k$;
- for each field point $x$ of $S$ over the closed point, after a field extension, a group isomorphism of the fibre $G'_x$ with $Y$ that is compatible with $f$ and $j$.

Suppose that $E$ satisfies `E.Theta L'`: there are a section $\theta$ of $L'$ and a nonempty open $O \subseteq Y$ such that $\theta$ does not vanish at any point $g$ of $H$ over the closed point with $f(g) \in j(O)$.

**Theorem.** Then there are a commutative semi-abelian scheme $G$ over $\operatorname{Spec} R$ with a cubical line bundle $P$ and a map $\beta \colon G' \to G$ such that $G'$ is the group pullback $\pi^* G$ by $\beta$ (`IsGrpPullback`) and $L' \cong \beta^* L$, where $L$ is the line bundle of $P$.

## Proof

1. `Modif.appTop_bijective_surjective`: $\pi$ is surjective. It uses that $R$ is noetherian and integrally closed.
2. `exists_smooth_model_near_closedFibre_embedding`: there is a smooth, separated, quasi-compact $U$ over $\operatorname{Spec} R$ with an open immersion $U \times_R S \to G'$ over $S$ that hits every point over the closed point (`Near`). On this open, $f$ is the pullback of a map $f_U \colon U \to \mathbb{P}^N_R$.
3. `mul_descends_near_closed_fibre_of_embedding`: the group law of $G'$ descends to a law on an open of $U \times_R U$ that contains the closed fibre (`Near.Law`).
4. `semiAbelian_descends_of_descends_near_closedFibre`: there are a semi-abelian $G$ over $\operatorname{Spec} R$, an open immersion $U \to G$ and $\beta$ with $G' = \pi^* G$.
5. `exists_open_thetaNonvanishing_descendedGroup`: `E.Theta` gives an open of $G$ that meets the closed fibre, over which $\theta$ does not vanish on the closed fibre of $G'$.
6. `cubicalBundle_modification_descends_to_group`: there is a line bundle $L$ on $G$ with $L' \cong \beta^* L$.
7. `exists_cp_descent'`: $L$ is the line bundle of a cubical structure $P$ on $G$.

## In the Lean code

The theorem is in [SemiAbelianDescendsOfClosedFibreEmbedding.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SemiAbelianDescendsOfClosedFibreEmbedding.lean#L24). The lemmas of steps 2 to 7 are `GlobalTheory.T` statements, each in its own file. We read their statements, not their proofs. The proof only chains them.

The statement does not say that $P$ is the descent of $P'$ as a cubical structure: it only says that the underlying line bundles match. Of `Modif.appTop_bijective_surjective`, the proof uses only the surjectivity of $\pi$.
