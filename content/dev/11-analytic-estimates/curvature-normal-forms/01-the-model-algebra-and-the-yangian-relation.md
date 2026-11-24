---
title: The model algebra and the Yangian relation
decls:
  - Formalism.FourierDecayAlt.P.MAx1.ModelAlgebraRelations.generic
  - Formalism.FourierDecayAlt.P.MAx1.ModelAlgebraRelations.entries_of
  - Formalism.FourierDecayAlt.P.MAx1.qQRTTEntries
  - Formalism.FourierDecayAlt.P.MAx1.qQRTT
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The model algebra and the Yangian relation

This section sets up the model algebra of a level and the $2 \times 2$ matrix $Q(Y)$ of operators that it carries. It proves that $Q$ satisfies the defining relation of the Yangian $\mathrm{Y}(\mathfrak{gl}_2)$. The proof writes $Q(Y)$ as a product of a lower triangular, a diagonal and an upper triangular matrix at generic points, checks a list of commutation relations between the three factors, and then extends the result to all points because the entries of $Q$ are polynomials in $Y$. The relation is one of the four conditions of [the start matrix](/entry/start-is-start/), which the next section assembles. Through [the start data at a model level](/entry/start-ok/) it is used in the step [HypsAlt is nonempty](/step/nonempty-hyps/).

### Parameters and types

**Definition 1.1.1 (Parameters).** A *parameter* $P$ is a tuple $(k, r, T, T', u, u')$ with $k, r \in \mathbb{N}$, $T, T' \in \mathbb{R}$ and sequences $u, u' : \mathbb{N} \to \mathbb{R}$. Put $T_2 = T T'$ and, for $i \in \mathbb{N}$,

$$\mathrm{lo}_i = \max(u_{i+1}, u'_{i+1}) + \tfrac12, \qquad \mathrm{hi}_i = \min(u_i, u'_i) - \tfrac12,$$

and let $w_i = \lfloor \mathrm{hi}_i - \mathrm{lo}_i \rfloor$ in $\mathbb{N}$, with the convention that the floor of a negative number is $0$. The parameter is *admissible* when $k \ge 1$, $T > 0$, $T' > 0$, the numbers $u_i - u_1$ and $u'_i - u_1$ are integers for $1 \le i \le k$, and $\mathrm{lo}_i \le \mathrm{hi}_i$ for $1 \le i \le k - 1$.

**Definition 1.1.2 (Types).** A *type* of $P$ is a function $\pi$ on $\{1, \dots, k-1\}$ with $\pi_i \in \{0, 1, \dots, w_i\}$. Its *coordinates* are $\rho_i(\pi) = \mathrm{lo}_i + \pi_i$ for $1 \le i \le k-1$, and $\rho_i(\pi) = 0$ for other $i$. For $1 \le l \le k-1$ we write $\pi \to_l \pi'$ when $\pi' = \pi + e_l$, that is, $\pi'_l = \pi_l + 1$ and $\pi'_i = \pi_i$ for $i \ne l$.

