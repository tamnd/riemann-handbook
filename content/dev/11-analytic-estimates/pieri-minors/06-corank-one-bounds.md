---
title: Corank one bounds for pairs of terms
decls:
  - Formalism.MainNotions.BridgeLemma₂.small_term_of_corank_one_pair
  - Formalism.MainNotions.BridgeLemma₂.corank_one_bound_of_fibres
  - Formalism.MainNotions.BridgeLemma₂.corank_one_bound_general
  - Formalism.MainNotions.BridgeLemma₂.corank_one_bound_of_fibres_alt
  - Formalism.MainNotions.BridgeLemma₂.corank_one_bound_of_injective_terms
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Corank one bounds for pairs of terms

This section proves the row bound for pairs of terms of corank one. The terms carry a hermitian lattice and two flags, and the two terms of a pair are glued by a linear map $\beta$. A pair has corank one when the index $s_0$ of the gluing is $1$. For such a pair, Theorem B on gluing says that one of the two terms is small. A weighted count over the fibres of the reduced Gram matrices then bounds the sum of the weights of all pairs of corank one. The result is the estimate that [the theorem on the rows of corank one](/entry/rows-one-of/) of Volume 10 takes as its input.

**Definition 4.6.1 (Terms, pairs and row bounds).** We work in the setting of the row estimates of Volume 10. There is a number field $E$ with a hermitian space $V$, a rank $k$, integers $r_S, m, f$ with $m = 2r_S + 2$, two words $u, u'$ with integers $T_u, T_{u'}$ and real traces $\mathrm{Tr}_u, \mathrm{Tr}_{u'}$, and an integer $g$. There are finite sets of *terms* $t$ and of *pairs* $p$. A term $t$ has a Gram value $G(t)$, a lattice $\Lambda_t \subseteq V$, a flag $F_t$ of $T_u$ and a flag $F'_t$ of $T_{u'}$; it can be *generic* and *relevant*. A pair $p$ has a first term $p_1$ and a second term $p_2$ with $\Lambda_{p_1} = \Lambda_{p_2}$ and $F_{p_1} = F_{p_2}$, an $E$-linear automorphism $\beta_p$ of $V$, an index $s_0(p) \leq k$ and a *scalar* property. Each pair has a row weight $w_{\mathrm{row}}(p) > 0$, and each term has an amplitude $a(t) \geq 0$, the Hilbert-Schmidt norm of an operator $J_t$. Put
$$w(p) = w_{\mathrm{row}}(p)\, a(p_1)\, a(p_2).$$
Let $M \geq 0$ be the mass of the rows and $\dim \Pi_u > 0$ the dimension attached to $u$. For a property $Q$ of pairs and $B \in \mathbb{R}$, the *row bound* $\mathrm{RB}(Q, B)$ says: for every finite set $S$ of pairs with property $Q$,
$$\sum_{p \in S} w(p) \leq M \dim \Pi_u \cdot B.$$
A pair $p$ has *corank one* if $G(p_1) \neq 0$, $G(p_2) \neq 0$, both terms are generic, $s_0(p) = 1$ and $p$ is not scalar. A term $t$ is *small* if $D_r(F_t, F'_t) \neq 0$ and
$$\prod_\tau \min\bigl(\nu_\tau(t), \mathrm{Tr}_{u'}\bigr) \leq \Bigl(4 \sqrt{\mathrm{Tr}_{u'}/\mathrm{Tr}_u}\; g\Bigr)^{f},$$
where $\tau$ runs over the places of the setting and $\nu_\tau(t)$ is the local size of $t$ at $\tau$.

The weight $w(p)$ bounds the absolute value of the value attached to $p$ in the setting. A term with $G(t) \neq 0$ that is not relevant has amplitude $0$, so only pairs with two relevant terms count.

The proof of the main bound uses a counting lemma of Schur type.

**Lemma 4.6.2 (Weighted sums over fibres).** Let $S$ be a finite set, $w, a_1, a_2 : S \to \mathbb{R}$ with $w, a_2 \geq 0$, and $c_1, c_2 : S \to K$ maps to a set $K$. Let $M, R \geq 0$, $\Phi \in \mathbb{R}$, $N : K \times K \to \mathbb{R}$ and $\alpha_1, \alpha_2, \varphi : K \to \mathbb{R}_{\geq 0}$. Assume:

1. $a_1(p) \leq \alpha_1(c_1(p))$ and $a_2(p) \leq \alpha_2(c_2(p))$ for $p \in S$;
2. for $x \in c_1(S)$ and $y \in c_2(S)$, every $S' \subseteq S$ with $c_1 = x$ and $c_2 = y$ on $S'$ has $\sum_{p \in S'} w(p) \leq M\, N(x, y)$;
3. $N(x, y)\, \alpha_1(x)\, \alpha_2(y) \leq R\, \varphi(x)\, \varphi(y)$ for $x \in c_1(S)$ and $y \in c_2(S)$;
4. $\sum_{x \in Z} \varphi(x) \leq \Phi$ for every finite $Z \subseteq c_1(S)$ and every finite $Z \subseteq c_2(S)$.

Then $\sum_{p \in S} w(p)\, a_1(p)\, a_2(p) \leq M R \Phi^2$.

Lean: `Formalism.MainNotions.BridgeLemma₂.weighted_sum_le_of_fibre_counts`.

*Proof.* Split $S$ into the fibres $S_{x,y} = \{p : c_1(p) = x, c_2(p) = y\}$ for $x \in c_1(S)$, $y \in c_2(S)$. On $S_{x,y}$, item 1 gives $w(p) a_1(p) a_2(p) \leq w(p) \alpha_1(x) \alpha_2(y)$. Items 2 and 3 give
$$\sum_{p \in S_{x,y}} w(p) a_1(p) a_2(p) \leq M N(x, y) \alpha_1(x) \alpha_2(y) \leq M R \varphi(x) \varphi(y).$$
Sum over $x$ and $y$. The double sum of $\varphi(x)\varphi(y)$ is the product of $\sum_{x \in c_1(S)} \varphi(x)$ and $\sum_{y \in c_2(S)} \varphi(y)$, and item 4 bounds each factor by $\Phi$. $\square$

**Theorem 4.6.3 (Small term of a corank one pair).** Assume the counting hypotheses of the setting. If $p$ is a pair of corank one with $p_1$ and $p_2$ relevant, then $p_1$ is small or $p_2$ is small.

Lean: `Formalism.MainNotions.BridgeLemma₂.small_term_of_corank_one_pair`.

*Proof.* Put $\Lambda = \Lambda_{p_1}$ and $F = F_{p_1} = F_{p_2}$. Since $G(p_i) \neq 0$, both $(\Lambda, F, F'_{p_i})$ are terms, and they are generic. The counting hypotheses give the prime hypothesis for $(u, T_{u'})$. [Theorem B](/entry/theorem-b-section/) applies to $(\Lambda, F, F'_{p_1}, F'_{p_2}, \beta_p)$, because $s_0(p) = 1$. It gives one of two cases. In the first case the gluing is scalar; then $p$ is scalar, which is false for a pair of corank one. In the second case,
$$\Bigl(\frac{T_u T_{u'}}{g^2}\Bigr)^{f/2} \leq \prod_\tau \bigl(\chi_\tau(F, F'_{p_1})\, \iota_\tau(F, F'_{p_2}) + \iota_\tau(F, F'_{p_1})\, \chi_\tau(F, F'_{p_2})\bigr)$$
for local factors $\chi_\tau$ and $\iota_\tau$ of the flags. Since both terms are relevant with $G \neq 0$, a comparison of the local sizes of the two terms turns this inequality into the smallness of $p_1$ or of $p_2$. $\square$

**Theorem 4.6.4 (Corank one bound from fibre counts).** Assume the standing hypotheses on the constants $c, C_2, C_h, \delta, \delta_m, C_0, C_a, q$ of the row estimates, the switch bound, the bound on partner counts, the admissibility of order 7, and the two *single fibre bounds*: for every pair $p_0$, every Gram class $Z$ and every finite set $S$ of pairs $p$ with $G(p_1), G(p_2) \neq 0$, both terms generic, $s_0(p) = 1$ and $\Lambda_{p_1} = \Lambda_{(p_0)_1}$,

1. if $F'_{p_1}$ is equivalent to $F'_{(p_0)_1}$ and the Gram matrix of $p_2$ is in the class $Z$, then $|S|$ is at most the number of partners of $(\Lambda_{(p_0)_1}, F'_{(p_0)_1})$ with Gram class $Z$;
2. the same with the roles of $p_1$ and $p_2$ exchanged.

Assume also $\delta \leq 1/2$, $0 \leq \delta_m \leq 1/4$, $0 \leq C_a$, $\max(C_a, 1)^3 \leq k$ and
$$12 c r_S^2 + \tfrac{1}{2} C_2 m^2 + |C_2 m^4| + 12 (r_S + 1)^2 \leq \frac{q}{r_S + 1}.$$
Then $\mathrm{RB}(\text{corank one}, B_1)$ holds with $B_1 = 2\, C_{\mathrm{lab}}\, \Phi^2$, where $C_{\mathrm{lab}}$ is the label pair constant and $\Phi$ is the row constant of the setting.

Lean: `Formalism.MainNotions.BridgeLemma₂.corank_one_bound_of_fibres`.

*Proof.* By the remark after the definition, it is enough to treat sets $S$ of pairs of corank one whose two terms are relevant. Split $S$ into the pairs with $p_1$ small and the other pairs. By the previous theorem, $p_2$ is small for every pair of the second part.

For the first part, apply the lemma on weighted sums with the weights $w_{\mathrm{row}}$, $a_i(p) = a(p_i)/\sqrt{\dim \Pi_u}$, and the classes $c_i(p)$, the reduced Gram matrix of $p_i$. The reduced Gram matrices are good and equivalent to the Gram matrices of the terms. Item 1 of the lemma holds with the small term amplitude for $p_1$ and the row amplitude for $p_2$. Item 2 holds with $N(x, y)$, the two label count: the minimum of the switch bound of $x$ times the fourth moment bound of $(x, y)$ and the same expression with $x$ and $y$ exchanged. This step uses the two single fibre bounds. Item 3 holds with $R = C_{\mathrm{lab}}$ and $\varphi(Z) = \mathrm{size}(Z)^{-12(r_S + 1)^2}$; this step uses the condition on $q$. Item 4 holds with $\Phi$. Since $\sum_p w(p) = \dim \Pi_u \sum_p w_{\mathrm{row}}(p)\, a_1(p)\, a_2(p)$, the first part has weight at most $M \dim \Pi_u\, C_{\mathrm{lab}} \Phi^2$.

The second part is the same with the two amplitudes exchanged, and the two label count is symmetric in $(x, y)$. The sum of the two parts is at most $M \dim \Pi_u \cdot 2 C_{\mathrm{lab}} \Phi^2$. $\square$

**Theorem 4.6.5 (Corank one bound, general constant).** Assume the hypotheses of the previous theorem. Let $C$ satisfy $4\sqrt{A} \leq C$, $2\sqrt{2 C_0}\, c \leq C$ and $C_\Gamma + C_2 \leq C$, and the exponent condition
$$\begin{aligned} & 1 + 12 f (r_S + 1)^2 + e(c, C_h)\bigl(6 c r_S^2 + 6 (r_S + 1)^2\bigr) \\ & \leq C^2 m^5 f, \end{aligned}$$
where $e(c, C_h)$ is the exponent shift of the pair count. Then $\mathrm{RB}(\text{corank one}, B(C)\, r_{DD})$ holds, where $B(C)$ is the corank one constant of the setting and $r_{DD} = d_S(u')/D^*$.

Lean: `Formalism.MainNotions.BridgeLemma₂.corank_one_bound_general`.

*Proof.* A numerical lemma shows $2 C_{\mathrm{lab}} \Phi^2 \leq B(C)\, r_{DD}$ under the conditions on $C$, with $0 \leq \delta \leq 1$. A row bound stays true when $B$ grows, since $M \dim \Pi_u \geq 0$. Apply this to the previous theorem. $\square$

**Theorem 4.6.6 (Corank one bound, quadratic condition).** In the previous theorem, the exponent condition can be replaced by
$$4 + 2\bigl(c^2 + 2 \max(C_h - c, 0)\bigr)(c + 1) \leq C^2.$$

Lean: `Formalism.MainNotions.BridgeLemma₂.corank_one_bound_of_fibres_alt` (also `Formalism.MainNotions.BridgeLemma₂.corank_one_bound_of_fibres_ge_one`, the form with $1 \leq C_a$ and $C_a^3 \leq k$).

*Proof.* The exponent shift is $e(c, C_h) = c^2 m^3 f + 4\max(C_h - c, 0)\, m^2 f (r_S + 1)$. Put $P = c^2 + 2\max(C_h - c, 0)$. With $m = 2 r_S + 2$ we have $e(c, C_h) = m^3 f P$. Since $f \geq 1$, $c \geq 0$ and $r_S \geq 0$, the quadratic condition gives the exponent condition. Then apply the previous theorem. $\square$

**Definition 4.6.7 (Injective terms and the lattice of gluings).** The terms are *injective* if two terms $t, t'$ with $\Lambda_t = \Lambda_{t'}$ and equivalent flags $F'_t$ and $F'_{t'}$ are equal. The gluings satisfy the *lattice condition* if for every lattice $\Lambda$, every flag $F$ of $T_u$ with the fixed hypothesis, every two flags $F', F''$ of $T_{u'}$ such that $(\Lambda, F, F')$ and $(\Lambda, F, F'')$ are generic terms, and every two gluings $\beta_1, \beta_2$ of $(\Lambda, F, F', F'')$ with $s_0 = 1$:
$$\beta_2(x) - \beta_1(x) \in X(F'') \quad \text{for every } x \perp X(F'),$$
where $X(F')$ is the subspace of the flag $F'$.

**Theorem 4.6.8 (Corank one bound for injective terms).** Assume the hypotheses of the quadratic form, with the two single fibre bounds replaced by the injectivity of the terms and the lattice condition on the gluings. Then $\mathrm{RB}(\text{corank one}, B(C)\, r_{DD})$ holds.

Lean: `Formalism.MainNotions.BridgeLemma₂.corank_one_bound_of_injective_terms`.

*Proof.* First, a pair of corank one is fixed by its two terms. Let $p, q$ be pairs with $p_1 = q_1$, $p_2 = q_2$, $s_0 = 1$, generic terms and $G \neq 0$. The lattice condition, applied to $\beta_p$ and $\beta_q$, gives the condition on $\beta$ under which the setting identifies two pairs with the same lattice, so $p = q$. Second, the injectivity of the terms and this uniqueness of pairs give the first single fibre bound, and, with the symmetry of pairs, the second. Then apply the theorem with the quadratic condition. $\square$

**Remark 4.6.9 (Formalization).** The setting of Volume 10 enters through two records, `TermTie` and `LoopTie`, and through the record of standing hypotheses `rows_Hyps` with nineteen fields; none of these, the switch bound `stSW`, the partner count bound `PartnerCountBound` or the admissibility `adm7` was unfolded here. The constants $C_{\mathrm{lab}}$ (`labelPairConstant`), $\Phi$ (`rows_Phi`) and $B(C)$ (`oneB`) were opened, but the text does not write them out. The local sizes $\nu_\tau(t)$, the factors $\chi_\tau, \iota_\tau$ and the comparison lemma `rowsT_small` of the proof of the small term theorem were read only as statements, as were the amplitude bounds, the count `corank_one_pair_count`, the size bound and the numerical lemma `corankOneBound_le`. In the proof for injective terms, the step from the lattice condition to the uniqueness of pairs (`rows_BetaUnique_of`) and the two single fibre bounds (`rows_OneFibre_of`, `rows_OneFibre'_of'`) were read at the level of their statements. The name `corank_one_bound_of_fibres_alt` (RowsOneE.lean, line 158) suggests a second proof, but the theorem only replaces the exponent condition by the quadratic condition; `corank_one_bound_of_fibres_ge_one` (line 172) is one more wrapper with $1 \leq C_a$. The two halves of the main proof (RowsOneD.lean, lines 102 and 147) repeat the same argument with the roles of the two terms exchanged.

## Notes and references

The chapter feeds two parts of the proof. Sections 1 to 5 give the [inclusion of models](/entry/l-incl-of-models/): the integral inclusion of the forms with values in dual Weyl modules into the forms with values in Weyl lattices, with an explicit exponent at each large prime. Section 6 gives the input of [the theorem on the rows of corank one](/entry/rows-one-of/) in the row estimates of Volume 10, which bound sums over pairs of terms. Both enter the proof through [the unitary hypotheses](/proof/unitary-hypotheses/). The Pieri rule and the column minors of Sections 1 and 2 are the classical tools of the representation theory of $\mathrm{GL}_n$ over the integers. The lattices with a Frobenius matrix of Section 5 are lattices over power series rings of the kind studied by Wach and Berger.

- I. G. Macdonald, *Symmetric Functions and Hall Polynomials*, 2nd ed., Chapter I, §5.
- W. Fulton, *Young Tableaux*, London Math. Soc. Student Texts 35.
- J. C. Jantzen, *Representations of Algebraic Groups*, 2nd ed., Part II, Chapters 2 and 8.
- J. A. Green, *Polynomial Representations of GL_n*, Lecture Notes in Math. 830.
- A. Okounkov and A. Vershik, *A new approach to representation theory of symmetric groups*, Selecta Math. 2 (1996).
- N. Wach, *Représentations p-adiques potentiellement cristallines*, Bull. Soc. Math. France 124 (1996).
- L. Berger, *Limites de représentations cristallines*, Compositio Math. 140 (2004).
