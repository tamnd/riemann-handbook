---
title: Spaces and the projective bundle formula
decls:
  - GlobalTheory.T.etaleCohomology_projectiveBundle_formula
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Spaces and the projective bundle formula

The first half of this chapter proves the projective bundle formula in [étale cohomology](/learn/geometry/#tale-cohomology) for a vector bundle on an arbitrary space, not only on a scheme. This section sets up the objects. A space is a simplicial presheaf on schemes, its cohomology is computed from a complex of free étale sheaves, and a vector bundle of rank $N$ on a space is a map to a model of $B\mathrm{GL}_N$. We end with the formula for a scheme, which the proof takes from [the chapter on étale clopen descent](/entry/cb-etale-cohomology-projective-bundle-formula/), and with the fact that every vector bundle on a constant space is trivial.

**Definition 2.1.1 (Space).** Let $\mathrm{PSh}$ be the category of presheaves of sets on the category of [[schemes|5A35TYZD02]]. A *space* is a simplicial object $E$ in $\mathrm{PSh}$, see [[simplicial object|WK0A32TZHB]]. We write $E_p$ for the presheaf of $p$-simplices. A presheaf $F$ gives the *constant space* $\mathrm{disc}(F)$, with $F$ in each degree and identity maps as faces and degeneracies. A scheme $U$ gives the constant space $\mathrm{sch}(U) = \mathrm{disc}(\mathrm{Hom}(-, U))$, and a ring $A$ gives $\mathrm{sp}(A) = \mathrm{sch}(\operatorname{Spec} A)$.

A functor $C$ from commutative rings to small categories also gives a space: its value on a scheme $T$ is the nerve of the category $C(\Gamma(T, \mathcal{O}_T))$. We use three such spaces. $B\mathrm{GL}_N$ comes from the group $\mathrm{GL}_N(A)$, seen as a category with one object. $P_N$ comes from the category whose objects are the unimodular vectors $v \in A^N$ (the entries of $v$ generate the unit ideal) and whose morphisms $v \to w$ are pairs $(g, \lambda)$ with $g \in \mathrm{GL}_N(A)$, $\lambda \in A^\times$ and $g v = \lambda w$. The functor $(g, \lambda) \mapsto g$ gives $\mathrm{pr} : P_N \to B\mathrm{GL}_N$, and $(g, \lambda) \mapsto \lambda$ gives $\ell : P_N \to B\mathrm{GL}_1$.

**Definition 2.1.2 (Vector bundle and projective bundle).** A *vector bundle of rank* $N$ on a space $E$ is a map $V : E \to B\mathrm{GL}_N$. A *line bundle* is a vector bundle of rank $1$. The *projective bundle* of $V$ is the fibre product $\mathbb{P}(V) = E \times_{B\mathrm{GL}_N} P_N$, with projection $\pi : \mathbb{P}(V) \to E$ and tautological line bundle $L_V = \ell \circ \mathrm{pr}_2 : \mathbb{P}(V) \to B\mathrm{GL}_1$. The *trivial bundle* $\mathrm{triv}_N : E \to B\mathrm{GL}_N$ sends every simplex to the one object and every edge to the identity.

**Definition 2.1.3 (Cohomology of a space).** Let $R$ be a commutative ring and let $\mathrm{Shv}(R)$ be the category of [[sheaves|RT8A8FJ566]] of $R$-modules on the big étale site of schemes. For a space $E$, let $C_\bullet(E)$ be the complex of sheaves with the free sheaf $R[E_p]$ in degree $-p$ and the alternating sum of the face maps as differential. For a sheaf $F$, fix an [[injective resolution|ZW3W6FX4PW]] $F \to I^\bullet(F)$. Then
$$
H^n(E, F) = H^n\big(\mathrm{Hom}^\bullet(C_\bullet(E), I^\bullet(F))\big),
$$
the group of homotopy classes of maps of complexes of degree $n$. A map of spaces $f : E' \to E$ gives a pullback $f^* : H^n(E, F) \to H^n(E', F)$.

For $E = \mathrm{sch}(U)$ the complex $C_\bullet(E)$ is the free sheaf $R[\mathrm{Hom}(-, U)]$ in degree $0$. By the Yoneda lemma $\mathrm{Hom}(R[\mathrm{Hom}(-,U)], I) = I(U)$, so $H^n(\mathrm{sch}(U), F)$ is the cohomology of $F$ on $U$ in the sense of [[sheaf cohomology|PQ6Q143ARJ]].

**Definition 2.1.4 (Tate twists).** Let $q \geq 1$ and $i \in \mathbb{Z}$. For a ring $A$, let $\mathrm{Prim}_q(A)$ be the set of roots of the cyclotomic polynomial $\Phi_q$ in $A$, if $q$ is a unit in $A$, and the empty set otherwise. Let $\mathbb{Z}/q(i)(A)$ be the free $\mathbb{Z}/q$-module on $\mathrm{Prim}_q(A)$ modulo the relations $[\zeta^a] = a^i [\zeta]$ for $a \in (\mathbb{Z}/q)^\times$. The sheaf $\mathbb{Z}/q(i)$ is the étale sheaf that this functor of rings gives. We write $H^n(E, \mathbb{Z}/q(i))$ for its cohomology. The relation says that a change of the [[primitive root of unity|0EHM5ZP5QH]] $\zeta$ to $\zeta^a$ multiplies the class $[\zeta]$ by $a^i$, as for a generator of $\mu_q^{\otimes i}$. This is how the twist enters without a choice of root.

