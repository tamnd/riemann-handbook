---
id: bhatt-scholze-integral-of-literature
title: Crystalline lattices are prismatic F-crystals, as a literature input
kind: theorem
decl: UpperTheory.LiteratureTheorems.bhatt_scholze_integral_of_literature
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.EveryCharacterOfLiteratureOfVWin
covers: 741
status: drafted
drafted_by: writer@claude
---
This theorem gives the statement `BhattScholzeIntegral`. It takes a proof $O$ of [OpenLiteratureStatements](/step/open-literature-statements-def/) and does not use it. The proof is one term, [`bhattScholzeIntegral`](/entry/bhatt-scholze-integral/), and that entry has the real content. The result fills the field `bs` of `published_results_local`, which is the field `nLink` of [the eigen bundle](/step/published-results-eigen/). The theorem `bhatt_scholze_crystalline_lattices_of_literature` also uses it. Below this theorem are 741 declarations.

## Statement

Let $\ell$ be a prime and $K$ a finite extension of $\mathbb{Q}_\ell$. Let $P_0$ be a prism over $\mathcal{O}_K$ with an isomorphism $e$ from its ring to $A_{\mathrm{inf}}$, compatible with Frobenius, the ideal and the structure map (`IsAinf`).

**Theorem.**

1. Let $V$ be a continuous representation of $G_K$ on a finite-dimensional $\mathbb{Q}_\ell$-space that is crystalline (`IsCrys`) for a standard local prime. Let $T \subset V$ be a $G_K$-stable $\mathbb{Z}_\ell$-lattice. Then there are a prismatic F-crystal $E$ (`FCrys`) and a map $j$ such that $E$ realises $T$ at $P_0$ (`Realises`).
2. Let $E$ and $E'$ realise $T$ and $T'$. Then each $G_K$-equivariant $\mathbb{Z}_\ell$-linear map $f \colon T \to T'$ comes from a unique map $u \colon E \to E'$ of F-crystals.

`Realises` says that $j$ is a map from the value $E(P_0)$ to `WCb l` $\otimes\, T$, compatible with Frobenius and with $G_K$. We have not unfolded `WCb`, `FCrys` or `IsStd`.

Part 1 is essential surjectivity and part 2 is full faithfulness of the étale realisation. This is the theorem of Bhatt and Scholze (Prismatic F-crystals and crystalline Galois representations, Camb. J. Math. 11, 2023).

## Proof

Apply `GlobalTheory.BSP.bhattScholzeIntegral`. The argument $O$ is not used.

## In the Lean code

The theorem is at [EveryCharacterOfLiteratureOfVWin.lean line 267](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L267). The statement is in [BhattScholzeIntegral.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/GaloisCohomology₂/BhattScholzeIntegral.lean#L12). The proof below is in [the proof file](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/BhattScholzeIntegral.lean#L14). It uses `etaleRealisation_indep_ainfModel`, `crystallineLattice_prismaticFCrystal_perfectPrism` and `exists_FCrystalHom_of_equivariantEtaleMap_ainf`.

Odd points. The name says "of literature", but the code proves the statement and ignores $O$. In part 1 the local prime $P$ enters only through `IsCrys`; the conclusion does not mention it.
