---
title: Zero density and the Deuring-Heilbronn phenomenon
decls:
  - Formalism.HermitianLattices.Ext.PrimesInProgressions.Dens.log_density_bound
  - Formalism.HermitianLattices.Ext.PrimesInProgressions.logDensityM_proof'
  - Formalism.HermitianLattices.Ext.PrimesInProgressions.deuring_heilbronn_lossy
  - Formalism.HermitianLattices.Ext.PrimesInProgressions.deuringHeilbronnMB_proof'
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Zero density and the Deuring-Heilbronn phenomenon

This section proves two facts about the zeros of Dirichlet $L$-functions modulo $M$ near the line $\mathrm{Re}\, s = 1$. The first is a zero density estimate: the number of zeros with real part at least $\sigma$ and height at most $T$, over all characters modulo $M$, is at most $C(MT)^{24(1-\sigma)}\log^{10}(MT)$. The second is a form of the Deuring-Heilbronn phenomenon: if a real character has a real zero $\beta_1$ very close to $1$, then all other zeros are pushed away from $1$. Both results are inputs of the prime number theorem in progressions of the next section ([Theorem 6.2.3](/entry/pnt-progressions-relative-weak-holds/)). The Background on [zeros of Dirichlet L-functions](/learn/analytic-number-theory/#zeros-of-dirichlet-l-functions) states the classical forms.

Let $M \geq 1$. For a [[Dirichlet character|JR4QSEFXWF]] $\chi$ modulo $M$ let $L(s, \chi) = \sum_{n \geq 1}\chi(n)n^{-s}$ for $\mathrm{Re}\, s > 1$, continued meromorphically to $\mathbb{C}$. We do not assume that $\chi$ is primitive. Let $\chi_0$ be the trivial character modulo $M$. Then $L(s, \chi_0) = \zeta(s)\prod_{p \mid M}(1 - p^{-s})$ has a pole at $s = 1$, and $L(s, \chi)$ is entire for $\chi \neq \chi_0$. Put $F_\chi(s) = -L'(s, \chi)/L(s, \chi)$. For $\mathrm{Re}\, s > 1$, $F_\chi(s) = \sum_n \Lambda(n)\chi(n)n^{-s}$, where $\Lambda$ is the von Mangoldt function.

**Definition 6.1.1 (Zero of a character).** Let $\chi$ be a character modulo $M$. A complex number $\rho$ is a *zero of $\chi$* if $L(\rho, \chi) = 0$, and $\rho \neq 1$ when $\chi = \chi_0$.

**Definition 6.1.2 (Spaced set of zeros).** Let $\sigma \geq \frac{1}{2}$ and $T \geq 2$. A finite set $S$ of pairs $(\chi, \rho)$, with $\chi$ a character modulo $M$ and $\rho$ a zero of $\chi$, is *spaced in the box $(\sigma, T)$* if $\sigma \leq \mathrm{Re}\,\rho$ and $|\mathrm{Im}\,\rho| \leq T$ for each pair, and $|\mathrm{Im}\,\rho - \mathrm{Im}\,\rho'| \geq 1$ for any two distinct pairs $(\chi, \rho)$ and $(\chi, \rho')$ with the same character.

