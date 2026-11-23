---
title: The rest terms at one prime
decls:
  - GroundTheory.Heights₂.Heights.RestTerms.RestPrimeBound.full
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The rest terms at one prime

This section bounds the contribution $M(p)$ of one large prime $p$ to the rest terms. The rest terms are flag integrals, in the sense of [the previous section](/entry/lemma-a-full/), of one fixed polynomial $F_c$ against power sums. The bound has the form $|M(p)| \le 1.5\, f X (fra + 1)|D_c| \log p / p^2$, where $D_c$ is the flag integral of the fibre class and $X = 2(ra + r + a)$. The factor $\log p/p^2$ makes the bound summable over the primes. The sum is the subject of [the next section](/entry/rest-bound-full/), and the result goes into [the finite bound](/entry/finite-bound/) of the chapter on arithmetic volumes. The proof has two parts. The first bounds one rest term by the characters of symmetric groups. The second is a pair of elementary bounds on series.

### The rest polynomial

Fix integers $f, r, a \ge 1$ and put $N = r + a$. We use the ring $R_{f,N}$ of [the previous section](/entry/lemma-a-full/), its flag integral $\int$ and its power sums $p_k(\tau)$.

**Definition 4.2.1 (Small block).** A small block is one of two choices, $c = \mathrm{last}$ or $c = \mathrm{first}$, with sign $\epsilon_c = 1$ or $\epsilon_c = -1$. It splits the roots of each block $\tau$ into $r$ roots $y_{\tau,i}$ and $a$ roots $z_{\tau,i}$:

- for $c = \mathrm{last}$: $y_{\tau,i} = X_{\tau,a+i}$ and $z_{\tau,i} = X_{\tau,i}$;
- for $c = \mathrm{first}$: $y_{\tau,i} = -X_{\tau,i}$ and $z_{\tau,i} = X_{\tau,r+i}$.

**Definition 4.2.2 (Rest polynomial, fibre degree).** For a small block $c$ put
$$\mu = \sum_{\tau<f} \sum_{i<r} y_{\tau,i}, \qquad \Delta_c = \prod_{\tau<f} V(y_\tau)\, V(z_\tau).$$
The rest polynomial is $F_c = \mu^{fra+1}\Delta_c$ and the fibre degree is $D_c = \int \mu^{fra}\Delta_c$. The small power sums are $q_k(\tau) = \sum_{i<r} y_{\tau,i}^k$. Put $X = 2(ra + r + a)$.

The degree of $\Delta_c$ is $f(r(r-1)/2 + a(a-1)/2)$, and $fra$ more makes the top degree $f N(N-1)/2$. So $D_c$ is the flag integral of a polynomial of the top degree, and $F_c$ has degree one more than the top degree.

**Definition 4.2.3 (Rest term).** Let $(Q_{k,\tau})$ be a power sum decomposition of $F_c$. For $k \ge 1$, a block $\tau$ and $G \in R_{f,N}$, the rest term is
$$T(k, \tau, G) = k \int G\, Q_{k,\tau}.$$

By [Lemma A](/entry/lemma-a-full/), $T(k,\tau,G)$ does not depend on the decomposition when $G$ is homogeneous of degree $k-1$.

**Definition 4.2.4 (Prime term).** Let $s(p, n, \tau) < f$ be a choice of block and $e(p, n, \tau, k) \in \mathbb{Q}$ a choice of number, for all primes $p$, integers $n, k$ and blocks $\tau$. For a prime $p$ put
$$M(p) = \log p \sum_{\tau<f} \sum_{k=2}^{N} \sum_{n \ge 0} p^{-(n+1)k}\, e(p, n+1, \tau, k)\, T\bigl(k, \tau, q_{k-1}(s(p, n+1, \tau))\bigr).$$

The inner sum over $n$ converges absolutely when $|e| \le 1$, by Lemma (Series bounds) below.

### Characters and the bound for one term

We use the characters of the symmetric groups. For a partition $\lambda = (\lambda_0 \ge \dots \ge \lambda_{m-1})$ of $n$ and a list $\rho$ of positive integers with sum $n$, let $\chi^\lambda(\rho)$ be the coefficient of $x^{\lambda + \delta}$ in $V(x_0, \dots, x_{m-1}) \prod_j p_{\rho_j}(x)$, where $\delta = (m-1, m-2, \dots, 0)$. By the Frobenius formula this is the value of the irreducible character of $S_n$ indexed by $\lambda$ on the class of cycle type $\rho$ (Macdonald, Chapter I, §7). Let $f^\lambda$ be the number of standard Young tableaux of shape $\lambda$. Let $s_\nu$ be the Schur polynomial, given by the Jacobi-Trudi determinant $\det(h_{\nu_i - i + j})$. For a partition $\nu$ with at most $r$ parts, $a + \nu$ is the partition $(a + \nu_0, \dots, a + \nu_{r-1})$, and $(a^r)$ is the rectangle with $r$ rows of length $a$.

**Lemma 4.2.5 (Inputs on characters).** Let $r, a \ge 1$, $N = r + a$ and $1 \le k \le N$.

