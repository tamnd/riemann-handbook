---
title: Realisations of multiplicity spaces
decls:
  - GlobalTheory.MtId.side_read
  - GlobalTheory.MtId.tup_read
  - GlobalTheory.MtId.fam_read
  - GlobalTheory.MtId.real_state
  - GlobalTheory.MtId.inMt_state
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Realisations of multiplicity spaces

For each tuple $\mu$ and each step $i$, the ambient datum has a multiplicity space $M_t(\mu, i + 1)$ over the coefficient field. The membership statement needs this space as a space of automorphic forms on the definite unitary group $U(n)$: an injective map into the functions on $U(n, \mathbb{A}_f)$ with values in an algebraic representation, whose image is the space of forms of a fixed type, and on which the Hecke operators at split places act integrally. We call such a map a realisation. In this section we construct realisations, first for one side input, then for a tuple, a family and a stage, and finally the multiplicity data of a stage with identity frames. The result enters [the nonempty hypotheses at unramified exponents](/entry/hypotheses-nonempty-of-unramified-exponents-alt/).

### Two facts of linear algebra

**Lemma 1.21.1 (Span of a transported family).** Let $T : M \to N$ be an isomorphism of complex vector spaces, $f : \iota \to M$ a family with span $S$, and $S' \subset N$ a subspace with $x \in S$ if and only if $T(x) \in S'$. Then the span of $T \circ f$ is $S'$.

*Proof.* The span of $T \circ f$ is $T(S)$, and $T(S) = S'$ since $T$ is bijective. $\square$

**Lemma 1.21.2 (Extension of a semilinear map).** Let $\sigma : K \to \mathbb{C}$ be a field map, and let $j : K^d \to M$ and $\Phi : K^d \to N$ be $\sigma$-semilinear. Assume that the vectors $j(e_a)$ form a basis of $M$ and that the vectors $\Phi(e_a)$ are linearly independent. Then there is an injective linear map $r : M \to N$ with image the span of the $\Phi(e_a)$ and $r(j(x)) = \Phi(x)$ for all $x$.

*Proof.* Let $r$ send the basis vector $j(e_a)$ to $\Phi(e_a)$. It is injective since the images are independent. Both $r \circ j$ and $\Phi$ are semilinear and agree on the $e_a$, so they agree. $\square$

### One side

Let $D$ be an ambient datum with CM field $E$, real subfield $F^+$ and coefficient field $L_L$ with its embedding into $\mathbb{C}$. Let $V$ be a definite hermitian space of rank $n \ge r$ with Gram matrix $1$ and standard lattice, and let $P$ be a unit frame of $V$. Then $P$ identifies the finite adelic points of the group of $V$ with $U(n, \mathbb{A}_f)$. Let $c$ be a coefficient datum for $V$ with representation space $W$.

A side input $u$ at step $j$, with level index $\beta = 1$, places $P_g$ and $Q$, characters $\chi$, $\xi$ and additive characters $\psi$, consists of a space of dimension $d$ over $L_L$, a semilinear map $x \mapsto u(x)$ into the $W$-valued functions on the group of $V$, a lattice $\nabla_u$ in it, a group isomorphism $e_G$ and a subgroup $P_0$ with a character $\psi_0$. Let $L_v$ be the level of $u$, and let $J$ and $\chi_J$ be the standard level and character of the datum $(n, P_g, Q, L_v, \chi, \xi)$. For an algebraic weight $a$ of $U(n)$ with representation $\rho_a$, the type space $\mathrm{Typ}(\rho_a, J, \chi_J)$ is the space of functions $f$ on $U(n, \mathbb{A}_f)$ with values in the space of $\rho_a$ that transform under $U(n, F^+)$ by $\rho_a$ and under $J$ by $\chi_J$. The Hecke operator $T_k(s, \varpi)$ at a split place $s$ with a uniformizer $\varpi$ is the operator of the double coset of $\mathrm{diag}(\varpi, \dots, \varpi, 1, \dots, 1)$ with $k$ entries $\varpi$.

