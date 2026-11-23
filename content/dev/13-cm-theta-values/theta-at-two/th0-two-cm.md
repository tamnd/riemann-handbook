---
id: th0-two-cm
title: The theta function at a 2-torsion point is 2-adically integral, CM case (second name)
kind: theorem
decl: Formalism.L2.Th1.B.th0TwoCM
module: Formalism.LocalToGlobal.TorsionIntegrality.FrobeniusFibreCurves.FinalL
covers: 607
status: drafted
drafted_by: writer@claude
---
This theorem is a second name. Its proof is the term `LCm.theta_zero_two_complex_mult`, and the statement and proof are in [the CM case at 2](/entry/theta-zero-two-complex-mult/). [Integral jets at the prime 2](/entry/integral-operator-two-orthogonal/) uses the third part of its conclusion.

## Statement

`ThetaZeroTwoCM`. Let $d \equiv 7 \pmod 8$ and let $L$ be a lattice with $\omega_K L \subseteq L$, $\omega_K = (1 + \sqrt{-d})/2$. Let $\iota \colon \mathbb{C} \to \mathbb{C}_2$ and the Weierstrass curve $W$ be as in [the parent entry](/entry/integral-operator-two-orthogonal/): $W$ has the invariants $\iota(g_2(L)), \iota(g_3(L))$, integral coefficients, unit discriminant and $|a_1| = 1$. Let $\omega_0 \in L$ with $\omega_K \omega_0/2 \notin L$ and $\bar\omega_K \omega_0/2 \notin L$. Then:

1. the even sigma log series $\varphi$ at the point $\omega_0/2$ has constant term $0$ and $\exp(\varphi)$ has integral coefficients;
2. $\theta_0 \circ \lambda$ has constant term $1$ and integral coefficients, where $\lambda$ is the formal logarithm of $W$;
3. for each odd $M > 0$ and $s$ with $M s \in L$, the series $(U_s \theta_0) \circ \lambda$ has integral coefficients, and one of them has norm $1$.

The objects are defined in [the CM case at 2](/entry/theta-zero-two-complex-mult/).

## Proof

The proof is one line: `LCm.theta_zero_two_complex_mult`.

## In the Lean code

The theorem is in [FinalL.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/FinalL.lean#L5). `ThetaZeroTwoCM` is in [StatementL.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/StatementL.lean#L34).