1. For every partition $\lambda$ and every $\rho$ as above, $|\chi^\lambda(\rho)| \le f^\lambda$.
2. Let $\nu$ be a partition of $k$ and $\epsilon = \pm 1$. Write $s_\nu(\epsilon x_0, \dots, \epsilon x_{N-1}) = \pi(S)$ with $\pi$ the power sum map. Then $[X_{k-1}] S = \epsilon^k (-1)^{\ell}/k$ if $\nu$ is a hook ($\nu_i \le 1$ for $i \ge 1$) with $\ell$ parts equal to $1$ after the first, and $[X_{k-1}]S = 0$ otherwise.
3. If numbers $b_\nu$ satisfy $|b_\nu| \le f^{a+\nu}$ for all partitions $\nu$ of $k$ with at most $r$ parts, then the sum of $|b_\nu|$ over the hooks among them is at most $\binom{ra+k}{k} 2^{k-1} f^{(a^r)}$.

Lean: `GroundTheory.Heights₂.Heights.RestTerms.CharacterBound.full` (also `GroundTheory.Heights₂.Heights.RestTerms.SchurSignCoefficient.full`, `GroundTheory.Heights₂.Heights.RestTerms.HookSumBound.full`)

Part 1 is the bound $|\chi(g)| \le \chi(1)$ for a character, with $\chi^\lambda(1^n) = f^\lambda$. Part 2 says that the coefficient of $p_k/k$ in $s_\nu$ is $\chi^\nu((k))$, which vanishes off the hooks. Part 3 bounds a sum of numbers of tableaux of the shapes $a + \nu$.

**Lemma 4.2.6 (Same-factor formula).** There is $C_0 \ne 0$ with
$$D_c = C_0\, \frac{(fra)!}{(ra)!^f}\, \bigl(f^{(a^r)}\bigr)^f,$$
such that for every power sum decomposition $Q$ of $F_c$, every $2 \le k \le N$ and every block $\tau$, there is $S$ with $\pi(S) = \sum_{\nu} \chi^{a+\nu}\bigl((k-1), 1^{ra+1}\bigr)\, s_\nu(\epsilon_c X)$, the sum over the partitions $\nu$ of $k$ with at most $r$ parts, and
$$T\bigl(k, \tau, q_{k-1}(\tau)\bigr) = C_0\, k\, \frac{(fra+1)!}{(ra+1)!\,(ra)!^{f-1}}\, \bigl(f^{(a^r)}\bigr)^{f-1}\, [X_{k-1}]S.$$

Lean: `GroundTheory.Heights₂.Heights.RestTerms.SameFactorFormula.full`

The proof goes through [Lemma A](/entry/lemma-a-full/): it computes the block $\tau$ part of the divided difference of $q_{k-1}(\tau) F_c$ with the Frobenius formula $p_q p_1^m = \sum_\lambda \chi^\lambda(q, 1^m) s_\lambda$ and a formula for the divided difference of $s_\lambda(y) V(y) V(z)$ in one block (Lemma B: it is $\pm r!\,a!\, s_{\lambda - a}(\epsilon_c X)$ if all $\lambda_i \ge a$, and $0$ otherwise). There is a second formula of the same kind for $\tau' \ne \tau$, when $f \ge 2$, with $\chi^{(a^r)}((k-1), 1^{ra-k+1})$ in the constant and $f^{a+\nu}$ in place of the character values.