**Definition 2.1.5 (Cup product and Chern class).** The cup product
$$
\cup : H^n(E, \mathbb{Z}/q(i)) \times H^m(E, \mathbb{Z}/q(j)) \to H^{n+m}(E, \mathbb{Z}/q(i+j))
$$
is defined from the Alexander-Whitney map and a pairing of the resolutions. For a line bundle $L$ on $E$, the [[Chern class|PAD37GKDPD]] $c_1(L) \in H^2(E, \mathbb{Z}/q(1))$ is the class of a $2$-cocycle built from the Kummer classes of $q$-th roots of the transition units of $L$ on the $1$-simplices. We write $c_1(L)^j$ for the $j$-fold cup power, with $c_1(L)^0 = 1$.

**Definition 2.1.6 (Invertible on a space).** We say that $q$ is *invertible on* a space $E$ if $q$ is a unit in $\Gamma(T, \mathcal{O}_T)$ for every scheme $T$ with $E_0(T) \neq \emptyset$. For $E = \mathrm{sch}(U)$ this says that $q$ is a unit on $U$.

**Definition 2.1.7 (Projective bundle formula).** Let $V$ be a vector bundle of rank $N$ on a space $E$. The *formula map* in degree $n$ and weight $i$ is
$$
\begin{aligned}
\Phi_V : \bigoplus_{j=0}^{N-1} H^{n-2j}(E, \mathbb{Z}/q(i-j)) &\to H^n(\mathbb{P}(V), \mathbb{Z}/q(i)), \\
(a_j)_j &\mapsto \sum_{j=0}^{N-1} \pi^* a_j \cup c_1(L_V)^j.
\end{aligned}
$$
We say that the *projective bundle formula holds for* $V$ if $\Phi_V$ is bijective for all $n, i \in \mathbb{Z}$.

Lean: `GlobalTheory.EtC.pbfMap` (also `GlobalTheory.EtC.PBF`, the condition that it is bijective).

For a complex vector bundle on a manifold, the same statement is the [projective bundle formula of topology](/learn/geometry/#complex-manifolds). In étale cohomology it is due to Grothendieck (SGA 5, Exposé VII). The case of a scheme is in Milne, *Étale Cohomology*, Chapter VI, §10.

**Theorem 2.1.8 (Projective bundle formula on a scheme).** Let $q \geq 1$, let $U$ be a scheme, and let $V$ be a vector bundle of rank $N$ on $\mathrm{sch}(U)$. Suppose that $q$ is invertible on $\mathrm{sch}(U)$, that is, $q$ is a unit on $U$. Then the projective bundle formula holds for $V$.

Lean: `GlobalTheory.T.etaleCohomology_projectiveBundle_formula` (also `UpperTheory.Cb.etaleCohomology_projectiveBundle_formula`).

*Proof.* This is [Theorem 2.1.8](/entry/cb-etale-cohomology-projective-bundle-formula/) of the chapter on étale clopen descent. There, the bundle $V$ is first shown to be trivial, by the argument of the next lemma, and then the formula for the trivial bundle of rank $N$ is proved for every space on which $q$ is invertible, by induction on $N$, in [Lemma 5.5.3](/entry/pbf-all/). $\square$

**Lemma 2.1.9 (Bundles on constant spaces are trivial).** Let $F$ be a presheaf and let $V : \mathrm{disc}(F) \to B\mathrm{GL}_N$ be a vector bundle. Then $V = \mathrm{triv}_N$.

Lean: `GlobalTheory.T.discrete_glBundle_eq_trivialGLBundle` (also `GlobalTheory.EtC.disc_eq_trivV`).

*Proof.* The category $\mathrm{GL}_N(A)$ has one object, so $V$ and $\mathrm{triv}_N$ agree on $0$-simplices. Let $x \in F(T)$ be a $p$-simplex of $\mathrm{disc}(F)$. It is the image of the $0$-simplex $x$ under the degeneracy map $s : [p] \to [0]$, because all simplicial maps of $\mathrm{disc}(F)$ are identities. Since $V$ is a map of simplicial objects, $V(x) = s^* V(x)$, and $s^*$ of the one $0$-simplex of the nerve is the $p$-simplex made of identity arrows. This is $\mathrm{triv}_N(x)$. $\square$

So on a constant space, the projective bundle is $\mathrm{disc}(F) \times P_N$, a product. The next two sections use this to pass from schemes to all constant spaces and then to all spaces.

**Remark 2.1.10 (Formalization).** The cup product and $c_1$ are defined by choosing a class with a stated property, and the choice is $0$ if no class has the property. The formula above is then still a statement, but the meaning of $c_1$ rests on the existence of the Kummer cocycle. The theorem on a scheme has a second name in the chapter on étale clopen descent. We have not opened the sheafification step in the definition of $\mathbb{Z}/q(i)$.
