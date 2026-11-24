---
title: Curvature from the Yangian relation
decls:
  - Formalism.FourierDecayAlt.P.Mx6.generic
  - Formalism.FourierDecayAlt.P.Mx6.entries_of
  - Formalism.FourierDecayAlt.P.transfer_rtt_entries
  - Formalism.FourierDecayAlt.P.NFx4.SX.model_scalar
  - Formalism.FourierDecayAlt.P.NFx4.SX.curv
  - Formalism.FourierDecayAlt.P.shift_extra
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Curvature from the Yangian relation

The first two sections went from relations of the operators to the Yangian relation and the quantum determinant. This section goes back. It takes an abstract normal form, that is, a matrix built by the formula of the model from a level and from raising operators about which little is known, and it shows that if this matrix is a start, then the level has the curvature of the model and the raising operators satisfy the relations (N), (C) and (M) of the model. The key input is one scalar identity between polynomials. We compute it in a concrete model, the model over Hahn series, where the Yangian relation is proved by the argument of the first section. The result is used for [the second shift phase](/entry/second-shift-phase-holds/), and through it in the step [HypsAlt is nonempty](/step/nonempty-hyps/).

We keep the notation of the first two sections: the parameter $P$, the types $\pi$ with coordinates $\rho_i$, the scalar functions $x_\pi$, $x^{(S)}_\pi$, $q$, $a_\pi$, $w_\pi$, the norms $N_l$ and $N^-_l$, and the relations (N), (C), (M), (S), (K) and (Sh).

### The Hahn series model

**Definition 1.3.1 (Hahn series model).** Let $r \in \mathbb{N}$ and let $\Gamma$ be the group of integer vectors indexed by the variables $z$, $\bar z$, $c_l$, $\bar c_l$ ($l < r$), with the lexicographic order. The ring $R_{\mathrm{H}}$ is the field of Hahn series $\sum_{\gamma} a_\gamma X^\gamma$ with $a_\gamma \in \mathbb{C}$ and well ordered support in $\Gamma$. The coordinate $x_v$ is the monomial $X^{e_v}$, and $E_v$ is the Euler operator $X^\gamma \mapsto \gamma_v X^\gamma$, extended to series coefficient by coefficient.

These data satisfy the laws of a model algebra: $E_v$ is a derivation with $E_v(x_w) = \delta_{vw} x_w$, the $E_v$ commute, and $x_v$ and $x_z x_{\bar z} - T_2$ are nonzero, hence units of the field. The model operators $\zeta$, $G$, $\nabla$, $\nabla^*$, $S_l$, the algebra $A_{\mathrm{H}}$ of matrices over $\mathrm{Pr}$ indexed by types, and the matrix $Q_{\mathrm{H}}(Y)$ of the level are defined from $R_{\mathrm{H}}$ by the formulas of the first section. We write (N$_{\mathrm{H}}$), (C$_{\mathrm{H}}$), (M$_{\mathrm{H}}$), (S$_{\mathrm{H}}$) and (K$_{\mathrm{H}}$) for the five relations of the first section in this model, each asked for every parameter, and (N$_{\mathrm{H}}$), (C$_{\mathrm{H}}$), (M$_{\mathrm{H}}$) only for admissible ones.

**Theorem 1.3.2 (Yangian relation in the Hahn model at good points).** Assume (N$_{\mathrm{H}}$), (C$_{\mathrm{H}}$), (M$_{\mathrm{H}}$), (S$_{\mathrm{H}}$) and (K$_{\mathrm{H}}$). Let $P$ be an admissible parameter and let $u$, $v$ be good points with $u - v \notin \{0, 1, -1\}$. Then for all $i, j, k, l \in \{1, 2\}$

$$\begin{aligned} (u - v)\bigl[Q_{\mathrm{H}, ij}(u), Q_{\mathrm{H}, kl}(v)\bigr] = {} & Q_{\mathrm{H}, kj}(u) Q_{\mathrm{H}, il}(v) \\ & - Q_{\mathrm{H}, kj}(v) Q_{\mathrm{H}, il}(u) . \end{aligned}$$

Lean: `Formalism.FourierDecayAlt.P.Mx6.generic`

