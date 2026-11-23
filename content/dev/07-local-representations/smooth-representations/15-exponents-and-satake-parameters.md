---
title: Exponents and Satake parameters
decls:
  - GlobalTheory.CompanionTheory.GlFrob.embedding_of_exponent
  - GlobalTheory.CompanionTheory.LocGL.expSat
  - GlobalTheory.T.exponent_to_saturation
  - GlobalTheory.CompanionTheory.ExpProd.expToSat
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Exponents and Satake parameters

An exponent of a representation $\pi$ of $\mathrm{GL}_n$ over a $p$-adic field is a character of the diagonal torus that occurs in the Jacquet module of $\pi$ for the Borel subgroup. This section proves three facts about exponents. First, an exponent gives an embedding of an irreducible $\pi$ into a principal series. Second, if the exponent is unramified and its values at a uniformizer have decreasing absolute values, then $\pi$ is spherical and its Satake parameter is the exponent. Third, if such a $\pi$ is a subquotient of a product $\sigma_1 \times \dots \times \sigma_c$, then every $\sigma_i$ is spherical and the Satake parameters of the $\sigma_i$ together give the exponent. The third fact is the local input that reads Satake parameters off the Jacquet module in the base change argument behind the step [EveryCharacter](/step/every-character/). For background see [parabolic induction and the Jacquet module](/learn/representations/#parabolic-induction-and-the-jacquet-module).

### Setting

Let $k$ be a nonarchimedean local field of characteristic $0$ with ring of integers $\mathcal{O}$, uniformizer $\varpi$ and residue field of order $q$. Let $G_n = \mathrm{GL}_n(k)$, $K = \mathrm{GL}_n(\mathcal{O})$, $B$ the upper triangular Borel subgroup, $N$ its unipotent radical and $T$ the diagonal torus. Let $\delta_B$ be the modulus character of $B$.

**Definition 1.15.1 (Jacquet module and exponents).** For a representation $\pi$ of $G_n$ on $V$, the *Jacquet module* $r_B(\pi)$ is the representation of $T$ on $V/V(N)$ given by $t \mapsto \delta_B(t)^{-1/2}\pi(t)$. For characters $\xi_1, \dots, \xi_n$ of $k^\times$ put $\xi(t) = \prod_i \xi_i(t_i)$ for $t = \mathrm{diag}(t_1, \dots, t_n)$. We say that $\xi$ is an *exponent* of $\pi$ if there is a nonzero $v \in r_B(\pi)$ that lies, for every $t \in T$, in the generalized eigenspace of $r_B(\pi)(t)$ for the eigenvalue $\xi(t)$.

Here $V(N)$ is the span of the vectors $\pi(u)v - v$ for $u \in N$, as in Section 12. Let $\xi_1 \times \dots \times \xi_n$ be the normalized parabolic induction of $\xi$ from $B$ to $G_n$. A character $\xi_i$ is *unramified* if it is trivial on $\mathcal{O}^\times$. For an unramified $\xi_i$ there is the number $\xi_i(\varpi)$, and $\xi_i$ is determined by it.

**Definition 1.15.2 (Satake parameter).** For $0 \leq j \leq n$ let $T_j \in \mathcal{H}(G_n, K)$ be the indicator function of $K\,\mathrm{diag}(\varpi, \dots, \varpi, 1, \dots, 1)\,K$, with $j$ entries $\varpi$. Let $b$ be a multiset of $n$ elements of $\mathbb{C}^\times$. A nonzero vector $x \in V^K$ is a *Satake vector* with parameter $b$ if
$$T_j \cdot x = q^{j(n-j)/2}\,e_j(b)\,x \qquad (0 \leq j \leq n),$$
where $e_j$ is the $j$-th elementary symmetric function. A smooth $\pi$ *has Satake parameter* $b$ if $V^K \neq 0$ and every nonzero vector of $V^K$ is a Satake vector with parameter $b$.

A Satake vector determines its parameter, since a multiset of $n$ numbers is determined by its elementary symmetric functions. For irreducible $\pi$ we also say that $\pi$ has Satake parameter $\alpha = (\alpha_1, \dots, \alpha_n)$ when $\pi$ is spherical and is a subquotient of the unramified principal series with $\xi_i(\varpi) = \alpha_i$. The two notions agree by the theorem of Satake (1963), in the form of Cartier (1979), Section 4.

### The embedding

**Theorem 1.15.3 (Inputs on Jacquet modules).** Let $\pi$ be a smooth representation of $G_n$ and let $T_m = T \cap K_m$, where $K_m = 1 + \varpi^m M_n(\mathcal{O})$.

1. The groups $T_{m+1}$ decrease in $m$. For $m \leq m'$ and $u \in T_{m+1}$, some power $u^N$ with $N > 0$ lies in $T_{m'+1}$.
2. Every vector of $r_B(\pi)$ is fixed by $T_m$ for some $m \geq 1$.
3. If $\pi$ is admissible, the space of $T_m$-fixed vectors of $r_B(\pi)$ is finite-dimensional for every $m \geq 1$.
4. Let $\Lambda$ be a group acting on $M$ by commuting operators, with a decreasing sequence of subgroups $U_m$ as in item 1, such that every vector is fixed by some $U_m$ and every space $M^{U_m}$ is finite-dimensional. If a character $\chi$ of $\Lambda$ has a nonzero generalized eigenvector in $M$, there is a nonzero functional $f$ on $M$ with $f(\lambda w) = \chi(\lambda) f(w)$.
5. (Frobenius reciprocity.) A nonzero functional $f$ on $r_B(\pi)$ with $f \circ r_B(\pi)(t) = \xi(t) f$ gives a nonzero $G_n$-map $\pi \to \xi_1 \times \dots \times \xi_n$.

