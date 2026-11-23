---
title: The residue of the Siegel Eisenstein series
decls:
  - GlobalTheory.CompanionTheory.Jp.jPos_of_idemEx
  - PositivityTheory.Rg.Rsw.resCore
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The residue of the Siegel Eisenstein series

This section proves the main theorem of the chapter. Let $B$ be the sum of a Hermitian space $W$ of rank $r$ and $t$ hyperbolic planes, with $1 \le r < t$, and let $n = r + t$. The Siegel Eisenstein series on $G_n$ of a Siegel-Weil section from $B$ has at most a simple pole at $s = t/2$, and its residue lies in the closed span of the theta functions of $W$: each function that is orthogonal to all theta functions of $W$ is orthogonal to the residue. This is the regularised Siegel-Weil formula in the form that the proof uses. The theorem is used in the proof of the non-vanishing of the down lift, [Theorem 8.53 of Volume 15](/entry/down-ne-k-of-hypotheses-prime/), and in the last section.

We keep the notation of the earlier sections: $\psi$ is an additive character, $\chi$ a Hecke character, $\omega_V$ the Weil representations of the sixth section, $f_\Phi(g) = (\omega_B(g)\Phi)(0)$ the Siegel-Weil section of a Schwartz function $\Phi$ on $M_{m_B \times n}(\mathbb{A}_E)$, and $n(x) = \begin{pmatrix} 1 & x \\ 0 & 1 \end{pmatrix}$. Since $m_B = n + t$, the Levi formula of $\omega_B$ shows that $f_\Phi$ is a section of degree $t/2$ for $\chi$.

### Meromorphic continuation and Laurent coefficients

**Definition 5.7.1 (Continuation data).** Let $H$ be a height on $G_n$, $s_0 \in \mathbb{C}$ and $\varphi$ a function on $G_n$ with height family $f_z = H^{z - s_0} \varphi$. *Continuation data* for $(H, \varphi, s_0)$ are an open set $U \subset \mathbb{C}$, a polynomial $d \neq 0$, a function $E \colon U \times G_n \to \mathbb{C}$ and a real $\sigma$ such that:

1. $s_0 \in U$, $U$ contains a right half-plane, and $z + a \in U$ for $z \in U$ and $a \ge 0$;
2. $E$ is continuous, and $z \mapsto E(z, g)$ is holomorphic on $U$ for each $g$;
3. $E(z, \gamma g) = E(z, g)$ for $z \in U$ and $\gamma \in G_n(F)$;
4. $E(z, g) = d(z)\, E(f_z)(g)$ for $\operatorname{Re} z > \sigma$.

So $E/d$ is a meromorphic continuation of the Eisenstein series of the height family, and $d$ clears its poles. A real $\varepsilon > 0$ is a *radius* for the data if the closed disc of radius $\varepsilon$ about $s_0$ lies in $U$ and $d$ has no zero in it except perhaps $s_0$. For such $\varepsilon$ and $k \ge 1$ put
$$c_k(g) = \frac{1}{2\pi i} \oint_{|z - s_0| = \varepsilon} (z - s_0)^{k-1}\, \frac{E(z, g)}{d(z)}\, dz.$$
This is the coefficient of $(z - s_0)^{-k}$ in the Laurent expansion of $E(z, g)/d(z)$ at $s_0$. The function $c_1$ is the residue.

For a Schwartz function $\Psi$ on $M_{r \times n}(\mathbb{A}_E)$ the *theta function* of $W$ is
$$\theta_W(\Psi)(g, h) = \sum_{\xi \in M_{r \times n}(E)} (\omega_W(g)\Psi)(h^{-1}\xi), \qquad g \in G_n,\ h \in U(W)(\mathbb{A}).$$

### A cut at a good place

The proof kills the higher Laurent coefficients with a Hecke operator at one finite place. Let $v$ be a finite place. A *cut at $v$* is a finite set of Hermitian matrices $x \in \mathrm{Herm}_n(\mathbb{A}_E)$ that vanish at all places except $v$, with a complex coefficient $a_x$ for each. It acts on functions by $(CF)(g) = \sum_x a_x F(g\, n(x))$. The cut *kills rank below $r$* if
$$\sum_x a_x\, \psi(\tfrac12 \operatorname{tr}(x \beta)) = 0$$
for each $\beta \in \mathrm{Herm}_n(E)$ of rank less than $r$ such that $\psi(\tfrac12 \operatorname{tr}(y\beta)) = 1$ for every $y$ that vanishes outside $v$ and is integral at $v$. Let $K_v \subset G_n$ be the subgroup of elements of the standard maximal compact subgroup that equal $1$ outside $v$.

