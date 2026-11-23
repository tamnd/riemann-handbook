---
title: The Kummer sequence
decls:
  - LateralTheory.E.H2CurveOrder.muUnits
  - LateralTheory.E.LeafKumFieldPf.kumMu
  - LateralTheory.E.LeafKumFieldPf.kumSeq
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Kummer sequence

Let $B$ be a ring in which the integer $q \geq 1$ is a unit. The Kummer sequence relates the first cohomology of $\mathrm{Spec}\, B$ with coefficients $\mathbb{Z}/q(1)$ to the units of $B$ and to the cohomology of $\mathbb{G}_m$. This section proves three facts in the model of étale cohomology of the code. The sheaf $\mu_q$ of $q$-th roots of unity is the Tate twist $\mathbb{Z}/q(1)$ on schemes over $B$. Hence $H^1(\mathrm{Spec}\, B, \mu_q) \cong H^1(\mathrm{Spec}\, B, \mathbb{Z}/q(1))$. Then the Kummer sequence $B^\times / B^{\times q} \to H^1(\mathrm{Spec}\, B, \mathbb{Z}/q(1)) \to H^1(\mathrm{Spec}\, B, \mathbb{G}_m)$ is exact. The proof needs the last fact to bound $H^1$ in [the finiteness theorem](/entry/etale-topology-top/).

We first fix the model. It is the same in all sections of this chapter.

**Definition 6.1.1 (Spaces).** A *space* is a simplicial presheaf of sets on the category of schemes. For a space $E$, a scheme $U$ and $N \geq 0$, an element $x \in E_N(U)$ is an *$N$-simplex of $E$ over $U$*. A scheme $X$ gives the discrete space $\mathrm{sch}(X)$: its $N$-simplices over $U$ are the morphisms $U \to X$, for each $N$. For a ring $B$ we write $\mathrm{sp}(B) = \mathrm{sch}(\mathrm{Spec}\, B)$.

**Definition 6.1.2 (Cohomology of a space).** Let $R$ be a ring. A *sheaf* is a sheaf of $R$-modules on the big étale site of schemes. For a space $E$, let $C_\bullet(E)$ be the complex of sheaves whose term in degree $N$ is the sheaf of free $R$-modules on $E_N$. For a sheaf $F$, the code fixes an injective resolution $F \to \mathcal{I}^\bullet(F)$, with augmentation $\iota_F : F \to \mathcal{I}^0(F)$. Then $H^n(E, F)$ is the $n$-th cohomology of the complex $\mathrm{Hom}(C_\bullet(E), \mathcal{I}^\bullet(F))$. An $n$-cochain $\alpha$ has one component $\alpha_N$ for each $N \geq 0$: it sends an $N$-simplex $x$ over $U$ to a section $\alpha_N(x) \in \mathcal{I}^{n-N}(F)(U)$. A map $f : E \to E'$ gives the pullback $f^* : H^n(E', F) \to H^n(E, F)$.

