---
id: class-number-finite-integral-level-closed-subgroup-gl
title: Finiteness of class numbers at integral level (second name)
kind: theorem
decl: GlobalTheory.T.classNumber_finite_integralLevel_closedSubgroupGL
module: Development.AbelianVarietyTheory.Proofs.AdelicLatticeProofs.ClassNumberFiniteIntegralLevelClosedSubgroupGLStatement
covers: 463
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the integral level case](/entry/class-finite-integral-level/), which has the real content. [The class number theorem](/entry/class-number-finite-holds/) calls it under this name.

## Statement

Let $F$ be a number field, $\mathbb{A}_f$ its ring of finite adeles, and $S$ a set of polynomials in the entries of an $n \times n$ matrix. For an $F$-algebra $B$, let $G(B)$ be the set of $g \in \mathrm{GL}_n(B)$ at which each $P \in S$ is zero. Suppose that $G(B)$ contains $1$ and is closed under products and inverses, for every $B$. Let $K$ be the set of $u \in G(\mathbb{A}_f)$ such that $u$ and $u^{-1}$ have entries in $\widehat{\mathcal{O}}_{F,v}$ at every place $v$. Then there is a finite set $T \subseteq G(\mathbb{A}_f)$ with

$$G(\mathbb{A}_f) = G(F) \cdot T \cdot K.$$

The statement writes the three group conditions out, and does not use `IsGroupLocus`.

## Proof

The proof is `exact @GlobalTheory.ClassFin.classFinite_integralLevel`, with two fallback tactics after `first`. The two statements are the same word for word.

## In the Lean code

The theorem is in [ClassNumberFiniteIntegralLevelClosedSubgroupGLStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/AdelicLatticeProofs/ClassNumberFiniteIntegralLevelClosedSubgroupGLStatement.lean#L8). The file sets `maxHeartbeats 1000000` for a proof that is one `exact`.
