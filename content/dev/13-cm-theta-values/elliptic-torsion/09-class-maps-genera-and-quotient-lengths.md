---
title: Class maps, genera and quotient lengths
decls:
  - Formalism.L2.GlobalTheoryTheory.Br.symmetric_level_clauses_hold
  - Formalism.L2.GenusGluing.Gen.unimodGenus_iff
  - Formalism.L2.Pj.QAt.qat_of_bridge'
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Class maps, genera and quotient lengths

This section proves three results on lattices that the chapter gives to other chapters. The first proves four properties of the class map of a system of symmetric forms. It is the input of [the forms map from a symmetric comparison](/entry/forms-map-of-symmetric-comparison-lower-map-finite-char/) in the chapter on depth valuations. The second proves that, for the standard [[Hermitian form|48P4A1CX85]] over a CM field, two statements are equivalent: every unimodular lattice is in the genus of the standard lattice, and every unimodular lattice is the image of the standard lattice under an adelic unitary element. It is used by [the theorem that the unimodular lattices form one genus](/entry/unimod-genus-holds/) in Volume 8. The third gives a bound on the lengths of quotients by a family of vectors, from local and archimedean data on a family of functionals. It is used by [the quotient index bound from a family of functionals that cuts out the kernel](/entry/qat-of-kill-detect/) in Volume 14.

### The class map of a symmetric system

We describe the objects only as far as the statement needs them. A *member datum* at a word $u$ has a top level $m$, a CM field $L$ and, at each level $i \le m$, a finite set $\mathrm{Cl}_i$ of classes, a finite stabilizer group $\mathrm{St}_i(c)$ for each class $c$, and a Hermitian lattice $\Lambda_i$ over $L$ with an embedding of $\Lambda_i \otimes \mathbb{Q}$ into the functions on classes. Its image spans a space $F_i$. The datum also has:
- a finite set $\mathrm{Cl}'$ of classes one level below the top, with finite stabilizers $\mathrm{St}'(c)$;
- a map $t : \mathrm{Cl}' \to \mathrm{Cl}_m$ and, for each $c \in \mathrm{Cl}'$, an injective homomorphism $s_c : \mathrm{St}'(c) \to \mathrm{St}_m(t(c))$;
- a space of points with a subspace $P_C$, a Hermitian lattice $\Lambda_P$ over $L$ that spans $P_C$, and a point map $\mathrm{Pt}$ from functions on $\mathrm{Cl}_m$ to points.

When the point map sends the rational vectors of $\Lambda_m$ to rational vectors of $\Lambda_P$, it descends to an $L$-linear map $\mathrm{Pt}_h : \Lambda_m \otimes \mathbb{Q} \to \Lambda_P \otimes \mathbb{Q}$. For an infinite place $v$ of $L$, write $\|x\|_v^2$ for the majorant of a Hermitian lattice at $v$.

A *symmetric system of forms* on the datum is a family of local Hermitian data on the classes at the bottom level and at the top level, tied to the data at the level below the top. We need two of its properties: the class lattices below the top are self-dual, and the values of the forms are invariant under the stabilizers. Both hold for every symmetric system. Two further conditions appear in the statement: the *tie of the lower map*, and the *vanishing on ties*.

**Theorem 7.9.1 (Class map of a symmetric system).** Let $T$ be a symmetric system of forms on a member datum, for any family of characters on the classes. Assume the tie of the lower map and the vanishing on ties. Then:
1. the map $t : \mathrm{Cl}' \to \mathrm{Cl}_m$ is injective;
2. each homomorphism $s_c$ is bijective;
3. for every $\varphi \in F_m$, the point $\mathrm{Pt}(\varphi)$ lies in $P_C$;
4. there is a constant $B$, which depends only on the datum, such that for every proof $h$ of rationality, every infinite place $v$ of $L$ and every $x \in \Lambda_m \otimes \mathbb{Q}$,
$$\|\mathrm{Pt}_h x\|_v^2 \le B\, \|x\|_v^2 .$$

Lean: `Formalism.L2.GlobalTheoryTheory.Br.symmetric_level_clauses_hold`

*Proof.* We prove the four clauses separately. The first two use neither the tie of the lower map nor the vanishing on ties.

Clause 1. Every symmetric system makes the class lattices below the top self-dual for their Hermitian form. Self-duality gives the injectivity of $t$.

