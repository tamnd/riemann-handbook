---
title: The closed fibre of a curve over the projective line
decls:
  - UpperTheory.Et.E2.n52
  - UpperTheory.Et.E2.n74
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The closed fibre of a curve over the projective line

The proof of proper base change in SGA 4, Exposé XII, reduces the theorem to proper relative curves over a strictly henselian local ring (see also J. S. Milne, *Étale Cohomology*, Chapter VI, §2, and the [Background](/learn/geometry/#tale-cohomology)). We follow a plan of the same kind. Its basic case is a scheme $Z$ that is integral over the projective line $\mathbb{P}^1_A$. In this section we compute $H^0$ and $H^1$ of the closed fibre of such a $Z$: the fibre is connected, and its $H^1$ is zero. The next sections use these two facts to prove the closed fibre condition for $Z \to \operatorname{Spec} A$.

We keep the notation of [the previous section](/entry/n78/): $q \geq 1$, $i \in \mathbb{Z}$, the closed fibre condition $\mathrm{PB}_{q,i}$ and AIC schemes. For a local ring $A$ with residue field $\kappa$ and a map $p : Z \to \operatorname{Spec} A$, we write $Z_0 = Z \times_{\operatorname{Spec} A} \operatorname{Spec} \kappa$ for the closed fibre.

**Definition 3.3.1 (Line over a base).** Let $\mathbb{P}^1 = \operatorname{Proj} \mathbb{Z}[x_0, x_1]$. A map $l : L \to S$ is a *line* if $l$ is proper and there is a map $f : L \to \mathbb{P}^1$ such that the square
$$\begin{array}{ccc} L & \xrightarrow{f} & \mathbb{P}^1 \\ \downarrow & & \downarrow \\ S & \to & \operatorname{Spec} \mathbb{Z} \end{array}$$
is a pullback. So $L \cong \mathbb{P}^1_S$ over $S$. A map $c : Z \to S$ is *integral over a line* if $c = l \circ u$ with $u : Z \to L$ integral and $l : L \to S$ a line.

A map that is integral over a line stays so after base change $S' \to S$, because integral maps and pullback squares are stable under base change. It also stays so after composition with an integral map $W \to Z$ on the source, because a composition of integral maps is integral.

Let $A$ be a local ring and $p : Z \to \operatorname{Spec} A$ integral over a line, with $Z$ an AIC scheme. Let $u : Z \to \mathbb{P}^1_A$ be the integral map. The two standard opens $D_+(x_0)$ and $D_+(x_1)$ of $\mathbb{P}^1_A$ are affine, and $u$ is affine, so their preimages $U, V \subseteq Z$ are affine and cover $Z$. We call them the *standard charts* of $Z$. Their intersection lies over $\mathbb{G}_{m,A} = D_+(x_0 x_1)$, the punctured line.

### Connectedness

**Theorem 3.3.2 (The closed fibre is connected).** Let $A$ be a strictly henselian local ring, let $p : Z \to \operatorname{Spec} A$ be integral over a line, and let $Z$ be an AIC scheme. Then the closed fibre $Z_0$ is nonempty and connected.

Lean: `UpperTheory.Et.E2.n52`.

*Proof.* First, $Z_0$ is nonempty. The map $p$ is proper, so its image is closed. The image contains a point of $\operatorname{Spec} A$, so it contains the closed point, which lies in the closure of every point of $\operatorname{Spec} A$. A point of $Z$ over the closed point gives a point of $Z_0$.

Next we describe $Z$ by algebra. Let $K$ be the function field of $Z$, let $B = \Gamma(U, \mathcal{O}_Z)$ and $C = \Gamma(V, \mathcal{O}_Z)$ be the rings of the standard charts, as subrings of $K$, and let $t \in K$ be the pullback of the coordinate $x_1/x_0$. Then $t \neq 0$, $t \in B$, $t^{-1} \in C$, $B$ is integral over $A[t]$, $C$ is integral over $A[t^{-1}]$, and $B[t^{-1}] = C[t]$ is the ring of $U \cap V$. Let $\mathfrak{m}$ be the maximal ideal of $A$. The closed fibres of the charts are $U_0 = \operatorname{Spec} B/\mathfrak{m}B$ and $V_0 = \operatorname{Spec} C/\mathfrak{m}C$. A clopen subset $W \subseteq Z_0$ restricts to clopen subsets of $U_0$ and $V_0$, so it gives idempotents of $B/\mathfrak{m}B$ and $C/\mathfrak{m}C$. We lift them to $e \in B$ and $f \in C$. Then $e^2 - e \in \mathfrak{m} B$, $f^2 - f \in \mathfrak{m} C$, and $e - f \in \mathfrak{m} B[t^{-1}]$, since the two idempotents agree on $U_0 \cap V_0$. We call $(e, f)$ an *idempotent pair*. If $e \in \mathfrak{m} B$ and $f \in \mathfrak{m} C$, then $W = \emptyset$. If $e - 1 \in \mathfrak{m} B$ and $f - 1 \in \mathfrak{m} C$, then $W = Z_0$. Each element of $B \cap C$ is integral over $A$.

So it is enough to prove the following lemma.

**Lemma 3.3.3 (Idempotent pairs).** Let $A$ be a henselian local ring with maximal ideal $\mathfrak{m}$, let $K$ be a field over $A$, and let $B, C \subseteq K$ and $t \in K$ be as above, with each element of $B \cap C$ integral over $A$. Then for each idempotent pair $(e, f)$, either $e \in \mathfrak{m} B$ and $f \in \mathfrak{m} C$, or $e - 1 \in \mathfrak{m} B$ and $f - 1 \in \mathfrak{m} C$.

*Proof.* We use a gluing fact for such charts over a henselian local ring: there is $g \in B \cap C$ with $g - e \in \mathfrak{m} B$ and $g - f \in \mathfrak{m} C$. Then $g$ is integral over $A$, so $A[g]$ is a finite $A$-algebra. Over a henselian local ring, a finite algebra is a finite product of local rings. But $A[g] \subseteq K$ is a domain, so it has no idempotents other than $0$ and $1$, and $A[g]$ is local. Its maximal ideal $\mathfrak{n}$ is the only prime over $\mathfrak{m}$, so $\mathfrak{n}$ is the radical of $\mathfrak{m} A[g]$. If $B = \mathfrak{m} B$, then $1 \in \mathfrak{m} B$ and the claim for $e$ is trivial, and the same holds for $C$. Otherwise no unit of $A[g]$ lies in $\mathfrak{m} B$. Now $g^2 - g \equiv e^2 - e \equiv 0 \bmod \mathfrak{m} B$, so $g(g - 1)$ is not a unit, and $g \in \mathfrak{n}$ or $g - 1 \in \mathfrak{n}$. In the first case $g^N \in \mathfrak{m} A[g]$ for some $N$, and then $e \equiv e^N \equiv g^N \equiv 0 \bmod \mathfrak{m} B$ and in the same way $f \equiv 0 \bmod \mathfrak{m} C$. In the second case the same argument for $1 - g$, $1 - e$ and $1 - f$ gives $e - 1 \in \mathfrak{m} B$ and $f - 1 \in \mathfrak{m} C$. $\square$

*End of the proof of the theorem.* Let $W \subseteq Z_0$ be clopen, with its idempotent pair $(e, f)$. The lemma gives $W = \emptyset$ or $W = Z_0$. So $Z_0$ is connected. $\square$

**Remark 3.3.4.** The theorem asks for a strictly henselian ring, but the proof uses only that $A$ is henselian.

### The first cohomology group

The second theorem uses the Mayer-Vietoris sequence for a Zariski cover: for an open cover $X = U \cup V$ there are maps $\delta : H^n(U \cap V, F) \to H^{n+1}(X, F)$, natural in the cover, such that the sequence
$$\begin{aligned} H^n(X, F) &\to H^n(U, F) \oplus H^n(V, F) \to H^n(U \cap V, F) \\ &\xrightarrow{\delta} H^{n+1}(X, F) \to H^{n+1}(U, F) \oplus H^{n+1}(V, F) \end{aligned}$$
is exact. It follows from the axioms of the first section.

**Theorem 3.3.5 (The first cohomology of the closed fibre vanishes).** Let $A$ be a strictly henselian local ring and let $q$ be a unit in $A$. Let $p : Z \to \operatorname{Spec} A$ be integral over a line, and let $Z$ be an AIC scheme. Then for every $i$,
$$H^1(Z_0, \mathbb{Z}/q(i)) = 0.$$

Lean: `UpperTheory.Et.E2.n74`.

*Proof.* Let $U$ and $V$ be the standard charts of $Z$, and let $U_0$ and $V_0$ be their closed fibres. They are open in $Z_0$ and cover $Z_0$.

First, $U_0$ and $V_0$ are acyclic. Indeed $U = \operatorname{Spec} R$ is a nonempty affine open of the AIC scheme $Z$ (or empty, and then there is nothing to prove), so $R$ is an absolutely integrally closed domain, and $q$ is a unit in $R$. The fibre $U_0$ is $\operatorname{Spec} R/\mathfrak{m} R$. By [Theorem 3.2.3](/entry/n78/), it is acyclic. The same holds for $V_0$.

So $H^1(U_0) = H^1(V_0) = 0$, and the Mayer-Vietoris sequence for $Z_0 = U_0 \cup V_0$ gives
$$H^1(Z_0, \mathbb{Z}/q(i)) \cong \operatorname{coker}\bigl(H^0(U_0) \oplus H^0(V_0) \to H^0(U_0 \cap V_0)\bigr),$$
where the map is $(a, b) \mapsto a|_{U_0 \cap V_0} - b|_{U_0 \cap V_0}$. It remains to show that this map is surjective.

Since $Z$ is an AIC scheme and $q$ is a unit, $\Gamma(Z, \mathcal{O}_Z)$ contains a primitive $q$-th root of unity $\zeta$. A choice of $\zeta$ gives an isomorphism, natural in $X$ over $Z$, between $H^0(X, \mathbb{Z}/q(i))$ and the group of locally constant functions $X \to \mathbb{Z}/q$. So we must show: each locally constant function $g$ on $U_0 \cap V_0$ is $a - b$ with $a$ locally constant on $U_0$ and $b$ locally constant on $V_0$.

This is a statement about the punctured line, and we prove it multiplicatively. Since $A$ is henselian with a separably closed residue field and $q$ is a unit, $A$ has a primitive $q$-th root of unity $\zeta$, and on each scheme over $A$ the map $c \mapsto \zeta^c$ identifies locally constant functions to $\mathbb{Z}/q$ with the $q$-th roots of unity in the ring of functions. Let $g$ be locally constant on $U_0 \cap V_0$, and lift $\zeta^g$ to $w \in B[t^{-1}]$, the ring of $U \cap V$. Then $w^q - 1 \in \mathfrak{m} B[t^{-1}]$. A product decomposition for such charts gives $u \in B$ and $v \in C$ with $u^q - 1 \in \mathfrak{m} B$, $v^q - 1 \in \mathfrak{m} C$ and $w - uv \in \mathfrak{m} B[t^{-1}]$. The image of $u$ on $U_0$ is a $q$-th root of unity, so it is $\zeta^a$ for a locally constant $a$ on $U_0$, and in the same way $v$ gives $\zeta^{b'}$ on $V_0$. On $U_0 \cap V_0$ we get $\zeta^g = \zeta^{a + b'}$, so $g = a - b$ with $b = -b'$. So the map is surjective, and $H^1(Z_0, \mathbb{Z}/q(i)) = 0$. $\square$

**Remark 3.3.6.** The proof of proper base change needs a third fact of the same kind: $H^n(Z_0, \mathbb{Z}/q(i)) = 0$ for $n \geq 2$, for $A$ any local ring with $q$ a unit and $p$, $Z$ as above. Here $A$ need not be strictly henselian. It follows from [Theorem 3.2.3](/entry/n78/) and the Mayer-Vietoris sequence for the cover of $Z_0$ by the closed fibres of the charts, which are acyclic.

**Remark 3.3.7 (Formalization).** The connectedness theorem uses only that $A$ is henselian ([StandardChartsLineZero.lean](lean:Development/EtaleCohomology/EtaleSheaves/StandardChartsLineZero.lean#L43)). The description of $Z$ by $K$, $B$, $C$, $t$, the gluing $g$ of an idempotent pair, the product decomposition $w \equiv uv$, the root of unity and the Mayer-Vietoris sequence are separate lemmas, which we checked from their statements. The lemma on the punctured line has the misleading name `proper_base_change_affine_line_of_stalk_iso`, a second name of `UpperTheory.cohomology_punctured_affine_line`: it is about locally constant functions, not stalks ([CohomologyPuncturedAffineLine.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/CohomologyPuncturedAffineLine.lean#L58)). The file of the second theorem defines a multivariable Hensel lemma that is not used ([StandardChartsLineOne.lean](lean:Development/EtaleCohomology/EtaleSheaves/StandardChartsLineOne.lean#L21)).
