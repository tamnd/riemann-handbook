---
title: Mean squares and the stage
decls:
  - QH.meanSqK
  - QH.stage
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Mean squares and the stage

This section proves two results on primes $q$ in a progression. The first is a mean square bound for prime sums twisted by the Legendre symbol $(\cdot/q)$, summed over $q$. The second, the stage theorem, uses it to show that for almost all such $q$ every twist $\xi\cdot(\cdot/q)$ of a fixed small set of characters has a zero-free box and a small prime sum. The stage theorem is used in the next section to find good pairs of primes ([Theorem 6.6.5](/entry/pair-share/)). The method is the classical one of the [large sieve](/learn/analytic-number-theory/#mean-values-and-the-large-sieve): a mean square over a family turns into a count of exceptions.

Throughout, $\Lambda$ is the von Mangoldt function. For $y > 0$ and $n \geq 1$ put $c_y(n) = \Lambda(n)\min(1, y/n)$. For odd $q$ write $(n/q)$ for the [[Jacobi symbol|0ADTQBXRMC]]; for prime $q$ it is the [[Legendre symbol|0JTC045NNZ]].

**Definition 6.5.1 (Twisted prime sum).** For real $Z, y > 0$, an odd integer $q$ and a function $\kappa : \mathbb{N} \to \mathbb{C}$ put
$$S_\kappa(Z, y; q) = \sum_{1 \leq n \leq Z} c_y(n)\,\kappa(n)\Bigl(\frac{n}{q}\Bigr).$$
Let $\mathcal{P}(m_0, a_0, U)$ be the set of primes $q$ with $U^{1/2} < q \leq U$ and $q \equiv a_0 \pmod{m_0}$.

Lean: `QH.S` (also `Formalism.HermitianLattices.ZeroFreeRegionGL2.PPset`).

**Definition 6.5.2 (Admitted parameters).** Let $0 < \varepsilon \leq 1$, let $Y, U$ be real and let $m_0, a_0$ be natural numbers. The tuple $(\varepsilon, Y, U, m_0, a_0)$ is *admitted* if $m_0 > 0$, $8 \mid m_0$, $\gcd(a_0, m_0) = 1$ and
$$\tfrac14\log^2 Y\,\log m_0 \leq \log U, \qquad Y^{\varepsilon/6} \leq \log U \leq Y^{\varepsilon/5}\log^2 Y.$$

Lean: `QH.admitted`.

So $U$ is doubly exponential in a small power of $Y$, and $m_0$ is small compared to $U$.

**Lemma 6.5.3 (Jacobi sums over primes in a progression).** For all $\varepsilon, A, B > 0$ there is $Y_0$ such that for all $Y \geq Y_0$ and all admitted $(\varepsilon, Y, U, m_0, a_0)$ there is an integer $n^*$ with the following property. For every odd squarefree $s > 1$ with $\gcd(s, m_0) = 1$, $s \leq Y^A$ and $s \neq n^*$,
$$\Bigl|\sum_{q \in \mathcal{P}(m_0, a_0, U)}\Bigl(\frac{q}{s}\Bigr)\Bigr| \leq Y^{-B}\,|\mathcal{P}(m_0, a_0, U)|.$$

Lean: `QH.twistK`.

*Proof.* As a function of $q$, the symbol $(q/s)$ is a real primitive character modulo $s$, since $s > 1$ is odd and squarefree. Split $\mathcal{P}$ by the class of $q$ modulo $m_0 s$, and count each class with the theorem on [primes in progressions](/entry/pnt-progressions-relative-weak-holds/) for the modulus $M = m_0 s$, which is divisible by $8$. The main terms $\mathrm{li}\,U/\varphi(M)$ cancel, since $(\cdot/s)$ sums to $0$ over the classes. The relative errors are small: $\log M \leq 4\log U/\log^2 Y + A\log Y$ by the first admitted inequality, so $e^{-c_3\log U/\log M}$ and $e^{-\sqrt{c_3\log U}}$ are smaller than any power of $Y$. The term of an exceptional zero survives only if the exceptional real character is induced by $(\cdot/s)$ times a character modulo $m_0$. By the theorem of Landau and Page, at most one primitive real character of conductor at most $m_0Y^A$ has a zero that close to $1$. Its conductor determines $n^*$. A lower bound for the size of $\mathcal{P}$ from the same theorem turns the bound into a relative one. $\square$

**Theorem 6.5.4 (Mean square over primes).** There is $C > 0$ such that for all $0 < \varepsilon \leq 1$ and $K \geq 1$ there is $Y_0$ with the following property. Let $Y \geq Y_0$, let $(\varepsilon, Y, U, m_0, a_0)$ be admitted, and assume that every prime $p \mid m_0$ has $p \leq Y^{\varepsilon/5}$ or $p > Y^{400K}$. Put $Z = Y^{400K}$ and $\mathcal{P} = \mathcal{P}(m_0, a_0, U)$. Then for all $y \in [Y, Y^K]$ and all $\kappa$ with $|\kappa(n)| \leq 1$ for all $n$,
$$\sum_{q \in \mathcal{P}}|S_\kappa(Z, y; q)|^2 \leq C\,y\log y\,|\mathcal{P}|.$$

Lean: `QH.meanSqK` (also `QH.MeanSq`).

The bound is the size of the diagonal: if the symbols $(n/q)$ were orthogonal in $q$, the sum would be $|\mathcal{P}|\sum_n c_y(n)^2 \asymp |\mathcal{P}|\,y\log y$.

*Proof.* Expand the square:
$$\sum_{q \in \mathcal{P}}|S_\kappa|^2 = \sum_{n, n' \leq Z}c_y(n)c_y(n')\kappa(n)\overline{\kappa(n')}\sum_{q \in \mathcal{P}}\Bigl(\frac{nn'}{q}\Bigr).$$
Only prime powers $n, n'$ occur. Every $q \in \mathcal{P}$ is larger than $Z^2$, because $\log U \geq Y^{\varepsilon/6} \geq 1600K\log Y$ for large $Y$. So $q \nmid nn'$.

Let $s(N)$ be the product of the primes $p \nmid m_0$ that divide $N$ to an odd power. For $q \equiv a_0 \pmod{m_0}$ the symbols $(2/q)$ and $(p/q)$ with $p \mid m_0$ odd depend only on $a_0$, by quadratic reciprocity and $8 \mid m_0$. The same holds for the sign in $(s/q) = \pm(q/s)$. Hence
$$\Bigl|\sum_{q \in \mathcal{P}}\Bigl(\frac{nn'}{q}\Bigr)\Bigr| = \Bigl|\sum_{q \in \mathcal{P}}\Bigl(\frac{q}{s(nn')}\Bigr)\Bigr|.$$
Put $w = Y^{\varepsilon/5}$. For a prime $p$ let $s_p = \sum_{a \geq 1,\,p^a \leq Z}c_y(p^a)$. Let $R$ be the sum of $c_y(p^a)$ over the prime powers $p^a \leq Z$ with $a$ even or $p \mid m_0$. By the hypothesis on $m_0$, the primes $p \mid m_0$ with $p \leq Z$ are at most $w$. We use four standard bounds, with constants $C_1, \ldots, C_4$:
$$\begin{aligned} R &\leq C_1(\sqrt y + w\log y), & s_p &\leq C_2\log y,\\ \sum_p s_p^2 &\leq C_3\,y\log y, & \sum_{n \leq Z}c_y(n) &\leq C_4\,y\log Z. \end{aligned}$$
Now split the pairs $(n, n')$ by $s = s(nn')$.

