---
id: ref-exp-le-of-osc-le
title: The reference exponent is at most the oscillation, off the host primes
kind: theorem
decl: GlobalTheory.RefAway.refExp_le_of_oscLe
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.BaseLocusExponentLeOscillationNonTypePrime
covers: 407
status: drafted
drafted_by: writer@claude
---
This theorem bounds the reference exponent $r_q(G)$ at a prime $q \ne g_0, g_1$ by the oscillation $b$ of the depth $\nu_q$. The method is theta series: a harmonic polynomial with the right local depth gives cusp forms of weight $G$ whose valuations at a point lie between $A$ and about $A + b$, and division by a scalar of valuation $A$ makes them integral. Its only user is its renaming [baseLocusExponent_le_oscillation_nonTypePrime](/entry/base-locus-exponent-le-oscillation-non-type-prime/), step 4 of [refCore_of_size_sumPt](/entry/ref-core-of-size-sum-pt/). Below this theorem are 407 declarations.

## Statement

We use $r_q(G)$ (`refExp_vp`) of [the reference exponent bound](/entry/refined-sum-weight-of-size-alt/) and `OscLe` of [sum_pt_of_size](/entry/sum-pt-of-size/). Recall that $r_q(G) \le b$ means: for each algebraic integral point $y$ over a complete discrete valuation ring above $q$, and each $\varphi$ with `HasPhi` $y$ $\varphi$,

$$\delta_G(y) \le b + \frac{c\,\varphi}{v(q)},$$

where $\delta_G(y)$ (`depthAt_vp`) is the least valuation at $y$ of a section in the lattice `latW` of weight $G$.

**Theorem.** Let $T$ be a core with `LawsM`, `ErrX` $D$, and a level $j$ with `InR`. Let $a$ be exponents with `Dom` $a$ $n$ and `LastPos`, with $\sum_f 2\,\mathrm{rk}(f) \le n$ and $2r \le n$, and with `JetNum` $D$ $(\mathrm{DF}(a))$ $c$. Let $q \ne g_0, g_1$ be prime. If `OscLe` holds at $q$ for `gap` $a$ with bound $b$, then $r_q(\mathrm{wtZ}(a, n)) \le b$ with constant $c$ on the family `T.U j`.

## Proof

Fix a point $\lambda$ of the flag model at $q$, a point $y$ above it and $\varphi$. Let $v = v(q)$. `OscLe` gives $A \in \mathbb{N}$ with $\nu_q \in [A, A + b]$ above $\lambda$.

1. **The polynomial.** [exists_harmonicPolynomial_localDepth_between](/entry/exists-harmonic-polynomial-local-depth-between/) gives a harmonic polynomial $P_1 \in$ `harmA` $a$ $n$ whose local depth lies in $[A, A + b]$ at every chart of every algebraic point above $\lambda$.
2. **The upper bound.** `exists_finiteExtension_uniformisedChart_scale` moves $y$ to a point $y'$ over a finite extension with ramification $r$ and a uniformised chart. `exists_short_periodLattice_basis_balanced_slope` gives a short basis of size $\rho \le 2fm$. `LawsM` gives the level $M = g_0 g_1$, and `half_principal_and_split` an $\alpha$ with $\alpha\bar\alpha = M$. Since $q \nmid M$, $M$ is a unit. Then `iInf_thRule_le_nuLocOf` says: the least valuation at $y'$ of a theta series built from $P_1$ is at most the local depth of $P_1$ plus an error. `JetNum` and `err_le` bound the error by $c\varphi/v$. So this least valuation is at most $A + b + c\varphi/v$.
3. **The lower bound.** `thRule_lower` gives valuation at least $A$ for each such theta series $f$ at every algebraic point above $\lambda$. `thetaRules_exist_and_cusp` makes $f$ a cusp form of weight $G$, and `thetaRule_bounded_below` bounds it below at all places. Then `cuspForm_clear_denominators_away_from_place` gives $s$ with $v_\lambda(s) = -A\,v_\lambda(q)$ and $s f \in$ `latW`. Hence $\delta_G(y) \le \operatorname{val}_y(f) - A$.

Steps 2 and 3 give $\delta_G(y) + A \le A + b + c\varphi/v$. The rest is bookkeeping of the normalizations $v$ and $rv$.

## In the Lean code

The theorem is at [BaseLocusExponentLeOscillationNonTypePrime.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/BaseLocusExponentLeOscillationNonTypePrime.lean#L125). `refExp_vp_le_iff` is at [NonnegOfMemCStarSet.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/NonnegOfMemCStarSet.lean#L276), `JetNum` at [PolyBetween.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/PolyBetween.lean#L43).

- The helper lemmas `vLa_nat_pos`, `isUnit_nat`, `nat_not_mem`, `le_nval_place`, `coprime_type` and `err_le` are in the same file. `err_le` is an inequality of real numbers.
- The hypothesis $2r \le n$ is used only to get $n \ge 1$.
- `ErrX` $D$ is an unnamed binder, but it is used: `half_principal_and_split` and `level_halfSplit` take it.
- We have not opened the proofs of the lemmas of steps 2 and 3, nor `HasPhi`, `latW` or `IsThRule`.
