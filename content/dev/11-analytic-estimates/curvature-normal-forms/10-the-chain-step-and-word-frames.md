---
title: The chain step and word frames
decls:
  - Formalism.FourierDecayAlt.P.Qx6.stp_chainStepFromRules
  - Formalism.FourierDecayAlt.P.chain_descent_from_rules
  - Formalism.FourierDecayAlt.P.qx_chainStepBoth
  - Formalism.FourierDecayAlt.P.chain_descent_relation
  - Formalism.FourierDecayAlt.P.plus_letter_maps_frames
  - Formalism.FourierDecayAlt.P.minus_letter_maps_frames
status: drafted
drafted_by: writer@claude-opus-5-5
---

## The chain step and word frames

The actual operators exist at every level $i = 0, 1, \dots, r$ of a place. This section relates two adjacent levels. The chain step says that the operators of level $l$, restricted to a slice through a Weyl element, are the operators of level $l + 1$ conjugated by an explicit $2 \times 2$ matrix in the torus coordinate $c_l$. This is how the Yangian structure passes down the levels, and it gives the RTT relation at every level from the one at the top. The second half of the section is algebraic. A word of letters gives a product of $R$-matrices, and the letters act on frame data. We prove that one plus letter or one minus letter maps a frame to a frame. Both results are used in the step [HypsAlt is nonempty](/step/nonempty-hyps/).

### The restriction to a slice

Fix a parameter $P$ with rank $r$, a level $l < r$, and points $z, z'$ of the middle block. For $l$ let $\bar l = n - 1 - l$ be the paired index. For $c \in \mathbb C^\times$ let $w_1(c)$ be the matrix with
$$w_1(c) e_l = c\, e_{\bar l}, \qquad w_1(c) e_{\bar l} = \bar c^{-1} e_l,$$
and $w_1(c) e_a = e_a$ for the other basis vectors. It is a Weyl element twisted by the torus coordinate $c$. Let $G_{l+1}$ be the subgroup of $U(H)$ that fixes $e_a$ and $e_{\bar a}$ for $a \le l$.

Let $D$ be a domain at level $l$, and let $\mathcal F_l(D)$ be the smooth functions $J$ on $D$ that are left and right equivariant under the unipotent groups with the characters $\psi$ and under $\pi, \pi'$. For $J \in \mathcal F_l(D)$, $c = (c_0, \dots, c_{r-1}) \in (\mathbb C^\times)^r$ and $g \in G_{l+1}$ with $w_1(c_l) g \in D$, the *restriction* is
$$\operatorname{res}_l J(c, g) = |c_l|^{m_l - 1}\, J\bigl(w_1(c_l)\, g\bigr), \qquad m_l = 2(r - l) + k + 1.$$
On the restriction the torus coordinate $c_l$ acts by the Wirtinger operators $p_l = c_l \partial_{c_l}$ and $\bar p_l = \bar c_l \partial_{\bar c_l}$. Put
$$T_l(Y) = \begin{pmatrix} Y + p_l & -c_l \\ c_l^{-1} & 0 \end{pmatrix}, \qquad T^*_l(Y) = \begin{pmatrix} Y - \bar p_l & \bar c_l^{-1} \\ -\bar c_l & 0 \end{pmatrix}.$$
These are matrices of operators in the variable $c_l$. The matrix $T_l$ has the form of the [model matrix](/entry/q-qrtt/) of a single site, and $T^*_l$ is its star.

### The chain step

The proof of the chain step uses ten rules for the actual operators. They are: two identities that expand bordered minors along the border (one for each side), the full border expansion, the commutation relations of the generators $E_{ab}$ of $\mathfrak{gl}$ at a level, the preservation of the levels by these generators, the left invariance of the quantum minors, the rules for right and left translation by $w_1(c)$, the rule for the torus action, and the facts about the Weyl element $w_1(c)$ at a level.

**Theorem 1.10.1 (Chain step from the rules).** Assume the ten rules above. Then for every place, every level $l < r$, every domain $D$ at level $l$, every $J \in \mathcal F_l(D)$, all $c$ and $g \in G_{l+1}$ with $w_1(c_l) g \in D$, all $Y$ and all $a, b \in \{1, 2\}$:

1. each $\operatorname{res}_l(t^{(l)}_{ab}(Y) J)(c, g)$ is given by an explicit sum of left Capelli elements of level $l + 1$ applied to $\operatorname{res}_l J$;
2. the chain relation holds:
$$\operatorname{res}_l\bigl(t^{(l)}_{ab}(Y) J\bigr)(c, g) = \bigl(T^*_l(Y)\, Q^{(l+1)}(Y)\, T_l(Y)\bigr)_{ab}\, \operatorname{res}_l J(c, g).$$

