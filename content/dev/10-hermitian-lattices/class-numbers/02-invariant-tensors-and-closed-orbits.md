---
title: Invariant tensors and closed orbits
decls:
  - GlobalTheory.ClassFin.exists_tensor_stabiliser_closed_orbit
  - GlobalTheory.T.exists_tensor_stabiliser_closed_SL_orbit
  - GlobalTheory.T.leftTranslateMatrixPoly_completelyReducible
  - GlobalTheory.T.exists_leftTranslation_reynoldsOperator
  - GlobalTheory.T.exists_rational_invariant_tensor'
  - GlobalTheory.T.exists_leftInvariantPoly_separating_coset
  - GlobalTheory.T.isClosed_image_SL_under_generating_invariants
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Invariant tensors and closed orbits

A completely reducible rational group is the stabiliser of a rational tensor whose orbit under $\mathrm{SL}_I(\mathbb{C})$ is closed. This section proves that theorem. It is the bridge from the group to a lattice problem: in the next section a double coset of the group becomes a point of the orbit with bounded denominators, and a closed orbit has only finitely many such points up to $\mathrm{SL}_I(\mathbb{Z})$. The proof is classical invariant theory: a Reynolds operator, Hilbert's finiteness of invariants, and the Nullstellensatz. We keep the notation of the first section.

### Tensors and their orbits

**Definition 1.2.1 (Tensors and the right action).** A *type* is a tuple $d = (d_1, \dots, d_m)$ of integers $d_i \geq 0$. Let $I(d)$ be the finite set of pairs $(i, a)$ with $1 \leq i \leq m$ and $a \in I^{d_i}$. A *tensor of type $d$* over a commutative ring $A$ is an element $t \in A^{I(d)}$, that is, an $m$-tuple of tensors $t_i \in (A^I)^{\otimes d_i}$. For $y \in M_I(A)$ let
$$(t \cdot y)_{(i, a)} = \sum_{b \in I^{d_i}} t_{(i, b)} \prod_{k = 1}^{d_i} y_{b_k a_k}.$$

So $t_i \cdot y$ is the row vector $t_i$ times the Kronecker power $y^{\otimes d_i}$. Since $(yz)^{\otimes d} = y^{\otimes d} z^{\otimes d}$, this is a right action: $t \cdot 1 = t$ and $(t \cdot y) \cdot z = t \cdot (yz)$. Each entry of $t \cdot y$ is a polynomial in the entries of $y$ whose coefficients are entries of $t$. For a rational tensor $t$ these are polynomials $\Phi_k \in \mathbb{Q}[x]$, $k \in I(d)$, with $\Phi_k(y) = (t \cdot y)_k$ over every $\mathbb{Q}$-algebra.

**Definition 1.2.2 (Orbit).** The *orbit* of a complex tensor $t$ of type $d$ is
$$O(t) = \{ t \cdot y : y \in \mathrm{SL}_I(\mathbb{C}) \} \subseteq \mathbb{C}^{I(d)}.$$

**Example 1.2.3.** Let $I = \{1, 2\}$, $d = (2)$, and let $t$ be the symmetric tensor of the quadratic form $q(v) = v_1^2 + v_2^2$. Then $t \cdot y$ is the form $q(yv)$, the stabiliser of $t$ in $\mathrm{SL}_2(\mathbb{C})$ is the special orthogonal group of $q$, and $O(t)$ is the set of symmetric matrices of determinant $1$. It is closed.

### Invariant polynomials

Let $\mathbb{C}[x]$ be the polynomial ring over $\mathbb{C}$ in the variables $x_{ij}$. For $g \in M_I(\mathbb{C})$ the *left translation* $\lambda_g$ is the $\mathbb{C}$-algebra map of $\mathbb{C}[x]$ with $(\lambda_g f)(y) = f(gy)$. A polynomial $f$ is *left invariant* under $\Gamma$ if $f(gy) = f(y)$ for all $g \in \Gamma$ and $y \in M_I(\mathbb{C})$. The left invariant polynomials form a subalgebra $\mathbb{C}[x]^\Gamma$. A subspace $U \subseteq \mathbb{C}[x]$ is *stable* if $\lambda_g U \subseteq U$ for all $g \in \Gamma$.