On functions with left $G_n(F)$-invariance, the cut multiplies the Fourier coefficient at $\beta$ by $\sum_x a_x \psi(\frac12 \operatorname{tr}(x\beta))$. So a cut that kills rank below $r$ kills each function whose Fourier coefficients are supported on rank less than $r$.

**Theorem 5.7.2 (Cut at a good place).** Assume the conclusion of the theorem on idempotents. Let $n = r + t$ with $r \ge 1$, $\psi$ an additive character, $\chi$ a Hecke character that satisfies the restriction condition for $r$, and $S$ a finite set of finite places. Then there are a finite place $v \notin S$, a cut $C$ at $v$ that kills rank below $r$, and an entire function $c$ with $c(t/2) \neq 0$, with the following property. For each Haar probability measure $\nu_v$ on $K_v$, each $z \in \mathbb{C}$ and each continuous section $f$ of degree $z$ for $\chi$ that is right invariant under $K_v$,
$$\int_{K_v} (Cf)(gk)\, d\nu_v(k) = c(z)\, f(g) \qquad \text{for all } g \in G_n.$$

Lean: `GlobalTheory.CompanionTheory.Jp.jPos_of_idemEx`.

*Proof.* We take three results as given. First, outside each finite set there is a place $v$ where $\psi$ is unramified in a suitable sense, $v$ splits in $E$, and $\chi$ satisfies a condition at $v$. Second, at such a split place there are a cut $C$ that kills rank below $r$ and an entire $c$ with $c(t/2) \neq 0$ such that the $K_v$-average of $C$ applied to the local spherical section of parameter $z$ is $c(z)$ times that section; this comes from a local computation at $v$. Third, a right $K_v$-invariant section of degree $z$ is, at $v$, a multiple of the local spherical section, so the local identity gives the global one. $\square$

### The residue theorem

**Theorem 5.7.3 (Residue of the Siegel Eisenstein series).** Let $B$ and $W$ have a hyperbolic decomposition with $t$ planes, $r = m_W$, $n = r + t$, and assume $1 \le r < t$ and $r + 2 < 2t$. Let $\psi$ be an additive character and $\chi$ a Hecke character that satisfies the restriction condition for $r$. Let $\omega_B$ and $\omega_W$ be Weil representations of $G_n$ for $\psi$ and $\chi$, for measures of covolume one. Let $H$ be a height on $G_n$ that is right invariant under an open subgroup of the finite part of $G_n$. Let $\Phi$ be a Schwartz function on $M_{m_B \times n}(\mathbb{A}_E)$, let $(U, d, E, \sigma)$ be continuation data for $(H, f_\Phi, t/2)$, and let $\varepsilon$ be a radius. Then:

1. $c_k = 0$ for every $k \ge 2$;
2. let $(X, \pi)$ be a finite measure space, $\gamma \colon X \to G_n$ measurable with relatively compact image, and $\kappa \in L^1(\pi)$; if
$$\int_X \theta_W(\Psi)(\gamma(x), h)\, \kappa(x)\, d\pi(x) = 0$$
for all Schwartz $\Psi$ on $M_{r \times n}(\mathbb{A}_E)$ and all $h \in U(W)(\mathbb{A})$, then $\int_X c_1(\gamma(x))\, \kappa(x)\, d\pi(x) = 0$.

Lean: `PositivityTheory.Rg.Rsw.resCore`.

*Proof.* The proof uses the results of the earlier sections and several inputs that we take as given. The first input is the *polar part identity*: for $k \ge 2$, the Fourier coefficients of $c_k$ vanish at all $\beta$ of rank at least $r$. It is proved from the [edge bound](/entry/sph-bound/), the [Fourier-Jacobi coefficient](/entry/rsw-fj-eis/), the [reduced sections](/entry/r-sec/), the [completeness of theta functions](/entry/rsw-th-total/), and inputs that we take as given. The second input says that only finitely many $c_k$ are nonzero, and that each $c_k$ is continuous and left $G_n(F)$-invariant.

