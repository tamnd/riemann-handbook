---
title: Integrality of CM jets
decls:
  - GlobalTheory.JetIntElliptic.jetInt
  - GlobalTheory.T.cmLatticeDividedPowerJetIntegrality_of_ellipticCM
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Integrality of CM jets

The derivatives at the origin of the deformed Eisenstein sum of a CM lattice are, up to explicit factors, the lattice sums of the [previous section](/entry/cm-lattice-deriv-class-invariance-of-hecke/). Here we bound their $l$-adic denominators. After a suitable scaling by periods, the derivative of order $\kappa$ has denominator at most $l^{e + (2s g + |\kappa|) c}$, where $e$ comes from the partial zeta values of the real subfield and $c$ from the ramification at $l$. The proof writes the derivative as a jet of a Hilbert Eisenstein series at a diagonal CM point and uses the integrality of the CM values of $j$, $G_2^*$ and the Weierstrass function. The bound is one of the five inputs of the [toric denominator bounds](/entry/join-out-of-five/).

### The published inputs

The theorems of this section and the next one are proved under four published theorems. We state them here. The fourth one is the functional equation of partial zeta functions, stated before the [Theorem 1.1.10](/entry/hecke-weight-two-of-fe/) on Hecke's series of weight two.

Let $F$ be a totally real field and $\mathfrak{f} \neq 0$ an ideal of $\mathcal{O}_F$. Two nonzero ideals $I, J$ prime to $\mathfrak{f}$ are *narrowly equivalent modulo $\mathfrak{f}$* if $(a)I = (b)J$ for some nonzero $a, b \in \mathcal{O}_F$ that are totally positive and congruent to $1$ modulo $\mathfrak{f}$. A *ray class function modulo $\mathfrak{f}$* is a map $\varepsilon$ from ideals of $\mathcal{O}_F$ to $\mathbb{Q}$ that is constant on these classes. Its $L$-function is a function $L(\varepsilon, \cdot)$, holomorphic on $\mathbb{C} \setminus \{1\}$, with $L(\varepsilon, s) = \sum_{I} \varepsilon(I)\, N I^{-s}$ for $\operatorname{Re} s > 1$, the sum over nonzero ideals $I$ prime to $\mathfrak{f}$ ([zeta functions of number fields](/learn/l-functions/#zeta-functions-of-number-fields)). It is unique if it exists.

**Theorem 1.3.1 (Siegel-Klingen).** Let $F$ be totally real, $\mathfrak{f} \neq 0$, and $\varepsilon$ a ray class function modulo $\mathfrak{f}$. Then $L(\varepsilon, \cdot)$ exists, and $L(\varepsilon, 1 - k) \in \mathbb{Q}$ for every integer $k \geq 1$.

This is due to Klingen (1962) and Siegel (1970).

**Theorem 1.3.2 (Deligne-Ribet).** Let $F$ be totally real, $l$ a prime, $n \geq 1$, and $\varepsilon$ a ray class function modulo $l^n$ whose values on ideals prime to $l$ lie in $\mathbb{Z}_{(l)}$. Let $\mathfrak{c}$ be an ideal prime to $l$ and put $\varepsilon_{\mathfrak{c}}(I) = \varepsilon(\mathfrak{c} I)$. Then for every $k \geq 1$,
$$L(\varepsilon, 1 - k) - N\mathfrak{c}^{\,k}\, L(\varepsilon_{\mathfrak{c}}, 1 - k) \in \mathbb{Z}_{(l)}.$$

This is the congruence of Deligne and Ribet (1980).

Let $K \subset \mathbb{C}$ be an imaginary quadratic field. For a fractional ideal $\mathfrak{a}$ of $K$, which is a lattice in $\mathbb{C}$, let $j(\mathfrak{a})$ be the $j$-invariant of the curve $\mathbb{C}/\mathfrak{a}$ ([complex multiplication](/learn/elliptic-curves/#complex-multiplication)).

**Theorem 1.3.3 (the Hilbert class field).** Let $K \subset \mathbb{C}$ be imaginary quadratic with class number $h$. Then $K(j(\mathcal{O}_K))$ is the Hilbert class field of $K$ (the maximal abelian extension unramified at all finite primes), $[K(j(\mathcal{O}_K)) : K] = h$, and $j(\mathfrak{a}) = j(\mathfrak{b})$ if and only if $\mathfrak{a}$ and $\mathfrak{b}$ have the same class. The set of values $j(\mathfrak{a})$ has $h$ elements, and it is the set of conjugates of $j(\mathcal{O}_K)$ over $K$.

See Silverman, *Advanced Topics*, Theorem II.4.3, and Cox, Theorem 11.1.

**Theorem 1.3.4 (main theorem of complex multiplication).** Let $K \subset \mathbb{C}$ be imaginary quadratic, $\operatorname{Art}$ the global Artin map of $K$, $\sigma \in \operatorname{Aut}(\mathbb{C}/K)$, and $s$ an idele of $K$ with $\sigma|_{K^{ab}} = \operatorname{Art}(s)$. Let $X$ be an elliptic curve over $\mathbb{C}$, $\mathfrak{a}$ a fractional ideal, and $\xi : \mathbb{C}/\mathfrak{a} \to X(\mathbb{C})$ an analytic isomorphism. Then there is exactly one analytic isomorphism $\xi' : \mathbb{C}/s_f^{-1}\mathfrak{a} \to X^\sigma(\mathbb{C})$ with $\sigma(\xi(x)) = \xi'(s_f^{-1} x)$ for all $x \in K/\mathfrak{a}$, where $s_f$ is the finite part of $s$.

See Shimura, *Introduction to the Arithmetic Theory of Automorphic Functions*, Theorem 5.4, and the [main theorem of complex multiplication](/learn/theta-functions-cm/#the-main-theorem-of-complex-multiplication).

### Sizes and admissible data

Let $\bar{\mathbb{Q}}$ be the algebraic closure of $\mathbb{Q}$ in $\mathbb{C}$, $l$ a prime, and $\lambda : \bar{\mathbb{Q}} \to \mathbb{C}_l$ a ring homomorphism. Normalize $|l|_l = l^{-1}$.

**Definition 1.3.5 (size).** For $r \in \mathbb{R}$ let $\mathcal{B}_\lambda(r)$ be the set of $x \in \mathbb{C}$ such that $x \in \bar{\mathbb{Q}}$ and $|\lambda(x)|_l \leq l^{r}$.

So $x \in \mathcal{B}_\lambda(r)$ says that the $l$-adic denominator of $x$ is at most $l^r$. We have $\mathcal{B}_\lambda(r) \subset \mathcal{B}_\lambda(r')$ for $r \leq r'$, $\mathcal{B}_\lambda(r)\,\mathcal{B}_\lambda(r') \subset \mathcal{B}_\lambda(r + r')$, $l \in \mathcal{B}_\lambda(-1)$, and every rational number $q$ is in $\mathcal{B}_\lambda(-v_l(q))$.

Let $E$ be a CM field, $F$ its real subfield, $g = [F : \mathbb{Q}]$, and keep the notation of the previous section. For a prime $l$ and an admissible conductor $\mathfrak{f}$ put:

- $a_0 = \max\{\operatorname{ord}_v \mathfrak{f} : v \mid l\}$, the maximum over primes $v$ of $F$ (and $a_0 = 0$ if no such $v$ divides $\mathfrak{f}$);
- $\delta_l = v_l(\operatorname{disc} E)/[E : \mathbb{Q}]$;
- $c = a_0$ if some prime of $F$ over $l$ divides $\mathfrak{f}$, and $c = \delta_l$ otherwise.

For a function $z$ on the ideal class group $\operatorname{Cl}(F)$ with rational values put $e = \max_C \max(0, -v_l(z(C)/2^g))$.

**Definition 1.3.6 (admissible data).** Let $d$ be a prime with $d > 4$, and let $\Lambda \subset \mathbb{C}$ be the ring of integers of $\mathbb{Q}(\sqrt{-d})$. *Admissible data* for $l$ are: a CM field $E$, abelian over $\mathbb{Q}$, and a CM type $\varphi = (\varphi_i)_{i \in I}$, such that

1. $E/F$ is unramified at all finite primes, $2 \mid \operatorname{disc} E$, and $|I| \geq 2$;
2. $\prod_i \varphi_i(\zeta) = 1$ for every root of unity $\zeta \in E$;
3. there is $w \in E$ with $w^2 = -d$ and $\varphi_i(w) = i\sqrt d$ for all $i$;

together with an integer $s \geq 1$, a function $z : \operatorname{Cl}(F) \to \mathbb{Q}$ such that each $z(C)$ is the value at $1 - 2s$ of a partial zeta function of $C$, an admissible conductor $\mathfrak{f}$, a set $Q$ admissible for $\mathfrak{f}$ whose primes do not lie over $l$, and $y \in \mathbb{A}_f^\times$ with $y_w = 1$ at every prime $w$ of $E$ over $l$. The lattice of the data is $L = L(\mathfrak{c}(\mathfrak{f}, Q), y)$.

Let $\Delta(\Lambda) = g_2(\Lambda)^3 - 27 g_3(\Lambda)^2$ be the discriminant of $\Lambda$ ([lattices and the Weierstrass function](/learn/elliptic-curves/#lattices-and-the-weierstrass-function)).

### The theorem

**Theorem 1.3.7 (integrality of CM jets).** Assume the theorems of Siegel-Klingen and Deligne-Ribet, the functional equation of partial zeta functions, the Hilbert class field theorem and the main theorem of complex multiplication. Let a prime $l$ and admissible data for $l$ be given, with lattice $L$. Let $\lambda : \bar{\mathbb{Q}} \to \mathbb{C}_l$ be a ring homomorphism and $\Omega \in \mathbb{C}$ with $\Omega^{12} = \Delta(\Lambda)$. Then there are nonzero $a_i, b_i \in \mathbb{C}$ $(i \in I)$ such that for all $i$
$$\frac{a_i}{\Omega} \in \mathcal{B}_\lambda(a_0), \qquad \Bigl(\frac{a_i b_i \sqrt d}{2\pi}\Bigr)^{-1} \in \mathcal{B}_\lambda\bigl(c + \tfrac12 [l = d]\bigr),$$
and for every defining sum $\mathcal{G}$ of weight $2s$ for $L$, every $\kappa \in \mathbb{N}^I$ and every word $u$ in which each $i$ occurs $\kappa_i$ times,
$$\partial_u \mathcal{G}(0) \prod_{i \in I} \frac{(b_i/a_i)^{\kappa_i}}{a_i^{2s}} \in \mathcal{B}_\lambda\bigl(e + (2s|I| + |\kappa|)\, c\bigr), \qquad |\kappa| = \textstyle\sum_i \kappa_i.$$

Lean: `GlobalTheory.T.cmLatticeDividedPowerJetIntegrality_of_ellipticCM` (also `GlobalTheory.JetIntElliptic.jetInt`, a second name).

We need one more object. For an $\mathcal{O}_F$-lattice $L' \subset F^2$, a weight $k$ and $a, b \in \mathbb{C}^g$, let $G_{L'}(b, a)$ be the sum of $\prod_j (x_0^{(j)} b_j + x_1^{(j)} a_j)^{-k}$ over $(L' \setminus 0)/\mathcal{O}_F^\times$, regularized by Hecke's method when $k = 2$. The *jet* of order $\mu \in \mathbb{N}^g$ at $\tau \in \mathbb{H}$ is the derivative $\partial^\mu$ at $z = 0$ of $z \mapsto c_k\, G_{L'}(\tau + z\bar\tau, 1 + z)$. The lattice $L'$ has *level $N$* if $N\mathcal{O}_F^2 \subset L' \subset \mathcal{O}_F^2$.

*Proof.* Write $\varepsilon_d = \frac12[l = d]$.

*The CM point.* Put $\theta = (-1 + w)/2$ if $d \equiv 3 \bmod 4$ and $\theta = w$ otherwise. Then $\varphi_i(\theta) = \tau$ for one $\tau \in \mathbb{H}$ and all $i$, $\Lambda = \mathbb{Z} + \mathbb{Z}\tau$, and $\operatorname{Im}\tau = \sqrt d/2$ or $\sqrt d$. The number $\theta$ is integral, and $(\theta - \bar\theta)^2 = -D$ with $D = d$ or $D = 4d$. Since $d$ is an odd prime, $\tfrac12 v_l(D) = \varepsilon_d + [l = 2,\ d \not\equiv 3 \bmod 4]$.

*The level.* Choose an integer $M_0 > 1$ prime to $l$. There are integers $M, M'$ prime to $l$ with $M_0 \mid M'$ and an $\mathcal{O}_F$-lattice $L' \subset F^2$ of level $N = M' l^{b}$, $b = v_l(D) + a_0$, such that $x \in L'$ if and only if $MD\,y' = x_0\theta + x_1$ for some $y' \in L$. All real conjugates of the coordinates of vectors of $L'$, and $N$, lie in $\mathcal{B}_\lambda(-v_l(D)/2)$. This uses $y_w = 1$ over $l$ and the conditions on $\mathfrak{f}$ and $Q$.

*The choice.* Pick $\gamma \neq 0$ with $\gamma \in \mathcal{B}_\lambda(-c - \varepsilon_d)$ and $\gamma^{-1} \in \mathcal{B}_\lambda(c + \varepsilon_d)$; this is possible since $c$ is rational. Put $a_i = \Omega/l^{a_0}$ and $b_i = 2\pi\gamma/(\sqrt d\, a_i)$. Then $a_i/\Omega = l^{-a_0} \in \mathcal{B}_\lambda(a_0)$ and $(a_i b_i\sqrt d/2\pi)^{-1} = \gamma^{-1}$. This gives the first two claims.

*Derivatives as jets.* Identify $I$ with the real embeddings of $F$. For $x = x_0\theta + x_1$ we have $\varphi_i(x) + z_i\overline{\varphi_i(x)} = x_0^{(i)}(\tau + z_i\bar\tau) + x_1^{(i)}(1 + z_i)$. Comparing the series term by term, as in the proof of the [derivative formula](/entry/cm-lattice-deriv-class-invariance-of-hecke/), gives $\partial_u \mathcal{G}(0) = (MD)^{2sg}\, J_\kappa$, where $J_\kappa$ is the jet of order $\kappa$ of weight $2s$ for $L'$ at $\tau$. This uses the Hilbert Eisenstein series of weight $2s$ and their $q$-expansions. They come from the Lipschitz formula and, for weight two, from the [Theorem 1.1.10](/entry/hecke-weight-two-of-fe/) on Hecke's series. This is the only place where the functional equation is used.

*CM values.* Let $\omega = \Omega/(2\pi i)$. Since $\Omega^{12} = \Delta(\Lambda)$, $\omega^{12} = \Delta(\tau)$. The value $j(\tau)$ is an algebraic integer, so $j(\tau) \in \mathcal{B}_\lambda(0)$. For a nonzero torsion point $t \in (\mathbb{Z}/N)^2$ with $M_0 t = 0$, the value $(G_2^*(\tau)/(2\pi i)^2 + \wp_N(t, \tau))/\omega^2$ lies in $\mathcal{B}_\lambda(\rho)$ with $\rho = 2c + 2a_0 + v_l(D)/2$. Here $G_2^*$ is the nonholomorphic Eisenstein series of weight $2$ and $\wp_N(t, \cdot)$ the Weierstrass function at the torsion point $t$. The bound from CM theory has exponent $1$ or $2$ at $l = 2$ and $\varepsilon_d$ otherwise; at $l = 2$ we use $c \geq \delta_2 \geq \tfrac12$, which holds since $2 \mid \operatorname{disc} E$.

*Jets at CM points.* The bound for jets of Hilbert Eisenstein series at a diagonal CM point now gives
$$\frac{J_\kappa\, (\pi/\operatorname{Im}\tau)^{|\kappa|}}{(2\pi i)^{w}\, \omega^{w}} \in \mathcal{B}_\lambda\bigl(e + s\, v_l(d_F) + 2sbg + |\kappa|\rho\bigr), \qquad w = 2sg + 2|\kappa|.$$
Its inputs are the existence of Hilbert Eisenstein series of weight $2s$ with their $q$-expansions, the integrality above, the zeta values $z$, and the inequality $b + v_l(d_F)/g - v_l(D)/2 \leq \rho$. The inequality holds since $v_l(d_F)/g \leq \delta_l \leq c$.

*Assembly.* A direct computation gives
$$\begin{aligned} \partial_u \mathcal{G}(0)\prod_i \frac{(b_i/a_i)^{\kappa_i}}{a_i^{2s}} &= \frac{J_\kappa\,(\pi/\operatorname{Im}\tau)^{|\kappa|}}{(2\pi i)^{w}\,\omega^{w}} \cdot (MD\, l^{a_0})^{2sg} \\ &\quad \cdot \Bigl(\frac{2\operatorname{Im}\tau}{\sqrt d}\,\gamma\, l^{2a_0}\Bigr)^{|\kappa|}. \end{aligned}$$
Here $MD\,l^{a_0} \in \mathcal{B}_\lambda(-b)$, and $2\operatorname{Im}\tau/\sqrt d$ is $1$ or $2$, which lies in $\mathcal{B}_\lambda(-[l = 2,\ d \not\equiv 3 \bmod 4])$. Adding exponents, the terms $2sbg$ cancel, and the coefficient of $|\kappa|$ is $\rho - [l = 2,\ d \not\equiv 3] - c - \varepsilon_d - 2a_0 = c$. So the product lies in $\mathcal{B}_\lambda(e + s\,v_l(d_F) + |\kappa| c)$. Finally $s\, v_l(d_F) \leq s g c \leq 2s|I| c$, since $|I| = g$. $\square$

**Remark 1.3.8 (Formalization).** The first name is proved from the second by `first | exact @…`. The proof uses only the functional equation: the other three published theorems are hypotheses that are not used ([CMLatticeDividedPowerJetIntegralityOfHyp.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CMLatticeDividedPowerJetIntegralityOfHyp.lean#L251)). The name speaks of divided powers, but the bound is for $\partial_u\mathcal{G}(0)$ itself, with no factor $1/\kappa!$. The bound for jets at CM points, the level lemma and the CM bounds are proved elsewhere; we have read their statements, not their proofs.
