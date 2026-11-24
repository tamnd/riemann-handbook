---
title: The dual kernel inequality
decls:
  - Formalism.FourierDecayAlt.P.PBF.dk_partial
  - Formalism.FourierDecayAlt.P.PBF.dk_radial
status: drafted
drafted_by: writer@claude-opus-5-5
---

## The dual kernel inequality

A word $L w$ of plus letters on top of a word $w$ has a form $R_{Lw}$, and its dual word $L^\vee w$, in which each plus letter at $Y$ becomes a minus letter at $Y + 1$, has a form $R_{L^\vee w}$. When both forms are positive, the dual kernel inequality bounds a mixed pairing, built from the form $R_w$ of the shorter word, by the product of the two quadratic forms divided by a product of quantum determinants. The proof has two parts. The algebraic part is a duality between the word and its dual: a single matrix $\Psi$, made from the [quantum determinant](/entry/det-core/) of the [start](/entry/start-is-start/), carries $R_{Lw}$ to $R_{L^\vee w}$ up to a scalar. The analytic part is the Cauchy-Schwarz inequality for the positive form $R_{Lw}$, which [Theorem P](/entry/actual-compact-theorem/) supplies at level zero. The inequality on the radial space is used in the step [HypsAlt is nonempty](/step/nonempty-hyps/), where it bounds the mixed terms in the size estimate for the standard data.

### Pairings and adjoints

Let $V$ be a complex vector space and $\mathrm{Pr}(V) = \mathrm{End}(V) \times \mathrm{End}(V)^{\mathrm{op}}$ the pair algebra of Section 01, with star $(a_1, a_2)^* = (a_2, a_1)$. Let $U \subseteq V$ be a subspace and $\beta : V \times V \to \mathbb C$ a function.

**Definition 1.15.1 (Hermitian class).** The function $\beta$ is *of hermitian class on $U$* if for all $x, x', y \in U$ and $c \in \mathbb C$
$$\begin{aligned} \beta(y, x) &= \overline{\beta(x, y)}, \\ \beta(x + x', y) &= \beta(x, y) + \beta(x', y), \\ \beta(c x, y) &= c\, \beta(x, y). \end{aligned}$$

From the first identity, $\beta$ is additive and conjugate linear in the second variable on $U$.

**Definition 1.15.2 (Adjoint algebra).** For $\beta$ of hermitian class on $U$, the *adjoint algebra* $\mathcal A(U, \beta)$ is the set of $a = (a_1, a_2) \in \mathrm{Pr}(V)$ such that $a_1$ and $a_2$ map $U$ into $U$ and $\beta(a_1 x, y) = \beta(x, a_2 y)$ for all $x, y \in U$.

The set $\mathcal A(U, \beta)$ is a star subalgebra: products and sums are checked directly, and the star is closed because $\beta(a_2 x, y) = \overline{\beta(a_1 y, x)} = \beta(x, a_1 y)$. So an element of $\mathcal A(U, \beta)$ is an operator $a_1$ on $U$ together with its adjoint $a_2$.

Let $S$ be the finite set of sites, and let families $X : \{0, 1\}^S \to V$ be the vectors of the tensor space. A matrix $M$ over $\mathrm{Pr}(V)$ indexed by $\{0, 1\}^S$ acts by $(M X)_a = \sum_b (M_{ab})_1 X_b$, and the *tensor pairing* is
$$\langle X, X' \rangle_\beta = \sum_{z \in \{0,1\}^S} \beta(X_z, X'_z).$$
We write $M^*$ for the matrix with entries $(M^*)_{ab} = (M_{ba})^*$, and say $X$ lies in $U$ if every $X_z$ does.

