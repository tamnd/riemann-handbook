---
id: exists-quasi-projective-harris-taylor-family
title: A quasi-projective representing family exists (statement form)
kind: theorem
decl: GlobalTheory.T.exists_quasiProjective_harrisTaylor_family
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsQuasiProjectiveHarrisTaylorFamilyStatement
covers: 2132
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [the existence of a quasi-projective representing family](/entry/exists-rep-fam-qproj/), which has the real content. Its one user is [the existence of an integral model](/entry/model-nonempty/), which adds smoothness.

## Statement

Use the datum $D$ for a prime $p$, the base $b$ over $R$ and the objects of level $N$ from [the integral model entry](/entry/model-nonempty/).

**Theorem.** Let $R$ be noetherian and $b$ a base over $R$. If $N \geq 3$ and $\gcd(N, p) = 1$, then there is a scheme $X$ over $R$ with an object $u$ of level $N$ over $X$ such that $X$ is quasi-projective over $R$ and each object over a scheme $S$ is the pullback of $u$ along a unique map $S \to X$.

A family with this universal property but with no condition on $X$ is a *representing family*.

## Proof

The statement is the same as that of `GlobalTheory.UPel.HT.exists_repFam_qproj`, and the proof applies it.

## In the Lean code

The theorem is in [ExistsQuasiProjectiveHarrisTaylorFamilyStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsQuasiProjectiveHarrisTaylorFamilyStatement.lean#L7). The proof is `first | exact @GlobalTheory.UPel.HT.exists_repFam_qproj | ...`, a tactic that tries the alias in three forms. The conclusion is `∃ F : RepFam b N, IsQProjOver F.s`. `RepFam` is in [ToRepFam.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ToRepFam.lean#L12): it is `Model` with the fields for quasi-projectivity and smoothness removed.
