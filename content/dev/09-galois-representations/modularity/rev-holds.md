---
id: rev-holds
title: A nonzero unitary period gives a nonzero theta pairing
kind: theorem
decl: UpperTheory.ConvolutionTheory.RankTwoDescent.rev_holds
module: Development.AutomorphicArithmetic.Foundations.Convolution.SplitEigenfunctions.RevTop
covers: 318
status: drafted
drafted_by: writer@claude
---
This theorem is step 8 of [the descent of a normalised cusp form](/entry/down-n/). It takes a cusp form on $\mathrm{GL}_2$ over an imaginary quadratic field $E$ with a nonzero period over $\mathrm{SL}_2(\mathbb{Q})$. It gives a [[cuspidal representation|9AZ164C298]] $\pi$ of $\mathrm{GL}_2$ over $\mathbb{Q}$ and a [[theta lift|ZBGT50BW0Z]] from $\pi$ with a nonzero pairing against the form. The quadratic space is $\mathbb{Q}^4$ with the form $q(\xi) = \xi_2^2 - \delta\xi_3^2 - \xi_1\xi_0$, where $E = \mathbb{Q}(\sqrt{\delta})$.

## Statement

Let $E$, the datum `Dat` (with $\delta < 0$), a Weil representation $W$, measures $M$ on $\mathrm{SL}_2(\mathbb{A}_\mathbb{Q})$ and $N$ on $\mathrm{SL}_2(\mathbb{A}_E)$, and a cuspidal subspace $P$ over $E$ be given. Write $\mathrm{UPer}(\varphi)$ for the integral of $\varphi$ over $\mathrm{SL}_2(\mathbb{Q})\backslash\mathrm{SL}_2(\mathbb{A}_\mathbb{Q})$, then over a fundamental domain of the norm one ideles of $E$. Write $J_1$ for the same kind of double integral over $\mathrm{SL}_2(E)\backslash\mathrm{SL}_2(\mathbb{A}_E)$.

**Theorem.** If $\mathrm{UPer}(\varphi(\cdot\,h)) \neq 0$ for some $\varphi \in P$ and $h \in \mathrm{SL}_2(\mathbb{A}_E)$, then there are a cuspidal $\pi$ over $\mathbb{Q}$ invariant under `centralSection` (`PosInv`; we have not unfolded `centralSection`), $f \in \pi$, a Fock vector $\phi$ and $\varphi' \in P$ with $J_1(\mathrm{lift}(f, \phi) \cdot \varphi') \neq 0$.

The hypothesis that $P$ is normalised is not needed here.

## Proof

`rev_holds` applies the lemma `rev` to six Props, each proved in another file. The proof of `rev`:

1. Let $f_0(\phi, \varphi)(g) = J_1(\Theta_\phi(g, \cdot)\,\varphi)$ be the theta lift of $\varphi$ to $\mathrm{SL}_2$ over $\mathbb{Q}$. Suppose $f_0(\phi, \varphi) = 0$ for all Fock $\phi$.
2. By `thetaConstantTerm_eq`, $f_0$ equals the part of the theta sum over $\xi$ with $q(\xi) \neq 0$. By `Coef`, its Fourier coefficient at $t$ is the volume of $\mathbb{Q}\backslash\mathbb{A}_\mathbb{Q}$ times the part over $\{q = t\}$. Take $t = q(X_0) = -\delta \neq 0$, with $X_0 = (0,0,0,1)$. The volume is nonzero, so the part over the orbit $\{q = q(X_0)\}$ vanishes at $g = 1$.
3. `CoefPer` turns this into $\mathrm{UPer}(\varphi(\cdot\,h)) = 0$ for all $h$. This contradicts the hypothesis, so $f_0(\phi, \varphi) \neq 0$ for some $\phi$.
4. `ThetaLiftIsBoundedCuspidal` says $f_0$ is continuous, bounded and cuspidal. `Dens` gives a $\pi$ and $f \in \pi$ whose integral against $f_0$ is nonzero. `Fub` exchanges the two integrals, which gives $J_1(\mathrm{lift}(f, \phi)\,\varphi) \neq 0$.

## In the Lean code

The theorem is at [line 28 of RevTop.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/SplitEigenfunctions/RevTop.lean#L28). `rev` is at [line 8 of Rev.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/SplitEigenfunctions/Rev.lean#L8). The Props and `UPer`, `qr`, `f0` and `Rev` are in [ThetaLiftEqAnisotropicPart.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/SplitEigenfunctions/ThetaLiftEqAnisotropicPart.lean#L163).

We read the proof of `rev` but not the proofs of `coef`, `coefPer`, `dens`, `fub` and `thetaPairing_constantTerm_cuspidal`. `CoefPer` uses `orbS`, `orbFn` and `momKill` (Fock vectors detect integrals against a weight).
