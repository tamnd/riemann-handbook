---
id: unit-period-translates-moments-finite
title: The moments of the unit period translates, a second name
kind: theorem
decl: GlobalTheory.T.unitPeriodTranslates_moments_finite
module: Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.UnitPeriodTranslatesMomentsFiniteStatement
covers: 1357
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the moments of the unit period translates](/entry/moments-fin/). That entry has the content. Its user is [the integral jet moments](/entry/jet-moments/), which passes it to `jetMoments_of_unitPeriod`.

## Statement

**Theorem.** Assume the equivariance laws `EqP` for all theta data, and assume that the Taylor coefficients of the translates $U_t e$ of the theta family are algebraic for all torsion points $t$. Let $p \ne 2$ be a prime with $\left(\frac{-d}{p}\right) = 1$, prime to $N(c)$, and let $\lambda \colon \overline{\mathbb{Q}} \to \mathbb{C}_p$ be an embedding. Then there is $\Omega \in \mathbb{C}_p$ with $|\Omega| = 1$ such that the jets of the translated theta functions are the moments of $p$-adic measures of norm at most 1.

It is stated in full in [the moments of the unit period translates](/entry/moments-fin/).

## Proof

The proof applies `GlobalTheory.MomFin.moments_fin`, which has the same statement. Nothing else happens.

## In the Lean code

The theorem is in [UnitPeriodTranslatesMomentsFiniteStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/UnitPeriodTranslatesMomentsFiniteStatement.lean#L7). The proof is a `first | exact ... | ...` combinator with three tries, each with the same lemma. Line 6 sets `maxHeartbeats 1000000`, which a one-line proof does not need. The file is named as a statement file, but it imports the proof module (line 2) and only renames the theorem there.

The word "finite" in the name does not match the conclusion, which is a norm bound $\|\mu\| \le 1$ on each measure.
