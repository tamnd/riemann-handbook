---
id: gs-tate-poitou-tate-hypotheses
title: The Poitou-Tate package for the Galois group unramified outside S, with real places
kind: theorem
decl: GroundTheory.ProfCoh.gsTatePoitouTateHypotheses
module: GroundTheory.ProfiniteCohomology.PoitouTate.NonemptyOfNatCastMemOfNeOne
covers: 336
status: drafted
drafted_by: writer@claude
---
This theorem checks that the Galois group $G_S$ of a number field, unramified outside a finite set $S$, satisfies a list of duality axioms in which the real places enter through Tate cohomology. The proof splits into $N$ even and $N$ odd and calls one theorem for each case. In the proof, its result goes to [injectivity of restriction to the real places in degree 3](/entry/injective-gs-real-res-three/).

## Statement

Let $K \subset \overline{\mathbb{Q}}$ be a number field and $S$ a finite, nonempty set of finite places of $K$. Let $K_S$ be the union of the finite extensions of $K$ in $\overline{\mathbb{Q}}$ unramified outside $S$, and $G_S = \mathrm{Gal}(K_S/K)$. Fixed embeddings give maps $G_{K_v} \to G_S$ for $v \in S$ and for $v$ real. Let $N \geq 1$, with each prime above $N$ in $S$, and let $\mu_N \subset K_S$ be the $N$-th roots of unity.

Write $H^r_c(G_S, M)$ for the cohomology of the cone of restriction to the local groups, where at each real place the norm map is added, so that Tate cohomology appears there. Let $t \colon H^3_c(G_S, \mu_N) \to \mathbb{Z}/N$ be `gsTrace`.

**Theorem.** `TatePoitouTateHypotheses` holds for these data. For finite discrete $G_S$-modules $M$ killed by $N$, with $M' = \mathrm{Hom}(M, \mu_N)$, its fields say:

- $\mu_N \cong \mathbb{Z}/N$;
- for $r + s = 3$ and $s \geq 1$, cup product and $t$ give a bijection $H^r(G_S, M) \to \mathrm{Hom}(H^s_c(G_S, M'), \mathbb{Z}/N)$;
- $H^r(G_S, M)$ is finite for $r \leq 2$;
- $t$, composed with the map from local $H^2$ to $H^3_c$, is the sum of the local invariants at $v \in S$ and at the real places;
- $H^0(G_S, M)$ injects into $\prod_{v \in S} H^0(K_v, M)$;
- the local pairings in degrees 0 and 2 are surjective onto the duals (at real places in degree 2, onto the characters that kill the norm classes).

## Proof

If $N$ is even, `gsEvenTatePoitouTateHypotheses` gives the result. If $N$ is odd, `gsOddTatePoitouTateHypotheses` gives it for another trace, `gsOddTrace`: the trace `gsCompactInv` without real places, after the map that forgets them. Its duality field comes from `poitouTate_duality_gs`, which rests on the [base case](/entry/gs-base-case/). The lemma `gsTrace_eq_gsOddTrace` shows that the two traces are equal: both satisfy the formula with local invariants, and the map from local $H^2$ to $H^3_c$ is surjective.

## In the Lean code

The theorem is in [NonemptyOfNatCastMemOfNeOne.lean](lean:GroundTheory/ProfiniteCohomology/PoitouTate/NonemptyOfNatCastMemOfNeOne.lean#L57), with `gsTrace_eq_gsOddTrace` at [line 40](lean:GroundTheory/ProfiniteCohomology/PoitouTate/NonemptyOfNatCastMemOfNeOne.lean#L40).

- `TatePoitouTateHypotheses`: [RealAbstract.lean](lean:GroundTheory/ProfiniteCohomology/PoitouTate/RealAbstract.lean#L51).
- `gsEvenTatePoitouTateHypotheses`: [RealEvenHyp.lean](lean:GroundTheory/ProfiniteCohomology/PoitouTate/RealEvenHyp.lean#L92). We have not opened its duality lemma.
- `gsOddTatePoitouTateHypotheses`: [RealOdd.lean](lean:GroundTheory/ProfiniteCohomology/PoitouTate/RealOdd.lean#L204).

The map `gsTrace` in [RealTraceMap.lean](lean:GroundTheory/ProfiniteCohomology/PoitouTate/RealTraceMap.lean#L42) is a `Classical.choose`: some map whose composite with the local map is the sum of invariants. The odd case shows that the choice does not matter there. The nonemptiness of $S$ is the `[Nonempty S]` of the file; the odd case needs it, since no prime divides $N = 1$.
