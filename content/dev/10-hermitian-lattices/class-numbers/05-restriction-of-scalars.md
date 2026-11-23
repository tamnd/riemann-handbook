---
title: Restriction of scalars
decls:
  - GlobalTheory.ClassFin.classFinite_integralLevel
  - GlobalTheory.T.classNumber_finite_integralLevel_closedSubgroupGL
  - GlobalTheory.T.glFreeAlgebraToSpecialLinearEmb_injective_hom
  - GlobalTheory.T.glFreeAlgebraEmb_integral_and_rational
  - GlobalTheory.T.adelic_pair_reduced_basis
  - GlobalTheory.T.exists_isQGroup_weilRestriction_alt
  - GlobalTheory.T.exists_rational_equations_weil_restriction
  - GlobalTheory.T.mem_ratZariskiClosurePoints_iff_of_isReduced
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Restriction of scalars

This section passes from $\mathbb{Q}$ to a number field $F$. A group $G \subseteq \mathrm{GL}_n$ over $F$ is cut out by polynomial equations with coefficients in $F$. Restriction of scalars from $F$ to $\mathbb{Q}$ turns $G$ into a rational group $\Gamma$ of matrices of size $n[F : \mathbb{Q}] + 1$, and it turns the finite adeles of $F$ into an adelic pair. The theorem over $\mathbb{Q}$ of the last section then gives the finiteness of $G(F) \backslash G(\mathbb{A}_{F,f}) / G(\widehat{\mathcal{O}})$, the class number of $G$ at the integral level. The next section passes from the integral level to an open compact level.

### Group loci

Let $F$ be a field and $n \geq 0$. For a set $S \subseteq F[x_{ij} : 1 \leq i, j \leq n]$ of polynomials and a commutative $F$-algebra $B$ let
$$G_S(B) = \{ g \in \mathrm{GL}_n(B) : P(g) = 0 \text{ for all } P \in S \}.$$

**Definition 1.5.1 (Group locus).** The set $S$ is a *group locus* if for every commutative $F$-algebra $B$ the set $G_S(B)$ contains $1$ and is closed under products and inverses in $\mathrm{GL}_n(B)$.

Then $B \mapsto G_S(B)$ is a functor to groups, and the zero set of $S$ is a closed subgroup of $\mathrm{GL}_n$ over $F$: a [[linear algebraic group|GA81VVQHEP]] with a given embedding into $\mathrm{GL}_n$. For example, $S = \{\det - 1\}$ gives $\mathrm{SL}_n$, and $S = \{x_{ij} : i \neq j\}$ gives the diagonal torus. The condition is asked for all $F$-algebras $B$, not only for fields, so that it holds for the finite adeles.

