---
title: Haar measure in polar coordinates
decls:
  - ReciprocityTheory.ChartRestriction.DS.coreP
  - ReciprocityTheory.ChartRestriction.DS.muPolarMat_mul_right
  - ReciprocityTheory.ChartRestriction.DS.muPolar_mul_right
  - ReciprocityTheory.ChartRestriction.DS.muPolar_isHaar
  - ReciprocityTheory.ChartRestriction.DS.muPolar_near_one
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Haar measure in polar coordinates

To compare formal degrees with the volumes that appear in the trace formula, the proof needs a Haar measure on $U(p,q)$ that is given by a formula. This section builds it from the polar decomposition $g = k \exp(X)$, with $k$ in the maximal compact subgroup and $X$ in the noncompact part of the Lie algebra. We prove that the measure is right invariant, that it is a Haar measure, and that near the identity it has an explicit density with respect to Lebesgue measure. The density uses the volumes of unitary groups from [Theorem 3.1.5](/entry/vol-u-density/). The measure is used in the next section to fix the normalization of Haar measure, and through it in the step [EveryCharacter from the literature](/step/every-character-of-literature/).

Background: [Haar measure](/learn/analysis/#haar-measure), [Lie groups and Lie algebras](/learn/analysis/#lie-groups-and-lie-algebras), [unitary groups](/learn/groups/#unitary-groups), [[Haar measure|VY0HXD3GC4]].

### The group and its polar coordinates

Fix $n \geq 0$ and a sign vector $\varepsilon \in \{+,-\}^n$ with $p$ plus signs and $q$ minus signs. Let $J_\varepsilon = \operatorname{diag}(\varepsilon_1, \dots, \varepsilon_n)$, with $\pm$ read as $\pm 1$.

**Definition 3.2.1 (The group $G_\varepsilon$ and its compact subgroup).** Let $G_\varepsilon = \{ g \in M_n(\mathbb{C}) : g^* J_\varepsilon g = J_\varepsilon \}$. It is a group isomorphic to $U(p,q)$. Let $K_\varepsilon$ be the subgroup of unitary matrices in $G_\varepsilon$. Then $K_\varepsilon \cong U(p) \times U(q)$ is a maximal compact subgroup of $G_\varepsilon$. Let $dk$ be the Haar probability measure on $K_\varepsilon$.

The Lie algebra of $G_\varepsilon$ is $\mathfrak{g} = \mathfrak{k} \oplus \mathfrak{p}$. Here $\mathfrak{k}$ consists of the skew-Hermitian matrices with nonzero entries only between indices of the same sign, and $\mathfrak{p}$ consists of the Hermitian matrices with nonzero entries only between indices of different signs. We parametrize $\mathfrak{p}$ directly.

**Definition 3.2.2 (Polar coordinates).** Let $\Pi_\varepsilon$ be the set of pairs $(a,b)$ with $b < a$ and $\varepsilon_a \neq \varepsilon_b$. For $z \in \mathbb{C}^{\Pi_\varepsilon}$ let $P(z)$ be the Hermitian matrix with entry $z_{ab}$ at $(a,b)$ and entry $\overline{z_{ab}}$ at $(b,a)$ for $(a,b) \in \Pi_\varepsilon$, and $0$ elsewhere. Let $\mu_1(z), \dots, \mu_n(z)$ be the eigenvalues of $P(z)$. Put $\operatorname{shc}(u) = \sinh(u)/u$ for $u \neq 0$ and $\operatorname{shc}(0) = 1$, and
$$\operatorname{Jac}(z) = \prod_{a < b} \operatorname{shc}\bigl(\mu_a(z) - \mu_b(z)\bigr).$$
The *polar map* is $\Phi(k, z) = k \exp(P(z))$, from $K_\varepsilon \times \mathbb{C}^{\Pi_\varepsilon}$ to $M_n(\mathbb{C})$.

The set $\Pi_\varepsilon$ has $pq$ elements, so $\mathbb{C}^{\Pi_\varepsilon}$ is a real space of dimension $2pq = \dim \mathfrak{p}$. The function $\operatorname{Jac}$ is positive and continuous, it does not depend on the order of the eigenvalues, and it equals $1$ at $z = 0$.

**Definition 3.2.3 (Polar measure).** Let $\mu^{\mathrm{mat}}_\varepsilon$ be the image under $\Phi$ of the product measure $dk \times \operatorname{Jac}(z)\,dz$, where $dz$ is Lebesgue measure on $\mathbb{C}^{\Pi_\varepsilon}$. It is a measure on $M_n(\mathbb{C})$. Let $\mu^{\mathrm{pol}}_\varepsilon$ be its pullback along the inclusion $G_\varepsilon \to M_n(\mathbb{C})$.

The factor $\operatorname{Jac}$ is the Jacobian of the map $\mathfrak{p} \to K_\varepsilon \backslash G_\varepsilon$, $X \mapsto K_\varepsilon \exp(X)$. For a general real reductive group this is the integral formula for the decomposition $G = K \exp(\mathfrak{p})$ in Helgason's book (see the Notes at the end of the chapter).

### Invariance of the density on $\mathfrak{p}$

The group $G_\varepsilon$ acts on the right on $K_\varepsilon \backslash G_\varepsilon$. In polar coordinates this action is a map on $\mathbb{C}^{\Pi_\varepsilon}$. For a matrix $h$, let $\operatorname{plog}(h) = \tfrac12 \log(h^* h)$, defined by the functional calculus of the Hermitian matrix $h^* h$.

**Definition 3.2.4 (Right action on $\mathfrak{p}$).** For $g \in G_\varepsilon$ and $z \in \mathbb{C}^{\Pi_\varepsilon}$, let $z \cdot g \in \mathbb{C}^{\Pi_\varepsilon}$ be the vector of the $\Pi_\varepsilon$ entries of $\operatorname{plog}\bigl(\exp(P(z))\, g\bigr)$.

If $\exp(P(z)) g = k' \exp(P(z'))$ is the polar decomposition, then $(\exp(P(z))g)^*(\exp(P(z))g) = \exp(2P(z'))$, so $z \cdot g = z'$.

**Lemma 3.2.5 (Invariance of $\operatorname{Jac}(z)\,dz$).** For every $g \in G_\varepsilon$, the image of the measure $\operatorname{Jac}(z)\,dz$ under $z \mapsto z \cdot g$ is $\operatorname{Jac}(z)\,dz$.

Lean: `ReciprocityTheory.ChartRestriction.DS.coreP`.

*Proof.* The matrix $h = J_\varepsilon g^* J_\varepsilon$ lies in $G_\varepsilon$ and is the inverse of $g$. So $z \mapsto z \cdot g$ is a bijection with inverse $z \mapsto z \cdot h$, and it is differentiable. The key identity is the Jacobian formula
$$\bigl|\det D_z(z \mapsto z \cdot g)\bigr| \cdot \operatorname{Jac}(z \cdot g) = \operatorname{Jac}(z)$$
for all $z$. It comes from the derivative of the exponential map, $D\exp_X = \exp(X) \circ \frac{1 - e^{-\operatorname{ad} X}}{\operatorname{ad} X}$, restricted to $\mathfrak{p}$: the determinant of this operator on $\mathfrak{p}$, modulo $\mathfrak{k}$, is $\operatorname{Jac}$. Given the identity, the change of variables formula gives, for a measurable set $A$,
$$\int_{\{z : z \cdot g \in A\}} \operatorname{Jac}(z)\,dz = \int_{\{z : z \cdot g \in A\}} |\det D_z|\,\operatorname{Jac}(z \cdot g)\,dz = \int_A \operatorname{Jac}(z')\,dz'.$$
$\square$

### Right invariance and the Haar property

**Proposition 3.2.6 (Right invariance on matrices).** Let $G_0 \in G_\varepsilon$. Then the image of $\mu^{\mathrm{mat}}_\varepsilon$ under $A \mapsto A G_0$ is $\mu^{\mathrm{mat}}_\varepsilon$.

Lean: `ReciprocityTheory.ChartRestriction.DS.muPolarMat_mul_right`.

*Proof.* Fix $z$. Write $\exp(P(z)) G_0 = k' \exp(P(z \cdot G_0))$ with $k' \in K_\varepsilon$. Then $\Phi(k, z) G_0 = \Phi(k k', z \cdot G_0)$. For a measurable set $S$, Fubini gives
$$\mu^{\mathrm{mat}}_\varepsilon(S G_0^{-1}) = \int dk\bigl(\{k : \Phi(k k', z \cdot G_0) \in S\}\bigr) \operatorname{Jac}(z)\,dz.$$
Since $dk$ is invariant under $k \mapsto kk'$, the integrand is $dk(\{k : \Phi(k, z \cdot G_0) \in S\})$. By [Lemma 3.2.5](/entry/core-p/), the substitution $z \mapsto z \cdot G_0$ keeps $\operatorname{Jac}(z)\,dz$, so the integral is $\mu^{\mathrm{mat}}_\varepsilon(S)$. $\square$

**Corollary 3.2.7 (Right invariance on the group).** For every $g \in G_\varepsilon$, the image of $\mu^{\mathrm{pol}}_\varepsilon$ under $x \mapsto x g$ is $\mu^{\mathrm{pol}}_\varepsilon$.

Lean: `ReciprocityTheory.ChartRestriction.DS.muPolar_mul_right`.

*Proof.* The inclusion $G_\varepsilon \to M_n(\mathbb{C})$ is a closed embedding, and right multiplication by $g$ commutes with it. So the pullback of $\mu^{\mathrm{mat}}_\varepsilon$ commutes with right translation, and [Proposition 3.2.6](/entry/mu-polar-mat-mul-right/) gives the claim. $\square$

**Theorem 3.2.8 (The polar measure is a Haar measure).** The measure $\mu^{\mathrm{pol}}_\varepsilon$ is a left Haar measure on $G_\varepsilon$: it is finite on compact sets, positive on nonempty open sets, and invariant under left translation.

Lean: `ReciprocityTheory.ChartRestriction.DS.muPolar_isHaar`.

*Proof.* The measure is invariant under inversion. Indeed $(k \exp(P(z)))^{-1} = k^{-1} \exp(-k P(z) k^{-1})$. The substitutions $k \mapsto k^{-1}$ and $z \mapsto$ (the coordinates of $-kP(z)k^{-1}$) keep $dk$ and $\operatorname{Jac}(z)\,dz$, because conjugation by $k \in K_\varepsilon$ is a unitary change of coordinates on $\mathfrak{p}$ that keeps the eigenvalues. A measure that is invariant under right translation, by [Corollary 3.2.7](/entry/mu-polar-mul-right/), and under inversion is invariant under left translation, since $gx = (x^{-1} g^{-1})^{-1}$. The polar map is onto $G_\varepsilon$: for $g \in G_\varepsilon$, take $z$ with $\exp(P(z)) = (g^*g)^{1/2}$ and $k = g \exp(-P(z))$. The polar map is also a closed embedding of $K_\varepsilon \times \mathbb{C}^{\Pi_\varepsilon}$ into $M_n(\mathbb{C})$. So the preimage of a compact set $K$ is compact, and $\mu^{\mathrm{pol}}_\varepsilon(K)$ is the integral of the continuous function $\operatorname{Jac}$ over a compact set, which is finite. The preimage of a nonempty open set is nonempty and open, by continuity and surjectivity, and $dk \times \operatorname{Jac}(z)\,dz$ is positive on nonempty open sets. $\square$

### The density near the identity

To compare $\mu^{\mathrm{pol}}_\varepsilon$ with other normalizations, we need its density near the identity. Let $\Pi^K_\varepsilon$ be the set of pairs $(a,b)$ with $b < a$ and $\varepsilon_a = \varepsilon_b$, and let $\mathcal{K}_\varepsilon = \mathbb{R}^n \times \mathbb{C}^{\Pi^K_\varepsilon}$. For $x = (s, w) \in \mathcal{K}_\varepsilon$ let $S(x)$ be the skew-Hermitian matrix with diagonal $i s$, entry $w_{ab}$ at $(a,b)$ and $-\overline{w_{ab}}$ at $(b,a)$. Then $S$ is a linear isomorphism of $\mathcal{K}_\varepsilon$ onto $\mathfrak{k}$, and it is the product of the coordinates of [Theorem 3.1.5](/entry/vol-u-density/) for $U(p)$ and $U(q)$. For $D \subseteq \mathcal{K}_\varepsilon \times \mathbb{C}^{\Pi_\varepsilon}$ let
$$\operatorname{Pol}(D) = \{ g \in G_\varepsilon : g = \exp(S(x)) \exp(P(z)) \text{ for some } (x, z) \in D \}.$$
Let $v(m)$ be the volume of $U(m)$ from [the previous section](/entry/vol-u-density/).

**Proposition 3.2.9 (Density of the polar measure near $1$).** Let $\eta > 0$. There is $\delta > 0$ with the following property. Let $B \subseteq \mathcal{K}_\varepsilon$ and $C \subseteq \mathbb{C}^{\Pi_\varepsilon}$ be measurable, with $\|x\| < \delta$ for $x \in B$ and $\|z\| < \delta$ for $z \in C$. Then
$$\begin{aligned}
\mu^{\mathrm{pol}}_\varepsilon\bigl(\operatorname{Pol}(B \times C)\bigr) &\leq \frac{1 + \eta}{v(p)\,v(q)} \operatorname{vol}(B) \operatorname{vol}(C), \\
\mu^{\mathrm{pol}}_\varepsilon\bigl(\operatorname{Pol}(B \times C)\bigr) &\geq \frac{1 - \eta}{v(p)\,v(q)} \operatorname{vol}(B) \operatorname{vol}(C).
\end{aligned}$$

Lean: `ReciprocityTheory.ChartRestriction.DS.muPolar_near_one`.

*Proof.* Let $t = \min(\eta, 1)/3$. Three facts hold for small $\delta$. First, since $\operatorname{Jac}$ is continuous with $\operatorname{Jac}(0) = 1$, the integral of $\operatorname{Jac}$ over $C$ lies between $(1 \pm t)\operatorname{vol}(C)$. Second, the map $x \mapsto \exp(S(x))$ is injective on the ball of radius $\delta$, so $\exp(S(B))$ is a measurable subset of $K_\varepsilon$. Third, the $dk$-measure of $\exp(S(B))$ lies between $(1 \pm t)\operatorname{vol}(B)/(v(p)v(q))$. This last fact is [Theorem 3.1.5](/entry/vol-u-density/) applied to the factors $U(p)$ and $U(q)$ of $K_\varepsilon$, since $dk$ is the product of the Haar probability measures of the factors. Since the polar map is injective, $\mu^{\mathrm{pol}}_\varepsilon(\operatorname{Pol}(B \times C))$ is the product of the $dk$-measure of $\exp(S(B))$ and the integral of $\operatorname{Jac}$ over $C$. Multiply the bounds: $(1+t)^2 \leq 1 + 3t \leq 1 + \eta$ and $(1-t)^2 \geq 1 - 2t \geq 1 - \eta$. $\square$

**Remark 3.2.10 (Formalization).** The polar measure is first built on all matrices and then pulled back to $G_\varepsilon$. The pullback of a measure is defined to be $0$ when the map is not a measurable embedding, so the proof of right invariance has a second case that never occurs for the inclusion ([PolarRight.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/FormalDegree/PolarRight.lean#L89)). The function $\operatorname{plog}$ is defined for all matrices, without a positivity hypothesis ([PolarAct.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/FormalDegree/PolarAct.lean#L16)); it is only used on $\exp(P(z))g$ with $g \in G_\varepsilon$. The Jacobian identity in the proof of the invariance lemma is a separate lemma ([JacAll.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/FormalDegree/JacAll.lean#L115)); we have read its statement but not its proof, so the explanation through $D\exp$ is the classical argument, not a summary of that proof.