**Theorem 1.21.3 (Realisation of one side).** Let $V$, $c$, $u$, $P$ and $L_v$ be as above. Then there are an algebraic weight $a$ of $U(n)$, an isomorphism $e_W$ from the space of $\rho_a$ to $W$, and an $L_L$-semilinear map $\Phi$ from $L_L^d$ to the functions on $U(n, \mathbb{A}_f)$ with values in the space of $\rho_a$, with the following properties.

1. For each weight $a'$ dual to $a$ and each embedding $\tau$, the highest weight of $a'$ at $\tau$ is $\lambda_L(n, j, \tau)$.
2. $e_W(\rho_a(g) v) = \rho_c(\gamma) e_W(v)$ whenever $\gamma \in U(V)(F^+)$ has the same finite image as $g$ under the frame.
3. $e_W(\Phi(x)(g)) = u(x)(P(g))$ for all $x$ and $g$.
4. The functions $\Phi(e_k)$ are linearly independent, and their span is $\mathrm{Typ}(\rho_a, J, \chi_J)$.
5. For each finite set $B$ of places outside which $J$ is hyperspecial, each split place $s \notin B$, each uniformizer $\varpi$ at $s$ and each $1 \le k \le n$, and each $x$, there is $x'$ with $\Phi(x') = T_k(s, \varpi)\Phi(x)$. If $x \in \nabla_u$ and $\mathfrak{w}$ is a prime of $L_L$ that contains no prime $p$ under $s$, then $d x' \in \nabla_u$ for some $d \notin \mathfrak{w}$.

Lean: `GlobalTheory.MtId.side_read`.

*Proof.* The frame $P$ gives a bijection from $U(n, \mathbb{A}_f)$ to the finite adelic group of $V$ and a rational isomorphism of the groups. The coefficient space of the definite forms is an irreducible algebraic representation; this gives $a$, $e_W$ and properties 1 and 2. Define $\Phi(x) = e_W^{-1} \circ u(x) \circ P$, which gives property 3. The level forms of $u$ have an adelic basis, and the definite level forms are the forms of the type space of the standard group. This gives property 4, with the lemma on the span of a transported family. Hecke operators at split places outside $B$ keep the rational integral level forms, up to a denominator prime to $\mathfrak{w}$. This gives property 5. $\square$

### Tuples, families and stages

A realisation of $M_t(\mu, i + 1)$ is an algebraic weight with representation space $W_m$, an open compact subgroup, and an injective linear map $m$ from $M_t(\mu, i + 1)$ to the $W_m$-valued functions on $U(n_V, \mathbb{A}_f)$, whose image is the type space of the level and the character. We say that a realisation is good for a Hecke character $\chi$ at step $i$ if it satisfies the conditions of goodness at $i$ for $\chi$.

**Theorem 1.21.4 (Realisation of a tuple).** Let $L$ be level and character data with reference tuple $\mu_0$, whose places $P_g$ are the places over the auxiliary primes, with level index $\beta_V(i) = 1$, let $\psi$ be generic at $P_g$, and let $\tau$ be a tuple input at step $i$ for a tuple $t$. Assume that the space $V_c(i)$ of step $i$ has Gram matrix $1$ and standard lattice, and let $P$ be a unit frame. Then there are a realisation $m$ of $M_t(\mu, i + 1)$ and $e_W$ such that $m$ is good at $i$ for $\mu_0(i) \cdot \xi_H(t)$, $e_W$ intertwines the representations as in property 2, and
$$e_W\big(m(j(\tau.e(x)))(g)\big) = \tau.u(x)(P(g)).$$

Lean: `GlobalTheory.MtId.tup_read`.

*Proof.* The realisation of one side gives $a$, $e_W$ and $\Phi$. The lemma on the extension of a semilinear map, applied to $j \circ \tau.e$ and $\Phi$, gives an injective $r$ with $r \circ j \circ \tau.e = \Phi$ whose image is the span of the $\Phi(e_k)$, which is the type space. For goodness, the standard frame level group is bounded, open and hyperspecial outside the places over the auxiliary primes and the ramified places of $\mu_0(i)\xi_H(t)$. It is a product of local levels and equals the two block unipotent level. At the ramified places it is the parahoric level with the tuple character. The generic character of the unipotent level at the type places is the character of the level, and the infinitesimal character of the weight $\lambda_L$ is the parameter of the step. $\square$

