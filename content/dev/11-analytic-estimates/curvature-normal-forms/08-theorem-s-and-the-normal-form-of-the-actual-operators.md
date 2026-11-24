---
title: Theorem S and the normal form of the actual operators
decls:
  - Formalism.FourierDecayAlt.P.theorem_S_ring
  - Formalism.FourierDecayAlt.P.NFx2.sc_main
  - Formalism.FourierDecayAlt.P.normalFormFromModule_statement
status: drafted
drafted_by: writer@claude-opus-5-5
---

## Theorem S and the normal form of the actual operators

The first part of this chapter studied a model: a level datum with explicit shift operators, its matrix $Q_{\mathsf d}(Y)$, and the relations of a [normal form datum](/entry/curv/). This section proves that the operators that act on the radial space of a real place have this model form. The main algebraic result is Theorem S. It says that a $2 \times 2$ matrix over a star algebra that is a start, and whose entries obey a few commutation rules with one function $\zeta$, is the matrix $Q_{\mathsf d}$ of a normal form datum. Then we reduce the normal form of the actual operators to Theorem S and four facts about the actual operators: they form a start, they obey the commutation rules with $\zeta$, they have the right leading terms in $Y$, and the radial space splits by types. The result is used in the step [HypsAlt is nonempty](/step/nonempty-hyps/).

### Pre-levels and the hypotheses of Theorem S

We keep the notation of the [first section](/entry/q-qrtt/). Let $P = (k, r, T, T', u, u')$ be a parameter, with its types $\pi$, the relations $\rho \to_l \rho'$ between types, the norms $N_l(\rho)$ and the functions $x_\pi(Y)$. Let $\mathcal A$ be a star ring that is a $\mathbb C$-algebra.

**Definition 1.8.1 (Pre-level).** A *pre-level* $L_0$ in $\mathcal A$ consists of the elements $\zeta, \bar\zeta, G, G^{-1}$, the site operators $c_l, c_l^{-1}, \bar c_l, \bar c_l^{-1}, p_l, \bar p_l$ for $l < r$, and a set of function operators that contains them. A level datum $L$ *extends* $L_0$ if it has the same elements and adds a connection $\nabla$ and its partner $\nabla^*$.

A level datum is the object of the first section without its connection. The connection is the one piece of a normal form datum that Theorem S has to construct.

**Definition 1.8.2 (Hypotheses of Theorem S).** Let $L_0$ be a pre-level, let $Q(Y)$ be a family of $2 \times 2$ matrices over $\mathcal A$, and let $\kappa$ be an algebra map from the complex functions on types to $\mathcal A$. We say that $(L_0, Q, \kappa)$ satisfies (SH) if:

