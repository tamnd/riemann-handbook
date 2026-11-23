---
title: The energy bound at infinity
decls:
  - Formalism.L2.SG.RealObj.EnergyInst.inInfinityXAt
  - Formalism.L2.SG.Pf.realObj_inInfinityX_ofG
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The energy bound at infinity

The constants of the previous sections describe how the Haar measure of $G_\infty$ disintegrates along double cosets $S_u \gamma S_{u'}$. This section uses that disintegration to bound an integral of orbit operators. For two words $u, u'$ and $\gamma \in G_\infty$ the orbit operator $O(\gamma)$ is a convolution of two vector valued Whittaker functions. We show that the integral of $\|O(\gamma)\|_{\mathrm{HS}}^2$ over the double cosets, against the disintegration measure, is at most $1/d$, where $d$ is the formal degree of the discrete series at infinity. The bound is used by the [archimedean objects under the uniqueness gap](/entry/real-obj-in-infinity-x-jsz/), and through them by the [theta local matching](/step/theta-local-matching/).

### The setting

Let $F$ be a totally real field and let $G_\infty = \prod_v \mathrm{U}(J_{\varepsilon_v})$, the product over the infinite places $v$ of $F$, with a fixed [Haar measure](/learn/analysis/#haar-measure) $\mu$. Let $\sigma$ be a unitary representation of $G_\infty$ on a Hilbert space $\mathcal{H}$, the tensor product of discrete series representations $\sigma_v$ of formal degrees $d_v$, and let $w \in \mathcal{H}$ be the tensor product of the chosen unit vectors. Let $d = \prod_v d_v$.

Fix $r \geq 0$, $k \geq 1$ and $\mathrm{sc} > 0$. To a word $u$ the setting attaches an isotropic family $e_1, \dots, e_r$ and a vector $z_u$ with $h(z_u, z_u) = -T_u$, $T_u > 0$. At each place $v$ let
$$f_u(a) = \mathrm{sc}^{-(r - a)} e_a \quad (1 \leq a \leq r), \qquad f_u(r + 1) = z_u.$$
For $\gamma \in G_\infty$ and words $u, u'$ let $Z_v(\gamma)$ be the matrix of size $r + 1$ with entries $h(f_u(a), \gamma_v f_{u'}(b))$, and let $D_l(Z)$ be the leading principal minor of size $l$ of a matrix $Z$, with $D_0 = 1$. Put
$$G(Z) = |D_{r+1}(Z)|^2 - T_u T_{u'} |D_r(Z)|^2.$$

**Definition 5.4.1 (Diagonal coordinates).** Let $C = \prod_v \mathbb{C}^{r+1}$, with the measure $dc$ that is the product of $2$ times Lebesgue measure on each factor $\mathbb{C}$. The *good set* is the set of $c \in C$ with $c_{v,l} \neq 0$ for all $v, l$ and $G(\mathrm{diag}(c_v)) > 0$ for all $v$. The *weight* of $c$ is
$$\mathrm{wt}(c) = \prod_v G(\mathrm{diag}(c_v))^{k - 1} \prod_{l = 1}^{r} |D_l(\mathrm{diag}(c_v))|^4.$$
An element $\gamma \in G_\infty$ *has diagonal* $c$ if $Z_v(\gamma) = \mathrm{diag}(c_v)$ for every $v$. For each $c$ we fix an element $\gamma(c)$ that has diagonal $c$, if one exists, and we put $\gamma(c) = 1$ otherwise.

Lean: `Formalism.L2.SG.RealObj.Good`, `Formalism.L2.SG.RealObj.wt`, `Formalism.L2.SG.RealObj.HasDiag`.

So $D_l(\mathrm{diag}(c_v)) = c_{v,1} \cdots c_{v,l}$, and the good set is the set where the last coordinate is large: $|c_{v, r+1}|^2 > T_u T_{u'}$. This is the open set of [the previous section](/entry/jac-gauge/), on which the Levi invariant $\zeta$ has $|\zeta|^2 > T T'$, and the weight is the weight of the big cell written in the coordinates $c$.

For each word $u$ let $S_u \subseteq G_\infty$ be the subgroup attached to the frame of $u$, with Haar measures $\mu_{N,u}$ on its unipotent part and $\mu_{H,u}$ on the stabilizer $H_u$ of the frame. Let $\mu_{S_u}$ be the image of $\mu_{N,u} \times \mu_{H,u}$ under multiplication, and let $\nu_u$ be a quotient measure, in the sense of Weil's formula: $\int f \, d\mu = \int \int f(s x) \, d\mu_{S_u}(s) \, d\nu_u(x)$ for every measurable $f \geq 0$. Let $V_u$ be a finite dimensional Hilbert space with a unitary representation $\pi_u$ of $S_u$, and let $\psi_u$ be a character of $S_u$. A *Whittaker function* for $u$ is a continuous map $W_u : G_\infty \to V_u$ such that:

1. $W_u(s x) = \psi_u(s) \pi_u(s) W_u(x)$ for $s \in S_u$;
2. $W_u$ is reproduced by the matrix coefficient: $\int_{G_\infty} d \cdot \overline{\langle w, \sigma(y) w \rangle} \, W_u(x y) \, d\mu(y) = W_u(x)$ for every $x$;
3. $\int \|W_u\| \, d\nu_u < \infty$ and $\int \|W_u\|^2 \, d\nu_u = 1$.

**Definition 5.4.2 (Disintegration constant).** A real number $C_X > 0$ is a *disintegration constant* for $(u, u', \mathrm{sc})$ if for every measurable $\varphi \geq 0$ on $G_\infty$,
$$\int_{G_\infty} \varphi \, d\mu = \int_{\mathrm{good}} C_X \, \mathrm{wt}(c) \int \int \varphi\big(s \, \gamma(c) \, s'^{-1}\big) \, d\mu_{S_{u'}}(s') \, d\mu_{S_u}(s) \, dc.$$
We write $\nu_M$ for the measure $C_X \, \mathrm{wt}(c) \, dc$ on the good set.

Lean: `Formalism.L2.SG.RealObj.Disint`, `Formalism.L2.SG.RealObj.nuM`.

**Definition 5.4.3 (Orbit operator).** For $\gamma \in G_\infty$ the *orbit operator* $O(\gamma) : V_{u'} \to V_u$ is
$$O(\gamma) \xi = \int_{G_\infty} \langle W_{u'}(\gamma^{-1} x), \xi \rangle \, W_u(x) \, d\mu(x),$$
whenever the integral converges absolutely as an integral of rank one operators.

Lean: `Formalism.L2.SG.RealObj.OOinf`.

**Definition 5.4.4 (Energy bound at infinity).** We say that the *energy bound at infinity* holds for $(u, u', \mathrm{sc})$ if:

1. a disintegration constant $C_X > 0$ exists;
2. every good $c$ is the diagonal of some $\gamma \in G_\infty$, and the orbit integral of $\gamma(c)$ converges absolutely for every good $c$;
3. with the chosen constant $C_X$,
$$\int_{\mathrm{good}} \|O(\gamma(c))\|_{\mathrm{HS}}^2 \, d\nu_M(c) \leq \frac{1}{d}.$$

Lean: `Formalism.L2.SG.RealObj.InInfinityX`.

The bound $1/d$ is the one that the Schur orthogonality relations give for a single matrix coefficient: $\int |\langle w, \sigma(x) w \rangle|^2 \, d\mu(x) = 1/d$ for a unit vector $w$. The orbit operators split this integral over the double cosets, and the bound says that no mass is created by the splitting.

### The bound

The main input is the [abstract energy bound](/entry/energy-abs-holds/). Let $G$ be a unimodular, locally compact, second countable group with Haar measure $\mu$, and let $\sigma$ be a unitary representation that satisfies the Schur orthogonality relations with formal degree $d > 0$. Let $S, S'$ be closed subgroups with Haar measures that satisfy a Følner condition, with quotient measures $\nu, \nu'$, and let $W, W'$ be Whittaker functions as above. If the Haar measure disintegrates as $\int \varphi \, d\mu = \int \int \int \varphi(s h(c) s'^{-1}) \, d\mu_{S'} \, d\mu_S \, dm(c)$ for a measurable map $h$, the orbit integrals of $h(c)$ converge absolutely, and three quadruple integrals of $|\langle \sigma(z) w, \sigma(s h(c) s'^{-1}) \sigma(z') w \rangle| \, \|W(z)\| \, \|W'(z')\|$ are finite, then $\int \|O(h(c))\|_{\mathrm{HS}}^2 \, dm(c) \leq 1/d$.

**Theorem 5.4.5 (Energy bound at infinity).** Fix the setting and its data $D$. Assume:

1. (integrability) for all words $u, u'$, all $\mathrm{sc} > 0$, all good $c$ and all $\gamma$ with diagonal $c$, the orbit integral of $\gamma$ converges absolutely;
2. (convergence) for the same data, the quadruple integral
$$\int \int \int \int \big| \langle \sigma(z) w, \sigma(s \gamma s'^{-1}) \sigma(z') w \rangle \big| \, \|W_u(z)\| \, \|W_{u'}(z')\| \, d\mu_{S_{u'}}(s') \, d\mu_{S_u}(s) \, d\nu_{u'}(z') \, d\nu_u(z)$$
is finite, and for every word $u''$ the triple integral of $$|\langle \sigma(z) w, \sigma(s) \sigma(z') w \rangle| \, \|W_{u''}(z)\| \, \|W_{u''}(z')\|$$ against $d\mu_{S_{u''}}(s) \, d\nu_{u''}(z') \, d\nu_{u''}(z)$ is finite.

Then for all words $u, u'$ and every $\mathrm{sc} > 0$, the energy bound at infinity holds for $(u, u', \mathrm{sc})$.

Lean: `Formalism.L2.SG.RealObj.EnergyInst.inInfinityXAt`.

*Proof.* The Haar disintegration at the real places gives a disintegration constant $C_X > 0$; this is condition 1. At each real place, a good $c$ prescribes the Gram matrix of the frames $f_u$ and $\gamma_v f_{u'}$ jointly, and this Gram matrix is nondegenerate on the good set. Witt's theorem for nondegenerate Hermitian spaces then gives an isometry $\gamma_v$ that moves a frame with this Gram matrix to $\gamma_v f_{u'}$, so every good $c$ is the diagonal of some $\gamma$. With the integrability assumption this gives condition 2.

For condition 3 we apply the abstract energy bound to $G = G_\infty$, the subgroups $S_u, S_{u'}$ and the measure $\nu_M$. The Schur relations hold for $\sigma$ with $d = \prod_v d_v$, and the matrix coefficient $d \, \overline{\langle w, \sigma(y) w \rangle}$ is the reproducing kernel of the Whittaker functions. The subgroups $S_u$ are closed, their Haar measures are bi-invariant and satisfy the Følner condition, and $\psi_u \pi_u$ is a representation of $S_u$; so each $W_u$ satisfies the hypotheses of the abstract bound. The abstract bound needs a measurable map $h$. The chosen $\gamma(c)$ need not be measurable, so we take a measurable map $g$ on $C$ such that $g(c)$ has diagonal $c$ for every good $c$, and we extend it off the good set by a constant value at a good point. If two elements $\gamma, \gamma'$ have the same diagonal, then $\gamma' \in S_u \gamma S_{u'}$ with factors that act unitarily on $V_u$ and $V_{u'}$, so the disintegration of $\mu$ holds with $g$ in place of $\gamma(c)$, and $\|O(g(c))\|_{\mathrm{HS}} = \|O(\gamma(c))\|_{\mathrm{HS}}$ on the good set. The integrability and convergence assumptions, applied at a good point with the same diagonal as $g(c)$, give the remaining hypotheses. The abstract bound gives $\int \|O(g(c))\|_{\mathrm{HS}}^2 \, d\nu_M \leq 1/d$. Since $\nu_M$ lives on the good set, this is condition 3. If the good set is empty, the integral is $0$. $\square$

### The gap hypothesis

The two assumptions of the theorem are proved for the data that satisfy a gap condition on the Harish-Chandra parameters.

**Definition 5.4.6 (Gap hypothesis).** Let the data $D$ have rank $R$ and Harish-Chandra parameters $\tau \mapsto (b_0(\tau), \dots, b_{m-1}(\tau))$. The data satisfy the *gap hypothesis* if $R \geq 1801$ and for every $\tau$ and every $j$ with $j + 1 < m$,
$$b_{j+1}(\tau) - b_j(\tau) \geq 16 R^{19}.$$

Lean: `Formalism.L2.SG.ConcreteSettingExists.GapHyp`.

**Corollary 5.4.7 (Energy bound under the gap hypothesis).** Assume that the integrability and the convergence of the theorem hold for all data $D$ that satisfy the gap hypothesis. Let $D$ satisfy the gap hypothesis. Then for every setting over $D$, all words $u, u'$ and every $\mathrm{sc} > 0$, the energy bound at infinity holds for $(u, u', \mathrm{sc})$.

Lean: `Formalism.L2.SG.Pf.realObj_inInfinityX_ofG`.

*Proof.* This is the [theorem](/entry/in-infinity-xat/) applied to the integrability and the convergence for $D$, which hold by assumption since $D$ satisfies the gap hypothesis. $\square$

The two assumptions are proved from the uniqueness of Bessel models with a gap, in the [archimedean objects under the uniqueness gap](/entry/real-obj-in-infinity-x-jsz/). The quotient measures and the Følner condition come from the [Haar measures on the subgroups](/entry/step-sub-g-holds/) and the [measures on the unipotent radicals](/entry/meas-n-holds/).

**Remark 5.4.8 (Formalization).** The corollary is a pass-through ([RealObjInInfinityXOfG.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/RealObjInInfinityXOfG.lean#L11)): the gap hypothesis is only passed on to the two assumptions. The constant $C_X$ (`DisintegrationConstant`) and the element $\gamma(c)$ (`hOf`) are chosen by the axiom of choice, with the values $0$ and $1$ when none exists. The theorem fixes $D$ and takes the two assumptions for this $D$ (`StepIntAt`, `StepConvAt`); the corollary takes them for all $D$ with the gap hypothesis (`StepIntG`, `StepConvG`). The Schur relations, the subgroup properties and the measurable section are proved inputs (`stepSchurG_holds`, `stepSubG_holds`, `stepSection_holds`). We did not unfold the subgroup condition `InS`, the character `psiInf`, or the formal degree `fdegOf`.
