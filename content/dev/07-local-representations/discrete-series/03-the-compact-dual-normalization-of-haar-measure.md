---
title: The compact dual normalization of Haar measure
decls:
  - ReciprocityTheory.ChartRestriction.DS.tie_d_eq
  - ReciprocityTheory.ChartRestriction.DS.omegaDensity_muCDtr
  - ReciprocityTheory.ChartRestriction.DS.muCD_eq_cd_vol
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The compact dual normalization of Haar measure

A Haar measure on $U(p,q)$ is fixed up to a positive constant. Formal degrees are usually given for one particular choice: the measure that matches the Haar probability measure of the compact dual group $U(p+q)$ through the common complexified Lie algebra $\mathfrak{gl}_n(\mathbb{C})$. This section proves that the polar measure of [Theorem 3.2.8](/entry/mu-polar-is-haar/), multiplied by an explicit constant, is this measure. The result is used in the step [EveryCharacter from the literature](/step/every-character-of-literature/), where formal degrees of discrete series are compared with the values in the literature.

Background: [Haar measure](/learn/analysis/#haar-measure), [discrete series and formal degrees](/learn/real-groups/#discrete-series-and-formal-degrees), [[Haar measure|VY0HXD3GC4]].

We keep the notation of the previous two sections: the sign vector $\varepsilon$ with $p$ plus signs and $q$ minus signs, $n = p + q$, the group $G_\varepsilon \cong U(p,q)$, the polar measure $\mu^{\mathrm{pol}}_\varepsilon$, and the volumes $v(m)$ of [Theorem 3.1.5](/entry/vol-u-density/).

### The density in exponential coordinates

Let $\mathcal{G}_\varepsilon = \mathcal{K}_\varepsilon \times \mathbb{C}^{\Pi_\varepsilon}$, with the coordinates $S$ on $\mathfrak{k}$ and $P$ on $\mathfrak{p}$ of the previous section. So $(x, z) \mapsto S(x) + P(z)$ is a real linear isomorphism from $\mathcal{G}_\varepsilon$ onto $\mathfrak{g}$. For $D \subseteq \mathcal{G}_\varepsilon$ put
$$\operatorname{Exp}(D) = \{ g \in G_\varepsilon : g = \exp\bigl(S(x) + P(z)\bigr) \text{ for some } (x, z) \in D \}.$$

**Definition 3.3.1 (Density at the identity).** Let $\nu$ be a measure on $G_\varepsilon$ and $d > 0$. We say that $\nu$ has *density $d$ at the identity in exponential coordinates* if for every $\eta > 0$ there is $\delta > 0$ such that for every measurable $D \subseteq \mathcal{G}_\varepsilon$ with $\|s\| < \delta$ for all $s \in D$,
$$(1 - \eta)\, d \operatorname{vol}(D) \leq \nu\bigl(\operatorname{Exp}(D)\bigr) \leq (1 + \eta)\, d \operatorname{vol}(D).$$

Every Haar measure on $G_\varepsilon$ has a density at the identity in this sense, because the exponential map is a diffeomorphism near $0$ with differential $1$ at $0$, and a Haar measure is a smooth positive multiple of the Riemannian volume.

**Proposition 3.3.2 (Density of the polar measure).** Let $d > 0$. If $\mu^{\mathrm{pol}}_\varepsilon$ has density $d$ at the identity in exponential coordinates, then
$$d = \frac{1}{v(p)\,v(q)}.$$

Lean: `ReciprocityTheory.ChartRestriction.DS.tie_d_eq`.

*Proof.* For a Haar measure, a density $d$ in exponential coordinates $\exp(S(x) + P(z))$ is also a density $d$ in the polar coordinates $\exp(S(x))\exp(P(z))$ on product sets. The two maps agree to first order at $0$, and the Haar measure is invariant under the translations that relate them. On the other hand, [Proposition 3.2.9](/entry/mu-polar-near-one/) says that $\mu^{\mathrm{pol}}_\varepsilon$ has density $D = 1/(v(p)v(q))$ in polar coordinates on product sets $B \times C$. Fix $\eta \in (0, 1)$ and take $B$ and $C$ to be small balls, so that both estimates apply to the same set $\operatorname{Pol}(B \times C)$, whose coordinate volume $\operatorname{vol}(B)\operatorname{vol}(C)$ is positive and finite. Then
$$(1 - \eta)\, d \leq (1 + \eta)\, D \quad\text{and}\quad (1 - \eta)\, D \leq (1 + \eta)\, d.$$
Let $\eta \to 0$. $\square$

### The Lebesgue measure of the compact dual

The Lie algebra of $U(p,q)$ and the Lie algebra of $U(p+q)$ are two real forms of $\mathfrak{gl}_n(\mathbb{C})$. A measure on the first one fixes a measure on the second, and this is how the two Haar measures are matched. We use the standard model: $U(P,Q)$ is the group of $g$ with $g^* J g = J$ for $J = \operatorname{diag}(1_P, -1_Q)$, with Lie algebra $\mathfrak{u}(P,Q) = \{ X : X^* J + J X = 0 \}$.

**Definition 3.3.3 (Lebesgue measure on $\mathfrak{u}(P,Q)$).** Let $\lambda$ be an additive Haar measure on the real vector space $\mathfrak{u}(P,Q)$. We call $\lambda$ *compatible* if the image of $\lambda \times \lambda$ under $(X, Y) \mapsto X + iY$ is Lebesgue measure on $M_{P+Q}(\mathbb{C}) = \mathbb{C}^{(P+Q)^2}$.

Since $\mathfrak{u}(P,Q) \oplus i\,\mathfrak{u}(P,Q) = \mathfrak{gl}_{P+Q}(\mathbb{C})$, the map $(X,Y) \mapsto X + iY$ is a real linear isomorphism, and there is exactly one compatible measure. The same rule for $Q = 0$ gives the compatible measure on $\mathfrak{u}(P)$.

**Definition 3.3.4 (Density with respect to the Lie algebra).** Let $\nu$ be a measure on $U(P,Q)$ and $c \in [0, \infty]$. Let $B_r = \{X \in \mathfrak{u}(P,Q) : \sum_{a,b} |X_{ab}| < r\}$. We say that $\nu$ has *Lie density $c$* if, for the compatible measure $\lambda$,
$$\lim_{r \to 0^+} \frac{\nu\bigl(\exp(B_r)\bigr)}{\lambda(B_r)} = c.$$

Put
$$c(N) = \frac{1}{2^{N(N-1)/2}\, v(N)}, \qquad C_\varepsilon = \frac{\prod_{i<n} i!}{\pi^{pq} \prod_{i<p} i! \prod_{i<q} i!}.$$
A short computation with the formula for $v$ gives $C_\varepsilon = v(p)\,v(q)/v(n)$. By [Theorem 3.1.5](/entry/vol-u-density/), the Haar probability measure of $U(N)$ has Lie density $c(N)$: the factor $2^{-N(N-1)/2}$ is the ratio between the compatible measure and Lebesgue measure in the coordinates $S$.

Fix a bijection $e : \{1, \dots, P\} \sqcup \{1, \dots, Q\} \to \{1, \dots, n\}$ such that $\varepsilon \circ e$ is $+$ on the first part and $-$ on the second. Conjugation by the permutation matrix of $e$ is an isomorphism $U(P,Q) \to G_\varepsilon$. Let $\mu^{\mathrm{cd}}_\varepsilon = C_\varepsilon\, \mu^{\mathrm{pol}}_\varepsilon$, and let $\mu^{\mathrm{cd}}_{e}$ be the corresponding measure on $U(P,Q)$.

**Theorem 3.3.5 (Lie density of the normalized polar measure).** With $e$ as above, the measure $\mu^{\mathrm{cd}}_e$ on $U(P,Q)$ has Lie density $c(n)$.

Lean: `ReciprocityTheory.ChartRestriction.DS.omegaDensity_muCDtr`.

*Proof.* Since $\mu^{\mathrm{pol}}_\varepsilon$ is a Haar measure ([Theorem 3.2.8](/entry/mu-polar-is-haar/)), it has some density $d > 0$ at the identity in exponential coordinates, and [Proposition 3.3.2](/entry/tie-d-eq/) gives $d = 1/(v(p)v(q))$. The linear isomorphism $(x, z) \mapsto S(x) + P(z)$, followed by the reindexing by $e$, carries Lebesgue measure on $\mathcal{G}_\varepsilon$ to $2^{-n(n-1)/2}$ times the compatible measure. So for small $r$, the ratio $\mu^{\mathrm{cd}}_e(\exp B_r)/\lambda(B_r)$ is close to $C_\varepsilon\, d / 2^{n(n-1)/2}$. By $C_\varepsilon = v(p)v(q)/v(n)$ this is $1/(2^{n(n-1)/2} v(n)) = c(n)$. $\square$

### Matching with the compact dual

**Definition 3.3.6 (Compact dual normalization).** A *compact dual normalization* is a family of measures $\nu_{P,Q}$ on $U(P,Q)$, one for each $P, Q \geq 0$, such that:

1. each $\nu_{P,Q}$ is a Haar measure;
2. $\nu_{N,0}$ is a probability measure on the compact group $U(N)$;
3. for all $P, Q$ there is $c \in (0, \infty)$ such that $\nu_{P,Q}$ and $\nu_{P+Q,0}$ both have Lie density $c$.

Condition 3 is the matching through $\mathfrak{gl}_n(\mathbb{C})$. Conditions 1 to 3 determine the family, as the next theorem shows.

**Theorem 3.3.7 (The normalized polar measure is the compact dual measure).** Let $(\nu_{P,Q})$ be a compact dual normalization, and let $e$ be as above. Then for every measurable set $A \subseteq G_\varepsilon$,
$$\mu^{\mathrm{cd}}_\varepsilon(A) = \nu_{P,Q}\bigl(\{ g \in U(P,Q) : e \cdot g \cdot e^{-1} \in A \}\bigr),$$
where $e \cdot g \cdot e^{-1}$ is the matrix $g$ with rows and columns reindexed by $e$.

Lean: `ReciprocityTheory.ChartRestriction.DS.muCD_eq_cd_vol`.

*Proof.* Both $\nu_{P,Q}$ and $\mu^{\mathrm{cd}}_e$ are Haar measures on $U(P,Q)$. By uniqueness of Haar measure, there is a finite constant $a$ with $\nu_{P,Q}(E)\, C_\varepsilon = a\, \mu^{\mathrm{cd}}_e(E)$ for every $E$. Lie densities are unique, because the compatible measure is unique and limits are unique. By condition 3, $\nu_{P,Q}$ has the same Lie density as $\nu_{n,0}$. By conditions 1 and 2 and [Theorem 3.1.5](/entry/vol-u-density/), that density is $c(n)$. By [Theorem 3.3.5](/entry/omega-density-mu-cdtr/), $\mu^{\mathrm{cd}}_e$ also has Lie density $c(n)$. Taking the limit in the relation between the two measures on the sets $\exp(B_r)$ gives $c(n)\, C_\varepsilon = a\, c(n)$, so $a = C_\varepsilon$. Hence $\nu_{P,Q} = \mu^{\mathrm{cd}}_e$, which is the claim. $\square$

**Remark 3.3.8 (Formalization).** The compact dual normalization is a hypothesis of the last theorem: the family $(\nu_{P,Q})$ is an argument, and the theorem does not construct it. Its existence follows from the theorem in the other direction (take $\nu_{P,Q}$ to be the normalized polar measures), but we have not found that statement among the declarations of this chapter. The group $G_\varepsilon$ is defined twice, once in the discrete series development and once in the general notation; the final theorem converts between the two copies ([OmegaDensityUnique.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/FormalDegree/HaarVolumes/OmegaDensityUnique.lean#L298)). The Lie density of the Haar probability measure of $U(N)$ is a separate lemma that uses the density theorem of the first section ([Bridge.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/FormalDegree/HaarVolumes/Bridge.lean#L28)); we have read only its statement.
