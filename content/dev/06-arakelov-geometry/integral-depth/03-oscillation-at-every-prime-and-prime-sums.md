---
title: Oscillation at every prime and prime sums
decls:
  - GlobalTheory.RefSum.oscLe_eOf
  - GlobalTheory.T.depthOscillation_le_bound_every_prime
  - GlobalTheory.RefSum.sumAt_of_sizes
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Oscillation at every prime and prime sums

This section bounds the oscillation of the depth at every prime by one explicit function of the prime. The bound joins the [bound at odd inert primes](/entry/osc-le-e-small-of-inert/) of the previous section with bounds at split primes, at large primes, at the small primes of the host and at a finite set of special primes. Summed against $\log q$, the bound gives a prime sum. This is the oscillation sum that [the theorem on oscillation sums](/entry/sum-pt-of-sizes-alt/) of the previous chapter needs.

We keep the notation of the previous sections: a datum of signature $(s, t)$ with $N = s + t$, an exponent function $c$ on factors, a shape $(F, k, m)$ and an exponent bound with $M_b$, $S_m$, $M$.

**Definition 3.3.1 (The exponent at a prime).** Let $\mathrm{vd}$ be a function from the natural numbers to $\mathbb{R}$, and $S$, $R$ finite sets of natural numbers. For a prime $p$ put $e(p) = 0$ if $M < p$. Otherwise put
$$e(p) = \begin{cases}
F m (1 + \tfrac12 \mathrm{vd}(p)) M_b + S_m & \text{if } p \in S, \\
(F N M_b + S_m)/(p - 1) & \text{if } p \notin S,\ p \in R, \\
e_{\mathrm{sm}}(p) + 1 & \text{if } p \notin S \cup R,\ mp < k, \\
(6 F m M_b + S_m)/(p - 1) + 1 & \text{otherwise.}
\end{cases}$$
Here $e_{\mathrm{sm}}(p)$ is the bound of the previous section.

For example, $e(5) = 0$ when $M = 3$, whatever the other data are. The set $S$ will be the set of small primes of the host, and $R$ the set of the two host integers.

A prime $q$ satisfies the *splitting condition* with the number $\mathrm{vd}(q)$ if the places of $E$ over $q$ split in the way that the bound at the small primes needs, with a weighted sum of local data equal to $F\,\mathrm{vd}(q)$. We do not unfold this condition.

**Theorem 3.3.2 (Oscillation at every prime).** Assume the datum has shape $(F, k, m)$ and $c$ satisfies the exponent bound with $M_b$, $S_m$, $M$. Let $\mathrm{vd} \ge 0$ and let $S$, $R$ be finite sets with:

1. every $q \in S$ is a prime that satisfies the splitting condition with $\mathrm{vd}(q)$;
2. $2 \in S$ and $d \in R$;
3. every prime $q \notin S \cup R$ is unramified in $E$.

Then for every prime $p$ the oscillation at $p$ is at most $e(p)$ for $c$.

Lean: `GlobalTheory.RefSum.oscLe_eOf` (also `GlobalTheory.T.depthOscillation_le_bound_every_prime`, a second name).

*Proof.* We follow the cases of the definition of $e(p)$. Four bounds are inputs whose proofs we did not open: a bound $0$ for $M < p$, together with the bound $(F N M_b + S_m)/(p - 1)$ at every prime; a bound $F m (1 + \tfrac12 \mathrm{vd}) M_b + S_m$ at a prime with the splitting condition; a bound $(F m M_b + S_m)/(p - 1)$ at an odd unramified prime that is split in $K_0$; and a bound $(6 F m M_b + S_m)/(p - 1) + 1$ at an unramified prime that is inert in $K_0$ with $k \le mp$.

If $M < p$, the first input gives $0$. If $M \ge p$ and $p \in S$, the splitting condition at $p$ and the second input give the bound. If $p \in R \setminus S$, the bound at every prime gives it. Now let $p \notin S \cup R$ with $p \le M$. Then $p \ne 2$ because $2 \in S$, $p$ is unramified by condition 3, and $p \ne d$ because $d \in R$, so $p \nmid d$. If $-d$ is a square modulo $p$, then $p$ is split in $K_0$, and the third input gives the oscillation bound $(F m M_b + S_m)/(p - 1)$. This is at most both of the last two values of $e(p)$: the first because $4 + \tfrac12 \log_p M \ge 1$ and the other term of $e_{\mathrm{sm}}(p)$ is nonnegative, and the second because $F m M_b \le 6 F m M_b$. An oscillation bound can be raised, so the bound $e(p)$ follows. If $-d$ is not a square modulo $p$, then $p$ is inert. If $mp < k$, [the theorem at odd inert primes](/entry/osc-le-e-small-of-inert/) gives $e_{\mathrm{sm}}(p) + 1$, since $M \ge p \ge 1$. If $k \le mp$, the fourth input gives the last value. $\square$

