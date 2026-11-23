---
id: exists-split
title: A split point with fixed integer bounds where a Fourier-Jacobi coefficient is nonzero
kind: theorem
decl: GlobalTheory.ArcDetect.exists_split
module: Development.AbelianVarietyTheory.Proofs.ThetaShiftProofs.ExistsFamilyMemberFunctionalNeZero
covers: 650
status: drafted
drafted_by: writer@claude
---
This theorem is an adapter. It takes the split point of [the nonzero coefficient at a split point](/entry/exists-fj-ne-zero-at-split-point-prime/) and states it with the fixed constants `nQ` and `LaQ` of the CM family. The real content is in that entry. Its only user is step 1 of [the CM arc datum that sees a coefficient](/entry/exists-fam-cf-of-ne-zero/).

## Statement

Let $X$ be lattice data (`DataX`) over $X_0$, of rank $r$, with signature index $q$ and level $g$. Let $\lambda$ be a dominant weight, $c_1 > 0$ and $w \ge 1$ with $\sum_\tau \mathrm{spread}(\lambda, \tau) \le w$ and $r \le w$. Suppose that the character $\chi_\lambda$ is trivial on all of $\Gamma$. Let $P$ be a cusp form in $\mathrm{SS}(\lambda)$ that is not in $\mathrm{SS}_{>c_1}(\lambda)$.

**Theorem.** There are an isotropic $\xi$, exponents $\nu$ with $\sum_\tau \nu_\tau \le c_1$, a point $x$ of the domain and vectors $v_1, \dots, v_{r-2}$ of $E^r$ such that:

1. `SplitData` holds at $(\xi, x, v)$ with the bound `LaQ E r q g NA NC c₁ w`;
2. for each $\mu \in \Lambda_p(\xi)$ there is $e \in E$ with $e\xi \in \Lambda$ and $\mathrm{nQ} \cdot \mathrm{aproj}_x(\xi, \mu) = e\xi$;
3. $\mathrm{fj}_{\lambda, \xi, \nu}(P)(x) \neq 0$.

## Proof

The proof calls [`exists_fj_ne_zero_at_split_point'`](/entry/exists-fj-ne-zero-at-split-point-prime/). That theorem gives the point for every integer $n' \ge 1000\, m_s / r_h$. The proof takes $n' = \mathrm{nQ}$, which is the ceiling of $1000\, m_s / r_h$ plus one. The bound $L_a$ on the norms of the $v_j$ becomes the weaker bound $\mathrm{LaQ} = \max(1, L_a)$. The proof drops the facts $\nu \ge 0$ and `ShortVectorHypotheses`.

## In the Lean code

The theorem is in [ExistsFamilyMemberFunctionalNeZero.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/ExistsFamilyMemberFunctionalNeZero.lean#L139). `nQ` and `LaQ` are in [ModelsAt.lean](lean:Development/AbelianVarietyTheory/Definitions/ArchimedeanThetaValues/ModelsAt.lean#L190).

- The hypotheses $p_0 = q$ and $g_X = g$ are only names for the same numbers. The proof substitutes them at once.
- The hypothesis on $\chi_\lambda$ is stronger than the callee needs. The callee asks for $\chi_\lambda(\gamma) = 1$ only when $\gamma v - v \in g\Lambda$ for all $v \in \Lambda$.
- The clauses of `SplitData` are spelled out in [the next entry](/entry/exists-fj-ne-zero-at-split-point-prime/). We have not unfolded `Λp` or `aproj`.
