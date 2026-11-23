---
title: Definite pairs and marked pairs
decls:
  - GlobalTheory.LKDef.cls_equiv_dcls_irr
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Definite pairs and marked pairs

This section sets up the objects of the chapter: a unitary datum, the term of a pair, definite pairs and marked pairs. Its theorem is a bijection between two sets of classes. On one side are the classes of marked pairs whose polynomial is irreducible and whose mark is a chosen root of that polynomial. On the other side are the classes of definite pairs whose polynomial is irreducible. The bijection keeps the polynomial and the term. The [weighted count](/entry/weighted-count-definite-unitary/) uses it to move a sum over marked pairs to a sum over definite pairs, and the rest of this chapter works with definite pairs only.

### The unitary datum

**Definition 6.1.1 (Unitary datum).** Let $p$ be a prime. A *unitary datum* $\mathsf{G}$ consists of the following.

- A CM field $F$ ([kinds of number fields](/learn/number-fields/#kinds-of-number-fields)) and a subfield $E \subseteq F$ of degree $2$ over $\mathbb{Q}$ such that, for each embedding $\tau \colon F \to \mathbb{C}$, some $x \in E$ has $\operatorname{Im} \tau(x) \neq 0$.
- An integer $n > 0$ and a central simple $F$-algebra $C$ of dimension $n^2$, with an anti-automorphism $x \mapsto x^*$ of order $2$ that restricts to complex conjugation on $F$.
- For each infinite place $v$ of $F$, a ring map $\psi_v \colon C \to M_n(\mathbb{C})$ that is the scalar map $v$ on $F$, and an invertible [[Hermitian|0EKZCX4K3P]] matrix $H_v$ with $\psi_v(x^*) = H_v^{-1} \psi_v(x)^{\dagger} H_v$, where $\dagger$ is the conjugate transpose. The signature of $H_v$ is $(1, n-1)$ or $(0, n)$.
- Places $w_1, \dots, w_m$ of $F$ above $p$, with completions $F_{w_i}$, and ring maps $\rho_i \colon C \to M_n(F_{w_i})$ that are the scalar map on $F$.

Let $a$ be the number of infinite places $v$ at which $H_v$ has signature $(1, n-1)$.

For a commutative $\mathbb{Q}$-algebra $R$, extend the involution to $R \otimes_{\mathbb{Q}} C$ by $(r \otimes x)^* = r \otimes x^*$, and let
$$G(R) = \{ (g, \nu) \in (R \otimes_{\mathbb{Q}} C)^\times \times R^\times : g g^* = \nu \}.$$
This is the group of [[unitary similitudes|0R9R0Y1HDK]] of $C$ ([unitary groups](/learn/groups/#unitary-groups)). Let $\mathbb{A}^p$ be the restricted product of the fields $\mathbb{Q}_\ell$, $\ell \neq p$, with respect to the rings $\mathbb{Z}_\ell$ ([adeles](/learn/number-fields/#adeles-and-ideles)). A *level* is an open subgroup $K^p$ of $G(\mathbb{A}^p)$ that is compact ([adelic points](/learn/groups/#adelic-points-and-compact-open-subgroups)).

At $p$, let $\mathbb{Q}_{p^r}$ be the unramified extension of $\mathbb{Q}_p$ of degree $r$ and $\sigma$ its Frobenius. Let
$$G_r = \mathrm{GL}_1(\mathbb{Q}_{p^r}) \times \prod_{i=1}^m \mathrm{GL}_n(F_{w_i} \otimes_{\mathbb{Q}_p} \mathbb{Q}_{p^r}),$$
with $\sigma$ acting on the coefficients, and let $K_r \subseteq G_r$ be its subgroup of integral points. Let $G_p = \mathbb{Q}_p^\times \times \prod_i \mathrm{GL}_n(F_{w_i})$, included in each $G_r$, and $\lambda \colon C^\times \times \mathbb{Q}^\times \to G_p$ the map $(y, s) \mapsto (s, (\rho_i(y))_i)$. The norm of $\delta \in G_r$ is $N_r \delta = \delta\, \sigma(\delta) \cdots \sigma^{r-1}(\delta)$.

### Test functions and point sums

In this chapter a sum $\sum$ over an infinite set is the finite sum of its nonzero terms if there are finitely many of them, and $0$ otherwise. For a set $S$, $|S|^{-1}$ is $0$ if $S$ is infinite.

**Definition 6.1.2 (Test function).** Let $H$ be a group, $\theta$ an endomorphism of $H$ and $K_0, K$ subgroups. A function $\varphi \colon H \to \mathbb{C}$ is a *test function for $(\theta, K_0, K)$* if $K$ is commensurable with $K_0$, $\theta(K) \subseteq K$, $\varphi(k^{-1} g\, \theta(k)) = \varphi(g)$ for all $k \in K$ and $g \in H$, and there is a finite set $S \subseteq H$ such that $\varphi(g) \neq 0$ implies $g \in K_0 s K_0$ for some $s \in S$.

Lean: `GlobalTheory.LKMid.IsTest`.

**Definition 6.1.3 (Point sum).** Let $\Gamma, G_1, G_2$ be groups, $\iota_j \colon \Gamma \to G_j$ homomorphisms, $\theta$ an endomorphism of $G_2$, $K_j \subseteq G_j$ subgroups, $\gamma_1 \in G_1$, $\delta \in G_2$, and $f_1 \colon G_1 \to \mathbb{C}$, $\varphi \colon G_2 \to \mathbb{C}$. For $x = (x_1, x_2) \in G_1 \times G_2$ let $\mathrm{St}(x) = \{ h \in \Gamma : \iota_1(h) \in x_1 K_1 x_1^{-1},\ \iota_2(h) \in x_2 K_2 x_2^{-1} \}$. The *point sum* is
$$\Sigma = \sum_{[x]} |\mathrm{St}(x)|^{-1}\, f_1(x_1^{-1} \gamma_1 x_1)\, \varphi(x_2^{-1} \delta\, \theta(x_2)),$$
over the double cosets $[x] \in (\iota_1 \times \iota_2)(\Gamma) \backslash (G_1 \times G_2) / (K_1 \times K_2)$, each with a fixed representative $x$.

Lean: `GlobalTheory.LKCount.pointSum`.

### Definite pairs and their terms

**Definition 6.1.4 (Definite pair).** A *definite pair* is a triple $P = (\beta, \gamma, c)$ with $\beta, \gamma \in C^\times$ and $c \in \mathbb{Q}^\times$ such that:

1. $\beta^* = \beta$ and $\gamma \beta \gamma^* = c \beta$;
2. the minimal polynomial $P_\gamma$ of $\gamma$ over $F$ has degree $n$ and is separable;
3. there are $x \in (\mathbb{A}^p \otimes C)^\times$ and $t \in (\mathbb{A}^p)^\times$ with $x \beta x^* = t$ (a *trivialization* $(x, t)$);
4. for each infinite place $v$ and each $u \in \mathbb{C}^n$, $u \neq 0$, the real part of $u^\dagger H_v \psi_v(\beta^{-1}) u$ is positive if $H_v$ has signature $(1, n-1)$ and negative otherwise.

Lean: `GlobalTheory.LKDef.DPair`.

Condition 4 says that the Hermitian form of $\beta^{-1}$ is [[positive definite|0KX66CZMBB]] at the places of signature $(1, n-1)$ and negative definite at the others. Two definite pairs $P, Q$ are *related*, $P \sim Q$, if there are $y \in C^\times$ and $s \in \mathbb{Q}$, $s > 0$, with $\beta_Q = s\, y \beta_P y^*$ and $\gamma_Q = y \gamma_P y^{-1}$. This is an equivalence relation. Related pairs have the same polynomial, since conjugate elements have the same minimal polynomial. They have the same $c$: from $\gamma_Q \beta_Q \gamma_Q^* = s\, y \gamma_P \beta_P \gamma_P^* y^* = c_P \beta_Q$ we get $c_Q = c_P$. We write $[P]$ for the class of $P$ and fix a representative of each class.

**Definition 6.1.5 (Term).** Let $P$ be a definite pair. Let $Z_P = \{ (y, s) \in C^\times \times \mathbb{Q}^\times : y\gamma = \gamma y,\ y \beta y^* = s \beta \}$; it contains $(\gamma, c)$. A trivialization $(x, t)$ gives $\iota_x \colon Z_P \to G(\mathbb{A}^p)$, $(y, s) \mapsto (x y x^{-1}, s)$, and $z \in G_r$ gives $\iota_z \colon Z_P \to G_r$, $(y, s) \mapsto z^{-1} \lambda(y, s) z$. Let $K^p \subseteq G(\mathbb{A}^p)$ and $K \subseteq G_r$ be subgroups and $f \colon G(\mathbb{A}^p) \to \mathbb{C}$, $\varphi \colon G_r \to \mathbb{C}$. If there are $\delta, z \in G_r$ with $N_r \delta = z^{-1} \lambda(\gamma, c) z$, fix such $\delta, z$ and a trivialization $(x, t)$, and let $T(P)$ be the point sum for $\Gamma = Z_P$, $\iota_x$, $\iota_z$, $\theta = \sigma$, $K^p$, $K$, $\gamma_1 = \iota_x(\gamma, c)$, $\delta$, $f$ and $\varphi$. If there are none, $T(P) = 0$.

Lean: `GlobalTheory.LKDef.DPair.term`.

We write $T(P) = T(P; K^p, f, r, K, \varphi)$ when the data matter. The term has the shape of the contribution of one rational class to a count of points in the method of Kottwitz (see the Notes and references). The [trace identity](/entry/lkdef-trace-definite-forms-identity/) uses $r = 1$.

**Example 6.1.6.** Let $F = \mathbb{Q}(i)$ with $E = F$, $n = 1$, $C = F$ with complex conjugation, and $H_v = 1$ at the one infinite place, so $a = 1$. Then $(\beta, \gamma, c) = (1, 2 + i, 5)$ is a definite pair: $\gamma \gamma^* = 5$, $P_\gamma = X - (2 + i)$, and $(x, t) = (1, 1)$ is a trivialization.

### Marked pairs

**Definition 6.1.7 (Pair and mark).** A *pair* is a triple $P = (\beta, \gamma, c)$ with conditions 1 to 3 of a definite pair, and with some $z \in (\mathbb{R} \otimes C)^\times$ with $z \beta z^* = 1$. It is *marked* by $\mu \in \mathbb{C}$ if there are an infinite place $v$ with $H_v$ of signature $(1, n-1)$ and $u \in \mathbb{C}^n$ with $\psi_v(\gamma) u = \mu u$ and $\operatorname{Re}(u^\dagger H_v \psi_v(\beta^{-1}) u) > 0$. A *selection* is a map $\mathrm{sel} \colon F[X] \to \mathbb{C}$ such that $\mathrm{sel}(P_0)$ is a root of $v(P_0)$ for each monic $P_0$ of degree $n$ and each infinite place $v$ with $H_v$ of signature $(1, n-1)$.

Lean: `GlobalTheory.LKMid.Pair` (also `GlobalTheory.LKMid.Pair.Mark`, the mark, and `GlobalTheory.LKMid.IsSel`, the selection).

The relation $\sim$, the polynomial $P_\gamma$, the group $Z_P$ and the term $T(P)$ are defined for pairs by the same formulas.

**Lemma 6.1.8 (Marks of related pairs).** If $P \sim Q$ are pairs and $\mu \in \mathbb{C}$, then $P$ is marked by $\mu$ if and only if $Q$ is.

Lean: `GlobalTheory.LKMid.Pair.mark_iff_of_rel`.

*Proof.* Let $\beta_Q = s y \beta_P y^*$ and $\gamma_Q = y \gamma_P y^{-1}$. If $\psi_v(\gamma_P) u = \mu u$, then $u' = \psi_v(y) u$ has $\psi_v(\gamma_Q) u' = \mu u'$. From $\psi_v(y^*) = H_v^{-1} \psi_v(y)^\dagger H_v$ we get $u'^\dagger H_v \psi_v(\beta_Q^{-1}) u' = s^{-1} u^\dagger H_v \psi_v(\beta_P^{-1}) u$, and $s > 0$. The converse uses $y^{-1}$. $\square$

### Moving a pair

The next three results are inputs. They are proved in other parts of the development, and we state them here with an outline of the first.

**Theorem 6.1.9 (Moving a definite pair).** Assume $a = 1$ and $n$ odd. Let $P_0 \in F[X]$ be irreducible, $v$ an infinite place with $H_v$ of signature $(1, n-1)$, and $\mu \in \mathbb{C}$ a root of $v(P_0)$. Then there is $A \in F[X]$ with these two properties.

1. For each definite pair $Q$ with $P_{\gamma_Q} = P_0$ there is a pair $P$ with $\gamma_P = \gamma_Q$, $c_P = c_Q$, $\beta_P = A(\gamma_Q) \beta_Q$, marked by $\mu$, and there is $u \in (\mathbb{A}^p \otimes C)^\times$ with $u \gamma_Q = \gamma_Q u$ and $u \beta_Q u^* = \beta_P$.
2. For each pair $P$ with $P_{\gamma_P} = P_0$ marked by $\mu$ there is a definite pair $Q$ with $\gamma_Q = \gamma_P$, $c_Q = c_P$, $\beta_P = A(\gamma_P) \beta_Q$, and there is $u$ as in 1.

Lean: `GlobalTheory.T.exists_polynomial_move_definiteSimilitudePair_marked` (also `GlobalTheory.LKDef.move_definite`).

*Proof.* We outline the argument. Let $M = F[X]/(P_0)$. All complex roots $z$ of $P_0$ have $|z|^2 = c_0$ for one $c_0 \in \mathbb{Q}^\times$, the common factor $c$ of the pairs with polynomial $P_0$, and complex conjugation extends to an involution of $M$. One finds $b \in M$ fixed by this involution, positive at the embedding $\varepsilon$ of $M$ above $v$ that sends $X$ to $\mu$, negative at the other embeddings above $v$, positive above the other infinite places, and with a local condition at the finite places. The embeddings above $v$ other than $\varepsilon$ and $\bar\varepsilon$ number $2(n-1)$, which is divisible by $4$ since $n$ is odd; this is the parity that makes such a $b$ exist. Write $b = A(X)$. Multiplying $\beta$ by $A(\gamma)$ or by $A(\gamma)^{-1}$ changes the signs of the form at the infinite places as required, and the local condition gives $u$. $\square$

**Lemma 6.1.10 (Related pairs have the same term).** If $Q \sim Q'$ are definite pairs, then $P_{\gamma_Q} = P_{\gamma_{Q'}}$ and $c_Q = c_{Q'}$. If also $r > 0$, $f(k^{-1} g k) = f(g)$ for $k \in K^p$, and $\varphi(k^{-1} g\, \sigma(k)) = \varphi(g)$ for $k \in K$, then $T(Q) = T(Q')$.

Lean: `GlobalTheory.T.related_pairs_orbital_term_eq` (also `GlobalTheory.LKDef.DPair.rel_pol_c_term`).

*Proof.* This is an input from another part of the development, which we did not read. $\square$

**Lemma 6.1.11 (Locally isometric pairs have the same term).** Let $P$ be a pair and $Q$ a definite pair with $\gamma_P = \gamma_Q$ and $c_P = c_Q$. Assume there is $u \in (\mathbb{A}^p \otimes C)^\times$ with $u \gamma_Q = \gamma_Q u$ and $u \beta_Q u^* = \beta_P$. Under the three conditions on $r$, $f$ and $\varphi$ of the last lemma, $T(P) = T(Q)$.

Lean: `GlobalTheory.T.kottwitzTerm_eq_definitePair_of_local_isometry` (also `GlobalTheory.LKDefTerm.term_eq_of_local_isom`).

*Proof.* This is an input from another part of the development, which we did not read. $\square$

### The bijection

**Theorem 6.1.12 (Marked classes and definite classes).** Assume $a = 1$ and $n$ odd, and let $\mathrm{sel}$ be a selection. Then there is a bijection $e$ from the set of classes $[P]$ of pairs whose representative $P$ has irreducible $P_\gamma$ and is marked by $\mathrm{sel}(P_\gamma)$, onto the set of classes of definite pairs whose representative has irreducible $P_\gamma$, with these two properties. The representative of $e([P])$ has the polynomial of $P$. For all subgroups $K^p \subseteq G(\mathbb{A}^p)$, $f \colon G(\mathbb{A}^p) \to \mathbb{C}$, $r > 0$, $K \subseteq G_r$ and $\varphi \colon G_r \to \mathbb{C}$ with $f(k^{-1} g k) = f(g)$ for $k \in K^p$ and $\varphi(k^{-1} g\, \sigma(k)) = \varphi(g)$ for $k \in K$, the representative of $e([P])$ has the term of $P$.

Lean: `GlobalTheory.LKDef.cls_equiv_dcls_irr`.

*Proof.* Since $a = 1$, there is an infinite place $v_0$ with $H_{v_0}$ of signature $(1, n-1)$. The minimal polynomial of a unit with irreducible $P_\gamma$ is monic of degree $n$, so $\mathrm{sel}(P_\gamma)$ is a root of $v_0(P_\gamma)$. For each irreducible $P_0$ of this kind, the theorem on moving a definite pair, applied to $P_0$, $v_0$ and $\mu = \mathrm{sel}(P_0)$, gives a polynomial $A_{P_0}$.

Define $e$: for a marked class with representative $P$, part 2 gives a definite pair $Q(P)$ with $\gamma_{Q(P)} = \gamma_P$, and $e([P]) = [Q(P)]$. Define $e'$ in the other direction: for a definite class with representative $Q$, part 1 gives a pair $P(Q)$ with $\gamma_{P(Q)} = \gamma_Q$ marked by $\mathrm{sel}(P_{\gamma_Q})$, and $e'([Q]) = [P(Q)]$. Both land in the right sets: the polynomial is unchanged, it is a class invariant, and so is the mark, by the lemma on marks of related pairs.

We check $e' \circ e = \mathrm{id}$. Let $P$ be a representative, $Q = Q(P)$ and $Q'$ the representative of $[Q]$, with $\beta_{Q'} = s y \beta_Q y^*$ and $\gamma_{Q'} = y \gamma_P y^{-1}$. Then $P(Q')$ has $\gamma = y \gamma_P y^{-1}$ and
$$\beta_{P(Q')} = A(y \gamma_P y^{-1})\, s\, y \beta_Q y^* = s\, y A(\gamma_P) \beta_Q y^* = s\, y \beta_P y^*,$$
since $A(y \gamma y^{-1}) = y A(\gamma) y^{-1}$. So $P(Q') \sim P$. The check of $e \circ e' = \mathrm{id}$ is the same with the roles exchanged, using $\beta_Q = A(\gamma)^{-1} \beta_P$.

For the polynomial: the representative $Q'$ of $e([P])$ is related to $Q(P)$, so it has the polynomial of $Q(P)$, which is that of $P$. For the term: $T(Q') = T(Q(P))$ by the lemma on related pairs, and $T(Q(P)) = T(P)$ by the lemma on locally isometric pairs, with the $u$ of part 2. $\square$

**Remark 6.1.13 (Formalization).** In [MarkedFieldPairsEquivDefiniteFieldPairsOdd.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/MarkedFieldPairsEquivDefiniteFieldPairsOdd.lean#L81) the classes are quotients by the relation, a class is identified with its chosen representative `Quot.out`, and the term uses a chosen trivialization and a chosen pair $(\delta, z)$. The subgroup $K^p$ in the theorem is any subgroup; it need not be a level. The moving theorem is a wrapper of `GlobalTheory.LKDef.move_definite`; we read the outline of its proof (an element of $M$ with prescribed signs from `GlobalTheory.T.exists_totallyReal_even_neg_places_local_norm`) but not every step. We opened the statements of the two lemmas on terms, not their proofs. The text calls the subfield $E$; this chapter uses it only in the next section.
