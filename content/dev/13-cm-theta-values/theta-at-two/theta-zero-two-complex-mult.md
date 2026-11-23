---
id: theta-zero-two-complex-mult
title: The theta function at a 2-torsion point is 2-adically integral, CM case
kind: theorem
decl: Formalism.L2.Th1.B.LCm.theta_zero_two_complex_mult
module: Formalism.LocalToGlobal.TorsionIntegrality.FrobeniusFibreCurves.LogarithmicSubstitution.ThetaZeroTwoComplexMult
covers: 606
status: drafted
drafted_by: writer@claude
---
This theorem proves `ThetaZeroTwoCM`, which [its second name](/entry/th0-two-cm/) passes up to [integral jets at the prime 2](/entry/integral-operator-two-orthogonal/). It is the case $\alpha = \omega_K$ of [the trace form](/entry/theta-zero-two-adic-trace/), which has the real content.

## Statement

Use the notation of [integral jets at the prime 2](/entry/integral-operator-two-orthogonal/): the lattice $L$, its constant $s_2$, the operators $U_x$, the function $\theta_0$ attached to $\omega_0$, the isomorphism $\iota \colon \mathbb{C} \to \mathbb{C}_2$ and the curve $W$. Let $\lambda$ be the formal logarithm of $W$. For $f$ holomorphic near $0$, let $f^\lambda \in \mathbb{C}_2[[z]]$ be the image under $\iota$ of the Taylor series of $f$ at $0$, composed with $\lambda$ (the Lean `inW`).

Let $x_T = \iota(\wp(\omega_0/2)) - b_2/12$, the $x$-coordinate on $W$ of the point $\omega_0/2$. Put $e_1 = x_T + b_2/12$, $\kappa = 3e_1^2 - g_2(W)/4$, and $w = z^2/(1 + z^2 P - e_1 z^2)$, where $P$ is the regular part of the $\wp$-series of $W$. Let $\Phi$ be the series with $\Phi(0) = \Phi'(0) = 0$ and $\Phi'' = e_1 + \kappa w$. The even sigma log series is $\varphi = \Phi(\lambda) + \tfrac{1}{2}\iota(s_2)\lambda^2$.

**Theorem.** Let $d \equiv 7 \pmod 8$, $\omega_K = (1 + \sqrt{-d})/2$, $\omega_K L \subseteq L$, and let $W$ have integral coefficients, $|\Delta(W)| = 1$, $|a_1(W)| = 1$ and the invariants $\iota(g_2(L)), \iota(g_3(L))$. Let $\omega_0 \in L$ with $\omega_K \omega_0/2 \notin L$ and $\bar\omega_K \omega_0/2 \notin L$. Then:

1. $\varphi(0) = 0$ and $\exp(\varphi)$ has integral coefficients;
2. $\theta_0^\lambda$ has constant term $1$ and integral coefficients;
3. for odd $M > 0$ and $s$ with $M s \in L$, $(U_s \theta_0)^\lambda$ has integral coefficients, and one of them has norm $1$.

## Proof

Write $d = 8k + 7$. Then $\omega_K + \bar\omega_K = 1$, which is odd, and $\omega_K \bar\omega_K = (1 + d)/4 = 2k + 2$, which is even. The hypothesis $\omega_K L \subseteq L$ is the hypothesis `MulStable` for $\alpha = \omega_K$. So `theta_zero_two_adic_trace`, with $\alpha = \omega_K$, $T = 1$ and $N = 2k + 2$, gives the three claims. The rest is a computation of $\bar\omega_K$ (`conj_omegaK`).

## In the Lean code

The theorem is in [ThetaZeroTwoComplexMult.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/LogarithmicSubstitution/ThetaZeroTwoComplexMult.lean#L102). The statement `ThetaZeroTwoCM` is in [StatementL.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/StatementL.lean#L34), and $\varphi$ is `evenSigmaLogAtTwoTorsion` in [StatementW.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/StatementW.lean#L27). Claim 1 is written `Simeq φ 0`, which means: constant term $0$ and integral exponential. Claim 2 is `OneUnit`, claim 3 is `GaussOne`.

The congruence $d \equiv 7 \pmod 8$ is used only to make the norm of $\omega_K$ even.
