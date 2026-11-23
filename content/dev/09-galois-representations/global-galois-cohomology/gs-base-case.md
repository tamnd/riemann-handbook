---
id: gs-base-case
title: The base case of Poitou-Tate duality at each prime power of N
kind: theorem
decl: GroundTheory.ProfCoh.gsBaseCase
module: GroundTheory.ProfiniteCohomology.PoitouTate.PoitouTateNineTermGs
covers: 501
status: drafted
drafted_by: writer@claude
---
This theorem applies [the duality axioms for one prime power](/entry/exists-compact-duality-hypotheses-gs/) to each prime power that exactly divides $N$. The proof only chooses the arguments. The result goes to `gsPoitouTateDualityHypotheses`, which glues the prime powers. That gives Poitou-Tate duality, the nine-term sequence and Sha for $G_S$, used by the [real-place version](/entry/gs-tate-poitou-tate-hypotheses/) and by a count of $H^2$ in `PoitouTateH2Nat`. Through them it lies below [EveryCharacter from Row0b](/step/every-character-of-row/).

## Statement

Let $K$, $S$ (finite) and $G_S$ be as in [the Poitou-Tate package](/entry/gs-tate-poitou-tate-hypotheses/). Let $N \geq 1$, with each prime above $N$ in $S$, and suppose that $N$ is odd or $K$ is totally complex. For $n \mid N$ let $t_n \colon H^3_c(G_S, \mu_n) \to \mathbb{Z}/n$ be `gsCompactInv`, with compact support at the finite places of $S$ only.

**Theorem.** For each prime $p \mid N$, with $n = p^{v_p(N)}$, there is an open subgroup $U_0$ of $G_S$ such that `CompactDualityHypotheses` holds for $(G_S, n, \mu_n, t_n, U_0)$.

## Proof

Apply [`exists_compactDualityHypotheses_gs`](/entry/exists-compact-duality-hypotheses-gs/) with $\ell = p$ and $k = v_p(N)$. The primes above $p$ lie in $S$ because $p \mid N$ (`mem_of_natCast_dvd_mem`). The rest is bookkeeping.

## In the Lean code

The theorem is in [PoitouTateNineTermGs.lean](lean:GroundTheory/ProfiniteCohomology/PoitouTate/PoitouTateNineTermGs.lean#L23). It is a pass-through; the content is in the [pairing input](/entry/gs-pairing-input/). `gsPoitouTateDualityHypotheses`, in [ZmodToQZCompactCohomologyResMapOfLocalInv.lean](lean:GroundTheory/ProfiniteCohomology/PoitouTate/ZmodToQZCompactCohomologyResMapOfLocalInv.lean#L207), takes this statement as its hypothesis `H`. The file omits `[NeZero N]`: for $N = 0$ there are no prime factors and the statement holds trivially.
