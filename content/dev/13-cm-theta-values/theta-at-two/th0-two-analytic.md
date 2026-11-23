---
id: th0-two-analytic
title: The analytic step at 2, with its four inputs filled in
kind: theorem
decl: Formalism.L2.Th1.B.th0TwoAnalytic
module: Formalism.LocalToGlobal.TorsionIntegrality.FrobeniusFibreCurves.FinalJ
covers: 483
status: drafted
drafted_by: writer@claude
---
This theorem is a pass-through. It applies [`An2.Th0TwoAnalytic_of`](/entry/th0-two-analytic-of/) to four facts that are proved elsewhere, and so proves `ThetaZeroTwoAnalytic` with no hypothesis. [The final step at 2](/entry/th0-two-final-of/) uses it for the first two integrality claims. The real content is in [the analytic step](/entry/th0-two-analytic-of/).

## Statement

`ThetaZeroTwoAnalytic`. Use the notation of [the CM case at 2](/entry/theta-zero-two-complex-mult/) and of [the final step at 2](/entry/th0-two-final-of/). Let $W$ have integral coefficients and the invariants $\iota(g_2(L)), \iota(g_3(L))$. Let $\alpha \ne 0$ with $\alpha L \subseteq L$, $\iota(\alpha) = b$, $\iota(\bar\alpha) = b'$ with $b, b' \in \mathbb{Z}_2$, $|b| = 1$, $|b'| < 1$. Let $\omega_0 \in L$ with $\omega_0/2 \notin L$. Suppose that $2z \notin L$ and $|x(P(z))| \le 1$ for every $z$ with $\alpha z - \omega_0/2 \in L$, and that $|x(P(\omega_0/2))| \le 1$. Then $\varphi(0) = 0$ with $\exp(\varphi)$ integral, and $\theta_0^\lambda$ is $1$ plus an integral series.

## Proof

The proof is one line:

```
An2.Th0TwoAnalytic_of halfFibreExists fibreZInstance halfShiftSeries fibreMap
```

The four inputs are second names, in the same file, for:

- `Half.half_fibre_exists_holds`: representatives of the solutions of $\alpha Q \equiv \omega_0/2 \pmod L$ up to sign exist;
- `Fib.fibre_integer_instance_holds`: the isogeny identity of power series over these representatives;
- `Fib.half_shift_series_holds`: the series of $\wp(z + \omega_0/2)$;
- `Half.fibre_map_holds`: the identity survives a ring map such as $\iota$.

[The analytic step](/entry/th0-two-analytic-of/) states each of them.

## In the Lean code

The theorem is in [FinalJ.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/FinalJ.lean#L13), and `ThetaZeroTwoAnalytic` in [StatementJ.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/StatementJ.lean#L51). The same file also defines `pointsIntTwo`, which this proof does not use.
