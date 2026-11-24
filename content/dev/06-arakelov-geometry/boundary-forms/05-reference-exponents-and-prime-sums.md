---
title: Reference exponents and prime sums
decls:
  - GlobalTheory.RefSum.sumPt_of_sizes_alt
  - GlobalTheory.T.sum_pt_of_wt_pt_num_pt
  - GlobalTheory.RefSum.sumPt_of_size_alt
  - GlobalTheory.T.sum_pt_of_size
  - GlobalTheory.RefSum.refCore_of_size_sumPt
  - GlobalTheory.T.reference_core_of_size_and_sum_point
  - GlobalTheory.RefSum.refinedSum_weight_of_size_alt
  - GlobalTheory.T.refW_of_prints_deepGood_size_flatDeg
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Reference exponents and prime sums

The section that carries cusp forms from one weight to another (the next section) needs a bound for the finite places. At each prime $q$, the lattice of cusp forms of a weight can differ from the reference lattice by a power of $q$, and the exponent of this power is the reference exponent at $q$. This section proves that the reference exponents of a weight are bounded by a *prime sum*: a function $e$ on primes, supported on a finite set, with $T \sum_q e_q \log q \le C E$. The bound is proved first for the theta weight of the core tower, then on each good cover, and then for the weight itself. The constant $C$ is uniform in the sense of [the first section](/entry/to-classical-theorems/). The result enters the multiplicity estimate of the height lower bound.

We fix a point $p$ and a level $i$ with $i + 1 < m$, so that covers exist. Let $T$ be the length and $E$ the unit of error. A weight $u_1$ of the datum at level $i + 1$ is a *quotient weight* if it is the quotient weight of the level for the length $T$; the size condition says that quotient weights exist. For a quotient weight $u_1$ we write $a(u_1)$ for the associated column weight, $G(u_1)$ for the theta weight of $a(u_1)$ with the number of columns of the datum, and $g(u_1)$ for the gap of $a(u_1)$. Let $g_0$ and $g_1$ be the two host primes.

**Definition 2.5.1 (Prime sum).** Let $S$ be a finite set of natural numbers, $e$ a function from the natural numbers to $\mathbb{R}$ and $s \in \mathbb{R}$. The triple $(S, e, s)$ is a *prime sum* if every element of $S$ is a prime, $e_q \ge 0$ for all $q$, $e_q = 0$ for $q \notin S$, and
$$\sum_{q \in S} e_q \log q \le s.$$

**Definition 2.5.2 (Reference bound).** Let $U$ be a family of uniformizations at level $i + 1$ and $G$ a weight. The *reference bound* with constant $C$ holds for $(U, G)$ if there is a prime sum $(S, e, s)$ with $T s \le C E$ such that for every prime $q$
$$r_q(U, G) \le e_q,$$
where $r_q(U, G) \in [-\infty, \infty]$ is the reference exponent of the weight $G$ at $q$ for $U$, with the parameter $1/2500$.

**Definition 2.5.3 (Oscillation sum).** For a quotient weight $u_1$, the *oscillation sum* with constant $C$ holds if there is a prime sum $(S, e, s)$ with $T s \le C E$ such that for every prime $q$ other than $g_0$ and $g_1$ the oscillation of the moduli space at $q$ for the gap $g(u_1)$ is at most $e_q$.

We do not unfold the reference exponent, the oscillation at $q$ or the gap. Their role is the following: at a prime $q$ other than the host primes, a bound for the oscillation at $q$ is a bound for the reference exponent of the theta weight at $q$.

Two families of numerical conditions enter.

**Definition 2.5.4 (Weight bounds and numerical bounds).** At $(p, i)$ with parameter $P$ and constant $C$, the *weight bounds* for a quotient weight $u_1$ say: the ranks have the shape of the family, $k \le p_i + 1$, and there are $B \in \mathbb{N}$ and $\Sigma \in \mathbb{R}$ such that the entries of $u_1$ are bounded by $B$ and their partial sums by $\Sigma$ (with the conditions on the shape of $u_1$ that we do not list), and
$$T (B + 1) \le C b, \qquad T \Sigma \le C b, \qquad 1 \le T.$$
The *numerical bounds* say: $1 \le L$, $1 \le b$, $\log b \le C L$, $1 \le \log \log x$, $f m b L \log\log x \le C E$, $\log \log k \le C \log\log x$, $\log r \le C L$, $T r^3 \le C b$, and $r \log t / (t - 1) \le C m L$ for the two integers $t$ of the host.

The *weight statement* is the level statement of the weight bounds for all quotient weights at the levels $i + 1 < m$. The *numerical statement* is the level statement of the numerical bounds at the levels $i + 1 < m$. The *oscillation statement* is the level statement of the oscillation sum for all quotient weights at the levels $i + 1 < m$.

**Theorem 2.5.5 (Oscillation sums from the weight bounds).** The weight statement and the numerical statement imply the oscillation statement. If they hold with constants $C_1$ and $C_2$, the oscillation statement holds with the constant
$$C = 40 \bigl( 4 C_1 K^2 + C_2 K + 2 C_1 \bigr) C_2, \qquad K = 2 C_1 + C_2 + 1.$$

