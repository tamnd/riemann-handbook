---
title: Pairings and the cup product
decls:
  - LateralTheory.Fix.CupProductTensor.holds_of
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Pairings and the cup product

This section defines the cup product
$$
\cup : H^n(E, \mathbb{Z}/q(i)) \times H^m(E, \mathbb{Z}/q(j)) \to H^{n+m}(E, \mathbb{Z}/q(i+j))
$$
on the cohomology of a space $E$. The definition has two parts. A pairing of the injective resolutions gives products of cochains by the Alexander-Whitney formula. The pairing is chosen so that, in degree $0$, it sends $\zeta \otimes \zeta$ to $\zeta$ for a primitive root of unity $\zeta$. The main theorem says that such pairings exist, that all of them give the same cup product, and that the cup product is associative. We use the spaces, the resolutions $\mathcal{I}^\bullet(F)$ and the sheaves $\mathbb{Z}/q(i)$ of [the first section](/entry/kum-seq/). The cup product is used in all later sections of this chapter: for its unit, its graded commutativity, its naturality and the Chern classes.

All sheaves in this section are sheaves of $\mathbb{Z}/q$-modules, and $q \geq 1$. We write $\mathcal{I}_i = \mathcal{I}^\bullet(\mathbb{Z}/q(i))$ and $\iota : \mathbb{Z}/q(i) \to \mathcal{I}_i^0$ for the augmentation.

**Definition 6.2.1 (Pairing).** Let $\mathcal{I}$, $\mathcal{J}$, $\mathcal{K}$ be complexes of sheaves. A *pairing* $\mu : \mathcal{I} \times \mathcal{J} \to \mathcal{K}$ is a family of bilinear maps
$$
\mu_U : \mathcal{I}^s(U) \times \mathcal{J}^t(U) \to \mathcal{K}^{s+t}(U),
$$
one for each scheme $U$ and all $s, t \in \mathbb{Z}$, with two properties. It commutes with restriction along each $V \to U$. It satisfies the Leibniz rule $d\mu(a, b) = \mu(da, b) + (-1)^s \mu(a, db)$ for $a \in \mathcal{I}^s(U)$.

**Definition 6.2.2 (Faces).** Let $x$ be an $N$-simplex of a space $E$ over $U$, and let $j + l \leq N$. The face $x_{[j, j+l]}$ is the $l$-simplex of $E$ over $U$ on the vertices $j, j+1, \dots, j+l$ of $x$.

**Definition 6.2.3 (Alexander-Whitney product).** Let $\mu : \mathcal{I} \times \mathcal{J} \to \mathcal{K}$ be a pairing and $E$ a space. Let $\alpha$, $\beta$, $\gamma$ be cochains of degrees $n$, $m$ and $n + m$ with values in $\mathcal{I}$, $\mathcal{J}$ and $\mathcal{K}$. We say that $\gamma$ is an *Alexander-Whitney product* of $\alpha$ and $\beta$ for $\mu$ if, for each $N$-simplex $x$ of $E$,
$$
\gamma_N(x) = \sum_{p=0}^{N} (-1)^{mp}\, \mu\big(\alpha_p(x_{[0,p]}),\ \beta_{N-p}(x_{[p,N]})\big).
$$

For a simplicial set and constant coefficients this is the cup product of simplicial cochains (Hatcher, *Algebraic Topology*, Section 3.2). Here the cochains also have a degree in the resolution. The sign $(-1)^{mp}$ comes from moving $\beta$ past the $p$ simplicial degrees of $\alpha$.

Several objects in this chapter are defined as "the element with a given property, if there is one". We make this convention explicit.

**Definition 6.2.4 (Choice convention).** Let $A$ be an abelian group and $P$ a property of elements of $A$. If some element of $A$ has $P$, then $\mathrm{pick}(P)$ is a fixed choice of such an element. If no element has $P$, then $\mathrm{pick}(P) = 0$.

**Definition 6.2.5 (Cup product of a pairing).** Let $\mu : \mathcal{I} \times \mathcal{J} \to \mathcal{K}$ be a pairing and $E$ a space. The cup product $\cup_\mu$ is $\mathrm{pick}(P)$, where $P$ is this property of a biadditive map $c$ from $H^n(E, \mathcal{I}) \times H^m(E, \mathcal{J})$ to $H^{n+m}(E, \mathcal{K})$: for all cocycles $\alpha$, $\beta$, $\gamma$ such that $\gamma$ is an Alexander-Whitney product of $\alpha$ and $\beta$ for $\mu$, we have $c([\alpha], [\beta]) = [\gamma]$.

