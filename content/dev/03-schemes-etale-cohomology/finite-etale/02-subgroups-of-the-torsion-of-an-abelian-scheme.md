---
title: Subgroups of the torsion of an abelian scheme
decls:
  - UpperTheory.SubRep.core
  - UpperTheory.Cb.exists_finite_etale_trivializing_torsion_abelianScheme
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Subgroups of the torsion of an abelian scheme

Let $A$ be an [abelian scheme](/learn/elliptic-curves/#abelian-varieties-and-abelian-schemes) over $S$ and let $k \geq 1$ be an integer that is invertible on $S$. The $k$-torsion $A[k]$ is finite étale over $S$. So the clopen subsets of $A[k]$ are the points of a finite étale scheme, by the theorem of the last section. This section cuts out the clopen subsets that are subgroups, and it shows that they classify the kernels of homomorphisms from $A$ to abelian schemes when the kernel is killed by $k$ (Theorem 5.2.3 and Corollary 5.2.4). The corollary is the first step of the proof that isogenies of type $T_j$ are representable, in the next section and in [the isogeny theorem](/entry/isogeny-rep/).

We work with group schemes through their points. A *group* over $S$ is an $S$-scheme $A$ with a group structure on the sets $A(T)$ of $S$-morphisms $T \to A$, natural in $T$. It is *commutative* if each group $A(T)$ is commutative. A *homomorphism* $f : A \to B$ is an $S$-morphism that gives group homomorphisms $A(T) \to B(T)$. For $a \in A(T)$ we write $a^k$ for the $k$-th power in the group $A(T)$, and $1$ for the unit.

**Definition 5.2.1 (Torsion).** Let $A$ be a commutative group over $S$ and $k \geq 1$. The *$k$-torsion* $A[k]$ is the kernel of the homomorphism $a \mapsto a^k$ of $A$. Its $T$-points are the $a \in A(T)$ with $a^k = 1$. The inclusion $A[k] \to A$ is a monomorphism and a homomorphism.

If $A$ is an [[abelian scheme|JDDXZ89N33]] and $k$ is invertible on $S$, then multiplication by $k$ is finite étale and surjective, and $A[k]$ is its fibre over the unit section. So $A[k]$ is finite étale over $S$ ([[étale|H84VHC8PX2]]). This is the only property of abelian schemes that the proof uses.

**Definition 5.2.2 (Subgroup locus).** Let $G \to S$ be a group that is finite étale, and let $(Y_0, U)$ represent the clopen functor $\mathrm{Clop}_G$ of the last section. A point $t \in Y_0(T)$ gives a clopen subset $U_t$ of $G_T$. We say that $t$ lies in the *subgroup locus* if $U_t$ contains the unit section of $G_T$, and $a b^{-1}$ lies in $U_t$ whenever $a$ and $b$ do. The second condition is on the $T'$-points of $G_T$, for all $T' \to T$.

**Theorem 5.2.3 (Scheme of subgroups killed by k).** Let $S$ be a locally noetherian scheme and $A$ a commutative group over $S$. Let $G \to S$ be a finite étale group with a homomorphism $\iota : G \to A$ that is a monomorphism. Let $k$ be a natural number that is a unit in $\Gamma(S, \mathcal{O}_S)$. Suppose that each $a \in A(T)$ with $a^k = 1$ comes from $G(T)$, and that $\iota(b)^k = 1$ for each $b \in G(T)$. So $G$ is the $k$-torsion of $A$. Then there is a finite étale $S$-scheme $Y$ with this property. Let $A_Y$ be a commutative group over $Y$ that is a pullback of $A$ to $Y$ as a group. Then there are a finite étale group $H$ over $Y$ and a homomorphism $i : H \to A_Y$ that is a monomorphism with $i^k = 1$, such that the following holds. Let $x : T \to S$ be a morphism, let $A_T$ be a commutative group over $T$ that is a pullback of $A$ along $x$ as a group, let $B$ be an abelian scheme over $T$, and let $f : A_T \to B$ be a homomorphism such that $g^k = 1$ for each point $g$ of $A_T$ with $f(g) = 1$. Then there is exactly one $y : T \to Y$ over $S$ such that, for each $T$-scheme $T'$ and each $g \in A_T(T')$, we have $f(g) = 1$ if and only if there is a point $h$ of $H$ over $y$ with $i(h) = g$ as points of $A$.

Lean: `UpperTheory.SubRep.core`.

In short, $Y$ is the scheme of finite étale subgroups of $A$ killed by $k$, and $H \subseteq A_Y$ is the universal subgroup. A homomorphism to an abelian scheme with kernel killed by $k$ is classified by its kernel.

*Proof.* We give the proof in five steps.

First, apply the theorem of the last section to $G$. This gives a finite étale $S$-scheme $Y_0$ and a clopen subset $U$ of $G_{Y_0}$ that represent $\mathrm{Clop}_G$.