Clause 2. Each $s_c$ is injective by the definition of the datum, so the content is surjectivity. It follows from self-duality together with the invariance of the form values under the stabilizers.

Clause 3. Every symmetric system has the following extension property. Let $\kappa$ be an element of the level group of a class below the top, and let $G$ be a finite adelic element that extends $\kappa$ and lies in the unitary group of the top form. Then at every place $G$ lies in the local level group of the top class, and the character of the top class at $G$ equals the character of the lower class at $\kappa$. With the tie of the lower map, this property carries each $\varphi \in F_m$ into $P_C$.

Clause 4. A bound on the norms over each class, together with clauses 1 and 2, gives the bound at each infinite place.

The four clauses together are the claim. $\square$

### Unimodular lattices and genera

Let $F$ be a totally real field and $E/F$ a CM extension: $E$ is a quadratic extension of $F$, the involution $a \mapsto \bar a$ of $E$ has fixed field $F$, $E$ is totally complex, and every complex embedding of $E$ carries the involution to complex conjugation. We also assume that for every maximal ideal $P$ of $\mathcal{O}_E$ there is $\theta \in \mathcal{O}_E$ with $\theta - \bar\theta \notin P$. We call this a *CM datum*. The ring $\mathcal{O}_E$ is a [[Dedekind domain|7NPY2CN5KB]].

On $E^n$ put the standard Hermitian form $h(x, y) = \sum_i \bar x_i y_i$, and let $L_0 = \mathcal{O}_E^n$ be the standard lattice. An $\mathcal{O}_E$-lattice $N \subset E^n$ is *unimodular* if it equals its dual for $h$. Two lattices $N, N'$ are in the *same genus* if for every maximal ideal $P$ of $\mathcal{O}_E$ there is an isometry $g$ of $(E^n, h)$ with $g(N_P) = N'_P$, where $N_P$ is the localization at $P$.

Let $\mathbb{A}_f$ be the finite adeles of $F$, and let $U(\mathbb{A}_f)$ be the group of invertible matrices over $E \otimes_F \mathbb{A}_f$ that preserve $h$. For $x \in U(\mathbb{A}_f)$, let $x L_0$ be the lattice of the vectors $y \in E^n$ with $x^{-1} y$ in the closure of $L_0$. Let $U(F)$ be the group of rational unitary matrices.

**Definition 7.9.2 (Weak approximation).** The unitary group of $h$ has *weak approximation* if for every $x \in U(\mathbb{A}_f)$ and every finite place $v$ of $F$ there is $\gamma \in U(F)$ such that $\gamma^{-1} x$ and $x^{-1} \gamma$ have entries integral at $v$.

**Theorem 7.9.3 (Genus and adelic orbit).** Let $E/F$ be a CM datum and $n \in \mathbb{N}$. The following are equivalent:
1. every unimodular lattice $N \subset E^n$ is in the genus of $L_0$;
2. every unimodular lattice $N \subset E^n$ equals $x L_0$ for some $x \in U(\mathbb{A}_f)$.

Lean: `Formalism.L2.GenusGluing.Gen.unimodGenus_iff`

*Proof.* First, weak approximation holds for every CM datum and every $n$. Fix $x$ and $v$. A shift step gives a diagonal matrix $t$ with entries $t_i \in E$, $\bar t_i t_i = 1$, such that the determinant of $x$ plus the image of $t$ is a unit at $v$. A Cayley step then gives a rational unitary $\gamma$ with $x^{-1}\gamma$ integral at $v$ whenever $1 + x$ is invertible. Together with integrality of the inverse, this gives weak approximation.

Assume 1 and let $N$ be unimodular. Then $N$ is in the genus of $L_0$: at each maximal ideal there is a rational isometry that carries the localization of $L_0$ to that of $N$. Since $N$ and $L_0$ are commensurable, only a finite set of places matters. A gluing step gives $x \in U(\mathbb{A}_f)$ whose component at each place of this set is the chosen isometry, and then $x L_0 = N$.

Assume 2 and let $N$ be unimodular, so $N = x L_0$ with $x \in U(\mathbb{A}_f)$. Fix a finite place $v$. By weak approximation there is $\gamma \in U(F)$ with $\gamma^{-1} x$ and $x^{-1}\gamma$ integral at $v$. Then at the maximal ideals over $v$ the localization of $x L_0$ is the image of the localization of $L_0$ under $\gamma$, and $\gamma$ is an isometry of $(E^n, h)$. So $N$ is in the genus of $L_0$. $\square$

