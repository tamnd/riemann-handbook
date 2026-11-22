---
id: has-fin-of-lab-cover
title: A labelled cover gives a uniformisation after a finite extension
kind: theorem
decl: GlobalTheory.Mum.hasFin_of_labCover
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.HasSemiAbelianUniformisationOfLabelledCover
covers: 1084
status: drafted
drafted_by: writer@claude
---
This theorem turns a labelled cover of degeneration data into a uniformised semi-abelian scheme over a finite extension of the base. A labelled cover is a semi-abelian scheme over a proper modification of $\operatorname{Spec} R$ that is uniformised along every complete trait. The proof descends it to $\operatorname{Spec} R'$ and then uses one trait. It is restated as [`hasSemiAbelianUniformisation_of_labelledCover`](/entry/has-semi-abelian-uniformisation-of-labelled-cover/), and that name is step 4 of [`has_of_base`](/entry/has-of-base/).

## Statement

Let $R$ be a local domain with maximal ideal $\mathfrak{m}$ and fraction field $K$ that satisfies `Base R`, and let $D$ be degeneration data over $R$ for $\mathfrak{m}$. The [entry for `has_of_base`](/entry/has-of-base/) unfolds both.

A labelled cover $C$ of $D$ (`LabCover D`) consists of:

- a modification: an integral scheme $S$ with a proper map $\pi \colon S \to \operatorname{Spec} R$ and a dominant point $\operatorname{Spec} K \to S$ over $\operatorname{Spec} R$ (`Modif`);
- a semi-abelian $G$ over $S$ with a cubical line bundle, and a polarised abelian variety $A$ over $K$ that is the generic fibre of $G$;
- an odd prime $n$ that is a unit in $R$, and labels: for each $j$, a map from the $n^j$-torsion points of $D$ over $\overline{K}$ (`QkPt`) to $A(\overline{K})$;
- the trait condition: for each complete discrete valuation ring $W$ with an injective local map $R \to W$ and a lift $\xi \colon \operatorname{Spec} W \to S$, there is a finite extension $W \to W'$ over which $\xi^* G$ is uniformised by the pullback of $D$, compatibly with the labels (`QkToAkU`).

`HasFin D` says: there are a finite injective map $R \to R'$ (`FinExt`) and a pullback $D'$ of $D$ over $R'$ (`IsPullDeg`) with `Has D'`.

**Theorem.** If `Base R` and $D$ has a labelled cover, then `HasFin D`.

## Proof

1. `exists_labelledCover_embedding_closedFibre`: after a finite extension $R \to R'$, the pullback $D'$ has a labelled cover $C'$ with a map $E$ of a neighbourhood of the closed fibre of $C'.G$ to $\mathbb{P}^N_{R'}$ (`Emb`). The fibres of $C'.G$ over the closed fibre of $S$ all match one smooth group $Y$ over the residue field, and a theta section does not vanish on an open part of $Y$ (`Emb.Theta`).
2. `semiAbelian_descends_of_closedFibre_embedding`: $C'.G$ is the pullback by $\pi$ of a semi-abelian scheme $G$ over $\operatorname{Spec} R'$, with its line bundle.
3. `PrimeUnif.exists_cdvr`: there is an injective local map $\varphi \colon R' \to V$ to a complete discrete valuation ring. By the valuative criterion of properness (`val_exists`, applied to $\pi$), $\operatorname{Spec} V \to \operatorname{Spec} R'$ lifts to $\xi \colon \operatorname{Spec} V \to S$.
4. The trait condition of $C'$ at $(V, \varphi, \xi)$ gives a uniformisation over a finite extension $W'$ of $V$ of the pullback of $C'.G$, which is also a pullback of $G$.
5. `exists_finiteExtension_uniformisation_of_trait_unif`: a uniformisation of $G$ along one trait gives a uniformisation of $G$ after a finite extension $R' \to R_1$. So `HasFin D'`.
6. `hasSemiAbelianUniformisation_of_finiteExt_trans` carries `HasFin` from $D'$ to $D$.

## In the Lean code

The theorem is in [HasSemiAbelianUniformisationOfLabelledCover.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasSemiAbelianUniformisationOfLabelledCover.lean#L43). Two helper lemmas are in the same file: `CoverFin.semiAbelian_of_pull` (a group pullback of a semi-abelian scheme is semi-abelian) and `CoverFin.isLocalHom_of_comap`. The first is the same lemma, with the same proof, as `Mum.isSemiAbelian_of_isGrpPullback'` in the file of `has_of_base`.

We read the statements of the lemmas in steps 1 to 6, not their proofs. The labels of $C'$ and the last clause of the trait condition are not used in this proof; the proof drops the last output of `C'.trait`.