**Definition 1.2.4 (Reynolds operator).** A *Reynolds operator* for $\Gamma$ is a $\mathbb{C}$-linear map $\rho : \mathbb{C}[x] \to \mathbb{C}[x]$ such that

1. $\rho(f)$ is left invariant for every $f$;
2. $\rho(f) = f$ for every left invariant $f$;
3. $\rho(af) = a \rho(f)$ for every left invariant $a$ and every $f$;
4. $\rho(U) \subseteq U$ for every stable subspace $U$.

For a finite group, $\rho(f) = |\Gamma|^{-1} \sum_{g \in \Gamma} \lambda_g f$ is a Reynolds operator. For a compact group one integrates over the group.

**Lemma 1.2.5 (Polynomials are completely reducible).** Let $\Gamma$ be a Galois-stable group that is completely reducible. Then every stable subspace $U \subseteq \mathbb{C}[x]$ has a stable complement.

Lean: `GlobalTheory.T.leftTranslateMatrixPoly_completelyReducible` (also `GlobalTheory.ClassFin.ltr_completely_reducible`, a second name).

*Proof.* We use that the representations $g \mapsto (g^{\otimes n})^{\mathsf{T}}$ of $\Gamma$ on $\mathbb{C}^{I^n}$ are completely reducible for every $n$. For $b \in I^n$ let $p_b : \mathbb{C}^{I^n} \to \mathbb{C}[x]$ send $v$ to the polynomial $y \mapsto \sum_a v_a \prod_k y_{a_k b_k}$. A direct computation gives $p_b((g^{\otimes n})^{\mathsf{T}} v) = \lambda_g p_b(v)$, so $p_b$ is a map of representations. Every monomial of degree $n$ is a product $\prod_k x_{a_k b_k}$, so $\mathbb{C}[x]$ is the sum of the images of the $p_b$, over all $n$ and $b$. A sum of images of semisimple representations is semisimple, and in a semisimple representation every subrepresentation has a complement. $\square$

**Lemma 1.2.6 (Reynolds operator).** Let $\Gamma$ be a Galois-stable group that is completely reducible. Then $\Gamma$ has a Reynolds operator.

Lean: `GlobalTheory.T.exists_leftTranslation_reynoldsOperator`.

*Proof.* Let $V = \mathbb{C}[x]$, $V^\Gamma$ the invariants and $V_1$ the span of the vectors $\lambda_g w - w$. Both are stable. By the previous lemma $V^\Gamma$ has a stable complement $V'$. For $w = w_0 + w'$ with $w_0 \in V^\Gamma$ and $w' \in V'$ we have $\lambda_g w - w = \lambda_g w' - w' \in V'$, so $V_1 \subseteq V'$. A stable complement $C$ of $V_1$ in $V'$ consists of invariants, since $\lambda_g c - c \in V_1 \cap C = 0$, so $C \subseteq V^\Gamma \cap V' = 0$. So $V = V^\Gamma \oplus V_1$. Let $\rho$ be the projection onto $V^\Gamma$ along $V_1$. It has properties 1 and 2. A linear map that commutes with every $\lambda_g$ preserves $V^\Gamma$ and $V_1$, so it commutes with $\rho$. Multiplication by an invariant $a$ commutes with $\lambda_g$, since $\lambda_g(af) = \lambda_g(a) \lambda_g(f) = a \lambda_g(f)$. This gives property 3. For property 4, the same argument inside a stable subspace $U$ gives $U = U^\Gamma \oplus U_1$ with $U_1 \subseteq V_1$, so $\rho(U) = U^\Gamma \subseteq U$. $\square$

**Lemma 1.2.7 (Rational invariant tensors).** Let $\Gamma$ be a Galois-stable group that is completely reducible. Then there are a type $d$ and a rational tensor $t$ of type $d$ such that $t \cdot g = t$ for all $g \in \Gamma$, and such that every left invariant $f \in \mathbb{C}[x]$ has the form $f(y) = P(t \cdot y)$ for a polynomial $P$ with complex coefficients in the entries of a tensor of type $d$.