Let $F$ be a number field ([number fields](/learn/number-fields/#number-fields-and-their-integers)). For a finite place $v$ of $F$ let $\mathcal{O}_v$ be the ring of integers of the completion $F_v$, and let $\mathbb{A}_{F,f}$ be the ring of finite adeles ([[adele ring|NYJFYZ0B4M]], see [adeles](/learn/number-fields/#adeles-and-ideles)). An adele $a$ is *integral* if $a_v \in \mathcal{O}_v$ for every finite place $v$. A matrix $u \in \mathrm{GL}_n(\mathbb{A}_{F,f})$ is *integral* if the entries of $u$ and of $u^{-1}$ are integral, that is, if $u \in \mathrm{GL}_n(\widehat{\mathcal{O}})$ with $\widehat{\mathcal{O}} = \prod_v \mathcal{O}_v$.

### The embedding into $\mathrm{SL}$

Let $R$ be a commutative ring, $A$ a commutative $R$-algebra, and $b = (b_k)_{k \in \beta}$ a finite basis of $A$ over $R$. For $a \in A$ let $m_b(a) \in M_\beta(R)$ be the matrix of multiplication by $a$, so that $a\, b_l = \sum_k m_b(a)_{kl}\, b_k$. For a finite set $\kappa$ and $g \in M_\kappa(A)$ let $\operatorname{res}_b(g) \in M_{\kappa \times \beta}(R)$ be the matrix with blocks $m_b(g_{ij})$:
$$\operatorname{res}_b(g)_{(i,k),(j,l)} = m_b(g_{ij})_{kl}.$$
It is the matrix of $g$, seen as an $R$-linear map of $A^\kappa \cong R^{\kappa \times \beta}$. Let $\star$ be one more index. For $g \in \mathrm{GL}_\kappa(A)$ let
$$\operatorname{emb}_b(g) = \begin{pmatrix} \operatorname{res}_b(g) & 0 \\ 0 & \det \operatorname{res}_b(g^{-1}) \end{pmatrix} \in M_{(\kappa \times \beta) \sqcup \{\star\}}(R).$$
The corner entry makes the determinant $1$, so that the image is a group of matrices of determinant $1$, as the theorem over $\mathbb{Q}$ needs. It also makes the inverse a polynomial in the entries: the inverse of $\operatorname{res}_b(g)$ is the corner entry times the adjugate.

**Lemma 1.5.2 (The embedding is a homomorphism).** Let $R$, $A$, $b$ and $\kappa$ be as above. Then $\operatorname{emb}_b(1) = 1$, $\operatorname{emb}_b(gh) = \operatorname{emb}_b(g)\operatorname{emb}_b(h)$, $\det \operatorname{emb}_b(g) = 1$ and $\operatorname{adj}(\operatorname{emb}_b(g)) = \operatorname{emb}_b(g^{-1})$ for all $g, h \in \mathrm{GL}_\kappa(A)$, and $\operatorname{emb}_b$ is injective on $\mathrm{GL}_\kappa(A)$.

Lean: `GlobalTheory.T.glFreeAlgebraToSpecialLinearEmb_injective_hom`.

*Proof.* The map $a \mapsto m_b(a)$ is a ring homomorphism, so $\operatorname{res}_b$ is multiplicative on matrices and $\operatorname{res}_b(1) = 1$. Then $\det \operatorname{res}_b(g) \cdot \det \operatorname{res}_b(g^{-1}) = \det \operatorname{res}_b(1) = 1$, which gives the determinant and the multiplicativity of the corner entry. A matrix of determinant $1$ has its inverse as adjugate, and the inverse of $\operatorname{emb}_b(g)$ is $\operatorname{emb}_b(g^{-1})$. If $\operatorname{res}_b(g) = \operatorname{res}_b(h)$, then $m_b(g_{ij}) = m_b(h_{ij})$ for all $i, j$, and $g_{ij} = g_{ij} \cdot 1$ is determined by $m_b(g_{ij})$ and the coordinates of $1$. So $g = h$. $\square$

**Lemma 1.5.3 (Integral and rational points).** Let $R$, $A$, $b$ and $\kappa$ be as above.

1. Let $R_0 \subseteq R$ be a subring such that the coordinates of $1 \in A$ in the basis $b$ lie in $R_0$, and let $u \in \mathrm{GL}_\kappa(A)$ be such that all entries of $\operatorname{emb}_b(u)$ lie in $R_0$. Then the coordinates of all entries of $u$ and of $u^{-1}$ in the basis $b$ lie in $R_0$.
2. Let $F$ be a field of characteristic $0$ with a basis $\omega = (\omega_k)_{k \in \beta}$ over $\mathbb{Q}$. Let $R$ be a commutative $\mathbb{Q}$-algebra and let $A$ also be an $F$-algebra, with $b_k = \omega_k$ in $A$ for every $k$. Then for every $\gamma \in \mathrm{GL}_\kappa(F)$ the matrix $\operatorname{emb}_b(\gamma)$ of the image of $\gamma$ in $\mathrm{GL}_\kappa(A)$ is the image in $R$ of the rational matrix $\operatorname{emb}_\omega(\gamma)$.

Lean: `GlobalTheory.T.glFreeAlgebraEmb_integral_and_rational`.

*Proof.* For part 1, let $c_k \in R_0$ be the coordinates of $1$. Then $a = \sum_k c_k\, a\, b_k$, so the coordinates of $a$ are $\sum_k c_k\, m_b(a)_{\cdot k}$, which lie in $R_0$ if $m_b(a)$ has entries in $R_0$. This gives the claim for $u$. For $u^{-1}$, the matrix $\operatorname{res}_b(u^{-1})$ is the inverse of $\operatorname{res}_b(u)$, and it equals the corner entry of $\operatorname{emb}_b(u)$ times $\operatorname{adj}(\operatorname{res}_b(u))$. Both factors have entries in $R_0$, and the first argument applies. For part 2, a map from $\mathbb{Q}$ to a ring is unique, so the images of a rational number in $R$, in $F$ and in $A$ are compatible. If $a \in F$ and $a\, \omega_l = \sum_k m_\omega(a)_{kl}\, \omega_k$ with rational coefficients, the same identity holds in $A$ with $b$ in place of $\omega$. So $m_b(a) = m_\omega(a)$ in $M_\beta(R)$, and the same holds for $\operatorname{res}$, for the determinant and for $\operatorname{emb}$. $\square$

### The rational group of a group locus

We use the following two facts.

**Lemma 1.5.4 (Rational equations for restriction of scalars).** Let $F$ be a field of characteristic $0$ with a finite basis $\omega$ over $\mathbb{Q}$ indexed by $\beta$, and let $S \subseteq F[x_{ij}]$ be any set. Then there is a set $S'$ of polynomials with rational coefficients in the entries of matrices indexed by $(\{1, \dots, n\} \times \beta) \sqcup \{\star\}$ such that the following holds. For every commutative $\mathbb{Q}$-algebra $R$, every commutative ring $A$ that is an $R$-algebra and an $F$-algebra, every basis $b$ of $A$ over $R$ with $b_k = \omega_k$ in $A$, and every matrix $y$ over $R$: all $f \in S'$ vanish at $y$ if and only if $y = \operatorname{emb}_b(g)$ for some $g \in G_S(A)$.

Lean: `GlobalTheory.T.exists_rational_equations_weil_restriction`.

This is the construction of the restriction of scalars $\mathrm{R}_{F/\mathbb{Q}} G_S$ by equations (see Platonov and Rapinchuk, Chapter 2, §2.1). We do not prove it here.

**Lemma 1.5.5 (Points over a reduced ring).** Let $S'$ be a set of rational polynomials in the entries of $I \times I$ matrices, and let $\Gamma \subseteq M_I(\mathbb{C})$ be its complex zero set. Let $R$ be a commutative $\mathbb{Q}$-algebra and $y \in M_I(R)$. If $y \in \Gamma(R)$, then all $f \in S'$ vanish at $y$. If $R$ is reduced and all $f \in S'$ vanish at $y$, then $y \in \Gamma(R)$.

Lean: `GlobalTheory.T.mem_ratZariskiClosurePoints_iff_of_isReduced`.

*Proof.* The first claim holds since $S' \subseteq \mathfrak{a}(\Gamma)$. For the second, let $f \in \mathfrak{a}(\Gamma)$, and let $J$ be the ideal of $\mathbb{Q}[x]$ generated by $S'$. By the Nullstellensatz over $\mathbb{C}$, some power $f^m$ lies in $J\,\mathbb{C}[x]$. Since $J\,\mathbb{C}[x] \cap \mathbb{Q}[x] = J$ (take the coefficients of an expression of $f^m$ with respect to a basis of $\mathbb{C}$ over $\mathbb{Q}$ that contains $1$), $f^m \in J$. So $f(y)^m = 0$, and $f(y) = 0$ since $R$ is reduced. $\square$

**Proposition 1.5.6 (Restriction of scalars of a group locus).** Let $F$ be a field of characteristic $0$ with a finite basis $\omega$ over $\mathbb{Q}$ indexed by $\beta$, and let $S \subseteq F[x_{ij}]$ be a group locus. Then there is a rational group $\Gamma$ of matrices indexed by $(\{1, \dots, n\} \times \beta) \sqcup \{\star\}$ such that for every commutative $\mathbb{Q}$-algebra $R$, every commutative ring $A$ that is an $R$-algebra and an $F$-algebra, and every basis $b$ of $A$ over $R$ with $b_k = \omega_k$ in $A$:

1. every $y \in \Gamma(R)$ is $\operatorname{emb}_b(g)$ for some $g \in G_S(A)$;
2. if $R$ is reduced, then $\operatorname{emb}_b(g) \in \Gamma(R)$ for every $g \in G_S(A)$.

Lean: `GlobalTheory.T.exists_isQGroup_weilRestriction_alt` (also `GlobalTheory.ClassFin.exists_isQGroup_weilRestriction`, a second name).

*Proof.* Let $S'$ be given by the lemma on rational equations, and let $\Gamma$ be the complex zero set of $S'$. Apply that lemma to $R = \mathbb{C}$, $A = \mathbb{C} \otimes_\mathbb{Q} F$ and $b = 1 \otimes \omega$. So $\Gamma$ is the image of $G_S(\mathbb{C} \otimes_\mathbb{Q} F)$ under $\operatorname{emb}_b$. Since $S$ is a group locus, the lemma on the embedding shows that $\Gamma$ contains $1$, is closed under products and adjugates, and has determinant $1$. It is stable under the automorphisms of $\mathbb{C}$, since $S'$ has rational coefficients, so it is a Galois-stable group. By the first part of the lemma on reduced rings, every point of $\Gamma(\mathbb{C})$ is a zero of $S'$, so $\Gamma(\mathbb{C}) \subseteq \Gamma$, and $\Gamma$ is a rational group. Now let $R$, $A$ and $b$ be given. For $y \in \Gamma(R)$, the polynomials of $S'$ vanish at $y$ by the first part of the lemma on reduced rings, and the lemma on rational equations gives part 1. For $g \in G_S(A)$, the polynomials of $S'$ vanish at $\operatorname{emb}_b(g)$ by the lemma on rational equations, and if $R$ is reduced the second part of the lemma on reduced rings gives part 2. $\square$

### The finite adeles as an adelic pair

We use the following fact.

**Lemma 1.5.7 (Finite adeles over an adelic pair).** Let $F$ be a number field and $\omega$ a basis of $\mathcal{O}_F$ over $\mathbb{Z}$, indexed by $\beta$. Then there are a reduced commutative $\mathbb{Q}$-algebra $R$, a subring $R_0 \subseteq R$ such that $(R, R_0)$ is an adelic pair, a structure of $R$-algebra on $\mathbb{A}_{F,f}$, and a basis $b$ of $\mathbb{A}_{F,f}$ over $R$ with $b_k = \omega_k$ for every $k$, such that an adele $a$ is integral if and only if all its coordinates in the basis $b$ lie in $R_0$.

Lean: `GlobalTheory.T.adelic_pair_reduced_basis`.

In the model case $R = \mathbb{A}_{\mathbb{Q},f}$ and $R_0 = \widehat{\mathbb{Z}}$: then $\mathbb{A}_{F,f} = \mathbb{A}_{\mathbb{Q},f} \otimes_\mathbb{Q} F$ has the basis $\omega$, and $\widehat{\mathcal{O}} = \widehat{\mathbb{Z}} \otimes_\mathbb{Z} \mathcal{O}_F$ (see [adeles](/learn/number-fields/#adeles-and-ideles)). We do not prove the lemma here.

### Class finiteness at the integral level

**Theorem 1.5.8 (Class finiteness at the integral level).** Let $F$ be a number field, $n \geq 0$, and $S \subseteq F[x_{ij}]$ a group locus. Then there is a finite set $T \subseteq G_S(\mathbb{A}_{F,f})$ such that every $x \in G_S(\mathbb{A}_{F,f})$ is
$$x = \gamma\, s\, u, \qquad \gamma \in G_S(F),\ s \in T,\ u \in G_S(\mathbb{A}_{F,f}) \text{ integral}.$$

Lean: `GlobalTheory.ClassFin.classFinite_integralLevel` (also `GlobalTheory.T.classNumber_finite_integralLevel_closedSubgroupGL`, a second name).

*Proof.* Let $\omega$ be a basis of $\mathcal{O}_F$ over $\mathbb{Z}$. It is also a basis of $F$ over $\mathbb{Q}$. Take $R$, $R_0$ and $b$ from the lemma on finite adeles, and $\Gamma$ from the proposition on restriction of scalars. By the [theorem over $\mathbb{Q}$](/entry/cf-of-is-qgroup/), there is a finite set $T_0 \subseteq \Gamma(R)$ with $\Gamma(R) = \Gamma(\mathbb{Q})\, T_0\, (\Gamma(R) \cap M(R_0))$. By part 1 of the proposition with $A = \mathbb{A}_{F,f}$, each $s \in T_0$ is $\operatorname{emb}_b(\tilde s)$ with $\tilde s \in G_S(\mathbb{A}_{F,f})$. Choose one $\tilde s$ for each $s$, and let $T = \{\tilde s : s \in T_0\}$.

Let $x \in G_S(\mathbb{A}_{F,f})$. Since $R$ is reduced, part 2 of the proposition gives $\operatorname{emb}_b(x) \in \Gamma(R)$. So
$$\operatorname{emb}_b(x) = \gamma_0\, s\, u_0, \qquad \gamma_0 \in \Gamma(\mathbb{Q}),\ s \in T_0,\ u_0 \in \Gamma(R) \text{ with entries in } R_0.$$
Part 1 of the proposition with $R = \mathbb{Q}$, $A = F$ and the basis $\omega$ gives $\gamma_0 = \operatorname{emb}_\omega(\gamma)$ with $\gamma \in G_S(F)$. Part 1 with $A = \mathbb{A}_{F,f}$ gives $u_0 = \operatorname{emb}_b(u)$ with $u \in G_S(\mathbb{A}_{F,f})$. The adele $1$ is integral, so its coordinates lie in $R_0$, and part 1 of the lemma on integral and rational points shows that the coordinates of the entries of $u$ and $u^{-1}$ lie in $R_0$. By the lemma on finite adeles, $u$ is integral. By part 2 of the lemma on integral and rational points, $\operatorname{emb}_b(\gamma) = \operatorname{emb}_\omega(\gamma)$ in $R$, where $\gamma$ is seen in $\mathrm{GL}_n(\mathbb{A}_{F,f})$. So by the lemma on the embedding,
$$\operatorname{emb}_b(x) = \operatorname{emb}_b(\gamma)\operatorname{emb}_b(\tilde s)\operatorname{emb}_b(u) = \operatorname{emb}_b(\gamma\, \tilde s\, u),$$
and $x = \gamma\, \tilde s\, u$ since $\operatorname{emb}_b$ is injective. $\square$

The classical form of this theorem is the finiteness of the class number of a linear algebraic group (Borel); the next section states it.

**Remark 1.5.9 (Formalization).** The lemma on rational equations and the lemma on finite adeles are proved in the same folder, by `GlobalTheory.T.exists_rational_equations_weil_restriction` and `GlobalTheory.AdeleFree.finiteAdele_free`; we have opened their statements, not their proofs. The ring $R$ of the lemma on finite adeles is built as a subring of $\mathbb{A}_{F,f}$ from the integral adeles, and the statement does not identify it with $\mathbb{A}_{\mathbb{Q},f}$; only the stated properties are used. The proof given for the lemma on reduced rings is ours. The lemmas on the embedding and the proposition ask for no compatibility between the structures of $\mathbb{Q}$-algebra, $R$-algebra and $F$-algebra; the only link is $b_k = \omega_k$, and the uniqueness of maps from $\mathbb{Q}$ makes this enough. The second name of the theorem is a wrapper proved by `first | exact ...` under `set_option maxHeartbeats 1000000`.
