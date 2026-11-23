---
title: Primes represented by norms in short intervals
decls:
  - GlobalTheory.Hk.normPrimes_short_interval_lower
  - GlobalTheory.T.normPrimesImagQuad_short_interval_lower_bound
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Primes represented by norms in short intervals

This section proves the main theorem of the first half of the chapter. For a prime $d \equiv 3 \pmod 4$ and a modulus $M$, the interval $(X, X(1+h)]$ contains at least $c'hX/((4dM^2)^A \log X)$ norm-one primes, as soon as $h \geq \exp(-c\sqrt{\log X})$ and $\log(4dM^2) \leq c\sqrt{\log X}$. The bound is polynomial in $d$ and $M$. In Volume 8 it is [the short interval norm theorem](/entry/short-norm/). The proof combines [the ray class family](/entry/exists-l-fam-ray/) of Section 2 with [the bound for the trivial class](/entry/trivial-class-short-interval/) of Section 1, and removes the prime powers with a Chebyshev bound.

We use the notation of Section 2: $\mathcal{P}_{d,M}(X, Y)$ is the set of norm-one primes $p$ for $(d, M)$ with $\lfloor X \rfloor < p \leq \lfloor Y \rfloor$. Let $\psi(x) = \sum_{n \leq x} \Lambda(n)$ and $\theta(x) = \sum_{p \leq x} \log p$ be the Chebyshev functions.

**Theorem 2.3.1 (Chebyshev).** There is $C$ such that $\psi(x) - \theta(x) \leq C\sqrt{x}$ for all real $x$.

This holds because $\psi(x) - \theta(x)$ is the contribution of the prime powers $p^k \leq x$ with $k \geq 2$. It equals $\sum_{k \geq 2} \theta(x^{1/k})$, and $\theta(y) \ll y$ by Chebyshev's estimate. The term $k = 2$ is $O(\sqrt{x})$, and the at most $\log_2 x$ terms with $k \geq 3$ give $O(x^{1/3}\log x)$. For the functions $\theta$ and $\psi$ see Hardy and Wright, Chapter XXII.

**Lemma 2.3.2 (From weights to primes).** Let a family of ray class type have the property that every prime $p$ with $\lambda(0, p) \neq 0$ is a norm-one prime for $(d, M)$. Then for all real $X$ and all $Y \geq 1$,
$$\sum_{\lfloor X \rfloor < n \leq \lfloor Y \rfloor} \lambda(0, n) \leq 2\log Y \cdot |\mathcal{P}_{d,M}(X, Y)| + 2\bigl(\psi(Y) - \theta(Y)\bigr).$$

*Proof.* By property 5 of a family and $\lambda \geq 0$, we have $0 \leq \lambda(0, n) \leq \sum_g \lambda(g, n) \leq 2\Lambda(n)$. Split the sum into primes and other integers. A prime $p$ in the range contributes only if $\lambda(0, p) \neq 0$. Then $p$ is a norm-one prime, and $\lambda(0, p) \leq 2\log p \leq 2\log Y$. This gives the first term. An integer $n \leq Y$ that is not prime has $\Lambda(n) \neq 0$ only if $n = p^k$ with $k \geq 2$. The sum of $2\Lambda(n)$ over these $n$ is $2(\psi(Y) - \theta(Y))$. $\square$

**Lemma 2.3.3 (The square root term is small).** Let $A, K, c > 0$ with $c \leq 1/(2(1 + A) + 2 + K)$. Let $B \geq 4$, $X \geq 1$ and $h$ satisfy $\log B \leq c\sqrt{\log X}$ and $h \geq e^{-c\sqrt{\log X}}$. Then $\log X \geq 1$ and
$$K\sqrt{X} \leq \frac{hX}{B^A}.$$