The hypothesis on $\theta - \bar\theta$ says that $E/F$ is unramified at every finite place. Indeed, if $E/F$ is ramified at $P$, the involution acts trivially on $\mathcal{O}_E/P$, so $\theta - \bar\theta \in P$ for every $\theta$. Conversely, at a split or inert prime some $\theta$ has $\theta - \bar\theta \notin P$.

### Lengths of quotients

Let $K$ be a number field, $V$ a finite-dimensional vector space over $K$, $M \subset V$ a finitely generated $\mathcal{O}_K$-module that spans $V$, and $W \subset V$ a subspace. Let $Q = M/(M \cap W)$. It is a finitely generated torsion-free $\mathcal{O}_K$-module, and we write $\rho$ for its rank. For a prime $\lambda$ of $\mathcal{O}_K$, $N\lambda$ is its norm and $\ell_\lambda$ is the [[length|CZSCNZH8VY]] of a module after localization at $\lambda$. Two local statements enter:
- *local length*: if $\mathcal{O}$ is a discrete valuation ring, $Q$ is free of rank $\rho$ over $\mathcal{O}$, $c_1, \ldots, c_\rho$ are linear forms on $Q$ and $\theta_1, \ldots, \theta_\rho \in Q$ with $\det(c_i(\theta_k)) \ne 0$, then the length of $Q / \sum_k \mathcal{O}\theta_k$ is at most the valuation of $\det(c_i(\theta_k))$;
- *descent of lengths*: for a finite extension $K_1/K$, a prime $w$ of $K_1$ over $\lambda$ and $\theta_1, \ldots, \theta_\rho \in M$, the length at $w$ after base change equals $e(w|\lambda)$ times the length at $\lambda$ of $Q / \sum_k \mathcal{O}_K \theta_k$.

In the application, $K$ is a number field attached to a weight family, $V$ is a space of cusp forms of a given level $j$ and weight $\kappa$, $M$ is a lattice in it, and $W$ is a subspace cut out by the data. Each form $F$ has a sup norm $\|F\|_\sigma$ at each complex embedding $\sigma$ of $K$. We write $P(C, A)$ for an explicit quantity that depends on a pair of constants and on the data, and $s$ for the size of the weight.

**Definition 7.9.4 (Bridge).** A *bridge* with constants $C_h, A_h, C_c, A_c$ consists of a number field $K_1 \supseteq K$, linear forms $c_1, \ldots, c_\rho$ on $K_1 \otimes_K V$, a function $b \ge 0$ on the primes of $K$ with finite support, functions $s_i$ on the primes of $K_1$ with finite support, functions $a_i$ on the infinite places of $K_1$, and reals $C_{\mathrm{arch}}, B_{\deg}$, such that:
1. a vector of $K_1 \otimes_K V$ is killed by every $c_i$ if and only if it lies in the $K_1$-span of $W$;
2. $\frac{1}{[K:\mathbb{Q}]} \sum_\lambda b(\lambda) \log N\lambda \le P(C_c, A_c)\, s$;
3. for $w$ over $\lambda$ and $F \in M$ with $c_i(F) \ne 0$: $\operatorname{ord}_w c_i(F) + s_i(w) \ge -e(w|\lambda)\, b(\lambda)$;
4. the sup norms are invariant under complex conjugation of the embedding;
5. for every infinite place $\sigma$ of $K_1$ and $F \in M$ with $c_i(F) \ne 0$: $\log |c_i(F)|_\sigma + a_i(\sigma) \le \log \|F\|_{\sigma|_K} + C_{\mathrm{arch}}$;
6. for each $i$: $\frac{1}{[K_1 : \mathbb{Q}]}\bigl(\sum_w s_i(w) \log Nw - \sum_\sigma m_\sigma a_i(\sigma)\bigr) \le B_{\deg}$, where $m_\sigma$ is $1$ or $2$ as $\sigma$ is real or complex;
7. $P(C_h, A_h)\, s + C_{\mathrm{arch}} + B_{\deg} + \tfrac12 \log \rho \le P(C_c, A_c)\, s$.

