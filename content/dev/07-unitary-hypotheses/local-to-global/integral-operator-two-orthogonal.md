---
id: integral-operator-two-orthogonal
title: Integral jets of translated theta functions at the prime 2
kind: theorem
decl: Formalism.L2.Th1.Top.integral_operator_two_orthogonal
module: Formalism.LocalToGlobal.TorsionIntegrality.UniformGaussModels.OrthogonalGaussModels.IntegralOperatorTwoOrthogonal
covers: 614
status: drafted
drafted_by: writer@claude
---
This theorem proves a 2-adic integrality statement for the Taylor coefficients of sums of products of translated theta functions of a CM lattice. It is `IntOpTwoOrth_of` applied to `th0TwoCM`, the one-variable statement at the prime 2. Its only user is [the jets at 2](/entry/jets-two-of/), which takes the first half of its conclusion for each translate.

## Statement

Let $L \subset \mathbb{C}$ be a lattice and $d \equiv 7 \pmod 8$ with $\omega_K L \subseteq L$, where $\omega_K = (1 + \sqrt{-d})/2$. Let $\sigma$ be the Weierstrass sigma function of $L$, $\sigma^*(z) = \sigma(z) e^{-s_2 z^2/2}$ for a constant $s_2$ of $L$, and $H(z, x) = z \bar{x} / \mathrm{area}(L)$. For $x \in \mathbb{C}$ let

$$(U_x F)(z) = F(z + x) \, e^{-\pi H(z, x) - \pi H(x, x)/2}.$$

Let $\omega_0 \in L$ with $\omega_K \omega_0/2 \notin L$ and $\bar\omega_K \omega_0/2 \notin L$, and let $\theta_0(z) = (U_{\omega_0/2}\sigma^*)(z) / (U_{\omega_0/2}\sigma^*)(0)$.

Let $\iota \colon \mathbb{C} \to \mathbb{C}_2$ be a field isomorphism and $W$ a Weierstrass curve over $\mathbb{C}_2$ with $g_2(W) = \iota(g_2(L))$ and $g_3(W) = \iota(g_3(L))$, integral coefficients, $|\Delta(W)| = 1$ and $|a_1(W)| = 1$.

**Theorem.** Let $r_k \in \mathbb{C}_2$ with $|r_k| \le 1$ ($k$ in a finite set), let $N$ be odd and positive, and let $s_{k,i} \in \mathbb{C}$ with $N s_{k,i} \in L$ ($i$ in a finite set). Let $\Theta \in \mathbb{C}_2[[z_i]]$ be the image under $\iota$ of the Taylor series at $0$ of
$$\sum_k r_k \prod_i (U_{s_{k,i}} \theta_0)(z_i).$$
Then $|\kappa! \, c_\kappa(\Theta)| \le 1$ for every multi-index $\kappa$, and $\bigl|\sum_\kappa p_\kappa \, \kappa! \, c_\kappa(\Theta)\bigr| \le 1$ for every polynomial $P = \sum p_\kappa z^\kappa$ with $|p_\kappa| \le 1$.

In words: all partial derivatives of $\Theta$ at $0$ are 2-adically integral, and so is the value at $0$ of $P(\partial)\Theta$.

## Proof

Let $\lambda$ be the formal logarithm of $W$ (the integral of its invariant differential) and $e$ its compositional inverse.

1. `th0TwoCM` gives, for each odd torsion translate, that $U_{s}\theta_0$ composed with $\lambda$ is a power series with coefficients in the unit ball (the Lean `GaussOne`).
2. `E.prodInt` shows that the sum of products of these series, with the $r_k$, has integral coefficients.
3. Substituting $e(z_i)$ for each variable undoes $\lambda$ and gives back $\Theta$ (`KJ.toZ_thetaProd`).
4. The invariant differential has integral coefficients and constant term $1$ (`coeffMem`, `logSpec`). So `G.jetsIn_toZ` shows that this substitution sends integral series to series with integral jets $\kappa! c_\kappa$. `G.jets_in_norm_holds` turns this into the norm bound.
5. The bound for $P$ follows because the unit ball is a ring.

We did not open the proofs of `th0TwoCM` or `jetsIn_toZ`.

## In the Lean code

The theorem is in [IntegralOperatorTwoOrthogonal.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/UniformGaussModels/OrthogonalGaussModels/IntegralOperatorTwoOrthogonal.lean#L54), with `IntOpTwoOrth_of` at line 15. `IntOpTwoOrth` is in [StatementH.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/UniformGaussModels/StatementH.lean#L13), `ThetaZeroTwoCM` in [StatementL.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/StatementL.lean#L34), and `jetsIn_toZ` in [ThetaZeroJetsCurveHolds.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/RamifiedCurveKernels/PairedSquareJets/ThetaZeroJetsCurveHolds.lean#L202).

Odd points:

- Nothing in the statement is orthogonal. The word comes from the folder name. "Two" is the prime 2, and "integral operator" refers to the second conclusion, $P(\partial)\Theta(0)$.
- The proof uses only the third part of `ThetaZeroTwoCM`; the first two parts are discarded.
- The user `jets_two_of` takes only the first conclusion (`.1`). The second conclusion is not used there.
- `intOpTwoOrth` in [OneLetterGaussSharpTranslateHolds.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/UniformGaussModels/OneLetterGaussSharpTranslateHolds.lean#L134) is a second name for this theorem.
