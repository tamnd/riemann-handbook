---
title: The rest terms summed over the primes
decls:
  - GroundTheory.Heights₂.Heights.RestTerms.RestBound.full
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The rest terms summed over the primes

This section sums [the bound at one prime](/entry/rest-prime-bound-full/) over all primes $p > B_0$, or over the primes of any subset of $\mathbb{N}$. The result is that the rest terms form an absolutely summable family and that their total is at most $1.6\,(fra+1)|D_c|$, a bound that does not depend on $B_0$, on the choices $s$ and $e$, or on the power sum decomposition. The only arithmetic input is Chebyshev's bound $\theta(x) \le x \log 4$. The result is used in [the finite bound](/entry/finite-bound/) of the chapter on arithmetic volumes.

We keep the notation of the previous section: $f, r, a \ge 1$, $N = r + a$, a small block $c$, the rest polynomial $F_c$, the fibre degree $D_c$, the number $X = 2(ra + r + a)$ and the prime terms $M(p)$.

### Chebyshev's bound

**Definition 4.3.1 (Chebyshev's function).** For a real $x \ge 0$, put $\theta(x) = \sum_{p \le x} \log p$, the sum over the primes $p \le x$.

**Lemma 4.3.2 (Chebyshev's bound).** For every real $x \ge 0$, $\theta(x) \le x \log 4$.

Lean: `GroundTheory.Heights₂.Heights.RestTerms.ChebyshevThetaBound.full`

*Proof.* It is enough to show $\prod_{p \le n} p \le 4^n$ for integers $n \ge 1$, by induction on $n$. The cases $n = 1, 2$ are clear, and for an even $n > 2$ the product does not change from $n - 1$ to $n$, since $n$ is not prime. For $n = 2m + 1$, every prime $p$ with $m + 1 < p \le 2m + 1$ divides the binomial coefficient $\binom{2m+1}{m}$, because it divides the numerator $(2m+1)!$ and not the denominator $m!\,(m+1)!$. This coefficient appears twice in the expansion of $(1+1)^{2m+1}$, so it is at most $4^m$. With the induction hypothesis for $m + 1$ we get $\prod_{p \le 2m+1} p \le 4^{m+1} \cdot 4^m = 4^{2m+1}$. $\square$

**Lemma 4.3.3 (Tail of the primes).** Let $B > 0$. Then the family $\log p / p^2$, for the primes $p > B$, is summable, and
$$\sum_{p > B} \frac{\log p}{p^2} \le \frac{2 \log 4}{B}.$$

Lean: `GroundTheory.Heights₂.Heights.RestTerms.PrimeLogSquareTail.full`

*Proof.* The terms are positive, so it is enough to bound the partial sums. For $x > B$, partial summation (a Stieltjes integral against $d\theta$) gives
$$\begin{aligned}
\sum_{B < p \le x} \frac{\log p}{p^2} &= \frac{\theta(x)}{x^2} - \frac{\theta(B)}{B^2} + 2 \int_B^x \frac{\theta(u)}{u^3}\, du \\
&\le \frac{\log 4}{x} + 2 \log 4 \Bigl(\frac1B - \frac1x\Bigr) \le \frac{2 \log 4}{B},
\end{aligned}$$
by Chebyshev's bound and $\theta(B) \ge 0$. $\square$

### The bound over the primes

**Theorem 4.3.4 (Rest terms over the primes).** Let $f, r, a \ge 1$, $N = r + a$, let $c$ be a small block and $B_0$ a real number with $4fN^2 \le B_0$. Then $F_c$ has a power sum decomposition. For every power sum decomposition $Q$ of $F_c$, all choices $s$, all choices $e$ with values in $\{1, -1\}$, and every set $P \subseteq \mathbb{N}$, the family $|M(p)|$, for the primes $p \in P$ with $p > B_0$, is summable, and
$$\Bigl| \sum_{p \in P,\ p \text{ prime},\ p > B_0} M(p) \Bigr| \le 1.6\, (fra + 1)\, |D_c|.$$

Lean: `GroundTheory.Heights₂.Heights.RestTerms.RestBound.full` (also `GroundTheory.Heights₂.Heights.RestTerms.RestBoundOfPrimeBound.full`, the summation step)

*Proof.* The decomposition exists by [the bound at one prime](/entry/rest-prime-bound-full/). Fix $Q$, $s$, $e$ and $P$, and put $C = (fra+1)|D_c|$ and $K = 1.5\, f X C$. By the bound at one prime, $|M(p)| \le K \log p / p^2$ for every prime $p > B_0$. Since $B_0 \ge 4fN^2 > 0$, the tail lemma shows that the family $|M(p)|$ over the primes $p \in P$ with $p > B_0$ is summable, with sum at most $K \cdot 2\log 4 / B_0$. The absolute value of a sum is at most the sum of the absolute values. It remains to bound the constant. We have $X \le \frac32 N^2$ (see the series bounds of the previous section), $2 \log 4 \le 2.78$ and $B_0 \ge 4fN^2$, so
$$K \cdot \frac{2\log 4}{B_0} \le 1.5\, f \cdot \tfrac32 N^2 \cdot C \cdot \frac{2.78}{4fN^2} = \frac{1.5 \cdot 1.5 \cdot 2.78}{4}\, C \le 1.6\, C. \qquad \square$$

**Remark 4.3.5.** The bound is uniform in everything except $f$, $r$, $a$ and $c$. In particular the sets $P$ and the signs $e$ may be chosen after $Q$, and the same bound holds. The constant $1.6$ is not sharp: the proof gives $1.564$.

**Remark 4.3.6 (Formalization).** The tail of the primes is proved by a discrete partial summation over the integers, with weights $\log i$ for primes $i > B$ and $0$ otherwise ([PrimeWeightEqZeroOfLt.lean](lean:GroundTheory/HeightsAndTheta/Heights/RemainderTerms/PrimeWeightEqZeroOfLt.lean#L113)), and not by a Stieltjes integral. Chebyshev's bound, the prime tail, $X \le \frac32 N^2$ and the numerical inequalities $2\log 4 \le 2.78$ and $1.5 \cdot \frac32 \cdot 2.78/4 \le 1.6$ are proved by lemmas whose names end in `intersectionNumber_baseChange` ([Imports.lean](lean:GroundTheory/HeightsAndTheta/Heights/RemainderTerms/Imports.lean#L593)); the names say nothing about the content. The theorem itself only joins the bound at one prime with the summation step ([PRestBound.lean](lean:GroundTheory/HeightsAndTheta/Heights/RemainderTerms/PRestBound.lean#L10)).