Now we return to the setting of [the previous chapter](/entry/sum-pt-of-sizes-alt/): a point and a level $i$, the length $T$, the unit of error $U$, a quotient weight $u_1$ with column weight $a(u_1)$, and the two host primes $g_0$, $g_1$. The *gap* of a weight $a$ on factors is the function on factors with
$$\mathrm{gap}(a)(\tau, j) = a(\tau, j) - a(\tau, j + 1),$$
read as $0$ when $j + 1 = \mathrm{mult}(\tau)$. A *prime sum* is a triple $(S, e, s)$ with $S$ a finite set of primes, $e \ge 0$, $e = 0$ off $S$, and $\sum_{q \in S} e(q) \log q \le s$. The *oscillation sum* with constant $C$ holds for $u_1$ if there is a prime sum $(S, e, s)$ with $T s \le C U$ such that for every prime $q$ other than $g_0$, $g_1$ the oscillation at $q$ is at most $e(q)$ for $\mathrm{gap}(a(u_1))$, on the moduli space of the level $i + 1$.

**Theorem 3.3.3 (Oscillation sums from weight and numerical bounds).** Let $C_1, C_2 \ge 0$. Assume that the weight bounds hold for $u_1$ with constant $C_1$ and the numerical bounds hold with constant $C_2$, in the sense of [the previous chapter](/entry/sum-pt-of-sizes-alt/). Put $K = 2C_1 + C_2 + 1$. Then the oscillation sum holds for $u_1$ with the constant
$$40\,(4 C_1 K^2 + C_2 K + 2 C_1)\, C_2.$$

Lean: `GlobalTheory.RefSum.sumAt_of_sizes`

*Proof.* The weight bounds give the shape $(F, k, m)$ of the datum, $k \le s + 1$, and $B \in \mathbb{N}$, $\Sigma \in \mathbb{R}$ that bound the entries and partial sums of $u_1$. A lemma on theta exponents, which we take as an input, turns these into the exponent bound for $\mathrm{gap}(a(u_1))$ with
$$M_b = B + 1, \qquad S_m = F(\Sigma + 2tB), \qquad M = 2B + 1.$$
Take for $S$ the set of small primes of the host and $R = \{q_H, d\}$, where $q_H$ and $d$ are the two primes of the host that the numerical bounds name. The host gives the splitting condition at each $q \in S$, $2 \in S$, unramified primes off $S \cup R$, and the bound
$$\sum_{q \in S} (1 + \tfrac12 \mathrm{vd}(q)) \log q \le \tfrac32 K L.$$
Put $\ell_2 = K L$ and $\ell = K \log\log x$, so $\ell_2, \ell \ge 1$. The numerical bounds give $\log N \le \ell_2$, $\log \log k \le \ell$, and $N \log q/(q - 1) \le m \ell_2$ for $q \in R$. From $T(B + 1) \le C_1 b$ and $\log b \le C_2 L$ we get
$$\log(2B + 1) \le \log\bigl((2C_1 + 1) b\bigr) \le K L.$$
A summation lemma for the function $e$, an input, then shows that the restriction of $e$ to the primes up to $M$ is a prime sum with
$$\begin{aligned}
s = 40\bigl(&(F m M_b + S_m)\, \ell_2\, \ell \\
&+ F N^3 \ell_2 + M\bigr).
\end{aligned}$$
For the length, insert $M_b$, $S_m$, $M$ and use $T(B + 1) \le C_1 b$, $T \Sigma \le C_1 b$, $t \le m$, $T N^3 \le C_2 b$ and $F m b L \log\log x \le C_2 U$. Each term of $T s$ is then at most a multiple of $C_2 U$, and the sum is at most the stated constant times $U$. Finally, the theorem on every prime gives the oscillation bound $e(q)$ at every prime $q$. For $q > M$ we have $e(q) = 0$ in both readings. $\square$

**Remark 3.3.4 (Formalization).** In the theorem on every prime, the bound at the primes of $S$ is a lemma whose name speaks of the prime $2$, but it is applied at every $p \in S$ ([DepthOscillationLeBoundEveryPrime.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/DepthOscillationLeBoundEveryPrime.lean#L30)). The case $p \in R$ uses a bound that holds at every prime, so membership in $R$ is not used there; the conditions $2 \in S$ and $d \in R$ only serve to exclude $p = 2$ and $p = d$ in the last cases. The two last cases are closed by tactic alternatives (`first | ... | ...`) at lines 48 to 61, and the odd inert case with $mp < k$ uses a theorem that does not need $mp < k$. The oscillation sum asks for the bound only at primes other than the host primes, but the proof proves it at every prime and drops this hypothesis (`fun q hqp _`, [SumPointOfWeightNumerical.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SumPointOfWeightNumerical.lean#L89)). The definition of $e(p)$ is followed by a sanity example with $M = 3$, $p = 5$ ([ESmall.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ESmall.lean#L51)). The splitting condition, the four bounds of the first proof, the lemma on theta exponents and the summation lemma are quoted by their statements.
