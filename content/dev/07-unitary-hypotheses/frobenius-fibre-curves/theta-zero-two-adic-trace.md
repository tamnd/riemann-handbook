---
id: theta-zero-two-adic-trace
title: The theta function at a 2-torsion point is 2-adically integral, for a multiplier of odd trace and even norm
kind: theorem
decl: Formalism.L2.Th1.B.LCm.theta_zero_two_adic_trace
module: Formalism.LocalToGlobal.TorsionIntegrality.FrobeniusFibreCurves.LogarithmicSubstitution.ThetaZeroTwoComplexMult
covers: 604
status: drafted
drafted_by: writer@claude
---
This theorem proves the three integrality claims of [the CM case at 2](/entry/theta-zero-two-complex-mult/) for any multiplier $\alpha$ of $L$ with odd trace and even norm. The CM case takes $\alpha = \omega_K$. The theorem does one thing itself: it shows that $\iota(\alpha)$ and $\iota(\bar\alpha)$ lie in $\mathbb{Z}_2$, one a unit and one not. Then it calls [the final step at 2](/entry/th0-two-final-of/).

## Statement

Use the notation of [the CM case at 2](/entry/theta-zero-two-complex-mult/): $L$, $\iota$, $W$, $\lambda$, $\theta_0$, $U_s$, $f^\lambda$ and the even sigma log series $\varphi$.

**Theorem.** Let $W$ have integral coefficients, $|\Delta(W)| = 1$, $|a_1(W)| = 1$ and the invariants $\iota(g_2(L)), \iota(g_3(L))$. Let $\alpha \in \mathbb{C}$ with $\alpha L \subseteq L$, $\alpha + \bar\alpha = T$ and $\alpha\bar\alpha = N$ for integers $T$ odd and $N$ even. Let $\omega_0 \in L$ with $\alpha\omega_0/2 \notin L$ and $\bar\alpha\omega_0/2 \notin L$. Then the three claims of the CM case hold: $\varphi(0) = 0$ with $\exp(\varphi)$ integral; $\theta_0^\lambda$ is $1$ plus an integral series; and $(U_s\theta_0)^\lambda$ is integral with a coefficient of norm $1$ when $Ms \in L$ for an odd $M > 0$.

## Proof

1. The polynomial $x^2 - Tx + N$ has roots $b, b' \in \mathbb{Z}_2$ with $|b| = 1$ and $|b'| < 1$ (`quadratic_two_adic_holds`). This is Hensel's lemma at $x = 0$: $|N| < 1 = |T|^2$. The root near $0$ is $b'$, and $b = T - b'$ is a unit.
2. $\iota(\alpha)$ and $\iota(\bar\alpha)$ are the two roots of the same polynomial in $\mathbb{C}_2$. So $\{\iota(\alpha), \iota(\bar\alpha)\} = \{b, b'\}$ (`roots_two_adic_holds`).
3. If $\iota(\alpha) = b$, apply `ThetaZeroAtTwo` to $\alpha$, with the hypothesis $\bar\alpha\omega_0/2 \notin L$. If $\iota(\alpha) = b'$, apply it to $\bar\alpha$, with the hypothesis $\alpha\omega_0/2 \notin L$. Here $\bar\alpha = T - \alpha$ also maps $L$ into $L$ (`mulStable_conj`), and $\alpha \ne 0$ because $T$ is odd.
4. `ThetaZeroAtTwo` is [`KFin.Th0TwoFinal_of`](/entry/th0-two-final-of/) applied to `PointsTwoFinal_of`. Its inputs are `KernelIntegral` (from `KKer.KernelIntegral_of` and four facts of [StatementK.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/StatementK.lean#L17): uniqueness of a 2-torsion point in the formal group, a norm bound for 2-power torsion, a norm identity for $3x^2 - g_2/4$, and a sum of $\wp$ over the kernel of $\alpha$), the consequence `kernel_stable_of_integral_kernel`, and `two_torsion_kernel_unique_holds`.

`KernelIntegral` says: if $\iota(\alpha)$ is a unit $b$ of $\mathbb{Z}_2$ and $t \notin L$ with $\alpha t \in L$, then the point of $W$ attached to $t$ is not in the formal group: it is not $0$, and its $x$-coordinate has norm at most $1$.

## In the Lean code

The theorem is in [ThetaZeroTwoComplexMult.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/LogarithmicSubstitution/ThetaZeroTwoComplexMult.lean#L77). `ThetaZeroTwoTrace` is in [StatementL.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/StatementL.lean#L24), and `ThetaZeroAtTwo`, `KernelIntegral`, `PointsTwoFinal` are in [StatementK.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/StatementK.lean#L46). Step 1 calls Mathlib's `hensels_lemma`.

The word "trace" in the name refers to the hypothesis that $\alpha + \bar\alpha$ is odd. No trace map appears in the statement.
