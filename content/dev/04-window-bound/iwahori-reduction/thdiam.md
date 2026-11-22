---
id: thdiam
title: The coefficient congruence for diamond translates, with a unit index
kind: theorem
decl: UpperTheory.Kd.L.thdiam
module: Development.AutomorphicArithmetic.Foundations.IwahoriReduction.SiegelFixedPoints.Thdiam
covers: 1516
status: drafted
drafted_by: writer@claude
---
This theorem is a reindexing of [`thcocd`](/entry/thcocd/). It takes the index $\delta$ of the diamond operator as a unit of $\mathbb{Z}/N$, where `thcocd` takes it as a natural number prime to $N$. [The coefficient law](/entry/hco/) applies it to one admissible datum and averages the result over $\delta$. The mathematics is in [`thcocd`](/entry/thcocd/) and, below it, in [`law`](/entry/law/), [`mackey`](/entry/mackey/) and [`one`](/entry/one/).

## Statement

The hypotheses and the conclusion are those of [`thcocd`](/entry/thcocd/), with one change. There, the conclusion holds for each natural number $\delta$ with $\gcd(\delta, N) = 1$, and the diamond operator and the Eisenstein-type term use $\delta$ and the residue $\delta^{-1} \bmod N$. Here, the conclusion holds for each $\delta \in (\mathbb{Z}/N)^\times$. The diamond operator uses the representative $0 \leq \delta < N$, and the Eisenstein-type term uses the representative of $\delta^{-1}$. In short: there are $c_1$ and $\kappa_0 \neq 0$ such that the coefficients of a theta series of the $\delta$-translate of the class are congruent mod $\ell^n$, after multiplication by $\ell^{c_1}$, to $\ell^{c_0}\kappa_0\, t\, \ell^m$ times an Eisenstein-type coefficient, plus a coboundary $s(g_i) - g_i$.

## Proof

Apply `thcocd` with the natural number $\delta.\mathrm{val}$. It is prime to $N$ by `ZMod.val_coe_unit_coprime`. Then rewrite $(\delta.\mathrm{val} \bmod N)^{-1}$ as $\delta^{-1}$. Nothing else happens.

## In the Lean code

The theorem is in [Thdiam.lean](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/SiegelFixedPoints/Thdiam.lean#L12). The hypothesis that $j$ is holomorphic on the upper half plane repeats the field `j_hol` of the structure `Tower`. The row condition on $g_m \bmod \ell$ and the condition $N \mid (g_m)_{10}$ are only passed to `thcocd`, which does not use them.
