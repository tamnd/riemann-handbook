---
title: The model and power-sum classes
decls:
  - UpperTheory.Et.etale_duality_trace_isomorphism
  - UpperTheory.Et.D2.intersectionNumber_baseChange
  - UpperTheory.Et.D2.a0
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The model and power-sum classes

This chapter proves three theorems of [[étale cohomology|7YX76G0838]] in an axiomatic model: the proper base change theorem, the finiteness of the cohomology of a proper scheme over an algebraically closed field, and a congruence relation for Frobenius on crystalline periods. The model states the main facts of étale cohomology as a list of axioms. In this section we describe the model and the axioms, and we prove the first and simplest of the axioms that the chapter derives from the others: the existence of power-sum classes of vector bundles. These classes are $k!$ times the components of the Chern character.

We use the model of [the projective bundle formula](/entry/pbf-all/). A *space* is a simplicial presheaf on schemes. A scheme $U$ gives the discrete space $\mathrm{sch}(U)$, and a ring $A$ gives $\mathrm{sp}(A) = \mathrm{sch}(\operatorname{Spec} A)$. For a commutative ring $R$, a *sheaf* $F$ is a sheaf of $R$-modules on the big étale site of schemes, and $H^n(E, F)$ is the cohomology of the space $E$ with coefficients in $F$. A map of spaces $f : E \to E'$ gives a pullback $f^* : H^n(E', F) \to H^n(E, F)$. For $q \geq 1$ and $i \in \mathbb{Z}$, $\mathbb{Z}/q(i)$ is the Tate twist, and we write $H^n(E, \mathbb{Z}/q(i))$. The cup product, the first Chern class $c_1(L) \in H^2(E, \mathbb{Z}/q(1))$ of a line bundle, the space $B\mathrm{GL}_N$ and the direct sum $V \oplus W$ of two maps $E \to B\mathrm{GL}_a$ and $E \to B\mathrm{GL}_b$ are those of [the projective bundle formula](/entry/pbf-all/). A map $V : E \to B\mathrm{GL}_N$ is a *vector bundle of rank* $N$ on $E$.

**Definition 3.1.1 (Equivalence for cohomology).** Let $f : E \to E'$ be a map of spaces and $F$ a sheaf. We say that $f$ is an *equivalence for* $F$ if $f^* : H^n(E', F) \to H^n(E, F)$ is bijective for every $n \in \mathbb{Z}$.

**Definition 3.1.2 (Rings and spaces).** A ring $A$ is *absolutely integrally closed* if every monic polynomial of positive degree over $A$ has a root in $A$. A *strictly henselian* ring is a henselian local ring with a separably closed residue field. A space $E$ is *acyclic* for $q$ if $H^n(E, \mathbb{Z}/q(i)) = 0$ for all $n > 0$ and all $i$. We say that $q$ is *invertible on* $E$ if $q$ is a unit on every scheme over which $E$ has a $0$-simplex. For $E = \mathrm{sch}(U)$ this says that $q$ is a unit on $U$.

An algebraically closed field is absolutely integrally closed. A domain is absolutely integrally closed if and only if it is integrally closed with an algebraically closed fraction field.

**Definition 3.1.3 (The axioms).** We name the following statements. Let $q \geq 1$ and suppose that $q$ is invertible where it is needed.

- A1 to A11 (except A6): cohomology is invariant under quasi-isomorphism of complexes, a smooth surjective map satisfies Čech descent, a levelwise equivalence of spaces is an equivalence, a map of Mayer-Vietoris squares is an equivalence when three of its maps are, a class of positive degree on a scheme dies on an étale surjective cover, a short exact sequence of sheaves gives a long exact sequence, the coefficient ring can be changed, cohomology vanishes in negative degrees and is the group of sections in degree $0$, a map of sheaves that is bijective on sections is bijective on cohomology, and reduction from $\mathbb{Z}/Q$ to $\mathbb{Z}/q$ for $q \mid Q$ respects cup products and $c_1$.
- B1 to B7 (except B6): cohomology of $\operatorname{Spec}$ commutes with filtered colimits of rings (B1). A strictly henselian ring is acyclic for every sheaf (B2). A map over a base is an equivalence if it is an equivalence after base change to every strictly henselian point of the base (B3). An integral surjective map satisfies Čech descent (B4). An absolutely integrally closed domain is acyclic (B5). The cohomology of a field is Galois cohomology (B7).
- C1 to C5: a field algebraic over $k(t)$ with $k$ algebraically closed has cohomological dimension at most $1$ (C1). A Dedekind domain of finite type over an algebraically closed field has cohomological dimension at most $1$ (C2). A base change statement for étale algebras over $T[x]$ with $T$ an absolutely integrally closed local domain (C3). Homotopy invariance for $A \to A[x]$ (C4). The cohomology of $A[x, x^{-1}]$ for $A$ strictly henselian (C5).
- D1: the projective bundle formula. D2: the statement that we prove in this section. D3: a statement about slant products with group homology that this part does not use.
- E1: for a henselian pair $(A, I)$, the map $\mathrm{sp}(A/I) \to \mathrm{sp}(A)$ is an equivalence for $\mathbb{Z}/q(i)$. E2: proper base change. E3: a base change to the generic fibre over an absolutely integrally closed local domain. E4: finiteness.

