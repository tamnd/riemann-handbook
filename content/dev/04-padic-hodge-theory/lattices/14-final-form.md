---
title: The final form of Theorem E
decls:
  - Formalism.ExponentWindows.E.theorem_E_final_form
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The final form of Theorem E

The final form of Theorem E is the form that [Theorem E in lifting form](/entry/crystalline-lifting-second-form/) applies. Its hypotheses are the final conditions of the previous section on the base, the numbers and the lattices, the unit and class conditions of the primitive form, the $W'$-condition at the cuts, and final arc data at every cut, with the heights $H(c, s) = g + h_J(c - s)$ fixed by the kinds of the letters. This section proves it from [the primitive form](/entry/theorem-e-primitive-form/) and [the arc condition](/entry/prim-arc/) of the previous section. It then bounds the two numbers $\nu(J_c)$ and $\nu(J'_c)$ of the final numbers by an explicit expression in $\ell$, $\ell_{\max}$, $g$ and $t$.

We keep the notation of the two previous sections: $M$, $A$, $E$ from the parameters, the final conditions, the sets $J_c$ and $J'_c$ of a cut, and the numbers $\nu_E(J)$. For a pair of families $\kappa'$ for $V_2$ we write $h(\kappa_1)$ for the image of a pair $\kappa_1$ for $V_1$ under $h$, coordinate by coordinate.

**Theorem 8.14.1 (Final form of Theorem E).** Let $\mathcal{O}$ be a discrete valuation ring with uniformizer $\varpi$ and fraction field $L$, $B$ a Frobenius base, $e \in \mathbb{N}$, $\mathcal{C}$ a set of cuts for $n$, and let each letter have a kind and a size. Let $j, g, G_0, S, \eta, t, \sigma, r, \kappa, \ell_{\max} \in \mathbb{N}$ and $u, x \in \mathcal{O}^\times$. Let $h \colon V_1 \to V_2$ be a map of lattices, $e_0 \in V_0$, and $Z_1$, $Z_2$ additive groups of pairs for $V_1$, $V_2$. Assume:

1. the base is final for $\varpi$, $e$, $u$, $x$, and the numbers are final;
2. $V_1$ and $V_2$ are final lattices;
3. $e_0$ is a unit, and $Z_1$, $Z_2$ are primitive classes for the heights $H$, with $G_0$ in place of $G$;
4. $h$ satisfies the $W'$-condition with $r$;
5. at each cut $c$ there are final arc data for $H(c, \cdot)$, with $M$, $g$, $G_0$, $S$, $\eta$ and the kinds and sizes of the arc.

Then for every $\kappa' \in Z_2$ there is $\kappa_1 \in Z_1$ such that $\ell^E \kappa' - h(\kappa_1)$ is a coboundary of $V_2$, with
$$E = 2r + 4\sigma + 2A + 2\kappa, \qquad A = 2\sigma + r + 2 g\, \ell_{\max} .$$

Lean: `Formalism.ExponentWindows.E.theorem_E_final_form`

*Proof.* We apply the primitive form of Theorem E with the heights $H$ and with $G = G_0$, and check its hypotheses.

The base is primitive, since a final base is primitive by definition. The numbers are primitive: the final numbers give $G_0 \le g \le t$, $1 \le j$, $j \le \ell_c \le \ell_{\max}$ for each cut $c$, and the inequality of primitive numbers. A final lattice is a primitive lattice for $\mathcal{C}$, $j$, $G_0$ and $t$, so $V_1$ and $V_2$ are primitive. The unit and the classes are assumed in 3, with the same heights $H$.

It remains to give primitive arc data at each cut $c$, for $H(c, \cdot)$, $g$, $\sigma$, $r$, $A$ and $\kappa$. The final base, the final numbers, the final lattices $V_1$ and $V_2$, the $W'$-condition and the final arc data at $c$ are the hypotheses of the proposition of the previous section, and it gives these arc data. The primitive form now gives, for each $\kappa' \in Z_2$, an element $\kappa_1 \in Z_1$ such that $\ell^E \kappa' - h(\kappa_1)$ is a coboundary, with the exponent $E = 2r + 4\sigma + 2A + 2\kappa$ of the primitive form. $\square$

