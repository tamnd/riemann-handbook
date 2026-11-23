---
id: base-locus-exponent-le-oscillation-non-type-prime
title: The reference exponent at a prime off the host primes, renamed
kind: theorem
decl: GlobalTheory.T.baseLocusExponent_le_oscillation_nonTypePrime
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.BaseLocusExponentLeOscillationNonTypePrimeStatement
covers: 408
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It restates [refExp_le_of_oscLe](/entry/ref-exp-le-of-osc-le/) with the same statement. It is step 4 of [refCore_of_size_sumPt](/entry/ref-core-of-size-sum-pt/): at a prime $q$ that is not a host prime $g_0, g_1$, it turns an oscillation bound into a bound on the reference exponent. Below this theorem are 408 declarations.

## Statement

We use the reference exponent $r_q(G)$ of [the reference exponent bound](/entry/refined-sum-weight-of-size-alt/) and `OscLe` of [sum_pt_of_size](/entry/sum-pt-of-size/).

**Theorem.** Let $T$ be a core with the laws `LawsM`, and let $j$ be a level with `InR`. Let $a$ be exponents with `Dom` $a$ $n$, `LastPos`, $\sum_f 2\,\mathrm{rk}(f) \le n$, $2r \le n$ and `JetNum` with constant $c$. Let $q$ be a prime with $q \ne g_0, g_1$. If `OscLe` holds at $q$ for `gap` $a$ with bound $b$, then $r_q(G) \le b$ for the weight $G = $ `wtZ` $a$ $n$, with constant $c$, on the family `T.U j`.

## Proof

The proof is `first | exact @GlobalTheory.RefAway.refExp_le_of_oscLe | ...`. The tactic tries `exact` with [refExp_le_of_oscLe](/entry/ref-exp-le-of-osc-le/) first. There is no other step.

## In the Lean code

The theorem is at [BaseLocusExponentLeOscillationNonTypePrimeStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/BaseLocusExponentLeOscillationNonTypePrimeStatement.lean#L12).

- The name speaks of a "base locus exponent". `refExp_vp` is built from the least valuation at $y$ of a section of weight $G$ ([IsHomogeneousCompIdeal.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsHomogeneousCompIdeal.lean#L210)), the order of the base locus at $y$. So the name fits.
- "Non-type prime" means $q \ne g_0, g_1$, the hypothesis `∀ k, q ≠ D.host.g k`.
- The content is in [refExp_le_of_oscLe](/entry/ref-exp-le-of-osc-le/).