Statement D1 says this. Let $V$ be a vector bundle of rank $N$ on a space $E$ on which $q$ is invertible, let $\pi : \mathbb{P}(V) \to E$ be its projective bundle and $\xi = c_1(L)$ the first Chern class of its tautological line bundle. Then for all $n, i$ the map
$$
\begin{aligned}
\bigoplus_{j=0}^{N-1} H^{n-2j}(E, \mathbb{Z}/q(i-j)) &\to H^n(\mathbb{P}(V), \mathbb{Z}/q(i)), \\
(a_j) &\mapsto \sum_j \pi^* a_j \cup \xi^j
\end{aligned}
$$
is bijective. Other chapters of this volume prove the axioms A1 to D1, for instance [the projective bundle formula](/entry/projective-bundle-formula-vector-bundle-any-space/). This chapter proves E2 and E4, and its second part proves E1 and E3. Statement B6, $H^1(\operatorname{Spec} A, \mathbb{G}_m) \cong \operatorname{Pic}(A)$, is the last axiom that we name. The finiteness proof uses it.

**Definition 3.1.4 (Chern classes).** Let $V$ be a vector bundle of rank $N$ on a space $E$ on which $q$ is invertible, with $\pi$ and $\xi$ as above. A sequence $c_j \in H^{2j}(E, \mathbb{Z}/q(j))$, $j \geq 0$, is a *sequence of Chern classes* of $V$ if $c_0 = 1$, $c_j = 0$ for $j > N$, and
$$\sum_{j=0}^{N} \pi^* c_j \cdot \xi^{N-j} = 0.$$

The projective bundle formula writes $\xi^N$ in a unique way as a combination of $1, \xi, \dots, \xi^{N-1}$ with coefficients from $E$. So the sequence exists and is unique. This is the definition of A. Grothendieck, *La théorie des classes de Chern*, Bull. Soc. Math. France 86 (1958), §3, up to sign. With our convention a line bundle $L$ has $c_1 = -c_1(L)$, so that the Chern polynomial $c(X) = \sum_j c_j X^j$ of a sum of line bundles $L_1, \dots, L_N$ is $\prod_i (1 - c_1(L_i) X)$.

**Definition 3.1.5 (Newton polynomials).** Let $A$ be a commutative ring and $c(X) = \sum_{j \geq 0} c_j X^j \in A[[X]]$ with $c_0 = 1$. For $k \geq 1$ the $k$-th *Newton polynomial* of $c$ is
$$p_k(c) = \text{the coefficient of } X^k \text{ in } -X c'(X) c(X)^{-1}.$$