**Theorem 7.9.5 (Quotient lengths from a bridge).** Assume that $M$ is a lattice and that a bridge exists. Then there is a function $b \ge 0$ on the primes of $K$ with finite support and $\frac{1}{[K:\mathbb{Q}]}\sum_\lambda b(\lambda) \log N\lambda \le P(C_c, A_c)\, s$, with the following property. Let $\theta_1, \ldots, \theta_\rho \in M$ be such that their span and $W$ together span $V$, and such that the mean over the complex embeddings of $\log \|\theta_k\|_\sigma$ is at most $P(C_h, A_h)\, s$ for each $k$. Then there is a function $n \ge 0$ on the primes with finite support such that for every $\lambda$,
$$\ell_\lambda\Bigl(Q \big/ \textstyle\sum_k \mathcal{O}_K \bar\theta_k\Bigr) \le n(\lambda) + \rho\, b(\lambda), \qquad \frac{1}{[K:\mathbb{Q}]}\sum_\lambda n(\lambda) \log N\lambda \le \rho\, P(C_c, A_c)\, s .$$

Lean: `Formalism.L2.Pj.QAt.qat_of_bridge'`

*Proof.* The function $b$ is the one of the bridge, and its sum bound is condition 2. Let $\theta_1, \ldots, \theta_\rho$ be as in the statement. The determinant $\det(c_i(\theta_k))$ is nonzero, by condition 1 and the spanning hypothesis. The function $n$ is built from its valuations and from the functions $s_i$. The local length statement, the descent of lengths and condition 3 give the bound on $\ell_\lambda$ at each prime. Conditions 4, 5 and 6 and the bound on the $\theta_k$ give
$$\frac{1}{[K:\mathbb{Q}]}\sum_\lambda n(\lambda) \log N\lambda \le \rho \bigl(P(C_h, A_h)\, s + C_{\mathrm{arch}} + B_{\deg} + \tfrac12 \log \rho\bigr).$$
Condition 7 bounds the right side by $\rho\, P(C_c, A_c)\, s$. $\square$

The theorem in the development also lists conditions on the sizes of the constants and of the weight: $C_R \ge 0$, a bound on an auxiliary family, the shape of the weight, a bound $s \le C_k\, k f b$ on its size, and $T > 0$, $c > 0$, $Tc \le 1$. The proof does not use them.

**Remark 7.9.6 (Formalization).** In [SymmetricLevelClausesHold.lean](lean:Formalism/LocalToGlobal/GlobalTheory/BlockActions/SymmetricLevelClausesHold.lean#L6) the theorem is one line that combines the four clauses. The statements of clauses 1 and 2 take the symmetric system as an unnamed argument: [ClassMapEstimateOfPartial.lean](lean:Formalism/LocalToGlobal/GlobalTheory/BlockActions/ClassMapEstimateOfPartial.lean#L14). The conjunction of the four clauses has the same name as two other definitions with different arguments: [FiniteModelOfAdmissibleTransports.lean](lean:Formalism/SharpRestriction/GlobalSchurBounds/FiniteModelOfAdmissibleTransports.lean#L2251) and [ClassMapInjectiveBijectiveNorms.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/ClassMapInjectiveBijectiveNorms.lean#L9). The genus theorem is in [FinalW.lean](lean:Formalism/LocalToGlobal/GenusGluing/GenusApproximation/FinalW.lean#L25); its local side keeps the hypothesis on $\theta - \bar\theta$, although a CM datum already contains it. The standard Hermitian form is defined twice, in [StdLatUnimodular.lean](lean:Formalism/LocalToGlobal/Columns/StdLatUnimodular.lean#L22) and in [UnimodGenus.lean](lean:Formalism/PeriodIntegrals/UnimodGenus.lean#L67), and the hypothesis on $\theta - \bar\theta$ is defined at least four times, for example in [UnimodGenus.lean](lean:Formalism/PeriodIntegrals/UnimodGenus.lean#L77) and [StatementMass.lean](lean:Formalism/HermitianLattices/StatementMass.lean#L44). In [QatOfBridgeAlt.lean](lean:Formalism/LocalToGlobal/ProjectiveLattices/ArchimedeanQuadraticData/QatOfBridgeAlt.lean#L10) the constant $C_k$ occurs only in the conclusion, and in [QatOfBridge.lean](lean:Formalism/LocalToGlobal/ProjectiveLattices/ArchimedeanQuadraticData/QatOfBridge.lean#L42) the size conditions are introduced and not used.
