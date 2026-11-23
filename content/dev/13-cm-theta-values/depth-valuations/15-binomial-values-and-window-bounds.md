---
title: Binomial values and window bounds
decls:
  - GlobalTheory.OddBlock.BinomialValue.main
  - GlobalTheory.OddBlock.WindowValuationBound.main
  - GlobalTheory.OddBlock.windowBound
  - GlobalTheory.OddBlock.BlockContent.biContent_and_biWindow
  - GlobalTheory.OddBlock.content_and_window
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Binomial values and window bounds

This section bounds the valuation of the model jets that come out of the [main term normal form](/entry/cm-theta-values/depth-valuations/#main-terms-at-odd-levels). The model jet $\Lambda(y)$ is a determinant power operator applied to the exponential of the main term plus a remainder. We write it as a Capelli number times a binomial sum $\sum_s \binom{y}{s} a_s$ with $a_0 = 1$ and $a_s$ divisible by $\ell$ for large $s$, and deduce that the binomial sum is a unit for at least one $y$ in every window of a fixed length. Adding factorials for the rows outside the normal form gives the content and window bounds used by the [odd block supply](/entry/cm-theta-values/depth-valuations/#the-odd-block-supply).

### Model jets

Let $C$ be a field of characteristic $0$ with an additive valuation $v$ into $\mathbb{R} \cup \{\infty\}$, and $\ell \geq 5$ a prime with $v(\ell) = 1$. Fix an odd $i$, and let $E, \rho, r_1, r_2, \delta$ be as in the previous section. Put $\gamma = \ell/(\ell^2 - 1)$.

For $n_0 \geq 0$ take two $n_0 \times n_0$ matrices of variables, $x_{bc}$ on the left and $x'_{bc}$ on the right, and let $\Delta_L = \det(x)$ and $\Delta_R = \det(x')$. For a polynomial $P$ and a series $G$ put
$$[P, G] = \sum_\mu P_\mu\, \mu!\, G_\mu = \bigl(P(\partial)\, G\bigr)(0),$$
where $\mu! = \prod_x \mu(x)!$. When $G$ is a polynomial too this is the factorial weighted pairing $\langle P, G\rangle$. For a series $h$ without constant term, $\exp(h)$ is the usual exponential series. Given a series $h_1$ in the $2 n_0^2$ variables, put
$$h_P = -\ell^{-E} \sum_{b, c} x_{bc}^{\ell^i} x'_{bc} + h_1, \qquad \Lambda(y) = \bigl[\Delta_L^{\ell^i y} \Delta_R^{y}, \exp(h_P)\bigr].$$
We say $h_1$ satisfies (H1) if $1/(\ell - 1) \leq v(h_{1,\mu}) + |\mu|_L (r_1 - \delta) + |\mu|_R (r_2 - \delta)$ for every monomial $\mu$, and (H2) if every monomial with nonzero coefficient in $h_1$ contains a right variable. (H2) gives $h_P$ no constant term.

The *Capelli number* is $\mathrm{cap}(n_0, x) = \prod_{0 \leq a < n_0} (x + a)!/a!$. By the Cayley identity $\langle \Delta^x, \Delta^x \rangle = \mathrm{cap}(n_0, x)$ for the determinant $\Delta$ of an $n_0 \times n_0$ matrix of variables, and this number is not $0$. For $n \geq 1$ and $n_0 \leq n$ put
$$b(n_0, n, y) = n_0 y \bigl((\ell^i + 1)\gamma - 1\bigr) + n(\log_\ell n + 1), \qquad S_0(n_0) = \bigl\lceil 64\, n_0^2 \bigl(i + 3 + 3\log_\ell(n_0 + 1)\bigr) \bigr\rceil.$$

### The binomial expansion