For an admissible parameter the coordinates interlace: $\max(u_{i+1}, u'_{i+1}) < \rho_i < \min(u_i, u'_i)$. These are the Gelfand-Tsetlin patterns of one row between two given rows; see [highest weights and branching](/learn/representations/#highest-weights-and-branching). The following scalar functions of a type $\pi$ and of $Y \in \mathbb{C}$ appear in the entries of $Q$:

$$x_\pi(Y) = \prod_{i=1}^{k-1} (Y + \rho_i), \qquad x^{(S)}_\pi(Y) = \prod_{i \notin S} (Y + \rho_i),$$

$$q(Y) = -T_2 \prod_{i=1}^{k} \bigl(Y + \tfrac12 + u_i\bigr)\bigl(Y + \tfrac12 + u'_i\bigr),$$

$$a_\pi = \tfrac12 \sum_{i=1}^{k} (u_i + u'_i) - \sum_{i=1}^{k-1} \rho_i .$$

In $x^{(S)}$ the index $i$ runs over $\{1, \dots, k-1\} \setminus S$. The *norms* of the raising step at $l$ are the real numbers

$$N_l(\pi) = \frac{-q(-\rho_l - 1)}{\prod_{j \ne l} (\rho_j - \rho_l)(\rho_j - \rho_l - 1)},$$

$$N^-_l(\pi) = \frac{-q(-\rho_l)}{\prod_{j \ne l} (\rho_j - \rho_l + 1)(\rho_j - \rho_l)},$$

with $j$ running over $\{1, \dots, k-1\} \setminus \{l\}$ and $\rho = \rho(\pi)$. Last, $w_\pi(Y)$ is the quotient of the polynomial

$$q(X) + \sum_{l} N_l(\pi) \prod_{j \ne l} (X + \rho_j)(X + \rho_j + 1)$$

by the monic polynomial $\prod_i (X + \rho_i + 1)$, evaluated at $Y$.

### The model algebra

**Definition 1.1.3 (Model algebra).** Let $r \in \mathbb{N}$ and $T_2 \in \mathbb{R}$. A *model algebra* $D$ consists of a commutative $\mathbb{C}$-algebra $R$, elements $x_v \in R$ and $\mathbb{C}$-linear maps $E_v : R \to R$, indexed by the variables $v$, which are $z$, $\bar z$, $c_l$ and $\bar c_l$ for $l < r$. It *satisfies the laws* when:

1. each $E_v$ is a derivation, $E_v(fg) = E_v(f) g + f E_v(g)$;
2. $E_v(x_w) = x_w$ if $v = w$, and $E_v(x_w) = 0$ otherwise;
3. the maps $E_v$ commute with each other;
4. each $x_v$ is a unit of $R$, and so is $g = x_z x_{\bar z} - T_2$;
5. $R$ is a nontrivial ring.

Let $\mathrm{Op} = \mathrm{End}_{\mathbb{C}}(R)$ and let $\mathrm{Pr} = \mathrm{Op} \times \mathrm{Op}^{\mathrm{op}}$. The map $z \mapsto (z, \bar z)$ makes it a $\mathbb{C}$-algebra, and $(X, Y) \mapsto (Y, X)$ is an antilinear star. The second slot plays the part of the adjoint. Multiplication by $f$ in the first slot and by $\bar f$ in the second gives the pairs $\zeta = (x_z, x_{\bar z})$, $\bar\zeta = (x_{\bar z}, x_z)$, $G = (g, g)$ and their inverses. The derivative in $\zeta$ is the pair

$$\partial_\zeta = \bigl(x_z^{-1} E_z,\ -x_{\bar z}^{-1} E_{\bar z}\bigr),$$

and $\partial_{\bar\zeta}$ is the same with $z$ and $\bar z$ exchanged.

The *model algebra of the level* is the ring $A$ of square matrices over $\mathrm{Pr}$ whose rows and columns are indexed by the types of $P$. It is a star ring under the conjugate transpose. Write $\kappa(f)$ for the diagonal matrix with entries $f(\pi)$, for $f$ a complex function of types; $\kappa$ is a map of $\mathbb{C}$-algebras. We use the same letter for an element of $\mathrm{Pr}$ and the scalar matrix it gives.

**Definition 1.1.4 (Model operators).** The covariant derivatives are the diagonal matrices

$$\nabla = \mathrm{diag}_\pi \bigl(\partial_\zeta + a_\pi \bar\zeta G^{-1}\bigr), \qquad \nabla^* = \mathrm{diag}_\pi \bigl(-\partial_{\bar\zeta} + a_\pi \zeta G^{-1}\bigr).$$

For $l \in \mathbb{N}$ the *raising operator* $S_l \in A$ has the entry $\sqrt{N_l(\pi)}$ in row $\pi'$ and column $\pi$ when $\pi \to_l \pi'$, and $0$ in the other places. Here $\sqrt{t} = 0$ for $t < 0$.

### The matrix of a level

Put $l_0(Y) = -\nabla - (Y + \tfrac12) \bar\zeta G^{-1}$ and $m_0(Y) = -\nabla^* - (Y - \tfrac12) \zeta G^{-1}$. Let $x(Y) = \kappa(x_\pi(Y))$, $x^{(S)}(Y) = \kappa(x^{(S)}_\pi(Y))$ and put

$$\Sigma(Y) = \sum_{l} S_l\, x^{(l)}(Y), \qquad \Sigma^*(Y) = \sum_l x^{(l)}(Y)\, S_l^*,$$

$$\Sigma_4(Y) = \sum_{l} \sum_{j \ne l} S_l^* S_j\, x^{(l, j)}(Y),$$

with $l$ and $j$ in $\{1, \dots, k-1\}$.

**Definition 1.1.5 (Matrix of a level).** The matrix of the level is $Q(Y) = (Q_{ij}(Y))_{i, j = 1, 2}$ with entries

$$Q_{22} = G x, \qquad Q_{21} = G x\, l_0 + \Sigma, \qquad Q_{12} = G x\, m_0 + \Sigma^*,$$

$$\begin{aligned} Q_{11} = {} & G^{-1} \kappa(w) + G x\, m_0 l_0 + G m_0 G^{-1} \Sigma \\ & + \Sigma^* l_0 + G^{-1} \Sigma_4 , \end{aligned}$$

all taken at the same point $Y$.

At a generic point the matrix has a simple shape. Call $Y$ *good* if $Y + \rho_j(\pi) + n \ne 0$ for every type $\pi$, every $1 \le j \le k-1$ and every $n \in \{-2, -1, 0, 1, 2\}$. All but finitely many $Y$ are good. Put

$$\lambda(Y) = l_0(Y) + G^{-1} \sum_{j} \kappa\Bigl(\frac{1}{Y + \rho_j}\Bigr) S_j, \qquad \mu(Y) = \lambda(\bar Y)^*,$$

$$d(Y) = q(Y)\, G^{-1} \kappa\bigl(x_\pi(Y + 1)^{-1}\bigr), \qquad t(Y) = Q_{22}(Y).$$

When the relation (N) below holds, at a good point

$$Q(Y) = \begin{pmatrix} d + \mu t \lambda & \mu t \\ t \lambda & t \end{pmatrix} = \begin{pmatrix} 1 & \mu \\ 0 & 1 \end{pmatrix} \begin{pmatrix} d & 0 \\ 0 & t \end{pmatrix} \begin{pmatrix} 1 & 0 \\ \lambda & 1 \end{pmatrix} .$$

This is the Gauss decomposition of $Q$.

### The relations of the raising operators

The proof uses five families of relations. Each one is asked for every parameter and every model algebra that satisfies the laws; (N), (C) and (M) are asked only for admissible parameters, and $j$, $l$ run over $\{1, \dots, k-1\}$ with $j \ne l$ in (C) and (M).

- (N) $S_l^* S_l = \kappa(N_l)$ and $S_l S_l^* = \kappa(N^-_l)$.
- (C) $S_j S_l\, \kappa(\rho_j - \rho_l - 1) = S_l S_j\, \kappa(\rho_j - \rho_l + 1)$.
- (M) $S_l^* S_j = S_j S_l^*$.
- (S) $\nabla S_l = S_l \nabla - \bar\zeta G^{-1} S_l$ and $\nabla^* S_l = S_l \nabla^* - \zeta G^{-1} S_l$.
- (K) $\nabla^* \nabla - \nabla \nabla^* = \kappa(2 a_\pi T_2)\, G^{-1} G^{-1}$.

Relation (K) is the curvature of the level. All five hold in the model.

### The Yangian relation

Let $\mathcal{E}_1(M) = M \otimes 1$ and $\mathcal{E}_2(M) = 1 \otimes M$ be the two embeddings of $2 \times 2$ matrices into $4 \times 4$ matrices, and let $\mathcal{P}$ be the flip of the two tensor factors. A family $M(Y)$ of $2 \times 2$ matrices *satisfies the RTT relation* if for all $Y$ and $Y'$

$$\bigl((Y' - Y) - \mathcal{P}\bigr) \mathcal{E}_1(M(Y')) \mathcal{E}_2(M(Y))$$

equals

$$\mathcal{E}_2(M(Y)) \mathcal{E}_1(M(Y')) \bigl((Y' - Y) - \mathcal{P}\bigr).$$

This is the defining relation of the Yangian of $\mathfrak{gl}_2$. In entries, with $u = Y'$ and $v = Y$, it says

$$\begin{aligned} (u - v)\bigl[M_{ij}(u), M_{kl}(v)\bigr] = {} & M_{kj}(u) M_{il}(v) \\ & - M_{kj}(v) M_{il}(u) . \end{aligned} \tag{R}$$

**Theorem 1.1.6 (Yangian relation at good points).** Assume (N), (C), (M), (S) and (K). Let $P$ be an admissible parameter, let $D$ be a model algebra that satisfies the laws, and let $u$, $v$ be good points with $u - v \notin \{0, 1, -1\}$. Then the matrix $Q$ of the level satisfies (R) at $u$ and $v$ for all $i, j, k, l \in \{1, 2\}$.

Lean: `Formalism.FourierDecayAlt.P.MAx1.ModelAlgebraRelations.generic`

*Proof.* Write $\delta = u - v$, and put $t = t(u)$, $t' = t(v)$, and in the same way $d, d'$, $\lambda, \lambda'$ and $\mu, \mu'$. By the Gauss decomposition both $Q(u)$ and $Q(v)$ have the triangular shape above. A direct expansion shows that (R) holds for matrices of this shape in any ring, as soon as $\delta \ne 0, \pm 1$ and the factors satisfy these relations:

1. $t$ and $t'$ commute, $d$ and $d'$ commute, $d'$ commutes with $t$, and $d$ commutes with $t'$;
2. $\delta[t, \lambda'] = -t(\lambda - \lambda')$ and $\delta[t', \lambda] = -t'(\lambda - \lambda')$;
3. $\delta[d, \lambda'] = d(\lambda - \lambda')$ and $\delta[d', \lambda] = d'(\lambda - \lambda')$;
4. $\delta[t, \mu'] = (\mu - \mu')t$ and $\delta[t', \mu] = (\mu - \mu')t'$;
5. $\delta[d, \mu'] = -(\mu - \mu')d$ and $\delta[d', \mu] = -(\mu - \mu')d'$;
6. $\delta[\lambda, \lambda'] = (\lambda - \lambda')^2$ and $\delta[\mu, \mu'] = -(\mu - \mu')^2$;
7. $\delta(t' \mu \lambda' t - t' \lambda' \mu t) = d' t - t' d$, and the same with the roles of $u$ and $v$ exchanged.

In the expansion one uses the relations of items 2 to 5 to move $t$, $t'$, $d$, $d'$ to one side, and divides by $\delta$, $\delta - 1$ and $\delta + 1$.

Items 1 to 5 follow from the laws alone. The elements $t$, $d$, $t'$, $d'$ are $G^{\pm 1}$ times diagonal scalar matrices, so they commute. In item 2 the commutator of $G x(u)$ with $\lambda(v)$ comes from the commutator of $G$ with the derivative in $\nabla$, and from the factor $1/(v + \rho_j)$ in $\lambda(v)$, which changes to $1/(v + \rho_j + 1)$ when $S_j$ moves past a diagonal matrix. The second form of each item comes from the first by exchanging $u$ and $v$ and multiplying by $-1$. The first part of item 6 uses (C) and (S). The second part also uses (C) and (S), through the star of the first part. Item 7 is the only place where the five families meet. It uses (N), (M), (S) and (K): the product $\mu \lambda'$ contains $\nabla^* \nabla$, the product $\lambda' \mu$ contains $\nabla \nabla^*$, and (K) turns their difference into a diagonal term. The terms $S^*_j S_l$ with $j \ne l$ cancel by (M), and the terms $S_l^* S_l$ and $S_l S_l^*$ become $\kappa(N_l)$ and $\kappa(N^-_l)$ by (N). What is left are scalar identities between rational functions of $u$ and $v$ with poles at $-\rho_j$ and $-\rho_j - 1$. They follow from the partial fraction expansion of $q(Y) / (x_\pi(Y) x_\pi(Y + 1))$: its residue at $Y = -\rho_l - 1$ is $N_l(\pi)$, and its residue at $Y = -\rho_l$ is $-N^-_l(\pi)$. $\square$

**Theorem 1.1.7 (Yangian relation in entries, from the relations).** Assume (N), (C), (M), (S) and (K). For every admissible parameter $P$, every model algebra $D$ that satisfies the laws, every $u, v \in \mathbb{C}$ and all $i, j, k, l \in \{1, 2\}$, the matrix $Q$ of the level satisfies (R).

Lean: `Formalism.FourierDecayAlt.P.MAx1.ModelAlgebraRelations.entries_of`

*Proof.* Fix $i, j, k, l$ and let $F(u, v)$ be the left side of (R) minus the right side. The entries of $Q(Y)$ are polynomials in $Y$ with coefficients in $A$, so $F$ is a polynomial in $u$ for fixed $v$, and a polynomial in $v$ for fixed $u$. The set $B$ of points that are not good is finite. Fix a good point $v$. By the previous theorem $F(u, v) = 0$ for all $u$ outside the finite set $B \cup \{v, v + 1, v - 1\}$. A polynomial with coefficients in a complex vector space that vanishes at infinitely many points is zero, so $F(u, v) = 0$ for all $u$. Now fix any $u$. Then $F(u, v) = 0$ for all $v \notin B$, and the same argument gives $F(u, v) = 0$ for all $v$. $\square$

**Theorem 1.1.8 (Yangian relation in entries).** For every admissible parameter $P$, every model algebra $D$ that satisfies the laws, every $u, v \in \mathbb{C}$ and all $i, j, k, l \in \{1, 2\}$, the matrix $Q$ of the level satisfies (R).

Lean: `Formalism.FourierDecayAlt.P.MAx1.qQRTTEntries`

*Proof.* The five relations (N), (C), (M), (S) and (K) are proved in the model. Each is a computation with the entries of $S_l$ and $\nabla$: (N) and (C) reduce to properties of the numbers $N_l$, such as $N_l \ge 0$ on types and $N^-_l(\pi + e_l) = N_l(\pi)$, (M) holds because $S_l^* S_j$ and $S_j S_l^*$ have the same nonzero entries for $j \ne l$, (S) holds because $\partial_\zeta$ commutes with scalar matrices and $a_{\pi + e_l} = a_\pi - 1$, and (K) is the commutator of $\partial_\zeta$ and $\partial_{\bar\zeta}$ with the multiplication by $\bar\zeta G^{-1}$ and $\zeta G^{-1}$. The previous theorem then gives the claim. $\square$

**Theorem 1.1.9 (Yangian relation).** For every admissible parameter $P$ and every model algebra $D$ that satisfies the laws, the matrix $Q$ of the level satisfies the RTT relation.

Lean: `Formalism.FourierDecayAlt.P.MAx1.qQRTT`

*Proof.* Both sides of the RTT relation are $4 \times 4$ matrices with rows and columns indexed by pairs. Compare the entries in row $(i, k)$ and column $(j, l)$. The entry of $\mathcal{E}_1(M) \mathcal{E}_2(N)$ there is $M_{ij} N_{kl}$, and the entry of $\mathcal{E}_2(N) \mathcal{E}_1(M)$ is $N_{kl} M_{ij}$. Multiplication by $\mathcal{P}$ on the left exchanges $i$ and $k$, and on the right exchanges $j$ and $l$. With $u = Y'$ and $v = Y$ the entry equation is (R) after a rearrangement, and the previous theorem gives (R). $\square$

**Remark 1.1.10 (Formalization).** The Gauss argument is a separate lemma for $2 \times 2$ matrices over any ring, at `HermitianCurvatureProofs/CoordinateCommuteRaisingConstant.lean:1987`; two of its hypotheses carry names that do not match their content (`TwistedContraction` and `E2VanishingOtherColumns`, lines 1990 and 1991), while the others are numbered. The admissibility condition asks $u'_i - u_1 \in \mathbb{Z}$, comparing $u'$ with $u_1$ and not with $u'_1$ (`StatementM.lean:111`). The function $w_\pi$ is defined by division by a monic polynomial, which drops the remainder (`StatementM.lean:205`); the remainder is zero because the numerator vanishes at each root $-\rho_l - 1$ by the choice of $N_l$, and the definition does not record this.
