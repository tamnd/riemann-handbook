---
title: Depth bounds at odd inert primes
decls:
  - GlobalTheory.DepthLow.detDepth_lower
  - GlobalTheory.T.detDepth_lower_bound_saturated_even_type
  - GlobalTheory.RefSum.facBetween_fine
  - GlobalTheory.T.factor_depth_bounded_odd_inert_prime_cmType
  - GlobalTheory.RefSum.oscLe_eSmall_of_inert
  - GlobalTheory.T.depthOscillation_le_at_small_odd_inertPrime
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Depth bounds at odd inert primes

This section proves a lower bound for the determinant depth of a saturated frame on a formal group with a root of unity action, when the frame lies on an even type. With the [typed parts](/entry/typed-part-at/) of the previous section, it gives a window of small width for the depth of a factor in the CM type at an odd prime that is inert in $K_0 = \mathbb{Q}(\sqrt{-d})$. Summed over the factors, the windows give a bound for the oscillation of the depth at such a prime. The bound is one of the cases of [the oscillation bound at every prime](/entry/osc-le-e-of/).

We keep the notation of the previous section. All logarithms $\log_p$ are to base $p$.

**Theorem 3.2.1 (Determinant depth on an even type).** Let $C$ be an algebraically closed field of characteristic $0$ with an additive valuation $v$, $p \ge 3$ a prime with $v(p) = 1$, and $h > 0$ even. Let $G$ be a logarithmic formal group of dimension $d$ over $(C, v)$ with types $\mathrm{ty} \colon \{1, \dots, d\} \to \mathbb{Z}/h$ and an action of the roots of unity of order $p^h - 1$ as in the [typed part lemma](/entry/typed-part-at/). Let $j \in \mathbb{N}$ be such that at most $j$ coordinates have type $r$ for each $r$ with odd representative in $\{0, \dots, h - 1\}$. Let $\tau \in \mathbb{Z}/h$ be even, $c \ge 1$, and $u_1, \dots, u_i$ a saturated frame whose vectors vanish in all coordinates of type other than $\tau$. Then there is $c_r \in \mathbb{N}$ with $c_r \le i$ and $c_r \le j\bigl(\tfrac32 + \tfrac12 \log_p c\bigr)$ such that
$$\frac{(i - c_r)\, c\, p}{p^2 - 1} - i^2 (\log_p c + 1) \le \delta_c(G, u).$$

Lean: `GlobalTheory.DepthLow.detDepth_lower` (also `GlobalTheory.T.detDepth_lower_bound_saturated_even_type`, a second name).

For orientation, compare with the additive group, where $\delta_c = v(c!)$ is about $c/(p - 1)$. Here the main term is $c\, p/(p^2 - 1) = c/(p - 1) - c/(p^2 - 1)$ for each of the $i - c_r$ vectors. The vectors that meet the odd types, at most $c_r$ of them, are not counted.

*Proof.* Let $K$ be the least natural number with $c \le p^{2K+1}$. Then $K = 0$ or $p^{2K-1} < c$, so $K + 1 \le \tfrac32 + \tfrac12 \log_p c$. The root of unity action gives a basis $\gamma$ of the tangent space of $G$ with a stage number $\mathrm{dp}(b) \in \mathbb{N}$ for each basis vector. In this basis, the logarithm of $G$ is a sum of curves along $\gamma$, and the change of basis matrix is integral with determinant of valuation $0$. The number of basis vectors of type $\sigma$ with stage less than $K$ is at most $(K + 1)$ times the number of coordinates of type $\sigma - 1$. For even $\sigma$ the type $\sigma - 1$ is odd, so this number is at most $(K + 1) j$. Write the frame $u$ in the basis $\gamma$ as an integral frame $x$, which again vanishes off type $\tau$ and is saturated. Choose a new basis of the span of $x$, by an integral matrix of determinant of valuation $0$, such that the first $c_r$ vectors carry all the components along basis vectors of type $\tau$ and stage less than $K$. Then $c_r \le (K + 1) j \le j(\tfrac32 + \tfrac12 \log_p c)$. The determinant depth does not change under such a change of basis, and it can be computed in the integral coordinates given by $\gamma$.

