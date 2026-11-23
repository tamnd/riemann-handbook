---
id: gunif-holds
title: Complex uniformisation of the moduli models at the standard base point
kind: theorem
decl: UpperTheory.Gal.W2.GUnif_holds
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.SphericalCoordinates.FixedPointsIntBaseHolds
covers: 553
status: drafted
drafted_by: writer@claude
---
This theorem proves `GUnif`, the complex uniformisation of the moduli models. It is step 1 of [fixedPoints_int_base_holds](/entry/fixed-points-int-base-holds/), where it gives the smoothness of the base and the period lattices of the universal abelian scheme. The proof only applies [gUnif_of](/entry/g-unif-of/) to five proved facts. The real content is in that entry.

## Statement

Let $p$ be a prime and $D$ a PEL-type datum with $D.a = D.m = 1$, so that all embeddings of $F$ are one embedding $t_0$. Let $\rho \colon \mathcal{O}_D \to M_g(\mathbb{C})$ have the right signature at $t_0$ (`IsSigD`), and let `gb` be the standard base point over $\mathbb{C}$. Let $N \geq 3$ be prime to $p$, and $X$ a moduli model at level $N$ over $\mathbb{C}$ (`GenModel gb N`).

**Theorem.** $X$ is smooth of relative dimension $n - 1$, quasi-compact and separated over $\mathbb{C}$. Its universal abelian scheme is smooth of relative dimension $g$, the family is fine at level $N$ for $\rho$ (`FineAt`), and it has a complex uniformisation (`Unif`).

We have not unfolded `FineAt` or `Unif`.

## Proof

It is `gUnif_of` applied to:

- `ModelEx`: an integral model `Model b N` exists for each base $b$ and level $N$ (`GlobalTheory.UPel.HT.model_nonempty`, see [model_nonempty](/entry/model-nonempty/));
- `GenCmp`: $X$ is open and closed in the fibre of that model (`exists_open_closed_immersion_genModel_to_fibre`);
- `GenPts`: each complex point of the fibre lifts uniquely to $X$ (`complexModel_points_of_genericFiber_embedding`);
- `BaseC`: the standard base point comes from a base $b$ over $\mathbb{C}$ of type $\rho$ (`baseC_of`);
- `GFine`: fineness passes from the model to $X$ (`gFine_of`).

## In the Lean code

The theorem is in [FixedPointsIntBaseHolds.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/SphericalCoordinates/FixedPointsIntBaseHolds.lean#L164). `GUnif` and the five inputs are stated in [LevelChange.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/SphericalCoordinates/LevelChange.lean#L20), and `gUnif_of` is in [PGUnif.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/SphericalCoordinates/PGUnif.lean#L15). The theorem only passes the five facts along.