*Proof.* The proof is the same as for the Yangian relation at good points in the first section. At good points the Gauss decomposition writes $Q_{\mathrm{H}}(Y)$ as the triangular product with factors $t$, $d$, $\lambda$, $\mu$. The seven groups of relations between the factors at $u$ and at $v$ follow from the laws, from (C$_{\mathrm{H}}$) and (S$_{\mathrm{H}}$) for the commutator of $\lambda(u)$ with $\lambda(v)$ and of $\mu(u)$ with $\mu(v)$, and from (N$_{\mathrm{H}}$), (M$_{\mathrm{H}}$), (S$_{\mathrm{H}}$), (K$_{\mathrm{H}}$) for the mixed relation. The Gauss lemma for $2 \times 2$ matrices then gives the claim. $\square$

**Theorem 1.3.3 (Yangian relation in the Hahn model, from the relations).** Assume (N$_{\mathrm{H}}$), (C$_{\mathrm{H}}$), (M$_{\mathrm{H}}$), (S$_{\mathrm{H}}$) and (K$_{\mathrm{H}}$). Then for every admissible parameter $P$, all $u, v \in \mathbb{C}$ and all $i, j, k, l \in \{1, 2\}$ the matrix $Q_{\mathrm{H}}$ satisfies the relation of the previous theorem.

Lean: `Formalism.FourierDecayAlt.P.Mx6.entries_of`

*Proof.* Both sides are polynomials in $u$ and in $v$ with coefficients in $A_{\mathrm{H}}$, and the set of points that are not good is finite. Fix a good $v$; the difference of the two sides vanishes for all $u$ outside a finite set, hence for all $u$. Then fix $u$; the difference vanishes for all good $v$, hence for all $v$. $\square$

**Theorem 1.3.4 (Yangian relation in the Hahn model).** For every admissible parameter $P$, all $u, v \in \mathbb{C}$ and all $i, j, k, l \in \{1, 2\}$ the matrix $Q_{\mathrm{H}}$ satisfies the relation (R) of the first section.

Lean: `Formalism.FourierDecayAlt.P.transfer_rtt_entries`

*Proof.* The five relations hold in the Hahn model, by the same computations as in the first section: (N$_{\mathrm{H}}$) and (C$_{\mathrm{H}}$) are identities of the numbers $N_l$ and $N^-_l$, (M$_{\mathrm{H}}$) compares the entries of $S_l^* S_j$ and $S_j S_l^*$, (S$_{\mathrm{H}}$) uses $a_{\pi + e_l} = a_\pi - 1$, and (K$_{\mathrm{H}}$) is a commutator of Euler operators with multiplication operators. The previous theorem gives the claim. $\square$

### Normal form data

**Definition 1.3.5 (Normal form datum).** Let $\mathcal{A}$ be a star ring that is a $\mathbb{C}$-algebra and let $P$ be a parameter. A *normal form datum* $\mathsf{d}$ over $\mathcal{A}$ consists of a level datum $L$ in $\mathcal{A}$ (as in the second section, with its operators $\zeta$, $\bar\zeta$, $G$, $\nabla$, $\nabla^*$, its function operators and its number $T_L$), an algebra map $\kappa$ from complex functions of types to $\mathcal{A}$, and elements $S_l \in \mathcal{A}$ for $l \in \mathbb{N}$. Its *matrix* $Q_{\mathsf{d}}(Y)$ is given by the formulas for $Q_{11}$, $Q_{12}$, $Q_{21}$, $Q_{22}$ of the first section, with $\zeta$, $G$, $\nabla$, $\nabla^*$, $l_0$, $m_0$ taken from $L$, and $x(Y) = \kappa(x_\pi(Y))$.

The datum *satisfies the relations of a normal form* if:

1. $\kappa(f)^* = \kappa(\bar f)$ for every $f$;
2. every $\kappa(f)$ commutes with the function operators of $L$ and with $\nabla$ and $\nabla^*$;
3. every $S_l$ commutes with the function operators of $L$ and with all $p_m$ and $\bar p_m$;
4. the relation (Sh) holds for every $S_l$;
5. the relation (S) holds for $1 \le l \le k - 1$;
6. $S_l^* S_l = \kappa(N_l)$ for $1 \le l \le k - 1$.

