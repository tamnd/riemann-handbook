---
id: whit-gen-eq
title: The Whittaker coefficients in equal rank
kind: theorem
decl: PositivityTheory.SiegelWeilFormula.Fin.whitGenEq
module: Development.WeilBound.CoreStatements.AutomorphicKernels.SiegelWeilFormula.SiegelWeilStandard.SiegelWeilStdOf
covers: 561
status: drafted
drafted_by: writer@claude
---
This theorem proves `WhitGenEq`, the equal rank case of an identity between global Whittaker integrals and theta orbit sums. [The Siegel-Weil formula from its inputs](/entry/siegel-weil-std-of/) uses it for the case $n = m$, below the step [EveryCharacter](/step/every-character/). The theorem is a pass-through: it applies `Gen.whitGenEqOf` to six proved inputs.

## Statement

Let $E/F$ be a CM extension of number fields. Let $J$ be a nondegenerate Hermitian matrix of size $M$, anisotropic over $E$. Let $T$ be a Hermitian matrix of size $n = M \ge 1$ with $\det T \ne 0$. Fix an additive character, archimedean data, Haar measures and a pure Schwartz function $\Phi = \Phi_\infty \otimes \Phi_f$. Let $W_T(z) = \int \nu(b)^{-z}\, j(\Phi)(b)\, \psi(-\operatorname{tr} T b)\, db$, an integral over the adelic Hermitian matrices $b$ of size $n$, where $\nu$ is a norm function and $j(\Phi)$ is the function `jtR`, which we have not unfolded. Assume that the integrand is integrable for $\operatorname{Re} z$ large.

**Theorem.** For each Haar measure and fundamental domain, $W_T$ extends holomorphically to $z = 0$, and $W_T(0) = 2\,\mathrm{mean}(\theta_T)$. Here $\theta_T$ is the theta orbit sum of $\Phi$ over the $X$ whose Gram matrix under $J$ is $T$, and the mean is `meanC` over the fundamental domain.

This is `WhitGenX` with $c = 2$. The cases $n < M$ (`whitGenLt`, $c = 1$) and $M < n$ (`whitGenLow`, $c = 0$) are in the same file.

## Proof

The proof is one line:

```
Gen.whitGenEqOf SwLocFin.locFinX Gunr.unrWhitX (GReal.realWhitEq_of WR.wr) GFac.factorX Gen.lOrd PositivityTheory.Rg.Base1.densEq
```

The inputs are: holomorphy of the local Whittaker integrals at the finite places, the unramified local values, the archimedean case, the factorization of $W_T$ into local integrals, the order of the partial $L$-functions at the point, and the density identity [`densEq`](/entry/dens-eq/). The proof of `whitGenEqOf` is in [WqMain.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/WhittakerEqualRank/WqMain.lean#L10). It builds the continuation as the archimedean integral times the finite bad local integrals times an $L$-function factor, and evaluates it at $0$ by `densEq`.

## In the Lean code

The theorem is in [SiegelWeilStdOf.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilStandard/SiegelWeilStdOf.lean#L46). The statement is in [WhitGenLowOf.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/WhitGenLowOf.lean#L171). In `WhitGenX` the anisotropy is the alternative to $n + 2 \le M$, which cannot hold when $M = n$.
