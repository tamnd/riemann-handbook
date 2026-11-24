---
title: Theorem A and the mean value theorem
decls:
  - Formalism.MainNotions.G.GramWindowAlt.theorem_A_closed_form_holds
  - Formalism.MainNotions.G.CountingStatementReduction.alternative_mean_value_theorem
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Theorem A and the mean value theorem

This section closes two statements of the chapter on path polynomials. The first is the closed form of Theorem A, an averaged bound on the bad shares of block lattices. That chapter reduced it, in [the Theorem (Closed form from the window condition)](/entry/closed-of-minimal-vector/), to two facts on lattices over $\mathbb{Z}_p$ and one window condition. We prove the window condition here, so the closed form holds at every datum; it is one of the two main inputs of [the first theorem with constants](/entry/first-theorem-with-constants/) of Section 16. The second statement is the alternative mean value theorem, the mean bad count over a grid of tie coordinates, which the [box bound](/entry/rest-tm-exists/) of the chapter on path polynomials uses. It is the mean bad count of the chapter on character sums, read for the instances of the box bound.

### The window condition

We use the notation of the chapter on path polynomials: an instance $X$ with its prime $p$, rank $r$, length $s$, size $a$, parameter $Y$, window $A$ and constants; the classes $\delta$ of kept blocks, their boxes $\operatorname{box}(\delta)$ and index sets $I(\delta, a_{\mathrm{top}})$; for an index $(b, \ell)$, the level lattice $\Lambda_\ell$ with its tie pairing $\beta^{\Phi}_\ell$ and its pairings $\beta^{a_+}_\ell$ for $a_+ \in A$; the reduced depth $D_1 = D_1(C_M)$; and the bad count $\operatorname{bad}(\beta, L, D)$ of a lattice $L$ for a pairing $\beta$ at depth $D$. *Large constants* are as in that chapter: a statement holds for large constants if it holds whenever the constants pass thresholds chosen in the order $C_c$, then $C_0$, then $C_{E1}, C_{E2}$, then the remaining five.

**Definition 5.11.1 (Window condition).** Let $X$ be an instance and $C_M \geq 1$. The *window condition* holds for $X$ and $C_M$ if, at each class $\delta$, each $a_{\mathrm{top}} \in \operatorname{box}(\delta)$ and each $(b, \ell) \in I(\delta, a_{\mathrm{top}})$, every family $e_1, \dots, e_{n_1} \in \Lambda_\ell$ that is linearly independent over $\mathbb{Z}_p$, with $\beta^{\Phi}_\ell(e_a, e_c) = 0$ for $a \neq c$, $\beta^{\Phi}_\ell(e_a, e_a) \neq 0$ and $v_p(\beta^{\Phi}_\ell(e_a, e_a)) \leq \lfloor D_1\rfloor$, satisfies
$$\sum_{a_+ \in A}\operatorname{bad}\Big(\beta^{a_+}_\ell, \sum_a\mathbb{Z}_pe_a, \lfloor YD_1\rfloor\Big) \leq |A|\cdot\frac{5}{Y}\,n_1.$$

The pairings $\beta^{a_+}_\ell$ differ from one another by a shift of one tie coordinate of the block. So the left side is a sum over consecutive shifts, and the condition says that an orthogonal family that is good for the tie pairing stays good, at the deeper depth $\lfloor YD_1\rfloor$, for all but a share $5/Y$ of the shifts.

**Proposition 5.11.2 (Window condition).** For large constants, with the thresholds $1$, $1$ and $2$, the following holds: for all $C_\kappa, C_s$, all $C_M \geq 1$ and every admitted instance $X$ that satisfies the window hypotheses, the window condition holds for $X$ and $C_M$.

Lean: `Formalism.MainNotions.G.GramWindowAlt.restWinE_proved`.

