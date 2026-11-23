---
id: exists-compact-duality-hypotheses-gs
title: The duality axioms for one prime power, for the Galois group unramified outside S
kind: theorem
decl: GroundTheory.ProfCoh.exists_compactDualityHypotheses_gs
module: GroundTheory.ProfiniteCohomology.RestrictedRamification.BaseMain
covers: 500
status: drafted
drafted_by: writer@claude
---
This theorem gives, for $n$ a power of a prime $\ell$, an open subgroup $U_0$ of $G_S$ below which the cup product pairing of $\mathbb{Z}/n$ with $\mu_n$ is perfect. The [base case](/entry/gs-base-case/) applies it to each prime power that exactly divides $N$. The proof passes the [pairing input](/entry/gs-pairing-input/) to `exists_compactDualityHypotheses_gs_of_pairing`.

## Statement

Let $K$, $S$ (finite) and $G_S$ be as in [the Poitou-Tate package](/entry/gs-tate-poitou-tate-hypotheses/). Let $n = \ell^k \geq 1$ with $\ell$ prime. Suppose that the primes above $\ell$ are in $S$, that $n$ is odd or $K$ is totally complex, and that $H^3(G_S, \mu_n) = 0$. Write $H^r_c$ for cohomology with compact support at the finite places of $S$. Let $t \colon H^3_c(G_S, \mu_n) \to \mathbb{Z}/n$ be `gsCompactInv`: the map induced by $\sum_{v \in S} \mathrm{inv}_v$ along the surjection $\bigoplus_{v \in S} H^2(K_v, \mu_n) \to H^3_c(G_S, \mu_n)$.

**Theorem.** There is an open $U_0 \leq G_S$ such that `CompactDualityHypotheses` holds for $(G_S, n, \mu_n, t, U_0)$:

1. $\mu_n \cong \mathbb{Z}/n$;
2. $H^4_c(G_S, M) = 0$ for each finite discrete $G_S$-module $M$ killed by $n$;
3. for each open $U \leq U_0$ and $r + s = 3$, the map $H^r(U, \mathbb{Z}/n) \to \mathrm{Hom}(H^s_c(U, \mu_n), \mathbb{Z}/n)$, $x \mapsto (y \mapsto t(\mathrm{cor}(y \cup x)))$, is bijective. Here $H^s_c(U, \cdot)$ uses the local groups `mackeyFamily`, which we have not unfolded.

## Proof

The proof is `exists_compactDualityHypotheses_gs_of_pairing` applied to [`gsPairingInput`](/entry/gs-pairing-input/). That lemma takes for $U_0$ an open subgroup that fixes $\mu_n$ (`exists_openSubgroup_fixing_rootsOfUnity`). Fields 1 and 2 are `nonempty_addEquiv_gsRoots_of_places` and `subsingleton_compactCohomology_four`. For field 3, it writes $U$ as the subgroup that fixes a finite extension $L$ of $K$ in $K_S$ (`exists_gsOpenSubgroup_eq`), uses that corestriction on $H^3_c$ is surjective (`surjective_gs_compactCores_three`), and calls `gsBaseBijective_of_le` with the pairing input. We have not opened `gsBaseBijective_of_le`.

## In the Lean code

The theorem and `exists_compactDualityHypotheses_gs_of_pairing` are in [BaseMain.lean](lean:GroundTheory/ProfiniteCohomology/RestrictedRamification/BaseMain.lean#L61). `CompactDualityHypotheses` is in [IsDiscreteRepResHomCoindRes.lean](lean:GroundTheory/ProfiniteCohomology/PoincarePairs/IsDiscreteRepResHomCoindRes.lean#L134), and `gsCompactInv` in [BaseDefs.lean](lean:GroundTheory/ProfiniteCohomology/RestrictedRamification/BaseDefs.lean#L307). The theorem is a pass-through. The hypothesis $H^3(G_S, \mu_n) = 0$ enters the statement only through $t$: it makes the local map onto $H^3_c$ surjective.
