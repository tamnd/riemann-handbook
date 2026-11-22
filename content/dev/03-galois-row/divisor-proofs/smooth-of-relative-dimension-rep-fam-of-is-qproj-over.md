---
id: smooth-of-relative-dimension-rep-fam-of-is-qproj-over
title: A quasi-projective Harris-Taylor moduli scheme is smooth of the expected dimension
kind: theorem
decl: GlobalTheory.T.smoothOfRelativeDimension_repFam_of_isQProjOver
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.SmoothOfRelativeDimensionStatement
covers: 461
status: drafted
drafted_by: writer@claude
---
This theorem is the statement form of [the smoothness of the moduli scheme](/entry/smooth-of-relative-dimension/). It is a second name of that theorem, with the same statement. [The integral model entry](/entry/model-nonempty/) uses it to add smoothness to the quasi-projective representing family.

## Statement

Use the datum $D$ for a prime $p$, the base $b$ over a ring $R$, and the objects of level $N$ of [the integral model entry](/entry/model-nonempty/). A *representing family* of level $N$ (`RepFam b N`) is a scheme $X$ with $s \colon X \to \operatorname{Spec} R$ and an object $u$ of level $N$ over $X$, such that each object over a scheme $S$ is the pullback of $u$ along a unique map $S \to X$ over $\operatorname{Spec} R$. Let $a$ and $n$ be the integers of the datum.

**Theorem.** Let $R$ be noetherian, $N \geq 3$ and $\gcd(N, p) = 1$. Let $(X, s, u)$ be a representing family of level $N$. If $s$ is quasi-projective, then $s$ is smooth of relative dimension $a(n-1)$.

Here *quasi-projective* (`IsQProjOver`) means that $s$ factors as a quasi-compact immersion $X \to \mathbb{P}^m_R$ followed by the projection, for some $m$.

## Proof

The proof is `exact GlobalTheory.UPel.HT.RepFam.smoothOfRelativeDimension`. The real content is in that theorem and below it.

## In the Lean code

The theorem is in [SmoothOfRelativeDimensionStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SmoothOfRelativeDimensionStatement.lean#L7). The proof is a `first | exact … | …` combinator that closes the goal with the theorem of the same statement. `SmoothOfRelativeDimension` is the predicate of Mathlib; we have not opened its file. The dimension `D.a * (D.n - 1)` uses natural subtraction, which is safe since $n \geq 1$.