Lean: `GlobalTheory.RefSum.sumPt_of_sizes_alt` (also `GlobalTheory.T.sum_pt_of_wt_pt_num_pt`, a second name).

*Proof.* At each point and level, this is [Theorem 3.1](/entry/sum-at-of-sizes/) of the chapter on integral depth, applied to the weight bounds with $C_1$ and the numerical bounds with $C_2$. The constant does not depend on the point, so the pointwise statements combine into a level statement. $\square$

**Theorem 2.5.6 (Oscillation sums from the size condition).** The size condition implies the oscillation statement.

Lean: `GlobalTheory.RefSum.sumPt_of_size_alt` (also `GlobalTheory.T.sum_pt_of_size`, a second name).

*Proof.* The weight statement holds, since the weight numerics hold as a level statement and they imply the weight bounds. The numerical statement holds without any hypothesis, with the constant $|C_t| + 20$, where $C_t$ is a constant of the family. So [Theorem 2.5.5](/entry/sum-pt-of-sizes-alt/) applies. $\square$

**Theorem 2.5.7 (Reference bound on the core tower).** The size condition and the oscillation statement imply the following level statement: at the levels $i + 1 < m$, for every quotient weight $u_1$, the reference bound holds for the uniformizations $U_{i+1}$ of the core tower and the theta weight $G(u_1)$.

Lean: `GlobalTheory.RefSum.refCore_of_size_sumPt` (also `GlobalTheory.T.reference_core_of_size_and_sum_point`, a second name).

*Proof.* Let $C_1$ be the constant of the oscillation statement. The size condition gives, as level statements, bounds on the gaps of the quotient weights and bounds on the jet numbers, the number of columns and the length; let $C_3$ be the constant of the second, which includes $T(\log g_0 + \log g_1) \le C_3 E$. Fix a point, a level and a quotient weight $u_1$, with the oscillation prime sum $(S, e, s)$. Add the two host primes to the sum: put $S' = S \cup \{g_0, g_1\}$, $e' = e + \mathbf{1}_{\{g_0, g_1\}}$ and $s' = s + \log g_0 + \log g_1$. This is a prime sum, and $T s' \le (C_1 + C_3) E$. Now let $q$ be a prime. If $q$ is a host prime, the reference exponent of the theta weight at level $i + 1$ is at most $1 \le e'_q$. If $q$ is not a host prime, the oscillation at $q$ is at most $e_q$, so by [Theorem 3.4](/entry/base-locus-exponent-le-oscillation-non-type-prime/) of the chapter on integral depth the reference exponent of the theta weight at $q$ is at most $e_q = e'_q$; this theorem uses the jet number and column bounds given by the size condition. $\square$

The constant of the result is $C_1 + C_3$.

**Theorem 2.5.8 (Reference bound for the weight).** Assume the published Hodge bundle theorems, deep goodness, the size condition and the flat degree condition. Then the following cover statement holds: for every good cover $Y$ at a level $i + 1 < m$ and every quotient weight $u_1$, the reference bound holds for the uniformizations of $Y$ and the weight $u_1$ (with the trivial character).

Lean: `GlobalTheory.RefSum.refinedSum_weight_of_size_alt` (also `GlobalTheory.T.refW_of_prints_deepGood_size_flatDeg`, a second name).

*Proof.* By [Theorem 2.5.6](/entry/sum-pt-of-size-alt/) the oscillation statement holds, and by [Theorem 2.5.7](/entry/ref-core-of-size-sum-pt/) the reference bound holds on the core tower for the theta weights. The size condition moves the reference bound from the core tower to every good cover: the reference exponent on a cover is at most the reference exponent on the core tower. Finally, the published list, the size condition and the flat degree condition give the change of weight from the theta weight $G(u_1)$ to the weight $u_1$. For this one adds the bad primes of the level to the prime sum and bounds the reference exponents there by a valuation bound, which uses the flat degree. $\square$

**Remark 2.5.9 (Formalization).** The size condition is not used in the second theorem: the weight statement comes from `wt_pt_of_cov_size := fun _ => wtPt_of_wtN_alt lift_weight_numerator` ([WtPtOfSize.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/WtPtOfSize.lean#L25)) and the numerical statement from `numPt_of_size' := fun _ => numPt_alt` ([NumPtOfSize.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/NumPtOfSize.lean#L25)), both of which discard it. So the oscillation statement holds unconditionally. The last theorem discards deep goodness: it is `fun hP _ hS hF => …` ([RefinedSumWeightOfSizeLe.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RefinedSumWeightOfSizeLe.lean#L16)), with its second name at line 23. The steps from the core tower to the covers and from the theta weight to the weight are lemmas that we have not opened beyond their statements, so the description of them in the last proof follows their names and their inputs. We have not unfolded `refExp_vp`, `OscLe`, `gap`, `aOf`, `GOf`, the quotient weights `Quo` or the shape conditions `WtBd` and `Shape`.
