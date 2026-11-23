---
id: thm-a-limit
title: The reflection sum of the height polynomial
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.PB.thmA_limit
module: Development.AutomorphicSpectrum.Proofs.MetricProofs.HeightPolynomialReflectionSum
covers: 406
status: drafted
drafted_by: writer@claude
---
This theorem computes the sum of the height polynomial of a realization at two points that are symmetric along a direction $\varepsilon$, when a square system exists for $\varepsilon$. The answer is an explicit series in the degree polynomial with the constants $\kappa_k$. The [statement form](/entry/height-polynomial-reflection-sum/) repeats it, and [the adjacent swap relation](/entry/thm-a-swap/) applies it with $\varepsilon = \xi_{\tau,a}$.

## Statement

Let $\mathrm{SY}$ be an analytic system of dimension $d + 1$ over a finite set $\sigma$: a compact complex space $X$ and, for each $a \in \sigma$, a potential $\theta_a$, a singular weight $\varphi_a$ and a regularization $\varphi_{a,t}$ for $0 < t \leq t_0$. Let $\mathrm{Re}$ be a realization of $\mathrm{SY}$ on an arithmetic variety $P$ of dimension $d + 2$: a log resolution with a map $\pi$ of degree $\deg$ to $X$, and hermitian lines $\bar L_a(t)$ whose metrics are the reference metrics times $e^{-\varphi_{a,t} \circ \pi}$. Let $I$ be a full intersection system. For $w \colon \{0, \dots, d+1\} \to \sigma$ put

$$\ell(w) = \lim_{t \to 0^+} \frac{I(\bar L_{w_0}(t), \dots, \bar L_{w_{d+1}}(t))}{\deg}, \qquad \mathrm{PB}(x) = \sum_w \ell(w) \prod_j x_{w_j}.$$

Let $\delta(w)$ be the mixed integral (`mInt`) of $\theta_{w_0}, \dots, \theta_{w_d}$, and $\mathrm{Deg}(x) = \sum_w \delta(w) \prod_j x_{w_j}$. Let $\kappa_k$ be the double integral over $S^2 \times S^2$ of $-\tfrac12 \log\frac{1 - n_1 \cdot n_2}{2}$ times a fixed polynomial in the third coordinates.

**Theorem.** Assume `Inputs` (a conjunction of 17 analytic and arithmetic statements) and `FibreLocal.Statement`. Let $Q$ be a square system for $\mathrm{Re}$ at $a_0$ with coefficients $\varepsilon \colon \sigma \to \mathbb{Z}$. If $c \colon \sigma \to \mathbb{R}$ has $c(a_0) = 0$, then for every real $u$

$$\mathrm{PB}\bigl(c - \tfrac{u}{2}\varepsilon\bigr) + \mathrm{PB}\bigl(c + \tfrac{u}{2}\varepsilon\bigr) = \sum_{n \text{ odd}} (d+2)\, \frac{\kappa_{(n+1)/2}}{(n+1)/2}\, \bigl[u^n\bigr] \mathrm{Deg}\bigl(c - \tfrac{u}{2}\varepsilon\bigr)\; u^{n+1}.$$

`FibreLocal.Statement` contains the formula $\kappa_k = \tfrac12 \sum_{j<k} \frac{1}{2j+1}$. It is proved (`FibreLocal.proof`), and the caller supplies it.

## Proof

Write $\mathrm{pol}(f; c_0, \dots, c_{n-1}) = \sum_w \prod_r c_r(w_r)\, f(w)$ for the multilinear form of a coefficient function $f$.

1. `polar_identity_from_symmetric_forms` is the algebra. For symmetric $f$ in $d+2$ slots and $g$ in $d+1$ slots, it gives the identity above (with $f, g$ in place of $\ell, \delta$) from two coefficient identities for each integer vector $n$ with $n(a_0) = 0$: $\mathrm{pol}(f; n, \dots, n) = 0$, and $\mathrm{pol}(f; \varepsilon^{2k}, n, \dots) = -2\kappa_k\, \mathrm{pol}(g; \varepsilon^{2k-1}, n, \dots)$ for $1 \leq k$, $2k \leq d+2$.
2. Symmetry: `Realis.limNum_perm` (from the full intersection system) for $\ell$, and `AnSys.degNum_perm` for $\delta$.
3. At each scale $t \leq t_0(Q)$, `square_system_polar_vanishing` gives the first identity for the numbers at scale $t$, and gives the second one with the right side a sum of mixed integrals on the square $W$ of $Q$ against its function $g_t$.
4. As $t \to 0^+$, `agreement_positive` gives the convergence of the numbers to $\ell$, and `analytic_square_regularized_convergence` the convergence of the integrals on $W$.
5. `square_polar_integral_identity` evaluates the limit integrals as $2\kappa_k\,\mathrm{pol}(\delta; \dots)$. This is the one use of `FibreLocal.Statement`.

Uniqueness of limits gives the two identities.

## In the Lean code

The theorem is in [HeightPolynomialReflectionSum.lean](lean:Development/AutomorphicSpectrum/Proofs/MetricProofs/HeightPolynomialReflectionSum.lean#L41). The polynomial $\mathrm{PB}$ is `Realis.PB`, $\mathrm{Deg}$ is `AnSys.degPoly`, the series is `tsgPoly (d + 1) kappa (linePoly c ε SY.degPoly)` and $\kappa$ is `kappa` in [KappaSt.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/ArithmeticIntersection/KappaSt.lean#L21). The five `GlobalTheory.T` lemmas of the proof are statement forms that call other lemmas; we have not unfolded those. The square system $Q$ is used only through its analytic square `Q.an` and through `square_system_polar_vanishing`.
