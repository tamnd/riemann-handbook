---
id: exists-universal-first-order-deformation-harris-taylor
title: A universal first-order deformation exists (statement form)
kind: theorem
decl: GlobalTheory.T.exists_universal_firstOrder_deformation_harrisTaylor
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsUniversalFirstOrderDeformationHarrisTaylorStatement
covers: 314
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [GlobalTheory.HTUniv.main](/entry/htuniv-main/), which has the real content. Its one user is [the tangent space of a representing family](/entry/exists-univ-tangent/), which turns the universal deformation into a tangent space of dimension $a(n-1)$.

## Statement

Use the datum $D$, the base $b$ over $R$ and the objects of level $N$ of [the integral model entry](/entry/model-nonempty/). Let $d = a(n-1)$, $V = k^d$, and let $k[V] = k \oplus V$ and $k[\varepsilon] = k \oplus k$ be the square-zero extensions.

**Theorem.** Let $N \geq 3$ with $\gcd(N, p) = 1$. Let $k$ be an algebraically closed field, $t \colon \operatorname{Spec} k \to \operatorname{Spec} R$, and $o_0$ an object over $t$. Then there is an object $o$ over $\operatorname{Spec} k[V]$ (with the constant structure map) and a map $o_0 \to o$ over the closed point, such that for each object $o'$ over $\operatorname{Spec} k[\varepsilon]$ with a map $o_0 \to o'$ over the closed point, there is a unique $k$-linear $c \colon V \to k$ with a map $o' \to o$ over $\operatorname{Spec}(\mathrm{id} \oplus c)$.

## Proof

The statement is the same as that of `GlobalTheory.HTUniv.main`, and the proof applies it. See [its entry](/entry/htuniv-main/).

## In the Lean code

The theorem is in [ExistsUniversalFirstOrderDeformationHarrisTaylorStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsUniversalFirstOrderDeformationHarrisTaylorStatement.lean#L9). The proof is `first | exact @GlobalTheory.HTUniv.main | ...`, a tactic that tries the alias in three forms. A "map of objects" is `ObjMap` in [NotCompactOfMEqOne.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/NotCompactOfMEqOne.lean#L190): a cartesian map of abelian schemes that respects the $O$-action, the polarization bundle and the level structure.
