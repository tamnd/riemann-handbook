---
id: loc-hecke-inert
title: Matching of spherical functions at an inert place
kind: theorem
decl: UpperTheory.ConvolutionTheory.H.locHeckeInert
module: Development.AutomorphicArithmetic.Foundations.Convolution.SphericalHeckeOperators.LocHeckeInert
covers: 319
status: drafted
drafted_by: writer@claude
---
This theorem proves the base change matching of spherical functions at a place $v$ of $F$ that is unramified and not split in $E$, for functions whose Satake transform has an auxiliary factor $\gamma$. It moves the local result [base change matching with a deep factor](/entry/deep-hecke/), stated for an extension of local fields, to the completions of the number fields. Its only user is [matching at all unramified places](/entry/loc-all/).

## Statement

Let $E/F$ be a cyclic extension of number fields of prime degree, with generator $\sigma$, and $n > 0$. Let $v$ be a finite place of $F$, unramified in $E$ and not split, and let $w$ be a place of $E$ over $v$. Use $\mathrm{IsSph}$ and `MatchAt` as in [the parent entry](/entry/loc-all/).

**Theorem.** Let $t$ be a multiset of $n$ nonzero complex numbers and $D \in \mathbb{N}$. There is a polynomial $\gamma$ in $n$ variables with $\gamma(e_1(t), \dots, e_n(t)) \neq 0$ such that, for each $p$ of degree at most $D$: if $\mathrm{IsSph}(w, \gamma p, h)$ and $f$ is spherical on $\mathrm{GL}_n(F_v)$ with Satake transform $(\gamma p)(e(x^{l}))$, $l = [E:F]$, then $h$, seen as a function on $\mathrm{GL}_n(E \otimes F_v)$, matches $f$ with constant 1.

## Proof

1. Since $[E:F]$ is prime and $v$ does not split, $w$ is the only place over $v$ (`placeUniq_holds`). `placeData_holds` makes $E_w/F_v$ a cyclic unramified extension of degree $l$, with a generator $s$ compatible with $\sigma$.
2. Take Haar measures that give the maximal compact subgroups volume 1. Write $t$ as the entries of $z \in (\mathbb{C}^\times)^n$.
3. `polyAlg` gives a finite set $P$ whose span contains the Satake images of all $p$ of degree at most $D$, and the rule that base change of Satake transforms is $x \mapsto x^l$ in the variables.
4. `deepHecke` gives a symmetric $g$ with $g(z) \neq 0$ and the matching for $gp$, $p$ in the span of $P$. Write $g$ as the image of a polynomial $\gamma$ in $e_1, \dots, e_n$.
5. For given $h$ and $f$, `sphIndep` makes them elements of the spherical Hecke algebras with the normalized measures. `placeOfLocal_holds` carries the matching on $\mathrm{GL}_n(E_w)$ to $\mathrm{GL}_n(E \otimes F_v)$ with constant 1. The rest is bookkeeping with measures.

## In the Lean code

The theorem is in [LocHeckeInert.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/SphericalHeckeOperators/LocHeckeInert.lean#L39). The statement $\mathrm{LocHeckeInert}$ is in [the definitions file](lean:Development/AutomorphicArithmetic/Foundations/Convolution/GeneralizedMeasures/LocHeckeInert.lean#L151).

The result is weaker than matching for the full spherical Hecke algebra: it holds only for multiples of $\gamma$, and $\gamma$ depends on $t$ and $D$. The statement of $\mathrm{LocAll}$ asks only for $\gamma(t) \neq 0$ at the given Satake parameters.
