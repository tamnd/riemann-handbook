---
id: mul-mem-range-norm-of-not-mem
title: The product of two non-norms is a norm (statement)
kind: theorem
decl: GlobalTheory.T.mul_mem_range_norm_of_not_mem
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.MulMemRangeNormStatement
covers: 773
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`NormIndex.mul_mem_range_norm`](/entry/mul-mem-range-norm/), which has the real content (772 of the 773 declarations below this one). It is used under [the Gauss integral for a Hermitian form](/entry/has-gauss-herm/), in two places: to show that the sign $\eta_{E/F}$ (1 on norms, $-1$ off norms) is multiplicative, and to cancel two Gauss integrals over a norm form.

## Statement

Let $F$ be a nonarchimedean local field of characteristic $0$. Let $E/F$ be a quadratic extension, given by an $F$-algebra map $c \colon E \to E$ and a unit $\delta \in E$ with $c(\delta) = -\delta$ such that $(1, \delta)$ is an $F$-basis of $E$. Let $x, y \in F^\times$. If $x \notin N_{E/F}(E^\times)$ and $y \notin N_{E/F}(E^\times)$, then $xy \in N_{E/F}(E^\times)$.

## Proof

The proof is `GlobalTheory.KSp.NormIndex.mul_mem_range_norm`, with no change. That entry gives the argument through local class field theory.

## In the Lean code

The theorem is at [MulMemRangeNormStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/MulMemRangeNormStatement.lean#L10). Its proof is a `first | exact ...` that applies `mul_mem_range_norm` to the same arguments. The two statements are the same, word for word.

Its two callers are `KSp.sgn_mul_of_isQuad` in [LocalNormResidueSignMul.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LocalNormResidueSignMul.lean#L11) and `gauss_cancel` in [GaussIntegralNormFormNonNormCancel.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/GaussIntegralNormFormNonNormCancel.lean#L44). The sign is `KSp.sgn` in [UnipVal.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/UnipVal.lean#L50). `gauss_cancel` also applies the theorem with $x = y = t$ to get $t^2 \in N_{E/F}(E^\times)$, which holds for any $t$ since $t^2 = N_{E/F}(t)$.
