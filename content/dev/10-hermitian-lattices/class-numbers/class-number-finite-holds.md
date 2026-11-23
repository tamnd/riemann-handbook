---
id: class-number-finite-holds
title: Finiteness of class numbers for linear groups over a number field
kind: theorem
decl: GlobalTheory.classNumberFinite_holds
module: Development.AbelianVarietyTheory.Proofs.AdelicLatticeProofs.ClassNumberFiniteHolds
covers: 470
status: drafted
drafted_by: writer@claude
---
This theorem proves the finiteness of class numbers for a linear algebraic group over a number field, with any open level subgroup. [The geometric realization in weight one](/entry/geometric-realization-of-weight-one/) depends on it through two users. Both count classes for the centraliser torus of a similitude group: `ccf_holds` and `classes_finite_of_locus`. This theorem only reduces the level. The main work is in [the integral level case](/entry/class-number-finite-integral-level-closed-subgroup-gl/).

## Statement

Let $F$ be a number field, $\mathbb{A}_f$ its ring of finite adeles, and $S$ a set of polynomials in the entries of an $n \times n$ matrix. For an $F$-algebra $R$, let $G(R)$ be the set of $g \in \mathrm{GL}_n(R)$ at which each $P \in S$ is zero. Suppose that $G(R)$ is a subgroup for every $R$ (`IsGroupLocus S`). Let $U$ be an open subgroup of $G(\mathbb{A}_f)$ that is also compact. Then there is a finite set $T \subseteq G(\mathbb{A}_f)$ with

$$G(\mathbb{A}_f) = G(F) \cdot T \cdot U.$$

This is `ClassNumberFinite`. It is the finiteness of class numbers of Borel (Some finiteness properties of adele groups over number fields, Publ. Math. IHÉS 16 (1963), Theorem 5.1). Borel works over $\mathbb{Q}$; the Lean proof also goes to $\mathbb{Q}$, by restriction of scalars, in [the integral level case](/entry/class-finite-integral-level/).

## Proof

Let $K \subseteq G(\mathbb{A}_f)$ be the set of $u$ such that $u$ and $u^{-1}$ have entries in $\widehat{\mathcal{O}}_{F,v}$ at every place $v$.

1. The integral level case gives a finite $T_0$ with $G(\mathbb{A}_f) = G(F) \cdot T_0 \cdot K$.
2. $K$ is compact (`T.isCompact_integralPoints_finiteAdelic_algebraicGroup`).
3. A compact set meets only finitely many left cosets of an open subgroup (`T.compact_meets_finitely_many_leftCosets_open`). So $K \subseteq T_1 U$ for a finite $T_1$.
4. Let $T = \{ s t : s \in T_0, t \in T_1 \}$. If $x = \gamma s k$ and $k = t u$, then $x = \gamma (s t) u$.

We have not unfolded the proofs of the lemmas in steps 2 and 3.

## In the Lean code

The theorem is in [ClassNumberFiniteHolds.lean](lean:Development/AbelianVarietyTheory/Proofs/AdelicLatticeProofs/ClassNumberFiniteHolds.lean#L11). `ClassNumberFinite`, `IsGroupLocus` and `locusSubgroup` are in [ClassNumberFinite.lean](lean:Formalism/UnipotentAdelicQuotients/ClassNumberFinite.lean#L23). The topology on $G(\mathbb{A}_f)$ is the subspace topology that Lean gives to the subgroup; we have not unfolded it.

The predicate asks for a compact $U$, but the proof does not use the compactness (`intro F _ _ n S hS U hUo _` at line 13). An open subgroup is sufficient.
