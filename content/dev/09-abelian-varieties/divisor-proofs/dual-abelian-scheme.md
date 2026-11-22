---
id: dual-abelian-scheme
title: The dual abelian scheme exists, with biduality
kind: theorem
decl: GlobalTheory.dualAbelianScheme
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.DualAbelianSchemeExistsBiduality
covers: 1038
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement `DualAbelianScheme`: each abelian scheme has a dual abelian scheme with a Poincaré bundle, and the swapped bundle makes the first scheme the dual of the second. Twelve declarations use it directly. One of them is `dual_abelian_scheme_of_open`, the input of the field `dual` in [the CM and abelian variety inputs](/step/cm-abelian-inputs-from-literature/). Its users meet only at [EveryCharacter](/step/every-character/). The proof is a short assembly of two lemmas.

## Statement

Let $S$ be a scheme. An *abelian scheme* over $S$ is a commutative group object $A \to S$ that is smooth, proper and geometrically connected (`IsAbelianScheme`). A line bundle on a scheme $X$ is given here as Čech data (`LB X`): an open cover $(U_i)$ and units $g_{ij}$ on $U_i \cap U_j$, which form a line bundle when they satisfy the cocycle conditions (`IsLB`). A bundle $M$ on $A \times_S T$ is *additive* if $M_{(a a', t)} \cong M_{(a,t)} \otimes M_{(a',t)}$ for all points $a, a'$ of $A$ and $t$ of $T$ with values in any $Y$. A bundle $P$ on $A \times_S B$ makes $B$ *the dual of $A$* (`IsDual A B P`) if $P$ is an additive line bundle, $P$ is trivial on $A \times \{0\}$, and for each $S$-scheme $T$ and each additive line bundle $M$ on $A \times_S T$ there is exactly one $x \colon T \to B$ with $M \cong (1 \times x)^* P$.

**Theorem.** Let $A$ be an abelian scheme over $S$. Then there are an abelian scheme $B$ over $S$ and a bundle $P$ on $A \times_S B$ such that:

1. if $A \to S$ is smooth of relative dimension $g$, then so is $B \to S$;
2. $P$ makes $B$ the dual of $A$;
3. the swapped bundle $s^* P$ on $B \times_S A$ makes $A$ the dual of $B$.

Part 2 says that $B$ represents the functor of line bundles on $A \times_S T$ that are additive in the first variable. Part 3 is biduality. The statement asks for a scheme $B$ over every base scheme $S$, with no noetherian or projectivity hypothesis. In the literature, the dual of an abelian scheme over a general base is known to exist as an algebraic space, and as a scheme under extra hypotheses, for example when $A$ is projective over a noetherian base $S$. So the Lean statement may ask for more than the standard results give.

## Proof

1. `exists_dual_abelianScheme_poincare` gives $B$, $P$, part 2, and `DimLe A B`: for each $T \to S$, if $A_T \to T$ is smooth of relative dimension $g$, so is $B_T \to T$.
2. `isDualAbelianSchemePoincare_swap` gives part 3 from part 2 and `DimLe A B`.
3. For part 1, apply `DimLe A B` with $T = S$ and the identity map. The two lemmas of the same file, `smoothOfRelDim_pullback_snd_identity` and `smoothOfRelDim_of_pullback_snd_identity`, move smoothness between $A \to S$ and its base change along $\mathrm{id}_S$. The rest is bookkeeping.

## In the Lean code

The theorem is at [DualAbelianSchemeExistsBiduality.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/DualAbelianSchemeExistsBiduality.lean#L29). The statement is at [ExistsCrystalPairing.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/ExistsCrystalPairing.lean#L25). `IsDual` and `IsAdditive` are in [IsAdditiveOfUniversal.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/IsAdditiveOfUniversal.lean#L73), and `DimLe` is in [SameIdIff.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/SameIdIff.lean#L36).

- The two lemmas from `GlobalTheory.T` are one-line wrappers. The work is in [`DualExist.exists_dual`](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsDualAbelianSchemePoincare.lean#L63), which builds $B$ over affine opens of $S$ (`abelianScheme_dual_representable_affine_base`) and glues, and in [`BidualAbelian.isDual_swap`](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsDualAbelianSchemePoincareSwap.lean#L94), which takes the dual $C$ of $B$ and the classifying map $\kappa \colon A \to C$ of $s^* P$, shows that $\kappa$ is a homomorphism (`isMonHom_of_classifying`) and an isomorphism on geometric fibres (`fibre_isIso`), and so an isomorphism. We have not read the proofs of these lemmas.
- `IsDual` does not ask $M$ to be trivial on $\{0\} \times T$; additivity gives that.
- The statement does not say that $B$ is unique.