*Proof.* Fix the constants above the thresholds, $C_M \geq 1$ and $X$. The window hypotheses give the segment facts of the instance, and in particular $k^2Y^2 \leq p$ and $a \in A$. Fix $\delta$, $a_{\mathrm{top}}$, $(b, \ell)$ and an orthogonal family $e_1, \dots, e_{n_1}$ as in the definition.

The main step is a level window lemma for one block. Let $J = \min(d_u - j_+, B - j_+)$ be the length of the level, where $d_u$ is the degree of the last row. All letter degrees, the size $B$ and the tie sizes are at most $2a$. For $z$ in a run of $W$ consecutive shifts, with $W \leq p^h$ and $J + 1 \leq p^h$, the lemma gives
$$\sum_{z}\operatorname{bad}\Big(\beta^{(z)}_\ell, \sum_a\mathbb{Z}_pe_a, k\Big) \leq W n_1\Big(\frac{J}{W} + \frac{x_0 + D + \lambda + Jh/W}{k + 1}\Big)$$
for every $k \geq 0$, where $D$ bounds the valuations $v_p(\beta^{\Phi}_\ell(e_a, e_a))$, $\lambda$ is the logarithmic size and $x_0$ is an explicit multiple of $\lambda$. Its proof writes the pairing at shift $z$ as a polynomial of degree at most $J$ in $z$. After multiplication by $p^{x_0}$ and division by a product of factorials, the coefficients are integral; this uses the bound $m/(p - 1) - v_p(m!) \leq \lambda$ for $m \leq 2a$, which follows from Legendre's formula $v_p(m!) = (m - s_p(m))/(p - 1)$, with $s_p(m)$ the sum of the $p$-adic digits of $m$. A Gram window lemma then bounds the number of shifts at which the family fails to be good.

Apply the lemma with $W = |A|$, the run of shifts $a_+ - o_+$ for $a_+ \in A$, and $k = \lfloor YD_1\rfloor$. A numerical lemma, which uses the segment facts and $k^2Y^2 \leq p$, gives $h$ with $|A| \leq p^h$ and $J + 1 \leq p^h$, and shows that the bracket is at most $5/Y$. So the sum over $A$ is at most $|A|\cdot n_1\cdot 5/Y$. $\square$

**Theorem 5.11.3 (Closed form of Theorem A).** For every datum, the closed form of Theorem A holds for large constants: for all $C_\kappa, C_s$ there is $C > 0$ such that every admitted instance $X$ satisfying the window hypotheses has mean bad share at most $C(t + 1)N_1/Y$ at depth $CY^2N_1^2(r + 1)^2\lambda + 2\kappa_0$.

Lean: `Formalism.MainNotions.G.GramWindowAlt.theorem_A_closed_form_holds`.

*Proof.* [The Theorem (Closed form from the window condition)](/entry/closed-of-minimal-vector/) gives the closed form from three inputs. The first is the minimal vector theorem for lattices over $\mathbb{Z}_p$ with $p \neq 2$, and the second is the diagonal count lemma; both are proved in the chapter on path polynomials. The third is the window condition for large constants, which is the Proposition (Window condition). $\square$

### The mean value theorem on a grid

We use the notation of the chapter on character sums. Let $L$ be letters of length $2s + 1$ and $T$ tie data with $t$ ties, at positions $\mathrm{pos}_i$ and with thresholds $J$. For $n \in \mathbb{N}^t$ let $L_n$ be $L$ with its ties set to $n$, let $Y(L_n)$ be the highest weight space over $\mathbb{Q}_p$ and $Y_{\mathbb{Z}}(L_n)$ its integral lattice, with the Fock pairing composed with the tie operators $\Phi$. For each $i < t$ take numbers $Y_i \geq 1$, $n_{0,i}$ and $\delta_i > 0$, and put
$$G = \prod_{i < t}\{n_{0,i} + \delta_ij : 0 \leq j < Y_i\}, \qquad n^{\mathrm{top}}_i = n_{0,i} + \delta_i(Y_i - 1).$$
Let $S_i$ be the size of the truncation of $L_{n^{\mathrm{top}}}$ at the tie $i$. With $\lambda = \log_p(8a + r) + 1$ put
$$\kappa = 3(s + 2)r^2\lambda, \qquad \varepsilon_i = \frac{2S_i}{Y_i} + \frac{2\kappa + 2S_i\lambda/Y_i}{E}, \qquad D_1 = t(E + \kappa) + \kappa.$$