**Theorem 4.15.1 (binomial expansion of the model jet).** Assume (H1) and (H2). There are $a_0, a_1, \dots \in C$ with $a_0 = 1$,
$$\Lambda(y) = (-\ell^{-E})^{n_0 y}\, \mathrm{cap}(n_0, \ell^i y) \sum_{s = 0}^{y} \binom{y}{s} a_s \quad \text{for all } y \geq 0,$$
and $v(a_s) \geq s/8 - n_0^2 (3 \log_\ell n_0 + 2 \log_\ell s + i + 3)$ for all $s \geq 1$.

Lean: `GlobalTheory.OddBlock.BinomialValue.main`.

*Proof.* If $n_0 = 0$, both determinants are $1$ and $\exp(h_P)$ has constant term $1$, so $\Lambda(y) = 1$; take $a_s = 0$ for $s \geq 1$, so $v(a_s) = \infty$.

Let $n_0 \geq 1$. Step 1. Since $i$ is odd, a geometric sum gives $E = 1 + (\ell^i - \ell)/(\ell^2 - 1)$. Also $r_1 - \delta = \rho + 3/(8\ell^i)$ and $r_2 - \delta = \rho + 1/2 - 1/(8\ell^i)$. So (H1) is the weight hypothesis of the exponential binomial theorem, and (H2) is its hypothesis that every monomial meets a right variable. That theorem gives polynomials $Q_s$ in the left variables, homogeneous of degree $n_0 \ell^i s$, with $Q_0 = 1$, $v$ of every coefficient of $Q_s$ at least $s/8 - n_0^2(\log_\ell(n_0 s) + 1)$ for $s \geq 1$, and
$$\Lambda(y) = (-\ell^{-E})^{n_0 y} \sum_{s = 0}^{y} \binom{y}{s} \bigl\langle \Delta^{\ell^i y}, \Delta^{\ell^i (y - s)} Q_s \bigr\rangle.$$

Step 2. For $Q$ homogeneous of degree $n_0 M$ and $M \leq Y$, the pairing is proportional:
$$\langle \Delta^Y, \Delta^{Y - M} Q \rangle\, \langle \Delta^M, \Delta^M \rangle = \langle \Delta^M, Q \rangle\, \langle \Delta^Y, \Delta^Y \rangle.$$
With $M = \ell^i s$, $Y = \ell^i y$ and the Cayley identity, the $s$-th term is $\mathrm{cap}(n_0, \ell^i y)\, a_s$ with $a_s = \langle \Delta^{\ell^i s}, Q_s\rangle / \mathrm{cap}(n_0, \ell^i s)$. For $s = 0$ this is $\mathrm{cap}(n_0, 0)/\mathrm{cap}(n_0, 0) = 1$.

Step 3. A lower bound for quotients of determinant pairings turns the coefficient bound on $Q_s$ into $v(a_s) \geq s/8 - n_0^2(3\log_\ell n_0 + 2\log_\ell s + i + 3)$. $\square$

### Windows

**Lemma 4.15.2 (binomial windows).** Let $S \geq 1$ and $a_0, a_1, \dots \in C$ with $a_0 = 1$ and $v(a_s) > 0$ for $s \geq S$. Then every interval $[Y_0, Y_0 + S)$ contains a $y$ with $v\bigl(\sum_{s \leq y} \binom{y}{s} a_s\bigr) \leq 0$.

*Proof.* Put $B_k(y) = \sum_{s \leq y} \binom{y}{s} a_{s + k}$, so $B_0(y)$ is the sum in question. Pascal's rule gives $B_{k+1}(y) = B_k(y + 1) - B_k(y)$. Integers have $v \geq 0$, so sums and integer multiples of elements of positive valuation have positive valuation. Suppose $v(B_0(y)) > 0$ for all $y$ in the window. By induction on $k$, $v(B_k(y)) > 0$ whenever $Y_0 \leq y$ and $y + k < Y_0 + S$. For $k \geq S$, every $a_{s+k}$ has positive valuation, so $v(B_k(y)) > 0$ for all $y$. Hence $v(B_k(Y_0)) > 0$ for every $k$. Now descend in $y$: if $v(B_k(y)) > 0$ for all $k$, then $B_k(y - 1) = B_k(y) - B_{k+1}(y - 1)$, and descending induction on $k$ from $k \geq S$ gives $v(B_k(y - 1)) > 0$ for all $k$. At $y = 0$ we get $v(a_0) = v(B_0(0)) > 0$, against $a_0 = 1$. $\square$