**Corollary 1.21.5 (Realisation along a family).** Let $A$ be a family over a finite group $G$, and let $L$, $\psi$, $V_c(i)$ and $P$ be as in the theorem, with a group isomorphism $e_G : G \cong G_0(L)$ and a level $P_0$ with character $\psi_0$ that give the level of $L$. Let the lift forms of $A$ at $(i, t)$ have a class presentation with an action tie whose reduction is the right translation, a coefficient map with its ties, character values in the integers of $L_L$, a basis $e$ of $M_t^L(\mu, i + 1)$ with independent and spanning images, and a lattice tie. Then the conclusion of the theorem holds for this tuple input.

Lean: `GlobalTheory.MtId.fam_read`.

*Proof.* The listed data are a tuple input at step $i$ for $t$. Apply the theorem. $\square$

Let $x$ be a state of the construction over a column datum $w$ with a column pin, with ambient datum $D(x)$, coefficient field data $c_f(x)$, and row reading $Y$. A tuple $\mu$ is used if it is a tuple of the rows of $Y$.

**Theorem 1.21.6 (Realisations at a state).** Let $w$ have a column pin, and let $F_m(i)$ be unit frames of the spaces $V_c(i)$. For each tuple $\mu$ and each step $i$ there is a realisation $m$ of $M_t(\mu, i + 1)$ that is good at $i$ for $\mu_0(i) \cdot \xi_\mu$, and if $\mu$ is used, then $m$ reads the rows of $Y$ through some $e_W$ and the frames $F_m$.

Lean: `GlobalTheory.MtId.real_state`.

*Proof.* If $\mu$ is used, then $\mu$ is the tuple of a row $t$ of $Y$. The rows of $Y$ come with lift forms that satisfy the hypotheses of the corollary: the places of the level are those over the auxiliary primes, the level index is $1$, the spaces have Gram matrix $1$ and standard lattices, and the character values are integral. The corollary gives $m$ and $e_W$ for $t$. The character $\mu_0(i)\xi_H(t)$ is $\mu_0(i)\xi_\mu$ since the coefficient data of the state are $c_f(x)$ and $\xi_H(t)$ is $\xi$ of the tuple of $t$. If $\mu$ is not used, take the level data of all indices. The lift coordinates of the row package at $\mu$ are the lift matrices of the family of all indices, and the cast of the lift tie gives a basis with independent and spanning images and a lattice tie. With the good set of levels and characters, the realisation of all tuples gives $m$. The second claim is empty. $\square$

**Theorem 1.21.7 (Multiplicity data with identity frames).** Let $w$ have a column pin, and let $x$ be a state over $w$. Then there are multiplicity data for the rows $Y$ of $x$, the coefficient data $c_f(x)$, the characters $\xi$ of $w$ and the primes of the state, whose frames are identity frames at each step.

Lean: `GlobalTheory.MtId.inMt_state`.

*Proof.* Each space $V_c(i)$ has Gram matrix $1$ and a standard lattice, so it has a unit frame $F_m(i)$ that is standard and an identity frame. The casts of these frames to rank $n_V$ keep these properties and are rational. The multiplicity data are built from such frames, from the realisations at the state, and from the general state data. Their frames are the casts of the $F_m(i)$, which are identity frames. $\square$

**Remark 1.21.8 (Formalization).** The objects `MtReal`, `Good`, `InMt` and the reading `Reads` ([SpanRangeEquiv.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/SpanRangeEquiv.lean#L256)) are not unfolded here, and the statements above give them only through the properties used. The theorem on one side is at line 65 of that file, the tuple at line 126, the family at line 204, the state at line 435 and the multiplicity data at line 462. The two linear algebra lemmas are `span_range_equiv` and `constr_semi` at lines 39 and 50. In the theorem at a state, the unused case returns a realisation and an empty second claim, so for unused tuples the theorem gives only goodness. The goodness steps in the proof of the tuple theorem are lemmas of the form `GlobalTheory.T.*` that we have not opened.
