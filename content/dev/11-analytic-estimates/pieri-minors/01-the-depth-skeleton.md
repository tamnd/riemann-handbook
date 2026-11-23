---
title: Weyl lattices and the depth skeleton
decls:
  - Formalism.CohomologicalDescent.BinaryFormsExample.depth_skeleton_second_form_holds
  - Formalism.CohomologicalDescent.BinaryFormsExample.depth_skeleton_valuation_holds
  - Formalism.CohomologicalDescent.BinaryFormsExample.depth_skeleton_literal_holds
  - Formalism.CohomologicalDescent.BinaryFormsExample.depth_skeleton_third_form_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Weyl lattices and the depth skeleton

Let $V$ be a representation of $\mathfrak{gl}_{p+q}$ over a field of characteristic zero, and let $W \subseteq V$ be the space of vectors that the first $p$ coordinates see only through a scalar. Inside $V$ there are two integral forms: the lattice $\Delta$ generated from an integral lattice $L \subseteq W$ by divided powers of lowering operators, and its dual $\Delta^\vee$. In general $\Delta \subsetneq \Delta^\vee$. This section proves that a vector of $\Delta^\vee$ of a given weight lands in $\Delta$ after multiplication by $l^{e + v_l(D_n)}$, where $e$ is the exponent that works inside $W$ and $D_n$ is an explicit product over the contents of the Young diagrams that the Pieri rule allows. This is the "depth skeleton". Section 2 applies it to the Weyl modules of $\mathrm{GL}_{p+q}$ over $\mathbb{Q}$, and the result feeds the lattice inclusions of Sections 3 and 4.

