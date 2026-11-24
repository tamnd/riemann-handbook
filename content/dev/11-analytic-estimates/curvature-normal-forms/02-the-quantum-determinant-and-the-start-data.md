---
title: The quantum determinant and the start data
decls:
  - Formalism.FourierDecayAlt.P.MAx1.D7.qQDet_of
  - Formalism.FourierDecayAlt.P.MAx1.qQDet
  - Formalism.FourierDecayAlt.P.MAx1.startIsStart
  - Formalism.FourierDecayAlt.P.MAx1.startOK
  - Formalism.FourierDecayAlt.P.start_admissible
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The quantum determinant and the start data

This section proves that the matrix $Q$ of a level has the scalar quantum determinant $q$, and it assembles the start data of a model level. With the Yangian relation of the previous section and a Hermitian symmetry, the determinant makes the pair $(Q, q)$ a start, and ten conditions together make the start data admissible at the model level. The last result is an input of the model frame, which builds the frames on cut words at a model level and is used in the step [HypsAlt is nonempty](/step/nonempty-hyps/).

We keep the notation of the previous section, with $t(Y) = Q_{22}(Y) = G x(Y)$.

### More relations of the model

Besides $\zeta$ and $\bar\zeta$ the model algebra has the multiplication operators $c_l = (x_{c_l}, x_{\bar c_l})$ and $\bar c_l = (x_{\bar c_l}, x_{c_l})$ for $l < r$, their inverses, and the derivative pairs $p_l = (E_{c_l}, -E_{\bar c_l})$ and $\bar p_l = (E_{\bar c_l}, -E_{c_l})$. The proof of the determinant uses the following facts, each asked for every parameter and every model algebra that satisfies the laws.

