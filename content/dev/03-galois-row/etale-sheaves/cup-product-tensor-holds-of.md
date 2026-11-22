---
id: cup-product-tensor-holds-of
title: Associativity and uniqueness of the étale cup product, from the generators of the Tate twist
kind: theorem
decl: LateralTheory.Fix.CupProductTensor.holds_of
module: Development.EtaleCohomology.EtaleSheaves.TwPairExists
covers: 369
status: drafted
drafted_by: writer@claude
---
This theorem proves two facts about the cup product on étale cohomology with coefficients $\mathbb{Z}/q(i)$: it is associative, and it does not depend on the choice of the pairing of resolutions that defines it. Its hypothesis describes the sheaf $\mathbb{Z}/q(i)$ by local generators. Three one-line theorems apply it to the proof `twSec` of that hypothesis: the associative law $\mathrm{s39}$ and the existence of a pairing $\mathrm{s2}$ of [the ring laws](/entry/s41/), and the graded commutativity $\mathrm{s40}$ through `ringComm`. Below this theorem are 369 declarations.

## Statement

The spaces $E$ and the groups $H^n(E, \mathbb{Z}/q(i))$ are as in [the power-sum entry](/entry/s57/). In the Lean code, $\mathbb{Z}/q(i)$ is the étale sheafification of the presheaf $A \mapsto \mathbb{Z}/q[\mu_q^{\mathrm{prim}}(A)] / R$. Here $\mu_q^{\mathrm{prim}}(A)$ is the set of roots $\zeta$ of the $q$-th cyclotomic polynomial in $A$, with $q$ a unit in $A$. $R$ is spanned by $[\zeta^a] - a^i [\zeta]$ for $a \in (\mathbb{Z}/q)^\times$. Write $g_i(\zeta)$ for the class of $[\zeta]$.

A *pairing* $\mu \colon I \times J \to K$ of complexes of sheaves is a family of bilinear maps on sections in each bidegree, compatible with restriction, that satisfies the Leibniz rule with the sign $(-1)^s$. It gives a product on cohomology by the Alexander-Whitney formula. Let $I_i$ be the chosen injective resolution of $\mathbb{Z}/q(i)$. A pairing $I_i \times I_j \to I_k$ is *twisted* if in degree $0$ it sends $(g_i(\zeta), g_j(\zeta))$ to $g_k(\zeta)$. The cup product $a \cup b$ is defined by a chosen twisted pairing, or by $0$ if there is none.

**Theorem.** Suppose that, for all $q \geq 1$ and $i$: each section of $\mathbb{Z}/q(i)$ is étale locally $0$ or $c\, g_i(\zeta)$; for each $\zeta$, each section is étale locally a multiple of $g_i(\zeta)$; $c\, g_i(\zeta) = 0$ on a nonempty scheme only if $q \mid c$; $g_i$ commutes with restriction and $g_i(\zeta^a) = a^i g_i(\zeta)$; and maps $\mathbb{Z}/q(i) \to M$ correspond to families $e(\zeta)$ with these two laws. Then:

1. $(a \cup b) \cup c = a \cup (b \cup c)$ for all classes;
2. for all $i, j$ the chosen pairing $I_i \times I_j \to I_{i+j}$ is twisted, and if $i + j = k$, any two twisted pairings $I_i \times I_j \to I_k$ give the same cup product.

## Proof

1. The hypotheses give the map $\mathbb{Z}/q(i+j) \to \mathbb{Z}/q(i) \otimes \mathbb{Z}/q(j)$ that sends $g_{i+j}(\zeta)$ to $g_i(\zeta) \otimes g_j(\zeta)$. It is locally injective (`etale_tate_twist_generator_map_injective_of_sections_glue`) and locally surjective, so it is an isomorphism (`etale_tate_twist_generator_map_isIso_of_inj_surj`).
2. So the tensor product of a resolution of $\mathbb{Z}/q(i)$ and a flat resolution of $\mathbb{Z}/q(j)$ is a resolution of $\mathbb{Z}/q(i+j)$ with the right generator in degree $0$ (`etale_tensor_twisted_resolution_of_existence_bound_and_sides`).
3. From this and the universal property of the tensor complex (`tens_ex`, `tens_univ`), `etale_tate_twist_cup_pairing_of_tensor_and_resolution_properties` proves part 2.
4. `t_pair_assoc_of` proves that $(a \cup_{\mu_1} b) \cup_{\mu_2} c = a \cup_{\nu_2} (b \cup_{\nu_1} c)$ for any four twisted pairings. With the chosen pairings, `etale_twisted_cup_assoc_of_twisted_pairing_exists_assoc` gives part 1.

We have not unfolded the proofs of these lemmas.

## In the Lean code

The theorem is in [TwPairExists.lean](lean:Development/EtaleCohomology/EtaleSheaves/TwPairExists.lean#L67). The hypothesis is `EtaleTateTwistSectionsLocallyGenerated`. It is proved as `LeafAWCutTw.twSec` in [LeafAWCutTw.lean](lean:Development/EtaleCohomology/CohomologicalPurity/LeafAWCutTw.lean#L116), so every use of the theorem is unconditional. The objects are in [PullHlComp.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/PullHlComp.lean#L24): `Prim`, `tw`, `twGen`, `Pair`, `IsTwPair`, `twPair` and `cup`. The choices are made by `pick`, which returns $0$ when no object has the property.

Part 2 overlaps with $\mathrm{s12}$ (`LeafTwPairUnique_of`), a separate proof of the same uniqueness that [the unit law](/entry/s38/) uses. Many lemmas called here are named `intersectionNumber_baseChange`; none of them is about intersection numbers.