**Definition 5.11.4 (Mean value instance).** A *mean value instance* is a tuple $(p, s, r, L, T, a, E, Y, n_0, \delta, \rho)$ as above, with $p$ prime, $r \neq 0$ and $\rho < r$. It satisfies the *hypotheses of the mean value theorem* if:

1. $p \neq 2$, $r \geq 2$ and $\rho = r - 1$;
2. $T$ is admissible for $L$, the letter at $j$ is a vector exactly when $j$ is even, and each threshold $J_k$ is $2s + 1$ or some $\mathrm{pos}_i + 1$;
3. $a \geq 1$ and $E \geq 1$; for each $i$, $Y_i \geq 1$, $\delta_i > 0$ is prime to $p$, and $S_i \leq n_{0,i}$;
4. $|L_{n^{\mathrm{top}}}| \leq 8a + r$, and for each $i$ the numbers $d_{\mathrm{pos}_i} + d_{\mathrm{pos}_i + 1} + r + z_i + 1$, $Y_i$ and $2S_i + 1$ are at most $8a + r$, all for $L_{n^{\mathrm{top}}}$.

**Theorem 5.11.5 (Alternative mean value theorem).** For every datum and every mean value instance that satisfies the hypotheses of the mean value theorem,
$$\frac{1}{|G|}\sum_{n \in G}\operatorname{bad}\big(Y_{\mathbb{Z}}(L_n), \lfloor D_1\rfloor\big) \leq \sum_{i < t}\varepsilon_i\cdot\frac{1}{|G|}\sum_{n \in G}\dim Y\big(L_{n[i \mapsto n^{\mathrm{top}}_i]}\big),$$
where the bad count is taken for the Fock pairing with the tie operators applied to its first argument.

Lean: `Formalism.MainNotions.G.CountingStatementReduction.alternative_mean_value_theorem`.

*Proof.* This is [the Theorem (Mean bad count on a progression grid)](/entry/top-theorem-mv7/) applied to the data of the instance; its eleven hypotheses are the conditions 1 to 4. That theorem is [the mean bad count with explicit constants](/entry/mc-theorem-mv7/) without the three hypotheses at the points of $G$, which hold with the exponents $\lfloor r^2\lambda\rfloor$ and $(s + 4)r^2\lambda$. $\square$

The bound is a mean: at one point of the grid the bad count can be as large as the rank. Each tie contributes the share $\varepsilon_i$ of the dimension at the top of its own coordinate. In the box bound, $Y_i$ is of size $Y$ and $E$ is large, so $\varepsilon_i$ is $O(S_i/Y)$.

**Remark 5.11.6 (Formalization).** The proposition `restWinE_proved` (FockGramWindow.lean:12) ignores the hypothesis that the instance is admitted (`AdmNoK`, the unnamed argument at line 15), so the window condition holds for every instance with the window hypotheses. The level window lemma is `winLvl` (FockGramWindow/WinLvl.lean:77), the numerical lemma is `restWinNum_proved` (FockGramWindow/InitialPointNumericBound.lean:183), and the Gram window lemma `gramWindow2_proved` and its use `win_abs` were not unfolded. `ModelLatticeRank` takes the datum as an unused argument `_D` (FlipOneThree.lean:416), so the mean value theorem does not depend on the datum. The name `ModelLatticeRank` says nothing about a mean value bound, and a second definition with this name is in ColumnSystems.lean:159.
