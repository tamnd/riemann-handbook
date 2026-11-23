---
id: mat-in-holds
title: The piece of a tower embeds into the cohomology of a model
kind: theorem
decl: UpperTheory.Gal.Seam.matIn_holds
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.CrystallineTowers.LocTowerHolds
covers: 4163
status: drafted
drafted_by: writer@claude
---
This theorem proves `MatIn`: over a local field, the Galois action on a piece of a tower embeds into the Galois action on the cohomology of a smooth projective model. It is step 3 of [the crystalline step from the comparison theorem](/entry/crys-step-of/). After it, the comparison theorem for the model makes the piece crystalline. Almost all of its 4,163 declarations are below [the finiteness of $\ell$-adic cohomology](/entry/v-fin-holds/).

## Statement

Let $K$ be a finite extension of $\mathbb{Q}_\ell$ in $\overline{\mathbb{Q}}_\ell$ and $H$ a nice tower over $K$ with eigenvalues $\theta$ (see [the local steps](/entry/steps-holds/)). Let $C$ be a cover of $H$ over $\mathcal{O}_K$ that is onto (see [the crystalline step from the comparison theorem](/entry/crys-step-of/)), with scheme $Y$ over $\mathcal{O}_K$. Write $V_n = H^n(Y_{\overline{\mathbb{Q}}_\ell}, \mathbb{Q}_\ell)$. Let $\rho_1 \colon G_K \to \mathrm{GL}_d(\overline{\mathbb{Q}}_\ell)$ be a matrix form of the Galois action on the piece (`IsMat`).

**Theorem.** There are $N$, bases $b_n$ of $V_n$ for $n < N$, and an injective matrix $M$ with entries in $\overline{\mathbb{Q}}_\ell$, such that for all $\sigma \in G_K$

$$\Bigl(\bigoplus_{n < N} R_n(\sigma)\Bigr) M = M \rho_1(\sigma),$$

where $R_n(\sigma)$ is the matrix of $\sigma$ on $V_n$ in the basis $b_n$. So the piece is a $G_K$-subrepresentation of $\overline{\mathbb{Q}}_\ell \otimes \bigoplus_{n < N} V_n$.

## Proof

The proof is `matInS vFin_holds pieceIn_holds negVan`. The theorem `matInS` takes three hypotheses.

1. `pieceIn_holds` proves `PieceIn`. Let $Z$ be the variety of the tower. The cover gives a finite étale Galois map $Z_{\overline{\mathbb{Q}}_\ell} \to Y_{\overline{\mathbb{Q}}_\ell}$ with group $\Delta$. Then the pullback $H^*(Y_{\overline{\mathbb{Q}}_\ell}) \to H^*(Z_{\overline{\mathbb{Q}}_\ell})$ is injective, commutes with $G_K$, and has the piece in its image (after the base change to $\overline{\mathbb{Q}}_\ell$). The proof `pieceInS` uses `vInv_holds`: for a finite étale Galois cover, the pullback is injective with image the $\Delta$-invariants. It also uses `hopEx_holds`: each $\delta \in \Delta$ is an operator $T_g$ with $\theta(g) = 1$, so it fixes the piece.
2. `vFin_holds` proves that each $V_n$ has finite dimension. $Y$ is proper because it is projective.
3. `negVan` proves that $V_n = 0$ for $n < 0$, because the Ext groups in negative degree are zero.

Then a private lemma `core` of linear algebra gives $N$, the bases and $M$. The piece has finite dimension and lies in the image of an injective equivariant map from $\bigoplus_n V_n$. Only finitely many $V_n$ meet it, and none with $n < 0$. The rest is bookkeeping.

## In the Lean code

The theorem is in [LocTowerHolds.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/CrystallineTowers/LocTowerHolds.lean#L23). Also used:

- `MatIn` and `PieceIn`, in [LocTower.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/CrystallineTowers/LocTower.lean#L62).
- `matInS`, in [MatInS.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/CrystallineTowers/MatInS.lean#L132).
- `pieceInS`, in [PieceInS.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/CrystallineTowers/PieceInS.lean#L126).
- `negVan`, in [NegVan.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/CrystallineTowers/NegVan.lean#L27).

The lemma `hopEx_holds` is `hopExS trivial`. The theorem `hopExS` has the type `True → HopEx`, so its hypothesis is vacuous ([HopExS.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/CrystallineTowers/HopExS.lean#L37)).