The level is a *star level* if $\zeta^* = \bar\zeta$, $\nabla^* $ is the star of $\nabla$, and $T_L$ is real.

The proofs below use only conditions 1, 4, 6 and the part of condition 2 that concerns $\nabla$, $\nabla^*$, $\zeta$, $\bar\zeta$, $G$ and $G^{-1}$. Let $E_\pi = \kappa(\delta_\pi)$, where $\delta_\pi$ is the indicator of the type $\pi$. These are orthogonal idempotents with sum $1$, and $\kappa(f) = \sum_\pi f(\pi) E_\pi$. Condition 4 gives $E_\sigma S_l E_\pi = S_l E_\pi$ if $\pi \to_l \sigma$ and $0$ otherwise, so $S_l$ raises the type by $e_l$ and $S_l^*$ lowers it by $e_l$. Two elements $X$, $X'$ are equal when $X E_\pi = X' E_\pi$ for all $\pi$.

### The scalar of the diagonal blocks

For a type $\pi$, an index $m$ and $Y, Y' \in \mathbb{C}$, put $c_m(\pi; Y, Y') = x^{(m)}_\tau(Y)\, x^{(m)}_\tau(Y')$ if there is a type $\tau$ with $\tau \to_m \pi$, and $c_m(\pi; Y, Y') = 0$ otherwise. Define

$$\begin{aligned} C_\pi(u, v) = {} & x_\pi(u) w_\pi(v) - x_\pi(v) w_\pi(u) \\ & - (u - v) \sum_m x^{(m)}_\pi(u) x^{(m)}_\pi(v) N_m(\pi) \\ & + (u - v) \sum_m c_m(\pi; v, u) N^-_m(\pi), \end{aligned}$$

with $m$ running over $\{1, \dots, k-1\}$. This is a polynomial in $u$ and $v$ that depends only on $P$ and $\pi$.

The link between $C_\pi$ and the curvature is a diagonal identity. Let $\mathsf{d}$ be a normal form datum that satisfies conditions 1, 2, 4 and 6, assume $S_l S_l^* = \kappa(N^-_l)$ for $1 \le l \le k-1$, and assume that $Q_{\mathsf{d}}$ satisfies (R) with $(i, j, k, l) = (1, 2, 2, 1)$:

$$(u - v)\bigl[Q_{12}(u), Q_{21}(v)\bigr] = Q_{22}(u) Q_{11}(v) - Q_{22}(v) Q_{11}(u) .$$

Multiply on both sides by $E_\pi$. In the products of entries only the terms that keep the type survive. On the right, $E_\pi Q_{11}(v) E_\pi = (G^{-1} w_\pi(v) + G x_\pi(v) m_0(v) l_0(v)) E_\pi$, because the terms with $\Sigma$, $\Sigma^*$ and $S_l^* S_j$ for $j \ne l$ move the type. On the left, the product $\Sigma^*(u) \Sigma(v)$ gives $\sum_m x^{(m)}_\pi(u) x^{(m)}_\pi(v) N_m(\pi)$ by condition 6, and $\Sigma(v) \Sigma^*(u)$ gives $\sum_m c_m(\pi; v, u) N^-_m(\pi)$ by the relation for $S_l S_l^*$. The remaining terms contain $m_0$ and $l_0$; their commutators are computed with the level relations, and they produce the curvature. The result is

$$\begin{aligned} & (u - v) x_\pi(u) x_\pi(v) \bigl(G^2 (\nabla^* \nabla - \nabla \nabla^*) \\ & \quad + (1 + u + v)(\zeta \bar\zeta - G)\bigr) E_\pi = C_\pi(u, v) E_\pi . \end{aligned} \tag{D}$$

**Theorem 1.3.6 (The model scalar).** Let $P$ be an admissible parameter. For every type $\pi$ and all $u, v \in \mathbb{C}$,

$$C_\pi(u, v) = (u - v)\, x_\pi(u) x_\pi(v) \bigl(2 a_\pi T_2 + (1 + u + v) T_2\bigr).$$

Lean: `Formalism.FourierDecayAlt.P.NFx4.SX.model_scalar`