For a scheme $X$, the group $H^n(\mathrm{sch}(X), F)$ plays the role of the [[étale cohomology|7YX76G0838]] of $X$, as in [Volume 1](/learn/geometry/#tale-cohomology). The code does not prove that the two agree. It states the properties that it needs as axioms. We use four of them here.

- (A7) A short exact sequence $0 \to F_1 \to F_2 \to F_3 \to 0$ of sheaves gives a map $\delta : H^n(E, F_3) \to H^{n+1}(E, F_1)$, and the long sequence $H^n(E, F_1) \to H^n(E, F_2) \to H^n(E, F_3) \to H^{n+1}(E, F_1) \to H^{n+1}(E, F_2)$ is exact.
- (A8) For a ring map $R \to S$ and a sheaf $F$ of $S$-modules, the cohomology of $F$ as a sheaf of $S$-modules is the same as its cohomology as a sheaf of $R$-modules.
- (A9) $H^n(E, F) = 0$ for $n < 0$, and $H^0(\mathrm{sch}(X), F) \cong F(X)$, naturally in $X$.
- (A10) Let $\varphi : F \to G$ be a map of sheaves. If $\varphi(U)$ is bijective for each scheme $U$ over which $E$ has a $0$-simplex, then $\varphi$ induces a bijection $H^n(E, F) \to H^n(E, G)$ for each $n$.

**Definition 6.1.3 (Tate twists).** Let $q \geq 1$ and $i \in \mathbb{Z}$. For a ring $A$, let $\mathrm{Prim}_q(A)$ be the set of $\zeta \in A$ such that $q$ is a unit in $A$ and $\Phi_q(\zeta) = 0$, where $\Phi_q$ is the [[cyclotomic polynomial|08KEYFAH66]] of order $q$. The sheaf $\mathbb{Z}/q(i)$ is the étale sheafification of the presheaf
$$
A \mapsto \mathbb{Z}/q\,[\mathrm{Prim}_q(A)] \big/ \big\langle [\zeta^a] - a^i [\zeta] : \zeta \in \mathrm{Prim}_q(A),\ a \in (\mathbb{Z}/q)^\times \big\rangle .
$$
For $\zeta \in \mathrm{Prim}_q(\Gamma(U, \mathcal{O}_U))$ we write $\langle \zeta \rangle_i$ for the section of $\mathbb{Z}/q(i)$ over $U$ given by $[\zeta]$.

When $A$ is a field that contains a [[primitive root of unity|0EHM5ZP5QH]] $\zeta$ of order $q$, the elements of $\mathrm{Prim}_q(A)$ are the $\zeta^a$ with $a$ prime to $q$ (see [roots of unity](/learn/algebra/#roots-of-unity)). The value of the presheaf is then $\mathbb{Z}/q$ with basis $[\zeta]$, and a Galois element with $\sigma(\zeta) = \zeta^a$ acts by $a^i$. This is the usual $\mu_q^{\otimes i}$. When $q$ is not a unit in $A$, the presheaf is $0$ at $A$.

**Definition 6.1.4 (The multiplicative group).** $\mathbb{G}_m$ is the sheaf of abelian groups $U \mapsto \Gamma(U, \mathcal{O}_U)^\times$, made a sheaf by sheafification. Let $[q] : \mathbb{G}_m \to \mathbb{G}_m$ be the map $u \mapsto u^q$, and let $\mu_q$ be its kernel.

**Lemma 6.1.5 (Roots of unity and the Tate twist).** Let $B$ be a ring in which $q$ is a unit. There is a map of sheaves of abelian groups $\kappa : \mathbb{Z}/q(1) \to \mathbb{G}_m$ with $[q] \circ \kappa = 0$ that has these properties for each scheme $U$ over $\mathrm{Spec}\, B$:

1. $\kappa$ is injective on sections over $U$;
2. each $s \in \mathbb{G}_m(U)$ with $s^q = 1$ is $\kappa(t)$ for some section $t$ of $\mathbb{Z}/q(1)$ over $U$.

Lean: `LateralTheory.E.H2CurveOrder.muUnits`.

*Proof.* On the presheaf, let $\kappa$ send $[\zeta]$ to $\zeta$. It respects the relations, since $[\zeta^a]$ and $a [\zeta]$ both go to $\zeta^a$. Then $\kappa$ is the sheafification of this map. We have $\zeta^q = 1$, since $\Phi_q$ divides $X^q - 1$. So $[q] \circ \kappa = 0$.

Injectivity. A section of $\mathbb{Z}/q(1)$ is, étale locally, $0$ or $c \langle \zeta \rangle_1$ with $c \in \mathbb{Z}$. Its image is $\zeta^c$. Suppose that $\zeta^c = 1$ on a nonempty $V$, and let $d = \gcd(c, q)$. Then $\zeta^d = 1$. If $d < q$, then $\zeta$ is a root of $X^d - 1$ and of $\Phi_q$. These two polynomials are coprime factors of $X^q - 1$, which is separable because $q$ is a unit. So they generate the unit ideal of $\Gamma(V, \mathcal{O}_V)[X]$, and $1 = 0$ on $V$. This is false, so $q \mid c$ and the section is $0$. The units presheaf is separated, so the local statements glue.

Surjectivity. Let $u$ be a unit on $U$ with $u^q = 1$. First, étale locally on $U$ there is a primitive root $\zeta$: the algebra $\Gamma(U, \mathcal{O}_U)[X]/\Phi_q$ is étale over $\Gamma(U, \mathcal{O}_U)$ and its spectrum maps onto $U$, because $\Phi_q$ is a monic factor of the separable polynomial $X^q - 1$. Second, Zariski locally $u = \zeta^a$ for some $a$. Let $P(u, v) = \sum_{k=0}^{q-1} u^k v^{q-1-k}$, so that $P(u, v)(u - v) = u^q - v^q$. At a point with residue field $k$, the image of $\zeta$ is a primitive $q$-th root of unity, so the image of $u$ is the image of some $\zeta^a$. There $P(u, \zeta^a)$ has the value $q \zeta^{a(q-1)} \neq 0$. So $P(u, \zeta^a)$ is a unit near the point, and $u - \zeta^a = 0$ there. Hence $u = \kappa(a \langle \zeta \rangle_1)$ locally, and the local preimages glue by injectivity. $\square$

**Proposition 6.1.6 ($\mu_q$ and $\mathbb{Z}/q(1)$).** Assume the axioms of the étale model. Let $B$ be a ring in which $q \geq 1$ is a unit. Then $H^1(\mathrm{sp}(B), \mu_q) \cong H^1(\mathrm{sp}(B), \mathbb{Z}/q(1))$. On the left, $\mu_q$ is a sheaf of abelian groups. On the right, $\mathbb{Z}/q(1)$ is a sheaf of $\mathbb{Z}/q$-modules.

Lean: `LateralTheory.E.LeafKumFieldPf.kumMu`.

*Proof.* The map $\kappa$ of [the lemma above](/entry/mu-units/) factors through $\mu_q$, because $[q] \circ \kappa = 0$. The two properties of $\kappa$ say that $\kappa : \mathbb{Z}/q(1) \to \mu_q$ is bijective on sections over each $U$ over $\mathrm{Spec}\, B$. These are the schemes over which $\mathrm{sp}(B)$ has a $0$-simplex. By (A10), $\kappa$ gives a bijection on $H^1(\mathrm{sp}(B), -)$, with $\mathbb{Z}/q(1)$ seen as a sheaf of abelian groups. By (A8) for $\mathbb{Z} \to \mathbb{Z}/q$, this group is $H^1(\mathrm{sp}(B), \mathbb{Z}/q(1))$. $\square$

The classical Kummer sequence is the exact sequence of étale sheaves $0 \to \mu_q \to \mathbb{G}_m \xrightarrow{[q]} \mathbb{G}_m \to 0$ on a scheme on which $q$ is invertible (Milne, *Étale Cohomology*, Chapter II, §2). Its long exact sequence, with $H^1(X, \mathbb{G}_m) = \mathrm{Pic}(X)$ (Milne, Chapter III, Proposition 4.9), gives an exact sequence $\Gamma(X, \mathcal{O}_X)^\times \xrightarrow{q} \Gamma(X, \mathcal{O}_X)^\times \to H^1(X, \mu_q) \to \mathrm{Pic}(X) \xrightarrow{q} \mathrm{Pic}(X)$. The code proves the middle of this sequence.

**Theorem 6.1.7 (Kummer sequence).** Assume the axioms of the étale model. Let $B$ be a ring in which $q \geq 1$ is a unit. There are homomorphisms
$$
B^\times / B^{\times q} \xrightarrow{\ a\ } H^1(\mathrm{sp}(B), \mathbb{Z}/q(1)) \xrightarrow{\ b\ } H^1(\mathrm{sp}(B), \mathbb{G}_m)
$$
with $\mathrm{im}(a) = \ker(b)$.

Lean: `LateralTheory.E.LeafKumFieldPf.kumSeq`.

*Proof.* Let $I \subseteq \mathbb{G}_m$ be the image sheaf of $[q]$. Then $0 \to \mu_q \to \mathbb{G}_m \to I \to 0$ is exact, and (A7) gives an exact sequence
$$
H^0(\mathrm{sp}(B), \mathbb{G}_m) \to H^0(\mathrm{sp}(B), I) \xrightarrow{\ \delta\ } H^1(\mathrm{sp}(B), \mu_q) \xrightarrow{\ \beta\ } H^1(\mathrm{sp}(B), \mathbb{G}_m).
$$
Next we need a surjection $c : B^\times \to H^0(\mathrm{sp}(B), I)$ such that $c(u^q)$ is in the image of $H^0(\mathbb{G}_m)$. The map $[q]$ is onto étale locally, because $X^q - u$ is étale over a ring in which $q$ and $u$ are units. So $I = \mathbb{G}_m$ as sheaves. The units presheaf on affine schemes is already a sheaf, so $I(\mathrm{Spec}\, B) = B^\times$. By (A9), $H^0(\mathrm{sp}(B), I) \cong B^\times$, and the map from $H^0(\mathbb{G}_m)$ is $u \mapsto u^q$. Let $c$ be this isomorphism.

Then $\delta \circ c$ vanishes on $B^{\times q}$, so it factors through $B^\times / B^{\times q}$. Its image is the image of $\delta$, since $c$ is onto. This is $\ker(\beta)$. Let $e : H^1(\mu_q) \cong H^1(\mathbb{Z}/q(1))$ be [the isomorphism above](/entry/kum-mu/). Put $a = e \circ \delta \circ c$ and $b = \beta \circ e^{-1}$. Then $\mathrm{im}(a) = e(\ker \beta) = \ker(b)$. $\square$

**Remark 6.1.8.** The Lean statement only says that some $a$ and $b$ exist with $\mathrm{im}(a) = \ker(b)$. It does not say that $a$ is the Kummer map, that $b$ comes from $\mu_q \to \mathbb{G}_m$, or that $a$ is injective. The user of the theorem needs only this much. It gets the finiteness of $H^1(\mathrm{sp}(B), \mathbb{Z}/q(1))$ from the finiteness of the two outer groups. See [LeafKumCut.lean](lean:Development/EtaleCohomology/EtaleSheaves/LeafKumCut.lean#L13).

**Remark 6.1.9.** The proposition and the theorem take as hypothesis the bundle `Hyps` of 27 axioms, A1 to E3. The proofs read only A7, A8, A9 and A10 from it. The bundle also contains D1 and D2. D2 is the statement that [the last section](/entry/s57/) of this chapter proves from D1.

**Remark 6.1.10.** The lemma has the namespace `H2CurveOrder`, but it is not about curves. The same namespace has a second theorem with the short name `kumSeq`, at [ResMapNsmulHomotopy.lean](lean:Development/EtaleCohomology/EtaleSheaves/KummerSequence/ResMapNsmulHomotopy.lean#L80). That theorem is about $H^2$ of curves over an algebraically closed field. It is not the theorem of this section.