Give the variable $X_a$ the radius $\rho_a$, a number that decreases with the stage, and is at least the radius of stage $K$ for $a > c_r$. Each linear form $\sum_a x'_{a,b} X_a$ then has order at least the radius of the stage of $b$. The exponential along $x'$ is a solution of the logarithm equations with these orders, so every integral function composed with it has order at least $\sum_a \rho_a$ in the sense of radii. A bound for the content of the power $D_{i,c}$ of the determinant, of the form $ic/(p - 1) - i^2 \log_p(c + 1)$, then turns these orders into the stated lower bound. The two kinds of radii contribute $c\,p/(p^2 - 1)$ for each of the $i - c_r$ late vectors and nothing for the early ones. $\square$

A factor $f = (\tau, j)$ is *big* for $k$ if $\tau \in \Psi$ and $k \le \mathrm{rk}(f) + 1$, *spread* for $k$ if $\tau \in \Psi$ and $\mathrm{rk}(f) + 2 \le k$, and *small* if $\tau \notin \Psi$. Every factor that is not big is small or spread. For $p$ prime and $N, j', i, k \in \mathbb{N}$ put
$$\begin{aligned}
\beta(p, N, j', i, k) &= \frac{k (N - 2j' - i)\, p}{p^2 - 1} + \frac{k j' (3 + \tfrac12 \log_p k)}{p - 1} \\
&\quad + i^2 (\log_p k + 1).
\end{aligned}$$

**Theorem 3.2.2 (Factor depth at an odd inert prime).** Let $p \ne 2$ be a prime with $p \nmid \mathrm{disc}(E)$ that is inert in $K_0$, $x$ a point of the flag model at $p$, $f = (\tau, j)$ a factor with $\tau \in \Psi$, and $k \ge 1$. Put
$$\begin{aligned}
A &= \frac{\bigl(\mathrm{rk}(f) - t(\tfrac32 + \tfrac12 \log_p k)\bigr) k\, p}{p^2 - 1} - \mathrm{rk}(f)^2 (\log_p k + 1), \\
B &= k\Bigl(\frac{t}{p - 1} + \frac{(s - t)\, p}{p^2 - 1}\Bigr).
\end{aligned}$$
Then $f$ is between $A$ and $B$ at $x$ for $k$, and $B - A \le \beta(p, s + t, t, \mathrm{rk}(f), k)$.

Lean: `GlobalTheory.RefSum.facBetween_fine` (also `GlobalTheory.T.factor_depth_bounded_odd_inert_prime_cmType`, a second name).

*Proof.* The upper bound $\nu_f(y, k) \le B$ for algebraic $y$ over $x$ is an upper bound for factor depths at odd unramified primes, which we take as an input. For the lower bound, let $y$ be an integral point over $x$, $\mathrm{Ch}$ an integral chart at $y$ and $C$ a valued extension. Since $\nu_f(y, k)$ is an infimum, it suffices to show $A \le \nu_f^{\mathrm{Ch}, C}(k)$. Take the [typed part](/entry/typed-part-at/) at $\tau$, with orbit $\sigma_r$ and group $G'$. By [the theorem on typed parts](/entry/formal-group-types/), part 1, and since $p$ is inert, $\sigma_{r+1} \in \Psi$ if and only if $\bar\sigma_r \in \Psi$, that is, if and only if $\sigma_r \notin \Psi$. As $\sigma_0 = \tau \in \Psi$, induction on $r$ gives that $h$ is even and $\sigma_r \in \Psi$ exactly for even $r$. So for odd $r$ the number of coordinates of type $r$ is $\mathrm{mult}(\sigma_r) = t$. The frame $P u_f$ is saturated, lies on type $0$ and has $\mathrm{rk}(f)$ vectors, and $\nu_f^{\mathrm{Ch}, C}(k) = \delta_k(G', P u_f)$. The theorem on even types with $j = t$ and $i = \mathrm{rk}(f)$ gives $c_r \le t(\tfrac32 + \tfrac12 \log_p k)$ and
$$\frac{(\mathrm{rk}(f) - c_r)\, k\, p}{p^2 - 1} - \mathrm{rk}(f)^2(\log_p k + 1) \le \nu_f^{\mathrm{Ch}, C}(k),$$
and the left side is at least $A$. For the width, a direct computation gives
$$\begin{aligned}
\beta - (B - A) &= k t \Bigl(\frac{1}{2(p - 1)} \\
&\quad + \bigl(\tfrac32 + \tfrac12 \log_p k\bigr)\Bigl(\frac{1}{p - 1} - \frac{p}{p^2 - 1}\Bigr)\Bigr),
\end{aligned}$$
with $\beta = \beta(p, s + t, t, \mathrm{rk}(f), k)$. This is nonnegative since $p/(p^2 - 1) \le 1/(p - 1)$ and $\log_p k \ge 0$. $\square$

