---
id: b-odd
title: A rank bound for the homology of GL_n over a ring of integers, under a new name
kind: theorem
decl: UpperTheory.V.ZK.bOdd
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ClassCounting.BOdd
covers: 1788
status: drafted
drafted_by: writer@claude
---
This theorem is a new name for [`bOdd_zk`](/entry/b-odd-zk/), which holds all of its content. It is the input `BOdd` of [the bound on $H^2$](/entry/lemma-k-lit-n-alt/), and it is the largest part of that proof (1,788 of 2,836 declarations).

## Statement

For a commutative ring $R$ and $d, n \ge 1$, let $\psi_d \colon \mathrm{GL}_n(R) \to \mathrm{GL}_{dn}(R)$ be the block diagonal map $A \mapsto 1_d \otimes A$, and let $\iota \colon \mathrm{GL}_n(R) \to \mathrm{GL}_{dn}(R)$ be the inclusion $A \mapsto \mathrm{diag}(A, 1)$. Fix $l \ge 1$. For a class $x \in H_m(\mathrm{GL}_n(R))$ define $z_0(x) = x$ and
$$z_{t+1}(x) = (\psi_l)_* z_t(x) - l^{t+2}\, \iota_* z_t(x) \in H_m(\mathrm{GL}_{l^{t+1} n}(R)).$$
Here $H_m$ is group homology with coefficients in the trivial module $\mathbb{Z}$.

`BOdd` says: let $L$ be a totally complex number field with $r_2$ complex places. Let $k$ be even with $k + 1 < r_2$, let $l \ge 1$, and let $n \ge 2(k+1) + 4$. Then the classes $z_k(x)$, for $x \in H_{k+1}(\mathrm{GL}_n(\mathcal{O}_L))$, span a $\mathbb{Z}$-module of rank at most $r_2$.

**Theorem.** `BOdd` holds.

## Proof

The proof is the term `PositivityTheory.KB.bOdd_zk`. That theorem takes the bound [`bStarOdd`](/entry/b-star-odd/), which is stated for a copy of `zSeq` in the namespace `PositivityTheory.KB`, and moves it over with the lemmas `lev_zk`, `zSeq_zk` and `rank_heq`.

## In the Lean code

- The theorem is in [BOdd.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ClassCounting/BOdd.lean#L3), a file of three lines. `BOdd` is in [LemmaKOfSteps.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ClassCounting/LemmaKOfSteps.lean#L11), and $\psi_d$ and $z_t$ (`psi`, `zSeq`) are in [HasVal.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ClassCounting/HasVal.lean#L45).
- `bOdd_zk` is in [Bridge.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/KTheoryStability/ReductionBoundsTorsion/TorsionIntegers/Bridge.lean#L34).
- The hypothesis on $l$ is only $l > 0$; it need not be a prime.