Second, the subgroup locus is a clopen subset $U_1$ of $Y_0$. The reason is this. The conditions "the unit lies in $U_t$" and "$U_t$ is closed under $a b^{-1}$" say that two clopen subsets of finite étale schemes over $Y_0$ contain the whole scheme. These are the inverse image of $U$ under the unit section $Y_0 \to G_{Y_0}$, and the inverse image of $U$ under $(a, b) \mapsto a b^{-1}$ on the clopen subset $U \times_{Y_0} U$ of $G_{Y_0} \times_{Y_0} G_{Y_0}$. For a finite étale map $Z \to Y_0$ and a clopen subset $V$ of $Z$, the set of points of $Y_0$ over which the fibre lies in $V$ is the complement of the image of $Z \setminus V$. A finite étale map is open and closed, so this set is clopen.

Third, let $Y$ be the open and closed subscheme of $Y_0$ on the set $U_1$. It is finite étale over $S$, and $Y \to Y_0$ is a monomorphism. A point $t \in Y_0(T)$ factors through $Y$ if and only if it lies in the subgroup locus. Over $Y$ the clopen subset $U_Y$ of $G_Y$ contains the unit and is closed under $a b^{-1}$. So it is a subgroup scheme $H$ of $G_Y$, finite étale over $Y$, and $i : H \to G_Y \to A_Y$ is a homomorphism and a monomorphism. Since $\iota(b)^k = 1$ for all $b$, we have $i^k = 1$.

Fourth, let $x$, $B$ and $f$ be as in the statement, and let $K$ be the set of points $a$ of $G_T$ with $f(\iota(a)) = 1$. Each $a$ in $G_T$ satisfies $\iota(a)^k = 1$, so $f(\iota(a))$ lies in $B[k]$. Now $B[k]$ is finite étale over $T$, because $B$ is an abelian scheme and $k$ is a unit. The unit section of a separated étale scheme is an open and closed immersion. So $K$, the inverse image of the unit section of $B[k]$ under $f \circ \iota$, is clopen in $G_T$. The set $K$ is a subgroup, because $f \circ \iota$ is a homomorphism. By the first step, there is exactly one $y_0 : T \to Y_0$ over $S$ with $U_{y_0} = K$, and by the third step $y_0$ factors through $Y$ as $y$. Let $g \in A_T(T')$. If $f(g) = 1$, then $g$ is in the kernel of $f$, so $g^k = 1$ by the hypothesis on $f$, and $g = \iota(b)$ for some $b$. Then $b$ lies in $K$, so $g$ lies in $i(H_T)$. The converse is clear from the definition of $K$.

Fifth, let $y' : T \to Y$ be a second morphism with the property. The clopen subsets $U_{y'}$ and $U_y$ of $G_T$ then contain the same $T'$-points for all $T'$. Two open subsets with the same $T'$-points for all $T'$ are equal. So $U_{y'} = U_y$, and the uniqueness in the first step, together with the fact that $Y \to Y_0$ is a monomorphism, gives $y' = y$. $\square$

**Corollary 5.2.4 (Subgroups of the torsion of an abelian scheme).** Let $S$ be a locally noetherian scheme, $A$ a commutative group over $S$ that is an abelian scheme, and $k > 0$ an integer that is a unit in $\Gamma(S, \mathcal{O}_S)$. Then there is a finite étale $S$-scheme $Y$ such that, for each pullback $A_Y$ of $A$ to $Y$, there are a finite étale group $H$ over $Y$ and a homomorphism $i : H \to A_Y$ that is a monomorphism with $i^k = 1$, with the classification property of Theorem 5.2.3.

Lean: `UpperTheory.Cb.exists_finite_etale_trivializing_torsion_abelianScheme`.

*Proof.* Take $G = A[k]$ with its inclusion $\iota$. It is finite étale because $A$ is an abelian scheme and $k$ is a unit. The inclusion is a monomorphism, since a point of $A[k]$ is determined by its image in $A$. The group structure of $A$ restricts to $A[k]$, because products, inverses and the unit of $k$-torsion points are again $k$-torsion points. Each $a$ with $a^k = 1$ comes from $A[k]$ by definition, and $\iota(b)^k = 1$ for each $b$. This is the theorem applied to $G = A[k]$. $\square$

**Remark 5.2.5.** The hypothesis $k > 0$ is redundant. If $k = 0$, then $0$ is a unit in $\Gamma(S, \mathcal{O}_S)$, so this ring is zero and $S$ is empty. The homomorphism $f : A_T \to B$ need not be surjective or an isogeny. The classification holds for each homomorphism to an abelian scheme whose kernel is killed by $k$.

**Remark 5.2.6 (Formalization).** The proof of the corollary does not use $k > 0$. The name of the corollary says "trivializing torsion", but nothing in the statement trivializes $A[k]$: the scheme $Y$ classifies subgroups of $A[k]$. The statement asks for $H$ and $i$ for every pullback $A_Y$ of $A$ to $Y$, not for one chosen pullback, and the group structure on $H$ is part of the conclusion. Three inputs of the second and fourth steps were read as statements, not proofs: the subgroup locus is clopen, a clopen subset of a finite étale scheme is a finite étale subscheme ([RangeSubsetOfGeom.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/RangeSubsetOfGeom.lean#L118)), and the kernel locus is clopen.