Choose a finite set $S$ such that $H$ is right invariant under $K_v$ for $v \notin S$, such that $\omega_B$ fixes good Schwartz functions under $K^S$ (this uses the [generators](/entry/gen-k/) of the level subgroup), and such that $\Phi$ is good for $(S, e)$ for an $S$-idempotent $e$. Then $f_\Phi$ and $H$ are right invariant under $K_v$ for each $v \notin S$. The [Theorem 5.7.2](/entry/j-pos-of-idem-ex/) on a cut at a good place gives $v \notin S$, $C$ and $c$. Applied to the height family $H^{z - t/2} f_\Phi$, it shows that the $K_v$-average of $C E(z, \cdot)$ is $c(z) E(z, \cdot)$. Taking Laurent coefficients gives, for each $k \ge 1$ with $c_j = 0$ for all $j > k$,
$$\int_{K_v} (C c_k)(gk')\, d\nu_v(k') = c(t/2)\, c_k(g).$$

We show $c_k = 0$ for $k \ge 2$ by descending induction from the last nonzero coefficient. Let $k \ge 2$ with $c_j = 0$ for $j > k$. The function $c_k$ has Fourier coefficients only at rank less than $r$, by the polar part identity, so $C c_k = 0$ because $C$ kills rank below $r$. The displayed identity gives $c(t/2) c_k = 0$, so $c_k = 0$. This proves part 1.

For part 2, the case $k = 1$ of the identity holds now. Let $\Psi$ be the image of $\Phi$ under the map $\mathcal{I}$ of the fifth section and $\Psi' = \sum_x a_x\, \omega_W(n(x))\Psi$. An input that we take as given, the *cut identity*, gives a constant $\kappa'$ with
$$(C c_1)(g) = \kappa' \int_{\mathcal{F}} \theta_W(\Psi')(g, h)\, dh$$
for a fundamental domain $\mathcal{F}$ of $U(W)(F)$ in $U(W)(\mathbb{A})$. The cut identity rests on the residue functional: the [Theorem 5.6.3](/entry/eis-meas/) on the residue as an orbit integral and the [Theorem 5.5.6](/entry/column-splitting-main/) on the theta-side measure identify the Fourier coefficients of $c_1$ at rank $r$ with orbital integrals, and these are the Fourier coefficients of the theta integral. Bounds on $\theta_W(\Psi')$ for $g$ in a compact set allow Fubini's theorem. So
$$c(t/2) \int_X c_1(\gamma(x))\, \kappa(x)\, d\pi = \kappa' \int_{K_v} \int_{\mathcal{F}} \int_X \theta_W(\omega_W(k')\Psi')(\gamma(x), h)\, \kappa(x)\, d\pi\, dh\, d\nu_v(k'),$$
because $\theta_W(\Psi')(gk', h) = \theta_W(\omega_W(k')\Psi')(g, h)$. The inner integral is zero by hypothesis, and $c(t/2) \neq 0$. $\square$

**Remark 5.7.4 (Formalization).** The theorem on a cut at a good place takes the theorem on idempotents as a hypothesis and does not use it, and it does not use the continuity of $f$ ([JPosOfIdemEx.lean](lean:Development/WeilBound/RepresentationTheoryGL/RegularisedSiegelWeil/ThetaIdempotents/ThetaCoefficients/JPosOfIdemEx.lean#L19)). The input that supplies the good place is named after a bound of Jacquet and Piatetski-Shapiro, but its statement only gives a place. In the residue theorem the condition $r + 2 < 2t$ follows from $1 \le r < t$. In the proof of the residue theorem one input is passed through a function that ignores its three arguments ([ResCore.lean](lean:Development/WeilBound/RepresentationTheoryGL/RegularisedSiegelWeil/ThetaIdempotents/ThetaCoefficients/ResCore.lean#L61)). By the convention of the first section, $\theta_W(\Psi)(g, h)$ is $0$ when the sum does not converge absolutely; the bounds in the proof show that it converges. We have not opened the proofs of the inputs named above.
