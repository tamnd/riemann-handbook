---
title: Ingredients of Zuckerman tensoring
decls:
  - CompanionTheory.Zuck.zuckerman_ingredients
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Ingredients of Zuckerman tensoring

The Pieri rules of the next section rest on one structural fact: if $\sigma$ is a discrete series of $G = \mathrm{U}(r+k, r+1)$ with a large gap, and $F$ is the standard representation, its dual or an exterior power of the standard representation, then $F \otimes \sigma$ is a finite direct sum of discrete series, whose parameters are the shifts of the parameter of $\sigma$ by the weights of $F$. This is Zuckerman's tensoring principle for discrete series. This section collects the twenty-four statements from which the decomposition is assembled and proves that they all hold. The decomposition is used for the Pieri moments of [the next section](/entry/moment-first-length/) and, through the global hypotheses, for [the weighted bound on rotated points](/entry/weighted-bound-rotated-uniform/). Both are parts of [HypsAlt is nonempty](/step/nonempty-hyps/).

### The category of tensor products

Fix $k, r$ and $n = 2r + k + 1$, and let $G = \mathrm{U}(H_{k,r})$ as in [the first section](/entry/bounded/). We use the notation for discrete series of [the second section](/entry/bessel-map-uniq-gap/).

**Definition 6.5.1 (Finite-dimensional representation of polynomial growth).** A *finite representation* $F$ of $G$ is a finite index set $\iota_F$ and a matrix-valued map $\rho_F : G \to M_{\iota_F}(\mathbb{C})$ together with a degree $\deg F \in \mathbb{N}$. It is *admissible* if $\rho_F(1) = 1$, $\rho_F(gh) = \rho_F(g) \rho_F(h)$, $\rho_F$ is smooth, and $\| \rho_F(g) \|$ grows at most like $\|g\|^{\deg F}$.

The examples are the trivial representation, the standard representation $V$ on $\mathbb{C}^n$ and its dual $V^*$, the exterior powers $\Lambda^l V$, with basis indexed by the $l$-element subsets of $\{0, \dots, n-1\}$, and tensor products $F \otimes F'$.

**Definition 6.5.2 (Objects and morphisms).** An *object* is a pair $X = (F, U)$ of a finite representation $F$ and a unitary representation $U$ of $G$ on $\mathcal{H}_U$. Its space is $M(X) = (\mathcal{H}_U^\infty)^{\iota_F}$, the $\iota_F$-tuples of smooth vectors, with the action $g \cdot x = \rho_F(g) \, (U(g) x_c)_c$. A *morphism* $X \to Y$ is a linear map $f : M(X) \to M(Y)$ that is continuous for the word seminorms and commutes with the action of $G$. We write $\mathbf{1}(U) = (\mathrm{triv}, U)$.

So $M(F, U)$ is the space of smooth vectors of $F \otimes U$, and morphisms are continuous intertwiners. The category is $\mathbb{C}$-linear: morphisms can be added, scaled and composed, and identities are morphisms.