To sum these windows we need bounds on the exponents. Let $F, k, m \in \mathbb{N}$. The datum has *shape* $(F, k, m)$ if $s + t + 1 = k + m$, $t \le m \le k$, $1 \le m$, $2 \le k$ and $[E : \mathbb{Q}] = 2F$. For a function $c$ from factors to $\mathbb{N}$ and $M_b, S_m \in \mathbb{R}$, $M \in \mathbb{N}$, the *exponent bound* holds if $0 \le M_b$, the sum of $c(f)$ over the big factors $f$ over $\tau$ is at most $M_b$ for each $\tau$, the sum of $\mathrm{rk}(f)\, c(f)$ over the small and spread factors is at most $S_m$, and $c(f) \le M$ for all $f$. Put
$$\begin{aligned}
e_{\mathrm{sm}}(p) &= \frac{F m M_b (4 + \tfrac12 \log_p M) + S_m}{p - 1} \\
&\quad + F (m + 1) N^2 (\log_p M + 1).
\end{aligned}$$

**Theorem 3.2.3 (Oscillation at an odd inert prime).** Assume the datum has shape $(F, k, m)$ and $c$ satisfies the exponent bound with $M_b$, $S_m$, $M$, where $M \ge 1$. Let $p \ne 2$ be a prime with $p \nmid \mathrm{disc}(E)$ that is inert in $K_0$. Then the oscillation at $p$ is at most $e_{\mathrm{sm}}(p) + 1$ for $c$.

Lean: `GlobalTheory.RefSum.oscLe_eSmall_of_inert` (also `GlobalTheory.T.depthOscillation_le_at_small_odd_inertPrime`, a second name).

*Proof.* Let $x$ be a point of the flag model at $p$. For each factor $f$ we choose $A_f \le B_f$ with $f$ between $A_f$ and $B_f$ at $x$ for $c(f)$. If $f$ is big and $c(f) \ge 1$, the previous theorem gives $B_f - A_f \le \beta(p, N, t, \mathrm{rk}(f), c(f))$. For the other factors we take $A_f = 0$ and $B_f = \mathrm{rk}(f)\, c(f)/(p - 1)$, by a general bound for factor depths that we take as an input. A rounding lemma, also an input, gives $n \in \mathbb{N}$ such that $\nu_p(\cdot, c)$ is between $n$ and $n + \sum_f (B_f - A_f) + 1$ at $x$. It remains to show $\sum_f (B_f - A_f) \le e_{\mathrm{sm}}(p)$. Since $t \le m$, $N \le m + \mathrm{rk}(f)$ for big $f$ and $c(f) \le M$, each fine width is at most
$$c(f)\, \frac{m (4 + \tfrac12 \log_p M)}{p - 1} + N^2 (\log_p M + 1).$$
Over each $\tau$ there are at most $m + 1$ big factors, since their ranks lie in an interval from $k - 2$ to $s$ and $s - k + 2 \le m + 1$. There are at most $F$ embeddings in $\Psi$, since $2|\Psi| \le [E : \mathbb{Q}] = 2F$. With the exponent bound, the big factors give at most the two terms of $e_{\mathrm{sm}}(p)$ that contain $M_b$ and $N^2$. The other factors are small or spread and give at most $S_m/(p - 1)$. $\square$

**Remark 3.2.4 (Formalization).** The upper bound for factor depths at odd unramified primes, the bound $0 \le \nu_f \le \mathrm{rk}(f) k/(p - 1)$, the rounding lemma for sums of windows, and the stage basis and radius lemmas in the proof of the theorem on even types are quoted by their statements; we did not open their proofs. The theorem on factor depths receives the agreement of the star of $\mathcal{O}_E$ with the host conjugation as `fun _ => rfl` ([FactorDepthBoundedOddInertPrimeCmType.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/FactorDepthBoundedOddInertPrimeCmType.lean#L41)). The oscillation theorem asks for no relation between $m$, $p$ and $k$, although its name speaks of a small prime; the case split in [the next section](/entry/osc-le-e-of/) uses it when $mp < k$ ([DepthOscillationLeAtSmallOddInertPrime.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/DepthOscillationLeAtSmallOddInertPrime.lean#L180)). In the definition of $\beta$, the second argument $j'$ is always the second signature number $t$. We have not unfolded the points of the flag model or the integral charts.
