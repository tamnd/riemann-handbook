---
id: siegel-unit-edge-class-kummer-dlog-congruence
title: A congruence for the edge class of two Siegel units (restatement)
kind: theorem
decl: GlobalTheory.T.siegelUnit_edgeClass_kummer_dlog_congruence
module: Development.AbelianVarietyTheory.Proofs.FoundationProofs.SiegelUnitEdgeClassKummerDlogCongruenceStatement
covers: 1018
status: drafted
drafted_by: writer@claude
---
This theorem gives a congruence modulo $p^n$ between the logarithmic $q$-expansion of an "edge" Kummer class built from two Siegel units and the $q$-expansion of a product of two Eisenstein series of weight one. [The Siegel unit lemma `one`](/entry/one/) uses it, at line 160 of its file. This is a renaming. The real content is in [the edge congruence for a pair of Siegel units](/entry/pair-edge-dlog/).

## Statement

The statement is word for word the statement of `GlobalTheory.pair_edge_dlog`. In short: for each odd prime $p$ there is a constant $c$ with the following property. Take two Siegel units $a$ and $b$ of level $Np^L$ and their $p^n$-th roots $\alpha$ and $\beta$. Let $x$ and $y$ be the Kummer characters of $\alpha$ and $\beta$, and let $\eta$ be a locally constant cochain whose coboundary is $x \cup y$ on the subgroup that fixes a field $K$. Let $w \in K$ have a $p^n$-th root whose Kummer character is the edge class of $(x, y, \eta, \sigma)$. Then $p^c$ times the coefficients of the logarithmic derivative of $w$ are congruent modulo $p^n$ to a coboundary $s^{-1}(\xi_r) - \xi_r$ minus an explicit multiple of the coefficients of a product of two Eisenstein series. The entry for `pair_edge_dlog` gives all hypotheses.

## Proof

The proof is

```
first | exact @GlobalTheory.pair_edge_dlog | ...
```

It applies `pair_edge_dlog` to the same arguments.

## In the Lean code

The theorem is in [SiegelUnitEdgeClassKummerDlogCongruenceStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/SiegelUnitEdgeClassKummerDlogCongruenceStatement.lean#L8). It only copies the statement of `pair_edge_dlog` into the namespace `GlobalTheory.T`. Its subtree, 1,018 declarations, is that of `pair_edge_dlog` plus one.
