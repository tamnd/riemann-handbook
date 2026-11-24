---
title: The twisted character index
decls:
  - Formalism.L2.Col.twIdx_ok_of
  - Formalism.L2.Col.twIdx_ok
  - Formalism.L2.Col.twIdx_ok'
  - Formalism.L2.Col.twIdx_ok''
  - Formalism.L2.Col.twIdx_ok_full
  - Formalism.L2.Col.twistedIndex_firstUnfolding_ok
  - Formalism.L2.Col.twIdx_ok_closed
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The twisted character index

This section builds a character index from the twisted constants of Section 2 and proves that it is good. A character index records, at each step $j$ of the column and each prime $P$, a finite set of states and an element of $\mathrm{GL}(V_j)$ for each state. The states at the primes outside the exceptional set are the double cosets of Section 1 on which the first unfolding sum does not vanish. The final result, [the closed form of the twisted index](/entry/tw-idx-ok-closed/), asks only for three facts on the field $K$ and the element $\xi_0$. It gives [the good character index](/entry/tw-idx-ok-of-ok/) of Volume 13, and through it [the existence of a good character index](/entry/exists-ch-idx-of-cst/).

### Character indices

We keep the column data of Section 2, with $m = m_2 + 2$. In addition, we fix a global datum: the embedding $\sigma_0 \colon K \to \mathbb{C}$, the element $\xi_0 \in E$, and for each $j < m$ a [Hecke character](/learn/class-field-theory/#hecke-characters) $\mu^0_j$ with values in $\mathbb{C}^\times$, whose local component at a prime $w$ is $\mu^0_{j,w}$. Let $Q$ be the set of primes attached to the row character in the column data.

**Definition 5.3.1 (Character index).** A *character index* for local constants $\mathcal{C}$ consists of, for each step $j \leq m_2 + 1$: a finite set $\beta_j$ of states; for each state $b \in \beta_j$ and each prime $P$ of the row, an element $h_j(b, P) \in \mathrm{GL}(V_j)$; and level groups at the primes of $V$ and of $Q$.

**Definition 5.3.2 (Good character index).** A character index is *good* for $\mathcal{C}$ and the global datum if the following groups of conditions hold.

1. (Constants.) $m = m_2 + 2$; the local constants are good; $\xi_0$ is a unit at the primes of the row; the additive characters of $\mathcal{C}$ are tied to $\sigma_0$ and $\xi_0$ as in condition 5 of Section 2; the multipliers satisfy $\mu^\flat_{i+1}(P) = \mu_i(P)^{-1}\bar q^{-1}$ off $V$ and $\sigma_0(\mu^\flat_{i+1}(P)) = \mu^0_{i,P}(q)^{-1}\, \sigma_0(\bar q^{-1})$ on $V$.
2. (Depth.) The depth is $1$ on $V$, and off $V$ the depth $D_P$ satisfies $2M \leq D_P$ and $2(m-1) + 1 \leq D_P$.
3. (Ends.) Step $0$ has one state, with element $1$, the column level group on $V$, and the whole group on $Q$; the last step has one state, with element $1$.
4. (Transitions.) The first unfolding sum from each state of step $j$ to each state of step $j + 1$ is not $0$ at large depth exactly as the states require; the map from states to double cosets is injective and surjective onto the double cosets with nonzero sum; and the level groups are stable.
5. (Analysis.) Support and invariance of the additive characters and of the residue characters on the relevant lattices, integrality of the elements $h_j(b, P)$, and the group and character conditions at $V$ and at $Q$.

The conditions in 4 and 5 are the input of the descent in Volume 13: there, a good character index gives a nonzero vector in each step of the column.

**Definition 5.3.3 (Normal form, character condition).** An element $h$ of $\mathrm{GL}(V_j)$, bounded at step $j$, is in *normal form* if the lattice $h\Lambda_j$ is given by integers $-j \leq n_i \leq 0$ and a vector $z \in \Lambda_j$ as follows: $v \in h\Lambda_j$ if and only if $v_l - v_N z_l$ is integral for all $l$ and $q^{-n_i} v_{N+i}$ is integral for all $i$. The *character condition* at $h$ asks that a function $\chi_h$ on the group $R_1 \cap hJh^{-1}$ have no zero, and that $\chi_h(r'') = \chi_h(r)\chi_h(r')$ whenever $r''$ acts on $E^{N_j}$ as $rr'$.

**Definition 5.3.4 (The five conditions).** For local constants $\mathcal{C}$ with sharp level groups, consider the following conditions, where $P$ ranges over the primes of the row outside $V$ that are of degree one and unramified, and $i < m_2$.

1. (Finiteness.) For each such $P$ and $j$, the set of double cosets $R_1 h J_j$ that contain a bounded element is finite.
2. (Normal representatives.) If $g_0$ is bounded and in normal form at step $i$, $h$ is bounded at step $i+1$, and $\mathcal{E}^{\mathrm{col}}(g_0, h)$ is nonzero at large depth, then there is $h'$ in the double coset of $h$ that is bounded, in normal form, whose projection of $R_1 \cap h'Jh'^{-1}$ to $\mathrm{GL}(E^{N_{i+1}})$ is integral at $P$, and with $\mathcal{E}^{\mathrm{col}}(g_0, h')$ nonzero at large depth.
3. (Characters.) (i) Under the hypotheses of 2, with $h$ itself in normal form and with integral projection, the character condition holds at $h$; (ii) the character condition holds at $h = 1$ at step $m_2 + 1$.
4. (Step zero.) $\mathrm{GL}_{N_0}(\mathcal{O}_{(P)})$ lies in the projection at step $0$ and $h = 1$, and the character $\chi_1$ is $1$ there.
5. (Analysis.) The conditions of group 5 above, for the twisted constants.

The construction of the index is as follows. On $V$ the states and elements are the fixed ones of the column. Off $V$, the states of step $i+1$ are the double cosets in the finite set of condition 1 that carry a representative in normal form with nonzero first unfolding sum, and $h_{i+1}(b, P)$ is a chosen representative.

### The theorems

**Theorem 5.3.5 (The twisted index is good).** Let local constants $\mathcal{C}$ satisfy the base conditions of the column and have sharp level groups. Assume that the global characters are tied to $\sigma_0$, that $\xi_0$ is a unit at the primes of the row, that the additive characters are tied to $\sigma_0$ and $\xi_0$, that the multipliers satisfy the two formulas of condition 1 of a good index, that $m \leq A$ and $1 \leq B$, that $2M \leq D_P$ and $2(m-1)+1 \leq D_P$ off $V$, that $Q \cap V = \emptyset$, and that every prime of the row off $V$ is of degree one and unramified. Assume conditions 1 to 5. Then the character index built from $\mathcal{C}$ is good.

Lean: `Formalism.L2.Col.twIdx_ok_of`.

*Proof.* Most conditions of a good index are hypotheses or base conditions. Condition 2 gives a normal representative at every step $i < m_2$. On $V$ the first unfolding sum with $B$ equals the sum with $B = 1$, since $A \geq m$ and the additive character there has depth $1$; so the transitions on $V$ come from the column. The closed level groups are given by their entries, and the group and character conditions on $V$ hold for the column. Off $V$, injectivity and surjectivity hold because the states are the double cosets of condition 1, and conditions 3 and 4 give the character conditions and step zero. $\square$

**Theorem 5.3.6 (The twisted constants give a good index).** Let the column data be good, with $q(w) \equiv 1 \bmod 4$ for every $w \in V$. Let the global characters be tied to $\sigma_0$ and the Weil condition hold for $\sigma_0$ and $\xi_0$. Assume that for each $j < m$ and $w \in V$ there is $y \in K$ with $\sigma_0(y) = \mu^0_{j,w}(\varpi_w)^{-1}$, where $\varpi_w$ is the norm of $w$ as an element of $E^\times$. Let $m = m_2 + 2$, $Q \cap V = \emptyset$, and let every prime of the row off $V$ be of degree one and unramified. If the twisted constants are good and satisfy conditions 1 to 5, then the character index of the twisted constants is good.

Lean: `Formalism.L2.Col.twIdx_ok`.

*Proof.* This is the previous theorem applied to the twisted constants. The base conditions hold for them, and their level groups are sharp. The element $\xi_0$ is a unit on $V$ by the Weil condition and off $V$ by condition 6 of good constants. Off $V$ the multiplier is $\mu_i(P)^{-1}\bar q^{-1}$ by definition, since $i + 1 \leq m$. On $V$ the formula for $\sigma_0(\mu^\flat_{i+1})$ follows from the existence of $y$. Finally $A = B = m + 1$ and $D_P = 2m$ off $V$, so $m \leq A$, $1 \leq B$, $2M = 2m \leq D_P$ and $2(m-1)+1 \leq 2m$. $\square$

**Corollary 5.3.7 (Without step zero).** Under the hypotheses of the previous theorem without condition 4, the character index of the twisted constants is good.

Lean: `Formalism.L2.Col.twIdx_ok'`.

*Proof.* Condition 4 holds for good twisted constants. Apply the previous theorem. $\square$

**Corollary 5.3.8 (Without finiteness).** Assume the hypotheses of the previous corollary without conditions 1 and the goodness of the constants, and assume instead that for each prime $P$ of the row off $V$: there is $z \in K$ with $\sigma_0(z) = e^{2\pi i/q^{2m}}$; there is $z \in K$ with $z^2 = \bar q$; and $\xi_0$ is integral at $P$ with nonzero reduction. Then the character index of the twisted constants is good.

Lean: `Formalism.L2.Col.twIdx_ok''`.

*Proof.* The three assumptions make the twisted constants good: $\zeta$ and $s_P$ exist, so $\psi_P$ is a character of $q^{-2m}\mathcal{O}_{(P)}/\mathcal{O}_{(P)}$ with $\sigma_0(\psi_P(a)) = e^{2\pi i b/q^{2m}}$. Condition 1 holds in general: the bounded double cosets are finite in number. Apply the previous corollary. $\square$

**Corollary 5.3.9 (Without the analysis).** Under the hypotheses of the previous corollary without condition 5, the character index of the twisted constants is good.

Lean: `Formalism.L2.Col.twIdx_ok_full`.

*Proof.* Condition 5 holds for good twisted constants when $m = m_2 + 2$ and the primes off $V$ are of degree one and unramified. Apply the previous corollary. $\square$

**Theorem 5.3.10 (The index from the first unfolding).** Under the hypotheses of the previous corollary without conditions 2 and 3, assume instead:

- (a) the conclusion of [the nonvanishing in a double coset](/entry/unfolding-nonvanishing-double-coset-holds/) for the twisted constants;
- (b) for $i < m_2$, $P$ off $V$ of degree one and unramified, $g_0$ bounded and in normal form at step $i$, $h$ bounded and in normal form at step $i + 1$ with integral projection, and $\mathcal{E}^{\mathrm{col}}(g_0, h)$ nonzero at large depth, the character condition holds at $h$.

Then the character index of the twisted constants is good.

Lean: `Formalism.L2.Col.twistedIndex_firstUnfolding_ok`.

*Proof.* Condition 2 follows from (a). Let $h$ be bounded with $\mathcal{E}^{\mathrm{col}}(g_0, h)$ nonzero at large depth. Every bounded $h$ has a representative $h'$ in its double coset that is bounded, in normal form, and has integral projection. By (a), $\mathcal{E}^{\mathrm{col}}(g_0, h')$ is nonzero at large depth. Condition 3 (i) is (b). For 3 (ii), at $h = 1$ the group $R_1 \cap J$ has integral entries, and $\psi_P = 1$ on integral elements by good constants, so $\chi_1 = 1$ there. Apply the previous corollary. $\square$