Here $Q^{(l+1)}(Y)$ is the matrix of actual operators $t^{(l+1)}_{ab}(Y)$ of level $l + 1$, acting on the variable $g$, and the product on the right is a product of matrices of operators.

Lean: `Formalism.FourierDecayAlt.P.Qx6.stp_chainStepFromRules` (also `Formalism.FourierDecayAlt.P.chain_descent_from_rules`, a second name).

*Proof.* Each entry $t^{(l)}_{ab}(Y)$ is a bordered quantum minor of size $m_l$. Translating by $w_1(c_l)$ on the left moves the border vector $e_l$ to $c_l e_{\bar l}$. Expand the bordered minor along the row and the column of index $l$ and $\bar l$, using the border expansions. The minor that remains has size $m_{l+1} = m_l - 2$ and lives at level $l + 1$, by the preservation of levels. The terms of the expansion carry factors $c_l$, $c_l^{-1}$, $\bar c_l$, $\bar c_l^{-1}$, and one derivative in the direction of the torus. The torus rule turns this derivative into $p_l$ or $\bar p_l$ on the restriction. The first claim is the result of this expansion, written with left Capelli elements. Grouping the terms by the entries of $Q^{(l+1)}$ gives the matrix product in the second claim: the right factor $T_l(Y)$ comes from the column expansion and the left factor $T^*_l(Y)$ from the row expansion. $\square$

**Theorem 1.10.2 (Chain step).** For every place, every level $l < r$, and all data as above, the chain relation holds.

Lean: `Formalism.FourierDecayAlt.P.chain_descent_relation` (also `Formalism.FourierDecayAlt.P.qx_chainStepBoth`, which also gives claim 1).

*Proof.* This is the [chain step from the rules](/entry/stp-chain-step-from-rules/) applied to the ten rules, which are proved for the actual operators. $\square$

The chain relation is an RTT step. The matrix $T_l$ satisfies the RTT relation in the variable $c_l$, the matrix $Q^{(l+1)}$ satisfies it in the variable $g$, and the two act on different variables, so their product satisfies it. Iterating from the top level $r$ down gives the RTT relation at every level.

### Word frames

We now turn to the algebra of words. Fix a star ring $\mathcal A$ that is a $\mathbb C$-algebra, a level datum $L$ in $\mathcal A$ with coordinate $\zeta$, function $G$ and its inverse, and a finite set $S$ of sites. For a $2 \times 2$ matrix $m$ over $\mathcal A$ and a site $a$, let $\iota_a(m)$ be the element of the tensor algebra over the sites that puts $m$ in the factor $a$.

**Definition 1.10.3 (Frame data).** *Frame data* $f$ over $S$ consist of a set $\mathrm{reg} \subseteq \mathbb C$ of regular points and a smaller set $\mathrm{inv}$; a form $R$; a matrix $T(Y)$ for $Y \in \mathbb C$; a scalar function $q(Y)$; a length $N$; mutually inverse elements $F$ and $F^{-1}$; families $x(Y)$, $x(Y)^{-1}$; elements $c$, $c^{-1}$; and a family $e(Y)$. The data form a *frame* for $L$ if:

