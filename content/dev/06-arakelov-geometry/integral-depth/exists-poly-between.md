---
id: exists-poly-between
title: A global harmonic polynomial with the local depth of the columns
kind: theorem
decl: GlobalTheory.RefSum.GlobalPoly.exists_polyBetween
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsHarmonicPolynomialLocalDepthBetween
covers: 392
status: drafted
drafted_by: writer@claude
---
This theorem finds one global polynomial $P_1$, in the set `harmA` $a$ $n$, whose local depth at every algebraic point above $\lambda$ equals the depth $\nu_p$ there. So the bounds $A \le \nu_p \le B$ pass to $P_1$. Its only user is its renaming [exists_harmonicPolynomial_localDepth_between](/entry/exists-harmonic-polynomial-local-depth-between/), step 1 of [refExp_le_of_oscLe](/entry/ref-exp-le-of-osc-le/). Below this theorem are 392 declarations.

## Statement

The statement is the one of [exists_harmonicPolynomial_localDepth_between](/entry/exists-harmonic-polynomial-local-depth-between/): from `NuBetween` $\lambda$ $(\mathrm{gap}\,a)$ $A$ $B$ it gives $P_1 \in$ `harmA` $a$ $n$ with `PolyBetween` $\lambda$ $P_1$ $A$ $B$.

## Proof

The idea is approximation. Over each ring $T$ above $\lambda$, $P_1$ is congruent modulo a high power of $p$ to a product of minors of columns, and the local depth of that product is $\nu_p$.

1. **The precision.** Choose $N \in \mathbb{N}$ with $N > B + \sum_{q \mid \mathrm{condN}} v_{dH}(q)\,\mathrm{DF}(a)/2$, a sum over the prime factors of the conductor `condN` of the host of $D$.
2. **The global polynomial.** `exists_global_harmonic_congr_column_polynomial` gives $P_1 \in$ `harmA` $a$ $n$ such that, over each $T$ above $\lambda$, there are columns $B_{\mathrm{col}}$ with `IsCols` for `gap` $a$ and a polynomial $R$ in `FFV` with $P_1 = \mathrm{polyT}(B_{\mathrm{col}}) + p^N R$. Here `polyT` is the product over factors $f$ of the $\mathrm{gap}(a)(f)$-th powers of the minors `cMat` of the columns.
3. **The columns.** [columnPolynomial_localDepth_eq_placeDepth](/entry/column-polynomial-local-depth-eq-place-depth/) gives $\nu_{\mathrm{loc}}(\mathrm{polyT}(B_{\mathrm{col}})) = \nu_p(y, \mathrm{gap}\,a)$ at each point $y$ and chart.
4. **The perturbation.** `chBound_host` gives a chart bound $\rho$. `vV_prime_le` (if $v(p) > 0$, then $v(q) \le v(p)$ for each prime $q$) shows that $\rho$ is at most the sum in step 1, so $B + \rho < N$. Then `localDepth_stable_under_prime_pow_perturbation` says that adding $p^N R$ does not change the local depth.

So $\nu_{\mathrm{loc}}(P_1) = \nu_p(y, \mathrm{gap}\,a) \in [A, B]$. The upper bound uses that $y$ is algebraic.

## In the Lean code

The theorem is at [ExistsHarmonicPolynomialLocalDepthBetween.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsHarmonicPolynomialLocalDepthBetween.lean#L62). `IsCols` and `polyT` are at [NonemptyValExtOfOverLa.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/NonemptyValExtOfOverLa.lean#L339), `harmA` at [IsThRule.lean](lean:Formalism/LocalToGlobal/ProjectiveLattices/IsThRule.lean#L86).

- The helpers `vLa_pos_of_mem`, `vV_of_isUnit` and `vV_prime_le` are in the same file.
- $D$ enters only through its field $E$ and, in the proof, through `condN` and `vdH`. The host $H$ is a separate argument.
- We have not unfolded `harmA` (a set `HaO` of polynomials, called harmonic in the names), `FFV`, `ChBound` or the lemmas of steps 2 and 4.