Item 2 holds as $\pi$ is smooth and the map to $V/V(N)$ is onto. Item 3 is Jacquet's theorem that the Jacquet module of an admissible representation is admissible; see Casselman (1980), Section 2, and Bernstein and Zelevinsky (1977), Section 2. Item 4 is linear algebra on the finite-dimensional spaces $M^{U_m}$. Item 5 is Frobenius reciprocity for normalized induction, Bernstein and Zelevinsky (1977), Proposition 1.9.

**Theorem 1.15.4 (Embedding by an exponent).** Let $\pi$ be a smooth, admissible and irreducible representation of $G_n$. Let $\xi_1, \dots, \xi_n$ be smooth characters of $k^\times$, and assume $\xi$ is an exponent of $\pi$. Then there is an injective $G_n$-map $\pi \to \xi_1 \times \dots \times \xi_n$.

Lean: `embedding_of_exponent`.

*Proof.* The operators $r_B(\pi)(t)$ commute, as $T$ is commutative. By inputs 1, 2 and 3, the action of $T$ on $r_B(\pi)$ satisfies the conditions of input 4 with $U_m = T_{m+1}$. Input 4 gives a nonzero functional $f$ with $f \circ r_B(\pi)(t) = \xi(t)f$. Input 5 gives a nonzero $G_n$-map $F \colon \pi \to \xi_1 \times \dots \times \xi_n$. The kernel of $F$ is a subrepresentation of the irreducible $\pi$, and it is not all of $\pi$. So the kernel is $0$. $\square$

### Decreasing exponents

**Theorem 1.15.5 (Inputs on unramified products).** Let $\xi_1, \dots, \xi_n$ be unramified characters with $|\xi_1(\varpi)| \geq |\xi_2(\varpi)| \geq \dots \geq |\xi_n(\varpi)|$. Let $\mathfrak{m}$ be the multiset of the one-point segments $\{\xi_i\}$.

1. There is an irreducible representation $L(\mathfrak{m})$ of $G_n$ in the Langlands classification, and every representation in the class $L(\mathfrak{m})$ is the unique irreducible subrepresentation of $\xi_1 \times \dots \times \xi_n$.
2. A smooth $\pi$ lies in the class $L(\mathfrak{m})$ if and only if $\pi$ has Satake parameter $(\xi_1(\varpi), \dots, \xi_n(\varpi))$.

Item 1 is the Langlands classification for $\mathrm{GL}_n$ in the language of segments, Zelevinsky (1980), Section 6 and Section 9, in the case where all segments have length one. Item 2 is the description of the unramified representations of $\mathrm{GL}_n$, Casselman (1980), Section 3, together with item 1.

**Theorem 1.15.6 (Exponents give Satake parameters).** Let $\pi$ be a smooth, admissible and irreducible representation of $G_n$. Let $\xi_1, \dots, \xi_n$ be unramified characters with $|\xi_1(\varpi)| \geq \dots \geq |\xi_n(\varpi)|$, and assume $\xi$ is an exponent of $\pi$. Then $\pi$ has Satake parameter $(\xi_1(\varpi), \dots, \xi_n(\varpi))$.

Lean: `expSat`.

*Proof.* Unramified characters are smooth. The theorem on embedding by an exponent gives an injective map $\pi \to \xi_1 \times \dots \times \xi_n$. By input 1 there is an irreducible $\lambda$ in the class $L(\mathfrak{m})$, and $\lambda$ is the unique irreducible subrepresentation of the product. The image of $\pi$ is an irreducible subrepresentation, so $\pi \cong \lambda$. Hence $\pi$ is in the class $L(\mathfrak{m})$, and input 2 gives the claim. $\square$

### Exponents of subquotients of products

Now let $E$ be a number field, $w$ a finite place of $E$ and $k = E_w$.

**Theorem 1.15.7 (Inputs on spherical vectors in products).** Let $N_1 + \dots + N_c = n$ and let $\sigma_i$ be smooth irreducible representations of $G_{N_i}$.

