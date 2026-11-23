---
id: ref-core-of-size-sum-pt
title: The reference exponent bound on the core tower
kind: theorem
decl: GlobalTheory.RefSum.refCore_of_size_sumPt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.RefCoreOfSumPt
covers: 427
status: drafted
drafted_by: writer@claude
---
This theorem turns the oscillation bound `SumPtAlt` into a bound for the reference exponents on the core tower (`ReferenceCore`). It treats the two host primes apart from all other primes. Its only user is its renaming [reference_core_of_size_and_sum_point](/entry/reference-core-of-size-and-sum-point/), step 2 of [the reference exponent bound](/entry/refined-sum-weight-of-size-alt/). Below this theorem are 427 declarations.

## Statement

**Theorem.** `SizeCondition` and `SumPtAlt` imply `ReferenceCore`. If `SumPtAlt` holds with constant $C_1$ and the bound on $L(\log g_0 + \log g_1)$ below holds with constant $C_3$, then `ReferenceCore` holds with $C_1 + C_3$.

`SumPtAlt` is stated in [sum_pt_of_size](/entry/sum-pt-of-size/) and `ReferenceCore` in [reference_core_of_size_and_sum_point](/entry/reference-core-of-size-and-sum-point/). Here $g_0, g_1$ are the two host primes of the family.

## Proof

The proof combines three level statements with `Closed.and` and `Closed.imp`, and then works at one point $p$, one level $i$ with $i + 1 < m$ and one weight $u$ with `Quo`. Let $a_u$ be the exponents of the theta weight, so that $G_u = $ `wtZ` $a_u$ $n$ with $n$ = `nCol`.

1. **Inputs.** `SumPtAlt` gives $S$, $e$, $s$ with $L s \le C_1\,\mathrm{unitE}$ and `OscLe` with bound $e_q$ at each prime $q \ne g_0, g_1$. From `SizeCondition`, `quotient_weight_gap_bounds'` gives the shape conditions `Dom` and `LastPos` for $a_u$, and `jetNum_nCol_lenT_bounds_of_quo` gives `JetNum` with constant $1/2500$, $2r \le n$, and $L(\log g_0 + \log g_1) \le C_3\,\mathrm{unitE}$.
2. **The new prime sum.** `primeSum_add_pair` adds the host primes. The set is $S \cup \{g_0, g_1\}$, the exponents are $e'_q = e_q + 1$ at a host prime and $e'_q = e_q$ elsewhere, and the sum is $s' = s + \log g_0 + \log g_1$. Then $L s' \le (C_1 + C_3)\,\mathrm{unitE}$.
3. **At a host prime.** `supLatticeReferenceExponent_thetaWeight_level_le_one` gives $r_{g_k}(G_u) \le 1$. Since $e_{g_k} \ge 0$, this is at most $e'_{g_k}$.
4. **At another prime.** [baseLocusExponent_le_oscillation_nonTypePrime](/entry/base-locus-exponent-le-oscillation-non-type-prime/) says: at a prime $q \ne g_0, g_1$, `OscLe` with bound $b$ for the gaps of $a_u$ gives $r_q(G_u) \le b$. With $b = e_q$ this is the bound.

Steps 3 and 4 also need $1 \le i + 1 \le m$ (`InR`) and $\sum_f 2\,\mathrm{rk}(f) \le n$ (`sum_le_nCol`). The rest is bookkeeping.

## In the Lean code

The theorem is at [RefCoreOfSumPt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RefCoreOfSumPt.lean#L15).

- `SizeCondition` enters only through the two input lemmas. `quotient_weight_gap_bounds'` restates `quo_shape_dom_lastPos_weight_eq`, which is `fun _ => ...` and discards it. We have not checked whether `numbers_at_point`, behind `jetNum_nCol_lenT_bounds_of_quo`, uses it in the end.
- The constant of the shape statement is discarded (the pattern `⟨C2, -, h2⟩`), and so is most of its content: the proof keeps only `Dom` and `LastPos`.
- The host prime case needs no oscillation bound. The lemma of step 3 takes only the laws of the core, the shape conditions, $2r \le n$ and `JetNum`. This fits `SumAt`, which asks for `OscLe` only off $g_0, g_1$.
- A copy with the older names is `refCore_of_sumPt : Size → SumPt → RefCore` in [ReferenceCoreOfSumPoint.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ReferenceCoreOfSumPoint.lean#L39).
- We have not unfolded `JetNum`, `Dom`, `LastPos` or the two exponent lemmas of steps 3 and 4.