If $c(X) = \prod_i (1 - x_i X)$, then $-X c'/c = \sum_i x_i X/(1 - x_i X)$, so $p_k(c) = \sum_i x_i^k$ is the $k$-th power sum. The map $c \mapsto p_k(c)$ commutes with ring maps, and $p_k(c d) = p_k(c) + p_k(d)$ because $-X c'/c$ is a logarithmic derivative. These are the Newton identities ([Polynomials and power series](/learn/algebra/#polynomials-and-power-series)).

**Theorem 3.1.6 (Power-sum classes).** Let $q \geq 1$ and $k \geq 1$, and assume the axioms A1 to C5 and D1. There is a rule $s_k$ that gives for each vector bundle $V$ on a space $E$ a class $s_k(V) \in H^{2k}(E, \mathbb{Z}/q(k))$, with these properties.

1. If $f : E \to E'$ is a map, $V$ is a vector bundle on $E'$, and $q$ is invertible on $E'$, then $f^* s_k(V) = s_k(f^* V)$.
2. If $q$ is invertible on $E$, then $s_k(V \oplus W) = s_k(V) + s_k(W)$.
3. If $q$ is invertible on $E$ and $L$ is a line bundle on $E$, then $s_k(L) = c_1(L)^k$.

Lean: `UpperTheory.Et.D2.a0` (also `UpperTheory.Et.D2.intersectionNumber_baseChange`, a second name).

*Proof.* We follow [the proof in the chapter on étale sheaves](/entry/s57/). The even cohomology groups $H^{2k}(E, \mathbb{Z}/q(k))$ are separate groups, so we first collect them in one commutative ring. By [the ring lemma](/entry/s42/), for each $E$ on which $q$ is invertible there is a commutative ring $R(E)$ with additive maps $\iota_k : H^{2k}(E, \mathbb{Z}/q(k)) \to R(E)$ and $\pi_k : R(E) \to H^{2k}(E, \mathbb{Z}/q(k))$ such that $\pi_k \iota_k$ is the identity, $\iota_0(1) = 1$, $\iota$ sends cup products to products and $c_1^k$ to $\iota_1(c_1)^k$, and pullbacks give ring maps $R(E') \to R(E)$ that commute with $\iota$ and $\pi$. In $R(E)$ the definition of Chern classes reads $\sum_j \iota_j(c_j) \xi^{N-j} = 0$.

Four facts hold in this ring. Chern classes exist and are unique, by D1 as explained above. They are natural: the pullback of a sequence of Chern classes of $V$ is a sequence of Chern classes of $f^* V$. They satisfy the Whitney formula: the Chern polynomial of $V \oplus W$ is the product of the Chern polynomials of $V$ and $W$ ([the Whitney lemma](/entry/s54/)). For a line bundle, $\iota_1(c_1) = -\iota_1(c_1(L))$.

Now let $c(V)$ be the Chern polynomial of $V$ in $R(E)[[X]]$ and put $s_k(V) = \pi_k(p_k(c(V)))$ if $q$ is invertible on $E$, and $s_k(V) = 0$ otherwise. Property 1 follows from naturality, the uniqueness of Chern classes, and the fact that $p_k$ commutes with the ring map $R(E') \to R(E)$. Property 2 follows from the Whitney formula and $p_k(cd) = p_k(c) + p_k(d)$. For property 3, the Chern polynomial of $L$ is $1 - x X$ with $x = \iota_1(c_1(L))$, so $p_k = x^k = \iota_k(c_1(L)^k)$, and $\pi_k$ gives $c_1(L)^k$. $\square$

**Corollary 3.1.7 (Power-sum classes exist).** For $q \geq 1$ and $k \geq 1$ there is a rule $s_k$ with the properties 1 to 3 of the theorem.

Lean: `UpperTheory.Et.etale_duality_trace_isomorphism`.

*Proof.* Other chapters of this volume prove A1 to C5 and D1 as theorems, for instance [the projective bundle formula](/entry/projective-bundle-formula-vector-bundle-any-space/). So the hypotheses of the theorem hold, and the theorem gives $s_k$. $\square$

**Remark 3.1.8.** The property 3 fixes $s_k$ on line bundles, and properties 1 and 2 with the splitting principle fix it on all bundles. So $s_k(V)$ is the $k$-th power sum of the Chern roots of $V$, that is $k! \operatorname{ch}_k(V)$. The value of $s_k$ on a space on which $q$ is not invertible is not fixed by the properties, and we put it equal to $0$.

**Remark 3.1.9 (Formalization).** The names do not match the statement: the corollary is `etale_duality_trace_isomorphism`, the theorem is `intersectionNumber_baseChange` and `a0`, but the statement has no duality, trace, intersection number or base change. The duality axiom E8 is not used in this chapter. The theorem takes 22 hypotheses (A1 to A5, A7 to A11, B1 to B5, B7, C1 to C5 and D1), and [the proof](/entry/s57/) uses only D1 ([InstCommRingR.lean](lean:Development/EtaleCohomology/EtaleSheaves/InstCommRingR.lean#L85)). The wrapper `a0` is `s57`, and `intersectionNumber_baseChange` is `a0` ([A0.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/EtaleAxioms/A0.lean#L6)).
