---
title: Harmonic representatives in relative Lie algebra cohomology
decls:
  - UpperTheory.V.Cj.H.fnProj
  - UpperTheory.V.Cj.H.hodgeEx
  - UpperTheory.V.Cj.partH
  - UpperTheory.V.Cj.relOnto
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Harmonic representatives in relative Lie algebra cohomology

Let $E$ be a totally complex field. The cohomology of the locally symmetric spaces of $\mathrm{GL}_a$ over $E$ can be computed by relative Lie algebra cochains with values in smooth functions on $\mathrm{GL}_a(\mathbb{A}_E)$. This section proves two facts about these cochains. First, every compactly supported class has a harmonic representative whose coefficients are automorphic forms of the expected infinitesimal character. Second, a class of rapid decay is related, through an automorphism $\sigma$ of $\mathbb{C}$, to a class in any space of representatives for the conjugate coefficient system. These are the analytic inputs of [Clozel's theorem on conjugate representations](/entry/clozel-conj-c/): the conjugate $\sigma\pi$ of a cohomological cuspidal representation $\pi$ is again cohomological and automorphic ([cohomological representations](/learn/automorphic-forms/#regular-algebraic-cohomological-and-polarized-representations)).

### Relative cochains

Let $G = \mathrm{GL}_a$ over $E$, $E_\infty = E \otimes \mathbb{R} \cong \mathbb{C}^{r_2}$, and let $\mathfrak{p}$ be the real vector space of Hermitian matrices in $M_a(E_\infty)$. It is the $-1$ eigenspace of the Cartan involution on the Lie algebra of $G(E_\infty)$, and it is stable under the maximal compact subgroup $K_\infty$ (unitary matrices) by conjugation. Let $\mathcal{S}$ be the smooth functions on $G(\mathbb{A}_E)$. An *algebraic representation* $\Xi$ is a representation of $G(E_\infty)$ on $\mathbb{C}^d$ by matrices with regular entries; we also write $\Xi$ for its restriction to $G(E)$ and $d\Xi$ for its derivative.

**Definition 6.5.1 (Relative cochain).** A *$q$-cochain* with coefficients in $\Xi$ is an alternating $\mathbb{R}$-multilinear map
$$\omega : \mathfrak{p}^q \to \mathcal{S} \otimes_{\mathbb{C}} \mathbb{C}^d.$$
The differential $d$ is the Chevalley-Eilenberg differential for the action $X \mapsto X \otimes 1 + 1 \otimes d\Xi(X)$, with $X$ acting on $\mathcal{S}$ by the right derivative. A cochain is *of level $U$*, for an open compact $U \le G(\mathbb{A}_{E,f})$, if it is $K_\infty$-equivariant, vanishes when one argument is the identity matrix, and its components are functions $\varphi$ that are left invariant under $G(E)$, right invariant under $U$, and on which the identity matrix of the Lie algebra acts by $-m$ whenever $d\Xi(1) = m$. A cochain of level $U$ is *relatively exact* if it is $0$ in degree $0$, and in degree $q \ge 1$ it is $d\eta$ for a cochain $\eta$ of level $U$.

The cochains of level $U$ and their differential form the relative Lie algebra complex of $(\mathfrak{g}, K_\infty)$ with coefficients in the $G(E)$-invariant, $U$-invariant functions twisted by $\Xi$. By the de Rham theorem its cohomology is the cohomology of the locally symmetric space $G(E) \backslash G(\mathbb{A}_E) / K_\infty U$ with coefficients in the local system of $\Xi$ ([Borel-Wallach, Chapter VII]).

We use three growth conditions. Let $\|g\|$ be a height on $G(\mathbb{A}_E)$. A cochain $\omega$ is *compactly supported* if there is $R$ with $\omega(X)(g) = 0$ whenever $\|g\| > R$. It is *of rapid decay* if all its derivatives decay faster than every power of the height. A function $\varphi$ has *moderate growth* if $|\varphi(g y)| \le C \|y\|^N$ for $y \in G(E_\infty)$.

The infinitesimal character of $\Xi$ at an embedding $\tau : E \to \mathbb{C}$ is the multiset $m_\tau$ by which the Capelli elements act through $d\Xi$. A function $\varphi$ *has infinitesimal character $m$* if the Capelli element at $\tau$ with parameter $u$ acts on $\varphi$ by $\prod_{z \in m_\tau}(u + z)$, for all $\tau$ and $u$.

### The Casimir operator and a resolvent

Fix a *frame* of $\mathfrak{p}$: vectors $e_1, \dots, e_n$ with $X = \sum_j \operatorname{tr}(e_j X)\, e_j$ for all $X \in \mathfrak{p}$. Let $r$ be real. The *shifted Casimir operator* is $\Omega_r = \sum_j (e_j + r \ell(e_j))^2$ acting on $\mathcal{S}$, where $\ell$ is the trace form. For $c \in \mathbb{R}$ put $A = \Omega_r - c$.

**Definition 6.5.2 (Resolvent projection).** Let $N \subseteq \mathcal{S}$ be a subspace and $A$ an operator on $\mathcal{S}$. A *resolvent projection* for $A$ on $N$ is an operator $P$ and two sequences $Q_k$, $S_k$ of operators, all preserving $N$ and commuting with the Lie algebra and with right translations, such that for $\varphi \in N$:
$$\varphi - Q_k \varphi = A(S_k \varphi), \qquad A(P\varphi) = 0, \qquad Q_k\varphi \to P\varphi$$
uniformly on compact sets.

So $P$ projects onto the kernel of $A$, and the defect $\varphi - Q_k\varphi$ lies in the image of $A$. We need the space $N$ to be large enough.

**Definition 6.5.3 (Good space).** A subspace $N \subseteq \mathcal{S}$ is *good for $r$* if it is stable under the Lie algebra, its elements have moderate growth, every $\varphi \in N$ on which the identity matrix acts by $-r$ is square integrable modulo the center (after the twist by $|\det|^{r}$), and $N$ contains every function of some level, left invariant under $G(E)$, with the identity acting by $-r$, that vanishes where the height is large.

**Lemma 6.5.4 (Resolvent of the Casimir operator).** Let $a \ge 1$, $r \in \mathbb{R}$, $e$ a frame of $\mathfrak{p}$ and $c \in \mathbb{R}$. Then there is a good space $N$ for $r$ and a resolvent projection for $\Omega_r - c$ on $N$.

Lean: `UpperTheory.V.Cj.H.fnProj`.

*Proof.* Twist by the character $|\det|^{s}$ that turns the central action $-r$ into $0$; this carries good spaces and resolvent projections for $r$ to those for $0$. For $r = 0$ the functions on which the center acts trivially lie, after the growth conditions, in $L^2(G(E) \backslash G(\mathbb{A}_E)^1)$. There the Casimir operator is symmetric, and its spectral theory gives the projection $P$ onto the eigenspace for the eigenvalue $c$, with resolvent operators $Q_k$, $S_k$ that converge to $P$. $\square$

### The Hodge decomposition

**Theorem 6.5.5 (Harmonic representative).** Let $a \ge 1$, $e$ a frame of $\mathfrak{p}$, $U$ open compact, and $\Xi$ an algebraic representation on which the identity matrix of the Lie algebra acts by a real scalar $r$. Let $\alpha$ be a closed, compactly supported $q$-cochain of level $U$. Then there is a $q$-cochain $h$ of level $U$ such that $h$ is closed and coclosed (for the adjoint of $d$ with respect to $e$), its components are in the span of the square integrable functions, they have moderate growth, and $\alpha - h$ is relatively exact.

Lean: `UpperTheory.V.Cj.H.hodgeEx`.

*Proof.* The Casimir operator acts on $\Xi$ by a scalar; let $c$ be the scalar for the shift by $-r$. Take $N$ and the resolvent projection $(P, Q_k, S_k)$ for $A = \Omega_r - c$ given by the lemma, and apply the operators to the components of $\alpha$. They commute with $d$, so $P\alpha$, $Q_k\alpha$ and $S_k\alpha$ are closed cochains of level $U$. On closed cochains of level $U$, the operator $A$ has relatively exact values: this is the Kuga formula, which says that the Casimir operator of the coefficients acts as the Laplacian $dd^* + d^*d$ on cochains, up to the constant $c$. So $\alpha - Q_k\alpha = A(S_k\alpha)$ is relatively exact. Put $h = P\alpha$. Then $(\alpha - h) - (Q_k\alpha - h)$ is relatively exact for every $k$, and $Q_k\alpha - h \to 0$ uniformly on compact sets. A closed cochain that differs by exact cochains from a sequence that tends to $0$ is exact; so $\alpha - h$ is relatively exact. Finally $A h = 0$, and $h$ has square integrable values; by the second part of the Kuga formula this forces $d^* h = 0$. Moderate growth holds since $N$ is good. $\square$

**Theorem 6.5.6 (Automorphic representatives).** Let $E$ be totally complex, $a \ge 1$, $\Xi$ an algebraic representation and $m$ the negative of its infinitesimal character, so that $\Xi$ has infinitesimal character $-m_\tau$ at each $\tau$. For each $q$ there is a space $M$ of $q$-cochains with these properties:

- $M$ is stable under right translation by $G(\mathbb{A}_{E,f})$;
- every $\omega \in M$ is closed and of some level;
- the components of every $\omega \in M$ are automorphic forms with infinitesimal character $m$;
- an element of $M$ that is relatively exact (for some level) is $0$;
- every closed, compactly supported cochain $\alpha$ of some level is $\omega + {}$(a relatively exact cochain) for some $\omega \in M$.

Lean: `UpperTheory.V.Cj.partH`.

So $M$ maps injectively to cohomology, and its image contains the image of compactly supported cohomology. This is Borel's theorem that compactly supported classes have square integrable harmonic representatives, in the adelic form.

*Proof.* Choose a frame $e$ and let $r$ be the real scalar by which the identity acts on $\Xi$. Let $H$ be the space of harmonic cochains: closed, coclosed, of some level, with square integrable components that are automorphic forms with infinitesimal character $m$. It is stable under translation, and it is semisimple as a representation of $G(\mathbb{A}_{E,f})$: each stable subspace has a stable complement, because $H$ carries an invariant positive definite Petersson form and each vector is fixed by an open compact subgroup with finite-dimensional fixed space. Let $H_0 \subseteq H$ be the relatively exact elements; it is a stable subspace. Let $M$ be a stable complement of $H_0$ in $H$. Then elements of $M$ that are exact are $0$. Given $\alpha$ closed and compactly supported of level $U$, the harmonic representative $h$ of the theorem above is closed and coclosed with square integrable components of moderate growth. Such components satisfy the Casimir equation, so they have infinitesimal character $m$, and being of moderate growth and finite under the center and $K_\infty$, they are automorphic forms. So $h \in H$. Write $h = h_0 + \omega$ with $h_0 \in H_0$, $\omega \in M$; then $\alpha - \omega$ is relatively exact. $\square$

### Conjugate coefficients

Let $\sigma$ be an automorphism of $\mathbb{C}$, and let $\Xi$, $\Xi'$ be algebraic representations of the same dimension with $\Xi'(\gamma) = \sigma(\Xi(\gamma))$, entrywise, for $\gamma \in G(E)$. The cohomology of level $U$ with coefficients in $\Xi$ is also the group cohomology of $G(E)$ with values in the functions $G(\mathbb{A}_{E,f})/U \to \mathbb{C}^d$, twisted by $\Xi$ (as in [the section on level](/entry/coh-bound-free/)). A closed cochain $\alpha$ of level $U$ has a *period cocycle*: a group cocycle $c_\alpha$ that represents its class under this identification. Two closed cochains $\alpha$ for $\Xi$ and $\beta$ for $\Xi'$ are *$\sigma$-related at level $U$* if both have level $U$ and $c_\beta - \sigma(c_\alpha)$ is a coboundary for some choice of period cocycles. They are *$\sigma$-related* if they are $\sigma$-related at some level.

Since $\sigma$ acts on the values of a cocycle, the relation transports a class with coefficients in $\Xi$ to a class with coefficients in $\Xi'$. On group cohomology this is clear. The point is to realize the transported class by a form with automorphic coefficients.

**Theorem 6.5.7 (Conjugate representatives).** Let $E$ be totally complex, $a \ge 1$, $\sigma$, $\Xi$ and $\Xi'$ as above, and $q \ge 0$. Assume:

- (A) for every closed, compactly supported $\alpha$ of level $U$ for $\Xi$, there are $U' \le U$ open compact and a closed, compactly supported $\beta$ for $\Xi'$ that is $\sigma$-related to $\alpha$ at level $U'$.

Let $M$ be a space of closed $q$-cochains of some level for $\Xi'$ such that every closed, compactly supported cochain of some level is congruent to an element of $M$ modulo relatively exact cochains. Then every closed cochain $\omega$ of some level for $\Xi$ that is of rapid decay is $\sigma$-related to some $\beta' \in M$.

Lean: `UpperTheory.V.Cj.relOnto`.

*Proof.* A closed cochain of rapid decay is cohomologous to a compactly supported one: there is a closed, compactly supported $\alpha$ of the same level with $\omega - \alpha$ relatively exact (Borel). By (A) there is a closed, compactly supported $\beta$ for $\Xi'$, $\sigma$-related to $\alpha$ at a smaller level $U'$. By the hypothesis on $M$ there is $\beta' \in M$ with $\beta - \beta'$ relatively exact. The relation is linear, and two exact closed cochains are always $\sigma$-related, since both have coboundary period cocycles. So $\omega - \alpha$ and $\beta' - \beta$ are $\sigma$-related, and adding the relation between $\alpha$ and $\beta$ gives that $\omega$ and $\beta'$ are $\sigma$-related. $\square$

Together, the last two theorems give the cohomological part of Clozel's argument: apply the second with $M$ the space of automorphic representatives for $\Xi'$ of the first.

**Remark 6.5.8 (Formalization).** In the last theorem, hypothesis (A) is the first premise of the statement, not a hypothesis on the data. The Kuga formula, the limit argument for exact cochains, the existence of a frame, the semisimplicity of the harmonic space, and the passage from harmonic forms to automorphic forms are inputs of the Hodge theorem and of the theorem on automorphic representatives ([CasimirResolventProjection.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ConjugateRepresentations/LocalLimitConjugates/CasimirResolventProjection.lean#L502)). We did not unfold the construction of the resolvent for $r = 0$, the period cocycle (defined by a zig-zag through a geometric double complex), or Borel's comparison of rapid decay and compact support. The space $\mathfrak{p}$ is the full space of Hermitian matrices, and the condition that cochains vanish on the identity matrix makes the complex relative to the center as well.
