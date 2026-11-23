---
title: The unit of the cup product
decls:
  - LateralTheory.Fix.EtaleChapterDTwo.s31
  - LateralTheory.Fix.EtaleChapterDTwo.s32
  - LateralTheory.Fix.EtaleChapterDTwo.s33
  - LateralTheory.Fix.EtaleChapterDTwo.s34
  - LateralTheory.Fix.EtaleChapterDTwo.s38
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The unit of the cup product

This section proves that the class $1_E \in H^0(E, \mathbb{Z}/q(0))$ is a left unit for the cup product of [the previous section](/entry/cup-product-tensor-holds-of/): $1_E \cup a = a$ for every class $a$, when $q$ is invertible on $E$. The cup product is defined through a twisted pairing. So it is enough to find one twisted pairing $\mathcal{I}_0 \times \mathcal{I}_i \to \mathcal{I}_i$ that acts as the identity when its first argument is the generator. Most of the section builds this pairing. The tool is a lemma that extends a pairing along the augmentation $\mathbb{Z}/q(0) \to \mathcal{I}_0$. The unit law makes the even cohomology a ring with $1$ in [the last section](/entry/s42/).

We keep the notation of the previous sections: $\mathcal{I}_i$ is the injective resolution of $\mathbb{Z}/q(i)$ and $\iota$ is its augmentation. For a sheaf $F$, let $F[0]$ be the complex with $F$ in degree $0$ and $0$ elsewhere. Then $\iota$ is a map of complexes $\varepsilon : \mathbb{Z}/q(0)[0] \to \mathcal{I}_0$, and it is a quasi-isomorphism.

**Definition 6.3.1 (Invertible on a space).** Let $q \geq 1$ and let $E$ be a space. Then $q$ is *invertible on* $E$ if $q$ is a unit in $\Gamma(U, \mathcal{O}_U)$ for each scheme $U$ over which $E$ has a $0$-simplex.

**Definition 6.3.2 (Unit class).** A $0$-cocycle $\alpha$ of $E$ with values in $\mathcal{I}_0$ is a *unit cocycle* if $\alpha_0(x) = \iota \langle \zeta \rangle_0$ for each $0$-simplex $x$ of $E$ over $U$ and each $\zeta \in \mathrm{Prim}_q(\Gamma(U, \mathcal{O}_U))$. The *unit class* $1_E$ is $\mathrm{pick}$ of the property "is the class of a unit cocycle".

For weight $0$ the relation of the Tate twist reads $\langle \zeta^a \rangle_0 = \langle \zeta \rangle_0$. So the value $\iota \langle \zeta \rangle_0$ does not change when $\zeta$ is replaced by a power $\zeta^a$ with $a$ prime to $q$. Assume that $q$ is invertible on $E$. Then primitive $q$-th roots of unity exist étale locally over each $U$ over which $E$ has a $0$-simplex (see the proof of [the lemma on roots of unity](/entry/mu-units/)). We use two consequences.

- (U1) A unit cocycle $\alpha$ exists, and $1_E = [\alpha]$ for every unit cocycle $\alpha$.
- (U2) For every unit cocycle $\alpha$ and $0$-simplex $x$ over $U$, the section $\alpha_0(x)$ is étale locally on $U$ of the form $\iota \langle \zeta \rangle_0$.

For (U2), restrict $\alpha_0(x)$ to a covering of $U$ on which a primitive root $\zeta$ exists. Since $\alpha$ commutes with restriction, each restriction is $\iota \langle \zeta \rangle_0$. For (U1), the local sections $\iota \langle \zeta \rangle_0$ agree on overlaps, because two primitive roots are locally powers of each other. So they glue to a section $\alpha_0(x)$, and $\alpha_p = 0$ for $p > 0$. This cochain is a cocycle: $d \circ \iota = 0$, and the two faces of a $1$-simplex give the same local values. Two unit cocycles agree étale locally, so they are equal. Hence the chosen class $1_E$ is $[\alpha]$.

**Lemma 6.3.3 (Extension along the augmentation).** Let $q \geq 1$ and $i \in \mathbb{Z}$. For each pairing $\lambda : \mathbb{Z}/q(0)[0] \times \mathcal{I}_i \to \mathcal{I}_i$ there is a pairing $\nu : \mathcal{I}_0 \times \mathcal{I}_i \to \mathcal{I}_i$ with $\nu(\varepsilon x, b) = \lambda(x, b)$ for all sections $x$ of $\mathbb{Z}/q(0)$ and $b$ of $\mathcal{I}_i^t$.