Lean: `GlobalTheory.T.exists_rational_invariant_tensor'`.

*Proof.* The algebra $\mathbb{C}[x]^\Gamma$ is generated by finitely many homogeneous invariants $F_1, \dots, F_r$. This is Hilbert's finiteness theorem, and its proof uses the Reynolds operator: the ideal of $\mathbb{C}[x]$ generated by the invariants of positive degree is finitely generated by the Hilbert basis theorem, and property 3 of $\rho$ lets one express every invariant through the generators of that ideal, by induction on the degree. Next, a homogeneous invariant $F$ of degree $n$ can be written $F(y) = \sum_b (l_b \cdot y)_b$, where each $l_b \in \mathbb{C}^{I^n}$ is an invariant tensor of degree $n$, that is, $l_b \cdot g = l_b$ for $g \in \Gamma$. The space of invariant tensors of degree $n$ is stable under the automorphisms of $\mathbb{C}$, because $\Gamma$ is. So it is spanned by rational invariant tensors. Let $t$ collect, for each degree $n$ that occurs, finitely many rational invariant tensors that span the invariant tensors of degree $n$. Then each $F_j$ is a linear function of $t \cdot y$, and every invariant is a polynomial in the $F_j$, so a polynomial in $t \cdot y$. $\square$

### Separation and closed images

**Lemma 1.2.8 (Separation of cosets).** Let $\Gamma$ be a rational group with a Reynolds operator $\rho$. Let $y \in \mathrm{SL}_I(\mathbb{C})$ with $y \notin \Gamma$. Then there is a left invariant $f$ with $f(1) \neq f(y)$.

Lean: `GlobalTheory.T.exists_leftInvariantPoly_separating_coset`.

*Proof.* Since $\Gamma = \Gamma(\mathbb{C})$, the group $\Gamma$ is the zero set of $\mathfrak{a}(\Gamma)$, so it is Zariski closed in $M_I(\mathbb{C})$. The coset $\Gamma y$ is also Zariski closed, since $z \mapsto zy$ is a linear automorphism of $M_I(\mathbb{C})$. The two sets are disjoint, as $y \notin \Gamma$. Let $J_1$ and $J_2$ be their ideals in $\mathbb{C}[x]$. By the Nullstellensatz $J_1 + J_2 = \mathbb{C}[x]$, so $1 = a + b$ with $a \in J_1$ and $b \in J_2$. Both ideals are stable subspaces: if $f$ vanishes on $\Gamma y$, then $\lambda_g f$ vanishes on $\Gamma y$ for $g \in \Gamma$. So $\rho(a) \in J_1$ and $\rho(b) \in J_2$ by property 4, and $\rho(a) + \rho(b) = \rho(1) = 1$. Let $f = \rho(a)$. Then $f(1) = 0$ since $1 \in \Gamma$, and $f(y) = 1 - \rho(b)(y) = 1$. $\square$

**Lemma 1.2.9 (Closed image).** Let $\Gamma \subseteq \mathrm{SL}_I(\mathbb{C})$ be a set with a Reynolds operator $\rho$. Let $(\Phi_k)_{k \in K}$ be a finite family of left invariant polynomials that generates the algebra $\mathbb{C}[x]^\Gamma$. Then the set
$$Z = \{ (\Phi_k(y))_{k \in K} : y \in \mathrm{SL}_I(\mathbb{C}) \}$$
is closed in $\mathbb{C}^K$.

Lean: `GlobalTheory.T.isClosed_image_SL_under_generating_invariants`.

