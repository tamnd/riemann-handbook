---
id: th0-two-analytic-of
title: The theta function at a 2-torsion point is 2-adically integral, from the isogeny identity
kind: theorem
decl: Formalism.L2.Th1.B.An2.Th0TwoAnalytic_of
module: Formalism.LocalToGlobal.TorsionIntegrality.FrobeniusFibreCurves.LogarithmicSubstitution.Th0TwoAnalyticOf
covers: 450
status: drafted
drafted_by: writer@claude
---
This theorem proves `ThetaZeroTwoAnalytic` from four facts about $\wp$. [Its user](/entry/th0-two-analytic/) supplies the four facts. The theorem builds, from the isogeny $\alpha$ of $\mathbb{C}/L$, one identity of power series over $\mathbb{C}_2$, collects the 2-adic scalar facts about $\iota(\alpha)$, and hands both to [`th0Vanish`](/entry/th0-vanish/), which does the 2-adic estimate.

## Statement

The conclusion `ThetaZeroTwoAnalytic` is stated in [the analytic step at 2](/entry/th0-two-analytic/). The hypotheses are:

- `HalfFibreExists`: if $\alpha \ne 0$, $\alpha L \subseteq L$, $\omega_0 \in L$, and $2z \notin L$ whenever $\alpha z - \omega_0/2 \in L$, there is a finite set $S_q$ of solutions of $\alpha Q \equiv \omega_0/2 \pmod L$ with one element from each class $\pm Q$.
- `FibreZInstance`: let $S$ represent the nonzero points of $\ker \alpha$ on $\mathbb{C}/L$, and let $T(z)$ be the Taylor series of $\wp(z + \omega_0/2)$. Then $2|S_q| = |S| + 1$, and
$$\alpha^2\, T(\alpha z) = \sum_{Q \in S_q} \bigl(\wp(z + Q) + \wp(z - Q)\bigr) - \sum_{P \in S} \wp(P),$$
and for each $Q$ the second logarithmic derivative of $z^2(\wp(z) - \wp(Q))$ is $2(\wp(z) - z^{-2}) - \wp(z+Q) - \wp(z-Q)$.
- `HalfShiftSeries`: $T = e_1 + \kappa\, w$ with $e_1 = \wp(\omega_0/2)$, $\kappa = 3e_1^2 - g_2/4$ and $w = 1/(\wp(z) - e_1)$, written as $z^2/(1 + z^2(\wp(z) - z^{-2}) - e_1 z^2)$.
- `FibreMap`: such an identity stays true after a ring map applied to all coefficients.

## Proof

1. Choose $S_q$ (`HalfFibreExists`) and $S$ (`kerRepsExist`). `FibreZInstance` and `HalfShiftSeries` give the identity over $\mathbb{C}$, and `FibreMap` moves it by $\iota$ to $\mathbb{C}_2$.
2. Rewrite it in terms of $W$. The image of $\wp(z) - z^{-2}$ is the $\wp$-series of $W$ (`weierstrass_series_eq_transported`). The $x$-coordinate of the point of $t$ is $\iota(\wp(t)) - b_2/12$ (`AnaSysW.px_ptW`). As $\wp'(\omega_0/2) = 0$, the point $(x_T, y_T)$ of $\omega_0/2$ has $2y_T + a_1x_T + a_3 = 0$, and `bridgeTwoMore` gives $|y_T| \le 1$.
3. The scalars. $\iota(\alpha)\iota(\bar\alpha) = |\alpha|^2 = |S| + 1 = 2|S_q|$ (`kerRepsCard`). $\iota(\alpha)(\iota(\alpha) - \iota(\bar\alpha))\iota(s_2) = \iota\bigl(\sum_{P \in S} \wp(P)\bigr)$ (`quasiPeriodConstIsogeny`). `twoAdicScalars` uses $|b| = 1$ and $|b'| < 1$: the series `mulBy` of multiplication by $b$, built from $\lambda$ and its inverse, is integral (we did not unfold `mulBy`), $b$ is a limit of integers, $b \ne b'$, $b' \ne 1$, and the binomial coefficients of $(b(b - b'))^{-1}$ and $(b(1 - b'))^{-1}$ are integral.
4. [`th0Vanish`](/entry/th0-vanish/) takes all of this, with the bounds $|x_T| \le 1$ and $|x(P(Q))| \le 1$, and gives claim 1: $\varphi(0) = 0$ and $\exp(\varphi)$ is integral.
5. `inWTh0` gives $\theta_0^\lambda = \exp(-\varphi)$. Then `oneUnit_fExp_neg` turns claim 1 into claim 2.

## In the Lean code

The theorem is in [Th0TwoAnalyticOf.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/LogarithmicSubstitution/Th0TwoAnalyticOf.lean#L25). The four hypotheses are in [StatementJ.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/StatementJ.lean#L17), and the identity is the predicate `IsFibreZ` in [IsFibreCurve.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/IsFibreCurve.lean#L23). `ThetaZeroVanishing`, the statement of `th0Vanish`, is in [StatementI.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/StatementI.lean#L45); we did not open its proof.

The statement asks only for integral coefficients of $W$, not for $|\Delta(W)| = 1$ or $|a_1(W)| = 1$. The hypothesis on $|x(P(z))|$ is used only for $z \in S_q$.