The property $P$ holds for some map, so $\cup_\mu$ has the property $P$. Indeed, let $\alpha$ and $\beta$ be cocycles. The formula of Definition 6.2.3 defines a cochain $\gamma$, so an Alexander-Whitney product exists. The Leibniz rule for $\mu$ and the identities between faces give $d\gamma = \gamma' \pm \gamma''$, where $\gamma'$ and $\gamma''$ are the Alexander-Whitney products of $(d\alpha, \beta)$ and $(\alpha, d\beta)$. So $\gamma$ is a cocycle, and a change of $\alpha$ or $\beta$ by a coboundary changes $\gamma$ by a coboundary. Hence $[\alpha], [\beta] \mapsto [\gamma]$ is a well defined biadditive map with the property $P$. So, for cocycles $\alpha$ and $\beta$, the class $[\alpha] \cup_\mu [\beta]$ is the class of their Alexander-Whitney product.

**Definition 6.2.6 (Twisted pairing).** A pairing $\mu : \mathcal{I}_i \times \mathcal{I}_j \to \mathcal{I}_k$ is *twisted* if
$$
\mu\big(\iota \langle \zeta \rangle_i,\ \iota \langle \zeta \rangle_j\big) = \iota \langle \zeta \rangle_k
$$
in degree $0$, for each scheme $U$ and each $\zeta \in \mathrm{Prim}_q(\Gamma(U, \mathcal{O}_U))$. Let $\mu_{i,j} = \mathrm{pick}(\text{twisted})$ among the pairings $\mathcal{I}_i \times \mathcal{I}_j \to \mathcal{I}_{i+j}$. The *cup product* on $H^*(E, \mathbb{Z}/q(*))$ is $a \cup b = a \cup_{\mu_{i,j}} b$ for $a$ of weight $i$ and $b$ of weight $j$.

So the cup product is a choice made twice: first a twisted pairing, then a map on classes. The theorem below says that both choices are good: the chosen objects have their properties, and the result does not depend on the choice. It needs the following local description of the sheaves $\mathbb{Z}/q(i)$. We say that a property holds *étale locally* on $U$ if it holds on each member of some étale covering of $U$.

- (T1) Each section of $\mathbb{Z}/q(i)$ over $U$ is, étale locally, $0$ or $c \langle \zeta \rangle_i$ for some $\zeta$ and some $c \in \mathbb{N}$.
- (T2) If $\zeta \in \mathrm{Prim}_q$ is given on $U$, then each section is, étale locally, $c \langle \zeta \rangle_i$.
- (T3) If $U$ is nonempty and $c \langle \zeta \rangle_i = 0$ on $U$, then $q \mid c$.
- (T4) The sections $\langle \zeta \rangle_i$ commute with restriction.
- (T5) If $\xi = \zeta^a$ with $a \in (\mathbb{Z}/q)^\times$, then $\langle \xi \rangle_i = a^i \langle \zeta \rangle_i$.
- (T6) Let $M$ be a sheaf and let $e$ assign to each $\zeta \in \mathrm{Prim}_q(\Gamma(U, \mathcal{O}_U))$ a section $e(\zeta) \in M(U)$, naturally in $U$, with $e(\zeta^a) = a^i e(\zeta)$. Then there is exactly one map $\varphi : \mathbb{Z}/q(i) \to M$ with $\varphi(\langle \zeta \rangle_i) = e(\zeta)$.

**Theorem 6.2.7 (Existence, uniqueness and associativity of the cup product).** Assume (T1) to (T6) for all $q \geq 1$ and $i \in \mathbb{Z}$. Then, for each $q \geq 1$:

1. for all $i$ and $j$, the pairing $\mu_{i,j}$ is twisted;
2. if $k = i + j$ and $\mu$ and $\nu$ are two twisted pairings $\mathcal{I}_i \times \mathcal{I}_j \to \mathcal{I}_k$, then $\cup_\mu = \cup_\nu$ on $H^n(E, -) \times H^m(E, -)$ for every space $E$ and all $n, m$;
3. for all classes $a$, $b$, $c$ on a space $E$, $(a \cup b) \cup c = a \cup (b \cup c)$, where both sides lie in $H^{n+m+k}(E, \mathbb{Z}/q(i+j+l))$.

Lean: `LateralTheory.Fix.CupProductTensor.holds_of`.

*Proof.* The proof is about the coefficients. It reduces each claim to a statement on the complexes $\mathcal{I}_i$ and to the uniqueness of maps into injective complexes up to homotopy.

