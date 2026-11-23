---
id: whit-gen-low
title: The global Whittaker integral vanishes in low rank
kind: theorem
decl: PositivityTheory.SiegelWeilFormula.Fin.whitGenLow
module: Development.WeilBound.CoreStatements.AutomorphicKernels.SiegelWeilFormula.SiegelWeilStandard.SiegelWeilStdOf
covers: 310
status: drafted
drafted_by: writer@claude
---
This theorem says that the adelic Whittaker integral of the Siegel-Weil formula has the value $0$ at the point $s_0 = (M-n)/2$ when the space has dimension $M < n$. It is one of three cases. The case $n < M$ is `whitGenLt`, and the case $M = n$ is [`whitGenEq`](/entry/whit-gen-eq/). Its users are [`siegelWeilStd_of`](/entry/siegel-weil-std-of/) and `siegelWeilStd_of_k`, on the way to the step [every character](/step/every-character/).

## Statement

Let $E/F$ be a CM extension, $J \in M_M(E)$ a nondegenerate Hermitian matrix, and $T \in M_n(E)$ a Hermitian matrix with $\det T \neq 0$. Let $\psi$ be an additive character of $\mathbb{A}_F$. Let $\Phi = \Phi_\infty \otimes \Phi_f$, where $\Phi_f$ is a pure tensor that is the indicator of the standard lattice at almost all $v$. Let $\mu$ and $\nu$ be self-dual measures, and let $W(b, z)$ be the adelic Whittaker integrand, as in [`locC`](/entry/loc-c/) but over $\mathbb{A}_F$.

**Theorem.** Assume $1 \le M < n$, that the archimedean frames of $J$ have one sign at each place (so $J$ is definite there), that the polynomial part of $\Phi_\infty$ is $1$, and that $W(\cdot, z)$ is $\nu$-integrable for $\operatorname{Re} z$ large. Then $z \mapsto \int W(b, z)\, d\nu(b)$ continues holomorphically to $s_0$, with the value $0 \cdot I$. Here $I$ is the mean over a fundamental domain of the theta sum over frames $X$ with $X^* J X = T$.

## Proof

The theorem is `whitGenLowOf` applied to five inputs: the local integral at a finite place (`locFinX`), the unramified integral (`unrWhitX`), the archimedean integral (`realLow_of`), the factorisation into places (`factorX`), and the order of partial $L$-products (`lOrd`). The proof of `whitGenLowOf` goes as follows.

1. **Archimedean factor.** It is $(z - s_0)^a W_\infty(z)$, with $a = [F:\mathbb{Q}](n-M)$.
2. **Bad places.** Let $S$ be a finite set of places outside which the data are unramified and standard. For $v \in S$ the local factor $W_v$ is holomorphic with $W_v(s_0) = 0$. The reason is that the Gram density is $0$ when $M < n$ (`densZero`).
3. **Good places.** Outside $S$ the product of the local factors is $\prod_{i<n} Z_i(2z+n-i)$, a product of partial $L$-functions.
4. **Order count.** The pole order of this product at $s_0$ is at most $[F:\mathbb{Q}](n-M) + \lvert S \rvert - 1$. This is less than $a + \lvert S \rvert$, the order of the zero from steps 1 and 2.
5. So the product has a holomorphic extension with the value $0$ at $s_0$ (`analyticAt_update_zero`).

## In the Lean code

The theorem is in [SiegelWeilStdOf.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilStandard/SiegelWeilStdOf.lean#L49). `WhitGenX` and `WhitGenLow` are in [WhitGenLowOf.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/WhitGenLowOf.lean#L158), and the proof `whitGenLowOf` is in [WhittakerLowRank/WhitGenLowOf.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/WhittakerLowRank/WhitGenLowOf.lean#L13). We have not unfolded `phiInf`; "polynomial part" is our reading of the hypothesis that each `P i` is $1$. `WhitGenX` also assumes $n + 2 \le M$ or that $J$ is anisotropic. The proof does not use this hypothesis. Since $M < n$, no $M \times n$ frame has an invertible Gram matrix, so the theta sum is empty anyway.
