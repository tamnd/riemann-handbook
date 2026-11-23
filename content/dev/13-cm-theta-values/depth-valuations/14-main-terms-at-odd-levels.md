---
title: Main terms at odd levels
decls:
  - GlobalTheory.MainTerm.both
  - GlobalTheory.MainTerm.main
  - GlobalTheory.T.rowData_mainTerm_normalForm_and_levelOne
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Main terms at odd levels

This section proves that the series of a row datum between a big type $a$ and the type $a + i$, for odd $i$, has a normal form: after a change of integral bases it is a fixed monomial main term $\ell^{-E} \sum_{b, c} \Phi_{bc} X_c^{\ell^i} X'_b$ plus a remainder with good weights, and the matrix $\Phi$ starts with $-1$ on a diagonal of length $n_0$, where $n_0$ is at least $n$ minus a small multiple of $j + j'$. The normal form is the first input of the [odd block supply](/entry/cm-theta-values/depth-valuations/#the-odd-block-supply), which feeds the [depth bound at good places](/entry/cm-theta-values/depth-valuations/#depth-bounds-at-good-places). The second input, a valuation bound for the model jets of the normal form, is the [next section](/entry/cm-theta-values/depth-valuations/#binomial-values-and-window-bounds).

### Row data

Let $C$ be an algebraically closed field of characteristic $0$ with an additive valuation $v$ into $\mathbb{R} \cup \{\infty\}$ and an odd prime $\ell$ with $v(\ell) = 1$. An element $x$ is *integral* if $v(x) \geq 0$ and lies in the *maximal ideal* if $v(x) > 0$. A family $u_1, \dots, u_N$ of vectors in $C^\sigma$ is *independent modulo the maximal ideal* if every integral combination $\sum_\nu c_\nu u_\nu$ whose entries all lie in the maximal ideal has all $c_\nu$ in the maximal ideal. It is *saturated* if its entries are integral and it has an integral right inverse $w$, that is $\sum_x u_c(x) w_x(c') = \delta_{cc'}$.

A *row datum* $X$ with modulus $d$, as used in the [packages of row data](/entry/cm-theta-values/depth-valuations/#row-data-and-packages-at-good-primes), has the following parts. For each side $g \in \{0, 1\}$ there is a chart $G_g$ with two finite sets of letters $I_g$ and $J_g$, each letter carrying a type in $\mathbb{Z}/d$. There are integers $n, j, j'$, and we put $m = j + j'$. There is a predicate $\mathrm{big}(g, a)$ with $\mathrm{big}(1 - g, a)$ exactly when $\mathrm{big}(g, a)$ fails, such that $I_g$ has $n + j$ letters of type $a$ when $(g, a)$ is big and $j'$ letters otherwise. There are integral pairings $\pi_g : J_g \times I_{1-g} \to C$ that vanish between letters of different types and have integral right inverses. There are series $h(g, a, a')$ in one variable for each letter of $I_0 \sqcup I_1$. Finally there are axioms on these data, which we use through the lemmas below and did not unfold. The datum is *alternating* if $d$ is even and $(0, a)$ is big exactly when the representative of $a$ in $[0, d)$ is even. Then for odd $i$ the pair $(g, a + i)$ is not big when $(g, a)$ is big, and $(1 - g, a + i)$ is big.

A *system* $S$ on the chart $G_g$ is a unimodular tangent matrix $\mathrm{tan}$ on $I_g$ and, for each letter $c$, curve coefficients $\alpha_c(s, x)$ for $x \in I_g$ and $\beta_c(s, \kappa)$ for $\kappa \in J_g$, indexed by $s \geq 0$. Series $t_c$ without constant term are *standard coordinates* for $S$ if $\sum_{s} \sum_c \alpha_c(s, x)\, t_c^{\ell^s}$ is the variable $x$, coefficient by coefficient. For $\kappa \in J_g$ put $\zeta_\kappa = -\sum_{s \geq 1} \sum_c \beta_c(s, \kappa)\, t_c^{\ell^s}$.

### The normal form

Fix an odd $i$ and put
$$E = 1 + \ell \sum_{0 \leq t < (i-1)/2} \ell^{2t} = 1 + \frac{\ell^i - \ell}{\ell^2 - 1}, \quad \rho = \frac{1}{\ell^2 - 1}, \quad r_1 = \rho + \frac{1}{2\ell^i}, \quad r_2 = \rho + \frac12, \quad \delta = \frac{1}{8 \ell^i}.$$
A series $H$ in left variables $X_c$ and right variables $X'_b$ has *weight at least $w$* if $w \leq v(H_\mu) + |\mu|_L (r_1 - \delta) + |\mu|_R (r_2 - \delta)$ for every monomial $\mu$, where $H_\mu$ is the coefficient and $|\mu|_L, |\mu|_R$ are the degrees in the left and right variables. For a series in left variables only we use the same condition with $|\mu|_R = 0$.

Let $(g, a)$ be big. For vectors $e_1, \dots, e_{n_0}$ on $I_g$ and $v'_1, \dots, v'_n$ on $I_{1-g}$, let $h_M(e, v')$ be the series $h(g, a, a + i)$ with the variable of each letter $x$ of side $g$ replaced by $\sum_c e_c(x) X_c$ and the variable of each letter $k$ of side $1 - g$ replaced by $\sum_b v'_b(k) X'_b$. For an $n \times n_0$ matrix $\Phi$ let
$$M(\Phi) = \ell^{-E} \sum_{b, c} \Phi_{bc}\, X_c^{\ell^i} X'_b.$$

**Definition 4.14.1 (normal form).** Let $U$ be $n$ vectors on $I_g$ and $U'$ be $n$ vectors on $I_{1-g}$. Data $n_0, e, v', \Phi$ are a *normal form* for $(U, U')$ at $(g, a, i)$ if

1. $n \leq n_0 + (i + 1) j' + j$ and $n_0 \leq n$;
2. $e$ is saturated, and $e = A U$ for an integral $n_0 \times n$ matrix $A$;
3. $v' = Y U'$ for an integral $n \times n$ matrix $Y$ with $v(\det Y) = 0$;
4. $\Phi$ is integral and $\Phi_{bc} = -\delta_{bc}$ for $b < n_0$;
5. $h_M(e, v') - M(\Phi)$ has weight at least $1/(\ell - 1)$;
6. the coefficients of $h_M(e, v') - M(\Phi)$ on monomials without right variables vanish.

The data satisfy the *curve clause* if there are a system $S$ on $G_g$ with standard coordinates $t$, distinct letters $c_1, \dots, c_{n_0}$ of $I_g$ and an integral matrix $\Phi^t$ on $n_0 \times J_g$, such that $\mathrm{tan}(c_\nu) = e_\nu$, $\alpha_{c_\nu}(1, \cdot) = 0$, $\Phi_{b\nu} = \sum_{\kappa, k} \Phi^t_{\nu\kappa}\, \pi_g(\kappa, k)\, v'_b(k)$, and for each $\kappa$ of type $a + i$ the series $\zeta_\kappa(\sum_\nu e_\nu X_\nu) - \ell^{-E} \sum_\nu \Phi^t_{\nu\kappa} X_\nu^{\ell^i}$ has weight at least $0$. They satisfy the *level one clause* if $i = 1$ and the coefficients of $h_M(e, v') - M(\Phi)$ of left degree below $\ell^2$ and right degree below $\ell$ are integral.

**Theorem 4.14.2 (main term at an odd level).** Let $X$ be an alternating row datum with $\ell \geq 5$, let $(g, a)$ be big and let $i < d$ be odd. Let $U$ be saturated vectors on $I_g$ supported on letters of type $a$, and $U'$ saturated vectors on $I_{1-g}$ supported on letters of type $a + i$, $n$ of each. Then $(U, U')$ has a normal form at $(g, a, i)$ that satisfies the curve clause, and also the level one clause if $i = 1$.

Lean: `GlobalTheory.MainTerm.both`.

*Proof.* Put $K = (i + 1)/2$ and $s_0 = (i - 1)/2$, so $s_0 < K$ and $s_0 + K + 1 = i + 1$.

Step 1 (adapted chain data). The row datum gives a system $S$ on $G_g$, an integer $N_1$ and a chain datum: a level $\mathrm{lev}(c) \geq 0$ for each letter, numbers $\alpha^D_c(k, b)$ with $\alpha_c(k, x) = \sum_b \alpha^D_c(k, b)\, \alpha_b(0, x)$ for $k \geq 1$, and distinct letters $\iota_1, \dots, \iota_{N_1}$ of level $0$. Letters of level $s < K$ have type $a + 2s$. Also $n \leq N_1 + (K + 1) j'$, and $\alpha_{\iota_\nu}(0, \cdot) = \sum_b A_{\nu b} U_b$ with $A$ integral.

Step 2 (chain ranks). Let $M_0$ be the identity and $M_{s+1}(e, c_0) = \sum_{\mathrm{lev}(c) = s} \ell\, \alpha^D_c(2, e)\, M_s(c, c_0)^{\ell^2}$. By induction on $s \leq s_0$ there is a subfamily of at least $N_1 - s j'$ of the $\iota_\nu$ whose columns $M_s(\cdot, \iota_\nu)$, cut to letters of level $s$, are independent modulo the maximal ideal. The step from $s$ to $s + 1$ is a rank-nullity count for the semilinear map that raises coordinates to the power $\ell^2$: its kernel modulo the maximal ideal has rank at most $j'$.

Step 3 (main vectors). For a letter $c_0$ put $\psi_{c_0}(\kappa) = (-1)^{s_0 + 1} \sum_{\mathrm{lev}(c) = s_0} M_{s_0}(c, c_0)^\ell\, \ell\, \beta_c(1, \kappa)$. A lemma on the last step of the chain turns the independence at level $s_0$ into independence of the $\psi$, so at least $N_1 - s_0 j'$ main vectors $\psi_\nu$ are independent modulo the maximal ideal.

Step 4 (pairing with $U'$). Let $\Psi_{\nu b} = \sum_{\kappa, k} \psi_\nu(\kappa)\, \pi_g(\kappa, k)\, U'_b(k)$, which is integral. The main vectors are supported on letters of type $a + i$, and $(g, a + i)$ is not big. The pairing lemma for a non-big type says that the kernel of $\Psi$ modulo the maximal ideal has rank at most $j$. Rank-nullity then gives $n_0 \geq N_1 - s_0 j' - j$ rows of $\Psi$ that are independent modulo the maximal ideal. With Step 1,
$$n \leq N_1 + (K + 1) j' \leq n_0 + j + (s_0 + K + 1) j' = n_0 + (i + 1) j' + j.$$

Step 5 (unimodular completion). The transpose $\Psi^T$ of the selected rows is an integral $n \times n_0$ matrix whose columns are independent modulo the maximal ideal. For such a matrix $n_0 \leq n$, and there is an integral $Y$ with $v(\det Y) = 0$ such that $Y \Psi^T$ has $-\delta_{bc}$ in its first $n_0$ rows. Put $v' = Y U'$, let $c_1, \dots, c_{n_0}$ be the chosen letters $\iota_\nu$, $e_\nu = \mathrm{tan}(c_\nu)$, and $\Phi_{b\nu} = \sum_{\kappa, k} \psi_\nu(\kappa)\, \pi_g(\kappa, k)\, v'_b(k)$. This gives clauses 1, 3 and 4, and $\Phi^t = \psi$ gives the formula for $\Phi$ in the curve clause.

Step 6 (the series). The rows of a unimodular tangent matrix are saturated, and the curve coefficient $\alpha_{c}(0, \cdot)$ is the tangent vector $\mathrm{tan}(c)$, so $e = A' U$ with $A'$ the selected rows of $A$ from Step 1; this is clause 2. On side $1 - g$ we take any system with identity tangent matrix, and standard coordinates on both sides. For letters of level $0$ the chain datum gives $\alpha_{c_\nu}(1, \cdot) = 0$, and a lemma on $\zeta$ along leaves gives the weight bound of the curve clause with $\Phi^t = \psi$. A weight lemma for the gauge series combines this with the weights of the coordinates $t_{c_\nu}$ and gives clause 5. The coefficients of $h_M - M(\Phi)$ on the first axis vanish by a separate lemma, which is clause 6.

Step 7 (level one). If $i = 1$ then $s_0 = 0$ and the main vectors are the first level vectors $-\ell \beta_{c}(1, \cdot)$. The lemma on low bidegrees then gives the integrality of the level one clause. $\square$

**Corollary 4.14.3 (the main term lemmas).** For every row datum $X$, the following two statements hold.

1. If $X$ is alternating and $\ell \geq 5$, then for every big $(g, a)$, odd $i < d$ and saturated $U, U'$ of types $a$ and $a + i$, the pair $(U, U')$ has a normal form at $(g, a, i)$ with the curve clause.
2. If $X$ is alternating, $\ell \geq 5$ and $1 < d$, then for every big $(g, a)$ and saturated $U, U'$ of types $a$ and $a + 1$, the pair has a normal form at $(g, a, 1)$ with the curve clause and the level one clause.

Lean: `GlobalTheory.MainTerm.main` (also `GlobalTheory.T.rowData_mainTerm_normalForm_and_levelOne`, a second name).

*Proof.* The first statement is the theorem without the level one clause. For the second, apply the theorem with $i = 1$, which is odd and less than $d$ because $1 < d$. $\square$

The count of Step 4 is the source of the condition $n - n_0 \leq (i + 1) m$ used in the next sections: it follows from clause 1 since $(i + 1) j' + j \leq (i + 1)(j + j')$.

**Remark 4.14.4 (Formalization).** The theorem is in [RowDataMainTermNormalFormAndLevelOne.lean](lean:Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/RowDataMainTermNormalFormAndLevelOne.lean#L98), the corollary at line 196 of the same file, and the second name in [RowDataMainTermNormalFormAndLevelOneStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/RowDataMainTermNormalFormAndLevelOneStatement.lean#L6). The normal form and the two clauses are in [LatticeInclusionFormsInjective.lean](lean:Formalism/LocalToGlobal/CharacterGerms/LatticeInclusionFormsInjective.lean#L90), with the two lemmas at lines 123 and 144. The only user of the corollary, the theorem on minors of the odd block supply, takes the first statement ([OddLevelBlockBoundAttained.lean](lean:Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/OddLevelBlockBoundAttained.lean#L99)); the second statement has no user, and the hypothesis $1 < d$ serves only to make $i = 1$ admissible. The system on side $1 - g$ is an arbitrary one with identity tangent matrix ([RowDataMainTermNormalFormAndLevelOne.lean](lean:Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/RowDataMainTermNormalFormAndLevelOne.lean#L153)). The definitions file also has a variant `LemmaMLeaf` of the first lemma, at line 130, that nothing uses. We did not unfold the axioms of a row datum, the curve condition of a system, or the proofs of the lemmas cited in Steps 1 to 7.