1. the star rules $\zeta^* = \bar\zeta$, $c_l^* = \bar c_l$, $(c_l^{-1})^* = \bar c_l^{-1}$ and $p_l^* = -\bar p_l$ hold, and $G$ is hermitian;
2. $(Q, q)$ is a [start](/entry/start-is-start/) for the scalar $q$ of $P$, and the entries $Q_{21}(Y)$ and $Q_{21}(Y')$ commute for all $Y, Y'$;
3. $Q_{22}(Y) = G\, \kappa(x_\pi(Y))$, the map $\kappa$ satisfies $\kappa(f)^* = \kappa(\bar f)$, and each $\kappa(f)$ commutes with the function operators and the site operators;
4. $Q_{21}(Y) = -Y^k \bar\zeta + (\text{terms of lower degree in } Y)$;
5. the six rules
$$\begin{aligned} Q_{21}\zeta &= \zeta Q_{21} - Q_{22}, & Q_{22}\zeta &= \zeta Q_{22}, & Q_{12}\zeta &= \zeta Q_{12},\\ Q_{12}\bar\zeta &= \bar\zeta Q_{12} + Q_{22}, & Q_{21}\bar\zeta &= \bar\zeta Q_{21}, & Q_{22}\bar\zeta &= \bar\zeta Q_{22}\end{aligned}$$
hold at every $Y$, and every entry of $Q(Y)$ commutes with $c_l$, $\bar c_l$, $p_l$ and $\bar p_l$.

The rules in 5 say that $\zeta$ acts on the matrix $Q$ as a lowering operator: it moves $Q_{22}$ into $Q_{21}$ and $Q_{12}$, and it commutes with the rest. These are the rules that the multiplication by the coordinate $\zeta$ satisfies for the actual operators, as we see below.

### Theorem S

**Theorem 1.8.3 (Theorem S).** Let $P$ be an admissible parameter, let $L_0$ be a pre-level in $\mathcal A$, and let $(L_0, Q, \kappa)$ satisfy (SH). Then there are a level datum $L$ that extends $L_0$ and elements $S_l \in \mathcal A$ such that the datum $\mathsf d = (L, \kappa, (S_l))$ has a star level, satisfies the relations of a normal form, and $Q(Y) = Q_{\mathsf d}(Y)$ for every $Y \in \mathbb C$.

Lean: `Formalism.FourierDecayAlt.P.theorem_S_ring`

The proof has four steps. The first step finds the shape of $Q_{21}$. Put $\ell(Y) = \kappa(x_\pi(Y))^{-1} G^{-1} Q_{21}(Y)$ and $E_\rho = \kappa(\delta_\rho)$. Then the RTT relation between $Q_{22}(u)$ and $Q_{21}(v)$, evaluated at the base point $Y = i$, gives elements $b_\rho$ and $S_l$ with the block form
$$\begin{aligned} E_{\rho'}\, \ell(Y)\, E_\rho = {}& [\rho' = \rho]\bigl(b_\rho - Y \bar\zeta G^{-1}\bigr) E_\rho \\ &+ \sum_l [\rho \to_l \rho']\, (Y + \rho_l + 1)^{-1} G^{-1} S_l E_\rho. \end{aligned}$$
Here $[\cdot]$ is $1$ if the condition holds and $0$ otherwise. The diagonal blocks are linear in $Y$ by item 4. The off diagonal blocks have one pole each, at the shifted root of $x_\pi$, because $\kappa(x_\pi)$ is invertible off these points. The elements $S_l$ raise types: $\kappa(g) S_l = S_l \kappa(f)$ whenever $g(\rho') = f(\rho)$ for all $\rho \to_l \rho'$. They commute with the operators of $L_0$.

The second step defines the connection from the diagonal blocks.

**Lemma 1.8.4 (The connection).** Let $P$ be a parameter, let $(L_0, Q, \kappa)$ satisfy (SH), and let $b_\rho$ and $S_l$ give the block form above, with $S_l$ raising types and commuting with the operators of $L_0$. Put
$$\nabla = -\sum_\rho E_\rho\, b_\rho\, E_\rho - \tfrac12 \bar\zeta G^{-1}, \qquad \nabla^* = (\nabla)^*.$$
Then the level datum $L$ obtained from $L_0$ by adding $\nabla$ and $\nabla^*$ is a star level, the datum $(L, \kappa, (S_l))$ satisfies all relations of a normal form except the norm relation $S_l^* S_l = \kappa(N_l)$, and
$$Q_{21} = (Q_{\mathsf d})_{21}, \qquad Q_{12} = (Q_{\mathsf d})_{12}, \qquad Q_{22} = (Q_{\mathsf d})_{22}.$$

Lean: `Formalism.FourierDecayAlt.P.NFx2.sc_main`

*Proof.* The relations of a normal form are of three kinds. The star relations hold because $\kappa$ is star compatible, $\zeta^* = \bar\zeta$ and $G$ is hermitian; the definition of $\nabla^*$ as the star of $\nabla$ makes the level a star level. The commutation of $\kappa(f)$ and of $S_l$ with the function operators is item 3 and the hypothesis on $S_l$. The two relations
$$\nabla S_l = S_l \nabla - \bar\zeta G^{-1} S_l, \qquad \nabla^* S_l = S_l \nabla^* - \zeta G^{-1} S_l$$
come from the rules of item 5: $\bar\zeta$ commutes with $Q_{21}$, so it commutes with $\ell$ and with each block, and the $\zeta$ rule for $Q_{21}$ gives the shift by $G^{-1}$ when it is moved past $S_l$. For the entries: $(Q_{\mathsf d})_{22} = G \kappa(x_\pi)$ is item 3. Substituting $b_\rho$ from the definition of $\nabla$ into the block form gives exactly the formula of the model for $Q_{21}$ in terms of $\nabla$, $\bar\zeta$, $G$, $\kappa$ and the $S_l$. The entry $Q_{12}$ is the star of $Q_{21}$ at $\bar Y$, because $(Q, q)$ is a start, and the same holds in the model. $\square$

The third step is the norm relation. The quantum determinant $Q_{11}(Y+1)Q_{22}(Y) - Q_{21}(Y+1)Q_{12}(Y) = q(Y)$ of the start has a residue at each pole of the off diagonal blocks. Comparing residues on both sides gives $S_l^* S_l = \kappa(N_l)$, with the norms of the model. With the norm relation, the quantum determinant determines $Q_{11}$ from the other three entries, because $Q_{22}(Y)$ is invertible away from finitely many $Y$. So $Q_{11} = (Q_{\mathsf d})_{11}$. The fourth step collects the results.

*Proof.* The block form of the first step gives $b_\rho$ and $S_l$. The [Lemma 1.8.4](/entry/sc-main/) on the connection gives $L$, the relations other than the norm relation, and three entries. The residue argument of the third step gives the norm relation and the entry $Q_{11}$. Together these are the claims. $\square$

### The actual operators

Let $z, z'$ be points of the middle block with $T(z) > 0$ and $T(z') > 0$, let $\pi, \pi'$ be representations of the stabilizers, and let $\mathcal R$ be the radial space of the place. For a level $i \le r$ put $m_i = 2(r - i) + k + 1$. The *actual operators* $t_{ab}(Y)$, $a, b \in \{1, 2\}$, at level $i$ act on smooth functions on an open set of matrices. They are built from quantum minors of the right invariant derivatives (Capelli elements) and from bordered minors, with the shift $u = Y + (m_i - 1)/2$. The coordinate function $\zeta = \zeta_i$ is a matrix entry of the level, $G = \zeta\bar\zeta - T T'$ is the function of the [top unipotent integral](/entry/top-unipotent-integral/), and $X$ denotes the family of actual operators on $\mathcal R$ at the top level $i = r$, with matrix $X.Q(Y) = (t_{ab}(Y))$.

We use four properties.

- (A) For every place and every family $X$ of actual operators, $(X.Q, q)$ is a start, and the entries $t_{21}(Y)$, $t_{21}(Y')$ commute.
- (Z) At the top level, for every smooth $f$ and every $g$ in the domain,
$$\begin{aligned} t_{21}(\zeta f) &= \zeta\, t_{21} f - t_{22} f, & t_{22}(\zeta f) &= \zeta\, t_{22} f, & t_{12}(\zeta f) &= \zeta\, t_{12} f,\\ t_{12}(\bar\zeta f) &= \bar\zeta\, t_{12} f + t_{22} f, & t_{21}(\bar\zeta f) &= \bar\zeta\, t_{21} f, & t_{22}(\bar\zeta f) &= \bar\zeta\, t_{22} f. \end{aligned}$$
- (L) At each level $i$ there are operators $A_{ab, j}$ such that, with $m = m_i$,
$$\begin{aligned} t_{11}(Y) &= Y^m + \textstyle\sum_{j < m} Y^j A_{11,j}, & t_{12}(Y) &= -\zeta Y^{m-1} + \textstyle\sum_{j < m-1} Y^j A_{12,j},\\ t_{21}(Y) &= -\bar\zeta Y^{m-1} + \textstyle\sum_{j < m-1} Y^j A_{21,j}, & t_{22}(Y) &= \textstyle\sum_{j < m-1} Y^j A_{22,j}. \end{aligned}$$
- (RD) On a domain where $G \ne 0$, every equivariant function $J$ is a sum $J = \sum_\rho J_\rho$ of equivariant functions with $t_{22}(Y) J_\rho = G\, x_\rho(Y)\, J_\rho$ for every type $\rho$ and every $Y$.

Property (Z) is item 5 of (SH) for $X.Q$. Property (L) at the top level, where $m_r = k + 1$, gives item 4. Property (RD) gives the map $\kappa$: $\kappa(f)$ acts on the $\rho$ component by $f(\rho)$, so $t_{22} = G \kappa(x_\pi)$, which is item 3.

**Theorem 1.8.5 (Normal form of the actual operators).** Assume (A), (Z), (L) and (RD), and assume that actual operators exist at every place. Then for every place and every family $X$ of actual operators there is a normal form datum $\mathsf d$ on the radial space whose level is the actual level of $X$, whose level is a star level, which satisfies the relations of a normal form, and with $X.Q(Y) = Q_{\mathsf d}(Y)$ for every $Y$.

Lean: `Formalism.FourierDecayAlt.P.normalFormFromModule_statement`

*Proof.* Fix a place and $X$. The actual pre-level consists of the coordinate $\zeta$, the function $G$, the torus coordinates $c_l$ and their Wirtinger derivatives $p_l = c_l \partial_{c_l}$, $\bar p_l = \bar c_l \partial_{\bar c_l}$. These operators satisfy the star rules of item 1 for the pairing of the radial space, and the level coordinates commute with each other. The splitting (RD) and the completeness of the list of types give $\kappa$ with the properties of item 3. Then (A), (Z) and (L) give items 2, 5 and 4. The entries of $X.Q$ commute with the site operators, because the actual operators act on the variable $g$ and the site operators on the torus variable $c$. So $(L_0, X.Q, \kappa)$ satisfies (SH), and [Theorem S](/entry/theorem-s-ring/) gives $\mathsf d$. $\square$

Property (A) is proved in the [next section](/entry/actual-start/), and the remaining properties are proved by the results of the earlier chapters on the actual operators.

**Remark 1.8.6 (Formalization).** Theorem S is proved from four lemmas, one for each step; the connection lemma does not use the admissibility of $P$, and the lemmas for the first and third steps take three facts about types (interlacing, completeness, raising) that they do not use. The theorem on the actual operators takes the existence of actual operators as a hypothesis and never uses it ([InterpolationInverseMatrixSumIdentity.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/InterpolationInverseMatrixSumIdentity.lean#L139)). The four lemmas of Theorem S are assembled by a result that has two declarations of the same name in one namespace, in two files that are both imported by the file of the last theorem.