1. *$s = 1$.* Either $n, n'$ are powers of one prime, or both $n$ and $n'$ lie in the sum $R$. The inner sum is at most $|\mathcal{P}|$. These pairs give at most $(\sum_p s_p^2 + R^2)|\mathcal{P}|$.
2. *$s = n^*$, $s > 1$.* Here $n^*$ comes from the lemma with $A = 800K$ and $B = K + 1$. As $n, n'$ are prime powers, $n^*$ has one or two prime factors. If $n^* = p_1p_2$, the pairs give at most $2s_{p_1}s_{p_2}$. If $n^* = p$, one of $n, n'$ is an odd power of $p$ and the other is a power of $p$ or lies in $R$. In both cases the pairs give at most $(2B_0^2 + 2B_0R)|\mathcal{P}|$ with $B_0 = C_2\log y$.
3. *$s \neq 1, n^*$.* Then $s \leq nn' \leq Z^2 = Y^{800K}$, and the lemma bounds the inner sum by $Y^{-K-1}|\mathcal{P}|$. These pairs give at most $Y^{-K-1}(\sum_n c_y(n))^2|\mathcal{P}|$.

For large $Y$ and $y \geq Y$ we have $\log y \leq 2\sqrt y$ and $w\log y \leq 4\sqrt y$, as $w \leq y^{1/5}$. Hence $R^2 \leq 25C_1^2y$, $2B_0^2 \leq 4C_2^2y\log y$ and $2B_0R \leq 20C_1C_2y\log y$. Since $y \leq Y^K$,
$$Y^{-K-1}\Bigl(\sum_n c_y(n)\Bigr)^2 \leq C_4^2(400K)^2\frac{y\log^2 Y}{Y} \leq C_4^2\,y\log y$$
for large $Y$. The sum of the three cases is at most $C\,y\log y\,|\mathcal{P}|$ with $C = C_3 + 25C_1^2 + 4C_2^2 + 20C_1C_2 + C_4^2$. $\square$