Lean: `LateralTheory.Fix.EtaleChapterDTwo.s31`.

*Proof.* We use the tensor products of complexes of [the previous section](/entry/cup-product-tensor-holds-of/). Let $S = \mathbb{Z}/q(0)[0] \otimes \mathcal{I}_i$ and $T = \mathcal{I}_0 \otimes \mathcal{I}_i$. By the universal property, $\lambda$ is $u \circ \otimes$ for a chain map $u : S \to \mathcal{I}_i$. Let $j = \varepsilon \otimes 1 : S \to T$. If we find $g : T \to \mathcal{I}_i$ with $g \circ j = u$, then $\nu = g \circ \otimes$ is the pairing we want.

Such a $g$ exists by a lifting property of $\mathcal{I}_i$. It is a complex of injective sheaves in degrees $\geq 0$. So each chain map into $\mathcal{I}_i$ extends along a map of complexes that is injective in each degree and is a quasi-isomorphism. We check these two properties for $j$.

The map $j$ is injective in each degree. This is a local question, and it follows from a local splitting of $\mathbb{Z}/q(0)$: étale locally, its sections are the multiples of one section $e$, and either $e = 0$ or there is a linear map $r$ to $\mathbb{Z}/q$ with $r(e) = 1$. In the second case $\mathbb{Z}/q(0)$ is locally free of rank one with basis $e$. We omit the details of this step.

The map $j$ is a quasi-isomorphism. The map $\varepsilon$ is one, and tensor products with a complex of flat sheaves in degrees $\geq 0$ keep quasi-isomorphisms. The terms of $\mathcal{I}_i$ are flat, for two reasons. The sections of an injective sheaf form an injective $\mathbb{Z}/q$-module. An injective $\mathbb{Z}/q$-module $M$ is flat. Indeed, by the ideal criterion for flatness it is enough to show: if $e \mid q$ and $em = 0$, then $m \in (q/e)M$. The map $(q/e)\mathbb{Z}/q \to M$ that sends $q/e$ to $m$ is well defined, since the annihilator of $q/e$ is $e\mathbb{Z}/q$. By injectivity it extends to $\varphi : \mathbb{Z}/q \to M$, so $m = (q/e)\varphi(1)$. $\square$

**Definition 6.3.4 (Action).** An *action* of $\mathbb{Z}/q(0)$ on $\mathcal{I}_i$ is a family of bilinear maps $L : \mathbb{Z}/q(0)(U) \times \mathcal{I}_i^t(U) \to \mathcal{I}_i^t(U)$ that commutes with restriction and satisfies $d L(a, b) = L(a, db)$.

**Lemma 6.3.5 (Actions give pairings).** Let $L$ be an action of $\mathbb{Z}/q(0)$ on $\mathcal{I}_i$. There is a pairing $\nu : \mathcal{I}_0 \times \mathcal{I}_i \to \mathcal{I}_i$ with $\nu(\iota a, b) = L(a, b)$ for all sections $a$ of $\mathbb{Z}/q(0)$ and $b$ of $\mathcal{I}_i^t$.

Lean: `LateralTheory.Fix.EtaleChapterDTwo.s32`.

*Proof.* Let $\lambda(x, b) = L(x, b)$ for $x$ in degree $0$ of $\mathbb{Z}/q(0)[0]$, and $\lambda = 0$ in the other degrees. This is a pairing. The Leibniz rule holds because the differential of $\mathbb{Z}/q(0)[0]$ is $0$ and $L$ commutes with $d$. Then [the extension lemma](/entry/s31/) gives $\nu$. $\square$

**Lemma 6.3.6 (A unit pairing).** For each $i$ there is a pairing $\nu : \mathcal{I}_0 \times \mathcal{I}_i \to \mathcal{I}_i$ with $\nu(\iota \langle \zeta \rangle_0, b) = b$ for each scheme $U$, each $\zeta \in \mathrm{Prim}_q(\Gamma(U, \mathcal{O}_U))$ and each $b \in \mathcal{I}_i^t(U)$.

Lean: `LateralTheory.Fix.EtaleChapterDTwo.s33`.

