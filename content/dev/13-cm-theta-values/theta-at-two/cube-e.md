---
id: cube-e
title: The coboundary of the two-torsion theta logarithm is biadditive up to units
kind: theorem
decl: Formalism.L2.Th1.B.cubeE
module: Formalism.LocalToGlobal.TorsionIntegrality.FrobeniusFibreCurves.FinalE
covers: 323
status: drafted
drafted_by: writer@claude
---
This theorem says that the coboundary of $\phi_T$, the logarithm of the theta function at a two-torsion point, is symmetric and additive in each variable up to integral units. It gets this from the same fact for the sigma function. Its only user is [`th0Vanish`](/entry/th0-vanish/).

## Statement

The notation ($\simeq$, $P$, $F$, $l$, $\varepsilon$, $a_1$, $(x_T, y_T)$, $e_1$, $\kappa$, $w$) is that of [`th0Vanish`](/entry/th0-vanish/), with its hypotheses 1 to 4 (`IsWp`, `LawLog`, `IsInv`, `CurveHyp`, `CurveHyp3`, `TwoHyp`). Let

$$\phi_T = -\Sigma_1(l) + \tfrac{s_2}{2}\,l^2, \qquad \Sigma_1 = -\iint (e_1 + \kappa w).$$

For $\phi \in K[[t]]$ set $c(X,Y) = \phi(F(X,Y)) - \phi(X) - \phi(Y)$ and $(d_1c)(X,Y,Z) = c(F(X,Y),Z) - c(X,Z) - c(Y,Z)$.

**Theorem.** For $\phi = \phi_T$:

1. every monomial of $c$ with a nonzero coefficient contains both $X$ and $Y$;
2. $c(Y,X) = c(X,Y)$;
3. $d_1c \simeq 0$;
4. $d_1$ of $c(Y,X)$ is $\simeq 0$.

Part 4 follows from parts 2 and 3. By symmetry, part 3 also gives additivity in the second variable.

## Proof

Let $\phi_O = -\sigma_S(l) + \tfrac{s_2}{2}l^2 - \log(l/t)$ with $\sigma_S = -\iint P$. Then $\exp(-\phi_O(t)) = \sigma(l(t))\exp(-s_2l(t)^2/2)/t$, where $\sigma = z\exp(\sigma_S)$ is the sigma series.

1. `cobRules` gives parts 1 and 2 for every $\phi$ with $\phi(0) = 0$.
2. `first_level_all_formal_groups` gives $d_1$ of the coboundary of $\phi_O$ $\simeq 0$.
3. `beESim` gives $c_{\phi_T} \simeq c_{\phi_O}$. Its proof (`BeESim_of`) uses two identities. `GCob` is an addition formula for $g_T = \varepsilon - x_Tt^2$. `LDiv` writes $Xh(Y) + Yh(X) - a_1XY = F\nu$ with $\nu$ integral and $\nu(0,0) = 1$, where $h = (\varepsilon + y_Tt^3)/g_T$. Taking logarithms gives $c_{\phi_T} - c_{\phi_O} = \log\nu - \log\delta$ with $\delta = 1 - \kappa\,w(l(X))\,w(l(Y))$.
4. `cocycle_diff_exp_equiv`: if $F$ is integral with $F(0,0) = 0$, then $H \simeq H'$ implies $d_1H \simeq d_1H'$.
5. Transitivity of $\simeq$ gives part 3.

## In the Lean code

The theorem is at [FinalE.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/FinalE.lean#L15): `BeE.CubeE_of beESim first_cocycle_simeq_zero`. `CubeE_of` is in [CocycleDiffExpEquiv.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/LogarithmicSubstitution/CocycleDiffExpEquiv.lean#L166), and the statement `CubeE` is in [StatementE.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/StatementE.lean#L72). $\phi_T$ is `phE` in [CurveHyp.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/CurveHyp.lean#L78), and $d_1$, `DivAB`, `swap2` are in [IsLawOfLog.lean](lean:Formalism/ThetaLogCoordinates/UniformThetaSubstitution/IsLawOfLog.lean#L21).

- `first_cocycle_simeq_zero` (same file, line 14) is a second name for `cocycle_diff_exp_equiv`. Its name says that a cocycle is $\simeq 0$; its statement is the transfer of $\simeq$ through $d_1$.
- There is no hypothesis $|2| = 1$, unlike the sibling statement `Cube` in StatementB.lean. The proof goes through $\phi_O$, not through the parallelogram law.
- We have not opened the proofs of `first_level_all_formal_groups`, `cobRules`, `GCob_of` and `LDiv_of`.