A spaced set counts zeros at most once in each window of height $1$. A maximal spaced set $S$ in the box contains, for each zero $\rho$ of $\chi$ in the box, a pair $(\chi, \rho')$ with $|\mathrm{Im}\,\rho - \mathrm{Im}\,\rho'| < 1$. Since a window of height $2$ contains $O(\log(MT))$ zeros, the number of all zeros in the box is $O(|S|\log(MT))$. So a bound for spaced sets is a zero density estimate, up to one factor $\log(MT)$.

**Theorem 6.1.3 (Log zero density).** There are constants $A$, $B$ and $C$ with the following property. Let $M \geq 3$, $T \geq 2$ and $\sigma \geq \frac{1}{2}$, and let $S$ be spaced in the box $(\sigma, T)$. Then
$$|S| \leq C\,(MT)^{A(1 - \sigma)}\log^B(MT).$$
One can take $A = 24$ and $B = 10$.

Lean: `Formalism.HermitianLattices.Ext.PrimesInProgressions.Dens.log_density_bound` (also `Formalism.HermitianLattices.Ext.PrimesInProgressions.logDensityM_proof'`, a second name).

*Proof.* Put $q = \lceil MT \rceil$, so $q \geq 6$ and $\log(MT) \geq 1$. Two facts hold for any spaced set. First, the imaginary parts of the zeros of one character in $S$ lie in $[-T, T]$ and are $1$ apart, so $|S| \leq M(2T + 1) \leq 3MT$. Second, a zero of $\chi$ with real part $\geq 1$ does not exist, because $L(s, \chi) \neq 0$ on $\mathrm{Re}\, s \geq 1$ away from the pole. We take $C = |C_0| + |C_1| + 3 + 3\max(q_0, q_1)$, where $C_0, q_0$ and $C_1, q_1$ come from the two counts below.

*Case $\sigma < \frac{3}{4}$.* Then $24(1 - \sigma) > 6$, so $(MT)^{24(1-\sigma)} \geq MT$, and $|S| \leq 3MT$ gives the claim.

*Case $\sigma \geq \frac{3}{4}$ and $q < \max(q_0, q_1)$.* Then $|S| \leq 3MT \leq 3\max(q_0, q_1)$, and the right side is at least this.

*Case $\sigma \geq \frac{3}{4}$ and $q \geq \max(q_0, q_1)$.* Split $S = S_0 \cup S_1$, where $S_0$ holds the pairs with $\chi = \chi_0$ and $S_1$ the others. We show $|S_i| \leq C_i (MT)^{24(1-\sigma)}\log^{10}(MT)$ by zero detection with a mollifier. Put $Y = q^3$, $J = 8(\lfloor\log_2 q\rfloor + 1)$ and $N = 2^J$, and for $n \geq 1$
$$a(n) = \sum_{\substack{de = n \\ d \leq Y,\ e \leq N}}\mu(d).$$
Since $N > Y$, $a(1) = 1$ and $a(n) = \sum_{d \mid n}\mu(d) = 0$ for $1 < n \leq Y$. For $U \geq 1$ put $B_U(s, \chi) = \sum_{U < n \leq 2U}a(n)\chi(n)n^{-s}$.

1. *Detection.* Let $\chi \neq \chi_0$, and let $\rho$ be a zero of $\chi$ with $\mathrm{Re}\,\rho \geq \frac{3}{4}$ and $|\mathrm{Im}\,\rho| \leq T$. Then $|B_U(\rho, \chi)| \geq 1/(2J)$ for some $U = Y2^j$ with $j < J$. The reason: $\sum_{n \leq YN}a(n)\chi(n)n^{-\rho}$ is the product of $\sum_{d \leq Y}\mu(d)\chi(d)d^{-\rho}$ and a partial sum of $L(\rho, \chi) = 0$ of length $N$, so it is small. Its term $n = 1$ is $1$, the terms $1 < n \leq Y$ vanish, and the rest is the sum of the $J$ blocks $B_{Y2^j}$. For $\chi = \chi_0$ the same works with the alternating series $(1 - 2^{1-s})\zeta(s) = \sum_{n \leq 2K}n^{-s} - 2^{1-s}\sum_{n \leq K}n^{-s} + O((1 + |s|/\mathrm{Re}\, s)K^{-\mathrm{Re}\, s})$, because a zero of $\chi_0$ with positive real part is a zero of $\zeta$. The lower bound is then $c/((J + 1)\log q)$.
2. *Large values.* Fix $U$. The coefficients satisfy $\sum_{U < n \leq 2U}|a(n)|^2n^{-2\sigma} \leq 2U^{1 - 2\sigma}(1 + \log 2U)^3$, by the bound $\sum_{n \leq x}d(n)^2 \leq x(1 + \log x)^3$ for the divisor function. For two pairs of $S$ the sum $\sum_{U < n \leq 2U}\chi(n)\bar\chi'(n)n^{-w}$, with $w = (\rho - \sigma) + \overline{(\rho' - \sigma)}$, is at most $4(M + 1)(1 + |w|)$ when $\chi \neq \chi'$, and is at most $4U^{1 - \mathrm{Re}\, w}/|\mathrm{Im}\, w| + 4(M + 1)(1 + |w|)$ when $\chi = \chi'$ and $\rho \neq \rho'$. With the spacing, the sum over $\rho'$ is at most $U(9 + 8\log(2T + 1)) + 8|S|(M + 1)(2 + 2T)$. The duality principle for Dirichlet polynomials (the dual form of the large sieve) then gives
$$\#\{(\chi, \rho) \in S : |B_U(\rho, \chi)| \geq \theta\} \leq \frac{4U^{2 - 2\sigma}(1 + \log 2U)^3(9 + 8\log(2T + 1))}{\theta^2},$$
provided the term with $|S|$ is at most half of the diagonal. Since $U \geq Y = q^3$ and $\sigma \geq \frac{3}{4}$, this proviso holds for $q \geq q_i$.
3. *Summation.* Each pair of $S_1$ is detected by one of $J$ blocks, with $\theta = 1/(2J)$. Since $U \leq Y2^J \leq 2^8q^{11}$, we have $U^{2 - 2\sigma} \ll (MT)^{24(1 - \sigma)}$. The factors $J$, $\theta^{-2}$, $(1 + \log 2U)^3$ and $\log(2T + 1)$ give at most $\log^{10}(MT)$ up to a constant. The same holds for $S_0$.