We use [partitions and Young diagrams](/learn/combinatorics/#partitions-and-young-tableaux), [the Pieri rule](/learn/combinatorics/#the-pieri-and-littlewood-richardson-rules), [binomial coefficients and divided powers](/learn/combinatorics/#binomial-coefficients-factorials-and-divided-powers) and [highest weights](/learn/representations/#highest-weights-and-branching).

**Definition 4.1.1 (Shapes of depth $i$ and the number $D_n$).** Let $p, w, i, q \geq 0$ be integers and let $\lambda_2 = (\lambda_2(0), \dots, \lambda_2(q-1))$ be a sequence of natural numbers. For a second sequence $\tau$ with $\lambda_2 \leq \tau$, the *column length* of $\tau/\lambda_2$ at $j \geq 0$ is the number of rows $a$ with $\lambda_2(a) \leq j < \tau(a)$. The boxes of $\tau/\lambda_2$ of *content* $c \in \mathbb{Z}$ are the rows $a$ with $\lambda_2(a) \leq c + a < \tau(a)$. The set $\mathrm{Sh}(p, w, i, \lambda_2)$ consists of the $\tau$ with:

1. $\lambda_2(a) \leq \tau(a) \leq \lambda_2(a) + i$ for all $a$, $\tau$ is non-increasing, and $\sum_a \tau(a) = \sum_a \lambda_2(a) + i$;
2. every column of $\tau/\lambda_2$ that meets a row of $\tau$ has length at most $p$;
3. $\tau/\lambda_2$ has no box of content $w$.

The set $\mathrm{Sh}^{\mathrm{all}}(p, i, \lambda_2)$ is defined by conditions 1 and 2 only. Let $\mu(c)$ be the largest number of boxes of content $c$ in a shape $\tau \in \mathrm{Sh}(p, w, i, \lambda_2)$ (and $0$ if the set is empty). Then
$$D_n(p, w, i, \lambda_2) = \prod_{c = -q}^{w + i - 1} (w - c)^{\mu(c)} \in \mathbb{Z}.$$

When $\lambda_2$ is a partition, condition 1 says that $\tau/\lambda_2$ is a skew diagram with $i$ boxes, and condition 2 says that it has at most $p$ boxes in each column. For $p = 1$ these are the horizontal strips of the Pieri rule. Condition 3 removes the shapes on which the factor $w - c$ with $c = w$ would vanish. The factor $(w - c)$ is never zero in the product, so $D_n \neq 0$. For $q = 1$ and $\lambda_2 = (y)$ with $y \leq w$, the only shape is $\tau = (y + i)$, provided $y + i \leq w$; its contents are $y, \dots, y + i - 1$, and $D_n = (w - y)(w - y - 1) \cdots (w - y - i + 1) = i! \binom{w - y}{i}$.

**Definition 4.1.2 (Depth setting).** Let $O$ be a commutative ring, $K$ a field of characteristic zero with an $O$-algebra structure, and $V$ a $K$-vector space with a compatible $O$-module structure. Let $P$ be a finite set with $p$ elements and put $R = \{0, \dots, q-1\}$. A *depth setting* consists of:

1. operators $E_{ab} \in \mathrm{End}_K(V)$ for $a, b \in P \sqcup R$ with $[E_{ab}, E_{cd}] = \delta_{bc} E_{ad} - \delta_{da} E_{cb}$;
2. a subspace $W \subseteq V$ and a scalar $w \in K$ such that, for $u \in W$, $E_{\alpha a} u = 0$ for $\alpha \in P$, $a \in R$, $E_{\alpha \beta} u = \delta_{\alpha\beta}\, w u$ for $\alpha, \beta \in P$, and $E_{b b'} u \in W$ for $b, b' \in R$.

Put $f_{(b, \alpha)} = E_{b\alpha}$ for $(b, \alpha) \in R \times P$. Let $T_n(W)$ be the space of maps $z$ from words $g = (g_1, \dots, g_n)$ in $R \times P$ to $W$, and define $\mu_n : T_n(W) \to V$ by $\mu_n(z) = \sum_g f_{g_1} \cdots f_{g_n} z(g)$. For a multiset $m$ of size $n$ on $R \times P$, let $f^m$ be the product of the $f_v$ over $m$ and let $m!$ be the product of the factorials of the multiplicities. For an $O$-submodule $L \subseteq W$, let $\Delta_n(L)$ be the $O$-span of the vectors $f^m u / m!$ with $|m| = n$ and $u \in L$, and let $\Delta(L) = \sum_n \Delta_n(L)$. For $\kappa : P \sqcup R \to \mathbb{Z}$, the weight space $V_\kappa$ is the common kernel of the $E_{aa} - \kappa(a)$. For a bilinear form $B$ on $V$, $L^\vee \subseteq W$ is the set of $u \in W$ with $B(u, L) \subseteq O$, and $\Delta(L)^\vee \subseteq V$ is the set of $v$ with $B(\Delta(L), v) \subseteq O$.

The model is $V = \nabla(\lambda)$, $W$ its part of weight $w$ on the first $p$ coordinates, and $f_{(b,\alpha)}$ the lowering operators from the first block to the second. The lattice $\Delta(L)$ is the Kostant-type lattice generated by divided powers, and $\Delta(L)^\vee$ is its dual. On $T_n(W)$ there are Jucys-Murphy operators $x_1, \dots, x_n$ built from the $E_{b b'}$ on $W$ and the transpositions of the word, and $A(X) = \prod_j (X - x_j)$ is a polynomial with operator coefficients. For a shape $\tau \geq \lambda_2$, put $s_\tau(X) = \prod_a \prod_{\lambda_2(a) \leq j < \tau(a)} (X - (j - a))$.

**Definition 4.1.3 (Inputs of the skeleton).** Fix $n, w \in \mathbb{N}$, $\lambda_2 : R \to \mathbb{N}$, an $O$-submodule $L \subseteq W$, a family $M_\tau$ of subspaces of the symmetric tensors, an additive map $\xi : \mathbb{Z}^{P \sqcup R} \to \mathbb{Z}$, a weight $\lambda$, an element $l \in O$, $e \in \mathbb{N}$ and $i' \in \mathbb{Z}$. The *inputs* of the skeleton are:

1. the scalar of the setting is $w$, and $\lambda_2(b) \leq w$ for all $b$;
2. $B(E_{ab} x, y) = B(x, E_{ba} y)$ for all $a, b, x, y$, $V$ is generated by $W$ under the $E_{ab}$, and $B$ is nondegenerate on the right;
3. $L$ is stable under the $E_{b b'}$ for $b, b' \in R$;
4. (eigenvalues) on the symmetrization of $M_\tau$, for $\tau \in \mathrm{Sh}^{\mathrm{all}}(p, n, \lambda_2)$, the coefficient of $X^a$ in $A(X)$ acts by the coefficient of $X^a$ in $s_\tau(X)$, for $a < n$;
5. (decomposition) the $M_\tau$ for $\tau \in \mathrm{Sh}^{\mathrm{all}}(p, n, \lambda_2)$ span everything;
6. $\xi(e_\alpha - e_b) \geq 0$ for $\alpha \in P$ and $b \in R$;
7. for each $\kappa$ with $\xi(\lambda - \kappa) \leq i'$ and each $u \in L^\vee \cap V_\kappa$, $l^e u \in L$.

The *third inputs* replace items 4 and 5 by a Pieri condition and a column condition. For a path $\lambda_2 = \kappa_0 \subset \kappa_1 \subset \dots \subset \kappa_n = \tau$ that adds one box at a time and stays non-increasing, the path space is spanned by the $z \in T_n(W)$ on which the partial Casimir operators $C_j$ act by $\sum_b \kappa_j(b)(\kappa_j(b) + q - 1 - 2b)$ for $j \leq n$. Then:

4'. (Pieri) the path spaces for all $\tau$ span $T_n(W)$;
5'. (columns) the symmetrization kills the path space of $\tau$ when some column of $\tau/\lambda_2$ has more than $p$ boxes.

**Theorem 4.1.4 (Depth skeleton, second form).** Assume the inputs of the skeleton. Let $\nu$ be a weight with $\xi(\lambda - \nu) \leq i'$, and let $v \in \Delta(L)^\vee \cap \mu_n(T_n(W)) \cap V_\nu$. Put $D = D_n(p, w, n, \lambda_2)$. Then $l^e D\, v \in \Delta_n(L)$. If $D = \eta\, l^a$ with $\eta \in O^\times$, then $l^{e + a} v \in \Delta_n(L)$.

Lean: `Formalism.CohomologicalDescent.BinaryFormsExample.depth_skeleton_second_form_holds`.

*Proof.* The coefficients of $A(X)$ commute and act on each $M_\tau$ by the scalars of $s_\tau$. Over the integers, $s_\tau$ divides the polynomial $\prod_c (X - c)^{\mu(c)}$ for each good shape $\tau$, and the value of this polynomial at $X = w$ is $D$. For a shape with a box of content $w$, $s_\tau(w) = 0$, so $A(w)$ moves every tensor into the sum of the good parts. By division there is an operator $Q$, a polynomial with coefficients in $O$ in the coefficients of $A$, with $D\, m = A(w) Q\, m$ on the sum of the $M_\tau$. Let $\iota_n(v)$ be the tensor of divided raising operators $e^m v / m!$. A computation with the commutation relations gives $\iota_n(\mu_n z) = $ the symmetrization of $A(w) z$. The components of $\iota_n(v)$ lie in $L^\vee$ because $v \in \Delta(L)^\vee$ and $B$ is contragredient; they have weights $\nu + \beta(m)$, and item 6 gives $\xi(\lambda - \nu - \beta(m)) \leq i'$. So $Q$ keeps them in $L^\vee$ at depth at most $i'$, and item 7 moves $l^e Q \iota_n(v)$ into $L$. Applying $A(w)$ to a tensor with values in $L$ gives $\iota_n$ of an element of $\Delta_n(L)$. Since $\iota_n$ is injective on the image of $\mu_n$ (the form is nondegenerate and $V$ is generated by $W$), $l^e D\, v \in \Delta_n(L)$. For the second claim, $\eta^{-1}$ is in $O$, so $l^{e+a} v = \eta^{-1} l^e D v \in \Delta_n(L)$. $\square$

**Corollary 4.1.5 (Valuation form).** Let $l$ be a prime number such that every integer prime to $l$ is a unit in $O$. Assume the inputs of the skeleton with the element $l \in O$. Let $\nu$ and $v$ be as in the second form. Then $l^{e + v_l(D_n(p, w, n, \lambda_2))} v \in \Delta_n(L)$.

Lean: `Formalism.CohomologicalDescent.BinaryFormsExample.depth_skeleton_valuation_holds`.

*Proof.* Write $D = D_n(p, w, n, \lambda_2) = \eta\, l^a$ with $a = v_l(D)$ and $\eta \in \mathbb{Z}$ prime to $l$; this uses $D \neq 0$. Then $\eta$ is a unit of $O$, and the second claim of the [second form](/entry/depth-skeleton-second-form-holds/) gives the result. $\square$

**Lemma 4.1.6 (Depth of a weight).** In a depth setting with scalar $w \in \mathbb{N}$ where $V$ is generated by $W$, let $v \in V_\nu$ with $\sum_{\alpha \in P} \nu(\alpha) + n = p w$. Then $v \in \mu_n(T_n(W))$.

Lean: `Formalism.CohomologicalDescent.BinaryFormsExample.depth_of_weight_holds`.

*Proof.* The operator $H = \sum_{\alpha \in P} E_{\alpha\alpha}$ acts on $W$ by $p w$, and each $f_{(b,\alpha)}$ lowers its eigenvalue by $1$. So $\mu_n(T_n(W))$ lies in the $H$-eigenspace for $p w - n$. Since $V$ is generated by $W$ and the raising operators $E_{\alpha b}$ kill $W$, $V$ is the sum of the $\mu_n(T_n(W))$ over $n$. These sums lie in distinct eigenspaces, so the eigenspace for $p w - n$ is exactly $\mu_n(T_n(W))$, and it contains $v$. $\square$

**Corollary 4.1.7 (Literal form).** Let $l$ be a prime number such that every integer prime to $l$ is a unit in $O$, and assume the inputs of the skeleton. Let $\nu$ be a weight with $\sum_{\alpha \in P} \nu(\alpha) + n = p w$ and $\xi(\lambda - \nu) \leq i'$, and let $v \in \Delta(L)^\vee \cap V_\nu$. Put $N = e + v_l(D_n(p, w, n, \lambda_2))$. Then $l^N v \in \Delta(L)$ and $l^N v \in V_\nu$.

Lean: `Formalism.CohomologicalDescent.BinaryFormsExample.depth_skeleton_literal_holds`.

*Proof.* The weight condition and the lemma on the depth of a weight put $v$ in $\mu_n(T_n(W))$. Then the [valuation form](/entry/depth-skeleton-valuation-holds/) gives $l^N v \in \Delta_n(L) \subseteq \Delta(L)$. A weight space is a subspace, so $l^N v \in V_\nu$. $\square$

**Theorem 4.1.8 (Depth skeleton, third form).** Let $l$ be a prime number such that every integer prime to $l$ is a unit in $O$, and assume the third inputs of the skeleton (items 1 to 3, 4', 5', 6 and 7). Let $\nu$ be a weight with $\sum_{\alpha \in P} \nu(\alpha) + n = p w$ and $\xi(\lambda - \nu) \leq i'$, and let $v \in \Delta(L)^\vee \cap V_\nu$. Put $N = e + v_l(D_n(p, w, n, \lambda_2))$. Then $l^N v \in \Delta(L)$ and $l^N v \in V_\nu$.

Lean: `Formalism.CohomologicalDescent.BinaryFormsExample.depth_skeleton_third_form_holds`.

*Proof.* We show that the third inputs give the inputs of the skeleton, with $M_\tau$ the symmetrization of the path space of $\tau$. Items 1 to 3, 6 and 7 are the same. For item 4: the difference $C_{j+1} - C_j$ of partial Casimir operators is $2 x_{j+1}$ plus a constant. On a vector of the path space, each $C_j$ acts by the Casimir value of $\kappa_j$, so $x_{j+1}$ acts by the content $\kappa_j(\rho_j) - \rho_j$ of the box added at step $j$. So $A(X)$ acts by $\prod_j (X - \text{content of box } j) = s_\tau(X)$. For item 5: the path spaces span $T_n(W)$ by item 4', and item 5' kills those with a column longer than $p$ after symmetrization; what remains is the span of the $M_\tau$ for $\tau \in \mathrm{Sh}^{\mathrm{all}}(p, n, \lambda_2)$. The [literal form](/entry/depth-skeleton-literal-holds/) then applies. $\square$

**Example 4.1.9 (A sharp case of rank one).** Take $P$ and $R$ with one element each, $\lambda_2 = (y)$, $w = y + d$ with $d \geq 1$, $n = 1$ and $e = 0$. Then $D_1(1, y + d, 1, (y)) = d$. For an injective map $O \to K$, there is a depth setting satisfying the inputs for every $l$, with a vector $v \in \Delta(L)^\vee \cap \mu_1(T_1(W)) \cap V_\nu$ such that $c\, v \in \Delta_1(L)$ if and only if $d \mid c$ in $O$. So the factor $D_n$ in the second form cannot be made smaller in general.

**Remark 4.1.10 (Formalization).** The four results are proved in [BinaryFormsExample.lean](lean:Formalism/PieriBlockIdeals/PieriColumnMinors/BinaryFormsExample.lean#L382); the module name does not describe its content. The core of the second form is `lemma_d_skeleton_holds` in Symmetrization.lean, which we summarize and do not reprove step by step; the divisibility $s_\tau \mid \prod_c (X - c)^{\mu(c)}$ is `shape_divisibility_field`. We did not unfold the operators `Om`, `unitY`, `permY` behind the Jucys-Murphy elements beyond their defining sums. The example of rank one is `GL2PieriInstance`, an input statement in LemmaDSkeletonUnit.lean, proved in the same file as the four results. In rank two with $\lambda_2 = (y)$ and $p = 1$, the exact divisor is $\binom{w - y}{i}$ while $D_n = i!\binom{w-y}{i}$, so $D_n$ is not sharp there for $i \geq 2$.
