---
title: Unfolding and the flag measure bound
decls:
  - GlobalTheory.FlagUnfold.unfoldBound
  - GlobalTheory.T.isotropicFlag_unfolding_bound
  - GlobalTheory.FlagMeas.Bound.flagMeasureBound
  - GlobalTheory.T.isotropicFlagProbabilityBound_of_volumeRatio
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Unfolding and the flag measure bound

This section bounds the probability that a random point of the adelic quotient has a short isotropic flag of a given type. First it sums the bound for one flag class of the third section over all classes, which gives the unfolding bound. Then it divides by the volume of the quotient and uses the volume ratio between unitary groups of different ranks. The result is the flag measure bound, with an explicit constant $\kappa(E,p,q,j)$. The counting theorem of the sixth section uses it for the points where the lattice has a short flag.

### Points of a given type

We keep the global setting of the second section. Let $G_{\mathbb{A}} = G_\infty \times G_f$, let $\Gamma$ be the rational points, diagonally embedded, and let $\mu_f$ be a Haar measure on $G_f$. Let $\mu_{\mathbb{A}}$ be the product of $\bigotimes_v \mu_{G_v}$ and $\mu_f$. For $x \in G_{\mathbb{A}}$ let $\Lambda_x$ be the lattice attached to $x$. For $t > 0$ let $\Lambda_x^{<t}$ be the sum of the nonzero sublattices of $\Lambda_x$ whose largest size is less than $t$, and let $\Lambda_x^{\le t}$ be the same with "at most $t$". These are the steps of the canonical filtration of $\Lambda_x$ (see [lattices in Hermitian spaces](/learn/hermitian-lattices/#lattices-in-quadratic-and-hermitian-spaces)).

**Definition 3.4.1 (Points of type $(j, \tau)$).** Let $a \ge 1$, $j_1, \dots, j_a \ge 1$ and $\tau \in H_a$. A point $x \in G_{\mathbb{A}}$ has *type $(j, \tau)$* if there is a chain $0 = S_0 \subsetneq S_1 \subsetneq \dots \subsetneq S_a$ with these properties:

1. $S_a = \Lambda_x^{<1/2}$;
2. $S_i = \Lambda_x^{\le \tau_i}$ and the size of $S_i / S_{i-1}$ at $x$ is $\tau_i$, for each $i$;
3. every step $\Lambda_x^{\le t}$ with $t < 1/2$ is one of the $S_i$;
4. the rank of $S_i$ is the rank of $S_{i-1}$ plus $j_i$.

For $B \subseteq H_a$ let $T_j(B)$ be the set of $x$ of type $(j, \tau)$ for some $\tau \in B$.

So the chain is the part of the canonical filtration below $1/2$, and $(j, \tau)$ records its rank jumps and its sizes.

**Definition 3.4.2 (Gauge volume).** Let $c_v$ be gauge constants for the groups $G_v$. The *gauge volume* is
$$\operatorname{vol}_c(G) = \frac{\prod_v c_v \cdot \operatorname{covol}_\Gamma(\mu_{\mathbb{A}}, G_{\mathbb{A}})}{\mu_f(K_f)}.$$

It does not depend on the choice of $\mu_f$, since $\mu_f$ appears once above and once below.

**Definition 3.4.3 (General linear volume).** For $j \ge 1$ let
$$\operatorname{vol}_{GL}(E, j) = \sum_{[\Lambda]} \operatorname{vol}_{\mathrm{sl}}(\Lambda),$$
where $[\Lambda]$ runs over the classes of $\mathcal{O}_E$-lattices in $E^j$ under $GL_j(E)$ and $\operatorname{vol}_{\mathrm{sl}}$ is the slab volume of the second section.

### The unfolding bound

**Theorem 3.4.4 (Unfolding bound).** Let $p, q \ge 0$, $a \ge 1$ and $j_1, \dots, j_a \ge 1$ with $s = \sum_i j_i \le \min(p, q)$. Suppose that $G$ has signature $(p,q)$ at every infinite place, and let $G_0$ be a unitary group over the same CM field, with a star compatible isomorphism of fields, of signature $(p - s, q - s)$ at every infinite place. Let $c$ and $c_0$ be gauge constants for $G$ and $G_0$, let $\mu_f$ and $\mu_{0}$ be Haar measures, and let $B \subseteq H_a$ be measurable. Then
$$
\begin{aligned}
& \frac{\prod_v c_v \cdot \operatorname{covol}_\Gamma(\mu_{\mathbb{A}}, T_j(B))}{\mu_f(K_f)} \\
& \le c_{\mathrm{Iw}}(p,q,j)^f (2 v_E)^{f d_N/2} \prod_i 2^{f j_i^2} \operatorname{vol}_{GL}(E, j_i) \\
& \quad \cdot \operatorname{vol}_{c_0}(G_0) \cdot \int_B \rho_j(\tau)\, d\tau.
\end{aligned}
$$

Lean: `GlobalTheory.FlagUnfold.unfoldBound` (also `GlobalTheory.T.isotropicFlag_unfolding_bound`, a second name).

*Proof.* The group $\Gamma$ is countable and $K_f$ is open and compact. The proof has five steps.

1. Every $x \in T_j(B)$ is $\Gamma$-equivalent to a point $(g, x_f)$ whose chain $S$ is a saturated isotropic flag of type $j$ in $\Lambda_{x_f}$.
2. Every such flag has an adapted model with group $G_0$: there are lattices $\Lambda_i \subseteq E^{j_i}$, matrices $T_i$, $T'_i$, $T_0$ and a point $x_0$ of $G_{0,f}$ as in the second section. If two points have adapted models with the same classes of $\Lambda_i$ under $GL_{j_i}(E)$ and the same double coset of $x_0$ in $\Gamma_0 \backslash G_{0,f} / K_{0,f}$, then their flags are conjugate under $\Gamma$.
3. Index the classes by pairs: a tuple of classes $([\Lambda_i])_i$ and a double coset of $G_0$. Keep only the pairs that have an adapted model. The covolume of $T_j(B)$ is at most the sum over the pairs of the covolumes of the slices $\{ g : \sigma(g) \in B \}$ for the stabiliser $\Gamma_S$ of the flag of the pair.
4. Bound each slice by the measure of one flag class of the third section. The constant $c_{\mathrm{Iw}}(p,q,j)^f (2v_E)^{f d_N/2} \int_B \rho_j$ is the same for all pairs and comes out of the sum.
5. The sum over tuples of classes of $\prod_i 2^{f j_i^2} \operatorname{vol}_{\mathrm{sl}}(\Lambda_i)$ is at most $\prod_i 2^{f j_i^2} \operatorname{vol}_{GL}(E, j_i)$. The sum over double cosets of $\prod_v c_{0,v} \operatorname{covol}(\Gamma_{0,x_0})$, divided by $\mu_0(K_{0,f})$, is at most $\operatorname{vol}_{c_0}(G_0)$. $\square$

### Two volume inputs

The flag measure bound needs two volume identities.

**Definition 3.4.5 (Volume ratio).** The *volume ratio* is the statement: for $G$ of signature $(p,q)$ at every infinite place and $p_0 \le p$, $q_0 \le q$ with $p_0 + q_0 \ge 2$, there is a unitary group $G_0$ over the same field of signature $(p_0, q_0)$, and for every such $G_0$ and all gauge constants
$$\operatorname{vol}_c(G) = \operatorname{vol}_{c_0}(G_0) \prod_{M = p_0 + q_0 + 1}^{p + q} r_E(M),$$
where $r_E(M) = (2v_E)^{f(M - 1/2)} L_E(M)$. Here
$$L_E(M) = \prod_{P} e_P(M)$$
over the maximal ideals $P$ of $\mathcal{O}_E$, with $e_P(M) = (1 - (-1)^M \mathrm{N}P^{-M/2})^{-1}$ if $\bar P = P$ and $e_P(M) = (1 - \mathrm{N}P^{-M})^{-1/2}$ otherwise.

The volume ratio follows from the volume step of the fifth section by induction on the rank. The other identity is the volume of the general linear group, proved elsewhere in this volume: for $E$ totally complex and $j \ge 1$,
$$\operatorname{vol}_{GL}(E, j) = \operatorname{res}_{s=1} \zeta_E(s) \cdot v_E^{f j^2} \prod_{l=2}^{j} \zeta_E(l).$$
Here $\zeta_E$ is the [Dedekind zeta function](/learn/l-functions/#zeta-functions-of-number-fields) of $E$.

### The flag measure bound

For $j$ with $s = \sum_i j_i$ define
$$
\begin{aligned}
\kappa(E,p,q,j) = {} & v_E^{-f d_N/2}\, 2^{-f(ns - s^2 + s/2)} \Big( \frac{\sigma(p)\sigma(q)}{\sigma(p-s)\sigma(q-s)\prod_i \sigma(j_i)} \Big)^f \\
& \cdot \frac{(\operatorname{res}_{s=1}\zeta_E)^a \prod_i \prod_{l=2}^{j_i} \zeta_E(l)}{\prod_{M = n - 2s + 1}^{n} L_E(M)},
\end{aligned}
$$
with $n = p + q$ and $\sigma$ as in the first section.

**Theorem 3.4.6 (Flag measure bound).** Assume the volume step. Let $G$ have signature $(p,q)$ at every infinite place with $2q + 2 \le n$, let $D$ be a fundamental domain for $\Gamma$ in $G_{\mathbb{A}}$, let $a \ge 1$ and $j_i \ge 1$ with $\sum_i j_i \le q$, and let $B \subseteq H_a$ be measurable. Then $T_j(B)$ is measurable, $0 < \mu_{\mathbb{A}}(D) < \infty$, and
$$\frac{\mu_{\mathbb{A}}(T_j(B) \cap D)}{\mu_{\mathbb{A}}(D)} \le \kappa(E,p,q,j) \int_B \rho_j(\tau)\, d\tau.$$

Lean: `GlobalTheory.FlagMeas.Bound.flagMeasureBound` (also `GlobalTheory.T.isotropicFlagProbabilityBound_of_volumeRatio`, a second name).

*Proof.* The proof has six steps.

1. The set $T_j(B)$ is measurable and stable under $\Gamma$.
2. The volume step gives $0 < \mu_{\mathbb{A}}(D) < \infty$, and by induction it gives the volume ratio.
3. Apply the volume ratio with $p_0 = p - s$ and $q_0 = q - s$. Here $p_0 + q_0 = n - 2s \ge 2$, since $s \le q$ and $2q + 2 \le n$. This gives a group $G_0$ of signature $(p - s, q - s)$ over the same field. Gauge constants exist for $G$ and for $G_0$.
4. Apply the unfolding bound. Since $T_j(B)$ is stable under $\Gamma$, its covolume is $\mu_{\mathbb{A}}(T_j(B) \cap D)$, and the covolume of $G_{\mathbb{A}}$ is $\mu_{\mathbb{A}}(D)$.
5. Divide by $\operatorname{vol}_c(G) = \operatorname{vol}_{c_0}(G_0) \prod_{M} r_E(M)$. The factor $\operatorname{vol}_{c_0}(G_0)$ cancels, and the left side becomes the ratio of the theorem.
6. Insert the volume of the general linear group. The remaining constant is
$$\frac{c_{\mathrm{Iw}}(p,q,j)^f (2v_E)^{f d_N/2} \prod_i 2^{f j_i^2} \operatorname{vol}_{GL}(E,j_i)}{\prod_{M = n-2s+1}^{n} r_E(M)}.$$
An identity of real numbers turns it into $\kappa(E,p,q,j)$: the powers of $2$ in $c_{\mathrm{Iw}}$ and $r_E$ collect into $2^{-f(ns - s^2 + s/2)}$, the powers of $v_E$ collect into $v_E^{-f d_N/2}$, and the factors $V$ in $c_{\mathrm{Iw}}$ give the quotient of the $\sigma$. $\square$

**Remark 3.4.7 (Formalization).** The set $H_a$ is `simplexH`, $T_j(B)$ is `typeSet`, the type is `HasType` (LayerProd.lean, line 68), the gauge volume is `gaugeVol`, $\operatorname{vol}_{GL}$ is `glVol`, $\kappa$ is `kapBd`, $\rho_j$ is `dens`, and $L_E(M)$ is `lValEta`. The steps of the filtration are `stepLt` and `stepLe`. The unfolding bound takes the hypothesis $1 \le a$ but does not use it (IsotropicFlagUnfoldingBound.lean, line 214). It does not assume the volume step. In the flag measure bound the volume step is used only for the positivity and finiteness of $\mu_{\mathbb{A}}(D)$ and for the volume ratio, through `unitary_adelic_quotient_volume_pos_lt_top` and `hermVolumeRatioSameKind_of_volumeRatioInduction`. The identity of step 6 is `prod_five_factors_hermitian_volume`, and the volume of the general linear group is `genLin_tamagawa_volume`. The proof of the unfolding bound uses `covol_prod_le_tsum_slices`, `exists_adapted_basis_change_models`, `flags_conjugate_of_same_adapted_models`, `tsum_pi_prod_le` and `sum_latGroup_le`, none of which is unfolded here. The group $G_0$ in the unfolding bound is any unitary group over the same field with the right signature.