Two facts about this pairing are used. First, if every entry of $M$ lies in $\mathcal A(U, \beta)$ and $X, Y$ lie in $U$, then $\langle X, M Y \rangle_\beta = \langle M^* X, Y \rangle_\beta$; this is the defining identity of the adjoint algebra summed over the entries. Second, if the entries of $M$ preserve $U$ and $\langle M X, X \rangle_\beta$ is real and nonnegative for every $X$ in $U$, then
$$|\langle M X, X' \rangle_\beta|^2 \le \langle M X, X \rangle_\beta\, \langle M X', X' \rangle_\beta.$$
This is the Cauchy-Schwarz inequality for the form $(X, X') \mapsto \langle M X, X' \rangle_\beta$, which is linear in $X$ and conjugate linear in $X'$. A form of this kind whose values on the diagonal are real is hermitian, by polarization, so nonnegativity on the diagonal is all that is needed.

### Words and their duals

Fix a start $(Q, q)$ over $\mathrm{Pr}(V)$ in the sense of Section 02: $Q(Y)$ is hermitian for real $Y$, satisfies the RTT relation, and has quantum determinant $q$, which is real on the real line. A letter $l$ is a sign, a site $a_l \in S$ and a point $Y_l$. As in the [word frames](/entry/plus-letter-maps-frames/), a word $w$ has a transfer matrix $T_w(Y)$, a form $R_w$ and a scalar $q_w$, built letter by letter from $T_{[\,]}(Y) = Q(Y)$, $R_{[\,]} = 1$ and $q_{[\,]} = q$. For a plus letter $l$ on top of $w$,
$$\begin{aligned} R_{l w} &= R_w\, \iota_{a_l}\bigl(T_w(Y_l)\bigr), \\ q_{l w}(Y) &= q_w(Y)\, \frac{Y - Y_l + 1}{Y - Y_l}, \end{aligned}$$
and a minus letter uses the transpose $T_w(Y_l)^{\mathsf T}$ and the factor $(Y_l - Y)/(Y_l - Y - 1)$.

**Definition 1.15.3 (Dual word).** The *dual* of a plus letter at $Y$ is the minus letter at $Y + 1$ on the same site, and the dual of a minus letter at $Y$ is the plus letter at $Y - 1$. For a list $L$ of letters, $L^\vee$ is the list of the duals. Let $J = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$, and let $J_L$ be the product over the letters of $L$, in order, of $\iota_{a_l}(J)$ for a plus letter and $\iota_{a_l}(J^{\mathsf T})$ for a minus letter.

**Definition 1.15.4 (Dual kernel hypotheses).** A pair of words $(w, L)$ satisfies the *dual kernel hypotheses* for $q$ if every letter of $L$ is a plus letter, the words $L w$ and $L^\vee w$ are good (distinct sites, real points, and no two points of the pattern that makes a letter singular for an earlier one), $Y_l - Y_{l'} \notin \{0, 1, -1\}$ for distinct $l, l' \in L$, and $q_w(Y_l) \ne 0$ for every $l \in L$.

For such a pair let $\Psi$ be the product over the letters of $L$, head first, of the factors
$$\Psi_l = \iota_{a_l}\Bigl(-q_{L' w}(Y_l)^{-1}\, J\, T_{L' w}(Y_l + 1)^{\mathsf T}\Bigr),$$
where $L'$ is the part of $L$ below $l$. The duality behind the inequality is the following.

**Proposition 1.15.5 (Duality for words).** Let $(Q, q)$ be a start and let $(w, L)$ satisfy the dual kernel hypotheses. Then $\Psi$ is invertible, and with $\kappa = \prod_{l \in L} q_w(Y_l)$, which is nonzero,
$$\begin{aligned} \Psi^* R_{L w} &= J_L\, R_w, \\ \Psi^* R_{L w}\, \Psi &= \kappa^{-1} R_{L^\vee w}. \end{aligned}$$

*Proof.* By induction on $L$, it is enough to treat one letter at a free site $a$ with transfer matrix $T$ and scalar $q$ at a real point $Y$. The quantum determinant gives $T(Y)\, J\, T(Y+1)^{\mathsf T} = q(Y) J$, so with $\Psi_a = \iota_a(-q(Y)^{-1} J T(Y+1)^{\mathsf T})$ one has $\iota_a(T(Y))\, \Psi_a = \iota_a(J^{\mathsf T})$, and $\Psi_a$ is inverse to $\iota_a(J T(Y))$. The start is hermitian at real points, which turns the first identity into $\Psi_a^* R\, \iota_a(T(Y)) = \iota_a(J) R$, and then
$$\Psi_a^* R\, \iota_a(T(Y))\, \Psi_a = q(Y)^{-1} R\, \iota_a\bigl(T(Y+1)\bigr)^{\mathsf T},$$
whose right side is $q(Y)^{-1}$ times the form of the minus letter at $Y + 1$. The induction passes these identities through the factors already present, using that the factor at a free site commutes with the rest and an intertwining identity of $T_{Lw}$ and $T_{L^\vee w}$ by $\Psi$. The scalars collect to a recursive product, and for a list of plus letters this product is $\prod_l q_w(Y_l)$. $\square$

### The inequality for a pairing

**Theorem 1.15.6 (Dual kernel inequality).** Let $\beta$ be of hermitian class on $U$, let $(Q, q)$ be a start over $\mathrm{Pr}(V)$, and let $(w, L)$ satisfy the dual kernel hypotheses for $q$. Assume:

1. every entry of $\Psi$ lies in $\mathcal A(U, \beta)$;
2. every entry of $R_{L w}$ maps $U$ into $U$;
3. $\langle R_{L w} X, X \rangle_\beta$ is real and nonnegative for every $X$ in $U$.

Let $X_1, X_2$ lie in $U$, and put $A = \langle R_{L w} X_1, X_1 \rangle_\beta$ and $B = \langle R_{L^\vee w} X_2, X_2 \rangle_\beta$. Then $A B / \prod_{l \in L} q_w(Y_l)$ is real and
$$|\langle J_L R_w X_1, X_2 \rangle_\beta|^2 \le \frac{A B}{\prod_{l \in L} q_w(Y_l)}.$$

Lean: `Formalism.FourierDecayAlt.P.PBF.dk_partial`

*Proof.* Let $\kappa = \prod_{l \in L} q_w(Y_l)$, so that the duality for words applies with this $\kappa$, and $\kappa \ne 0$. The entries of $\Psi^*$ also lie in $\mathcal A(U, \beta)$, since it is a star algebra, so $\Psi X_2$ lies in $U$. By the first duality identity and the adjoint property,
$$\langle J_L R_w X_1, X_2 \rangle_\beta = \langle \Psi^* R_{L w} X_1, X_2 \rangle_\beta = \langle R_{L w} X_1, \Psi X_2 \rangle_\beta.$$
By the second identity, $R_{L^\vee w} = \kappa\, \Psi^* R_{L w} \Psi$, so
$$B = \kappa\, \langle R_{L w} \Psi X_2, \Psi X_2 \rangle_\beta = \kappa B',$$
where $B'$ is real and nonnegative by hypothesis 3 applied to $\Psi X_2$. Hence $A B / \kappa = A B'$ is real. The Cauchy-Schwarz inequality for $R_{L w}$, which applies by hypotheses 2 and 3, gives
$$|\langle R_{L w} X_1, \Psi X_2 \rangle_\beta|^2 \le A B' = \frac{A B}{\kappa}. \qquad \square$$

The theorem does not ask that $R_{L^\vee w}$ be positive. In the application both forms are positive, and then $\kappa > 0$ unless $B = 0$.

### The level zero pairing

We now take $V$ to be the radial space $\mathcal R$ of Section 07. Fix a normal form datum $(X, \mu, L, \mathrm{st}, l_0)$, a finite set $S$ of sites, and subspaces $K_0, \dots, K_r$ of $\mathcal R$ on which Theorem P holds: for each admissible word, the level form of its word matrix is sesquilinear and nonnegative on $K_i$ at each level $i$. A word is *admissible* if the start admits it, its points are real and lie on the cut, and any two of its points differ in real part by more than $2$.

Let $Q^{(0)}(Y)$ be the matrix of level zero operators. By the [actual start](/entry/actual-start/) and the [chain step](/entry/chain-descent-relation/), $Q^{(0)}$ with the scalar $q$ of the datum is a start. The *level zero pairing* $\beta_\mu(\Phi, \Psi)$ is the integral over $c \in (\mathbb C^\times)^r$, with weight $\prod_l |c_l|^{-2}$, of the pairing of $\Phi(c, \cdot)$ and $\Psi(c, \cdot)$ against $\mu$. The level zero form of a word $u$ on families with entries in $K_0$ is then $\langle R^{(0)}_u X, X' \rangle_{\beta_\mu}$, where $R^{(0)}_u$ is the form of $u$ built from $Q^{(0)}$; at level zero this form does not depend on the base point $c$.

Three facts hold for this pairing. Theorem P for the empty word says that the level zero form with $R = 1$ is sesquilinear on $K_0$, and the pairing is the integral of an inner product, so $\beta_\mu$ is of hermitian class on $K_0$. Next, let $Y$ be real and assume some one letter plus word at $Y$ is admissible. Its form is $\iota_{s}(Q^{(0)}(Y))$, and Theorem P says this form is sesquilinear and nonnegative, hence hermitian. Evaluating it on families supported at one point of a single site gives, for $\Phi, \Psi \in K_0$,
$$\beta_\mu\bigl(Q^{(0)}_{ij}(Y) \Phi, \Psi\bigr) = \beta_\mu\bigl(\Phi, Q^{(0)}_{ji}(Y) \Psi\bigr).$$
Finally, since $Q^{(0)}(Y)$ is hermitian at real $Y$, the second slot of $Q^{(0)}_{ij}(Y)$ is the first slot of $Q^{(0)}_{ji}(Y)$. To make the generators preserve a subspace, let $\mathrm{Pts} \subseteq \mathbb R$ be a set of such points, let $\mathrm{Gen}$ be the set of entries $Q^{(0)}_{ij}(Y)$ with $Y \in \mathrm{Pts}$, and let $U$ be the set of $\Phi$ with $m_1 \Phi \in K_0$ for every $m$ in the monoid generated by $\mathrm{Gen}$. Then $U \subseteq K_0$, the set $\mathrm{Gen}$ is closed under the star, and every element of $\mathrm{Gen}$ lies in $\mathcal A(U, \beta_\mu)$.

**Theorem 1.15.7 (Dual kernel inequality on the radial space).** Let $(X, \mu, L, \mathrm{st}, l_0)$ be a normal form datum, let $K_0, \dots, K_r$ be subspaces on which Theorem P holds, and let $\mathrm{Pts} \subseteq \mathbb R$ be such that for each $Y \in \mathrm{Pts}$ some one letter plus word at $Y$ is admissible. Let $(w, L)$ satisfy the dual kernel hypotheses for the scalar $q$ of the datum, and assume:

1. the words $L w$ and $L^\vee w$ are admissible;
2. every point of $L w$ lies in $\mathrm{Pts}$, and $Y_l + 1 \in \mathrm{Pts}$ for every $l \in L$.

Let $X_1, X_2$ be families with entries in $U$, and put
$$\begin{aligned} A &= \langle R^{(0)}_{L w} X_1, X_1 \rangle_{\beta_\mu}, \\ B &= \langle R^{(0)}_{L^\vee w} X_2, X_2 \rangle_{\beta_\mu}. \end{aligned}$$
Then $A$ and $B$ are real and nonnegative, and
$$\bigl|\langle J_L R^{(0)}_w X_1, X_2 \rangle_{\beta_\mu}\bigr|^2 \le \operatorname{Re} \frac{A B}{\prod_{l \in L} q_w(Y_l)}.$$

Lean: `Formalism.FourierDecayAlt.P.PBF.dk_radial`

*Proof.* The pairing $\beta_\mu$ is of hermitian class on $K_0$, hence on $U$. By hypothesis 2, every point at which a transfer matrix of $L w$ or of $L^\vee w$ is evaluated lies in $\mathrm{Pts}$: the dual of a plus letter at $Y_l$ sits at $Y_l + 1$. Since $\mathcal A(U, \beta_\mu)$ is an algebra that contains the scalars and the generators, the entries of $R^{(0)}_{L w}$, of $R^{(0)}_{L^\vee w}$ and of $\Psi$ lie in it; for $\Psi$ only the plus factors occur, because every letter of $L$ is a plus letter. In particular the entries of $R^{(0)}_{L w}$ preserve $U$. Theorem P for the admissible words $L w$ and $L^\vee w$ at level zero, with all torus coordinates equal to $1$, gives that $A$ and $B$ are real and nonnegative, and the same for $\langle R^{(0)}_{L w} X, X \rangle_{\beta_\mu}$ for every $X$ in $U$. The level zero form agrees with the tensor pairing, so the dual kernel inequality for a pairing applies with $\beta = \beta_\mu$ and the start $Q^{(0)}$, and gives the bound. $\square$

**Remark 1.15.8 (Formalization).** The radial theorem states $A$ and $B$ as the level zero form at the base point $c = 0$, which lies outside the set where Theorem P is stated; the proof first moves to $c = (1, \dots, 1)$ by the independence of the level zero form from $c$ ([SesquilinearLevelZeroPairing.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/SesquilinearLevelZeroPairing.lean#L213)). Only the positivity part of Theorem P is used. The proof also checks that the entries of $R^{(0)}_w$ and of $J_L R^{(0)}_w$ lie in the adjoint algebra and then does not use these facts, and it rules out the minus factors of $\Psi$ by contradiction with the hypothesis that $L$ has only plus letters. The reality of $A B / \prod q_w(Y_l)$, proved in the first theorem, is dropped in the second, which keeps only the bound. We did not unfold the intertwining identity in the duality for words or the exact goodness conditions; the statements above give them by their role.