**Definition 6.5.3 (Casimir operators).** For $Y \in M_n(\mathbb{C})$ let $L_X(Y)$ be the action of the complexified Lie algebra element $Y$ on $M(X)$, the sum of $d U(Y)$ on each coordinate and of $d\rho_F(Y)$ on the index. Put
$$\Omega_X = \sum_{a, b} L_X(E_{ab}) \, L_X(E_{ba}),$$
with $E_{ab}$ the matrix units. Let $\Omega^U_X$ be the same sum with $d U$ alone, and for finite representations $F, F'$ let $Q(F, F') = \sum_{a,b} d\rho_F(E_{ab}) \otimes d\rho_{F'}(E_{ba})$.

For a discrete series with Harish-Chandra parameter $\mu$, the Casimir acts by the scalar $c(\mu) = \sum_a \mu_a^2 - \sum_a \rho_a^2$, where $\rho$ is the half sum for $\mathrm{GL}_n$. This is the infinitesimal character of the discrete series, read on the Casimir ([discrete series and formal degrees](/learn/real-groups/#discrete-series-and-formal-degrees)).

**Definition 6.5.4 (Decomposition).** An object $X$ *decomposes* as $\bigoplus_{s \in S} T_s$, for a finite set $S$, if there are morphisms $i_s : T_s \to X$ and $p_s : X \to T_s$ with $p_s i_s = 1$, $p_t i_s = 0$ for $s \neq t$, and $\sum_s i_s p_s = 1$. A family $(T_s)$ is *simple* if each $M(T_s) \neq 0$, each endomorphism of $T_s$ is a scalar, and there are no nonzero morphisms $T_s \to T_t$ for $s \neq t$.

### The twenty-four statements

**Theorem 6.5.5 (Ingredients of Zuckerman tensoring).** The following statements hold for all $k, r$.

1. (Infinitesimal character.) A discrete series with Harish-Chandra parameter $\mu$ has infinitesimal character $\mu$.
2. (Decomposition from injectivity.) In a $\mathbb{C}$-linear category, let $(T_s)_{s \in S}$ be a finite simple family and $X$ an object such that: a vector of $M(X)$ killed by all morphisms $X \to T_s$ is $0$; any two morphisms $X \to T_s$ are linearly dependent; and each $T_s$ has a nonzero morphism to $X$. Then $X$ decomposes as $\bigoplus_s T_s$.
3. (Decomposition from a trace identity.) A decomposition follows from a simple family and an identity of Casimir traces of the form used in the counting statement 24.
4. (Category.) Objects and morphisms form a $\mathbb{C}$-linear category.
5. to 8. (Admissibility.) The trivial representation, $V$ and $V^*$, each $\Lambda^l V$, and the tensor product of two admissible finite representations are admissible.
9. (Matrices.) A matrix $A$ with $A \rho_F(g) = \rho_{F'}(g) A$ for all $g$ acts as a morphism $(F, U) \to (F', U)$.
10. (Unitary isomorphisms.) A unitary intertwiner $U \cong U'$ gives an isomorphism $(F, U) \cong (F, U')$.
11. (Lie algebra.) A morphism between objects with admissible finite parts commutes with each $L(Y)$.
12. (Casimir splitting.) For admissible $F, F'$:
$$\Omega_{(F \otimes F', U)} = \Omega_{(F, U)} \otimes 1 + 1 \otimes \Omega_{(F', U)} - \Omega^U_{(F \otimes F', U)} + 2\, Q(F, F').$$
13. (Casimir on discrete series.) If $k \geq 1$ and $U$ is a discrete series with parameter $\mu$, then $\Omega^U_{(F, U)} = c(\mu)$ and $\Omega_{\mathbf{1}(U)} = c(\mu)$.
14. (Exterior powers.) Let $j : \Lambda^{m+1} V \to \Lambda^m V \otimes V$ be the matrix with entry $(-1)^{\#\{b \in I : b < a\}}$ at $((I, a), J)$ when $a \notin I$ and $J = I \cup \{a\}$, and $0$ otherwise. Then $j$ and $j^{\mathsf T}$ intertwine the actions of $\mathrm{GL}_n$, and $j^{\mathsf T} j = m + 1$ on $\Lambda^{m+1} V$.
15. (Exterior quadratic term.) $Q(\Lambda^m V, V) = 1 - j j^{\mathsf T}$.
16. (Schur.) Discrete series with pairwise distinct parameters and one sign vector form a simple family.
17. (Adjunction.) Morphisms $(F, U) \to \mathbf{1}(U')$ correspond bijectively and linearly to morphisms $\mathbf{1}(U) \to (F^\vee, U')$, for $F = V$ and for $F = V^*$.
18. (Multiplicity one.) Let $F$ be $V$ or $V^*$, and $F^\vee$ the other one. Let $B$ and $T$ be unitary representations with Casimir scalars $c_B$ and $c_T$, with $\Omega^B$ the scalar $c_B$ on every $(F', B)$, and let $(B_t)$ be a family with Casimir scalars $c_t \neq 2 c_B - c_T$ whose morphisms detect vectors of $(F^\vee, B)$. If the endomorphisms of $\mathbf{1}(B)$ are scalars, $T$ is a discrete series and $\mathbf{1}(B) \to (F^\vee, T)$ has a nonzero morphism, then any two morphisms $\mathbf{1}(T) \to (F, B)$ are linearly dependent.
19. (Injectivity.) If $X = (F, U)$ with $F$ admissible and $U$ a discrete series whose matrix coefficients decay like $\|g\|^{-m}$ with $m \geq \deg F + n^2 + 1$, and each product of a $K$-finite coefficient of $U$ with a matrix entry of $F$ is a finite sum of coefficients of the discrete series $T_s$, then the morphisms $X \to \mathbf{1}(T_s)$ detect vectors.
20. (Occurrence.) Under the same decay, if a coefficient of a discrete series $T$ is a finite sum of products of $K$-finite coefficients of $U$ with matrix entries of $F$, then there is a nonzero morphism $X \to \mathbf{1}(T)$.
21. (Zuckerman hypothesis.) If discrete series with gap above a threshold $t$ exist and are realized in tensor products, then for $U$ a discrete series with parameter $\mu$ and gap $h > t + 1$, and for $V$ or $V^*$, there are discrete series $T_s$ with parameters $\mu \pm e_s$, one for each $s$ for which $\mu \pm e_s$ is a Harish-Chandra parameter, that satisfy the coefficient conditions of 19 and 20.
22. (Tensor products.) Decompositions of $(F, U)$ and of $(F', T_a)$ into objects with scalar Casimir combine into a decomposition of $(F \otimes F', U)$ on which the partial Casimir acts by the scalar of the first factor, and symmetrically.
23. (Raw form.) A decomposition of $(F, U)$ into objects $\mathbf{1}(T_a)$ gives an explicit system of inclusion and projection maps of $\rho_F \otimes U$.
24. (Counting.) Let $\mu$ satisfy $\mu_a - \mu_c \geq 2$ for $a < c$. Put $\mu_I = \mu + \sum_{a \in I} e_a$ for an $m$-element subset $I$. Then for each $(m+1)$-element subset $J$,
$$\sum_{(I, s) : \mu_I + e_s = \mu_J} \big( c(\mu_I) + c(\mu + e_s) + 2 - c(\mu) - c(\mu_J) \big) = 2(m + 1),$$
and the same sum at any $\nu$ that is not of the form $\mu_J$ is $0$.

Lean: `CompanionTheory.Zuck.zuckerman_ingredients`.

*Proof.* Each item is a separate result, and the theorem collects them. Statement 1 is the infinitesimal character of the discrete series, proved through Harish-Chandra's character theory ([discrete series and formal degrees](/learn/real-groups/#discrete-series-and-formal-degrees)). Statement 2 is linear algebra: the projections to the $T_s$ are well defined because each space of morphisms has dimension at most one, they detect vectors by hypothesis, and simplicity makes $p_t i_s = \delta_{st}$ after scaling. Statements 4 to 11 are direct verifications on matrices and smooth vectors; for 11, differentiate the equivariance $f(g \cdot x) = g \cdot f(x)$ along $\exp(tY)$. Statement 12 is the expansion of $\sum_{a,b} (A_{ab} + B_{ab})(A_{ba} + B_{ba})$, where $A$ is the action on $F$ and $B$ on $F' \otimes U$, with the cross terms giving $2Q$ and the double count of $U$ removed by $-\Omega^U$. Statement 13 combines statement 1 with Harish-Chandra's isomorphism for the center of the enveloping algebra. Statements 14 and 15 are identities of the exterior algebra: $j^{\mathsf T}$ is the wedge product, and $Q$ on $\Lambda^m V \otimes V$ is $1$ minus $j j^{\mathsf T}$, which is $m+1$ times the projection onto the image of $j$. Statement 16 is Schur's lemma for irreducible unitary representations, with distinct infinitesimal characters for distinct parameters. Statement 17 is the duality $\mathrm{Hom}(V \otimes A, B) \cong \mathrm{Hom}(A, V^* \otimes B)$. Statement 18 is proved elsewhere in the development from statements 4, 9, 11 and 12, the action of the Lie algebra on $V$, and the fact that a nonzero morphism out of $\mathbf{1}(T)$ for a discrete series $T$ has zero kernel. Statements 19 and 20 are proved elsewhere from the decay of matrix coefficients and the coefficient identities. Statement 21 is proved elsewhere; it is the form of Zuckerman's translation principle used here. Statements 22 and 23 assemble decompositions. Statement 24 is a finite computation with $c(\mu) = \sum \mu_a^2 - \sum \rho_a^2$. Let $\mu_I + e_s = \nu$. If $s \notin I$, then $c(\nu) - c(\mu_I) = 2\mu_s + 1 = c(\mu + e_s) - c(\mu)$, so the bracket is $2$; there are $m + 1$ such pairs for $\nu = \mu_J$. If $s \in I$, then $c(\nu) - c(\mu_I) = 2\mu_s + 3$, and the bracket is $0$. The condition $\mu_a - \mu_c \geq 2$ makes the two cases distinguishable from $\nu$. $\square$

**Remark 6.5.6.** These statements combine into the following form of the tensoring principle. Let $\sigma$ be a discrete series with parameter $\mu$ and gap above a threshold $t(\varepsilon) + n^2 + 3 + l$, with $\mu_a - \mu_c \geq l + 1$ for $a < c$. Then $\Lambda^l V \otimes \sigma$ decomposes as the sum of the discrete series with parameters $\mu + \sum_{a \in I} e_a$ over the $l$-element subsets $I$, and $V^* \otimes \sigma$ as the sum of those with parameters $\mu - e_s$. Zuckerman proved this for regular parameters in the same Weyl chamber as $\mu$; the gap hypothesis ensures that all shifted parameters stay regular and in the chamber.

**Remark 6.5.7 (Formalization).** The theorem is a structure of twenty-four fields, and its proof fills each field with a result proved elsewhere. Most of them come from wrappers in the folder `CompanionTheory/SpectralGeometry/LocalGlobalProofs/StableLattices/`, whose name is unrelated to representation theory ([ZuckermanIngredients.lean](lean:CompanionTheory/AutomorphicTheory/ZuckermanCommutation/ZuckermanFunctors/ZuckermanIngredients.lean#L27)). The proofs sketched above are the classical arguments behind the fields; we have not opened all twenty-four proofs. Statement 3 and statement 21 are stated with more data than given above. The decomposition is combined with library bounds in `ZuckermanGapSmall.lean` (line 7), which is the place where this theorem is used.