We now define the boxes of the stage theorem. For a [[Dirichlet character|JR4QSEFXWF]] $\psi$ modulo $N$ and $y > 0$ put
$$G_\psi(y) = \sum_{n \leq y}\Lambda(n)\psi(n)\Bigl(\frac yn - 1\Bigr) + y\,\frac{L'}{L}(1, \psi).$$

**Definition 6.5.5 (Boxes).** Let $Q, C, \tau, Y, X$ be real.

1. $\psi$ has a *zero-free box of height $Q$* if $L(s, \psi) \neq 0$ for all $s$ with $\mathrm{Re}\,s > 1 - 1/400$ and $|\mathrm{Im}\,s| \leq Q$.
2. $\psi$ is *$Q$-good* if $\psi \neq 1$, $N \leq Q$ and $\psi$ has a zero-free box of height $Q$.
3. $\psi$ *lies in the box* $(Q, C, \tau, Y, X)$ if it is $Q$-good, $|L'/L(1, \psi)| \leq C\log Y$, and $|G_\psi(y)| \leq y^{1/2 + \tau}$ for all $y \in [Y, X]$.
4. For $f : \mathbb{N} \to \mathbb{C}$ and $M \in \mathbb{N}$, the pair $(f, M)$ *lies in the box* if every primitive character $\psi$, of any modulus, with $\psi(n) = f(n)$ for all $n$ prime to $M$ lies in the box.

Lean: `QH.Box` (also `Formalism.HermitianLattices.ZeroFreeRegionGL2.ZeroFreeBox`, `QH.GoodC`, `QH.BoxAll`, `QH.Ind`, `Formalism.HermitianLattices.ZeroFreeRegionGL2.Gchi`).

The function $G_\psi$ is the smoothed prime sum of [the thin bound](/entry/thin/); the box asks for square root cancellation in it, up to $y^\tau$.

**Lemma 6.5.6 (Zero density in a box).** There is $C$ such that for all $Q \geq 3$ and $F$ the following holds. Let $\mathcal{B}$ be a finite set of primes $q > F$ such that for each $q \in \mathcal{B}$ there are $f \leq F$ and a primitive character $\psi$ modulo $fq$ with $fq \leq Q$ and no zero-free box of height $Q$. Then $|\mathcal{B}| \leq C\,Q^{1/4}$.

Lean: `QH.count_bad`.

*Proof.* The number of primitive characters of conductor at most $Q$ whose $L$-function has a zero with real part greater than $1 - 1/400$ and imaginary part at most $Q$ in absolute value is at most $CQ^{1/4}$. This is a large sieve zero density estimate (Iwaniec and Kowalski, Chapter 10). Since $f \leq F < q$, the prime $q$ is the only prime factor of $fq$ larger than $F$. So different $q \in \mathcal{B}$ give different characters $\psi$. $\square$

**Lemma 6.5.7 (Box from a small prime sum).** There is $C > 0$ such that for all $0 < \varepsilon \leq 1/4$, $\tau > 0$ and $K \geq 1$ there is $Y_0$ with the following property. Let $Y \geq Y_0$, let $Y^{\varepsilon/6} \leq \log Q \leq Y^{\varepsilon/4}$, and let $\psi$ be a $Q$-good character with $\psi(n) = \kappa(n)(n/q)$ for all $n$. If $|S_\kappa(Y^{400K}, y; q)| \leq y^{1/2 + \tau}/2$ for all $y \in [Y, Y^K]$, then $\psi$ lies in the box $(Q, C, \tau, Y, Y^K)$.

Lean: `QH.box_of_S`.

*Proof.* Put $Z = Y^{400K}$ and $t_\psi(Z) = -\frac{L'}{L}(1, \psi) - \sum_{n \leq Z}\Lambda(n)\psi(n)/n$. For $y \leq Z$ a direct computation gives
$$G_\psi(y) = -S_\kappa(Z, y; q) - y\,t_\psi(Z).$$
A contour argument in the zero-free box gives $Y^K|t_\psi(Z)| \leq Y^\varepsilon$, and the same argument with a Mertens type bound gives $|L'/L(1, \psi)| \leq C\log Y$. Since $\varepsilon \leq 1/4$ and $y \geq Y$, we have $Y^\varepsilon \leq y^{1/2 + \tau}/2$ for large $Y$. $\square$

**Lemma 6.5.8 (Share of large values).** For all $C \geq 0$, $\tau > 0$ and $\eta > 0$ there is $Y_0$ such that the following holds for $Y \geq Y_0$. Let $X, Z$ be real, let $\mathcal{B} \subseteq \mathcal{P}$ be finite sets, and let $|\kappa(n)| \leq 1$. Assume $\sum_{q \in \mathcal{P}}|S_\kappa(Z, y; q)|^2 \leq C\,y\log y\,|\mathcal{P}|$ for all $y \in [Y, X]$, and that each $q \in \mathcal{B}$ has some $y \in [Y, X]$ with $|S_\kappa(Z, y; q)| > y^{1/2 + \tau}/2$. Then $|\mathcal{B}| \leq \eta|\mathcal{P}|$.

Lean: `QH.bad_share`.

*Proof.* Cut $[Y, X]$ into the blocks $[2^iY, \min(2^{i+1}Y, X)]$. On one block, bound $\sup_y|S|^2$ by the value at one end plus the integral of the derivative in $y$; the mean square bound and Markov's inequality then bound the number of $q$ with a large value in block $i$ by a constant times $C\tau^{-1}(2^iY)^{-\tau}|\mathcal{P}|$. Sum the geometric series with ratio $r = 2^{-\tau}$. The total is at most $32C\tau^{-1}Y^{-\tau}(1 - r)^{-1}|\mathcal{P}|$, which is below $\eta|\mathcal{P}|$ for large $Y$. $\square$

**Theorem 6.5.9 (Stage).** There is $C > 0$ such that for all $0 < \varepsilon \leq 1/4$, $\tau > 0$, $K \geq 1$, $\eta > 0$ and $R \in \mathbb{N}$ there is $Y_0$ with the following property. Let $Y \geq Y_0$, let $(\varepsilon, Y, U, m_0, a_0)$ be admitted, and assume that every prime $p \mid m_0$ has $p \leq Y^{\varepsilon/5}$ or $p > Y^{400K}$. Let $1 \leq F \leq U^{1/2}$, and let $\Xi$ be a set of at most $R$ primitive characters, each of modulus at most $F$. Then $\mathcal{P} = \mathcal{P}(m_0, a_0, U)$ is not empty. Next, let $\mathcal{B} \subseteq \mathcal{P}$ be such that for each $q \in \mathcal{B}$ there are $\xi \in \Xi$ and $M \neq 0$ for which the pair $(n \mapsto \xi(n)(n/q), M)$ does not lie in the box $(FU, C, \tau, Y, Y^K)$. Then $|\mathcal{B}| \leq \eta|\mathcal{P}|$.

Lean: `QH.stage`.

*Proof.* Take $C$ from the lemma on boxes from small prime sums.

1. *Size of $\mathcal{P}$.* The theorem on [primes in progressions](/entry/pnt-progressions-relative-weak-holds/), with a bound for exceptional zeros, gives $|\mathcal{P}| \geq U^{9/10}$ for large $Y$. In particular $\mathcal{P}$ is not empty.
2. *The twist.* Let $q \in \mathcal{B}$, with $\xi$ of modulus $f$. Then $q > U^{1/2} \geq F \geq f$, so $q \nmid f$ and $q \neq 2$. Hence $\psi = \xi\cdot(\cdot/q)$ is a primitive character modulo $fq$ with $\psi \neq 1$, and $fq \leq FU$. A primitive character is determined by its values on the integers prime to any fixed $M \neq 0$. So the only primitive character that agrees with $\xi\cdot(\cdot/q)$ off $M$ is $\psi$, and $\psi$ does not lie in the box.
3. *Split $\mathcal{B}$.* Also $Y^{\varepsilon/6} \leq \log(FU) \leq \tfrac32\log U \leq \tfrac32Y^{\varepsilon/5}\log^2Y \leq Y^{\varepsilon/4}$ for large $Y$. If $\psi$ has a zero-free box of height $FU$, it is $FU$-good. Then, by the lemma on boxes from small prime sums, some $y \in [Y, Y^K]$ has $|S_\xi(Y^{400K}, y; q)| > y^{1/2 + \tau}/2$. So $\mathcal{B} \subseteq \mathcal{B}_1 \cup \bigcup_{\xi \in \Xi}\mathcal{B}_2(\xi)$, where $\mathcal{B}_1$ holds the $q$ of the first kind and $\mathcal{B}_2(\xi)$ those of the second kind for $\xi$.
4. *Bad zeros.* By the lemma on zero density in a box with $Q = FU$, and since $(FU)^{1/4} \leq U^{3/8}$,
$$|\mathcal{B}_1| \leq C_b\,U^{3/8} \leq \tfrac\eta2U^{9/10} \leq \tfrac\eta2|\mathcal{P}|$$
for large $U$, and $U$ is large when $Y$ is large.
5. *Large sums.* The mean square theorem holds for $\mathcal{P}$ with $Z = Y^{400K}$ on $[Y, Y^K]$. The lemma on the share of large values with $\eta/(2(R + 1))$ gives $|\mathcal{B}_2(\xi)| \leq \frac{\eta}{2(R + 1)}|\mathcal{P}|$ for each $\xi$. As $|\Xi| \leq R$, the union has at most $\frac\eta2|\mathcal{P}|$ elements.

Adding 4 and 5 gives $|\mathcal{B}| \leq \eta|\mathcal{P}|$. $\square$

**Remark 6.5.10 (Formalization).** The definitions are in [PrimeSetTwoBounds.lean](lean:Development/AutomorphicArithmetic/MeanSquareBounds/PrimeSetTwoBounds.lean#L13), and $\mathcal{P}$, the zero-free box and $G_\psi$ are in [SecondEstimateOfIntervalHypothesis.lean](lean:Formalism/GL3MeanSquares/SecondEstimateOfIntervalHypothesis.lean#L44). The mean square theorem is in [meanSqK.lean](lean:Development/AutomorphicArithmetic/MeanSquareBounds/meanSqK.lean#L51), under `set_option maxHeartbeats 800000`, and the stage theorem is in [StagePow.lean](lean:Development/AutomorphicArithmetic/MeanSquareBounds/StagePow.lean#L41). We have read both proofs, and the steps above follow them, with the constants of the code. We have not opened the proofs of `QH.twistK`, of the contour bounds `QH.tailK` and `QH.kappaC`, or of the zero density estimate `Formalism.HermitianLattices.Ext.PrimitiveCharacterCasts.ZD.zero_density_box` behind `QH.count_bad`; the proofs given for these follow the classical route and name the inputs that the code imports, namely the theorem of Section 2, a zero-free region and a bound for exceptional zeros. In the stage theorem a character of $\Xi$ is a pair $(N, \xi)$ with $\xi$ modulo $N + 1$, so that the modulus is never $0$. The bad condition quantifies over all $M \neq 0$; step 2 shows that the choice of $M$ does not matter. The bad set is not required to be the full set of bad primes: the theorem bounds every subset with the bad property, which is the same.
