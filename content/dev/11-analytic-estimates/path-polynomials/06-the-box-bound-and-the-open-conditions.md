---
title: The box bound and the open conditions
decls:
  - Formalism.MainNotions.G.SymmetricFormBlocks.restTM_exists
  - Formalism.MainNotions.G.SymmetricFormBlocks.restTM_closed
  - Formalism.MainNotions.G.SymmetricFormBlocks.openE_of_open4
  - Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_open_directions
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The box bound and the open conditions

The closed form of Theorem A is an averaged bound on bad shares: over a box of window points, the mean bad share of the segment lattices at a certain depth is at most a constant times $(t + 1) N_1 / Y$. Its proof in [Theorem 5.18](/entry/theorem-a-closed-form-holds/) reduces it to four *open conditions* on the blocks of an instance. This section proves two of the four: the block bound, from Section 4, and the box bound, from the [alternative mean value theorem](/entry/alternative-mean-value-theorem/). It follows that the closed form holds as soon as four other conditions hold, and Section 7 proves those from the lattice results of Section 1.

We keep the instances $X$, blocks $G(a_{\mathrm{top}}, a_+, b)$, level lattices $\Lambda_{j,j_+}$, pairings $\beta_{j,j_+}$ and bad counts of Sections 3 and 4.

**Definition 7.6.1 (For large constants).** Let $P(C_0, C_{Yb}, C_{de}, C_k, C_D, C_b, C_{E1}, C_{E2}, C_c)$ be a statement about nine real constants. We say that $P$ holds *for large constants* if for every $C_c \geq 0$ there is $T_0 > 0$ such that for every $C_0 \geq T_0$ there is $T_1 > 0$ such that for all $C_{E1}, C_{E2} \geq T_1$ there is $T_2 > 0$ such that $P$ holds whenever $C_{Yb}, C_{de}, C_k, C_D, C_b \geq T_2$.

The order of the quantifiers matters: each threshold may depend on the constants chosen before it. If $P$ implies $Q$ whenever $C_0 \geq 1$, $C_{Yb} \geq 2$, $C_D \geq 0$, $C_b \geq 1$ and $C_{E1}, C_{E2} \geq 0$, then $P$ for large constants implies $Q$ for large constants: raise $T_0$ to at least $1$ and $T_2$ to at least $2$.

**Definition 7.6.2 (Classes, boxes and level ranks).** Fix an instance $X$ with constants. The kept blocks fall into *classes* $\delta$, according to two of their numerical invariants. For a class $\delta$, the *box* $\operatorname{box}(\delta)$ is the set of points $a_{\mathrm{top}} \in A^{s}$ compatible with $\delta$, and for $a_{\mathrm{top}}$ in the box, $I(\delta, a_{\mathrm{top}})$ is the set of pairs $(b, \ell)$ of a kept block $b$ of class $\delta$ and a level $\ell = (j, j_+)$ of $G(a_{\mathrm{top}}, 0, b)$. For $n \geq 0$ let $d_r(n) = \binom{n + r - 1}{r - 1}$, the number of monomials of degree $n$ in $r$ variables. The *level rank* is
$$r_L(a_{\mathrm{top}}, b, \ell) = \dim Y_\ell(G(a_{\mathrm{top}}, 0, b))\, d_r(B - j_+),$$
where $Y_\ell$ is the highest weight space of the level and $B$ the top degree of the block. Let $\operatorname{bad}_Y(a_{\mathrm{top}}, b, \ell, D)$ be the bad count of the highest weight lattice of the level for the pairing through $\Phi$, and $\operatorname{bad}_\ell(a_{\mathrm{top}}, a_+, b, D)$ the bad count of $\Lambda_\ell(G(a_{\mathrm{top}}, a_+, b))$ for $\beta_\ell$, at depth $D$.

**Definition 7.6.3 (Depth).** Let $\kappa_S = 3(s + 2) r^2 \lambda$, with $\lambda$ the logarithmic size of the instance. For $C_M \geq 1$ the *reduced depth* is $D_1(C_M) = t (Y \kappa_S + C_M \kappa_S) + C_M \kappa_S$.

**Definition 7.6.4 (Box bound).** The instance satisfies the *box bound* with constant $C_M$ if for every class $\delta$, every $a_0 \in \operatorname{box}(\delta)$ and every $(b, \ell) \in I(\delta, a_0)$,
$$\sum_{a_{\mathrm{top}} \in \operatorname{box}(\delta)} \operatorname{bad}_Y(a_{\mathrm{top}}, b, \ell, \lfloor D_1(C_M) \rfloor) \leq \frac{30 + C_M}{Y} \sum_{i = 1}^{t} \sum_{a_{\mathrm{top}} \in \operatorname{box}(\delta)} \dim Y_\ell\bigl(G(a_{\mathrm{top}}^{(i)}, 0, b)\bigr),$$
where $a_{\mathrm{top}}^{(i)}$ is the box point obtained from $a_{\mathrm{top}}$ by a change in its $i$-th tie coordinate.