Step 1: the twists multiply. Let $M = \mathbb{Z}/q(i) \otimes \mathbb{Z}/q(j)$ and $e(\zeta) = \langle \zeta \rangle_i \otimes \langle \zeta \rangle_j$. By (T5) for both factors, $e(\zeta^a) = a^{i+j} e(\zeta)$. So (T6) gives a map $g : \mathbb{Z}/q(i+j) \to M$ with $g(\langle \zeta \rangle_{i+j}) = \langle \zeta \rangle_i \otimes \langle \zeta \rangle_j$. By (T1) and (T2) it is onto étale locally. By (T3) it is injective, because the sections of a sheaf are separated and glue. So $g$ is an isomorphism. This is the identity $\mu_q^{\otimes i} \otimes \mu_q^{\otimes j} \cong \mu_q^{\otimes (i+j)}$ in this model (for [tensor products](/learn/algebra/#tensor-products-and-coinvariants) see Volume 1).

Step 2: tensor products of complexes. For complexes $\mathcal{I}$ and $\mathcal{J}$ there is a complex $\mathcal{I} \otimes \mathcal{J}$ with a pairing $\mathcal{I} \times \mathcal{J} \to \mathcal{I} \otimes \mathcal{J}$ that is universal: each pairing $\mu : \mathcal{I} \times \mathcal{J} \to \mathcal{K}$ is $u \circ \otimes$ for one chain map $u : \mathcal{I} \otimes \mathcal{J} \to \mathcal{K}$. So pairings $\mathcal{I}_i \times \mathcal{I}_j \to \mathcal{I}_{i+j}$ are chain maps $\mathcal{I}_i \otimes \mathcal{I}_j \to \mathcal{I}_{i+j}$, and $\mu$ is twisted when its chain map extends $g^{-1}$ in degree $0$.

Step 3: existence. The sheaves $\mathbb{Z}/q(i)$ are flat, and tensor products with flat complexes keep quasi-isomorphisms. So $\mathcal{I}_i \otimes \mathcal{I}_j$ is a resolution of $\mathbb{Z}/q(i) \otimes \mathbb{Z}/q(j)$, which is $\mathbb{Z}/q(i+j)$ by Step 1. The complex $\mathcal{I}_{i+j}$ is an injective resolution. So $\iota \circ g^{-1}$ extends to a chain map $u : \mathcal{I}_i \otimes \mathcal{I}_j \to \mathcal{I}_{i+j}$, and $u \circ \otimes$ is a twisted pairing. Then the chosen pairing $\mu_{i,j}$ is twisted too. This is claim 1.

Step 4: uniqueness. Two twisted pairings give two chain maps $\mathcal{I}_i \otimes \mathcal{I}_j \to \mathcal{I}_{i+j}$ that extend the same map in degree $0$. Two such maps into a complex of injectives are homotopic. The cup product of a pairing is defined by the Alexander-Whitney formula, so it changes by a coboundary when the chain map changes by a homotopy. By the paragraph after Definition 6.2.5, $\cup_\mu$ and $\cup_\nu$ are computed by Alexander-Whitney products. Hence $\cup_\mu = \cup_\nu$. This is claim 2.

Step 5: associativity. Let $\mu_1$, $\mu_2$, $\nu_1$, $\nu_2$ be twisted pairings of weights $(i, j)$, $(i+j, l)$, $(j, l)$ and $(i, j+l)$. We show that $(a \cup_{\mu_1} b) \cup_{\mu_2} c = a \cup_{\nu_2} (b \cup_{\nu_1} c)$ for all classes $a$, $b$, $c$. The argument has three parts. The Alexander-Whitney formula is associative on cochains. Both bracketings factor through the triple tensor product $\mathcal{I}_i \otimes \mathcal{I}_j \otimes \mathcal{I}_l$, which is associative. The two chain maps from it to $\mathcal{I}_{i+j+l}$ extend the same map in degree $0$, so they are homotopic, as in Step 4. Now take $\mu_1 = \mu_{i,j}$, $\mu_2 = \mu_{i+j,l}$, $\nu_1 = \mu_{j,l}$ and $\nu_2 = \mu_{i,j+l}$. They are twisted by claim 1. So $(a \cup b) \cup c = a \cup (b \cup c)$. This is claim 3. $\square$

**Remark 6.2.8 (Formalization).** The hypotheses (T1) to (T6) form one statement, which is proved as `twSec` in the namespace `LeafAWCutTw`. The users of the theorem apply it to that proof (`ringAssoc` for associativity, `twPairExists` for existence), so the theorem holds with no hypothesis. The proof is a chain of lemmas in [TwPairExists.lean](lean:Development/EtaleCohomology/EtaleSheaves/TwPairExists.lean#L67). Several inputs carry the name `intersectionNumber_baseChange` in their own namespaces: the flatness of the twist sheaves, the tensor product of quasi-isomorphisms, the existence of flipped pairings, the extension property of the twisted resolutions and the naturality of the cup product in the coefficients. None of them is about intersection numbers or base change. We read their statements but did not unfold all their proofs, so Steps 2 to 5 give the structure of the argument. In claim 3, $\mathbb{Z}/q((i+j)+l)$ and $\mathbb{Z}/q(i+(j+l))$ are different types, and the two sides are compared after a cast along $(n+m)+k = n+(m+k)$ and $(i+j)+l = i+(j+l)$.