*Proof.* Take the Hahn series model and a model level $L$ in it. The datum $(L, \kappa, (S_l))$ is a normal form datum whose matrix is $Q_{\mathrm{H}}$, and it satisfies conditions 1, 2, 4 and 6 and $S_l S_l^* = \kappa(N^-_l)$, by direct computation and (N$_{\mathrm{H}}$). Its matrix satisfies (R) by the Yangian relation in the Hahn model. So (D) holds. In the model $\zeta \bar\zeta - G = T_2$, and by the curvature (K$_{\mathrm{H}}$)

$$G^2 (\nabla^* \nabla - \nabla \nabla^*) = G^2 \kappa(2 a_\pi T_2) G^{-2} = \kappa(2 a_\pi T_2),$$

since $\kappa(f)$ commutes with $G$. Hence the left side of (D) is $(u - v) x_\pi(u) x_\pi(v)(2 a_\pi T_2 + (1 + u + v) T_2) E_\pi$. Both sides of (D) are then complex multiples of $E_\pi$. In the model $E_\pi \ne 0$, because its $(\pi, \pi)$ entry is $1$ and $\mathrm{Pr}$ is a nontrivial ring. So the two complex numbers are equal. $\square$

**Theorem 1.3.7 (Curvature from a start).** Let $P$ be an admissible parameter and let $\mathsf{d}$ be a normal form datum over $\mathcal{A}$ that satisfies conditions 1, 4 and 6, and in which $\kappa(f)$ commutes with $\nabla$, $\nabla^*$, $\zeta$, $\bar\zeta$, $G$ and $G^{-1}$. Assume that $(Q_{\mathsf{d}}, q)$ is a start and that $S_l S_l^* = \kappa(N^-_l)$ for $1 \le l \le k - 1$. Then

$$\nabla^* \nabla - \nabla \nabla^* = \kappa(2 a_\pi T_2)\, G^{-1} G^{-1}.$$

Lean: `Formalism.FourierDecayAlt.P.NFx4.SX.curv`

*Proof.* Since $(Q_{\mathsf{d}}, q)$ is a start, $Q_{\mathsf{d}}$ satisfies the RTT relation, and so (R) in entries; this gives (D). Fix a type $\pi$. Write $K = G^2(\nabla^* \nabla - \nabla \nabla^*)$, and recall $\zeta \bar\zeta - G = T_L$ in any level datum. If $(u - v) x_\pi(u) x_\pi(v) \ne 0$, then (D), the previous theorem and the fact that $\mathcal{A}$ is a complex vector space give

$$K E_\pi + (1 + u + v) T_L E_\pi = 2 a_\pi T_2 E_\pi + (1 + u + v) T_2 E_\pi .$$

The roots of $x_\pi$ are real, so this applies to $(u, v) = (i, 2i)$ and to $(u, v) = (2i, 3i)$. The difference of the two equations is $2i (T_L - T_2) E_\pi = 0$, so $T_L E_\pi = T_2 E_\pi$. Then the first equation gives $K E_\pi = 2 a_\pi T_2 E_\pi = \kappa(2 a_\pi T_2) E_\pi$. Multiply on the left by $G^{-2}$ and move $G^{-1}$ past $\kappa(2 a_\pi T_2)$: this gives $(\nabla^* \nabla - \nabla \nabla^*) E_\pi = \kappa(2 a_\pi T_2) G^{-1} G^{-1} E_\pi$. As this holds for every $\pi$, the claim follows. $\square$

**Theorem 1.3.8 (Extra relations from a start).** Let $P$ be an admissible parameter, let $\mathcal{A}$ be a star ring that is a $\mathbb{C}$-algebra, and let $\mathsf{d}$ be a normal form datum over $\mathcal{A}$ whose level is a star level, which satisfies the relations of a normal form, and for which $(Q_{\mathsf{d}}, q)$ is a start. Then:

