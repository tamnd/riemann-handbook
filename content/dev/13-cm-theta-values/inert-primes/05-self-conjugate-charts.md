---
title: Self-conjugate charts
decls:
  - Formalism.L2.FormalSeriesBounds.funEqCore_holds
  - Formalism.L2.FormalSeriesBounds.rank_maximal_self_unconditional
  - Formalism.L2.FormalSeriesBounds.ptSelf_of_start2
  - Formalism.L2.FormalSeriesBounds.ptSelf_of_eig
  - Formalism.L2.FormalSeriesBounds.ptSelf_holds
  - Formalism.L2.FormalSeriesBounds.UpFBr.upCharS_chartL
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Self-conjugate charts

At an inert prime the embeddings of the CM field come in pairs that complex conjugation exchanges, so the local charts of the row data are *self-conjugate*. This section proves four facts about such charts over a complete field of residue characteristic $l$: a congruence for the coboundary of a Frobenius series, the rank maximal condition, the existence of typical curves through a given point, and an upper bound for the characters of a chart that comes from an integral chart. Section 6 uses all four to build the row data at an inert prime, in [the theorem on geometric label sets](/entry/label-set-geo-of-even-of-rank-ok-of-not-dvd-discr/) and in [the theorem on the characteristic condition](/entry/label-set-ev-of-geo-of-not-dvd-discr/).

### Charts

Let $l$ be an odd prime. Let $C$ be an algebraically closed field of characteristic $0$ with an additive valuation $v$ such that $v(l) = 1$, and assume that every sequence $(s_n)$ with $v(s_{n+1} - s_n) \ge n$ has a limit $x$ with $v(x - s_n) \ge n$. Write $\mathfrak{m}$ for the set of $x \in C$ with $v(x) > 0$, and call $x$ *integral* if $v(x) \ge 0$. A series is integral if all its coefficients are integral.

A *chart* $Y$ of dimension $n$ over $C$, with coefficients in a ring $O$ with an involution $x \mapsto x^*$, consists of the following data:
- a formal group law $F$ of dimension $n$ with an action of $O$, two cubical series $\varphi_1, \varphi_2$ in three points, a symmetric series and adjoint series, all with the cocycle laws of a biextension, and all integral;
- a series $h$ in two points that is a canonical gauge for these data;
- a logarithm $\lambda$ with linear term $X$ and $\lambda(X +_F Y) = \lambda(X) + \lambda(Y)$, and an exponential that is inverse to $\lambda$;
- an element $w_0 \in O$ with $w_0 + w_0^* = 1$, and an integer $k$ with $v(k) = 0$.

For $u \in C^n$ put
$$u_1(X, Y) = \exp\bigl(h([l]_F X, Y) - l\,h(X, Y)\bigr),$$
and let $a(u)(Y) = \sum_i u_i^{\,l}\,c_i(Y)$, where $c_i(Y)$ is the coefficient of $X_i^{\,l}$ in $u_1(X, Y)$. For a series $b$ in one point, the *coboundary* is $\partial b(X, Y) = b(X +_F Y) - b(X) - b(Y)$. The *linear term* of $Y$ at $u$ is the series $\ell_u(X, Y) = \sum_i u_i\,\partial_{Z_i}\varphi_2(Z, X, Y)\big|_{Z = 0}$. For a series $c$, its *Frobenius twist* $c^{(l)}$ has coefficient $c_\nu^{\,l}$ at $l\nu$ and $0$ at the exponents that are not divisible by $l$. Finally, $Y$ has *first vanishing* at $u$ if for every $k$, the sum $\sum_i u_i^{\,l}$ times the coefficient of $X_i^{\,l}$ in the $k$-th coordinate of $[l]_F X$ lies in $\mathfrak{m}$.

