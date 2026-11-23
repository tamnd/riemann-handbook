---
title: Peeling the twist places
decls:
  - GlobalTheory.T.chainTwistPlacesIntegralPeel_of_doubling
  - GlobalTheory.ChainTw.Peel.qPeel_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Peeling the twist places

The [Rallis inner product formula](/learn/theta/#the-rallis-inner-product-formula), in the form that the chain uses, integrates the doubling integrand over the set of elements that are integral at the good places. The step scalars of the chain are computed from an integral over the level set: the elements whose finite part lies in the level group. This section compares the two integrals. They differ by one local factor at each twist place, and these factors are those of [the last section](/entry/local-factor/). The result is used in [the proof of the step scalars](/entry/scalars-of-given-all/), where it turns the Rallis formula into an exact formula for the inner product of two lifts at each step.

We keep the setting and the notation of [the last section](/entry/local-factor/): a step from the stage $V_k$ to the stage $V_{k+1}$ of a twisted theta chain, the twist places $Q$, the doubling integrand $\mathcal{I}_z$ built from $F_1$ and $F_2$, and the numbers $\ell_{\mathfrak{P}}$ for $\mathfrak{P} \in Q$. Let $G = U(V_k)(\mathbb{A})$ with its Haar measure.

**Definition 2.4.1 (The two domains).** Let $S$ be the finite set of bad places of the stage. Let $\mathrm{Off} \subseteq G$ be the set of $g$ whose component $g_v$ stabilises the local lattice for every finite place $v \notin S$. Let $\mathrm{Lev} \subseteq G$ be the set of $g$ whose finite part lies in the level group of the stage.

At a good place the level group is the stabiliser of the lattice, so $\mathrm{Lev} \subseteq \mathrm{Off}$. The two sets differ at the places of $S$. At the places of $P'$ the integrand vanishes off the level group, so these places do not matter. At the twist places the level group is the parahoric $J$, and the integrand does not vanish off $J$: this gives the factors $\ell_{\mathfrak{P}}$.

**Theorem 2.4.2 (Peeling the twist places).** Assume the unramified doubling identity and the rapid decay of cusp forms, and assume the node gap condition. Let $k < m$, take a step from $V_k$ to $V_{k+1}$, a measure of covolume one, a majorant $a$, a polynomial $\varphi$, forms $u_1, u_2$ of the stage with $K$-finite vectors, and let $F_1, F_2$ be their automorphic functions. Assume that $F_1$ has the twisted type of the chain. Let $z > t/2 - 1$, and assume that $\mathcal{I}_z$ is integrable on $\mathrm{Lev}$. Then $\mathcal{I}_z$ is integrable on $\mathrm{Off}$, and if $z = t/2$,
$$\int_{\mathrm{Off}} \mathcal{I}_z(g)\, dg = \prod_{\mathfrak{P} \in Q} \ell_{\mathfrak{P}} \cdot \int_{\mathrm{Lev}} \mathcal{I}_z(g)\, dg.$$

Lean: `GlobalTheory.ChainTw.Peel.qPeel_holds` (also `GlobalTheory.T.chainTwistPlacesIntegralPeel_of_doubling`, a second name).

*Proof.* For $\mathfrak{P} \in Q$ over $v$, [the theorem on the local factor](/entry/local-factor/) gives an open subgroup $J_v$ of $G_v$, a Haar measure $\mu_v$ with $\mu_v(J_v) = 1$, and an integrable $\zeta_v$ with $\zeta_v = 1$ on $J_v$. The component at $v$ lies in the level group if and only if the projection to $G_v$ lies in $J_v$. Right translation at $v$ multiplies the integrand by $\zeta_v$, and $\int \zeta_v\, d\mu_v = \ell_{\mathfrak{P}}$ when $z = t/2$. The places of $Q$ lie over distinct places of $F$, so the local groups $G_v$ for $\mathfrak{P} \in Q$ are distinct factors of $G$.

For $T \subseteq Q$ let $E_T$ be the set of $g \in \mathrm{Off}$ whose component at the place of each $\mathfrak{P} \in T$ lies in $J_v$. So $E_\emptyset = \mathrm{Off}$. We prove by induction on $T$:
$$\int_{E_{Q \setminus T}} \mathcal{I}_z = \prod_{\mathfrak{P} \in T} \ell_{\mathfrak{P}} \int_{E_Q} \mathcal{I}_z,$$
together with the integrability of $\mathcal{I}_z$ on $E_{Q \setminus T}$. For $T = \emptyset$ there is nothing to prove. For the induction step, add one place $\mathfrak{P}$ over $v$ to $T$. Write $g = x \cdot \mathrm{emb}(y)$ with $x_v = 1$ and $y \in G_v$. The set $E_{Q \setminus (T \cup \{\mathfrak{P}\})}$ is the product of the part of $E_{Q \setminus T}$ away from $v$ with all of $G_v$, and $E_{Q \setminus T}$ is the same product with $J_v$ in place of $G_v$. By Fubini's theorem for this product, and since $\mathcal{I}_z(x\, \mathrm{emb}(y)) = \zeta_v(y)\, \mathcal{I}_z(x)$,
$$\int_{E_{Q \setminus (T \cup \{\mathfrak{P}\})}} \mathcal{I}_z = \int_{G_v} \zeta_v\, d\mu_v \cdot \int_{E_{Q \setminus T}} \mathcal{I}_z = \ell_{\mathfrak{P}} \int_{E_{Q \setminus T}} \mathcal{I}_z,$$
where the second integral on the right uses $\mu_v(J_v) = 1$ and $\zeta_v = 1$ on $J_v$. The same product gives integrability, since $\zeta_v$ is integrable. With $T = Q$ we get $\int_{\mathrm{Off}} \mathcal{I}_z = \prod_{\mathfrak{P} \in Q} \ell_{\mathfrak{P}} \int_{E_Q} \mathcal{I}_z$.

It remains to compare $E_Q$ with $\mathrm{Lev}$. The finite level group is the product of the local level groups. So $\mathrm{Lev} \subseteq E_Q$, and an element of $E_Q \setminus \mathrm{Lev}$ has its component outside the level group at some place of $P'$. There the coefficient of the Weil representation vanishes, since this coefficient is supported in the principal level group at the places of $P'$. So $\mathcal{I}_z = 0$ on $E_Q \setminus \mathrm{Lev}$, and $\int_{E_Q} \mathcal{I}_z = \int_{\mathrm{Lev}} \mathcal{I}_z$. The same argument moves integrability from $\mathrm{Lev}$ to $E_Q$. This proves the theorem. $\square$

The induction is the reason for the order of quantifiers in the last section: the function $\zeta_v$ is the same for every $x$ with $x_v = 1$, so the integral over $G_v$ splits off as a constant.

**Remark 2.4.3 (Formalization).** The theorem is at [ChainTwistPlacesIntegralPeelOfDoubling.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ChainTwistPlacesIntegralPeelOfDoubling.lean#L27), and the property it proves is defined in [IsLevMeas.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/IsLevMeas.lean#L159). The equality is claimed only at $z = t/2$; for other $z$ the theorem gives integrability only. This is enough for the Rallis formula, which is used at $z = t/2$. The Fubini step, the product description of the level group and the support of the Weil coefficient at the places of $P'$ are the statements of three lemmas whose proofs we have not opened.