1. $(R, T, q)$ is a module on $\mathrm{reg}$: $R$ is hermitian, $d_0(R)\, T(Y)$ is hermitian for real $Y$, $T$ satisfies the RTT relation, $T$ has quantum determinant $q$, and $q$ is real on the real line;
2. the entries $T_{21}(Y)$, $T_{21}(Y')$ commute for $Y, Y' \in \mathrm{reg}$, and $\mathrm{inv} \subseteq \mathrm{reg}$;
3. $F F^{-1} = F^{-1} F = 1$, $x(Y) x(Y)^{-1} = x(Y)^{-1} x(Y) = 1$ on $\mathrm{inv}$, and $c c^{-1} = c^{-1} c = 1$;
4. the $x(Y)$ commute with each other, with $c$, with the function operators of $L$ and with $\nabla$; $c$ commutes with the function operators; $x(Y)$ is hermitian for real $Y$, and $c$ is hermitian; each $e(Y)$ commutes with the function operators;
5. $R = F^* d_L F$, where $d_L$ is the diagonal form of the level;
6. $F\, T_{22}(Y) = G\, x(Y)\, F$ on $\mathrm{reg}$, and $F\, T_{21}(Y) = G\, x(Y)\, l(Y)\, F$ when $Y, Y + 1 \in \mathrm{inv}$.

Items 5 and 6 say that $F$ is a gauge in which the form is diagonal and the lower row of $T$ has the shape of the [normal form](/entry/curv/).

**Definition 1.10.4 (Plus and minus letters).** Let $a \in S$ be a site and $Y_a \in \mathbb C$. The *plus step* $f^+ = f.\mathrm{plus}(a, Y_a)$ has
$$\begin{aligned} R^+ &= R\, \iota_a(T(Y_a)), & T^+(Y) &= T(Y)\, R_a(Y - Y_a),\\ q^+(Y) &= q(Y)\, \frac{Y - Y_a + 1}{Y - Y_a}, & F^+ &= \iota_a\bigl(\operatorname{diag}(\zeta^{-1}, \bar\zeta^{-1})\, \Lambda_a\bigr) F, \end{aligned}$$
with $\Lambda_a = \begin{pmatrix} 1 & 0 \\ G\, l(Y_a) & G \end{pmatrix}$, and with $x$, $c$, $e$ changed by explicit factors at the site $a$. The regular set loses the point $Y_a + 1$, and the invertible set loses $Y_a$ and $Y_a + 1$. The *minus step* $f.\mathrm{minus}(b, Y_b)$ is defined in the same way with the transpose: $R^- = R\, \iota_b(T(Y_b))^T$, $T^-(Y) = R'_b(Y_b - Y)\, T(Y)$, $q^-(Y) = q(Y) (Y_b - Y)/(Y_b - Y - 1)$, and $\zeta$, $\bar\zeta$ exchanged in $F$.

Here $R_a$ and $R'_b$ are the one site $R$-matrices of the Yangian at the sites $a$ and $b$. A site $a$ is *free* for $f$ if none of the elements of $f$ involves the factor $a$.

**Theorem 1.10.5 (A plus letter maps frames to frames).** Let $L$ be a star level and $f$ a frame for $L$. Let $a$ be a free site, let $Y_a$ be real, let $Y_a, Y_a + 1 \in \mathrm{inv}$, and let $q(Y_a) \ne 0$. Then $f.\mathrm{plus}(a, Y_a)$ is a frame for $L$.

Lean: `Formalism.FourierDecayAlt.P.plus_letter_maps_frames`

*Proof.* We check the items of the definition for $f^+$. For item 1, the RTT relation for $T(Y) R_a(Y - Y_a)$ follows from the RTT relation for $T$, the Yang-Baxter equation for $R_a$, and the fact that $T$ does not involve the free site $a$. The quantum determinant of $R_a(Y - Y_a)$ is the factor $(Y - Y_a + 1)/(Y - Y_a)$, so the quantum determinant of $T^+$ is $q^+$. The form $R^+$ is hermitian and $d_0(R^+) T^+(Y)$ is hermitian for real $Y$, because $T(Y_a)$ is hermitian at the real point $Y_a$ and the inserted factor at $a$ is the value of $T$ there. Items 2 to 4 are entry computations at the site $a$ that use $Y_a, Y_a + 1 \in \mathrm{inv}$. For items 5 and 6, the new gauge $F^+$ differs from $F$ by the factor at $a$, and the product $\operatorname{diag}(\zeta^{-1}, \bar\zeta^{-1}) \Lambda_a$ is chosen so that $F^{+*} d_L F^+ = R^+$ and the lower row of $T^+$ again has normal form; here $q(Y_a) \ne 0$ makes $c^+$ invertible. $\square$

**Theorem 1.10.6 (A minus letter maps frames to frames).** Let $L$ be a star level and $f$ a frame for $L$. Let $b$ be a free site, let $Y_b$ be real, let $Y_b - 1, Y_b, Y_b + 1 \in \mathrm{inv}$, and let $q(Y_b - 1) \ne 0$. Then $f.\mathrm{minus}(b, Y_b)$ is a frame for $L$.

Lean: `Formalism.FourierDecayAlt.P.minus_letter_maps_frames`

*Proof.* The argument is that of the [plus letter](/entry/plus-letter-maps-frames/), with $T(Y_b)^T$ in place of $T(Y_a)$ and the $R$-matrix on the left. The transpose moves the pole of the quantum determinant from $Y_a$ to $Y_b - 1$, which is why the hypotheses ask for $Y_b - 1 \in \mathrm{inv}$ and $q(Y_b - 1) \ne 0$. $\square$

By induction on a word, an admissible word of letters maps the start frame to a frame. This gives the frames of words that are used for the [dual kernel inequality](/entry/dk-radial/).

**Remark 1.10.7 (Formalization).** The chain step from the rules is stated as one implication with ten rules as premises, and its conclusion is a pair; the chain step is the second component, and the first component (the explicit Capelli form) is a separate name. Each letter theorem is proved by a lemma that takes nine facts (four compatibility facts for inserting a matrix at a position, the module facts for the letter, the RTT relation in entries, the form, and the two gauge identities) and these are proved separately. We did not unfold the $R$-matrices of a single site or the change of $x$, $c$ and $e$ under a letter; the statements above give them only in the form needed.