**Theorem 6.5.1 (Coboundary congruence).** Let $Y$ be a chart over $C$, and let $u \in C^n$ be integral. If $Y$ has first vanishing at $u$, then every coefficient of
$$\partial\, a(u) - \ell_u^{(l)}$$
lies in $\mathfrak{m}$.

Lean: `Formalism.L2.FormalSeriesBounds.funEqCore_holds`

*Proof.* For a point $W$ in two variables with no constant term, and a lift $W'$ of $W$ to three variables that does not depend on the first variable, the coefficients of $a(u)$ at $W$ are the values $\Phi(u, U(W'))$, where $U(W')$ is the series $u_1$ with $W'$ in its second slot and $\Phi(u, f)$ at an exponent $\mu$ of the last two variables is $\sum_i u_i^{\,l}$ times the coefficient of $Z_i^{\,l}\cdot(\text{monomial }\mu)$ in $f$, with $Z$ the first variable. Apply this to the sum point $S$, which lifts $X +_F Y$, and to the two coordinate points $p_1$ and $p_2$. Then the coefficient of $\partial\,a(u) - \ell_u^{(l)}$ at $\mu$ is
$$\begin{aligned}
&\bigl(\Phi(U(S)) - \Phi(U(p_1)) - \Phi(U(p_2)) - \Phi(\varphi_2^{\,l}) + \Phi(Q)\bigr)\\
&\quad + \bigl(\Phi(\varphi_2^{\,l}) - (\ell_u^{(l)})_\mu\bigr) - \Phi(Q),
\end{aligned}$$
where $Q$ is a fixed correction series of the chart and all $\Phi$ are taken at $u$ and $\mu$. The series $U(S)$, $U(p_1)$ and $U(p_2)$ are integral, have the Frobenius property and restrict to $1$. A congruence for products of such series modulo $\mathfrak{m}$ shows that the first bracket lies in $\mathfrak{m}$. A second congruence, which needs only that $u$ is integral, puts the second bracket in $\mathfrak{m}$. A third congruence, which needs first vanishing at $u$, puts $\Phi(Q)$ in $\mathfrak{m}$. $\square$

### The rank maximal condition

A *curve* is an $n$-tuple $\gamma$ of power series in one variable with no constant term and integral coefficients. The chart $Y$ is *nondegenerate modulo $\mathfrak{m}$* if for every curve $\gamma$ with a degree-one coefficient outside $\mathfrak{m}$ such that $F(\gamma(X_0), \gamma(X_1)) \equiv \gamma(X_0 + X_1)$ modulo $\mathfrak{m}$ in the degrees below $l$ in each variable, there is no integral $b$ with $\ell_{\gamma'(0)} \equiv \partial b$ modulo $\mathfrak{m}$. In words, the linear term is not a coboundary modulo $\mathfrak{m}$. For charts that come from an integral chart this holds by [the nondegeneracy of the biextension](/entry/biextension-nondegenerate-mod-maximal-ideal-integral-chart/).

**Definition 6.5.2 (Self-conjugate data).** Self-conjugate data $P$ on $Y$ with $d$ types and index set $I$ consist of:
- ring maps $e_a : O \to C$ for $a \in \mathbb{Z}/d$ with integral values, $e_{a+1}(x) \equiv e_a(x)^l$ modulo $\mathfrak{m}$, any two of them different modulo $\mathfrak{m}$ at some $x$, and an element $\varepsilon \in O$ that is idempotent modulo $l$, is $1$ modulo $\mathfrak{m}$ under every $e_a$, and kills modulo $l$ every $x$ with all $e_a(x) \in \mathfrak{m}$;
- a shift $h_d \ne 0$ with $2h_d = 0$ and $e_a(x^*) = e_{a+h_d}(x)$;
- integral eigenvectors $e_c \in C^n$ for $c \in I$, of type $t(c)$, such that $x \in O$ acts on $e_c$ by $e_{t(c)}(x)$; the family has an integral left inverse, and every eigenvector of type $a$ is a combination of the $e_c$ of type $a$;
- matrices $g_a \in M_2(C)$ that are $l$-adic limits of $e_a$ applied to matrices over $O$, with $\sum_r g_{a+h_d}(r, s)\,g_a(r, s') = 0$ if $s = s'$ and $1$ otherwise.

The data $P$ give a raw chart $Y_P$ with two index sets equal to $I$. For $g \in \{0, 1\}$, the *typical curves* of $Y_P$ are sequences $x_0, x_1, \ldots$ of coordinate vectors that come from curves along the logarithm and the sigma series. The *Cartier hypotheses* at $g$ say that the typical curves contain $0$ and are closed under sums, negatives, Teichmüller multiples, the shift $V$, the Frobenius $F$ and convergent sums, and that the first nonzero term of a typical curve is integral. The *rank maximal condition* at a family of Cartier hypotheses says: if the alternation condition holds and $(g, a)$ is big, then for every curve $(w, x)$ that is good at $a$ and whose leading coordinates all lie in $\mathfrak{m}$, every $w_c$ lies in $\mathfrak{m}$.

**Theorem 6.5.3 (Rank maximal condition for self-conjugate charts).** Let $Y$ be a chart, nondegenerate modulo $\mathfrak{m}$, and let $P$ be self-conjugate data on $Y$ such that $Y_P$ satisfies the rank hypothesis. Then for every family of Cartier hypotheses on $Y_P$, the rank maximal condition holds.

Lean: `Formalism.L2.FormalSeriesBounds.rank_maximal_self_unconditional`

*Proof.* A general reduction proves the condition from five inputs: first vanishing for curves with linear logarithm, [the coboundary congruence](/entry/fun-eq-core-holds/), a congruence for the linear term along a curve, a law for the adjoint linear term, and the eigenvector decomposition below. All five are theorems. In the reduction, the eigenvector decomposition gives a projection onto the Lie algebra, which shows that no linear term survives; then a curve with some $w_c$ outside $\mathfrak{m}$ gives a contradiction with nondegeneracy. $\square$

### Typical curves through a point

**Definition 6.5.4 (Eigenvector decomposition).** Key data over $C$ consist of a ring $O$, a representation $\rho : O \to M_n(C)$ with integral entries, ring maps $e_a$ and an element $\varepsilon$ as in the self-conjugate data, and a matrix $P$ that is the limit of $\rho(\varepsilon^{\,l^N})$ as $N \to \infty$. The *eigenvector decomposition* says: for all such key data and every $v \in C^n$, there are vectors $w_1, \ldots, w_m$ and ring maps $\chi_1, \ldots, \chi_m : O \to C$ with
$$Pv = \sum_j w_j,\qquad P w_j = w_j,\qquad \rho(x)\,w_j = \chi_j(x)\,w_j .$$

The statement on *typical curves through a point* says: for all self-conjugate data, every $g$ and $a$, and every integral $w \in C^I$ with $w_c = 0$ when $t(c) \ne a$, there is a typical curve $x$ at $g$ with $x_0 = (w, 0)$ and $x_i(c) = 0$ for every index $c$ whose type is not $a + i$. The statement on *start points* says: for every $g$ and every integral $w$, there is a sequence $L$ in a fixed set of good sequences with $L_1 = w$ on the first index set.

**Proposition 6.5.5 (Typical curves from start points).** If the statement on start points holds, then the statement on typical curves through a point holds.

Lean: `Formalism.L2.FormalSeriesBounds.ptSelf_of_start2`

*Proof.* The general reduction from start points to typical curves needs two more inputs: the action of $O$ on the self-conjugate charts, and the stability condition. The stability condition says that the pairing of $e_c$ with $e_q$ by the sigma series is integral when $c$ and $q$ have different types. Both are theorems. $\square$

**Proposition 6.5.6 (Typical curves from eigenvectors).** If the eigenvector decomposition holds, then the statement on typical curves through a point holds.

Lean: `Formalism.L2.FormalSeriesBounds.ptSelf_of_eig`

*Proof.* The eigenvector decomposition gives the statement on start points. Then apply [the last proposition](/entry/pt-self-of-start2/). $\square$

**Theorem 6.5.7 (Typical curves through a point).** For all self-conjugate data, the statement on typical curves through a point holds.

Lean: `Formalism.L2.FormalSeriesBounds.ptSelf_holds`

*Proof.* The eigenvector decomposition is a theorem. Apply [the last proposition](/entry/pt-self-of-eig/). $\square$

### Characters of a base change

Let $E$ be a CM field and $T$ a complete discrete valuation ring. Let $Y$ be the base change of an integral chart over the fraction field of $T$ along an embedding $\iota$ into $C$ that respects the valuations: $v(\iota x) = v_T(x)/v_T(l)$ for $x \ne 0$. A *label set* for $Y$ assigns to each orbit $o$ and each $a \in \mathbb{Z}/d$ an embedding $\tau_{o,a} : E \to \mathbb{C}$, a shift $h_d$ and matrices $g_{o,a}$. It is *arithmetic* if the maps $(o, a) \mapsto \tau_{o,a}$ are injective and the induced maps on $O_E$ have the properties of the self-conjugate data, and *geometric* if the vectors of the integral chart give the eigenvectors. An arithmetic and geometric label set gives self-conjugate data $P_o$ for each orbit.

**Theorem 6.5.8 (Upper bound for characters).** Assume the upper bound law for formal groups over $T$ at $l$, that $\iota$ respects the valuations, and that $l$ does not divide the discriminant of $O_E$. Let $Y$ be a base change as above, and let the label set be arithmetic and geometric with the rank condition. Then for every orbit $o$ and every family of Cartier hypotheses on $Y_{P_o}$ there are characters $\chi_{g,i}$ of $Y$ such that, for every big $(g, a)$, there is a bijection $e$ from an index set onto the eigenvectors of type $a$ with these properties:
- if the alternation condition holds, the length of the cokernel of the matrix of values of $\chi_{g,i}$ at $e(c)$ is at most an explicit bound $B(l, n + j, j', \gamma_l)$;
- if every $(g, b)$ is big, the same length is at most $B(l, n + j, j', 0)$.

Lean: `Formalism.L2.FormalSeriesBounds.UpFBr.upCharS_chartL`

*Proof.* This is the general upper bound for characters at a chart that comes from an integral chart, applied with the place doubling criterion, which is a theorem. $\square$

**Remark 6.5.9 (Formalization).** Three of these results are one-line wrappers: `rank_maximal_self_unconditional` applies `rank_maximal_self_of_eigen` to five proved inputs, `ptSelf_of_start2` passes `OActSelf.oActSelf_holds` and `hStabSelf_holds` ([RowTiePPTClose.lean](lean:Formalism/LocalToGlobal/CharacterGerms/RowTiePPTClose.lean#L15)), and `ptSelf_of_eig` composes with `allStartSelf_of_eig` ([RowTiePPTEig.lean](lean:Formalism/LocalToGlobal/CharacterGerms/RowTiePPTEig.lean#L17)). The theorem `ptSelf_holds` is `ptSelf_of_eig RowTiePKey.keyEig_holds`. The word "unconditional" in the name of the rank maximal theorem means that the five inputs are proved, not that the statement has no hypotheses. The text does not unfold `RankHyp`, the alternation condition `AltC`, the predicate `Good` and the leading coordinates `c0'` in `RankMaximalCondition`, the set `AllSet` of the start statement, all fields of `KeyData`, the correction series `QQ`, the bound `upB`, or the upper bound law `UpFLaw`. The membership in $\mathfrak{m}$ is `VF.MM`. The theorem on characters is stated in namespace `UpFBr`, while the other five results are in `Formalism.L2.FormalSeriesBounds`.
