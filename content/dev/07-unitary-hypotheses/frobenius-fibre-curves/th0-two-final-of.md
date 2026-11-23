---
id: th0-two-final-of
title: Integrality of the theta function at 2 from the position of the half-period points
kind: theorem
decl: Formalism.L2.Th1.B.KFin.Th0TwoFinal_of
module: Formalism.LocalToGlobal.TorsionIntegrality.FrobeniusFibreCurves.LogarithmicSubstitution.LatticePointInKernelSubgroup
covers: 521
status: drafted
drafted_by: writer@claude
---
This theorem proves `ThetaZeroAtTwo`, the form of the three integrality claims that [the trace form](/entry/theta-zero-two-adic-trace/) uses once it knows $\iota(\alpha)$ and $\iota(\bar\alpha)$ in $\mathbb{Z}_2$. Its input is a statement about points: certain points of $W$ are not in the formal group. It turns this into bounds on $x$-coordinates and passes them to [the analytic step](/entry/th0-two-analytic/) and to `shiftAnalyticW`.

## Statement

Use the notation of [the CM case at 2](/entry/theta-zero-two-complex-mult/). For $t \in \mathbb{C}$ let $P(t)$ be the point of $W(\mathbb{C}_2)$ attached to $t$ (the Lean `ptW`). A point is in the formal group if it is $0$ or its $x$-coordinate has norm greater than $1$.

Fix $L$, $\iota$ and $W$ with integral coefficients, $|\Delta(W)| = 1$, $|a_1(W)| = 1$ and the invariants $\iota(g_2(L)), \iota(g_3(L))$. Fix $\alpha \ne 0$ with $\alpha L \subseteq L$, $\iota(\alpha) = b$ and $\iota(\bar\alpha) = b'$ for some $b, b' \in \mathbb{Z}_2$ with $|b| = 1$ and $|b'| < 1$, and $\omega_0 \in L$ with $\bar\alpha\omega_0/2 \notin L$.

`PointsTwoFinal` says that, under these hypotheses:

- (a) $P(\omega_0/2)$ is not in the formal group;
- (b) $P(Q)$ is not in the formal group when $\alpha Q - \omega_0/2 \in L$;
- (c) $2z \notin L$ when $\alpha z - \omega_0/2 \in L$.

`ThetaZeroAtTwo` says that, under the same hypotheses, the three claims of the CM case hold.

**Theorem.** `PointsTwoFinal` implies `ThetaZeroAtTwo`.

## Proof

1. A lattice point gives the zero point, which is in the formal group (`lattice_point_in_kernel_subgroup`). So (a) gives $\omega_0/2 \notin L$.
2. A point that is not in the formal group has $|x| \le 1$ (`Half.norm_x_le_one_of_not_in_kernel`, which holds by definition). So (a) gives $|x(P(\omega_0/2))| \le 1$, and (b) gives $|x(P(Q))| \le 1$ for each $Q$ with $\alpha Q - \omega_0/2 \in L$.
3. [`th0TwoAnalytic`](/entry/th0-two-analytic/), with these bounds and (c), gives claims 1 and 2: $\varphi(0) = 0$ with $\exp(\varphi)$ integral, and $\theta_0^\lambda$ is $1$ plus an integral series.
4. `Formalism.L2.Th1.E.shiftAnalyticW` gives claim 3 from claim 2 and $|x(P(\omega_0/2))| \le 1$: the translates $(U_s\theta_0)^\lambda$ by odd torsion $s$ are integral with a coefficient of norm $1$.

## In the Lean code

The theorem is in [LatticePointInKernelSubgroup.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/LogarithmicSubstitution/LatticePointInKernelSubgroup.lean#L269). Both statements are in [StatementK.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/StatementK.lean#L58), and `ShiftAnalyticW` is in [StatementW.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/TorsionTranslationPowers/StatementW.lean#L58).

The analytic step needs only integral coefficients of $W$ (`IntModel`), not $|\Delta(W)| = 1$; the proof drops the discriminant condition before the call. The file name refers to the helper `lattice_point_in_kernel_subgroup`, not to this theorem. `PointsTwoFinal` itself is proved in the same file by `PointsTwoFinal_of`.