*Proof.* The determinant is left invariant, since $\det(gy) = \det y$ for $g \in \Gamma$. So $\det = Q(\Phi)$ for a polynomial $Q$ on $\mathbb{C}^K$. Let $J$ be the ideal of polynomials $P$ on $\mathbb{C}^K$ with $P(\Phi) = 0$. We show that $Z$ is the zero set of $J$ and $Q - 1$. This set is Zariski closed, so it is closed. It contains $Z$. Conversely, let $z$ be a zero of $J$ and of $Q - 1$. Then $P(\Phi) \mapsto P(z)$ is a well defined $\mathbb{C}$-algebra map $\chi : \mathbb{C}[x]^\Gamma \to \mathbb{C}$. Let $\mathfrak{m}$ be its kernel. If $\mathfrak{m} \mathbb{C}[x] = \mathbb{C}[x]$, then $1 = \sum_i a_i f_i$ with $a_i \in \mathfrak{m}$, and property 3 of $\rho$ gives $1 = \sum_i a_i \rho(f_i) \in \mathfrak{m}$, which is false. So $\mathfrak{m} \mathbb{C}[x]$ lies in a maximal ideal of $\mathbb{C}[x]$. By the Nullstellensatz this is the ideal of a point $y \in M_I(\mathbb{C})$. Then $\Phi_k(y) = z_k$, as $\Phi_k - z_k \in \mathfrak{m}$, and $\det y = Q(z) = 1$. So $z \in Z$. $\square$

### The theorem

**Theorem 1.2.10 (Invariant tensor with closed orbit).** Let $\Gamma \subseteq M_I(\mathbb{C})$ be a rational group that is completely reducible. Then there are a type $d$ and a rational tensor $t$ of type $d$ such that

1. $t \cdot g = t$ for every $g \in \Gamma$;
2. every $y \in M_I(\mathbb{C})$ with $\det y = 1$ and $t \cdot y = t$ lies in $\Gamma$;
3. the orbit $O(t)$ is closed in $\mathbb{C}^{I(d)}$.

Lean: `GlobalTheory.ClassFin.exists_tensor_stabiliser_closed_orbit` (also `GlobalTheory.T.exists_tensor_stabiliser_closed_SL_orbit`, a second name).

*Proof.* The lemma on the Reynolds operator gives $\rho$, and the lemma on rational invariant tensors gives $t$ with property 1. For property 2, let $\det y = 1$, $t \cdot y = t$, and suppose $y \notin \Gamma$. The lemma on separation of cosets gives a left invariant $f$ with $f(1) \neq f(y)$. But $f = P(t \cdot -)$ for some $P$, and $t \cdot y = t = t \cdot 1$, so $f(y) = f(1)$. This is a contradiction. For property 3, let $\Phi_k \in \mathbb{Q}[x]$ be the polynomials with $\Phi_k(y) = (t \cdot y)_k$. Each $\Phi_k$ is left invariant, since $t \cdot (gy) = (t \cdot g) \cdot y = t \cdot y$ for $g \in \Gamma$. By the lemma on rational invariant tensors they generate $\mathbb{C}[x]^\Gamma$. Now $O(t)$ is the image of $\mathrm{SL}_I(\mathbb{C})$ under $(\Phi_k)$, and it is closed by the lemma on closed images. $\square$

Properties 1 and 2 say that $\Gamma$ is the stabiliser of $t$ in $\mathrm{SL}_I(\mathbb{C})$. The proof of property 3 shows more: $O(t)$ is Zariski closed, cut out by polynomials.

**Remark 1.2.11 (Formalization).** The statement asks for closedness of $O(t)$ in the product topology of $\mathbb{C}^{I(d)}$, which is the usual topology; we prove Zariski closedness, which implies it. The complete reducibility of the tensor powers $(g^{\otimes n})^{\mathsf{T}}$ used in the first lemma is `GlobalTheory.T.completelyReducible_kroneckerPower_transpose`, and the abstract Reynolds projection is `GlobalTheory.T.exists_reynolds_of_completelyReducible'`, which states properties 1 to 4 for any set of operators on a completely reducible space; the argument we give for it is ours, as we have not unfolded its proof. Hilbert's theorem is `GlobalTheory.T.hilbert_finiteness_leftInvariantMatrixPoly`, the decomposition of a homogeneous invariant into invariant tensors is `GlobalTheory.T.invariant_form_eq_sum_invariant_tensors'`, and the rational spanning is `GlobalTheory.T.mem_span_rational_kroneckerInvariants`; we have not unfolded these proofs either, and the sketches above give their mathematical content. The second name `GlobalTheory.T.exists_tensor_stabiliser_closed_SL_orbit` is a wrapper proved by `first | exact ...` under `set_option maxHeartbeats 1000000`.