**Theorem 5.3.11 (The closed form of the twisted index).** Let the column data be good, with $q(w) \equiv 1 \bmod 4$ for $w \in V$. Let the global characters be tied to $\sigma_0$, and the Weil condition hold for $\sigma_0$ and $\xi_0$. Assume that for each $j < m$ and $w \in V$ there is $y \in K$ with $\sigma_0(y) = \mu^0_{j,w}(\varpi_w)^{-1}$. Let $m = m_2 + 2$, $Q \cap V = \emptyset$, and let every prime $P$ of the row off $V$ be of degree one and unramified. Assume that for each such $P$:

$$\begin{aligned} &\text{there is } z \in K \text{ with } \sigma_0(z) = e^{2\pi i/q^{2m}}, \\ &\text{there is } z \in K \text{ with } z^2 = \bar q, \\ &\xi_0 \text{ is integral at } P \text{ and } \xi_0 \not\equiv 0 \bmod P. \end{aligned}$$

Then the character index of the twisted constants is good.

Lean: `Formalism.L2.Col.twIdx_ok_closed`.

*Proof.* The three assumptions make the twisted constants good. Then (a) of the previous theorem is [the nonvanishing in a double coset](/entry/unfolding-nonvanishing-double-coset-holds/) of Section 2. The statement (b) holds for good twisted constants with $m = m_2 + 2$: the character on $R_1 \cap hJh^{-1}$ is a value of $\psi_P$ at the character argument, and it is multiplicative and has no zero there. Apply the previous theorem. $\square$

**Remark 5.3.12 (Formalization).** The first theorem asks that the level groups be sharp, but the base conditions already contain this. The proof of (b) in the closed form does not use the normal form hypotheses; they are passed as unused arguments. Several objects of the construction have fallbacks: the set of classes is empty when it is infinite, the representative and the character values are chosen with Hilbert's choice operator, and the value attached to a state is $1$ when the character condition fails. We did not unfold the character $\chi_h$, the proof of condition 5, the normal form representatives, or the tie conditions for the global characters and the Weil condition. See [ChainTwMain.lean](lean:Formalism/LocalToGlobal/Columns/ChainTwMain.lean#L61), [ChainTwAll.lean](lean:Formalism/LocalToGlobal/Columns/ChainTwAll.lean#L20) and [ChainTwAux.lean](lean:Formalism/LocalToGlobal/Columns/ChainTwAux.lean#L87).
