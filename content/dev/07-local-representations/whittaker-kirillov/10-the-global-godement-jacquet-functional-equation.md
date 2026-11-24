---
title: The global Godement-Jacquet functional equation
decls:
  - GroundTheory.Automorphic.GJGlobal.thetaPairing_eq
  - GroundTheory.Automorphic.GJGlobal.globalZeta_entire_functionalEquation
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The global Godement-Jacquet functional equation

Godement and Jacquet attach to a cusp form on $\mathrm{GL}_n$ and a Schwartz-Bruhat function on $n \times n$ matrices a zeta integral over $\mathrm{GL}_n(\mathbb{A})$. This section proves that the zeta integral of a matrix coefficient of two cusp forms converges in a right half-plane, has an entire continuation, and satisfies the functional equation $s \mapsto 1 - s$ under the Fourier transform of the Schwartz-Bruhat function. The tool is Poisson summation on matrices, applied to a theta pairing of the two cusp forms. The result is used in the proof of [Theorem 7.30 of Volume 8](/entry/gen-fe/). For cusp forms see [constant terms and cusp forms](/learn/automorphic-forms/#constant-terms-and-cusp-forms), and for the Fourier transform see [the Fourier transform](/learn/analysis/#the-fourier-transform).

### Setting

Let $K$ be a number field of degree $d$ over $\mathbb{Q}$, $\mathbb{A}$ its adele ring, $n \geq 2$ and $G = \mathrm{GL}_n(\mathbb{A})$. Let $|\cdot|$ be the idele norm, and let
$$G^1 = \{ g \in G : |\det g| = 1 \}.$$
The group $\mathrm{GL}_n(K)$ lies in $G^1$ by the product formula. Fix a Haar measure $\mu$ on $G^1$ and a measurable fundamental domain $\mathcal{F} \subset G^1$ for the left action of $\mathrm{GL}_n(K)$. Fix a Haar measure $\nu$ on $G$ ([Haar measure](/learn/analysis/#haar-measure)).

For $t > 0$ let $c(t) \in G$ be the scalar matrix with entry $t^{1/(nd)}$ at each archimedean place and $1$ at each finite place. Then $c$ is a homomorphism into the center, and $|\det c(t)| = t$.

Let $\psi$ be the standard character of $\mathbb{A}/K$. For a Schwartz-Bruhat function $\Phi$ on $M_n(\mathbb{A})$, its Fourier transform is
$$\hat\Phi(y) = \int_{M_n(\mathbb{A})} \Phi(x)\, \psi(\operatorname{tr}(xy))\, dx,$$
for the self-dual measure. It is again Schwartz-Bruhat.

**Definition 4.10.1 (Matrix coefficient).** For cusp forms $\phi_1, \phi_2$ on $\mathrm{GL}_n(K)\backslash G$, the *matrix coefficient* is
$$f(g) = \int_{\mathcal{F}} \phi_1(xg)\, \overline{\phi_2(x)}\, d\mu(x).$$

This is the $L^2$ pairing of the right translate of $\phi_1$ by $g$ with $\phi_2$, over $\mathrm{GL}_n(K)\backslash G^1$.

**Definition 4.10.2 (Global zeta integral).** For $\Phi$ Schwartz-Bruhat, $f$ a function on $G$ and $s \in \mathbb{C}$,
$$Z(\Phi, f, s) = \int_G \Phi(g)\, f(g)\, |\det g|^{s + (n-1)/2}\, d\nu(g).$$

### The theta pairing

**Definition 4.10.3 (Theta pairing).** For a function $\Xi$ on $G$ and $t > 0$,
$$J_\Xi(t) = \int_{\mathcal{F}} \int_{\mathcal{F}} \overline{\phi_2(x)}\, \phi_1(y) \sum_{\gamma \in \mathrm{GL}_n(K)} \Xi(c(t)\,x^{-1}\gamma\, y)\, d\mu(y)\, d\mu(x).$$

Unfolding the sum over $\gamma$ against the integral over $y$ turns $J_\Xi$ into an integral of $\Xi$ against the matrix coefficient over $\{|\det g| = t\}$. So the Mellin transform of $J_\Xi$ in $t$ is a zeta integral.

**Theorem 4.10.4 (Poisson summation for the theta pairing).** Let $\phi_1, \phi_2$ be cusp forms, $\Phi$ a Schwartz-Bruhat function on $M_n(\mathbb{A})$ and $t > 0$. Put $\Xi_1(g) = \Phi(g)$ and $\Xi_2(g) = \hat\Phi(g^{-1})$. Then
$$J_{\Xi_1}(t) = t^{-n}\, J_{\Xi_2}(t).$$

Lean: `GroundTheory.Automorphic.GJGlobal.thetaPairing_eq`.

*Proof.* Fix $x, y \in G^1$ and put $a = c(t)x^{-1}$ and $b = y$.

1. Poisson summation on the lattice $M_n(K) \subset M_n(\mathbb{A})$, applied to $\xi \mapsto \Phi(a\xi b)$, gives
$$\sum_{\xi \in M_n(K)} \Phi(a\xi b) = t^{-n} \sum_{\xi \in M_n(K)} \hat\Phi(b^{-1}\xi a^{-1}).$$
The factor is $|\det a|^{-n}|\det b|^{-n} = t^{-n}$, because $\xi \mapsto a\xi b$ scales the measure of $M_n(\mathbb{A})$ by $|\det a|^n |\det b|^n$.
2. Integrate both sides against $\overline{\phi_2(x)}\phi_1(y)$ over $\mathcal{F} \times \mathcal{F}$. The terms with $\xi$ of rank less than $n$ give $0$: such a sum is, after a change of variables, invariant under the unipotent radical of a proper parabolic subgroup acting on $y$ (or on $x$), and the integral of a cusp form over that radical vanishes. So only $\xi \in \mathrm{GL}_n(K)$ remains on each side.
3. The interchange of the sums and integrals is justified by bounds on the theta series that are uniform on $\mathcal{F}$, together with the rapid decay of cusp forms.
4. On the right, $\hat\Phi(y^{-1}\gamma\, x\, c(t)^{-1}) = \Xi_2(c(t)\,x^{-1}\gamma^{-1} y)$, since $c(t)$ is central. Reindex $\gamma \mapsto \gamma^{-1}$.

$\square$

### The functional equation

**Theorem 4.10.5 (Global Godement-Jacquet functional equation).** Let $n \geq 2$, let $\phi_1, \phi_2$ be cusp forms on $\mathrm{GL}_n(K)\backslash G$ with $\phi_1(c(t)x) = \phi_1(x)$ for all $t > 0$ and $x \in G$, let $f$ be their matrix coefficient and let $\Phi$ be a Schwartz-Bruhat function on $M_n(\mathbb{A})$. Put $\check f(g) = f(g^{-1})$. Then there are $\sigma_0 \in \mathbb{R}$ and entire functions $\Lambda, \Lambda'$ such that:

1. for $\operatorname{Re} s > \sigma_0$, the integrand of $Z(\Phi, f, s)$ is $\nu$-integrable and $Z(\Phi, f, s) = \Lambda(s)$;
2. for $\operatorname{Re} s > \sigma_0$, the integrand of $Z(\hat\Phi, \check f, s)$ is $\nu$-integrable and $Z(\hat\Phi, \check f, s) = \Lambda'(s)$;
3. $\Lambda(s) = \Lambda'(1 - s)$ for all $s \in \mathbb{C}$.

Lean: `GroundTheory.Automorphic.GJGlobal.globalZeta_entire_functionalEquation`.

*Proof.* Write $J_1 = J_{\Xi_1}$ and $J_2 = J_{\Xi_2}$ with $\Xi_1, \Xi_2$ as in the Poisson theorem.

1. *Decay.* As $t \to \infty$, $J_1(t)$ and $J_2(t)$ decay faster than any power of $t$: the matrix $c(t)x^{-1}\gamma y$ goes to infinity in $M_n(\mathbb{A})$, and $\Phi$ and $\hat\Phi$ decay rapidly. The Poisson theorem turns the behavior of $J_1$ as $t \to 0$ into the behavior of $t^{-n}J_2(t)$, which decays rapidly as $t \to 0$ too, because the cusp forms remove the singular terms.
2. *Mellin transforms.* Decompose $G = G^1 \times c(\mathbb{R}_{>0})$, with $\nu$ the product of $\mu$ and a multiple of $dt/t$. Unfold the sum over $\gamma$ in $J_1$. The central invariance of $\phi_1$ makes the integrand depend on $c(t)$ only through $\Phi$. This gives, for $\operatorname{Re} s$ large,
$$Z(\Phi, f, s) = C \int_0^\infty J_1(t)\, t^{s + (n-1)/2}\, \frac{dt}{t},$$
with a constant $C > 0$ from the normalization of the measures. The same computation, with $g \mapsto g^{-1}$, gives $Z(\hat\Phi, \check f, s)$ as $C$ times the Mellin transform of $J_2$ at $s + (n-1)/2$.
3. *Continuation.* By step 1, both Mellin transforms converge for all $s$ and define entire functions. Call them $\Lambda$ and $\Lambda'$, including the constant $C$. Integrability for $\operatorname{Re} s > \sigma_0$ comes from the absolute convergence of the unfolded integral.
4. *Functional equation.* Insert $J_1(t) = t^{-n}J_2(t)$ into the Mellin transform and substitute $t \mapsto t^{-1}$. The exponent $s + (n-1)/2 - n$ of $t$ becomes $(1 - s) + (n-1)/2$ after the inversion, and the inversion of $t$ matches the inversion $g \mapsto g^{-1}$ in $\check f$ and $\Xi_2$. So $\Lambda(s) = \Lambda'(1 - s)$.

$\square$

**Remark 4.10.6.** In the classical theorem of Godement and Jacquet, the zeta integral of a matrix coefficient of a cuspidal representation $\pi$ is $L(s, \pi)$ times an entire function, and the functional equation relates $\pi$ and its contragredient. Here only the global statement is proved: the integral continues to an entire function and satisfies the functional equation with the Fourier transform of $\Phi$. No Euler product appears.

**Remark 4.10.7 (Formalization).** Only $\phi_1$ is assumed invariant under the central section $c(t)$; no such hypothesis is put on $\phi_2$ ([GJGlobal.lean](lean:GroundTheory/AutomorphicForms/GL2/GJGlobal.lean#L71)). The files are in a folder named for $\mathrm{GL}_2$, but the theorems hold for every $n \geq 2$. Both theorems are proved with `maxHeartbeats 1600000`. The bounds of step 3 of the Poisson theorem and the decay of step 1 above are separate lemmas, summarized here.
