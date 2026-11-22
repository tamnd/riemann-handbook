---
id: goal-holds
title: A small subrepresentation of a compact group from killing polynomials
kind: theorem
decl: LateralTheory.DivDb.goal_holds
module: Development.EtaleCohomology.DivisorCycles.GoalHolds
covers: 457
status: drafted
drafted_by: writer@claude
---
This theorem proves `DivWCoreLac`, the statement on compact groups that [divSet_holds](/entry/div-set-holds/) applies to $G_E$. The proof applies `goal_of` to thirteen lemmas. It is an assembly: the work is in those lemmas. Below it are 457 declarations.

## Statement

Let $\Gamma$ be a compact topological group. Let $K \subseteq K'$ be algebraically closed fields of characteristic $0$, with $K$ a Hausdorff topological field. Let $\rho \colon \Gamma \to \mathrm{GL}_N(K)$ be continuous and completely reducible. Let $S \subseteq \Gamma$ be dense, and for $s \in S$ let $P_s \in K[X]$ be monic of degree $n$ with $P_s(\rho(s)) = 0$. Let $X \in M_N(K')$ be in the Lie algebra of the Zariski closure of $\rho(\Gamma)$ (`InLieZar`), with $n$ distinct lacunary eigenvalues $e_1, \dots, e_n$ (`IsLac`, see the parent). Let $\psi \colon \Gamma \to K^\times$ be a continuous character with $\psi(s) = (-1)^n P_s(0)$ for $s \in S$.

**Theorem.** There is a continuous completely reducible $r \colon \Gamma \to \mathrm{GL}_n(K)$ such that:

1. $\rho(g) A = A r(g)$ for an $N \times n$ matrix $A$ of rank $n$;
2. $(r(g) \otimes 1_k) B = B \rho(g)$ for some $k$ and a matrix $B$ of rank $N$;
3. the characteristic polynomial of $r(g)$ kills $\rho(g)$ for each $g$, and $P_s(r(s)) = 0$ for $s \in S$;
4. $\det r = \psi$;
5. $r(g)$ has a separable characteristic polynomial on an open dense set;
6. for $s \in S$, the characteristic polynomial of $r(s)$ is $P_s$ if it is separable, or if $P_s$ satisfies `ProdGen` (separable, and no other multiset of $n$ roots has the same product).

## Proof

`goal_of` calls `plus_of`, which proves `DivPlus`. `DivPlus` has clauses 1 and 3 to 6 and, in place of clause 2, maps $T_j \colon \rho \to r$ and $T'_j \colon r \to \rho$ with $\sum_j T'_j T_j = 1$. `goal_of` stacks the $T_j$ into one matrix $B$. The stacked $T'_j$ form a left inverse of $B$, so $B$ has rank $N$.

`plus_of` uses the inputs in order. `SpecLie` moves $X$ and the $e_i$ from $K'$ down to $K$. `DegAll` extends the degree bound from $S$ to $\Gamma$ by continuity. `Struct`, `Key`, `BigCorner`, `Semis` and `MatrixUnits₂` build matrix units in an algebra that contains $\rho(\Gamma)$. `Rep` and `FinSub` give $r$ and $A$. `DenseAlg`, `FinDense` and `FinPoly` give clauses 4 to 6, and `FinEmbed` gives the $T_j, T'_j$. We have not opened the proofs of the thirteen inputs.

## In the Lean code

The theorem is in [GoalHolds.lean](lean:Development/EtaleCohomology/DivisorCycles/GoalHolds.lean#L19). See also [Imports.lean](lean:Development/EtaleCohomology/DivisorCycles/Imports.lean#L6) (`goal_of`), [DivPlus.lean](lean:Development/EtaleCohomology/DivisorCycles/DivPlus.lean#L37) (`plus_of`) and, for the input types, [CycleCount.lean](lean:Development/EtaleCohomology/DivisorCycles/CycleCount.lean#L28) and [OpenCoset.lean](lean:Development/EtaleCohomology/DivisorCycles/OpenCoset.lean#L90). `DivWCoreLac` is in [DivWCoreLacUseType.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/CocharacterLieDivisors/DivWCoreLacUseType.lean#L90).

The names are misleading. Each of the thirteen inputs is called `intersectionNumber_baseChange` (in `LateralTheory.Fin.SpecLie`, `LateralTheory.Fin.Key` and so on), an alias for a lemma such as `etale_spectrum_lie_algebra_instance` ([FinSpecLie.lean](lean:Development/EtaleCohomology/DivisorCycles/FinSpecLie.lean#L9)). The types are linear algebra and representation theory over a field, with no intersection numbers, base change or étale cohomology.