Adding the two bounds proves the theorem. $\square$

We now turn to the repulsion of zeros. The classical statement is in the Background ([Deuring and Heilbronn](/learn/analytic-number-theory/#zeros-of-dirichlet-l-functions)): with $\mathcal{L} = \log(q(|\gamma| + 2))$, every zero $\beta + i\gamma \neq \beta_1$ satisfies $\beta \leq 1 - (c_1/\mathcal{L})\log(c_2/((1 - \beta_1)\mathcal{L}))$; see Iwaniec and Kowalski, Chapter 18. We prove a weaker form with a power of the logarithm.

**Theorem 6.1.4 (Deuring-Heilbronn phenomenon, weak form).** There are $c_0, c_1, c_2 > 0$ and an integer $B \geq 0$ with the following property. Let $M \geq 3$ and $T \geq 2$. Let $\chi_1 \neq \chi_0$ be a character modulo $M$ with $\chi_1^2 = \chi_0$, and let $\beta_1$ be real with $L(\beta_1, \chi_1) = 0$ and $1 - c_1/\log(MT) < \beta_1 < 1$. Let $\chi$ be a character modulo $M$ and $\rho$ a zero of $\chi$ with $\mathrm{Re}\,\rho \geq 1 - c_0$, $|\mathrm{Im}\,\rho| \leq T$ and $(\chi, \rho) \neq (\chi_1, \beta_1)$. Then
$$1 - \mathrm{Re}\,\rho \geq \frac{c_2}{\log(MT)}\log\frac{c_1}{(1 - \beta_1)\log^B(MT)}.$$
One can take $B = 3$.

Lean: `Formalism.HermitianLattices.Ext.PrimesInProgressions.deuring_heilbronn_lossy` (also `Formalism.HermitianLattices.Ext.PrimesInProgressions.deuringHeilbronnMB_proof'`, a second name).

The right side is negative unless $1 - \beta_1 < c_1\log^{-B}(MT)$. So the theorem says something only when $\beta_1$ is very close to $1$, and then it says that the other zeros are at distance $\gg \log(1/((1 - \beta_1)\log^B(MT)))/\log(MT)$ from $1$. The proof uses two lemmas.

**Lemma 6.1.5 (Positivity).** Let $\chi_1$ and $\chi$ be characters modulo $M$ with $\chi_1^2 = \chi_0$. Let $\sigma > 1$, $\gamma$ real and $k \geq 0$. Then
$$\bigl|F_\chi^{(k)}(\sigma + i\gamma) + F_{\chi\chi_1}^{(k)}(\sigma + i\gamma)\bigr| \leq (-1)^k\bigl(F_{\chi_0}^{(k)}(\sigma) + F_{\chi_1}^{(k)}(\sigma)\bigr).$$

Lean: `Formalism.HermitianLattices.Ext.PrimesInProgressions.deuring_heilbronn_dominant`.

*Proof.* Differentiate the Dirichlet series: $(-1)^kF_\psi^{(k)}(s) = \sum_n \Lambda(n)(\log n)^k\psi(n)n^{-s}$. So the left side is $|\sum_n \Lambda(n)(\log n)^k\chi(n)(1 + \chi_1(n))n^{-\sigma - i\gamma}|$. For $(n, M) = 1$ we have $\chi_1(n) = \pm 1$, so $1 + \chi_1(n) \in \{0, 2\}$, and $|\chi(n)| = 1$. For $(n, M) > 1$ the term is $0$. The triangle inequality bounds the sum by $\sum_n \Lambda(n)(\log n)^k(\chi_0(n) + \chi_1(n))n^{-\sigma}$, which is the right side. $\square$

**Lemma 6.1.6 (Turán's power sum inequality).** There are $C > 0$ and an integer $A \geq 1$ with the following property. Let $n \geq 1$ and $m \geq 0$ be integers, and let $z_1, \ldots, z_n$ be complex numbers with $|z_i| \leq 1$ for all $i$ and $|z_i| = 1$ for some $i$. Then there is an integer $k$ with $m + 1 \leq k \leq m + An$ and
$$\Bigl|\sum_{i=1}^n z_i^k\Bigr| \geq \Bigl(\frac{n}{C(m + n)}\Bigr)^{An}.$$
One can take $C = 1600$ and $A = 1$.

Lean: `Formalism.HermitianLattices.Ext.PrimesInProgressions.turan_power_sum_bound`.

This is a weak form of Turán's second main theorem, which gives $(n/(8e(m + n)))^n$; see Montgomery, *Ten Lectures on the Interface between Analytic Number Theory and Harmonic Analysis*, Chapter 5.

*Proof of the theorem.* We give the main steps. Let $(\chi, \rho)$ be as in the theorem, put $\mathcal{L} = \log(MT)$, and fix a small $\eta > 0$.

1. *Local expansion.* By Jensen's formula and Cauchy's estimates in a disc of radius $\frac{4}{25}$ around $\frac{26}{25} + i\,\mathrm{Im}\,\rho$, the function $F_\chi + F_{\chi\chi_1}$ near $s = 1 + \eta + i\,\mathrm{Im}\,\rho$ is $\sum_{\rho'}(s - \rho')^{-1}$ over the $O(\mathcal{L})$ zeros $\rho'$ in the disc, plus a holomorphic part bounded by $O(\mathcal{L})$. Put $w = s - \rho'$. Then $\mathrm{Re}\, w \geq \eta$ for every $w$, and $\rho$ itself gives $w = \eta + (1 - \mathrm{Re}\,\rho)$. The $(j-1)$-th derivative turns the expansion into a bound for $|\sum w^{-j}|$ by $(-1)^{j-1}(F_{\chi_0} + F_{\chi_1})^{(j-1)}(1 + \eta)/(j-1)!$, plus $2j(1 - \beta_1)/\eta^{j+1}$ and $O(\mathcal{L}\,25^j)$. The positivity lemma is the step that replaces the complex point by the real point $1 + \eta$.
2. *The real side.* At real $\sigma \in (1, 2]$ the $k$-th derivative of $F_{\chi_0} + F_{\chi_1}$ has the Dirichlet coefficients $\Lambda(n)(\log n)^k(1 + \chi_1(n))$. Their size is governed by $\sum (1 * \chi_1)(n)/n$ over $y < n \leq x$, which is at most $|L(1, \chi_1)|\log(x/y) + CM(\log y + 1)/\sqrt{y}$. Since $L(\beta_1, \chi_1) = 0$, $|L(1, \chi_1)| \ll (1 - \beta_1)\log^2(3M)$. This bounds the $k$-th derivative by $O((1 - \beta_1)\log^2(3M)(k + 2)^2/(\sigma - 1)^{k+2})$ plus terms $(C\log 3M)^{k+1}/k!$ and $C(k + 2)\log^2(3M)/(M(\sigma - 1)^{k+1})$.
3. *Turán.* Apply the power sum lemma to $z = w_{\min}/w$, where $w_{\min}$ is the smallest $|w|$. It gives a $k$ in a range of length $O(\mathcal{L})$ where $|\sum w^{-k}|$ is at least $|w_{\min}|^{-k}e^{-O(\mathcal{L})}$, and $|w_{\min}| \leq \eta + 1 - \mathrm{Re}\,\rho$. Steps 1 and 2 bound the same sum from above by $(1 - \beta_1)$ times a power of $\mathcal{L}$, plus terms that are small for this $k$. Comparing the two bounds and choosing $\eta$ of size $1/\mathcal{L}$ gives the claim.
4. *Constants.* The zero-free region with one exception gives $1 - \mathrm{Re}\,\rho \geq c/(2\mathcal{L})$ for every $(\chi, \rho) \neq (\chi_1, \beta_1)$, when $c_1$ is small. Siegel's bound $\beta_1 \leq 1 - c(\frac{1}{2})M^{-1/2}$ bounds $\log(1/(1 - \beta_1))$ by $O(\log M)$. These two facts fix the constants $c_0$, $c_1$ and $c_2$.

$\square$

**Remark 6.1.7 (Formalization).** The theorem names `logDensityM_proof'` and `deuringHeilbronnMB_proof'` in [PNTFinal.lean](lean:Formalism/GL3MeanSquares/GenusMeanAsymptotics/JacobiCharacterSums/PNTFinal.lean#L18) only rename `Dens.log_density_bound` and `deuring_heilbronn_lossy`. The density statement counts spaced sets, not zeros with multiplicity. Characters are not assumed primitive, and $L(s, \chi)$ is Mathlib's $L$-function of the character modulo $M$; the condition $\rho \neq 1$ for $\chi_0$ excludes the value that Mathlib assigns at the pole. [DeuringHeilbronnM.lean](lean:Formalism/GL3MeanSquares/GenusMeanAsymptotics/JacobiCharacterSums/DeuringHeilbronnM.lean#L84) also states the classical repulsion with $B = 1$ (`DeuringHeilbronnM`); it is used only in `ZeroSumOf` (line 110), which no proof uses. The detection lemmas, the large values bound and the inputs of steps 1 and 2 of the second proof are proved in their own files; we have opened their statements, and the proofs above give only their main steps.
