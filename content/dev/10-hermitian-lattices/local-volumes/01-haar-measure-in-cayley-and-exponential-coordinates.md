---
title: Haar measure in Cayley and exponential coordinates
decls:
  - PI.AprimeInfW.cayDensEx_holds
  - PI.AprimeInfW.expProdU_holds
  - PI.AprimeInfW.grpStd_full
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Haar measure in Cayley and exponential coordinates

A Haar measure on a real Lie group is fixed only up to a scalar. To compare Haar measures on different groups we fix the scalar by the density at the identity: near $1$, in exponential coordinates, the measure is close to Lebesgue measure on the Lie algebra times a constant, the gauge constant. This section proves three facts about this constant for the indefinite unitary groups. In Cayley coordinates the Haar measure has a density that is continuous at $0$. In a product of two exponential charts along an orthogonal splitting of the Lie algebra the same holds, and the value at $0$ is the gauge constant. As a consequence, the Haar measure of a small tube around the stabilizer of a frame is the gauge constant times the volume of the transversal ball times the volume of the stabilizer. The last fact is the input of the [orbit constant on the compact real stabilizer](/entry/aprime-inf-of-hinf-compact/).

### The groups and their Lie algebras

Let $n \geq 0$ and let $\varepsilon \colon \{1, \dots, n\} \to \{+, -\}$ be a sign vector. Let $J_\varepsilon$ be the diagonal matrix with entry $1$ at $i$ if $\varepsilon(i) = +$ and $-1$ otherwise. The [unitary group](/learn/groups/#unitary-groups)
$$\mathrm{U}(J_\varepsilon) = \{ g \in \mathrm{GL}_n(\mathbb{C}) : g^* J_\varepsilon g = J_\varepsilon \}$$
is $\mathrm{U}(p, q)$, where $p$ and $q$ count the signs. Its [Lie algebra](/learn/analysis/#lie-groups-and-lie-algebras) is $\mathfrak{u}(J_\varepsilon) = \{ X \in M_n(\mathbb{C}) : X^* J_\varepsilon + J_\varepsilon X = 0 \}$. We view $M_n(\mathbb{C})$ as the real Euclidean space $\mathbb{R}^{n \times n \times 2}$ of real and imaginary parts of the entries, so that the norm is the Frobenius norm $\|X\|^2 = \sum_{i,j} |X_{ij}|^2$. Then $\mathfrak{u}(J_\varepsilon)$ is a real subspace with an inner product, and it carries a Lebesgue measure $\mathrm{vol}$. Let $B_\rho$ be the ball of radius $\rho$ about $0$ in $\mathfrak{u}(J_\varepsilon)$.

Fix a [Haar measure](/learn/analysis/#haar-measure) $\mu_\varepsilon$ on $\mathrm{U}(J_\varepsilon)$.

**Definition 5.1.1 (Gauge constant).** For $\rho > 0$ let $r_\varepsilon(\rho) = \mu_\varepsilon(\exp B_\rho) / \mathrm{vol}(B_\rho)$. The *gauge constant* $\gamma_\varepsilon$ is the limit of $r_\varepsilon(\rho)$ as $\rho \to 0^+$. We say that the *gauge density exists* for $\varepsilon$ if this limit exists and $\gamma_\varepsilon > 0$. Then the *gauge measure* is $\mu^{\mathrm{g}}_\varepsilon = \gamma_\varepsilon^{-1} \mu_\varepsilon$.

Lean: `Formalism.MainNotions.S.Gauge.gaugeU`, `Formalism.MainNotions.S.Gauge.GaugeDens`, `Formalism.MainNotions.S.Gauge.muGauge`.

The gauge measure does not depend on the choice of $\mu_\varepsilon$: if we scale $\mu_\varepsilon$ by $c$, then $\gamma_\varepsilon$ scales by $c$. It is the Haar measure that agrees with Lebesgue measure on $\mathfrak{u}(J_\varepsilon)$ to first order at the identity. For a product of groups $\prod_v \mathrm{U}(J_{\varepsilon_v})$ over the infinite places $v$ of a totally real field we write $\gamma = \prod_v \gamma_{\varepsilon_v}$.

**Definition 5.1.2 (Volume of the compact unitary group).** For $k \geq 0$ let
$$V_k = \prod_{i=1}^{k} \frac{(2\pi)^i}{(i-1)!}.$$

Lean: `Formalism.MainNotions.S.UnitaryVolumeMass.volU`.

Thus $V_0 = 1$, $V_1 = 2\pi$, the length of the circle $\mathrm{U}(1)$, and $V_k = V_{k-1} (2\pi)^k/(k-1)!$. The number $V_k$ is the volume of the compact group $\mathrm{U}(k)$ for the gauge measure. We take this as an input in the following form.

**Theorem 5.1.3 (Volume of $\mathrm{U}(k)$).** For each $k \geq 0$, the gauge density exists for the constant sign vector $(+, \dots, +)$ of length $k$, and $\mu^{\mathrm{g}}(\mathrm{U}(k)) = V_k$.

Lean: `PI.AprimeInfW.GaugeVolUD`.

This is the formula of Macdonald for the volume of a compact Lie group, for the metric induced by the trace form; see the Notes and references. In this chapter it is a hypothesis of the results that use it.

### The Cayley transform

For $X \in M_n(\mathbb{C})$ with $2 - X$ invertible let
$$\mathrm{cay}(X) = (2 + X)(2 - X)^{-1}.$$
If $X \in \mathfrak{u}(J_\varepsilon)$ then $J_\varepsilon X J_\varepsilon^{-1} = -X^*$, and a short computation gives $\mathrm{cay}(X)^* J_\varepsilon \mathrm{cay}(X) = J_\varepsilon$. So $\mathrm{cay}$ maps a neighbourhood of $0$ in $\mathfrak{u}(J_\varepsilon)$ into $\mathrm{U}(J_\varepsilon)$. It is a rational map, its inverse is $g \mapsto 2(g - 1)(g + 1)^{-1}$ near $1$, and its differential at $0$ is the identity, since $\mathrm{cay}(X) = 1 + X + O(X^2)$.

**Theorem 5.1.4 (Cayley density).** Let $n \geq 0$ and $\varepsilon$ a sign vector of length $n$. There are $r_0 > 0$ and a measurable function $f_0 \colon \mathfrak{u}(J_\varepsilon) \to \mathbb{R}$, continuous at $0$, such that for every measurable set $S \subseteq B_{r_0}$,
$$\mu_\varepsilon(\mathrm{cay}(S)) = \int_S f_0 \, d\mathrm{vol}.$$

Lean: `PI.AprimeInfW.cayDensEx_holds`.

*Proof.* Identify $\mathrm{U}(J_\varepsilon)$ with the standard group $\mathrm{U}(p, q)$ and $\mathfrak{u}(J_\varepsilon)$ with its Lie algebra by the permutation that puts the $+$ signs first; this is a homeomorphism and a group isomorphism, so it carries Haar measure to Haar measure and Lebesgue measure to a Haar measure of the Lie algebra. On $\mathrm{U}(p, q)$ the Cayley transform is a diffeomorphism from an open neighbourhood $D$ of $0$ onto an open neighbourhood of $1$. The pullback of a Haar measure by a diffeomorphism has a density with respect to Lebesgue measure: the Haar measure is given by a smooth nowhere vanishing top form, and its pullback is a smooth function times the Lebesgue form, by the change of variables formula. So the restriction of the Haar measure to $\mathrm{cay}(D)$, pushed to $D$ by $\mathrm{cay}^{-1}$, is Lebesgue measure on $D$ with a density $f$, measurable, continuous at $0$, finite and nonzero at $0$. Choose $r_0$ so that $B_{r_0}$ lies in $D$ and in the set where $f$ is finite, and let $f_0 = f$ on $B_{r_0}$. For $S \subseteq B_{r_0}$ the set $\mathrm{cay}(S)$ is the preimage of $S$ under $\mathrm{cay}^{-1}$ inside $\mathrm{cay}(D)$, and the formula follows. $\square$

**Lemma 5.1.5 (Value of the Cayley density at the identity).** Let $\varepsilon$ be a sign vector for which the gauge density exists, and let $r_0$ and $f_0$ be as in the Cayley density theorem. Then $f_0(0) = \gamma_\varepsilon$.

Lean: `PI.AprimeInfW.cayValId_holds`.

*Proof.* The maps $\exp$ and $\mathrm{cay}$ both have differential $1$ at $0$, so $\mathrm{cay}^{-1} \circ \exp$ is a diffeomorphism near $0$ with differential $1$ at $0$. It maps $B_\rho$ into $B_{\rho(1 + o(1))}$ and contains $B_{\rho(1 - o(1))}$ in its image. Hence $\mu_\varepsilon(\exp B_\rho) = \mu_\varepsilon(\mathrm{cay}(\mathrm{cay}^{-1} \exp B_\rho))$ lies between $\int_{B_{\rho(1 - o(1))}} f_0$ and $\int_{B_{\rho(1 + o(1))}} f_0$. By continuity of $f_0$ at $0$, both are $f_0(0) \mathrm{vol}(B_\rho)(1 + o(1))$. Dividing by $\mathrm{vol}(B_\rho)$ and letting $\rho \to 0$ gives $\gamma_\varepsilon = f_0(0)$. $\square$

### Products of exponential charts

**Theorem 5.1.6 (Haar density in a product chart).** Let $n \geq 0$ and $\varepsilon$ a sign vector of length $n$. Let $\mathfrak{m}, \mathfrak{h}$ be real subspaces of $M_n(\mathbb{C})$ with $\mathfrak{m} + \mathfrak{h} = \mathfrak{u}(J_\varepsilon)$ and $\mathfrak{m} \perp \mathfrak{h}$. Let $L_0 \colon \mathbb{R}^a \to \mathfrak{m}$ and $L_1 \colon \mathbb{R}^b \to \mathfrak{h}$ be linear isometries onto. Assume that the gauge density exists for $\varepsilon$. Then there are $r > 0$ and a measurable function $D$ on $\mathbb{R}^a \times \mathbb{R}^b$, continuous at $0$, with $D(0) = \gamma_\varepsilon$, such that for every measurable set $A$ in the ball of radius $r$,
$$\mu_\varepsilon\big( \{ \exp(L_0 p_1) \exp(L_1 p_2) : (p_1, p_2) \in A \} \big) = \int_A D \, dp.$$

Lean: `PI.AprimeInfW.expProdU_holds`.

*Proof.* By the [Cayley density](/entry/cay-dens-ex-holds/) the Haar measure near $1$ is $f_0 \, d\mathrm{vol}$ in Cayley coordinates, and $f_0(0) = \gamma_\varepsilon$ by the lemma on its value at the identity. Let $\Phi(p_1, p_2) = \mathrm{cay}^{-1}(\exp(L_0 p_1) \exp(L_1 p_2))$. Near $0$ this is a smooth map into $\mathfrak{u}(J_\varepsilon)$, and its differential at $0$ is $(p_1, p_2) \mapsto L_0 p_1 + L_1 p_2$. Since $\mathfrak{m} \perp \mathfrak{h}$ and $\mathfrak{m} + \mathfrak{h} = \mathfrak{u}(J_\varepsilon)$, this differential is an isometry onto, so its Jacobian is $1$ and $\Phi$ is a diffeomorphism near $0$. By the change of variables formula, $D = (f_0 \circ \Phi) \cdot |\det d\Phi|$ is the required density. It is continuous at $0$ and $D(0) = f_0(0) = \gamma_\varepsilon$. $\square$

### Tubes around the stabilizer of a frame

Let $F$ be a totally real number field with $d$ infinite places, and let $G_\infty = \prod_v \mathrm{U}(J_{\varepsilon_v})$ be the archimedean group of a Hermitian space of dimension $n$, with the product $\mu_\infty$ of the fixed Haar measures. Let $Y_0$ be a frame of $2r + 1$ vectors, and let $H_\infty \subseteq G_\infty$ be its stabilizer. For a set $V \subseteq G_\infty$ the *tube* over $V$ is $\mathrm{Tube}(V) = \{ g : g Y_0 \in V Y_0 \} = V H_\infty$.

Let $k$ be the dimension of the orthogonal complement of the frame. Assume that there are $c \in G_\infty$ and, at each $v$, a set $S_v$ of $k$ indices with $\varepsilon_v = +$ on $S_v$, such that $c^{-1} H_\infty c$ is the group of $g$ with $g_v e_i = e_i$ for all $i \notin S_v$ (the standard $\mathrm{U}(k)$ on the coordinates $S_v$). Let $L \colon \mathbb{R}^m \to \prod_v \mathfrak{u}(J_{\varepsilon_v})$ be a linear isometry onto the orthogonal complement of the Lie algebra of this standard $\mathrm{U}(k)^d$, and let $\kappa(x) = c \exp(L x) c^{-1}$.

**Theorem 5.1.7 (Tube volume).** Assume the product chart theorem and the volume of $\mathrm{U}(k)$ for every $k$. With the notation above, and under the standing hypotheses on the measures of the setting, the sets $\mathrm{Tube}(\kappa(B_\rho))$ are measurable with finite positive measure for small $\rho$, and
$$\lim_{\rho \to 0^+} \frac{\mu_\infty(\mathrm{Tube}(\kappa(B_\rho)))}{\mathrm{vol}(B_\rho)} = \gamma \, V_k^{d}.$$

Lean: `PI.AprimeInfW.grpStd_full`.

*Proof.* Apply the [product chart](/entry/exp-prod-u-holds/) at each place to the splitting of $\mathfrak{u}(J_{\varepsilon_v})$ into the Lie algebra $\mathfrak{u}(k)$ of the standard block and its complement. With $\mathfrak{m}$ the complement and $\mathfrak{h} = \mathfrak{u}(k)$, the theorem gives a chart of $\mathrm{U}(k)$ itself (take $\mathfrak{m} = \mathfrak{u}(k)$ and $\mathfrak{h} = 0$), and the volume of $\mathrm{U}(k)$ turns it into a description of the Haar measure on the block: in the coordinates $\exp(L x) h$, with $x$ small and $h$ in the block, the measure $\mu_\varepsilon$ is $D(x)\, dx \, d\mu^{\mathrm{g}}(h)$ up to an error that tends to $0$ with $x$. The tube $\kappa(B_\rho) H_\infty$ is the conjugate by $c$ of $\exp(L B_\rho) \cdot \mathrm{U}(k)^d$, and conjugation preserves Haar measure. So its measure is $\int_{B_\rho} D \, dx \cdot V_k^d$, and dividing by $\mathrm{vol}(B_\rho)$ and letting $\rho \to 0$ gives $D(0) V_k^d = \gamma V_k^d$. $\square$

**Remark 5.1.8 (Formalization).** The tube theorem is stated with a hypothesis on the measures of the setting (self-dual measures on frames and Hermitian matrices and a fibre family, bundled as `PushHyp`) that we do not unfold; the limit does not use it. The product chart is `expProdU_of_hua` applied to it and to the Cayley density ([CayDensExEnd.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ArchimedeanOrbitMeasures/CayDensExEnd.lean#L7)). The tube theorem is `grpStd_of_exp_block` applied to the product chart and to the block measure `blockHaarV_of (ukChart_of hE) hG`. The gauge constant is defined as a `limUnder`, so it is a number even when the limit does not exist; the condition that the gauge density exists is what makes it meaningful.