So the final form adds nothing to the primitive form at the level of the base, the lattices or the classes. Its content is the arc condition: the level models with filtrations replace the abstract level data, and the polynomials $P$ and $P'$ are the killing polynomials of $J_c$ and $J'_c$. The number $\kappa$ must bound $\nu_{\ell_c - 1}(J_c)$ and $\nu_{\ell_c - 1}(J'_c)$. We now give an explicit value of $\kappa$ that does this.

**Lemma 8.14.2 (Valuations in a window).** Let $\ell$ be a prime, $a \in \mathbb{Z}$, $L, D \in \mathbb{N}$, and let $S$ be a finite set of nonzero integers in $[a, a + L)$ with $|i| \le D$ for $i \in S$. Then
$$\sum_{i \in S} v_\ell(i) \le \frac{L}{\ell - 1} + \log_\ell D .$$

Lean: `Formalism.WindowSums.arc_WindowSum`

*Proof.* If $S$ is empty there is nothing to prove, so let $D \ge 1$. We have $\sum_{i \in S} v_\ell(i) = \sum_{k \ge 1} N_k$, with $N_k$ the number of $i \in S$ divisible by $\ell^k$. A nonzero multiple of $\ell^k$ has absolute value at least $\ell^k$, so $N_k = 0$ if $\ell^k > D$. An interval of $L$ integers contains at most $L/\ell^k + 1$ multiples of $\ell^k$. There are at most $\log_\ell D$ numbers $k \ge 1$ with $\ell^k \le D$. Hence
$$\sum_{k \ge 1} N_k \le \sum_{k \ge 1} \frac{L}{\ell^k} + \log_\ell D = \frac{L}{\ell - 1} + \log_\ell D . \qquad \square$$

**Lemma 8.14.3 (Window bound for $\nu$).** Let $\ell$ be a prime and $E, R \in \mathbb{N}$. Let $J$ be a finite set of integers with $|i| \le R$ for $i \in J$, contained in a union of $K$ intervals $[a_m, a_m + y_m)$. Then
$$\nu_E(J) \le E + \Bigl( E + 1 + \frac{1}{\ell - 1} \Bigr) \sum_{m} y_m + K \log_\ell R .$$

Lean: `Formalism.ExponentWindows.E.kappa_exponent_in_window`

*Proof.* Split $J \setminus \{0\}$ into the parts that lie in the intervals; each element is counted at least once. The number of nonzero elements of $J$ is at most $\sum_m y_m$, and by the last lemma, applied to each interval with $D = R$, $\sum_{i \in J, i \ne 0} v_\ell(i) \le \sum_m y_m / (\ell - 1) + K \log_\ell R$. So
$$\nu_E(J) = E + (1 + E)\, \bigl|J \setminus \{0\}\bigr| + \sum_{i \in J,\, i \ne 0} v_\ell(i)$$
is at most the stated bound. $\square$

**Proposition 8.14.4 (An explicit $\kappa$).** Let $\ell$ be a prime, and let $G_0, S, \eta \le g \le t$, $b_i + S \le t$ at each letter $i$ that is not thin, and $\ell_c \le \ell_{\max}$ for each cut $c$. Assume that the kinds and sizes of each arc form a text word for some $a_0$. If
$$\ell_{\max} - 1 + 7 g \Bigl( \ell_{\max} + \frac{1}{\ell - 1} \Bigr) + 3 \log_\ell (2t) \le \kappa ,$$
then $\nu_{\ell_c - 1}(J_c) \le \kappa$ and $\nu_{\ell_c - 1}(J'_c) \le \kappa$ for each cut $c$.

Lean: `Formalism.ExponentWindows.E.aux_statement_1`

*Proof.* Fix a cut $c$ and put $E = \ell_c - 1$. By the text word, all steps other than two steps $t_0$ and $t_1$ are thin. Since $E \le \ell_{\max} - 1$, the left side of the hypothesis is at least
$$E + 7 g \Bigl( E + 1 + \frac{1}{\ell - 1} \Bigr) + 3 \log_\ell (2t) .$$
By the window bound with $K = 3$ and $R = 2t$, it suffices to cover $J_c$ and $J'_c$ by three intervals of total length at most $7g$, and to show $|i| \le 2t$ on them.

For a step of kind $k$ and size $b$ let $a_2 = -g$, $-b - g$ or $b - g$, and $a_4 = -2g$, $-b - S - g$ or $b - g$, for $k$ thin, up or down. From the definitions, each set $W_2$ lies in $[-g, 0) \cup [a_2, a_2 + g)$, and since $G_0, S, \eta \le g$, each set $W_4$ lies in $[-2g, g) \cup [a_4, a_4 + 2g)$. At a thin step the second interval of $W_2$ equals the first, and the second interval of $W_4$ lies in the first. Hence
$$\begin{aligned} J_c &\subseteq [-g, 0) \cup [a_2(t_0), a_2(t_0) + g) \cup [a_2(t_1), a_2(t_1) + g), \\ J'_c &\subseteq [-2g, g) \cup [a_4(t_0), a_4(t_0) + 2g) \cup [a_4(t_1), a_4(t_1) + 2g), \end{aligned}$$
with total lengths $3g$ and $7g$. Every element of $W_2$ and $W_4$ has absolute value at most $b + S + g$ at a step that is not thin, and at most $2g$ at a thin step; both are at most $2t$, since $b + S \le t$ and $g \le t$. $\square$

**Example 8.14.5.** Let all steps of the arc at $c$ be thin and $E = \ell_c - 1$. Then $J_c = [-g, -1]$, and since $v_\ell(-i) = v_\ell(i)$,
$$\nu_E(J_c) = E + g\,(1 + E) + v_\ell(g!) .$$
By Legendre's formula $v_\ell(g!) \le g/(\ell - 1)$, which is the bound of the window lemma without the term in $\log_\ell$.

**Remark 8.14.6 (Formalization).** The statement is `ThmEFinal` ([FinalArcProps.lean](lean:Formalism/DistinguishedUnitIdeals/FinalArcProps.lean#L226)). Its proof ([ThmEFinal.lean](lean:Formalism/DistinguishedUnitIdeals/DistinguishedOrderProofs/ThmEFinal.lean#L513)) is a direct call of `theorem_E_primitive_form` with the heights `HArc` and with `primArc` at each cut. The explicit bound is `KapOfKAP` (FinalArcProps.lean line 85), with the expression `kapOf` (line 44); it is proved as `aux_statement_1` (ThmEFinal.lean line 509) through `kapExp_le`, `kap_mono`, `second_jump_set_in_windows` and `kappa_of_kappa_bound`. The final form does not use `KapOfKAP`: the final numbers `FinalNum` carry the bounds on $\nu$ directly as the field `kapOK`, so the explicit $\kappa$ is a separate statement that a user of the final form may apply. In `KapOfKAP` only the first part of the text word (at most two steps that are not thin) is used, and the number $a_0$ is free. The window bound is `KapExpWin` with `kapWin` (PhiFreeOfBasis.lean lines 46 to 51), and the window lemma is `WindowSum` (WindowSums/Statement.lean line 123). In the final form the unit $x$ and the field $L$ enter only through the final base.
