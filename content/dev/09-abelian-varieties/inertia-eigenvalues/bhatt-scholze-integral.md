---
id: bhatt-scholze-integral
title: Crystalline lattices are prismatic F-crystals, the proof
kind: theorem
decl: GlobalTheory.BSP.bhattScholzeIntegral
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.BhattScholzeIntegral
covers: 740
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement `BhattScholzeIntegral`: crystalline $\mathbb{Z}_\ell$-lattices come from prismatic F-crystals, and equivariant maps of lattices come from unique maps of F-crystals. Its only user is [`bhatt_scholze_integral_of_literature`](/entry/bhatt-scholze-integral-of-literature/), which states the theorem in full and gives the source (Bhatt and Scholze, Camb. J. Math. 11, 2023). This entry follows the proof. The proof reduces both parts from a given $A_{\mathrm{inf}}$-prism $P_0$ to one standard $A_{\mathrm{inf}}$-prism, and the work is done there by three lemmas.

## Statement

As in [the parent entry](/entry/bhatt-scholze-integral-of-literature/). Let $K$ be a finite extension of $\mathbb{Q}_\ell$ and $(P_0, e)$ a prism over $\mathcal{O}_K$ with an identification $e$ of its ring with $A_{\mathrm{inf}}$ (`IsAinf`). Then (1) each $G_K$-stable lattice $T$ in a crystalline representation is realised at $P_0$ by some F-crystal $E$, and (2) for F-crystals $E$, $E'$ that realise $T$, $T'$, each $G_K$-equivariant map $f \colon T \to T'$ comes from a unique map $u \colon E \to E'$.

Write $P_{\mathrm{st}}$ for the standard prism `ainfObj K` with its identity identification `ainfId K`.

## Proof

**Change of prism.** `etaleRealisation_indep_ainfModel` gives a map of prisms $a \colon P_0 \to P_{\mathrm{st}}$ with two properties for each F-crystal $M$. The transition map $M(a) \colon M(P_0) \to M(P_{\mathrm{st}})$ is bijective. A realisation $j_0$ of $T$ at $P_{\mathrm{st}}$ gives a realisation at $P_0$, and a realisation $j$ at $P_0$ comes from a realisation $j_0$ at $P_{\mathrm{st}}$ with $j_0 \circ M(a) = j$.

**Part 1.** `crystallineLattice_prismaticFCrystal_perfectPrism` gives $M$ and a realisation $j_0$ of $T$ at $P_{\mathrm{st}}$. Move $j_0$ to $P_0$.

**Part 2.** Move $j$, $j'$ to realisations $j_0$, $j_0'$ at $P_{\mathrm{st}}$. `exists_FCrystalHom_of_equivariantEtaleMap_ainf` gives $u \colon E \to E'$ with $j_0' \circ u = (1 \otimes f) \circ j_0$ at $P_{\mathrm{st}}$. A map of F-crystals commutes with transition maps (the field `u_tr` of `FHom`), so the same identity holds at $P_0$. For uniqueness, let $u'$ also satisfy it at $P_0$. Since $E(a)$ is surjective, each $y \in E(P_{\mathrm{st}})$ is $E(a)(x)$, and then $j_0'(u'(y)) = j_0'(u(y))$. `fCrystalHom_eq_of_etale_realisation_perfectPrism` then gives $u' = u$. The rest is bookkeeping.

## In the Lean code

The theorem is in [BhattScholzeIntegral.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/BhattScholzeIntegral.lean#L14). The statement is in [the statement file](lean:Development/AbelianVarietyTheory/PublishedTheorems/GaloisCohomology₂/BhattScholzeIntegral.lean#L12). The four lemmas, each a second name:

- `etaleRealisation_indep_ainfModel`, for `Prism.realisation_indep_model`;
- `crystallineLattice_prismaticFCrystal_perfectPrism`, for `BSP.clause1_perfectPrism`;
- `exists_FCrystalHom_of_equivariantEtaleMap_ainf`, for `BSP.exists_fHom_of_equivariant`;
- `fCrystalHom_eq_of_etale_realisation_perfectPrism`, for `BSP.fHom_eq_of_realises`.

We have not opened the proofs of these four lemmas, so we do not know how close the Lean `FCrys` and `Realises` are to the objects of Bhatt and Scholze. This proof only moves between two models of $A_{\mathrm{inf}}$.