1. Let $P$ be smooth and irreducible, and let $\xi_i$ be unramified. If some nonzero $y \in r_B(P)$ satisfies $r_B(P)(t)y = \xi(t)y$ for all $t$, then $\xi$ is an exponent of $P$.
2. Smooth irreducible representations of $G_n$ are admissible.
3. For irreducible $P$, having Satake parameter $\alpha$ in the sense of subquotients is the same as having Satake parameter given by the multiset of the $\alpha_i$ in the sense of Satake vectors.
4. If $S$ is smooth and $f \colon S \to P$ is onto, every $K$-fixed vector of $P$ is $f(u)$ for some $K$-fixed $u \in S$.
5. If $u$ is a nonzero $K$-fixed vector of $\sigma_1 \times \dots \times \sigma_c$, there are multisets $b_i$ such that $\sigma_i$ has Satake parameter $b_i$ for each $i$, and $u$ is a Satake vector with parameter $b_1 + \dots + b_c$.
6. If $f$ is a $G_n$-map and $u$ is a Satake vector with parameter $b$ with $f(u) \neq 0$, then $f(u)$ is a Satake vector with parameter $b$.

Item 1 holds since an eigenvector is a generalized eigenvector. Item 2 is the admissibility theorem of Bernstein (1974) and Jacquet; see Bernstein and Zelevinsky (1976), Section 3. Item 4 uses the averaging operator over $K$, which commutes with $f$. Item 5 is the computation of the Hecke algebra action on spherical vectors of induced representations, Cartier (1979), Section 4. Item 6 is clear, as $f$ commutes with $T_j$.

**Theorem 1.15.8 (Exponents and saturation).** Let $N_1 + \dots + N_c = n$, let $\sigma_i$ be smooth irreducible representations of $\mathrm{GL}_{N_i}(E_w)$, and let $P$ be a smooth irreducible representation of $\mathrm{GL}_n(E_w)$. Let $\xi_1, \dots, \xi_n \in \mathbb{C}^\times$ with $|\xi_1| \geq \dots \geq |\xi_n|$, and let $\chi_i$ be the unramified character with $\chi_i(\varpi) = \xi_i$. Assume:

1. $P$ is a subquotient of $\sigma_1 \times \dots \times \sigma_c$;
2. some nonzero $y \in r_B(P)$ satisfies $r_B(P)(t) y = \chi(t) y$ for all $t \in T$.

Then every $\sigma_i$ is spherical, and there are multisets $b_i$ such that $\sigma_i$ has Satake parameter $b_i$ and $b_1 + \dots + b_c = \{\xi_1, \dots, \xi_n\}$.

Lean: `expToSat` (also `exponent_to_saturation`).

*Proof.* By input 1, $\chi$ is an exponent of $P$, and $P$ is admissible by input 2. The theorem on exponents and Satake parameters shows that $P$ has Satake parameter $(\xi_1, \dots, \xi_n)$. By input 3 there is a Satake vector $x$ of $P$ with parameter $\{\xi_1, \dots, \xi_n\}$. Write $P$ as a quotient $f \colon S \to P$ of a subrepresentation $S$ of the product. The product is smooth, so $S$ is smooth. By input 4 there is a $K$-fixed $u \in S$ with $f(u) = x$, and $u \neq 0$ as $x \neq 0$. Input 5 gives multisets $b_i$ such that $\sigma_i$ has Satake parameter $b_i$, which makes $\sigma_i$ spherical, and such that $u$ is a Satake vector with parameter $b_1 + \dots + b_c$. A Satake vector in $S$ stays one in the product, so by input 6, $x = f(u)$ is a Satake vector with parameter $b_1 + \dots + b_c$. A Satake vector determines its parameter, so $b_1 + \dots + b_c = \{\xi_1, \dots, \xi_n\}$. $\square$

**Remark 1.15.9 (Formalization).** The three theorems are in [EmbeddingOfExponent.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/EmbeddingOfExponent.lean#L15), [ExpSat.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/ExpSat.lean#L11) and [ExponentToSaturation.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/ExponentToSaturation.lean#L42). The first statement carries the hypothesis `hd1 : ∑ _a : Fin n, 1 = n`, which always holds; it only builds the block structure of the Borel subgroup. The inputs on Jacquet modules are `deep_level_subgroups_filtration`, `jacquet_vector_fixed_deep_level`, `jacquet_module_admissible_fixed`, `generalized_eigenvector_exists`, `jacquet_cuspidal_support_of_functional` and `FrobInv.exists_map_prodIrr`. The inputs on unramified products are `socleOne` and `l_one_satake_bound`. The third theorem is stated for the completion $E_w$ of a number field, though its content is local, and its eigenvector condition is a true eigenvector, not a generalized one; `stdBridge` passes from one to the other. The inputs on spherical vectors are `stdBridge`, `bernsteinZelevinskyFiniteness`, `satBridge`, `exists_mem_fixed_map_eq` and `exists_sat_multiProd`. The wrapper `exponent_to_saturation` is proved by `first | exact …` under `maxHeartbeats 1000000`.
