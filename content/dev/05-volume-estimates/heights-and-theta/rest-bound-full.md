---
id: rest-bound-full
title: The bound on the rest terms, summed over primes
kind: theorem
decl: GroundTheory.Heights₂.Heights.RestTerms.RestBound.full
module: GroundTheory.HeightsAndTheta.Heights.RemainderTerms.Imports
covers: 625
status: drafted
drafted_by: writer@claude
---
This theorem bounds the sum over primes $p > B_0$ of the rest terms. Its proof joins the bound for one prime, [`RestPrimeBound.full`](/entry/rest-prime-bound-full/), with a summation lemma. Its one user is [`finite_bound`](/entry/finite-bound/), which moves it to real polynomials through `RestBound.imp` and uses it for a finite set of primes.

## Statement

We use the notation of [the entry for one prime](/entry/rest-prime-bound-full/): $N = r + a$, the polynomial $F_c$, the number $D_c$, the constant $X$ and the prime term $M(p)$.

**Theorem.** Let $f, r, a \ge 1$, let $c$ be one of the two small blocks, and let $4 f N^2 \le B_0$. Then $F_c$ has a power sum decomposition $Q$. For each such $Q$, all choices $s$, all signs $e = \pm 1$, and each set $P$ of natural numbers, the family $|M(p)|$, for $p \in P$ prime with $p > B_0$, is summable, and
$$\Bigl|\sum_{p \in P,\ p > B_0} M(p)\Bigr| \le 1.6\,(fra + 1)\,|D_c|.$$

## Proof

The proof term is `RestBound.proof RestPrimeBound.full RestBoundOfPrimeBound.full`. `RestBound.proof` takes the decomposition $Q$ and the bound $|M(p)| \le 1.5\, f X C \log p / p^2$, with $C = (fra+1)|D_c|$, from [`RestPrimeBound.full`](/entry/rest-prime-bound-full/). It gives that bound to `RestBoundOfPrimeBound.proof`, which sums it. The sum uses `prime_partial_le`, $\sum_{B_0 < p < K} \log p / p^2 \le 2 \log 4 / B_0$ for all $K$. That lemma comes from Chebyshev's bound $\sum_{p < K} \log p \le K \log 4$ (Hardy and Wright, An Introduction to the Theory of Numbers, §22.2) and partial summation. Then $X \le \tfrac32 N^2$, $2 \log 4 \le 2.78$ and $1.5 f \cdot \tfrac32 N^2 \cdot 2.78 / (4 f N^2) \le 1.6$ give the constant. The hard part, the bound on single rest terms by characters of the symmetric group, is in the entry for one prime.

## In the Lean code

The theorem is in [Imports.lean](lean:GroundTheory/HeightsAndTheta/Heights/RemainderTerms/Imports.lean#L572). The statement is at [Statements.lean](lean:GroundTheory/HeightsAndTheta/Heights/RemainderTerms/Statements.lean#L332), the assembly at [PRestBound.lean](lean:GroundTheory/HeightsAndTheta/Heights/RemainderTerms/PRestBound.lean#L10) and the summation at [PRestBoundOfPrimeBound.lean](lean:GroundTheory/HeightsAndTheta/Heights/RemainderTerms/PRestBoundOfPrimeBound.lean#L15). A second statement with this name, over $\mathbb{R}$ with a general flag integral, is in [IsFlagIntegralOne.lean](lean:GroundTheory/HeightsAndTheta/Heights/RemainderTerms/IsFlagIntegralOne.lean#L268); `RestBound.imp` at [RestAt.lean](lean:GroundTheory/HeightsAndTheta/Heights/RemainderTerms/RestAt.lean#L120) derives it from this one.