**Theorem 4.15.3 (window bound for model jets).** Assume (H1) and (H2), and let $1 \leq n$ and $n_0 \leq n$. If $n_0 \geq 1$, every interval $[Y_0, Y_0 + S_0(n_0))$ contains a $y$ with $v(\Lambda(y)) \leq b(n_0, n, y)$. If $n_0 = 0$, then $\Lambda(y) = 1$ for all $y$.

Lean: `GlobalTheory.OddBlock.WindowValuationBound.main` (also `GlobalTheory.OddBlock.windowBound`, a second name).

*Proof.* The case $n_0 = 0$ was done above. Let $n_0 \geq 1$ and take the $a_s$ of the expansion. Step 1. For $s \geq S_0(n_0)$ an elementary estimate gives $s/8 > n_0^2(3\log_\ell n_0 + 2\log_\ell s + i + 3)$, so $v(a_s) > 0$; it uses $\ell \geq 5$, $\log_\ell 64 \leq 3$ and $\log_\ell t \leq t - 1$. Also $S_0(n_0) \geq 1$. The lemma gives $y$ in the window with $v(\sum_s \binom{y}{s} a_s) \leq 0$.

Step 2. Since $v(\ell) = 1$, $v(p) = 0$ for primes $p \neq \ell$ and $v(N) = v_\ell(N)$ for positive integers $N$. So
$$v(\Lambda(y)) \leq -E\, n_0 y + v_\ell\bigl(\mathrm{cap}(n_0, \ell^i y)\bigr).$$

Step 3. A Legendre estimate for Capelli numbers gives $v_\ell(\mathrm{cap}(n_0, x)) \leq n_0 x/(\ell - 1) + n_0(\log_\ell n_0 + 1) \leq n_0 x/(\ell - 1) + n(\log_\ell n + 1)$. With $x = \ell^i y$ and the identity $\ell^i/(\ell - 1) - E = (\ell^i + 1)\gamma - 1$ we get $v(\Lambda(y)) \leq b(n_0, n, y)$. $\square$

### Content and windows of blocks

The blocks of the next section have $n$ rows, of which the first $n_0$ carry the model jet. Take $n \times n$ matrices of variables with determinants $\Delta_L, \Delta_R$, and series $h^r_\rho, t_\rho, t'_\rho$ for $\rho < n$. They satisfy the *block hypothesis* for $h_1$ if each $h^r_\rho$ involves only the variables of row $\rho$ and has no constant term, for $\rho \geq n_0$ the series $t_\rho$ and $t'_\rho$ involve only the left and right variables of row $\rho$ and agree with $x_{\rho\rho}$ and $x'_{\rho\rho}$ to first order, and $\sum_{\rho < n_0} h^r_\rho$ restricts on the first $n_0$ rows and columns to $h_P$. The *block jet* is
$$J(y) = \Bigl[\Delta_L^{\ell^i y} \Delta_R^{y}, \prod_{\rho < n} F_\rho \exp(h^r_\rho)\Bigr], \qquad F_\rho = 1 \ (\rho < n_0), \quad F_\rho = t_\rho^{\ell^i y} t'^{\,y}_\rho \ (\rho \geq n_0).$$
A block value lemma, proved earlier, gives $J(y) = \bigl((\ell^i y)!\, y!\bigr)^{n - n_0} \Lambda(y)$ under the block hypothesis.

