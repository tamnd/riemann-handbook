---
title: The truncated explicit formula
decls:
  - explicitFormula_closed
  - explicitFormula_of
  - PI.EF.explicitFormula_main
  - PI.EF.explicitFormula_of_local
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The truncated explicit formula

This section proves the truncated explicit formula for $\psi(u, \chi)$, for a primitive [[Dirichlet character|JR4QSEFXWF]] $\chi$. It writes the prime sum as a sum over the zeros of the [[Dirichlet L-function|24GAZHVTGB]] $L(s, \chi)$ of height less than $T$, with an error that is explicit in the modulus, in $u$ and in $T$. The formula is the analytic input of the bound for twisted prime sums of [the next section](/entry/psi-thin/). The Background section on [the explicit formula](/learn/analytic-number-theory/#the-explicit-formula) gives the idea; here every constant is uniform in the modulus.

Throughout, $N \geq 1$ is an integer and $\chi$ is a Dirichlet character modulo $N$. We write $\chi_0$ for the trivial character, $\delta_\chi = 1$ if $\chi = \chi_0$ and $\delta_\chi = 0$ otherwise, and $\varepsilon_\chi = 1$ if $\chi$ is even and $\chi \neq \chi_0$, and $\varepsilon_\chi = 0$ otherwise. For $\rho \in \mathbb{C}$ let $m(\rho)$ be the order of the zero of $L(s, \chi)$ at $\rho$ (it is $0$ if $L(\rho, \chi) \neq 0$).

**Definition 6.3.1 (Zeros below a height).** For real $T$ let
$$Z(\chi, T) = \{\rho \in \mathbb{C} : 0 < \mathrm{Re}\,\rho < 1,\ |\mathrm{Im}\,\rho| < T,\ L(\rho, \chi) = 0\},$$
and for real $t$ let $Z^{\ast}(\chi, t)$ be the set of zeros $\rho$ with $0 < \mathrm{Re}\,\rho < 1$ and $|\mathrm{Im}\,\rho - t| \leq 1$. Put
$$\psi_0(u, \chi) = \sum_{1 \leq n \leq u}\Lambda(n)\chi(n) - \delta_\chi u, \qquad S_1(\chi) = \sum_{\rho \in Z(\chi, 1)}\frac{m(\rho)}{|\rho|}.$$

Lean: `PI.ZerosBelow`, `PI.ZerosNear`, `PI.psi0`, `PI.EF.S1`.

The sum $S_1(\chi)$ is finite for primitive $\chi$ by the next lemma. It is large only when $L(s, \chi)$ has a zero close to $0$; by the functional equation, $1 - \bar\rho$ is then a zero of $L(s, \bar\chi)$ close to $1$, that is, an exceptional zero.

**Lemma 6.3.2 (Zeros in a window).** There is $C_w > 0$ such that for every $N \geq 1$, every primitive character $\chi$ modulo $N$ and every real $t$, the set $Z^{\ast}(\chi, t)$ is finite and
$$\sum_{\rho \in Z^{\ast}(\chi, t)} m(\rho) \leq C_w\log(N(|t| + 2)).$$

Lean: `zerosWindow_closed` (also `zerosWindow_of`, the same bound from the three inequalities of the next lemma).

*Proof.* This is the classical count of the zeros in a window of height $2$ (Davenport, Chapter 16). One applies Jensen's formula to $L(s, \chi)$, or to $(s - 1)\zeta(s)$ when $\chi = \chi_0$, on a disc with center $2 + it$. The value at the center is at least $1/2$ in absolute value by the third bound of the next lemma. On a larger disc the function is at most a power of $N(|t| + 2)$, by the first two bounds of the next lemma for $\mathrm{Re}\,s > 0$ and the functional equation for $\mathrm{Re}\,s \leq 0$. Jensen's formula then bounds the number of zeros in a smaller disc, which contains $Z^{\ast}(\chi, t)$, by a constant times $\log(N(|t| + 2))$. $\square$

**Lemma 6.3.3 (Bounds in the right half plane).** Let $q \geq 1$ and let $\chi$ be a character modulo $q$.

1. If $\chi \neq \chi_0$ and $\mathrm{Re}\,s > 0$, then $|L(s, \chi)| \leq 1 + 2(q + 1)(1 + |s|/\mathrm{Re}\,s)$.
2. If $\mathrm{Re}\,s > 0$ and $s \neq 1$, then $|\zeta(s)| \leq 1 + 1/|s - 1| + |s|(1 + 1/\mathrm{Re}\,s)$.
3. If $\mathrm{Re}\,s > 1$, then $|L(s, \chi)|^{-1} \leq \mathrm{Re}\,s/(\mathrm{Re}\,s - 1)$.

Lean: `chk_lBoundRight`, `chk_zetaBoundRight`, `chk_lInvRight`.

*Proof.* Let $\sigma = \mathrm{Re}\,s$. For 1, let $A(x) = \sum_{n \leq x}\chi(n)$. Then $|A(x)| \leq q$ since $\chi$ sums to $0$ over each full period, and partial summation gives $L(s, \chi) = s\int_1^\infty A(x)x^{-s-1}\,dx$, so $|L(s, \chi)| \leq q|s|/\sigma$. For 2, $\zeta(s) = s/(s - 1) - s\int_1^\infty\{x\}x^{-s-1}\,dx$ for $\sigma > 0$, and $s/(s - 1) = 1 + 1/(s - 1)$. For 3, $1/L(s, \chi) = \sum_n\mu(n)\chi(n)n^{-s}$, so $|L(s, \chi)|^{-1} \leq \zeta(\sigma) \leq 1 + \int_1^\infty x^{-\sigma}\,dx = \sigma/(\sigma - 1)$. $\square$

**Lemma 6.3.4 (Holomorphic functions on a disc).** Let $f$ be holomorphic on a neighborhood of the closed disc $\bar D(z_0, r)$ (more exactly, complex differentiable on the closed disc), with $f(z_0) \neq 0$, and let $0 < R_1 < r$.

1. There are a finite set $Z$, multiplicities $m(\rho) \geq 1$ for $\rho \in Z$, and a function $h$, complex differentiable on $\bar D(z_0, r)$ and without zeros on $\bar D(z_0, R_1)$, such that $Z$ is the set of zeros of $f$ in $\bar D(z_0, R_1)$ and $f(z) = h(z)\prod_{\rho \in Z}(z - \rho)^{m(\rho)}$ on $\bar D(z_0, r)$.
2. If $f$ has no zeros on the open disc $D(z_0, R)$, there is $g$ with $g(z_0) = 0$, $g' = f'/f$ and $f = f(z_0)e^{g}$ on $D(z_0, R)$.

Lean: `chk_discFactor`, `chk_discLog`.

*Proof.* For 1, the zeros of $f$ in the compact disc $\bar D(z_0, R_1)$, which lies in the open disc $D(z_0, r)$, are isolated since $f(z_0) \neq 0$, so they are finite. Divide by $\prod(z - \rho)^{m(\rho)}$, with $m(\rho)$ the orders. For 2, let $g$ be a primitive of $f'/f$ on the disc with $g(z_0) = 0$; then $fe^{-g}$ has derivative $0$. $\square$

**Lemma 6.3.5 (Local form of the logarithmic derivative).** There is $C > 0$ with the following property. Let $N \geq 1$, let $\chi$ be primitive modulo $N$, and let $s$ satisfy $-1/2 \leq \mathrm{Re}\,s \leq 3$, $s \neq 1$ and $L(s, \chi) \neq 0$. Then
$$\Bigl|\frac{L'}{L}(s, \chi) - \sum_{\rho \in Z^{\ast}(\chi, \mathrm{Im}\,s)}\frac{m(\rho)}{s - \rho} - \frac{\varepsilon_\chi}{s} + \frac{\delta_\chi}{s - 1}\Bigr| \leq C\log(N(|\mathrm{Im}\,s| + 2)).$$

Lean: `PI.EF.localLemma_of_helpers` (also `PI.EF.localLemma_of`, `PI.EF.localAbstract_of`, `PI.EF.lGrowth_of`).

*Proof.* Let $f(s) = L(s, \chi)$ if $\chi \neq \chi_0$ and $f(s) = (s - 1)\zeta(s)$ if $\chi = \chi_0$; it is entire. Let $t = \mathrm{Im}\,s$ and $s_0 = 2 + it$. We use a disc lemma, proved from the previous lemma: for $0 < r < R' < R$ there is $C_0$ such that if $f$ is holomorphic on $\bar D(s_0, R)$, $f(s_0) \neq 0$, $M \geq 0$ and $|f| \leq e^M|f(s_0)|$ on $\bar D(s_0, R)$, then
$$\Bigl|\frac{f'}{f}(s) - \sum_{|\rho - s_0| \leq R'}\frac{m(\rho)}{s - \rho}\Bigr| \leq C_0M \qquad (|s - s_0| \leq r).$$
Take $r = 5/2$, $R' = 11/4$ and $R = 6$. The disc $\bar D(s_0, 6)$ lies in $-4 \leq \mathrm{Re}\,s \leq 8$. There $|f(s)| \leq 300000\,(N(|t| + 2))^7$, by the first two bounds of the previous lemma and the functional equation of $L(s, \chi)$ for primitive $\chi$. At the center, $|f(s_0)| \geq 1/2$ by the third bound. So we may take $M = |\log 600000| + 7\log(4N(|t| + 2))$. Each $s$ in the strip $-1/2 \leq \mathrm{Re}\,s \leq 3$ with imaginary part $t$ lies in $\bar D(s_0, 5/2)$. The zeros in $\bar D(s_0, 11/4)$ are of three kinds. The zeros in $Z^{\ast}(\chi, t)$ give the sum in the statement. The other zeros in the critical strip have $|\mathrm{Im}(s - \rho)| > 1$; each term is at most $m(\rho)$, and by the lemma on zeros in a window there are $O(\log(N(|t| + 2)))$ of them. The zeros outside the critical strip with $\mathrm{Re}\,\rho \geq -3/2$ are only $0$ (when $\varepsilon_\chi = 1$) and $-1$ (when $\chi$ is odd), and $-1$ is never in the disc. The zero at $0$ gives the term $\varepsilon_\chi/s$. For $\chi = \chi_0$ the factor $s - 1$ gives the term $\delta_\chi/(s - 1)$. All other errors are $O(M)$. The constant is $C_0(2|\log 600000| + 21) + 4C_w + 2$. $\square$

The heart of the explicit formula is a contour shift. Let $c = 1 + 1/\log u$ and, for $T' > 0$,
$$V(u, T') = \frac{1}{2\pi}\int_{-T'}^{T'}\Bigl(-\frac{L'}{L}(c + it, \chi)\Bigr)\frac{u^{c + it}}{c + it}\,dt.$$
A height $T'$ is *good* for the constant $\kappa$ if $\bigl||\mathrm{Im}\,\rho| - T'\bigr| \geq 1/(\kappa\log(NT'))$ for each zero $\rho$ with $0 < \mathrm{Re}\,\rho < 1$. Put $E(N, u, T) = u\log^2(NuT)/T + \log(Nu)$.

**Lemma 6.3.6 (The sides of the rectangle).** Let $\kappa > 0$, $C_1 > 0$, $C_2 > 0$. Assume that for every primitive $\chi$ modulo $N$, every good height $T' \geq 2$ and every $-1/2 \leq \sigma \leq 3$,
$$\Bigl|\frac{L'}{L}(\sigma \pm iT', \chi)\Bigr| \leq C_1\log^2(NT'),$$
and that $|L'/L(-1/2 + it, \chi)| \leq C_2\log(N(|t| + 2))$ for all real $t$. Then for $2 \leq T \leq u$ and every good $T' \in [T, T + 1]$, the integral of $(L'/L)(s, \chi)u^s/s$ over the bottom, top and left sides of the rectangle $[-1/2, c] \times [-T', T']$ is at most $(21C_1 + 8C_2)E(N, u, T)$ in absolute value.

Lean: `PI.EF.perron_gluing_sides`.

*Proof.* On the horizontal sides $|u^s/s| \leq u^c/T' \leq eu/T$, and the side has length less than $2$, so these sides give $O(C_1u\log^2(NuT)/T)$. On the left side $|u^s| = u^{-1/2}$, and $\int|L'/L(-1/2 + it)|\,dt/|{-1/2} + it|$ over $|t| \leq T'$ is $O(C_2\log(NT)\log T)$, which is $O(C_2E)$ since $T \leq u$. $\square$

**Proposition 6.3.7 (Explicit formula from the local lemma).** Assume the conclusions of the lemma on zeros in a window (with a constant $C_w > 0$) and of the lemma on the local form of $L'/L$ (with some constant $C > 0$), and the conclusion of the lemma on the sides of the rectangle for every $\kappa$, $C_1$, $C_2$. Then the conclusion of the theorem below holds.

Lean: `PI.EF.explicitFormula_of_local`.

**Theorem 6.3.8 (Truncated explicit formula).** There is $C > 0$ with the following property. Let $N \geq 1$, let $\chi$ be a primitive character modulo $N$, and let $u$ and $T$ be real with $2 \leq T \leq u$. Then $Z(\chi, T)$ is finite and
$$\Bigl|\psi_0(u, \chi) + \sum_{\rho \in Z(\chi, T)} m(\rho)\frac{u^\rho}{\rho}\Bigr| \leq C\Bigl(\frac{u\log^2(NuT)}{T} + \log(Nu) + S_1(\chi)\Bigr).$$

Lean: `explicitFormula_closed` (also `explicitFormula_of`, the same conclusion with the six inputs above as hypotheses, and `PI.EF.explicitFormula_main`, of which `explicitFormula_of` is a second name).

*Proof.* We prove the proposition; the theorem follows, since its inputs are the lemmas above. Let $\kappa = 12C_w + 4$.

*Good heights.* Every $T \geq 2$ has a good height $T' \in [T, T + 1]$. Indeed, the zeros with $T - 1 \leq |\mathrm{Im}\,\rho| \leq T + 2$ number $O(C_w\log(NT))$ by the lemma on zeros in a window. The excluded intervals around their ordinates have length $2/(\kappa\log(NT'))$ each, so for this $\kappa$ their total length is less than $1$.

*Bounds for $L'/L$.* At a good height, the local lemma writes $L'/L(\sigma \pm iT')$ as a sum of $O(C_w\log(NT'))$ terms $m(\rho)/(s - \rho)$, each of size at most $\kappa\log(NT')$, plus $O(\log(NT'))$. This gives the first hypothesis of the lemma on the sides with $C_1 = 4C + 2C_w\kappa + 16$. On the line $\mathrm{Re}\,s = -1/2$ every zero in the critical strip is at distance more than $1/2$, which gives the second hypothesis with $C_2 = C + 2C_w + 6$.

*The decomposition.* Fix $u$, $T$ and a good $T' \in [T, T + 1]$, and let $z(T) = \sum_{\rho \in Z(\chi, T)}m(\rho)u^\rho/\rho$. Then
$$\begin{aligned}\psi_0(u, \chi) + z(T) = {} & \Bigl(\sum_{n \leq u}\Lambda(n)\chi(n) - V(u, T')\Bigr) + \bigl(V(u, T') - \delta_\chi u + z(T')\bigr) \\ & - \bigl(z(T') - z(T)\bigr).\end{aligned}$$
We bound the three terms.

*Perron's formula.* Since $-L'/L(s, \chi) = \sum_n\Lambda(n)\chi(n)n^{-s}$ for $\mathrm{Re}\,s > 1$, the truncated Perron formula on the line $\mathrm{Re}\,s = c$ gives $|\sum_{n \leq u}\Lambda(n)\chi(n) - V(u, T')| \leq 500\,E(N, u, T)$. It uses the bound $|\frac{1}{2\pi}\int_{-T}^{T}y^{c + it}\,dt/(c + it) - [y \geq 1]| \leq y^c\min(2, 1/(T|\log y|))$ for each term and the sum $\sum_n\Lambda(n)(u/n)^c\min(2, 1/(T|\log(u/n)|)) \ll u\log^2u/T + \log u$.

*The contour shift.* Let $H$ be the regular part of $L'/L$ on the rectangle $[-1/2, c] \times [-T', T']$, that is,
$$\frac{L'}{L}(s, \chi) = H(s) + \sum_{\rho \in Z(\chi, T')}\frac{m(\rho)}{s - \rho} + \frac{\varepsilon_\chi}{s} - \frac{\delta_\chi}{s - 1},$$
with $H$ holomorphic on the rectangle. The residue theorem gives
$$\begin{aligned}\oint\frac{L'}{L}(s, \chi)\frac{u^s}{s}\,ds = 2\pi i\Bigl(& H(0) + z(T') - \sum_{\rho \in Z(\chi, T')}\frac{m(\rho)}{\rho} \\ & + \varepsilon_\chi\log u - \delta_\chi(u - 1)\Bigr).\end{aligned}$$
The right side of the contour is $-2\pi i\,V(u, T')$, and the other three sides are $O(E)$ by the lemma on the sides. The local lemma at $s = 0$ and the window bound give $|\sum_{\rho \in Z(\chi, T')}m(\rho)/\rho - H(0)| \leq (C_w + C)\log(2N) + S_1(\chi)$. The terms $\varepsilon_\chi\log u$ and $\delta_\chi$ are at most $\log u + 1$. Hence $|V(u, T') - \delta_\chi u + z(T')| \leq C_s(E + S_1(\chi))$ with $C_s = 21C_1 + 8C_2 + C_w + C + 3$.

*Change of height.* The zeros with $T \leq |\mathrm{Im}\,\rho| < T'$ lie in at most two windows of the lemma on zeros in a window, so they number at most $2C_w\log(N(T + 3))$, and each has $|u^\rho/\rho| \leq u/T$. So $|z(T') - z(T)| \leq 4C_wE$.

Adding the three bounds gives the theorem with the constant $500 + C_s + 4C_w$. $\square$

The classical form of the theorem is the formula for $\psi(x, \chi)$ in Davenport, Chapter 19. There the zeros near $0$ are treated by hand. Here they are kept in the term $S_1(\chi)$, which the user of the formula must bound; in [the next section](/entry/psi-thin/) it is bounded with the zero-free region and the hypothesis that there is no exceptional zero.

**Remark 6.3.9 (Formalization).** The four names of the section are one result. [ExplicitFormula.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/ExplicitFormula.lean#L8) is a pure alias of `PI.EF.explicitFormula_main`, and `explicitFormula_closed` only fills in the six analytic inputs, which are proved in `AnalyticInputs.lean` by results of other chapters. The theorem is stated for primitive characters only; $\psi_0$ uses $\chi(n)$ for all $n$, and $m(\rho)$ is the analytic order of Mathlib's $L$-function. The local lemma uses the constant `max 300000 53946` at [LocalLemmaOfHelpers.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ExplicitFormula/LocalLemmaOfHelpers.lean#L18), which is just $300000$. We have opened the statements of the step lemmas (`PerronL`, `ShiftBound`, `TruncChange`, `GoodHeightExists`, `SidesBound`, `RegAtZero`, `LGrowth` and their constants), and the proof above follows them. We have not opened the proofs of the window count (`PI.ZW.zerosWindow_of_transfer`), of the disc lemma `Loc.local_abstract`, or of the bounds in the right half plane; the proofs given for these are the classical ones.