*Proof.* Let $\epsilon_0 : \mathbb{Z}/q(0) \to \mathbb{Z}/q$ be the augmentation that sends each $\langle \zeta \rangle_0$ to $1$, on the presheaf by the sum of the coefficients. It is well defined, because the relations $[\zeta^a] - [\zeta]$ of weight $0$ have coefficient sum $0$. Put $L(a, b) = \epsilon_0(a)\, b$ for sections $a$ of $\mathbb{Z}/q(0)$ and $b$ of $\mathcal{I}_i^t$. This is bilinear and commutes with restriction. It commutes with $d$, because $d$ is $\mathbb{Z}/q$-linear. So $L$ is an action, and $L(\langle \zeta \rangle_0, b) = b$. [The previous lemma](/entry/s32/) turns $L$ into $\nu$ with $\nu(\iota \langle \zeta \rangle_0, b) = b$. $\square$

**Lemma 6.3.7 (A twisted unit pairing).** For each $i$ there is a twisted pairing $\mu : \mathcal{I}_0 \times \mathcal{I}_i \to \mathcal{I}_{0+i}$ with the *unit property*: $\mu(a, b) = b$ for each $a \in \mathcal{I}_0^0(U)$ that is étale locally of the form $\iota \langle \zeta \rangle_0$, and each $b \in \mathcal{I}_i^t(U)$.

Lean: `LateralTheory.Fix.EtaleChapterDTwo.s34`.

*Proof.* Take $\nu$ from [the unit pairing lemma](/entry/s33/). Let $a$ be étale locally $\iota \langle \zeta \rangle_0$. Then $\nu(a, b)$ and $b$ have the same restrictions to the members of an étale covering, since $\nu$ commutes with restriction. Sections of a sheaf are separated, so $\nu(a, b) = b$. For $a = \iota \langle \zeta \rangle_0$ and $b = \iota \langle \zeta \rangle_i$ this gives $\nu(a, b) = \iota \langle \zeta \rangle_i$, so $\nu$ is twisted. Then $\mu$ is $\nu$ with the target $\mathcal{I}_i$ read as $\mathcal{I}_{0+i}$. $\square$

**Theorem 6.3.8 (Unit law).** Let $q \geq 1$ and let $E$ be a space on which $q$ is invertible. For every $a \in H^n(E, \mathbb{Z}/q(i))$,
$$
1_E \cup a = a \quad \text{in } H^{0+n}(E, \mathbb{Z}/q(0+i)) = H^n(E, \mathbb{Z}/q(i)).
$$

Lean: `LateralTheory.Fix.EtaleChapterDTwo.s38`.

*Proof.* Let $a = [\beta]$, and let $\mu$ be [the twisted unit pairing](/entry/s34/). The cup product is $\cup_{\mu_{0,i}}$, and $\mu_{0,i}$ is twisted. By [the uniqueness theorem](/entry/cup-product-tensor-holds-of/), $\cup_{\mu_{0,i}} = \cup_\mu$. Since $q$ is invertible on $E$, (U1) gives a unit cocycle $\alpha$ with $1_E = [\alpha]$, and by (U2) its values are étale locally $\iota \langle \zeta \rangle_0$. Now $\alpha$ is a $0$-cochain, so $\alpha_p(x)$ lies in $\mathcal{I}_0^{-p} = 0$ for $p > 0$. In the Alexander-Whitney formula only the term $p = 0$ is left:
$$
\gamma_N(x) = \mu\big(\alpha_0(x_{[0,0]}),\ \beta_N(x)\big) = \beta_N(x),
$$
by the unit property. So $\beta$ itself is an Alexander-Whitney product of $\alpha$ and $\beta$ for $\mu$. By the defining property of $\cup_\mu$ (see the paragraph after [Definition 6.2.7](/entry/cup-product-tensor-holds-of/)), $[\alpha] \cup_\mu [\beta] = [\beta]$. $\square$

**Remark 6.3.9.** The hypothesis that $q$ is invertible on $E$ is used only through (U1) and (U2). If $q$ is not invertible on $E$, a unit cocycle need not exist, and then $1_E = 0$ by the choice convention. The theorem says nothing in that case.

**Remark 6.3.10 (Formalization).** The five results are the terms `s31`, `s32`, `s33`, `s34` and `s38` of [AwSpec.lean](lean:Development/EtaleCohomology/EtaleSheaves/AwSpec.lean#L99). The facts (U1) and (U2) are the terms `s16`, `s36` and `s37`. The local splitting, the tensor products and the flatness of injective modules are `s19` to `s30`, and the action $L$ of Lemma 6.3.6 is `s17` and `s18`. The twisted unit pairing and the unit law hold up to the identification of $0 + i$ with $i$, and the unit property is stated with a heterogeneous equality, because $\mathcal{I}_{0+i}$ and $\mathcal{I}_i$ are different terms.