**Theorem 4.15.4 (content and window).** Let $\ell \geq 5$ be prime with $v(\ell) = 1$ and $i$ odd.

1. (Content.) Let $1 \leq n$, $n_0 \leq n$, $y \geq 0$, and $\Lambda \in C$ with $v(\Lambda) \leq b(n_0, n, y)$. Then
$$v\Bigl(\bigl((\ell^i y)!\, y!\bigr)^{n - n_0} \Lambda\Bigr) \leq b(n, n, y) + \frac{(n - n_0)(\ell^i + 1) y}{\ell - 1}.$$
2. (Window.) Let $1 \leq n_0 \leq n$ and $m$ with $n - n_0 \leq (i + 1) m$. Assume the block hypothesis, (H1) and (H2). Then every interval $[Y_0, Y_0 + S_0(n_0))$ contains a $y$ with
$$v(J(y)) \leq b(n, n, y) + \frac{(i + 1)\, m\, (\ell^i + 1)\, y}{\ell - 1}.$$

Lean: `GlobalTheory.OddBlock.BlockContent.biContent_and_biWindow` (also `GlobalTheory.OddBlock.content_and_window`, a second name).

*Proof.* Part 1. Let $N \geq 1$ be an integer. Write $N = \ell^e N'$ with $\ell \nmid N'$. A Bezout relation $1 = \ell A + N' B$ and $v(\ell A) > 0$ force $v(N') \leq 0$, so $v(N) \leq e = v_\ell(N)$. Legendre's formula gives $(\ell - 1) v_\ell(N!) \leq N$, so $v(N!) \leq N/(\ell - 1)$. Hence the factorials contribute at most $(n - n_0)(\ell^i y + y)/(\ell - 1)$. Since $\ell^i \geq \ell$, $(\ell^i + 1)\gamma - 1 \geq (\ell + 1)\ell/(\ell^2 - 1) - 1 = 1/(\ell - 1) \geq 0$, so $b(n_0, n, y) \leq b(n, n, y)$. Adding gives the bound.

Part 2. The window bound gives $y$ in the window with $v(\Lambda(y)) \leq b(n_0, n, y)$. The block value lemma writes $J(y)$ as the factorial power times $\Lambda(y)$, Part 1 bounds it, and $n - n_0 \leq (i + 1) m$ replaces the factor $n - n_0$. $\square$

**Remark 4.15.5 (Formalization).** The expansion is at [SumEqOfIsHomogeneous.lean](lean:Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/SumEqOfIsHomogeneous.lean#L796), the window bound at line 917 with its second name at line 961, and the content and window theorem at line 1074 with its second name at line 1084. The lemma on binomial windows is the second half of [NewtonBoundPosAndNewtonStep.lean](lean:Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/NewtonBoundPosAndNewtonStep.lean#L20). The statements are in [BiadditiveInSingleVariables.lean](lean:Formalism/LocalToGlobal/CharacterGerms/BiadditiveInSingleVariables.lean#L108); the window bound proves the predicate `ThmP` of the namespace `Formalism.L2.FormalSeriesBounds`, which is not the predicate of the same name in [StatementThmP.lean](lean:Formalism/IncomingBounds/StatementThmP.lean#L60), which has an unspecified constant $C_0$, windows of length $C_0 n^2 \ell^i \log(n \ell^i)$, the extra hypothesis $v(p) = 0$ for primes $p \neq \ell$, and a zero constant term in place of (H2); nothing in this chapter uses the second one. The file proves $\Lambda(y) = 1$ for $n_0 = 0$ twice, at lines 786 and 872. The proof of Part 1 does not use $\ell \geq 5$, and uses the oddness of $i$ only through $i \geq 1$. We used the exponential binomial theorem, the Cayley identity, the proportionality of pairings, the quotient bound and the block value lemma through their statements, and did not unfold the restriction map in the block hypothesis.
