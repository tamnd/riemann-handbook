---
id: column-polynomial-local-depth-eq-place-depth
title: The local depth of a column polynomial is the depth at the point, renamed
kind: theorem
decl: GlobalTheory.T.columnPolynomial_localDepth_eq_placeDepth
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ColumnPolynomialLocalDepthEqPlaceDepthStatement
covers: 358
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It restates [nuLocOf_eq_nuP](/entry/nu-loc-of-eq-nu-p/) with the same statement. It is step 3 of [exists_polyBetween](/entry/exists-poly-between/), where it computes the local depth of the column polynomial. Below this theorem are 358 declarations.

## Statement

Let $p$ be a prime, $\lambda$ a point of the flag model at $p$, and $T$ a complete discrete valuation ring above $\lambda$ (`OverLa`). Let $y$ be an integral point over $T$ with a chart $\mathrm{Ch}$, and let $c_x$ give a natural number to each factor $f$. Let $B$ give, for each $f$, a matrix of $\mathrm{rk}(f)$ rows and $n$ columns over $T$, with `IsCols`.

**Theorem.** For every $k$,

$$\nu_{\mathrm{loc}}\bigl(\mathrm{Ch}, v_T(p), k, \mathrm{polyT}(B, c_x)\bigr) = \nu_p(y, c_x).$$

Here $\mathrm{polyT}(B, c_x)$ is the product over $f$ of the $c_x(f)$-th powers of the minors of $B_f$, and $\nu_p(y, c_x) = \sum_f \nu_f(y, c_x(f))$ is the depth of [sum_pt_of_size](/entry/sum-pt-of-size/).

## Proof

The proof is `first | exact @GlobalTheory.ColDepth.nuLocOf_eq_nuP | ...`. The tactic tries `exact` with [nuLocOf_eq_nuP](/entry/nu-loc-of-eq-nu-p/) first. There is no other step.

## In the Lean code

The theorem is at [ColumnPolynomialLocalDepthEqPlaceDepthStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ColumnPolynomialLocalDepthEqPlaceDepthStatement.lean#L12).

- The name says "place depth" for $\nu_p$ at the point $y$.
- The content is in [nuLocOf_eq_nuP](/entry/nu-loc-of-eq-nu-p/).
