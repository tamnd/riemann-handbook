---
title: Mirabolic products and the functor Φ on ρ × τ
decls:
  - GlobalTheory.T.phi_gp_commutation_holds
  - GlobalTheory.CompanionTheory.LeibPhi.phiGP
  - GlobalTheory.CompanionTheory.LeibPhi.main_twisted
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Mirabolic products and the functor Φ on ρ × τ

The theory of Bernstein and Zelevinsky studies a smooth representation of $\mathrm{GL}_n$ over a $p$-adic field through its restriction to the mirabolic subgroup and two functors $\Phi$ and $\Psi$ on representations of mirabolic groups. Its main tool for products is a list of rules for $\Phi$ and $\Psi$ on the two kinds of mirabolic products $\rho \times \tau$ and $\tau \times \sigma$. This section sets up the objects and proves the simplest rule, $\Phi(\rho \times \tau) \cong \rho \times \Phi\tau$. The rule is one of the six facts behind the Leibniz rule for derivatives, [Theorem 7.5.2](/entry/leibniz-ord/), which the step [EveryCharacter](/step/every-character/) uses through the unitary dual of $\mathrm{GL}_n$. For background see [smooth representations of p-adic groups](/learn/representations/#smooth-representations-of-p-adic-groups) and [parabolic induction and the Jacquet module](/learn/representations/#parabolic-induction-and-the-jacquet-module).

### Mirabolic groups and the functors Φ and Ψ

Let $k$ be a nonarchimedean local field, with normalized absolute value $|\cdot|$. Write $G_n = \mathrm{GL}_n(k)$ and $\nu^s(g) = |\det g|^s$ for $s \in \mathbb{R}$. A representation $\pi$ of a topological group on a complex vector space $V$ is *smooth* if the stabilizer of every $v \in V$ is open. For a representation $\pi$ and a character $\chi$ we write $\pi\chi$ for the twist $g \mapsto \chi(g)\pi(g)$.

**Definition 1.5.1 (Mirabolic group).** For $n \geq 1$ the *mirabolic group* $P_n \subseteq G_n$ is the group of matrices whose last row is $(0, \dots, 0, 1)$. Its *unipotent part* $U_n$ is the group of matrices $1 + v e_n^{\mathsf{T}}$ with $v \in k^n$ and $v_n = 0$, that is, the identity plus a column $v$ in the last column. We embed $G_{n-1}$ into $P_n$ by $g \mapsto \mathrm{diag}(g, 1)$, and $P_{n-1}$ into $P_n$ through $G_{n-1}$.

So $P_n = G_{n-1} \ltimes U_n$ and $U_n \cong k^{n-1}$. For $g \in G_{n-1}$ we have $\mathrm{diag}(g,1)(1 + v e_n^{\mathsf{T}})\mathrm{diag}(g,1)^{-1} = 1 + (gv) e_n^{\mathsf{T}}$.

**Definition 1.5.2 (The functors).** Let $\psi : k \to \mathbb{C}^\times$ be a unitary character and $n \geq 2$. Put $\theta_\psi(1 + v e_n^{\mathsf{T}}) = \psi(v_{n-1})$, a character of $U_n$. For a representation $\tau$ of $P_n$ on $W$ and a character $\theta$ of $U_n$, let
$$W_{U_n, \theta} = W / \operatorname{span}\{\tau(u)w - \theta(u)w : u \in U_n,\ w \in W\}.$$
Then $\Phi^-(\tau)$ is the representation of $P_{n-1}$ on $W_{U_n, \theta_\psi}$ by $p \mapsto \tau(\mathrm{diag}(p,1))$, and $\Psi^-(\tau)$ is the representation of $G_{n-1}$ on $W_{U_n, 1}$ by $g \mapsto \tau(\mathrm{diag}(g,1))$. The normalized functors are $\Phi\tau = \Phi^-(\tau)\nu^{-1/2}$ and $\Psi\tau = \Psi^-(\tau)\nu^{-1/2}$.

The actions are well defined. For $p \in P_{n-1}$ the last row of $p$ is $e_{n-1}^{\mathsf{T}}$, so $(pv)_{n-1} = v_{n-1}$ and conjugation by $\mathrm{diag}(p,1)$ fixes $\theta_\psi$. This is why $\Phi^-$ lands in representations of $P_{n-1}$ and not of $G_{n-1}$. For $\Psi^-$ the character is trivial, and all of $G_{n-1}$ acts.

**Definition 1.5.3 (Compact induction).** Let $H$ be a subgroup of a topological group $G$ and $\sigma$ a representation of $H$ on $W$. Then $\operatorname{c-Ind}_H^G \sigma$ is the space of functions $f : G \to W$ such that $f(hg) = \sigma(h)f(g)$ for $h \in H$, the stabilizer of $f$ under right translation is open, and there is a compact $C \subseteq G$ with $f = 0$ outside $HC$. The group $G$ acts by right translation, $(g \cdot f)(x) = f(xg)$.

No modulus character enters this definition. The normalizations are put into the products by hand.

**Definition 1.5.4 (The product ρ × τ).** Let $m \geq 0$ and $l \geq 1$. Let $Q_{m,l} \subseteq P_{m+l}$ be the group of elements that are block upper triangular with diagonal blocks of sizes $m$ and $l$. The lower block of such an element lies in $P_l$, and we get a projection $Q_{m,l} \to G_m \times P_l$. For a representation $\rho$ of $G_m$ and $\tau$ of $P_l$, put
$$\rho \mathbin{\times_0} \tau = \operatorname{c-Ind}_{Q_{m,l}}^{P_{m+l}} (\rho \otimes \tau), \qquad \rho \times \tau = \rho\nu^{l/2} \mathbin{\times_0} \tau\nu^{-m/2},$$
where $\rho \otimes \tau$ is pulled back along the projection. Both are representations of $P_{m+l}$.

The twists $\nu^{l/2}$ and $\nu^{-m/2}$ are the half powers of the determinants of the two blocks that occur in the normalized product of Bernstein and Zelevinsky (Ann. Sci. ENS (4) 10 (1977), Section 4). We write $\cong$ for an isomorphism of representations.

**Theorem 1.5.5 (Bernstein and Zelevinsky).** Let $\psi$ be a nontrivial character of $k$, $\rho$ a smooth representation of $G_m$ and $\tau$ a smooth representation of $P_l$, $l \geq 2$. Then $\Phi(\rho \times \tau) \cong \rho \times \Phi\tau$ and $\Psi(\rho \times \tau) \cong \rho \times \Psi\tau$.

This is part of the computation of $\Phi$ and $\Psi$ on products in Bernstein and Zelevinsky (Ann. Sci. ENS (4) 10 (1977), Section 4). We prove the rule for $\Phi$ below. The rule for $\Psi$ is a separate input to the Leibniz rule and is not proved in this section.

### Coinvariants of a compactly induced representation

The rule comes from a general fact. If a subgroup $G'$ meets the double cosets of $G$ well, then the twisted coinvariants of a compactly induced representation of $G$ are again compactly induced, now to $G'$.

We take the following three facts as given; they are proved elsewhere in the development. Let $\iota : G' \to G$ be a continuous homomorphism of topological groups, $H \leq G$ and $H' = \iota^{-1}(H)$. Let $\sigma$ be a smooth representation of $H$ on $W$, $\sigma'$ a representation of $H'$ on $W'$, and $q : W \to W'$ linear with $q(\sigma(\iota h)w) = \sigma'(h)q(w)$ for $h \in H'$. For $f \in \operatorname{c-Ind}_H^G \sigma$ put $(Tf)(x) = q(f(\iota x))$. Consider the conditions:

- (b) the set $H\iota(G')$ is closed in $G$;
- (c) for every neighbourhood $K'$ of $1$ in $G'$ there is a neighbourhood $K$ of $1$ in $G$ such that $\iota(x) = h\kappa$ with $h \in H$, $\kappa \in K$ implies $x = h'\kappa'$ with $h' \in H'$, $\kappa' \in K'$;
- (d) every neighbourhood of $1$ in $G$ contains a compact open subgroup;
- (e) $G'$ has a compact neighbourhood of $1$.

**Theorem 1.5.6 (Three facts on compact induction).** (i) Under (b), (c) and (e), $Tf$ lies in $\operatorname{c-Ind}_{H'}^{G'}\sigma'$ for every $f$. (ii) Let $U \leq H$ be normal in $G$ and $\theta$ a character of $U$ with $\theta(\iota(x)u\iota(x)^{-1}) = \theta(u)$ for $x \in G'$, and assume that $\ker q$ is spanned by the $\sigma(u)w - \theta(u)w$. Assume (d), and that every $g \in G$ lies in $H\iota(G')$ or has some $u \in U$ with $gug^{-1} \in H$, $\sigma(gug^{-1}) = 1$ and $\theta(u) \neq 1$. If $q(f(\iota x)) = 0$ for all $x \in G'$, then $f$ lies in the span of the $u \cdot f' - \theta(u) f'$ with $u \in U$ and $f' \in \operatorname{c-Ind}_H^G\sigma$. (iii) If $q$ is surjective and (c), (d) hold, then every element of $\operatorname{c-Ind}_{H'}^{G'}\sigma'$ is $Tf$ for some $f$.

**Theorem 1.5.7 (Coinvariants of a compact induction).** Let $\iota$, $H$, $H'$, $U$, $\theta$, $\sigma$, $\sigma'$ and $q$ be as in (ii), with $q$ surjective. Assume (b) to (e) and the double coset condition of (ii). Let $G'$ act on $(\operatorname{c-Ind}_H^G\sigma)_{U,\theta}$ through $\iota$. Then
$$(\operatorname{c-Ind}_H^G \sigma)_{U,\theta} \cong \operatorname{c-Ind}_{H'}^{G'} \sigma'$$
as representations of $G'$.

*Proof.* By fact (i), $T$ maps $\operatorname{c-Ind}_H^G\sigma$ to $\operatorname{c-Ind}_{H'}^{G'}\sigma'$. We show that $T$ kills each generator $u \cdot f - \theta(u)f$ of the kernel of the coinvariants. Let $x \in G'$ and $u' = \iota(x)u\iota(x)^{-1}$. Then $u' \in U \subseteq H$ and $\theta(u') = \theta(u)$. Since $f(u'\iota(x)) = \sigma(u')f(\iota(x))$,
$$(u \cdot f - \theta(u)f)(\iota x) = f(u'\iota(x)) - \theta(u)f(\iota x) = \sigma(u')w - \theta(u')w, \quad w = f(\iota x),$$
and $q$ kills this element by the assumption on $\ker q$. So $T$ factors through a map $\bar T$ on the coinvariants. By fact (ii), $\bar T$ is injective, and by fact (iii) it is surjective. It intertwines the actions: $(T(\iota(y) \cdot f))(x) = q(f(\iota(x)\iota(y))) = (Tf)(xy)$. $\square$

### The rule for the unnormalized functor

**Theorem 1.5.8 (Double coset dichotomy).** Let $\psi \neq 1$, $m \geq 0$ and $l \geq 1$. Let $\iota : P_{m+l} \to P_{m+l+1}$ be the embedding $p \mapsto \mathrm{diag}(p,1)$. For every $g \in P_{m+l+1}$, either $g \in Q_{m,l+1}\,\iota(P_{m+l})$, or there is $u \in U_{m+l+1}$ with $gug^{-1} \in Q_{m,l+1}$, with trivial image in $G_m \times P_{l+1}$, and with $\theta_\psi(u) \neq 1$.

We take this as given; it is proved elsewhere in the development. We also take as given that $\iota^{-1}(Q_{m,l+1}) = Q_{m,l}$, that $Q_{m,l+1}\iota(P_{m+l})$ is closed, that condition (c) holds for $\iota$ and $Q_{m,l+1}$, that the projections $Q_{m,l} \to G_m \times P_l$ are continuous and compatible with $\iota$, and that $U_{m+l+1} \subseteq Q_{m,l+1}$ projects onto $\{1\} \times U_{l+1}$ with $\theta_\psi$ carried to $\theta_\psi$.

**Lemma 1.5.9 (Φ⁻ of an unnormalized product).** Let $\psi \neq 1$. Let $\rho$ be a smooth representation of $G_m$ on $V$ and $\tau$ a smooth representation of $P_{l+1}$ on $W$, $l \geq 1$. Then $\Phi^-(\rho \mathbin{\times_0} \tau) \cong \rho \mathbin{\times_0} \Phi^-(\tau)$ as representations of $P_{m+l}$.

*Proof.* Apply the theorem on coinvariants with $G = P_{m+l+1}$, $G' = P_{m+l}$, $\iota$ as above, $H = Q_{m,l+1}$, $H' = Q_{m,l}$, $U = U_{m+l+1}$ and $\theta = \theta_\psi$. Let $\sigma$ be $\rho \otimes \tau$ on $V \otimes W$ and $\sigma'$ be $\rho \otimes \Phi^-(\tau)$ on $V \otimes W_{U_{l+1},\theta_\psi}$, both pulled back along the projections. Let $q = 1 \otimes \mathrm{pr}$, with $\mathrm{pr} : W \to W_{U_{l+1},\theta_\psi}$ the quotient map. The representation $\sigma$ is smooth because $\rho$ and $\tau$ are smooth and the projection is continuous. The map $q$ is surjective and intertwines, since $\Phi^-(\tau)$ is defined through the same embedding $p \mapsto \mathrm{diag}(p,1)$. Since $V \otimes -$ is exact, $\ker q = V \otimes \ker \mathrm{pr}$. As $U_{m+l+1}$ projects onto $\{1\} \times U_{l+1}$ compatibly with $\theta_\psi$, this kernel is spanned by the $\sigma(u)x - \theta_\psi(u)x$ with $u \in U_{m+l+1}$. Conditions (b) and (c) and the double coset condition are the facts stated above, and the dichotomy is where $\psi \neq 1$ is used. Condition (d), and (e) for $P_{m+l}$, come from the fact, also taken as given, that the compact open subgroups of a mirabolic group form a basis of neighbourhoods of $1$. The conclusion is the claim, because the left side of the theorem is $\Phi^-(\rho \mathbin{\times_0} \tau)$ by definition. $\square$

### Twists and the normalized rule

**Lemma 1.5.10 (Twisting a product).** Let $\rho$ be a representation of $G_m$, $\tau$ a representation of $P_l$ and $r \in \mathbb{R}$. Then $(\rho \mathbin{\times_0} \tau)\nu^r \cong \rho\nu^r \mathbin{\times_0} \tau\nu^r$.

*Proof.* We take as given that for a character $\chi$ of $G$ with open kernel, $(\operatorname{c-Ind}_H^G\sigma)\chi \cong \operatorname{c-Ind}_H^G(\sigma \cdot \chi|_H)$. The kernel of $\nu^r$ on $P_{m+l}$ is open. An element of $Q_{m,l}$ with diagonal blocks $g_1 \in G_m$ and $g_2 \in P_l$ has determinant $\det g_1 \det g_2$, so $\nu^r$ restricts on $Q_{m,l}$ to $\nu^r(g_1)\nu^r(g_2)$, and $(\rho \otimes \tau)\nu^r = \rho\nu^r \otimes \tau\nu^r$ on $Q_{m,l}$. $\square$

We also take as given that $\Phi^-$ commutes with twists: for a representation $\tau$ of $P_{l+1}$ and $t \in \mathbb{R}$, $\Phi^-(\tau\nu^t) \cong \Phi^-(\tau)\nu^t$. On $P_l$ the character $\nu^t$ is the restriction of $\nu^t$ on $P_{l+1}$, since $\det \mathrm{diag}(p,1) = \det p$.

**Theorem 1.5.11 (Twisted form of the rule).** Let $\psi \neq 1$. Let $\rho$ be a smooth representation of $G_m$ and $\tau$ a smooth representation of $P_{l+1}$, $l \geq 1$. Let $s_0, s_1, t, r \in \mathbb{R}$ with $r + s_0 = s_1$. Then
$$\Phi^-\bigl(\rho\nu^{s_0} \mathbin{\times_0} \tau\nu^{t}\bigr)\nu^{r} \cong \rho\nu^{s_1} \mathbin{\times_0} \bigl(\Phi^-(\tau)\nu^r\bigr)\nu^{t}.$$

Lean: `GlobalTheory.CompanionTheory.LeibPhi.main_twisted`.

*Proof.* The twists $\rho\nu^{s_0}$ and $\tau\nu^t$ are smooth, since $\nu$ has open kernel. By the Lemma on $\Phi^-$ of an unnormalized product, the left side is isomorphic to $(\rho\nu^{s_0} \mathbin{\times_0} \Phi^-(\tau\nu^t))\nu^r$. By the Lemma on twisting a product, this is $\rho\nu^{s_0+r} \mathbin{\times_0} \Phi^-(\tau\nu^t)\nu^r$, and $s_0 + r = s_1$. Finally $\Phi^-(\tau\nu^t)\nu^r \cong \Phi^-(\tau)\nu^t\nu^r = (\Phi^-(\tau)\nu^r)\nu^t$, and compact induction respects isomorphisms of the inducing representation. $\square$

**Theorem 1.5.12 (Φ on ρ × τ).** Let $\psi$ be a continuous unitary character of $k$ with $\psi \neq 1$. Let $\rho$ be a smooth representation of $G_m$ and $\tau$ a smooth representation of $P_{j+2}$. Then
$$\Phi(\rho \times \tau) \cong \rho \times \Phi\tau$$
as representations of $P_{m+j+1}$.

Lean: `GlobalTheory.CompanionTheory.LeibPhi.phiGP` (also `GlobalTheory.T.phi_gp_commutation_holds`, the same statement).

*Proof.* By definition, $\Phi(\rho \times \tau) = \Phi^-(\rho\nu^{(j+2)/2} \mathbin{\times_0} \tau\nu^{-m/2})\nu^{-1/2}$, and
$$\rho \times \Phi\tau = \rho\nu^{(j+1)/2} \mathbin{\times_0} \bigl(\Phi^-(\tau)\nu^{-1/2}\bigr)\nu^{-m/2},$$
because $\Phi\tau$ is a representation of $P_{j+1}$. This is the twisted form of the rule with $s_0 = (j+2)/2$, $s_1 = (j+1)/2$, $t = -m/2$ and $r = -1/2$. $\square$

**Remark 1.5.13 (Formalization).** The theorem on coinvariants is `coinv_cInd` in [PhiGpCommutationHolds.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/PhiGpCommutationHolds.lean#L33), the lemma for $\Phi^-$ is `phiMinus_prodGP` (L120), and the lemma on twists is `twist_prodGP` (L279). The three facts on compact induction are the inputs `quotient_map_intertwines_restriction`, `jacquet_kernel_span_twisted_character` and `quotient_map_induced_surjective_intertwiner`. The dichotomy is `mirabolic_double_coset_dichotomy`; the other facts on $Q_{m,l}$ are `mem_parabolic_iff_mem_embedded`, `isClosed_parabolic_mul_embedded_mirabolic`, `embedded_small_neighbourhood_factor`, `continuous_parabolic_proj`, `parabolic_proj_embedding_compat`, `parabolic_proj_unipotent_character_compat`, `exists_unipotent_lift_parabolic_proj` and `mirabolic_unipotent_normal`, and compact open subgroups come from `BZMirOnto.exists_compactOpen`; the twist facts are `compactInduction_twist_equiv`, `modulus_parabolic_proj_factor` and `derivative_functor_twist_equiv`. We opened the statements of these inputs, not their proofs. The group $P_n$ of the text is `Mir k (n-1)`, a subgroup of $\mathrm{GL}_n$, so the indices in Lean are one less than here. The character $\nu^s$ is `dpow`, built from the normalized absolute value `nabs`, which we did not unfold. The statement asks $\psi$ to be continuous, but `phiGP` (L319) never uses this hypothesis. The wrapper `phi_gp_commutation_holds` is proved by `first | exact @…` under `maxHeartbeats 1000000`.
