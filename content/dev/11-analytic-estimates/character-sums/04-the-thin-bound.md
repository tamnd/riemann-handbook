---
title: The thin bound for twisted prime sums
decls:
  - QH.psi_thin
  - QH.thin
  - QH.thinH
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The thin bound for twisted prime sums

This section bounds the weighted prime sum $g_\chi(y)$ of a primitive [[Dirichlet character|JR4QSEFXWF]] $\chi$ for very large $y$, when the conductor of $\chi$ is a little more than polynomial in a parameter $x$ and $\chi$ has no exceptional zero. The bound is $|g_\chi(y)| \leq y\exp(-cx^{\varepsilon/8})$ for $y \geq \exp(x^{\varepsilon/3})/3$. We call it the thin bound, since it holds in a thin range of $y$ far beyond the conductor. It is first proved for $\psi(u, \chi)$ with the [truncated explicit formula](/entry/explicit-formula-closed/), then passed to $g_\chi$ by an integral identity, and finally stated for the characters of a host. The last form is used in the construction of hosts ([Theorem 3.3.3 of Volume 15](/entry/host-of-field-of/)). The Background section on [zeros of Dirichlet L-functions](/learn/analytic-number-theory/#zeros-of-dirichlet-l-functions) gives the zero-free region that we use.

We keep the notation of [the previous section](/entry/explicit-formula-closed/): $\psi_0(u, \chi) = \sum_{n \leq u}\Lambda(n)\chi(n) - \delta_\chi u$, with $\delta_\chi = 1$ exactly when $\chi$ is the trivial character $\chi_0$.

**Definition 6.4.1 (No exceptional zero).** Let $c_0 > 0$. A Dirichlet character $\chi$ has *no exceptional zero for $c_0$* if $L(\beta, \chi) \neq 0$ for every real $\beta$ with $1 - c_0 < \beta < 1$.

Lean: `QH.NoExc`.

The hypothesis is only needed for real characters $\chi \neq \chi_0$. For every other character the classical zero-free region already excludes real zeros close to $1$.

**Theorem 6.4.2 (Prime sums from a uniform zero-free region).** For every $c_0 > 0$ there are $C > 0$ and $c > 0$ with the following property. Let $N \geq 1$, let $\chi$ be a primitive character modulo $N$, and let $\lambda$ be real with $1 \leq \lambda$ and $\log N \leq \lambda$. Assume that if $\chi^2 = \chi_0$ and $\chi \neq \chi_0$, then $\chi$ has no exceptional zero for $c_0$. Then for every $u \geq e$,
$$|\psi_0(u, \chi)| \leq C\,u\,(\log u + \lambda)^2\exp\Bigl(-\frac{c\log u}{\lambda + \sqrt{\log u}}\Bigr).$$

Lean: `QH.psi_thin`.

For $\lambda = \log N$ and $\log N \leq \sqrt{\log u}$ the bound is the classical $\psi(u, \chi) - \delta_\chi u \ll u\exp(-c'\sqrt{\log u})$ for characters without an exceptional zero (Davenport, Chapter 20). The parameter $\lambda$ lets the conductor be larger than $\exp(\sqrt{\log u})$; then the saving is $\exp(-c\log u/\lambda)$.

*Proof.* There are three steps.

*Zero-free region.* By the classical zero-free region (Davenport, Chapter 14) there is an absolute $c_1 > 0$ such that $L(s, \chi)$ has no zero $\rho$ with $\mathrm{Re}\,\rho \geq 1 - c_1/\log(N(|\mathrm{Im}\,\rho| + 2))$, except possibly one zero, which is real and simple and occurs only when $\chi$ is real and $\chi \neq \chi_0$. Let $c = \min(c_1, c_0)$. Since $\log N \leq \lambda$ and $\lambda \geq 1$, a real zero $\beta$ with $\beta > 1 - c/(\lambda + \log 3)$ would satisfy $\beta > 1 - c_0$, which the hypothesis excludes. So every zero $\rho$ with $\mathrm{Re}\,\rho < 1$ satisfies
$$\mathrm{Re}\,\rho \leq 1 - \frac{c}{\lambda + \log(|\mathrm{Im}\,\rho| + 3)}.$$

*Zeros near $0$.* If $\rho$ is a zero of $L(s, \chi)$ in the critical strip, then $1 - \bar\rho$ is a zero of $L(s, \bar\chi)$ by the functional equation. The character $\bar\chi$ is primitive and satisfies the same hypotheses. So the zeros with $|\mathrm{Im}\,\rho| \leq 2$ have $\mathrm{Re}\,\rho \geq k/\lambda$ for some $k > 0$ that depends only on $c$. With the [lemma on zeros in a window](/entry/explicit-formula-closed/) (constant $C_w$) this gives, for every $T \geq 1$,
$$\sum_{\rho \in Z(\chi, T)}\frac{m(\rho)}{|\rho|} \leq 6C_w\Bigl(\frac{3}{k} + 4\Bigr)(\lambda + \log T)^2.$$
The zeros in windows of height $1$ near $0$ have $1/|\rho| \leq \lambda/k$; the others have $1/|\rho| \leq 1/|\mathrm{Im}\,\rho|$, and summing over windows gives a factor $\log T$.

*Explicit formula.* Let $v = \log u \geq 1$ and $T = \exp(\sqrt v)$, so that $2 \leq T \leq u$. The [truncated explicit formula](/entry/explicit-formula-closed/) (constant $C_7$) gives
$$|\psi_0(u, \chi)| \leq \sum_{\rho \in Z(\chi, T)}m(\rho)\frac{u^{\mathrm{Re}\,\rho}}{|\rho|} + C_7\Bigl(\frac{u\log^2(NuT)}{T} + \log(Nu) + S_1(\chi)\Bigr).$$
Each zero in the sum has $\mathrm{Re}\,\rho \leq 1 - c/(\lambda + \sqrt v + 2)$, so $u^{\mathrm{Re}\,\rho} \leq u\exp(-(c/3)v/(\lambda + \sqrt v))$, and the sum of $m(\rho)/|\rho|$ is at most a constant times $(\lambda + v)^2$ by the previous step. The term $S_1(\chi)$ is the case $T = 1$. In the other terms, $\log(NuT) \leq \lambda + 2v$ and $1/T = e^{-\sqrt v} \leq \exp(-v/(\lambda + \sqrt v))$. All terms are therefore at most a constant times $u(\log u + \lambda)^2\exp(-c'v/(\lambda + \sqrt v))$ with $c' = \min(c/3, 1)$. $\square$

To pass from $\psi$ to a smoother sum we use the following weights.

**Definition 6.4.3 (The weighted prime sum).** For $y \geq 1$ and a Dirichlet character $\chi \neq \chi_0$ modulo $N$ let
$$g_\chi(y) = \sum_{n \leq y}\Lambda(n)\chi(n)\Bigl(\frac{y}{n} - 1\Bigr) + y\,\frac{L'}{L}(1, \chi),$$
and for $\chi = \chi_0$ let
$$g_{\chi_0}(y) = \sum_{n \leq y}\Lambda(n)\Bigl(\frac{y}{n} - 1\Bigr) - y(\log y - 1 - \gamma),$$
where $\gamma$ is Euler's constant.

Lean: `Formalism.HC.An.gChi` (also `QH.G0`, the same function).

The weight $y/n - 1$ is the Cesàro weight $\int_n^y du/u$ times $y$. The constant terms make $g_\chi(y)$ small. Indeed, for primitive $\chi$ and $y \geq 1$,
$$g_\chi(y) = -y\int_y^\infty\frac{\psi_0(u, \chi)}{u^2}\,du.$$
To see this, note that $\sum_{n \leq y}\Lambda(n)\chi(n)(y/n - 1) = y\int_1^y\psi(u, \chi)u^{-2}\,du$ by partial summation. For $\chi \neq \chi_0$, $-L'/L(1, \chi) = \int_1^\infty\psi(u, \chi)u^{-2}\,du$. For $\chi_0$, $\int_1^\infty(\psi(u) - u)u^{-2}\,du = -1 - \gamma$.

**Theorem 6.4.4 (Thin bound).** Let $\varepsilon$, $A$, $c$ and $c_0$ be positive reals. There is $x_0$ with the following property. Let $x \geq x_0$, let $N \geq 1$ and let $\chi$ be a primitive character modulo $N$ with
$$\log N \leq A\,x^{\varepsilon/5}\log^2x.$$
Assume that if $\chi^2 = \chi_0$ and $\chi \neq \chi_0$, then $\chi$ has no exceptional zero for $c_0$. Then for every $y \geq \exp(x^{\varepsilon/3})/3$,
$$|g_\chi(y)| \leq y\exp(-c\,x^{\varepsilon/8}).$$

Lean: `QH.thin`.

The constant $c$ in the conclusion is arbitrary. This is not an error: the true saving is about $\exp(-x^{2\varepsilon/15}/\log^2x)$, and $2\varepsilon/15 > \varepsilon/8$, so any multiple of $x^{\varepsilon/8}$ is beaten once $x$ is large.

*Proof.* Let $C$ and $c_1$ be the constants of the theorem on prime sums for $c_0$. Take $x_0 \geq \max(e, 3^{3/\varepsilon})$, and large enough for the estimate of the integral below. Put $\lambda = \max(1, \log N)$; then $1 \leq \lambda \leq (A + 1)x^{\varepsilon/5}\log^2x$. For $x \geq 3^{3/\varepsilon}$ we have $x^{\varepsilon/3} \geq 3$, so $y \geq e^3/3 \geq e$. By the integral identity and the theorem on prime sums,
$$|g_\chi(y)| \leq y\int_y^\infty C(\log u + \lambda)^2\exp\Bigl(-\frac{c_1\log u}{\lambda + \sqrt{\log u}}\Bigr)\frac{du}{u}.$$
Here $\log u \geq \log y \geq x^{\varepsilon/3} - \log 3$. The exponent $c_1\log u/(\lambda + \sqrt{\log u})$ is increasing in $\log u$, and at $\log u = x^{\varepsilon/3}$ it is at least a constant times $x^{\varepsilon/3 - \varepsilon/5}/\log^2x = x^{2\varepsilon/15}/\log^2x$. For larger $u$ the integrand decays like a power of $u$ times $\exp(-c_1\sqrt{\log u}/2)$ once $\sqrt{\log u} \geq \lambda$. So the integral is at most $\exp(-c\,x^{\varepsilon/8})$ for $x \geq x_0$. $\square$

The last result restates the thin bound for the characters attached to a host. We need only a few features of a host $H$ (its definition is in [the construction of hosts](/entry/host-of-field-of/)). It has two primes $q$ and $d$, a positive integer $Q_S$, and the modulus $N_H = Q_Sq\,d$. It has a finite group $G$ with a homomorphism $\mathrm{art}_H : (\mathbb{Z}/N_H\mathbb{Z})^\times \to G$, the Artin map of a Galois number field with group $G$. We write $Q_S'$ for the odd part of $Q_S$.

**Definition 6.4.5 (Characters of a host).** A *character of $H$* is a primitive Dirichlet character $\chi$ that induces the character $\theta \circ \mathrm{art}_H$ modulo $N_H$, for some homomorphism $\theta : G \to \mathbb{C}^\times$. The host satisfies the *real box condition* if, for every real character $\chi$ of $H$ whose conductor is divisible by $q$ or by $d$, $L(\beta, \chi) \neq 0$ for all real $\beta > 1 - 1/400$.

Lean: `Formalism.HC.HostRaw.IsCharE`, `UpperTheory.Top.RealBox`.

**Theorem 6.4.6 (Thin bound for a host).** There is $c > 0$ with the following property. For all real $B$ and all $\varepsilon$ with $0 < \varepsilon < 1/52$ there is $x_0$ such that for every $x \geq x_0$ and every host $H$ with $Q_S' \leq B$, $\log N_H \leq 2x^{\varepsilon/5}\log^2x$ and the real box condition, every character $\chi$ of $H$ and every $y \geq \exp(x^{\varepsilon/3})/3$ satisfy
$$|g_\chi(y)| \leq y\exp(-c\,x^{\varepsilon/8}).$$

Lean: `QH.thinH` (also `UpperTheory.Top.ThinH`, the statement).

*Proof.* Take $c = 1$. For a fixed bound $N_1$ there is $c_0' > 0$ such that no character $\chi \neq \chi_0$ of modulus at most $N_1$ has a real zero in $(1 - c_0', 1)$; there are finitely many such characters, and $L(\beta, \chi) \neq 0$ at $\beta = 1$. Apply this with $N_1 = 8\lfloor B\rfloor$, and apply the thin bound with $A = 2$, $c = 1$ and $c_0 = \min(c_0', 1/400)$. Let $\chi$ be a character of $H$, of conductor $N$. Then $N$ divides $N_H$, so $\log N \leq \log N_H \leq 2x^{\varepsilon/5}\log^2x$. It remains to check the hypothesis on real zeros. Let $\chi$ be real and $\chi \neq \chi_0$. If $q$ or $d$ divides $N$, the real box condition gives it, since $c_0 \leq 1/400$. If neither divides $N$, every prime factor of $N$ divides $8Q_S'$. A real primitive character has a conductor whose odd part is squarefree and whose $2$-part divides $8$, so $N$ divides $8Q_S'$ and $N \leq 8\lfloor B\rfloor$. Then the choice of $c_0'$ gives it. $\square$

**Remark 6.4.7 (Formalization).** The thin bound for a host is in [GaussSumFunctionEq.lean](lean:Development/AutomorphicArithmetic/MeanSquareBounds/GaussSumFunctionEq.lean#L55). The name of the module and of its lemma `gauss_sum_function_eq` is misleading: no Gauss sum appears, and the lemma only says that the weight $\max(y/n - 1, 0)$ of `gChi` equals $y/n - 1$ for $n \leq y$. The arbitrary $c$ in [Thin.lean](lean:Development/AutomorphicArithmetic/MeanSquareBounds/Thin.lean#L10) is genuine, as explained above. The estimate of the integral is `int_thin` and the integral identity is `g_integral`; we have opened their statements, not their proofs. The finite check on small moduli is `small_zeros`, an induction on the bound with a lemma `noExc_level` that we have not opened. The zero-free region is `Formalism.ZeroFreeDirichlet.zFRDirichlet`, a result of another chapter.
