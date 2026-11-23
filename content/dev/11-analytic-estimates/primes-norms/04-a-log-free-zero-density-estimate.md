---
title: A log-free zero density estimate
decls:
  - GlobalTheory.Lin.LogFree.count_param
  - GlobalTheory.Lin.LogFree.zero_density
  - GlobalTheory.T.logFree_zeroDensity_dirichlet_one_modulus
status: drafted
drafted_by: writer@claude-opus-5-5
---
## A log-free zero density estimate

The second half of the chapter proves the prime number theorem in arithmetic progressions with a relative error, uniformly in the modulus. Its main analytic input is a zero density estimate near the line $\mathrm{Re}\, s = 1$ with no logarithmic loss: the number of zeros of all [[Dirichlet L-functions|24GAZHVTGB]] modulo $q$ with real part at least $\sigma$ and height at most $T$ is at most $C(qT)^{A(1 - \sigma)}$. This section proves it by Gallagher's method. A zero near $1 + i\tau$ makes a prime sum large on a long range, and a mean value theorem bounds how often a prime sum can be large. The estimate is used in Section 5 to bound [sums over zeros](/entry/sum-rpow-zeros-le/).

Throughout, $q \geq 1$ and $\chi$ runs over the [[Dirichlet characters|JR4QSEFXWF]] modulo $q$ (see [the Background](/learn/l-functions/#dirichlet-characters)). We write $L(s, \chi)$ for the Dirichlet L-function, continued to all of $\mathbb{C}$ (see [the Background](/learn/l-functions/#dirichlet-l-functions)), and $\mathrm{ord}_\rho$ for the order of vanishing of $L(s, \chi)$ at $\rho$.

**Definition 2.4.1 (Zeros in a box and in a disc).** For real $\sigma$ and $T$, let $Z(\chi; \sigma, T)$ be the set of $\rho$ with $\sigma \leq \mathrm{Re}\,\rho < 1$, $|\mathrm{Im}\,\rho| \leq T$ and $L(\rho, \chi) = 0$, and put
$$N(\sigma, T, \chi) = \sum_{\rho \in Z(\chi; \sigma, T)} \mathrm{ord}_\rho.$$
For $c \in \mathbb{C}$ and $R > 0$, let $D(\chi; c, R)$ be the set of zeros $w$ of $L(s, \chi)$ with $|w - c| \leq R$, where $w \neq 1$ if $\chi$ is principal.

**Definition 2.4.2 (Prime sums).** For $N \leq y$ and real $\tau$ put
$$P_\chi(N, y; \tau) = \sum_{N < p \leq y} \frac{\log p}{p}\, \chi(p)\, p^{-i\tau},$$
where $p$ runs over primes. For a function $c : \mathbb{N} \to \mathbb{C}$ and $k \geq 0$, put
$$D_k(c; s) = \sum_{n \geq 1} \Lambda(n)\, c(n) \frac{(\log n)^k}{k!}\, n^{-s}.$$

For $c = \chi$ the series $D_k(\chi; s)$ is $(-1)^{k}/k!$ times the $k$-th derivative of $\sum_n \Lambda(n)\chi(n)n^{-s} = -L'(s, \chi)/L(s, \chi)$. So a zero of $L$ close to $s$ makes $D_k(\chi; s)$ large for large $k$, by the term $\mathrm{ord}_\rho/(s - \rho)^{k+1}$.

We use four results from the literature on zeros of L-functions, which are proved elsewhere in the development. They are the steps of Gallagher's proof (see Notes and references).

**Theorem 2.4.3 (Few zeros in a small disc).** There is $C > 0$ such that for every $q$, every $\chi$ modulo $q$, every real $t$ with $\chi \neq 1$ or $|t| \geq 2$, and every $r$ with $0 < r \leq 1/2$, the set $D(\chi; 1 + it, r)$ is finite and
$$\sum_{w \in D(\chi; 1 + it, r)} \mathrm{ord}_w \leq C\bigl(1 + r\log(q(|t| + 2))\bigr).$$

Lean: `GlobalTheory.T.dirichletL_few_zeros_small_disc`.

**Theorem 2.4.4 (A zero makes a derivative large).** There are $A \geq 1$ and $C, r_0 > 0$ with the following property. Let $\chi$ be a character modulo $q$, let $\tau, r, L$ be real, let $K \geq 0$ be an integer, and let $\rho$ satisfy $L(\rho, \chi) = 0$ and $|\rho - (1 + i\tau)| \leq r$. Suppose $\chi \neq 1$ or $|\tau| \geq 2$, $\log(q(|\tau| + 2)) \leq L$, $1/L \leq r \leq r_0$ and $CrL \leq K$. Then there is an integer $k$ with $K \leq k \leq 2K$ and
$$\bigl|D_k(\chi; 1 + r + i\tau)\bigr| \geq \frac{1}{(Ar)^{k+1}}.$$

Lean: `GlobalTheory.T.exists_large_vonMangoldtLogPowerSeries_near_zero`.

**Theorem 2.4.5 (A large derivative gives a large prime sum).** For every $A \geq 1$ there are $a, b, C, r_0, K_0$ with $0 < a < b$, $C > 0$, $r_0 > 0$ and the following property. Let $c : \mathbb{N} \to \mathbb{C}$ satisfy $|c(n)| \leq 1$, let $0 < r \leq r_0$, and let $K_0 \leq K \leq k \leq 2K$ be integers with $|D_k(c; 1 + r)| \geq (Ar)^{-k-1}$. Put $N = e^{aK/r}$ and $M = e^{bK/r}$. Then
$$\frac{e^{-CK}}{r^3} \leq \int_N^M \Bigl|\sum_{N < p \leq y} \frac{\log p}{p}\, c(p)\Bigr|^2 \frac{dy}{y}.$$

Lean: `GlobalTheory.T.integral_prime_sum_sq_ge_of_derSeries_large`.

**Theorem 2.4.6 (Large sieve for primes).** There is $C > 0$ such that for every $q$, every $T \geq 1$, every $N$ with $(2qT)^2 \leq N$, every $y$ and every $a : \mathbb{N} \to \mathbb{C}$,
$$\sum_\chi \int_{-T}^{T} \Bigl|\sum_{N < p \leq y} a_p\, \chi(p)\, p^{-it}\Bigr|^2 dt \leq C \sum_{N < p \leq y} \frac{p\, |a_p|^2}{\log p}.$$

Lean: `GlobalTheory.T.primeMeanValue_characters_twist_integral_le`.

We also need that the principal L-function has no zeros close to $1$ at small height. Its zeros with $0 < \mathrm{Re}\, s < 1$ are those of the Riemann zeta function, and the classical zero-free region of $\zeta$ gives the following.

**Lemma 2.4.7 (Principal character).** There is $\eta > 0$ such that for every $q$, every zero $s$ of $L(s, \chi_0)$ with $1 - \eta \leq \mathrm{Re}\, s < 1$ has $|\mathrm{Im}\, s| \geq 3$. Here $\chi_0$ is the principal character modulo $q$.

Lean: `GlobalTheory.Lin.LogFree.principal_height`.

**Lemma 2.4.8 (Mean value of the prime sums).** There are $C > 0$ and $C_M \geq 0$ such that for all $q$, $T \geq 1$ and $1 \leq N \leq M$ with $(2qT)^2 \leq N$,
$$\sum_\chi \int_{-T}^{T} \int_N^M |P_\chi(N, y; \tau)|^2 \frac{dy}{y}\, d\tau \leq C(\log M + C_M)\log M.$$

Lean: `GlobalTheory.Lin.LogFree.mean_le`.

*Proof.* Exchange the integrals. For each $y$, the large sieve with $a_p = \log p/p$ bounds the inner sum over $\chi$ by $C\sum_{N < p \leq y} \log p/p$. By Mertens' theorem, $\sum_{p \leq y} \log p/p \leq \log y + C_M$. Integrate over $y \in [N, M]$ against $dy/y$; this gives a factor at most $\log M$. $\square$

**Lemma 2.4.9 (Counting by integration).** Let $Z$ be a finite set of complex numbers with weights $w \geq 0$. Let $F \geq 0$ be integrable on $[-U, U]$, and let $h, \delta, M_0 \geq 0$. Suppose that $|\mathrm{Im}\,\rho| + h \leq U$ for every $\rho \in Z$, and that for every $\rho \in Z$ and every $\tau$ with $|\tau - \mathrm{Im}\,\rho| \leq h$ we have $F(\tau) \geq \delta$ and $\sum_{z \in Z,\, |\tau - \mathrm{Im}\, z| \leq h} w(z) \leq M_0$. Then
$$2h\delta \sum_{\rho \in Z} w(\rho) \leq M_0 \int_{-U}^{U} F(\tau)\, d\tau.$$

Lean: `GlobalTheory.Lin.LogFree.count_le`.

*Proof.* Put $g = \sum_\rho \delta w(\rho)\mathbf{1}_{[\mathrm{Im}\rho - h, \mathrm{Im}\rho + h]}$. The integral of $g$ over $[-U, U]$ is $2h\delta\sum_\rho w(\rho)$. At each $\tau$ the value $g(\tau)$ is $\delta$ times the weight of the zeros within $h$ of $\tau$. If this set is not empty, then $g(\tau) \leq \delta M_0 \leq F(\tau) M_0$. So $g \leq M_0 F$. $\square$

**Proposition 2.4.10 (Density with parameters).** There are constants $a, D, C, C', r_0, K_0, \eta$, all positive except possibly $K_0$, with the following property. Let $q \geq 1$, $T \geq 2$, and let $\sigma, r, L$ be real and $K$ an integer with
$$\begin{aligned} &1 - \eta \leq \sigma, \quad 2(1 - \sigma) \leq r, \quad 0 < r \leq r_0, \quad 1/L \leq r, \quad \log(q(T + 3)) \leq L, \\ &C'rL \leq K, \quad K_0 \leq K, \quad 1 \leq K, \quad (2q(T + 1))^2 \leq e^{aK/r}. \end{aligned}$$
Then
$$\sum_\chi N(\sigma, T, \chi) \leq D(1 + rL)\, e^{CK} K^2.$$

Lean: `GlobalTheory.Lin.LogFree.count_param`.

*Proof.* Combine the theorem on a zero making a derivative large with the theorem on large derivatives with $c = \chi \cdot p^{-i\tau}$. This gives constants $a < b$, $C$, $C'$, $r_0$, $K_0$ such that the following holds, with $N = e^{aK/r}$ and $M = e^{bK/r}$: if $\chi \neq 1$ or $|\tau| \geq 2$, and $L(\rho, \chi) = 0$ with $|\rho - (1 + i\tau)| \leq r$, then
$$\int_N^M |P_\chi(N, y; \tau)|^2 \frac{dy}{y} \geq \frac{e^{-CK}}{r^3}.$$
Take $\eta$ from the lemma on the principal character, and replace $r_0$ by $\min(r_0, 1/2)$.

Fix $\chi$. Apply the counting lemma to $Z = Z(\chi; \sigma, T)$ with weights $\mathrm{ord}_\rho$, $U = T + 1$, $h = r/2$, $\delta = e^{-CK}/r^3$, and $F(\tau) = \int_N^M |P_\chi(N, y; \tau)|^2 dy/y$. We check its hypotheses. Let $\rho \in Z$ and $|\tau - \mathrm{Im}\,\rho| \leq r/2$. Since $\sigma \leq \mathrm{Re}\,\rho < 1$ and $2(1 - \sigma) \leq r$, we get $|\rho - (1 + i\tau)| \leq (1 - \mathrm{Re}\,\rho) + r/2 \leq r$. If $\chi$ is principal, then $|\mathrm{Im}\,\rho| \geq 3$ by the lemma, so $|\tau| \geq 2$. Also $\log(q(|\tau| + 2)) \leq \log(q(T + 3)) \leq L$. So the detection bound gives $F(\tau) \geq \delta$. The zeros $z \in Z$ with $|\tau - \mathrm{Im}\, z| \leq r/2$ lie in the disc $D(\chi; 1 + i\tau, r)$, by the same estimate. By the theorem on few zeros, their weight is at most $M_0 = C_2(1 + rL)$. So
$$r\, \delta\, N(\sigma, T, \chi) \leq C_2(1 + rL) \int_{-T-1}^{T+1} F(\tau)\, d\tau.$$
Sum over $\chi$. The condition $(2q(T + 1))^2 \leq N$ allows the mean value lemma with $T + 1$ in place of $T$, and $\log M = bK/r$. Hence
$$\begin{aligned} \sum_\chi N(\sigma, T, \chi) &\leq e^{CK} r^2\, C_2(1 + rL)\, C_5\Bigl(\frac{bK}{r} + C_M\Bigr)\frac{bK}{r} \\ &\leq C_2 C_5 (b + C_M) b\, (1 + rL)\, e^{CK} K^2, \end{aligned}$$
since $r \leq 1$ and $K \geq 1$. This is the claim with $D = C_2C_5(b + C_M)b$. $\square$

**Theorem 2.4.11 (Log-free zero density estimate).** There are $A, C, \eta > 0$ such that for every $q \geq 1$, every $T \geq 2$ and every $\sigma$ with $1 - \eta \leq \sigma \leq 1$,
$$\sum_{\chi \bmod q} N(\sigma, T, \chi) \leq C(qT)^{A(1 - \sigma)}.$$

Lean: `GlobalTheory.Lin.LogFree.zero_density` (also `GlobalTheory.T.logFree_zeroDensity_dirichlet_one_modulus`, a second name).

*Proof.* Take the constants of the proposition, and let $E = C' + |K_0| + 4/a$. Replace $\eta$ by $\min(\eta, r_0/2)$. Choose
$$L = \log(q(T + 3)) + \frac{1}{r_0}, \qquad r = \max\Bigl(2(1 - \sigma), \frac{1}{L}\Bigr), \qquad K = \lceil E\, rL \rceil.$$
We check the hypotheses of the proposition. Since $1 - \sigma \leq \eta \leq r_0/2$ and $L \geq 1/r_0$, we have $r \leq r_0$. Since $rL \geq 1$, we get $K \geq E\, rL \geq C'rL$ and $K \geq E \geq |K_0|$. Also $K \geq 1$, since $ErL > 0$. Finally $aK/r \geq aEL \geq 4L \geq 4\log(q(T+3))$, so $e^{aK/r} \geq (q(T + 3))^4 \geq (2q(T + 1))^2$.

The proposition gives $\sum_\chi N(\sigma, T, \chi) \leq D(1 + rL)e^{CK}K^2$. Put $x = rL \geq 1$. Then $K \leq (E + 1)x$, and $(1 + x)K^2 \leq (E + 1)^2 e^{3x}$. So the sum is at most $D(E + 1)^2 e^{Bx}$ with $B = C(E + 1) + 3$. If $r = 1/L$, then $x = 1$. Otherwise $x = 2(1 - \sigma)L$, and $2(1 - \sigma)/r_0 \leq 1$; with $\log(q(T + 3)) \leq 3\log(qT)$ for $qT \geq 2$, this gives $x \leq 2 + 6(1 - \sigma)\log(qT)$ in both cases. Hence the sum is at most $D(E + 1)^2 e^{2B} (qT)^{6B(1 - \sigma)}$. This is the claim with $A = 6B$. $\square$

The point of the estimate is that it has no factor $\log(qT)$ in front. For $\sigma = 1 - O(1/\log(qT))$ it says that there are $O(1)$ zeros, while the classical bound $N(T, \chi) \ll T\log(qT)$ gives many more.

**Remark 2.4.12 (Formalization).** The four theorems on zeros and prime sums are separate formal results, proved elsewhere in the development. We have not checked their proofs. The detection step is the lemma `GlobalTheory.Lin.LogFree.detect` ([LogFreeZeroDensityDirichletOneModulus.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/LogFreeZeroDensityDirichletOneModulus.lean#L212)), and Mertens' theorem enters as `GlobalTheory.mertens_first_vonMangoldt`. The proposition asks for $(2q(T + 1))^2 \leq e^{aK/r}$ among its hypotheses; the theorem gets it from the choice of $K$. The wrapper `GlobalTheory.T.logFree_zeroDensity_dirichlet_one_modulus` is stated in a file of its own and proved by citing the theorem.