The box bound says that, summed over a box, the highest weight lattices are bad only on a share $(30 + C_M) / Y$ of the dimension. It is a mean value statement: for one box point the bad count can be large.

**Theorem 7.6.5 (Box bound from three conditions).** There is $C_M \geq 1$ with the following property. Let $X$ be an instance satisfying the window hypotheses, and assume:

1. the index sets $I(\delta, a_{\mathrm{top}})$ do not depend on $a_{\mathrm{top}} \in \operatorname{box}(\delta)$;
2. the size conditions: at each $(\delta, a, b, \ell)$ the tie sizes are bounded by the corresponding numbers $n_0$, and the letter degrees and tie lengths by $2a$;
3. at each $(\delta, a, b, \ell)$ the tie exponents $\varepsilon_i$ of the associated mean value instance are at most $(30 + C_M)/Y$.

Then $X$ satisfies the box bound with constant $C_M$. One can take $C_M = 1$.

Lean: `Formalism.MainNotions.G.SymmetricFormBlocks.restTM_exists`.

*Proof.* Take $C_M = 1$. Fix $\delta$, $a_0$ and $(b, \ell)$. By condition 1 the pair $(b, \ell)$ is an index at every point of the box, so each box point defines a mean value instance: the word of the block at level $\ell$, its ties, the window $A$, the exponents $\varepsilon_i$ and the sizes. Conditions 2 and 3 are the hypotheses of the [alternative mean value theorem](/entry/alternative-mean-value-theorem/) for these instances. That theorem bounds the sum over the box of the bad counts at depth $\lfloor D_1(C_M) \rfloor$ by $\max_i \varepsilon_i$ times the sum of the dimensions of the highest weight spaces after a change of one tie coordinate, summed over the ties; condition 3 bounds $\max_i \varepsilon_i$ by $(30 + C_M) / Y$. $\square$

**Theorem 7.6.6 (Box bound).** There is $C_M \geq 1$ such that every instance $X$ satisfying the window hypotheses with $C_{Yb} \geq 2$, $C_b \geq 1$, $C_D \geq 0$, $C_0 \geq 1$ and $C_{E1}, C_{E2} \geq 0$ satisfies the box bound with constant $C_M$.

Lean: `Formalism.MainNotions.G.SymmetricFormBlocks.restTM_closed`.

*Proof.* Take $C_M$ from the previous theorem. Under these hypotheses the segment data satisfy the segment facts of [Theorem 5.18](/entry/theorem-a-closed-form-holds/). The segment facts give condition 1: the index sets only depend on the class. With condition 1 they give the size conditions 2. For condition 3, the tie exponent at a tie is bounded by
$$\frac{2 S}{Y_r} + \frac{2 \kappa + 2 S \lambda / Y_r}{Y \kappa},$$
where $S / Y_r \leq 7 / Y$, $\kappa > 0$ and $24 \lambda \leq \kappa$; the last inequality holds because $\kappa \geq \kappa_S \geq 24 \lambda$ for $r \geq 2$ and $s \geq 0$. This is at most $(15 + C_M)/Y \leq (30 + C_M)/Y$ when $Y \geq 1$ and $C_M \geq 1$. The previous theorem applies. $\square$

**Definition 7.6.7 (Open conditions).** Let $X$ be an instance and $C_M \geq 0$. The four *open conditions* are:

1. (Block bound.) For every block $G(a_{\mathrm{top}}, a_+, b)$ and every integer $D \geq 0$, the block lattice contains a sublattice of good pairs for the block pairing up to $p^{D + \ell(X)}$, whose rank misses the rank of the block lattice by at most the block bad count at depth $D$.
2. (Positive part.) For every class $\delta$, every $a_{\mathrm{top}} \in \operatorname{box}(\delta)$ and every $(b, \ell) \in I(\delta, a_{\mathrm{top}})$,
$$\begin{aligned}
&\sum_{a_+ \in A} \operatorname{bad}_\ell(a_{\mathrm{top}}, a_+, b, \lfloor Y D_1(C_M) \rfloor) \\
&\quad \leq |A| \Bigl(\operatorname{bad}_Y(a_{\mathrm{top}}, b, \ell, \lfloor D_1(C_M) \rfloor)\, d_r(B - j_+) + \frac{5}{Y}\, r_L(a_{\mathrm{top}}, b, \ell)\Bigr).
\end{aligned}$$
3. The box bound with constant $C_M$.
4. (Directions.) For every block, the sum of the level ranks $r_L$ over the levels is at most the rank of the block lattice.

