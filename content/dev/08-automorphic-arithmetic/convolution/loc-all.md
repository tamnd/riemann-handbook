---
id: loc-all
title: Matching of spherical functions at all unramified places
kind: theorem
decl: UpperTheory.ConvolutionTheory.GM.locAll
module: Development.AutomorphicArithmetic.Foundations.Convolution.GeneralizedMeasures.LocAll
covers: 349
status: drafted
drafted_by: writer@claude
---
This theorem gives the matching of spherical Hecke functions for cyclic base change at every place of $F$ unramified in $E$, from the matching of the units ($\mathrm{LocUnit}$). The functions carry an auxiliary factor $\gamma_w$ at the places $w$ of a finite set $\kappa$. [Matched test functions for one Hecke monomial](/entry/term-ex/) uses it at every place outside $S \cup \{q\}$. It joins the split case `locHeckeSplit` and the inert case [`locHeckeInert`](/entry/loc-hecke-inert/).

## Statement

Let $E/F$ be a cyclic extension of totally complex number fields of prime degree, and $n > 0$. For a finite place $w$ of $E$ over $v$, let $f(w)$ be its residue degree. Write $\mathrm{IsSph}(w, p, h)$ when $h$ is spherical on $\mathrm{GL}_n(E_w)$ and its Satake transform is $p(e_1, \dots, e_n)$, with $e_i$ the elementary symmetric polynomials in the Satake variables.

**Theorem.** $\mathrm{LocUnit}$ implies $\mathrm{LocAll}$: let $\kappa$ be a finite set of places of $E$ over places unramified in $E$, let $t_0(w)$ be a multiset of $n$ nonzero numbers for $w \in \kappa$, and let $D \in \mathbb{N}$. Then there are polynomials $\gamma_w$ with $\gamma_w(e(t_0(w))) \neq 0$ for $w \in \kappa$, with this property. Let $p_w$ have degree at most $D$, and let $v$ be unramified in $E$. Let $h_w$ satisfy $\mathrm{IsSph}(w, \gamma_w p_w, h_w)$ for $w \in \kappa$, and let $h_w$ be the unit for $w \notin \kappa$. Let $f$ be spherical on $\mathrm{GL}_n(F_v)$ with Satake transform $\prod (\gamma_w p_w)(e(x^{f(w)}))$ over $w \in \kappa$, $w \mid v$. Then $\bigotimes_{w \mid v} h_w$ matches $f$ with constant 1.

## Proof

1. **The polynomials.** For $w \in \kappa$ over a split place, put $\gamma_w = 1$. Over a non-split place, take $\gamma_w$ from `locHeckeInert` for $t_0(w)$ and $D$.
2. **Split $v$.** All $f(w) = 1$, and $x \mapsto x^1$ is the identity. `locHeckeSplit` gives the matching.
3. **Non-split $v$.** There is one place $w$ over $v$ (`placeUniq_holds`), and $f(w) = [E:F]$. If $w \in \kappa$, the choice of $\gamma_w$ gives the matching. If $w \notin \kappa$, the Satake transform of $f$ is 1. The Satake transform is injective, so $f$ is the unit, and $\mathrm{LocUnit}$ gives the matching.

## In the Lean code

The theorem is in [LocAll.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/GeneralizedMeasures/LocAll.lean#L82). $\mathrm{LocAll}$ is in [HeckeFinAlt.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/GeneralizedMeasures/HeckeFinAlt.lean#L142), and $\mathrm{LocUnit}$, $\mathrm{LocHeckeSplit}$ and $\mathrm{LocHeckeInert}$ are in [LocHeckeInert.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/GeneralizedMeasures/LocHeckeInert.lean#L140).

- $\mathrm{LocUnit}$ is used only at non-split places $v$ whose place above is not in $\kappa$ (line 139). At split places, `locHeckeSplit` covers the units as well.
- The factor $\gamma_w$ is needed only at inert places; at split places it is 1.
