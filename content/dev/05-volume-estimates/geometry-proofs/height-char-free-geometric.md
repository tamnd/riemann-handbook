---
id: height-char-free-geometric
title: Freeness at a geometric point of positive characteristic, restated
kind: theorem
decl: GlobalTheory.T.height_char_free_geometric
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.HeightCharFreeGeometricStatement
covers: 483
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`hfree_geom`](/entry/hfree-geom/), which has the content. Its one user is [`HodgeFreeStalk.at_point`](/entry/at-point/), which applies it at a stalk of residue characteristic $p$ after base change to an algebraically closed field.

## Statement

Let $E$ be a CM field with host datum $H$, with the star map of complex conjugation on $\mathcal{O}_E$. Let $t$ be a semi-abelian scheme over $X$ with $\mathcal{O}_E$-action and a cubical line bundle, with `PowFns t`. Let $k$ be an algebraically closed field of characteristic $p > 0$, and $x \colon \operatorname{Spec} k \to X$ a point with `GeomPF t x`. Let $g$ be a formal germ of $t$ at $x$ of dimension $d$. If `HChar` holds for $g$ with exponent $r$, then `HFree` holds for $g$ with exponent $r$.

The conditions are stated in [the entry on `hfree_geom`](/entry/hfree-geom/).

## Proof

The statement is the same as that of `hfree_geom`, and the proof applies it.

## In the Lean code

The theorem is in [HeightCharFreeGeometricStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/HeightCharFreeGeometricStatement.lean#L11). The name says "height", but no height appears in the statement. The H of `HChar` and `HFree` is the module $k^d \times k^d$ with its operators $\rho_H(a)$, and the file of the user calls the property "Hodge free".
