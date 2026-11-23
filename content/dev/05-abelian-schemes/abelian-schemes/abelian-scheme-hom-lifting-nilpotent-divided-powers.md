---
id: abelian-scheme-hom-lifting-nilpotent-divided-powers
title: Lifting abelian schemes and their homomorphisms over a nilpotent divided power thickening
kind: theorem
decl: GlobalTheory.abelianScheme_hom_lifting_nilpotent_dividedPowers
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.AbelianSchemeHomLiftingNilpotentDividedPowers
covers: 306
status: drafted
drafted_by: writer@claude
---
This theorem proves `AbelianLifting`: over a nilpotent divided power thickening, abelian schemes lift with any admissible Hodge filtration, and homomorphisms lift exactly when they respect the filtrations. It is the form of Grothendieck-Messing deformation theory that the proof uses. Its main user is `grothendieckDeformation_of_lifting`, which gives the input `grothendieck_deformation_of_literature` of the step [every character of the literature](/step/every-character-of-literature/), and so feeds [every character](/step/every-character/). The proof is one line. It calls [`abelianLifting_of_four`](/entry/abelian-lifting-of-four/) on four proved theorems.

## Statement

Let $R$ be a ring, $I \subset R$ an ideal with divided powers $\kappa$ that are nilpotent: some $N$ kills every product of divided powers of total degree at least $N$. Let $\pi \colon R \to R_0$ be surjective with kernel $I$. For an abelian scheme $A$ over $R$ write $H_{\mathrm{dR}}(A)$ for its de Rham module and $\mathrm{Fil}(A)$ for its Hodge filtration. If $A$ lifts $A_0$, there is a map $\mathrm{crys}_A \colon \mathrm{Crys}(A_0) \to H_{\mathrm{dR}}(A)$ from the crystalline module of $A_0$ on $(R, I, \kappa)$. Put $\mathrm{Fil}_A = \mathrm{crys}_A^{-1}(\mathrm{Fil}(A))$ (`liftFil`). A submodule $F \subset H_{\mathrm{dR}}(A)$ is admissible if it has a complement and reduces to $\mathrm{Fil}(A_0)$.

**Theorem.** For all such $R, I, \kappa, \pi$:

1. (Objects.) Let $A'$ be an abelian scheme of relative dimension $g$ over $R$ that lifts $A_0$, and let $F \subset H_{\mathrm{dR}}(A')$ be admissible. Then there is an abelian scheme $A$ of relative dimension $g$ over $R$ that lifts $A_0$, with $\mathrm{Fil}_A = \mathrm{crys}_{A'}^{-1}(F)$.
2. (Morphisms.) Let $A$ and $B$ be abelian schemes over $R$ that lift $A_0$ and $B_0$, and let $f_0 \colon A_0 \to B_0$ be a homomorphism whose crystalline map sends $\mathrm{Fil}_A$ into $\mathrm{Fil}_B$. Then there is exactly one homomorphism $f \colon A \to B$ that lifts $f_0$.

This is the theorem of Grothendieck and Messing (Messing, *The crystals associated to Barsotti-Tate groups*, LNM 264, 1972), for abelian schemes.

## Proof

The proof applies `abelianLifting_of_four` to:

- `abelianScheme_deRham_locallyFree_hodgeDegenerates`: the de Rham and Hodge structure of an abelian scheme;
- `dualAbelianScheme_exists_biduality`: the dual abelian scheme;
- `poincareDeRhamDuality_of_hodge`: the de Rham pairing with the dual is perfect, and the Hodge filtration is isotropic;
- `UnobTop.abelianUnobstructed`: abelian schemes lift over square-zero thickenings.

The real proof is in `abelianLifting_of_schemeLifts`, below [`abelianLifting_of_known_theorems`](/entry/abelian-lifting-of-known-theorems/).

## In the Lean code

The theorem is at [AbelianSchemeHomLiftingNilpotentDividedPowers.lean#L19](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/AbelianSchemeHomLiftingNilpotentDividedPowers.lean#L19). `AbelianLifting` is at [AbelianLifting.lean#L15](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/AbelianLifting.lean#L15). `LiftObj` and `LiftHom` are in [CanonicalOfAbelianDeRham.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/CanonicalOfAbelianDeRham.lean#L38), and `liftFil` in [IsKSValueOneOfRetraction.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsKSValueOneOfRetraction.lean#L649).

`AbelianLifting` has no prime $p$. The statement `GrothendieckMessing` in the same file as `LiftObj` asks that a prime $p$ be nilpotent in $R$, as Messing does. `AbelianLifting` drops this hypothesis, so it also covers rings in which no prime is nilpotent. We do not know a published source for that form. The object part gives existence only. Uniqueness of the lift up to isomorphism follows from the morphism part (`LiftHom.exists_iso_iff`, [CanonicalOfAbelianDeRham.lean#L95](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/CanonicalOfAbelianDeRham.lean#L95)).