*Proof.* Put $s = \sqrt{\log X}$. Since $\log B \geq \log 4 > 1$, we get $cs \geq 1$, so $s \geq 1/c \geq 2(1+A) + 2 + K$, and $\log X = s^2 \geq 1$. Since $h \geq e^{-cs}$ and $B^A \leq e^{Acs}$, the right side is at least $X e^{-(1 + A)cs} = \sqrt{X}\, e^{s^2/2 - (1+A)cs}$. Since $(1 + A)c \leq 1/2$, the exponent is at least $s(s - 1)/2$. Since $s \geq 2 + K$, this is at least $(2 + K)(1 + K)/2 \geq 1 + K$. So the exponential is at least $e^{1+K} \geq K$. $\square$

**Theorem 2.3.4 (Norm-one primes in short intervals).** There are $A, c, c' > 0$ with the following property. Let $d$ be a prime with $d \equiv 3 \pmod 4$ and $d \geq 100$, let $M \geq 3$, let $X \geq 1$, and let $h$ satisfy
$$\log(4dM^2) \leq c\sqrt{\log X}, \qquad e^{-c\sqrt{\log X}} \leq h \leq 1.$$
Then
$$\frac{c' h X}{(4dM^2)^A \log X} \leq \bigl|\mathcal{P}_{d,M}\bigl(X, X(1+h)\bigr)\bigr|.$$

Lean: `GlobalTheory.Hk.normPrimes_short_interval_lower` (also `GlobalTheory.T.normPrimesImagQuad_short_interval_lower_bound`, a second name).

*Proof.* Let $A$, $c_0$ and $e$ be the constants $A$, $c$, $c'$ of [the theorem on the trivial class](/entry/trivial-class-short-interval/), and let $C$ be the constant of Chebyshev's bound. Put $K = 8(|C| + 1)/e$ and
$$c = \min\Bigl(c_0, \frac{1}{2(1 + A) + 2 + K}\Bigr), \qquad c' = \frac{e}{8}.$$
Let $d, M, X, h$ be as in the statement. Take the family of [the ray class family theorem](/entry/exists-l-fam-ray/), with $B = 4dM^2$. Let $Y = X(1+h)$ and $N = |\mathcal{P}_{d,M}(X, Y)|$.

Step 1. Since $c \leq c_0$, the hypotheses of the theorem on the trivial class hold. It gives
$$\frac{e h X}{B^A} \leq \sum_{\lfloor X \rfloor < n \leq \lfloor Y \rfloor} \lambda(0, n).$$

Step 2. By the lemma from weights to primes and by Chebyshev's bound,
$$\frac{e h X}{B^A} \leq 2\log Y \cdot N + 2|C|\sqrt{Y}.$$
We have $X \leq Y \leq 2X$. So $\sqrt{Y} \leq 2\sqrt{X}$, and $\log Y \leq \log X + h \leq 2\log X$, since $\log X \geq 1$ by the second lemma.

Step 3. The second lemma with this $K$ gives $8(|C| + 1)\sqrt{X} \leq e\, hX/B^A$. So $4|C|\sqrt{X} \leq ehX/(2B^A)$. Together with Step 2,
$$\frac{ehX}{2B^A} \leq 4\log X \cdot N.$$
This is the claim with $c' = e/8$. $\square$

The factor $\log X$ in the denominator is the loss in passing from the weights $\lambda(0, p) \leq 2\log p$ to a count of primes. The polynomial dependence on $d$ and $M$ comes only from the factor $B^A$ of the trivial class bound, which comes in turn from the lower bound $1 - \beta \geq c/B^A$ for a possible exceptional zero.

**Remark 2.3.5 (Formalization).** Chebyshev's bound is taken from Mathlib, as `Chebyshev.psi_sub_theta_le_mul_sqrt`, in the form "there is $C$ with $\psi(x) - \theta(x) \leq C\sqrt{x}$ for all $x$" ([NormPrimesImagQuadShortIntervalLowerBound.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/NormPrimesImagQuadShortIntervalLowerBound.lean#L100)). The two lemmas are `GlobalTheory.Hk.sum_lam_zero_le_card_normPrimes` and `GlobalTheory.Hk.sqrt_le_short_main`. The same statement appears in Volume 8 as `UpperTheory.T3.ShortNorm`. The wrapper `GlobalTheory.T.normPrimesImagQuad_short_interval_lower_bound` is stated in a file of its own, which imports Mathlib twice and proves the statement by citing the theorem.
