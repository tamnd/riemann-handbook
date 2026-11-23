---
id: exists-hw-fon-cmp-ties
title: Wach modules, étale modules and comparisons at every prime, from Bhatt-Scholze
kind: theorem
decl: GlobalTheory.HWL.exists_hw_fon_cmp_ties
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.ExistsHwFonCmpTies
covers: 593
status: drafted
drafted_by: writer@claude
---
This theorem builds, at every prime $l$, a family of Wach modules, a family of étale $(\varphi, \Gamma)$-modules and comparison maps between them. Its one deep input is the Bhatt-Scholze theorem on crystalline lattices. The step [HypsAlt is nonempty from the closed bound](/step/nonempty-hyps/) uses it through `ExistsSlotsGlobal`. The proof is an assembly. The local construction is in [the next entry](/entry/exists-hw-of-fon-of-cmp-of-prime/) and below it.

## Statement

Assume `BhattScholzeCrystallineLattices`: for every crystalline $\mathbb Z_l$-lattice $T$ there is a prismatic F-crystal that realizes $T$, and every morphism of lattices lifts uniquely to the F-crystals. This is the main theorem of Bhatt and Scholze, "Prismatic F-crystals and crystalline Galois representations" (Cambridge J. Math. 11, 2023).

Let $L$ be a local theory (for each prime $l$, a record `LocPrime l` with period rings $B$ and $B_{\mathrm{dR}}$, their Galois actions, Frobenius and filtration). Let $A$ give for each $l$ an $A_{\mathrm{inf}}$ datum `LocAinf l (L l)`. Assume `LocTied` at every $l$: there are ring isomorphisms from $B$ to $B_{\mathrm{cris}}$ and from $B_{\mathrm{dR}}$ to the standard $B_{\mathrm{dR}}$, compatible with all this structure.

**Theorem.** There are $H$ (`HWOf L`), $F$ (`FonOf L A H`), a comparison in `CmpOf L A H F`, and a term of `Ties L A H F`.

## Proof

1. `wachLatticesExistAllLayers_of_bhattScholze` turns the Bhatt-Scholze hypothesis and `LocTied` into `WachEx (A l)` at each $l$: every étale layer has a Wach lattice.
2. [The statement](/entry/exists-hw-of-fon-of-cmp-of-prime/) `exists_hwOf_fonOf_cmpOf'` then gives $H$, $F$ and the comparison.
3. For `Ties`, the proof calls `nonempty_theta_deRhamFil_zero_concretePeriod` at each $l$ and picks a term with `Classical.choice`.

## In the Lean code

The theorem is at [ExistsHwFonCmpTies.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsHwFonCmpTies.lean#L13). The hypothesis is in [BhattScholzeCrystallineLattices.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/GaloisCohomology₂/BhattScholzeCrystallineLattices.lean#L12).

`Ties` is in [LocalSituation.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/LocalSituation.lean#L525). It has one field: at each $l$, a map $\theta \colon B_{\mathrm{dR}} \to \mathbb C_l$ that is a ring map on $\mathrm{Fil}^0$, onto, with kernel $\mathrm{Fil}^1$ and Galois-equivariant (`ThetaL`, line 508). This field does not use $H$ or $F$. So the last part of the conclusion says nothing about the objects that the theorem builds. Both callers discard it: `exists_hw_fon_cmp_of_integral` in [ExistsWachFunctorComparisonOfBhattScholze.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsWachFunctorComparisonOfBhattScholze.lean#L15) and [ExistsSlotsGlobal.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsSlotsGlobal.lean#L280).
