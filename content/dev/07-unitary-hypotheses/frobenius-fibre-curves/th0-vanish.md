---
id: th0-vanish
title: The theta function at a two-torsion point is a one-unit
kind: theorem
decl: Formalism.L2.Th1.B.th0Vanish
module: Formalism.LocalToGlobal.TorsionIntegrality.FrobeniusFibreCurves.FinalI
covers: 370
status: drafted
drafted_by: writer@claude
---
This theorem is the formal part of [`Th0TwoAnalytic_of`](/entry/th0-two-analytic-of/), its only user. It works over any complete ultrametric field $K$ of characteristic $0$. It says that the theta function at a two-torsion point, written in the parameter of an integral formal group, is an integral series with constant term $1$. The user takes $K = \mathbb{C}_2$ and a lattice with complex multiplication by $\alpha$, and uses only the first conclusion.

## Statement

Notation. For power series $f, g$ over $K$, write $f \simeq g$ if $f - g$ has constant term $0$ and $\exp(f - g)$ has all coefficients in the unit ball $\mathcal{O}_K$. A series is *integral* if all its coefficients are in $\mathcal{O}_K$.

The data and hypotheses:

1. $P \in K[[z]]$ is even with $P(0) = 0$, and $\wp = z^{-2} + P$ satisfies $\wp'^2 = 4\wp^3 - g_2\wp - g_3$.
2. $F$ is an integral formal group law with logarithm $l$ ($l(0) = 0$, $l'(0) = 1$, $l(F(X,Y)) = l(X) + l(Y)$), integral formal inverse $i$, and compositional inverse $l^{-1}$.
3. `CurveHyp` and `CurveHyp3` tie $F$ to $\wp$: $\wp(l(t)) = c_0 + \varepsilon(t)/t^2$ with $\varepsilon$ integral and $\varepsilon(0) = 1$, and similar conditions with constants $a_1, a_3$.
4. `TwoHyp`: $(x_T, y_T)$ is a two-torsion point, $2y_T + a_1x_T + a_3 = 0$, $e_1 = x_T + c_0$ is a root of $4e^3 - g_2e - g_3$, and $x_T$, $y_T$, $a_1$, $\kappa = 3e_1^2 - g_2/4$ are integral.
5. `IsFibreZ`: points $c_Q$ ($Q$ in a finite set $\iota$) and series $w_Q^\pm$ with $\alpha^2\,\tau(\alpha z) = \sum_Q (w_Q^+ + w_Q^-) - S$, where $\tau = e_1 + \kappa w$ and $w = z^2/(1 + z^2P - e_1z^2)$, plus a second identity for each $Q$.
6. Scalars $\alpha, \bar\alpha$ with $\alpha\bar\alpha = 2|\iota|$ and $\alpha(\alpha - \bar\alpha)s_2 = S$, an integral multiplication by $\alpha$ on $F$, and integrality conditions on some binomial coefficients.

Over $\mathbb{C}$, $\tau(z) = \wp(z + \omega/2)$ when $e_1 = \wp(\omega/2)$, by the classical formula $\wp(z + \omega/2) = e_1 + (e_1 - e_2)(e_1 - e_3)/(\wp(z) - e_1)$ (Whittaker and Watson, *A Course of Modern Analysis*, Chapter XX). Let $\theta_T = \exp\bigl(-\iint \tau\bigr)\exp(-s_2z^2/2)$ and let $\phi_T$ be defined by $\theta_T(l(t)) = \exp(-\phi_T(t))$.

**Theorem.** $\phi_T \simeq 0$, the constant term of $\theta_T \circ l$ is $1$, and $\theta_T \circ l$ is integral.

## Proof

1. `phEDef` gives $\phi_T(0) = 0$ and $\theta_T \circ l = \exp(-\phi_T)$.
2. [`cubeE`](/entry/cube-e/) gives that the coboundary of $\phi_T$ is additive up to $\simeq$ in its first variable.
3. `first_level_from_universal_law` gives $F = l^{-1}(l(X) + l(Y))$, integrality of this law, and the additivity fact `F1`.
4. `phENorm` gives the norm relation `PhNormAt`: $\phi_T([\alpha]t)$ is congruent to $\alpha\bar\alpha\,\phi_T(t)$.
5. `split_vanishing_at_two` uses steps 3 and 4 and gives `LG`: $\exp(\phi_T)$ is integral.
6. `LG` is closed under negation, so $\exp(-\phi_T) = \theta_T \circ l$ is integral with constant term $1$.

## In the Lean code

The theorem is at [FinalI.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/FinalI.lean#L12): `Van.Th0Vanish_of cubeE phENorm`. The proof is `Th0Vanish_of` in [TwoAdicScalarConditions.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/LogarithmicSubstitution/TwoAdicScalarConditions.lean#L16). The statement `ThetaZeroVanishing` is in [StatementI.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/StatementI.lean#L45). The series $\phi_T$, $\theta_T$ are `phTw`, `thTw` in [IsFibreCurve.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/IsFibreCurve.lean#L17).

- `phENorm` is `Nrm.PhENorm_of th0Isogeny`, and `th0Isogeny` is `theta_zero_isogeny_holds`. We have not opened their proofs.
- There is no hypothesis $|2| = 1$, so the theorem applies to $K = \mathbb{C}_2$.
- The name says "vanishing". The conclusion is that $\phi_T$ is $\simeq 0$, which is an integrality statement, not that a series is zero.
- The only user keeps the first conclusion and proves the one-unit property again by `oneUnit_fExp_neg`.