**Proposition 4.2.7 (One rest term).** Let $(Q_{k,\tau})$ be a power sum decomposition of $F_c$, let $2 \le k \le N$, and let $\tau, \tau'$ be blocks. Then
$$\bigl|T\bigl(k, \tau, q_{k-1}(\tau')\bigr)\bigr| \le (fra+1)\, |D_c|\, \frac{X^{k-1}}{k!}.$$
Also $D_c \ne 0$, $F_c$ has a power sum decomposition, and for $\tau' \ne \tau$ the term vanishes when $ra < k - 1$.

Lean: `GroundTheory.Heights₂.Heights.RestTerms.SameFactorBound.full` (also `GroundTheory.Heights₂.Heights.RestTerms.OtherFactorBound.full`, for $\tau' \ne \tau$)

*Proof.* We give the case $\tau' = \tau$; the other case uses the second formula in the same way. Write $S = \sum_\nu \chi_\nu S_\nu$ with $\pi(S_\nu) = s_\nu(\epsilon_c X)$ and $\chi_\nu = \chi^{a+\nu}((k-1), 1^{ra+1})$; this is possible since $\pi$ is injective. By parts 1 and 2 of the inputs, $|[X_{k-1}]S| \le \frac1k \sum_{\nu \text{ hook}} |\chi_\nu|$ with $|\chi_\nu| \le f^{a+\nu}$. By part 3,
$$|[X_{k-1}]S| \le \frac1k \binom{ra+k}{k} 2^{k-1} f^{(a^r)}.$$
Put this into the same-factor formula and divide by the formula for $|D_c|$. The constants $C_0$, $(ra)!^{f-1}$ and $(f^{(a^r)})^{f-1}$ cancel, and $(fra+1)!/(fra)! = fra+1$. We get
$$\frac{|T(k,\tau,q_{k-1}(\tau))|}{|D_c|} \le (fra+1)\, \frac{(ra)!}{(ra+1)!} \binom{ra+k}{k} 2^{k-1} = (fra+1)\, \frac{(ra+k)!}{(ra+1)!\, k!}\, 2^{k-1}.$$
Finally $(ra+2)(ra+3)\cdots(ra+k)\, 2^{k-1} \le (2(ra + N))^{k-1} = X^{k-1}$, since each factor $ra + j$ with $j \le k \le N$ is at most $ra + N$. $\square$

### Series bounds and the bound at one prime

**Lemma 4.2.8 (Series bounds).** Let $p$ be a real number and $k$ an integer.

1. If $p \ge 2$, $k \ge 1$ and $|c_n| \le M$ for all $n \ge 0$, then $\sum_{n \ge 0} p^{-(n+1)k} c_n$ converges absolutely and its absolute value is at most $2M p^{-k}$.
2. If $p > 0$ and $0 \le X \le 3p/8$, then for every $N$, $\sum_{k=2}^{N} 2 p^{-k} X^{k-1}/k! \le 1.5\, X/p^2$.
3. If $f \ge 1$, $N = r + a \ge 2$, $4fN^2 \le B_0 < p$, then $X/p \le 3/8$.

Lean: `GroundTheory.Heights₂.Heights.RestTerms.RestInnerTsumBound.full` (also `GroundTheory.Heights₂.Heights.RestTerms.RestKSumBound.full`, `GroundTheory.Heights₂.Heights.RestTerms.XOverPrime.full`)

*Proof.* 1. The geometric series gives $\sum_n p^{-(n+1)k} = p^{-k}/(1 - p^{-k}) \le 2p^{-k}$ for $p^k \ge 2$. 2. Put $u = X/p \le 3/8$. Since $p^{-k}X^{k-1} = (X/p^2)\, u^{k-2}$, the sum is at most $\frac{2X}{p^2} \sum_{k \ge 2} u^{k-2}/k!$. Here $\sum_{k \ge 2} u^{k-2}/k! \le \frac12 \sum_{j \ge 0} u^j/j! = \frac12 e^{u}$, so the sum is at most $e^{3/8} X/p^2 \le 1.5\, X/p^2$. 3. We have $X = 2ra + 2N \le N^2/2 + 2N \le \frac32 N^2$, using $ra \le N^2/4$ and $N \ge 2$. So $X/p < \frac32 N^2 / (4fN^2) \le 3/8$. $\square$

**Theorem 4.2.9 (Rest terms at one prime).** Let $f, r, a \ge 1$, $N = r + a$, let $c$ be a small block and $B_0$ a real number with $4fN^2 \le B_0$. Then $F_c$ has a power sum decomposition. For every power sum decomposition $Q$ of $F_c$, all choices $s$, all choices $e$ with values in $\{1, -1\}$, and every prime $p > B_0$,
$$|M(p)| \le 1.5\, f\, X\, \frac{\log p}{p^2}\, (fra+1)\, |D_c|.$$

Lean: `GroundTheory.Heights₂.Heights.RestTerms.RestPrimeBound.full`

*Proof.* The decomposition exists by the Proposition (One rest term). Fix $Q$, $s$, $e$ and $p$, and put $C = (fra+1)|D_c|$. For fixed $\tau$ and $k$, the numbers $c_n = e(p,n+1,\tau,k)\, T(k, \tau, q_{k-1}(s(p,n+1,\tau)))$ satisfy $|c_n| \le C X^{k-1}/k!$ by the Proposition, with $\tau' = s(p, n+1, \tau)$. By part 1 of the series bounds, the sum over $n$ is at most $2 p^{-k} C X^{k-1}/k!$ in absolute value. By part 3, $X \le 3p/8$, so part 2 bounds the sum over $2 \le k \le N$ by $1.5\, C X/p^2$. The sum over the $f$ blocks $\tau$ gives the factor $f$, and the factor $\log p$ is outside. $\square$

**Remark 4.2.10 (Formalization).** The prime term is a sum $\sum'$ over $n$ in the sense of unconditional sums, which is $0$ for a family that is not summable ([Statements.lean](lean:GroundTheory/HeightsAndTheta/Heights/RemainderTerms/Statements.lean#L312)). Its definition has no summability hypothesis; the summability is proved in part 1 of the series bounds. The assembly ([PRestPrimeBound.lean](lean:GroundTheory/HeightsAndTheta/Heights/RemainderTerms/PRestPrimeBound.lean#L10)) uses only the bounds of the Proposition. It drops the facts $D_c \ne 0$ and the vanishing for $ra < k-1$ (lines 14 and 15). The series bounds and $X \le \frac32 N^2$ are proved by lemmas whose names end in `intersectionNumber_baseChange` ([Imports.lean](lean:GroundTheory/HeightsAndTheta/Heights/RemainderTerms/Imports.lean#L582)), names unrelated to their content.
