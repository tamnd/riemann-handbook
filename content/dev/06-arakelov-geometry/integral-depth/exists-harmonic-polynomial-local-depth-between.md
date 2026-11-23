---
id: exists-harmonic-polynomial-local-depth-between
title: A harmonic polynomial with local depth between two bounds, renamed
kind: theorem
decl: GlobalTheory.T.exists_harmonicPolynomial_localDepth_between
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsHarmonicPolynomialLocalDepthBetweenStatement
covers: 393
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It restates [exists_polyBetween](/entry/exists-poly-between/) with the same statement. It is step 1 of [refExp_le_of_oscLe](/entry/ref-exp-le-of-osc-le/), where it supplies the harmonic polynomial from which the theta series are built. Below this theorem are 393 declarations.

## Statement

Let $p$ be a prime and $\lambda$ a point of the flag model at $p$. Let $a$ be exponents with $i \mapsto a(\tau, i)$ decreasing for each embedding $\tau$, and let $n \ge \sum_f 2\,\mathrm{rk}(f)$.

**Theorem.** Suppose that the depth $\nu_p(y, \mathrm{gap}\,a)$ is at least $A$ at every integral point $y$ above $\lambda$, and at most $B$ when $y$ is algebraic (`NuBetween`). Then there is a polynomial $P_1$ in the set `harmA` $a$ $n$ (called harmonic in the names; we have not unfolded it) such that, at every algebraic point $y$ above $\lambda$, every chart and every $k$, the local depth of $P_1$ (`nuLocOf`) lies in $[A, B]$ (`PolyBetween`).

## Proof

The proof is `first | exact @GlobalTheory.RefSum.GlobalPoly.exists_polyBetween | ...`. The tactic tries `exact` with [exists_polyBetween](/entry/exists-poly-between/) first. There is no other step.

## In the Lean code

The theorem is at [ExistsHarmonicPolynomialLocalDepthBetweenStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsHarmonicPolynomialLocalDepthBetweenStatement.lean#L12). `PolyBetween` is at [PolyBetween.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/PolyBetween.lean#L19), `NuBetween` at [EightDvdNCol.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/EightDvdNCol.lean#L26).

- The host $H$ is a separate argument, with type `Host D.host.E`. It need not be the host of $D$.
- The content is in [exists_polyBetween](/entry/exists-poly-between/).