1. $\nabla^* \nabla - \nabla \nabla^* = \kappa(2 a_\pi T_2)\, G^{-1} G^{-1}$;
2. $S_l S_l^* = \kappa(N^-_l)$ for $1 \le l \le k - 1$;
3. $S_j S_l\, \kappa(\rho_j - \rho_l - 1) = S_l S_j\, \kappa(\rho_j - \rho_l + 1)$ for $j \ne l$ in $\{1, \dots, k-1\}$;
4. $S_l^* S_j = S_j S_l^*$ for $j \ne l$ in $\{1, \dots, k-1\}$.

Lean: `Formalism.FourierDecayAlt.P.shift_extra`

*Proof.* All four parts are proved on the blocks $E_\sigma X E_\pi$ of the two sides.

Part 2. Both sides are diagonal, so fix $\pi$. If no type $\tau$ has $\tau \to_l \pi$, both blocks are $0$: on the left because $S_l^*$ lowers the type, on the right because $N^-_l(\pi) = 0$ at such a type. Otherwise put $Y = -\rho_l(\pi)$, so that $x_\pi(Y) = 0$. The seventh of the eight determinant relations, $Q_{21}(Y) Q_{12}(Y + 1) - Q_{22}(Y) Q_{11}(Y + 1) = -q(Y)$, holds because $(Q_{\mathsf{d}}, q)$ is a start. In its $(\pi, \pi)$ block the terms that begin with $G x(Y)$ vanish, and the block of $\Sigma(Y) \Sigma^*(Y + 1)$ reduces to the single term $x^{(l)}_\tau(Y) x^{(l)}_\tau(Y + 1)\, S_l S_l^* E_\pi$. The two products $x^{(l)}_\tau(Y)$ and $x^{(l)}_\tau(Y + 1)$ are the denominators of $N_l(\tau)$, which is positive, so they are nonzero. Comparing with $-q(Y)$ and using $N^-_l(\pi) = N_l(\tau)$ gives the block of part 2.

Part 4. Let $\sigma = \pi + e_j - e_l$; the other blocks of both sides vanish because both sides move the type by $e_j - e_l$. Take (R) with $(i, j, k, l) = (1, 2, 2, 1)$ at $u = -\rho_l(\sigma)$ and $v = -\rho_j(\sigma)$, and look at its $(\sigma, \pi)$ block. The terms with $Q_{22}$ vanish because $x_\sigma(u) = x_\sigma(v) = 0$. What is left is a nonzero scalar times $E_\sigma (S_l^* S_j - S_j S_l^*) E_\pi$, so this block vanishes.

Part 3. Let $\sigma = \pi + e_j + e_l$. The entries $Q_{21}(u)$ and $Q_{21}(v)$ commute, by (R) with $(i, j, k, l) = (2, 1, 2, 1)$ as in the second section. Take $u = -\rho_l(\pi)$ and $v = -\rho_j(\pi)$ and look at the $(\sigma, \pi)$ block of $[Q_{21}(u), Q_{21}(v)] = 0$. It is a combination of $S_j S_l E_\pi$ and $S_l S_j E_\pi$ with scalar coefficients, and the coefficients are proportional to $\rho_j - \rho_l - 1$ and $\rho_j - \rho_l + 1$. This gives part 3 on the block, and the other blocks vanish.

Part 1. With part 2 in hand, this is the previous theorem. $\square$

**Remark 1.3.9 (Formalization).** The proof of the model scalar is a detour: the identity is between polynomials in $u$ and $v$, but it is proved by building the Hahn series model, proving the Yangian relation there, and cancelling a projection (`HermitianCurvatureProofs/NormalFormOrderZeroOfParts.lean:2796`). The Yangian relation of the Hahn model repeats, nearly line by line, the proof of the Yangian relation for a general model algebra (`HermitianCurvatureProofs/TransferRtt.lean:1809` against `HermitianCurvatureProofs/CoordinateCommuteRaisingConstant.lean:3548`); the Hahn model satisfies the laws of a model algebra, so one proof would serve. The extra relations take the star level as a hypothesis and do not use it (`HermitianCurvatureProofs/NormalFormOrderZeroOfParts.lean:2912`), and they drop conditions 3 and 5 of a normal form when they pass to the smaller hypothesis set (line 1660). The curvature theorem uses only the RTT field of the start (line 2865); the determinant field enters through part 2. The proof of part 1 shows $T_L = T_2$ on each block, so it does not need the level number to equal $T T'$.
