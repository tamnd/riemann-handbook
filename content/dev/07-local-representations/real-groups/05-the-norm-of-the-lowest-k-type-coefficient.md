---
title: The norm of the lowest K-type coefficient
decls:
  - CompanionTheory.RgFd.psiNorm
  - CompanionTheory.RgFd.explicit_function_square_integrable
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The norm of the lowest K-type coefficient

For a Harish-Chandra parameter $\lambda$ of $U(p,q)$ there is an explicit operator-valued function $\Psi$ on the group, built from leading principal minors and averaged over $K$. When $\lambda$ is far from the walls between the two blocks, $\Psi$ is the matrix coefficient of the lowest $K$-type of a discrete series, and its $L^2$ norm is given by the formal degree. This section proves the norm formula for every Harish-Chandra parameter, by an induction that moves $\lambda$ far from the walls and comes back with a moment argument. As a corollary, $\Psi$ is square integrable for every Haar measure. Both facts are used in the step [EveryCharacter from the literature and VWin](/step/every-character-of-literature/), to build the discrete series with a given parameter and to fix its formal degree.

Background: [discrete series](/learn/representations/#discrete-series), [discrete series and formal degrees](/learn/real-groups/#discrete-series-and-formal-degrees), [[Haar measure|VY0HXD3GC4]].

### The group, the $K$-types and the function $\Psi$

Fix $n \geq 0$ and a sign vector $\varepsilon \in \{+,-\}^n$ with $p$ plus and $q$ minus signs, and let $J_\varepsilon = \mathrm{diag}(\pm 1)$. The group $G_\varepsilon = U(J_\varepsilon)$ consists of the complex $n \times n$ matrices $g$ with $g^* J_\varepsilon g = J_\varepsilon$; it is $U(p,q)$. Its maximal compact subgroup is $K_\varepsilon$, the elements that commute with $J_\varepsilon$ (see [the Weyl dimension formula](/entry/weyl-for-k-closed/)). Let $\mathfrak{p}$ be the set of matrices $X$ in the Lie algebra of $G_\varepsilon$ with $X J_\varepsilon = -J_\varepsilon X$. Every $g \in G_\varepsilon$ is $g = k \exp X$ with $k \in K_\varepsilon$ and $X \in \mathfrak{p}$, uniquely (the Cartan decomposition). Let $dk$ be the Haar measure on $K_\varepsilon$.

**Definition 2.5.1 ($K$-type with a highest vector).** A *$K$-type of highest weight $\Lambda$* is a finite-dimensional complex Hilbert space $V$ with a continuous irreducible unitary representation $\tau$ of $K_\varepsilon$, its derivative $d\tau$ on the Lie algebra of $K_\varepsilon$ (extended complex-linearly), and a unit vector $w \in V$ with $d\tau(E_{aa}) w = \Lambda_a w$ for all $a$ and $d\tau(E_{ab}) w = 0$ for $a < b$ in the same block.

Let $\rho(n)_a = \tfrac{n-1}{2} - a$. For a Harish-Chandra parameter $\lambda$ (strictly decreasing, with $\lambda_a - \tfrac{n-1}{2} \in \mathbb{Z}$; see [the previous section](/entry/h-alg-core/)) put $\mu = \lambda + \rho(n)$; it lies in $\mathbb{Z}^n$ and is strictly decreasing. Let $\Lambda = \lambda + \rho_n - \rho_c$ be the lowest $K$-type weight.

**Definition 2.5.2 (The function $\Psi$).** Let $\Delta_i(z)$ be the leading principal $i \times i$ minor of a matrix $z$, and put
$$\Phi_\mu(z) = \prod_{i<n} \Delta_{i+1}(z)^{-(\mu_i - \mu_{i+1})}, \qquad \mu_n = 0.$$
For a $K$-type $(V, \tau, w)$ of highest weight $\Lambda$, let $P_w$ be the orthogonal projection on $\mathbb{C} w$ and, for a matrix $x$,
$$\psi(x) = \frac{\dim V}{\mathrm{vol}(K_\varepsilon)} \int_{K_\varepsilon} \Phi_\mu(k^{-1} x k)\, \tau(k) P_w \tau(k)^{-1}\, dk.$$
Finally $\Psi(g) = \tau(k)\, \psi(\exp X)$ for $g = k \exp X$.

The function $\Phi_\mu$ is the classical highest weight function: on the open set where the leading minors do not vanish it transforms under upper and lower triangular matrices by characters. The average over $K$ with $\tau(k) P_w \tau(k)^{-1}$ turns it into a function with values in $\mathrm{End}(V)$ that is $\tau$-spherical on the left. For holomorphic discrete series it is a classical formula for the lowest $K$-type matrix coefficient.

**Definition 2.5.3 (The measure and the formal degree).** Let $\mu_{\mathrm{CD}}$ be the measure on $G_\varepsilon$ obtained from $dk \times (\text{Jacobian of the polar map})\, dX$ on $K_\varepsilon \times \mathfrak{p}$ by the map $(k, X) \mapsto k \exp X$, multiplied by
$$c_{p,q} = \frac{\prod_{i<n} i!}{\pi^{pq} \prod_{i<p} i! \prod_{i<q} i!}.$$
For $\lambda \in \mathbb{R}^n$ put
$$d(\lambda) = \prod_{a<b} \frac{|\lambda_a - \lambda_b|}{b - a}.$$
For $A \in \mathrm{End}(V)$ let $\|A\|_{\mathrm{HS}}^2 = \sum_i \|A e_i\|^2$, for an orthonormal basis $(e_i)$.

So $\mu_{\mathrm{CD}}$ is a Haar measure on $G_\varepsilon$ with a specific normalisation, and $d(\lambda)$ is the Weyl dimension formula of $U(n)$ evaluated at $\lambda$. By Harish-Chandra's formula, $d(\lambda)$ is the formal degree of the discrete series with parameter $\lambda$ for the measure $\mu_{\mathrm{CD}}$.

### The norm formula

**Theorem 2.5.4 (Norm of $\Psi$).** Let $\lambda$ be a Harish-Chandra parameter for $U(p,q)$, $(V, \tau, w)$ a $K$-type of highest weight $\Lambda = \lambda + \rho_n - \rho_c$, and $\mu = \lambda + \rho(n) \in \mathbb{Z}^n$. Then
$$\int_{G_\varepsilon} \|\Psi(g)\|_{\mathrm{HS}}^2\, d\mu_{\mathrm{CD}}(g) = \frac{(\dim V)^2}{d(\lambda)}.$$

Lean: `CompanionTheory.RgFd.psiNorm`.

The integral is taken in $[0, \infty]$; the formula shows that it is finite.

**Corollary 2.5.5 (Square integrability).** Under the same hypotheses, $g \mapsto \Psi(g)$ lies in $L^2(G_\varepsilon, \nu; \mathrm{End}(V))$ for every Haar measure $\nu$ on $G_\varepsilon$.

Lean: `CompanionTheory.RgFd.explicit_function_square_integrable`.

*Proof of the corollary.* The measure $\mu_{\mathrm{CD}}$ is a Haar measure, $\Psi$ is continuous, and the operator norm satisfies $\|A\|^2 \leq \dim V \cdot \|A\|_{\mathrm{HS}}^2$. So $\Psi \in L^2(\mu_{\mathrm{CD}})$ by the theorem. Two Haar measures differ by a positive constant. $\square$

### The proof

The proof has three cases: the compact case, the case of a large gap, and the general case by induction from the large gap.

**Lemma 2.5.6 (Large gaps).** Let $p, q \geq 1$. There is $h_0$ such that the norm formula holds for every Harish-Chandra parameter $\lambda$ with $|\lambda_a - \lambda_b| \geq h_0$ whenever $a, b$ lie in different blocks.

*Proof.* For such $\lambda$, the closed span in $L^2(G_\varepsilon)$ of the right translates of the vectors $\Psi(\cdot) v$ is a discrete series representation $\pi$, and the map $v \mapsto \Psi(\cdot) v$ is, up to a positive constant $C$, an isometric embedding of $V$ whose matrix coefficients are those of $\Psi$. The formal degree of $\pi$ for $\mu_{\mathrm{CD}}$ is $d(\lambda)$. The Schur orthogonality relations for square integrable representations then give $\int \|\Psi\|_{\mathrm{HS}}^2\, d\mu_{\mathrm{CD}} = (\dim V)^2 / d(\lambda)$. $\square$

*Proof of the theorem.* If $p = 0$ or $q = 0$, the group is compact and the formula is a direct computation, proved separately. So let $p, q \geq 1$, and let $h_0$ be as in the lemma.

Let $D \in \mathbb{Z}^n$ be $D_a = n - 1 - a$, and $\lambda_t = \lambda + t D$ for $t \in \mathbb{N}$. Then $\lambda_t$ is a Harish-Chandra parameter, $\mu_t = \mu + t D$, and $|(\lambda_t)_a - (\lambda_t)_b| \geq t$ for $a \neq b$. So the lemma applies to $\lambda_t$ for $t \geq \lceil h_0 \rceil$. Let $T_t$ and $T_D$ be $K$-types of highest weights $\Lambda_t$ and $D$.

By the Cartan decomposition and Schur orthogonality on $K$, the integral of $\|\Psi\|_{\mathrm{HS}}^2$ is $(\dim V)^2$ times an integral over $G_\varepsilon \times K \times K$ of
$$h(g, k_1, k_2) = \phi_\mu(g, k_1)\, \phi_\mu(g, k_2)\, |\langle w, \tau(k_1^{-1} k_2) w \rangle|^2,$$
where $\phi_\mu(g, k) = \Phi_\mu(k^{-1} \exp(X) k)$ is positive. Two multiplicativity facts hold: $\Phi_{\mu + tD} = \Phi_\mu \cdot \Phi_D^{\,t}$ on positive definite matrices, and $|\langle w_t, \tau_t(k) w_t \rangle| = |\langle w, \tau(k) w \rangle| \cdot |\langle w_D, \tau_D(k) w_D \rangle|^t$, because $w_t$ is the product of $w$ and $t$ copies of $w_D$ in the tensor product. So the integrand for $\lambda_t$ is $h \cdot U^t$, where $U$ is the integrand for $D$ with $\mu = D$; and $0 \leq U \leq 1$, because $\Phi_D(\exp X) \leq 1$ for $X \in \mathfrak{p}$.

The lemma gives, for $t \geq \lceil h_0 \rceil$,
$$\int h\, U^t = \frac{1}{d(\lambda_t)} = \frac{\prod_{a<b} (b - a)}{\prod_{a<b} \big((\lambda_a - \lambda_b) + t (b - a)\big)},$$
after the factor $(\dim T_t)^2$ is removed. We use a moment lemma: if $h \geq 0$ is measurable, $0 \leq U \leq 1$, and $\int h\, U^t = c / \prod_i (\alpha_i + t \beta_i)$ for all large $t$, with $\alpha_i > 0$ and $\beta_i \geq 0$, then $\int_{U > 0} h = c / \prod_i \alpha_i$. Here $\alpha_{ab} = \lambda_a - \lambda_b > 0$ and $\beta_{ab} = b - a$, so $\int_{U>0} h = 1/d(\lambda)$. Finally $h = 0$ almost everywhere on $\{U = 0\}$: there the coefficient of $T_D$ vanishes, and the coefficient of $T$ vanishes almost everywhere on the zero set of the coefficient of $T_D$. So $\int h = 1/d(\lambda)$, which is the formula. $\square$

The moment lemma is elementary. Let $m$ be the image of the measure $h\, d\mu$ under $U$, a measure on $[0, 1]$. For $\beta > 0$ one has $1/(\alpha + t\beta) = \beta^{-1} \int_0^1 u^{t} u^{\alpha/\beta - 1}\, du$, so $c / \prod_i (\alpha_i + t \beta_i) = \int_{(0,1]} u^t\, d\nu$ for an explicit finite positive measure $\nu$ on $(0, 1]$ (a convolution of such densities, times constants for the $\beta_i = 0$). The measures $u^{t_0} m$ and $u^{t_0} \nu$ on $(0,1]$ then have the same moments, so they agree by the Hausdorff moment theorem, and $m = \nu$ on $(0, 1]$. The mass of $\nu$ is its value at $t = 0$, which is $c / \prod_i \alpha_i$.

**Remark 2.5.7 (Formalization).** The inputs of the induction (the moment lemma, the two multiplicativity facts, the bound $\Phi_D \leq 1$, measurability and continuity) are separate statements assembled in [NormInductionOfEstimates.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/NormInductionOfEstimates.lean#L182); that module works in a namespace that copies the one of this section. The large-gap lemma is proved with results in a namespace named after the exceptional group $G_2$, although it concerns $U(p,q)$ ([GapNorm.lean](lean:CompanionTheory/RealGroups/FormalDegrees/ArchimedeanFormalDegrees/DegreeNormalization/GapNorm.lean#L19)). The function $\Psi$ is defined by choosing a polar decomposition, and is set to $0$ on matrices without one; for elements of $G_\varepsilon$ the decomposition exists.
