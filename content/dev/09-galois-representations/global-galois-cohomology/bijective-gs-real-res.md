---
id: bijective-gs-real-res
title: Restriction to the real places is bijective in degrees three and up
kind: theorem
decl: GroundTheory.ProfCoh.bijective_gsRealRes
module: GroundTheory.ProfiniteCohomology.PoitouTate.NonemptyOfNatCastMemOfNeOne
covers: 675
status: drafted
drafted_by: writer@claude
---
This theorem says that in degrees $r \ge 3$, the cohomology of $G_{K,S}$ is the sum of the cohomology at the real places. [The Euler ratio is one, from its coprime case](/entry/ratio-one-of-lemma-x/) uses it with $r = 3$, in the step where `gsEulerRatio` is multiplicative in short exact sequences.

## Statement

Let $K$ be a number field, $S$ a finite nonempty set of finite places of $K$, and $G_{K,S}$ the Galois group of the maximal extension of $K$ in $\overline{\mathbb{Q}}$ unramified outside $S$. Fix embeddings `ιr` at the real places and `ιs` at the places in $S$. Let $N > 0$ with every place above $N$ in $S$, and let $M$ be a finite discrete $G_{K,S}$-module with $N M = 0$.

**Theorem.** For $r \ge 3$, the restriction map
$$H^r(G_{K,S}, M) \to \prod_{v \text{ real}} H^r(K_v, M)$$
(`gsRealRes S ιr M r`) is bijective.

This is part (c) of the Poitou-Tate theorem in J. S. Milne, *Arithmetic Duality Theorems*, Theorem I.4.10.

## Proof

Surjectivity for all $r \ge 3$ is `surjective_gsRealRes_of_three_le`. Injectivity has two cases.

- $r = 3$: [`injective_gsRealRes_three`](/entry/injective-gs-real-res-three/). This case uses the Poitou-Tate sequence.
- $r \ge 4$: `injective_gsRealRes_of_four_le`. Compactly supported cohomology vanishes in degrees $\ge 4$ (`gsTateCompactCohomology_eq_zero`), and the finite places have no cohomology in degrees $\ge 3$.

So the theorem is a case split. The new content is in the $r = 3$ case.

## In the Lean code

The theorem is at [NonemptyOfNatCastMemOfNeOne.lean](lean:GroundTheory/ProfiniteCohomology/PoitouTate/NonemptyOfNatCastMemOfNeOne.lean#L142). The two lemmas for surjectivity and for $r \ge 4$ are in [Vanishing.lean](lean:GroundTheory/ProfiniteCohomology/RealPlaces/Vanishing.lean#L39). `gsRealRes` is in [GSDefs.lean](lean:GroundTheory/ProfiniteCohomology/RealPlaces/GSDefs.lean#L37).

- The statement does not mention `ιs`, but the theorem takes it as an explicit argument (`include ιs hS hM`). Only the case $r = 3$ needs it, through `gsTatePoitouTateHypotheses`. The two lemmas in `Vanishing.lean` choose their own embeddings.
- `bijective_gsRealRes_of_odd` in [RealOddMain.lean](lean:GroundTheory/ProfiniteCohomology/PoitouTate/RealOddMain.lean#L83) has the same proof for odd $N$.
- The users `ratio_shortExact_l` and `ratio_shortExact_prime` need only $r = 3$. `gsEulerRatio_shortExact_of_bijective` takes bijectivity for two modules of the sequence.