- (Sc) Each $S_l$ commutes with every scalar matrix.
- (Sh) If $f$, $g$ are functions of types with $g(\pi') = f(\pi)$ whenever $\pi \to_l \pi'$, then $\kappa(g) S_l = S_l \kappa(f)$.
- (U) If $\pi \to_l \pi'$, then $\rho_i(\pi') = \rho_i(\pi) + 1$ for $i = l$ and $\rho_i(\pi') = \rho_i(\pi)$ for the other $i$ in $\{1, \dots, k-1\}$.
- (F) The operators $c_l$, $\bar c_l$, $\zeta$, $\bar\zeta$, $G$ and their inverses commute with each other, each is inverse to its partner on both sides, and $G = \zeta \bar\zeta - T_2$.
- (D) $\nabla \zeta = \zeta \nabla + 1$, $\nabla \zeta^{-1} = \zeta^{-1} \nabla - \zeta^{-2}$, $\nabla G = G \nabla + \bar\zeta$, $\nabla G^{-1} = G^{-1} \nabla - \bar\zeta G^{-2}$, and $\nabla$ commutes with $\bar\zeta^{\pm 1}$ and with all $c_l^{\pm 1}$, $\bar c_l^{\pm 1}$.
- (D$^*$) $\nabla^* \bar\zeta = \bar\zeta \nabla^* - 1$, $\nabla^* \bar\zeta^{-1} = \bar\zeta^{-1} \nabla^* + \bar\zeta^{-2}$, $\nabla^* G = G \nabla^* - \zeta$, $\nabla^* G^{-1} = G^{-1} \nabla^* + \zeta G^{-2}$, and $\nabla^*$ commutes with $\zeta^{\pm 1}$ and with all $c_l^{\pm 1}$, $\bar c_l^{\pm 1}$.
- (St) $c_l^* = \bar c_l$, $(c_l^{-1})^* = \bar c_l^{-1}$, $p_l^* = -\bar p_l$, $\zeta^* = \bar\zeta$, $(\zeta^{-1})^* = \bar\zeta^{-1}$, $G^* = G$, $(G^{-1})^* = G^{-1}$ and $\nabla^{\,*} = \nabla^*$, the last being the star of $\nabla$.

Put $\iota(Y) = G^{-1} \kappa(x_\pi(Y)^{-1})$ when no $x_\pi(Y)$ is zero; it is the inverse of $t(Y)$. Let $\lambda(Y)$ be as in the previous section and put

$$\mu_0(Y) = m_0(Y) + G^{-1} \sum_j \kappa\Bigl(\frac{1}{Y + \rho_j}\Bigr) S_j^* .$$

- (G) Let $P$ be admissible and let no $x_\pi(Y)$ be zero. Then $Q_{21}(Y) = t(Y) \lambda(Y)$ and $Q_{12}(Y) = t(Y) \mu_0(Y)$. If also no $x_\pi(Y + 1)$ is zero, then $Q_{11}(Y) = q(Y)\iota(Y + 1) + t(Y) \mu_0(Y) \lambda(Y)$. If $Y$ is real, then $\mu_0(Y) = \lambda(Y - 1)^*$. This is a second form of the Gauss decomposition.

### The quantum determinant

Let $J = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$. A family $M(Y)$ of $2 \times 2$ matrices over a $\mathbb{C}$-algebra *has quantum determinant* $q$ if for every $Y$

$$M(Y + 1)^{T} J M(Y) = q(Y) J, \qquad M(Y) J M(Y + 1)^{T} = q(Y) J .$$

Here $M^T$ is the transpose without star. Write $M(Y) = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ and $M(Y + 1) = \begin{pmatrix} a' & b' \\ c' & d' \end{pmatrix}$. By a direct expansion, the two matrix equations hold when these eight relations hold:

$$a'c - c'a = 0, \quad a'd - c'b = q, \quad b'c - d'a = -q, \quad b'd - d'b = 0,$$

$$ab' - ba' = 0, \quad ad' - bc' = q, \quad cb' - da' = -q, \quad cd' - dc' = 0 .$$

The second relation reads $Q_{11}(Y + 1) Q_{22}(Y) - Q_{21}(Y + 1) Q_{12}(Y) = q(Y)$, which is the quantum determinant of the Yangian $\mathrm{Y}(\mathfrak{gl}_2)$ with the shift written as $Y + 1$.

**Theorem 1.2.1 (Quantum determinant, from the relations).** Assume (Sc), (Sh), (U), (F), (D), (D$^*$), (St), (S), (N), (M), (K) and (G). Then for every admissible parameter $P$ and every model algebra $D$ that satisfies the laws, the matrix $Q$ of the level has quantum determinant $q$.

Lean: `Formalism.FourierDecayAlt.P.MAx1.D7.qQDet_of`

*Proof.* Fix $Y$. It is enough to prove the eight relations above for $M = Q$.

First let $Y$ be a point where no $x_\pi(Y)$, $x_\pi(Y + 1)$, $x_\pi(Y + 2)$ is zero. Write $t_0 = t(Y)$, $t_1 = t(Y + 1)$, $\iota_n = \iota(Y + n)$, $\lambda_n = \lambda(Y + n)$ and $\mu_n = \mu_0(Y + n)$, and $q_n = q(Y + n)$. By (G) at $Y$ and at $Y + 1$,

$$Q(Y) = \begin{pmatrix} q_0 \iota_1 + t_0 \mu_0 \lambda_0 & t_0 \mu_0 \\ t_0 \lambda_0 & t_0 \end{pmatrix},$$

and $Q(Y + 1)$ is the same with every index raised by one. Three facts about the factors are needed.

1. $\lambda_0 t_1 = t_1 \lambda_1$. This uses (Sc), (Sh), (U), (F) and (D). Moving $\nabla$ past $G$ shifts $Y$ by one in $(Y + \tfrac12)\bar\zeta G^{-1}$, and moving $S_j$ past $\kappa(x_\pi)$ shifts the factors $1/(Y + \rho_j)$.
2. $\mu_1 t_0 = t_0 \mu_0$. This is the same computation with (D$^*$) in place of (D).
3. $\mu_1 \lambda_1 - \lambda_1 \mu_1 = q_0\, \iota_0 \iota_1 - q_1\, \iota_1 \iota_2$. This is the main computation. It uses all of (Sc), (Sh), (U), (F), (D), (D$^*$), (St), (S), (N), (M) and (K). The commutator of the two covariant derivatives in $\mu_1 \lambda_1$ is the curvature (K); the cross terms $S_j^* S_l$ with $j \ne l$ cancel by (M); and the terms $S_l^* S_l$ and $S_l S_l^*$ become the diagonal matrices $\kappa(N_l)$ and $\kappa(N^-_l)$ by (N). The diagonal parts then add up to the right side, by the partial fraction expansion of $q(Y) / (x_\pi(Y) x_\pi(Y + 1))$.

Each of the eight relations is now an identity in the ring $A$ between products of $t_0, t_1, \iota_0, \iota_1, \iota_2, \lambda_0, \lambda_1, \mu_0, \mu_1$. For example the second relation is

$$\bigl(q_1 \iota_2 + t_1 \mu_1 \lambda_1\bigr) t_0 - t_1 \lambda_1 \, t_0 \mu_0 = q_0 .$$

By fact 2, $t_1 \mu_1 \lambda_1 t_0 - t_1 \lambda_1 t_0 \mu_0 = t_1 \mu_1 \lambda_1 t_0 - t_1 \lambda_1 \mu_1 t_0$, and by fact 3 this is $t_1 (q_0 \iota_0 \iota_1 - q_1 \iota_1 \iota_2) t_0$. The terms with $q_1$ cancel because $t_1 \iota_1 = 1$, and the term with $q_0$ is $q_0\, t_1 \iota_1 \iota_0 t_0 = q_0$. The other seven relations follow in the same way from facts 1 to 3, the inverse relations $t_n \iota_n = \iota_n t_n = 1$ and the commutation of $\iota_0$ with $\iota_1$.

Now let $Y$ be arbitrary. The set of points where some $Y + \rho_j(\pi) + n$ with $n \in \{0, 1, 2\}$ is zero is finite. Each of the eight relations, with both sides taken as functions of $Y$, is an equation between polynomials in $Y$ with coefficients in $A$: the entries of $Q$, the function $q$ and the constants are polynomial. Two such polynomials that agree outside a finite set are equal. So the eight relations hold at every $Y$. $\square$

**Theorem 1.2.2 (Quantum determinant).** For every admissible parameter $P$ and every model algebra $D$ that satisfies the laws, the matrix $Q$ of the level has quantum determinant $q$.

Lean: `Formalism.FourierDecayAlt.P.MAx1.qQDet`

*Proof.* All twelve hypotheses of the previous theorem hold in the model. Relations (N), (M), (S) and (K) were discussed in the previous section. (Sc) holds because the nonzero entries of $S_l$ are complex numbers, which are central in $\mathrm{Pr}$. (Sh) holds because both sides have the entry $g(\pi')\sqrt{N_l(\pi)} = \sqrt{N_l(\pi)} f(\pi)$ at $(\pi', \pi)$ for $\pi \to_l \pi'$ and $0$ elsewhere. (U) is the definition $\rho_i = \mathrm{lo}_i + \pi_i$. (F) follows from the commutativity of $R$ and the units in the laws. (D) and (D$^*$) follow from the Leibniz rule and $E_v(x_w) = \delta_{vw} x_w$. (St) holds because the star of $\mathrm{Pr}$ swaps the two slots and $\kappa(f)^* = \kappa(\bar f)$. Last, (G) is the Gauss decomposition, proved from the definition of the entries in the same way as in the previous section, using (N) for the upper left entry. $\square$

### Starts

**Definition 1.2.3 (Start).** Let $M(Y)$ be a family of $2 \times 2$ matrices over a star ring that is a $\mathbb{C}$-algebra, and let $q : \mathbb{C} \to \mathbb{C}$. The pair $(M, q)$ is a *start* if:

1. $M(Y)^H = M(Y)$ for real $Y$, where $M^H$ is the conjugate transpose;
2. $M$ satisfies the RTT relation;
3. $M$ has quantum determinant $q$;
4. $q(Y)$ is real for real $Y$.

For $l \in \mathbb{N}$ put $s_l = (-1)^{k - l}$.

**Theorem 1.2.4 (The start matrix is a start).** Let $P$ be an admissible parameter and let $D$ be a model algebra that satisfies the laws. For every $l \in \mathbb{N}$ the pair $(s_l Q, q)$ is a start.

Lean: `Formalism.FourierDecayAlt.P.MAx1.startIsStart`

*Proof.* First consider $(Q, q)$. The matrix $Q$ satisfies $Q(Y)^H = Q(\bar Y)$ for every $Y$. This is a computation from the stars of the model operators: $\nabla$ and $\nabla^*$ are stars of each other, $\zeta^* = \bar\zeta$, $G^* = G$, $\kappa(f)^* = \kappa(\bar f)$, and the star of the term $\Sigma(Y)$ in $Q_{21}$ is the term $\Sigma^*(\bar Y)$ in $Q_{12}$, because the functions $x_\pi$, $x^{(l)}_\pi$ and $w_\pi$ have real coefficients. For real $Y$ this gives condition 1. Condition 2 is the Yangian relation of the previous section, and condition 3 is the quantum determinant above. The polynomial $q$ has real coefficients, which gives condition 4.

Now multiply by $s = s_l$. It is real and $s^2 = 1$. Condition 1 is kept because $(sM)^H = \bar s M^H = s M^H$. The two sides of the RTT relation are quadratic in $M$, so both get the factor $s^2 = 1$. The same holds for the quantum determinant. Condition 4 does not involve $M$. $\square$

### Start data at a model level

A *level datum* is a list of elements of a star ring: $p_l$, $\bar p_l$, $c_l$, $c_l^{-1}$, $\bar c_l$, $\bar c_l^{-1}$ for $l < r$, and $\zeta$, $\zeta^{-1}$, $\bar\zeta$, $\bar\zeta^{-1}$, $G$, $G^{-1}$, $\nabla$, $\nabla^*$ and a number $T_2$, subject to the relations (F), (D), (D$^*$) and the Weyl relations of the $p_l$ with the $c_m$. It is a *model level* if every entry is the model operator of the same name in $A$ and $T_2 = T T'$. Its *lowering constant* is $l_0(Y) = -\nabla - (Y + \tfrac12) \bar\zeta G^{-1}$.

**Definition 1.2.5 (Start data).** The start data of $l \in \mathbb{N}$ at the model are:

- the matrix $s_l Q(Y)$ and the scalar $q(Y)$;
- the elements $x(Y) = \kappa(s_l\, x_\pi(Y))$ and $\xi(Y) = \kappa\bigl((s_l\, x_\pi(Y))^{-1}\bigr)$;
- the element $e(Y) = \zeta \bar\zeta^{-1} \sum_{j} \kappa\bigl(1/(Y + \rho_j)\bigr) S_j$;
- the set $\Omega$ of $Y$ with $x_\pi(Y) \ne 0$ for all types $\pi$.

**Definition 1.2.6 (Admissible start).** Let $L$ be a level datum and let $(M, q, x, \xi, e, \Omega)$ be start data. They are *admissible* at $L$ when:

1. $(M, q)$ is a start;
2. $M_{21}(Y)$ and $M_{21}(Y')$ commute for all $Y, Y'$;
3. $x(Y) \xi(Y) = \xi(Y) x(Y) = 1$ for $Y \in \Omega$;
4. $x(Y)$ and $x(Y')$ commute for all $Y, Y'$;
5. $x(Y)$ commutes with $\zeta^{\pm 1}$, $\bar\zeta^{\pm 1}$ and $G^{\pm 1}$ of $L$;
6. $x(Y)$ commutes with $\nabla$ of $L$;
7. $x(Y)^* = x(Y)$ for real $Y$;
8. $e(Y)$ commutes with $\zeta^{\pm 1}$, $\bar\zeta^{\pm 1}$ and $G^{\pm 1}$ of $L$;
9. $M_{22}(Y) = G x(Y)$;
10. $M_{21}(Y) = G x(Y) \bigl(l_0(Y) + \bar\zeta \zeta^{-1} G^{-1} e(Y)\bigr)$ for $Y \in \Omega$.

**Theorem 1.2.7 (Start data at a model level).** Let $P$ be an admissible parameter and let $D$ be a model algebra that satisfies the laws. For every $l \in \mathbb{N}$ and every model level $L$, the start data of $l$ are admissible at $L$.

Lean: `Formalism.FourierDecayAlt.P.MAx1.startOK`

*Proof.* Since $L$ is a model level, its entries are the model operators, and $\zeta^{\pm 1}$, $\bar\zeta^{\pm 1}$, $G^{\pm 1}$ are scalar matrices. Condition 1 is the previous theorem.

Condition 2. The entries $Q_{21}(u)$ and $Q_{21}(v)$ commute for all $u, v$. Take $i = k = 2$ and $j = l = 1$ in the Yangian relation (R): it gives $(u - v)[Q_{21}(u), Q_{21}(v)] = [Q_{21}(u), Q_{21}(v)]$, so the commutator vanishes when $u - v \ne 1$. As a function of $v$ it is a polynomial with coefficients in $A$, so it vanishes for all $v$. The factor $s_l$ is a scalar and does not change this.

Conditions 3, 4, 5, 6 and 7 hold because $x(Y)$ and $\xi(Y)$ are diagonal matrices with complex entries: $\kappa$ is an algebra map, $s_l x_\pi(Y) \ne 0$ on $\Omega$, complex numbers are central in $\mathrm{Pr}$, $\nabla$ is diagonal, and for real $Y$ the entries $s_l x_\pi(Y)$ are real. Condition 8 holds because $e(Y)$ is a sum of products of diagonal scalar matrices and the $S_j$, and these commute with scalar matrices by (Sc). Condition 9 is $s_l Q_{22} = s_l G x = G \kappa(s_l x_\pi)$.

Condition 10. By definition $Q_{21} = G x\, l_0 + \sum_j S_j\, x^{(j)}$. Since $\zeta$, $\bar\zeta$ and $G$ commute with the diagonal matrices and the $S_j$,

$$G x \cdot \bar\zeta \zeta^{-1} G^{-1} e = x \sum_j \kappa\Bigl(\frac{1}{Y + \rho_j}\Bigr) S_j .$$

For $Y \in \Omega$ the diagonal matrix $x\,\kappa(1/(Y + \rho_j))$ is $\kappa(g)$ with $g(\pi') = \prod_{i \ne j} (Y + \rho_i(\pi'))$. By (U), $g(\pi') = x^{(j)}_\pi(Y)$ when $\pi \to_j \pi'$, so (Sh) gives $\kappa(g) S_j = S_j\, x^{(j)}$. Summing over $j$ gives condition 10 for $Q$, and multiplying by $s_l$ gives it for the start data. $\square$

**Theorem 1.2.8 (Admissible start at the model).** For every admissible parameter $P$, every model algebra $D$ that satisfies the laws, every $l \in \mathbb{N}$ and every model level $L$, the start data of $l$ are admissible at $L$.

Lean: `Formalism.FourierDecayAlt.P.start_admissible`

*Proof.* This is the previous theorem. $\square$

**Remark 1.2.9 (Formalization).** The last theorem differs from the one before only in how the laws enter: there they are an instance argument, here an explicit hypothesis, which the proof turns into an instance (`HermitianCurvatureProofs/CoordinateCommuteRaisingConstant.lean:6160`). Its one user is the theorem on the model frame at line 6190. The file states the Gauss decomposition twice: with $t$ on the right of the upper factor for the Yangian relation (line 3506), and as (G) with $t$ on the left for the determinant (line 124). The determinant theorem (line 5136) takes (G) as a hypothesis, though it follows from the definitions. The commutation of the lower left entries is proved directly from (Sc), (Sh), (C), (S), (D), (F) and (U) (line 3883), and not from the Yangian relation as above. The file name does not describe its content.