The closed form holds for large constants if the open conditions hold, for large constants and for all admitted instances, with some $C_M \geq 0$ depending on the constants; this is the reduction in [Theorem 5.18](/entry/theorem-a-closed-form-holds/). We now show that four other conditions suffice:

1. (Base dimension.) For every block, the rank of the block lattice is at most the sum of the ranks of its level lattices.
2. (Level part.) $\operatorname{bad}(\beta_\ell, \Lambda_\ell, \lfloor D_1(C_M) \rfloor) \leq \operatorname{bad}_Y(a_{\mathrm{top}}, b, \ell, \lfloor D_1(C_M) \rfloor)\, d_r(B - j_+)$ at each $(\delta, a_{\mathrm{top}}, b, \ell)$, for the blocks with $a_+ = 0$.
3. (Sum over the window.) $\sum_{a_+ \in A} \operatorname{bad}_\ell(a_{\mathrm{top}}, a_+, b, \lfloor Y D_1(C_M) \rfloor) \leq |A| \bigl(\operatorname{bad}(\beta_\ell, \Lambda_\ell, \lfloor D_1(C_M) \rfloor) + \frac{5}{Y} \operatorname{rk} \Lambda_\ell\bigr)$ at each $(\delta, a_{\mathrm{top}}, b, \ell)$.
4. The directions condition.

**Proposition 7.6.8 (Open conditions from four conditions).** Assume that for large constants, for all $C_\kappa, C_s$, all $C_M \geq 1$ and all admitted instances $X$ satisfying the window hypotheses, the base dimension, level part, sum over the window and directions conditions hold. Then the open conditions hold for large constants, for all admitted instances, with one constant $C_M$.

Lean: `Formalism.MainNotions.G.SymmetricFormBlocks.openE_of_open4`.

*Proof.* Take $C_M \geq 1$ from the Theorem (Box bound), and apply the hypothesis with this $C_M$. The constants are large, so the conditions $C_0 \geq 1$, $C_{Yb} \geq 2$, $C_D \geq 0$, $C_b \geq 1$, $C_{E1}, C_{E2} \geq 0$ may be assumed, by the remark after the definition of large constants. Then $Y > 0$. Open condition 1: the [Theorem (Block valuation bound over $\mathbb{Z}_p$)](/entry/block-valuation-over-zp-holds/) gives dual pairs in the standard lattice; with the base dimension condition they give the block bound, because the rank of the block lattice is at most the total rank of the level lattices, which the dual pairs miss by at most the block bad count. Open condition 2: the rank of a level lattice $\Lambda_\ell$ is at most $r_L$, since it is generated by products of a highest weight vector and a monomial of degree $B - j_+$ in $r$ variables. Insert this and the level part condition into the sum over the window. Open condition 3 is the Theorem (Box bound), and condition 4 is assumed. $\square$

**Theorem 7.6.9 (Closed form from four conditions).** Under the hypothesis of the previous proposition, the closed form of Theorem A holds for large constants: for all $C_\kappa, C_s$ there is $C > 0$ such that every admitted instance $X$ satisfying the window hypotheses has mean bad share at most $C (t + 1) N_1 / Y$ at depth $C Y^2 N_1^2 (r + 1)^2 \lambda + 2 \kappa_0$.

Lean: `Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_open_directions`.

*Proof.* The previous proposition gives the open conditions, and the reduction of [Theorem 5.18](/entry/theorem-a-closed-form-holds/) turns them into the closed form. $\square$

**Remark 7.6.10 (Formalization).** The size conditions `RestTMSize`, the mean value instances `XMof` and their exponents `epsM`, the classes `clSet`, the compatibility `Compat` and the coordinate change `upd` were not unfolded beyond their statements. In `restTM_exists` ([RestTMExists.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/RestTMExists.lean#L14)) and in `restTM_closed` ([EpsilonBoundMConstant.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/EpsilonBoundMConstant.lean#L228)) the datum $D$ is a bound variable `_D` that only reaches the mean value theorem. The arithmetic in `epsilon_bound_M_constant` (same file, line 33) proves the bound $(15 + C_M)/Y$ and then weakens it to $(30 + C_M)/Y$. The hypothesis `RestOpen4E` of `openE_of_open4` asks for every $C_M \geq 1$, but the proof uses only the one value from `restTM_closed` ([ThresholdsMonoNormalized.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/ThresholdsMonoNormalized.lean#L40)). The reduction from the open conditions to the closed form is `closed_of_open_conditions`; it adds three more proved bounds and calls `theorem_A_closed_of_all_remaining_bounds`, which we did not follow.
