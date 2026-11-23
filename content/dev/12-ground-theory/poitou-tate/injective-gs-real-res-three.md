---
id: injective-gs-real-res-three
title: Restriction to the real places is injective in degree three
kind: theorem
decl: GroundTheory.ProfCoh.injective_gsRealRes_three
module: GroundTheory.ProfiniteCohomology.PoitouTate.NonemptyOfNatCastMemOfNeOne
covers: 340
status: drafted
drafted_by: writer@claude
---
This lemma is the case $r = 3$ of the injectivity in [Restriction to the real places is bijective in degrees three and up](/entry/bijective-gs-real-res/). It is the one case of that theorem that uses Poitou-Tate duality. That entry has the setting; we keep its names: $K$, $S$, `ιr`, `ιs`, $N$ and $M$ with $N M = 0$. The result is used by [The Euler ratio is one, from its coprime case](/entry/ratio-one-of-lemma-x/) through its parent.

## Statement

**Theorem.** The restriction map
$$H^3(G_{K,S}, M) \to \prod_{v \text{ real}} H^3(K_v, M)$$
(`gsRealRes S ιr M 3`) is injective.

## Proof

Let $x \in H^3(G_{K,S}, M)$ map to $0$ at every real place.

1. **The finite places give nothing.** For $v \in S$, the group $H^3(K_v, M)$ has one element (`subsingleton_cohomology_gsFinFamily_of_three_le`). So $x$ maps to $0$ under the full map `ptTGlobalToLocal` to the finite and real places.
2. **The full map is injective in degree 3.** This is the field `injective_ptTGlobalToLocal_three` of the bundle [`gsTatePoitouTateHypotheses`](/entry/gs-tate-poitou-tate-hypotheses/). Its proof in `RealAbstract.lean` uses the Poitou-Tate sequence
   $$\prod_v H^2(K_v, M) \to H^3_c(G_{K,S}, M) \to H^3(G_{K,S}, M) \to \prod_v H^3(K_v, M).$$
   Exactness at $H^3(G_{K,S}, M)$ writes $x$ as the image of some $z \in H^3_c$. Duality shows that the first map is onto (`surjective_ptTLocalToCompact_two`, from the bijective compact dual map in degree 3 and the surjective local dual map in degree 2). So $z$ comes from local $H^2$, and exactness at $H^3_c$ gives $x = 0$.

## In the Lean code

The theorem is at [NonemptyOfNatCastMemOfNeOne.lean](lean:GroundTheory/ProfiniteCohomology/PoitouTate/NonemptyOfNatCastMemOfNeOne.lean#L131). The abstract argument is in [RealAbstract.lean](lean:GroundTheory/ProfiniteCohomology/PoitouTate/RealAbstract.lean#L336), and the local vanishing is in [VanishingPrimes.lean](lean:GroundTheory/ProfiniteCohomology/RealPlaces/VanishingPrimes.lean#L27).

- The statement does not mention `ιs`, but `include ιs hS hM` makes it an explicit argument. The proof needs it to build `gsFinFamily S ιs`. The sibling lemmas for $r \ge 4$ choose such embeddings with `Classical.choice`, and this lemma could do the same.
