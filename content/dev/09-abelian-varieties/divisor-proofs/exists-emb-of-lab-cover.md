---
id: exists-emb-of-lab-cover
title: Sections with a prescribed reduction give a projective map near the closed fibre
kind: theorem
decl: GlobalTheory.Mum.exists_emb_of_labCover
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsLabelledCoverEmbeddingClosedFibre
covers: 690
status: drafted
drafted_by: writer@claude
---
This theorem proves [`exists_labelledCover_embedding_closedFibre`](/entry/exists-labelled-cover-embedding-closed-fibre/), step 1 of [`hasFin_of_labCover`](/entry/has-fin-of-lab-cover/). It joins two results. The first gives sections of powers of the line bundle of a labelled cover with a prescribed reduction at the closed fibre. The second turns those sections into a map of a neighbourhood of the closed fibre to projective space.

## Statement

The statement is the one in the [statement entry](/entry/exists-labelled-cover-embedding-closed-fibre/): for $R$ with `Base R`, degeneration data $D$ and a labelled cover $C$ of $D$, there are a finite extension $\rho \colon R \to R'$ (`FinExt`), a pullback $D'$ of $D$, a labelled cover $C'$ of $D'$ and a datum $E$ (`Emb`) with `E.Theta`.

## Proof

1. [`exists_sections_prescribed_reduction_finite_ext`](/entry/exists-sections-prescribed-reduction-finite-ext/) gives a finite extension $\rho \colon R \to R_1$, a pullback $D_1$ of $D$ and a labelled cover $C_1$ of $D_1$ with a datum `Secs` for $C_1$. A `Secs` datum is a family of sections $s_0, \dots, s_N$ of $L^k$ and a section $\theta$ of $L$ on the generic fibre, with a smooth group $Y$ over the residue field and an immersion $Y \to \mathbb{P}^N$; along each complete trait the sections extend, and on the closed fibre they give the immersion and $\theta$ does not vanish on an open part of $Y$. The [entry for `secs_exists`](/entry/secs-exists/) gives the full definition.
2. $R_1$ again satisfies `Base`: `FinExt ρ` gives the first part, and $R_1$ has characteristic zero because $\rho$ is injective (`RingHom.charZero_iff`).
3. `exists_closedFibre_theta_embedding_of_sections`, applied to $C_1$ and its `Secs` datum, gives a labelled cover $C'$ of the same $D_1$ and a datum $E$ with `E.Theta`.

The output is $(R_1, \rho, D_1, C', E)$.

## In the Lean code

The theorem is in [ExistsLabelledCoverEmbeddingClosedFibre.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsLabelledCoverEmbeddingClosedFibre.lean#L14). It calls two lemmas:

- `GlobalTheory.T.exists_sections_prescribed_reduction_finite_ext`;
- `GlobalTheory.T.exists_closedFibre_theta_embedding_of_sections`, in [ExistsClosedFibreThetaEmbeddingOfSectionsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsClosedFibreThetaEmbeddingOfSectionsStatement.lean#L12). We read its statement, not its proof. It replaces $C_1$ by a new labelled cover $C'$ of the same data.

The finite extension is not needed. Step 1 is proved in [`exists_secs_finExt`](/entry/exists-secs-fin-ext/) with $R_1 = R$ and $\rho = \mathrm{id}$. So the proof gives $R' = R$, and the finite extension in step 1 of `hasFin_of_labCover` is the identity.
