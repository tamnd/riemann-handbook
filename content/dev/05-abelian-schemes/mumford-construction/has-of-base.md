---
id: has-of-base
title: Mumford's construction over a complete normal local base
kind: theorem
decl: GlobalTheory.Mum.has_of_base
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.HasSemiAbelianUniformisationCompleteNormalBase
covers: 3455
status: drafted
drafted_by: writer@claude
---
This theorem proves that degeneration data over a complete normal local domain of characteristic zero come from a semi-abelian scheme with a uniformisation. The proof reduces general data to data of unitary PEL type, and data of that type to a labelled cover. The [statement entry](/entry/has-semi-abelian-uniformisation-complete-normal-base/) restates it.

## Statement

Let $R$ be a local domain with maximal ideal $\mathfrak{m}$ and fraction field $K$. `Base R` says that $R$ is noetherian, integrally closed, $\mathfrak{m}$-adically complete and of characteristic zero.

Degeneration data $D$ over $R$ for $\mathfrak{m}$ (`DegData`) consist of: an abelian scheme $B$ over $R$ with an ample, rigidified, symmetric, cubical line bundle $L$ (`PolAV`, `DegPre`); a free abelian group $X$ of finite rank; a homomorphism $c \colon X \to B(R)$; and for each $\chi \in X$ a trivialisation $\psi(\chi)$ of $c(\chi)^* L^{-1}$ over $K$. From $\psi$ one forms $\tau(a, b) = \psi(a+b)\psi(a)^{-1}\psi(b)^{-1}$ (divided by the rigidification). The conditions: $\psi$ is even, $\tau$ is bimultiplicative, $\psi(\chi)$ has values in $\mathfrak{m}$ for $\chi \neq 0$, and for each $k$ only finitely many $\chi$ fail to have values in $\mathfrak{m}^k$. Faltings and Chai use two lattices and two maps $c, c^t$; here there is one of each.

`Has D` says: there are a semi-abelian scheme $G$ over $R$, a polarised abelian variety $A$ over $K$ and a uniformisation `Unif 𝔪 D A G`. Its fields say: $G$ is smooth and separated, its generic fibre is $A$ as a group, its cubical line bundle matches the one of $A$, and on each thickening $G \otimes R/\mathfrak{m}^{e+1}$ there are coordinates (`gt`) that compare it with the abelian part of $D$. The field `expand` asks for a bijection `ExpBij k` for each $k \geq 1$. We have not unfolded `GtCoord` or `ExpBij`.

**Theorem.** If `Base R`, then `Has D` for all degeneration data $D$ over $R$ for $\mathfrak{m}$.

The statement has the shape of Mumford's construction (D. Mumford, Compositio Math. 24 (1972); Faltings and Chai, *Degeneration of Abelian Varieties*, Springer 1990, Chapter III). We have not checked that `Unif` is the full uniformisation of those sources.

## Proof

1. If $X = 0$, `has_of_subsingleton` gives the result. It needs only that $R$ is noetherian, normal and complete.
2. Otherwise `exists_unitaryPELType_factor_degData` gives data $D'$ over $R$ of unitary PEL type for a CM field $E$ (`PelOK`, with signature $p = q \geq 1$). The data $D$ are a factor of $D'$ (`Factor`): an idempotent $e$ of a ring $O$ with involution that acts on $D'$ cuts out $D$.
3. `exists_labelledCover_unitaryPELType_finiteExt`: after a finite injective extension $R \to R'$, the pullback $D''$ of $D'$ has a labelled cover. $R'$ again satisfies `Base`.
4. [`hasSemiAbelianUniformisation_of_labelledCover`](/entry/has-semi-abelian-uniformisation-of-labelled-cover/) gives `HasFin D''`: a uniformisation after a further finite extension.
5. `hasFin_of_finExt` gives `HasFin D'`, and `hasSemiAbelianUniformisation_of_finiteExt` gives `Has D'`, with a semi-abelian $G'$ over $R$.
6. `exists_ringAction_extension_to_uniformised_semiAbelian` extends the action of $O$ to $G'$ and $A'$. The image of the idempotent $e$ on $G'$ is a semi-abelian $G$ (`IdemImage.isSemiAbelian_image`).
7. `idempotentFactor_uniformised_of_degData_factor`: after a finite extension $R \to R_1$, the pullback of $G$ is uniformised by the pullback of $D$. It is semi-abelian by `isSemiAbelian_of_isGrpPullback'`. Then `hasSemiAbelianUniformisation_of_finiteExt` gives `Has D`.

## In the Lean code

The theorem is in [HasSemiAbelianUniformisationCompleteNormalBase.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasSemiAbelianUniformisationCompleteNormalBase.lean#L32). The lemma `isSemiAbelian_of_isGrpPullback'` (line 27) is in the same file: a group pullback of a semi-abelian scheme is semi-abelian. The file [HasSemiAbelianUniformisationOfLabelledCover.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasSemiAbelianUniformisationOfLabelledCover.lean#L26) has the same lemma with the same proof under the name `CoverFin.semiAbelian_of_pull`.

We read the statements of the lemmas in steps 1 to 7, not their proofs.
