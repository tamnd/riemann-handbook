---
title: The sum for the exceptional set
decls:
  - UpperTheory.ExcSet.sum_exponent_log_le
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The sum for the exceptional set

This section proves the bound for the sum of the seventh recursion when the special primes of the weights form the exceptional set of the host. The bound is used by [the exponent bound at a point](/entry/has-exp-bound-at/) of section 08, for its clause 2, in the surjectivity branch of [the unitary hypotheses](/proof/unitary-hypotheses/). It reduces to [the sum of the seventh recursion](/entry/sum-exponent-log-le-of-cut/) of section 08, which needs at most $5$ special primes. The exceptional set can be larger, so the proof first shows that the extra primes do not change $J^{(7)}$.

### The exceptional set

We keep the notation of section 08: the parameters $P$ with the thresholds $\ell_J$ and $h$, the numbers $m$, $b$, $L$, $k$ and $t$; the weights $W$ on a set of $f$ indices, with the set $T_2$ of large weights and the set of special primes; the naive bound $J_A$, the coarse bound $c_W$ and the seventh recursion $J^{(7)}$, with a prime "in range" when $\ell_J < \ell \leq h$, $\ell$ is not excluded and $\ell$ is not special.

The host of the datum $D$ has two odd primes $q$ and $d$, a positive integer $Q_S$ and two further primes $p_{\mathrm{de}}$ and $p'_{\mathrm{de}}$. The *small set* is the set of prime factors of $Q_S$. The *ramified set* and the *exceptional set* are

$$\begin{aligned} \mathrm{Ram}(D) &= \mathrm{small}(D) \cup \{q, d\}, \\ \mathrm{Exc}(D) &= \mathrm{small}(D) \cup \{q, d, p_{\mathrm{de}}, p'_{\mathrm{de}}\}. \end{aligned}$$

The conductor of the host field divides $Q_S\, q\, d$. So a prime that divides the discriminant of the host field lies in $\mathrm{Ram}(D)$, hence in $\mathrm{Exc}(D)$. The host also gives $Q_S \leq n^2$, where $f = 2n$ is the degree of the datum.

**Theorem 7.13.1 (Sum for the exceptional set).** Assume the cut inequality for the exponents of dual Weyl modules. Let $D$ be a datum, and let $P$ satisfy its hypotheses and be large, with the row and size estimates for some $X'$ and $A$, and with $f = f(D)$. Let $W$ be good weights for $P$ on a set of $f$ indices, whose set of special primes is $\mathrm{Exc}(D)$. Let $T$ be a natural number with $|T_2| \leq T$. Then for every finite set $Q$ of primes,

$$\sum_{\ell \in Q} J^{(7)}(\ell) \log \ell \leq 30\, T\, m\, b\, L^2 + 2 m b.$$

Lean: `UpperTheory.ExcSet.sum_exponent_log_le`.

*Proof.* We take the steps in order.

1. Let $S = \{q, d, p_{\mathrm{de}}, p'_{\mathrm{de}}\}$, and let $W'$ be the weights $W$ with the set of special primes replaced by $S$. All the conditions for good weights other than the special primes are the same for $W$ and $W'$. So $W'$ is good for $P$. The set $S$ has at most $4$ elements, so at most $5$.
2. Every prime $\ell$ of the small set satisfies $\ell \leq \ell_J$. Indeed $\ell$ divides $Q_S$, so $\ell \leq Q_S \leq n^2$. The hypotheses of $P$ give $n \leq k$ and $n \leq t$, so $n^2 \leq k t$. The parameter bounds for a large $P$ give $k t \leq \ell_J$.
3. For each prime $\ell$, the three conditions "$\ell \leq \ell_J$, $\ell$ is excluded, or $\ell \in S$" and "$\ell \leq \ell_J$, $\ell$ is excluded, or $\ell \in \mathrm{Exc}(D)$" are equivalent. One direction holds since $S \subseteq \mathrm{Exc}(D)$. For the other, a prime of $\mathrm{Exc}(D)$ outside $S$ is in the small set, and then $\ell \leq \ell_J$ by step 2.
4. The seventh recursion takes the value $J_A(\ell)$ when the condition of step 3 holds and $c_W(\ell)$ otherwise. The numbers $J_A(\ell)$ and $c_W(\ell)$ do not depend on the special primes. So step 3 gives $J^{(7)}_{W'}(\ell) = J^{(7)}_{W}(\ell)$ for every $\ell$.
5. [The sum of the seventh recursion](/entry/sum-exponent-log-le-of-cut/) for $W'$, with at most $5$ special primes and $|T_2| \leq T$, gives

$$\sum_{\ell \in Q} J^{(7)}_{W'}(\ell) \log \ell \leq 30\, T\, m\, b\, L^2 + 2 m b.$$

By step 4 the left side is the sum for $W$.

This proves the theorem. $\square$

The proof shows a little more. For any set $S'$ with $S \subseteq S' \subseteq \mathrm{Exc}(D)$, the seventh recursion with the special primes $S'$ is the same. So the small primes of the host play no role in the bound, since they lie below the threshold $\ell_J$ in any case.

In section 08 the theorem is applied at each index $j$ of the run, with the weights $W_j$ of the matching numerical datum. There the special primes of $W_j$ are the exceptional set of the host by construction, the number of indices is $f$, and the bound on $|T_2|$ comes from the host. With $L = x_e$ and $b = e^{x_e}$, the right side is the bound that clause 2 of the exponent bound asks for.

**Remark 7.13.2 (Formalization).** The theorem is at line 50 of [ExcSet.lean](lean:Development/AutomorphicArithmetic/PrimeDiscriminants/ExcSet.lean#L50). It builds the changed weights by the structure update `{ W with Sp := S }` and checks the nine fields of `Wts.Ok` by hand. The bound for the small primes is `small_le_lJ` at line 30, which uses `QS_le`, the inequalities `t_ge` and `f_pos` of the hypotheses and the first part of `paramsLJ_holds`. The exceptional set is `excSet` at line 472 of [JumpSets.lean](lean:Formalism/SharpRestriction/Divisibility/JumpSets.lean#L472), and the ramified set `ramSet` is at line 474. The lemmas `mem_ramSet_of_dvd` at line 10, `ramSet_subset_excSet` at line 20 and `not_dvd_discr` at line 26 of ExcSet.lean prove the fact on the discriminant stated above, but the main theorem does not use them. The theorem it reduces to is `GlobalTheory.sum_exponent_log_le_of_cut`, stated in section 08.
