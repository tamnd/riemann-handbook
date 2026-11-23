---
title: The image of an idempotent
decls:
  - GlobalTheory.MumAdj.exists_linHom
  - GlobalTheory.MumAdj.adj_groups
  - GlobalTheory.T.uniformisedGroups_adjointHomPair_closedForm
  - GlobalTheory.MumIsoAdj.iso_of_factor_adj
  - GlobalTheory.T.idempotent_image_iso_uniformised_factor_with_adjoint_pair
  - GlobalTheory.MumDesc.image_unif
  - GlobalTheory.T.idempotent_image_uniformised_by_factor_data
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The image of an idempotent

The charts of the compactification are first built for a product of copies of the universal family, where Mumford's construction is explicit, and are then cut down by an idempotent of a ring acting on the product. This section proves that cutting down is compatible with uniformizations. If a semi-abelian group $G'$ is uniformized by degeneration data $D'$ and a ring $O$ acts on everything, and if $G$ is the image of an idempotent $e \in O$ whose degeneration data $D$ form a factor of $D'$, then $G$ is uniformized by $D$, and its bundle is the restriction of the bundle of $G'$ twisted by an element $f \in O$. The tool is a theorem that lifts adjoint pairs of maps of Mumford data to adjoint pairs of maps of the uniformized groups. The result is used in the [construction of charts](/entry/exists-chart-at/).

Throughout, $R$ is a local domain that is an admissible base of characteristic $0$, degeneration data are taken with respect to $\mathfrak{m}_R$, and $K = K_R$. A *uniformization* $U$ of a semi-abelian group $G$ over $R$ by degeneration data $D$ and a polarized abelian scheme $A$ over $K$ consists of an isomorphism of the generic fibre of $G$ with $A$, a rigidified cubical symmetric line bundle $L_U$ on $G$ that extends the bundle of $A$, and for each $e \ge 0$ an exact sequence
$$0 \to T_Y \xrightarrow{\;i_e\;} G \times_R R/\mathfrak{m}^{e+1} \xrightarrow{\;q_e\;} B_D \times_R R/\mathfrak{m}^{e+1} \to 0,$$
where $T_Y$ is the split torus with character group the lattice $Y$ of $D$, all compatible in $e$ and with the bundles, and with the expansion property of Mumford's construction ([semi-abelian degenerations](/learn/abelian-varieties/#semi-abelian-degenerations-and-mumfords-construction)).

**Definition 9.6.1 (Linear homomorphism).** Let $U_1, U_2$ be uniformizations of $G_1, G_2$ by $D_1, D_2$. Let $a : B_{D_1} \to B_{D_2}$ be a map and $h' : Y_2 \to Y_1$ additive. A homomorphism $u : G_1 \to G_2$ is *linear* over $(a, h')$ if for each $e$ it satisfies $q_{2,e} \circ u = a \circ q_{1,e}$ and $u \circ i_{1,e} = i_{2,e} \circ t$, where $t : T_{Y_1} \to T_{Y_2}$ is the map of tori with $t^*\chi = h'(\chi)$ on characters.

Lean: `GlobalTheory.MumFam.LinHom`.

**Definition 9.6.2 (Adjoint pairs).** Let $u : G_1 \to G_2$ and $u' : G_2 \to G_1$ be homomorphisms, and $L_1, L_2$ line bundles on $G_1, G_2$. The pair $(u, u')$ is *adjoint* for $(L_1, L_2)$ if
$$(u \times 1)^* \Lambda(L_2) \cong (1 \times u')^* \Lambda(L_1)$$
on $G_1 \times G_2$. Let $Q_1, Q_2$ be Mumford data. An *adjoint pair* from $Q_1$ to $Q_2$ consists of homomorphisms $a : B_1 \to B_2$, $a' : B_2 \to B_1$ and additive maps $h : Y_1 \to Y_2$, $h' : Y_2 \to Y_1$ with $c_2(h(y)) = a(c_1(y))$ and $c_1(h'(z)) = a'(c_2(z))$, and a generating isomorphism $w : (a \times 1)^* \Lambda(M_2) \cong (1 \times a')^* \Lambda(M_1)$ such that $\tau_2(h(y), z) = w \cdot \tau_1(y, h'(z))$ for all $y \in Y_1$, $z \in Y_2$.

Lean: `GlobalTheory.MumFam.GAdj`, `GlobalTheory.MumFam.Adj`.

Degeneration data $D$ give Mumford data with the same abelian scheme, bundle, lattice and map $c$, and the periods of $D$; we use the same letter for both.

**Theorem 9.6.3 (Adjoint pairs lift to uniformized groups).** Let $U_1, U_2$ be uniformizations of semi-abelian groups $G_1, G_2$ over $R$ by $D_1, A_1$ and $D_2, A_2$. Let $(a, a', h, h')$ be an adjoint pair from $D_1$ to $D_2$. Then there are homomorphisms $u : G_1 \to G_2$, linear over $(a, h')$, and $u' : G_2 \to G_1$, linear over $(a', h)$, such that $(u, u')$ is adjoint for $(L_{U_1}, L_{U_2})$.

Lean: `GlobalTheory.MumAdj.exists_linHom` (also `GlobalTheory.MumAdj.adj_groups` and `GlobalTheory.T.uniformisedGroups_adjointHomPair_closedForm`, wrappers).

*Proof.* First let $G_1 = G_2 = G$ with one uniformization $U$ by $D$, and let $(a, a', h, h')$ be an adjoint pair of endomorphisms of $D$. The adjoint pair gives endomorphism data of $D$. A lemma on formal endomorphisms gives a compatible family of endomorphisms of the thickenings $G \times_R R/\mathfrak{m}^{e+1}$, linear over $(a, h')$, and a lemma on algebraization makes it the restriction of one homomorphism $g : G \to G$. So $g$ is linear over $(a, h')$.

In the general case, a lemma on products gives a uniformization $U$ of a semi-abelian group $G$ by data $D$, with inclusions $i_k : B_k \to B_D$, projections $p_k : B_D \to B_k$, inclusions $j_k$ and projections $q_k$ of lattices, and linear inclusions and projections of the groups, all adjoint in pairs; it is the product of $U_1$ and $U_2$. Compose the given pair with these: $(i_1, j_1)$ and $(p_2, q_2)$ give an adjoint pair of endomorphisms of $D$ whose entry from the first to the second factor is $(a, a', h, h')$. By the first case it lifts to an endomorphism $g$ of $G$, and its adjoint pair lifts to $g'$. A lemma on linear endomorphisms shows that $(g, g')$ is adjoint for $(L_U, L_U)$. Restrict: $u$ is $g$ composed with the inclusion of $G_1$ and the projection to $G_2$, and $u'$ is defined in the same way from $g'$. A composite of linear homomorphisms is linear, so $u$ is linear over the composite of $p_1 \circ i_1 = 1$, $a$ and $p_2 \circ i_2 = 1$, that is over $(a, h')$, and $u'$ is linear over $(a', h)$. A composite of adjoint pairs is adjoint, so $(u, u')$ is adjoint. $\square$

**Definition 9.6.4 (Ring action).** Let $O$ be a ring with an involution $*$. An *action* of $O$ on a commutative group scheme $G$ is a map $a \mapsto \mathrm{act}(a)$ to group endomorphisms that is additive, sends $1$ to the identity and $ab$ to $\mathrm{act}(a) \circ \mathrm{act}(b)$. An action on a polarized abelian scheme $(B, L)$ is *Rosati compatible* if $(\mathrm{act}(a), \mathrm{act}(a^*))$ is adjoint for $(L, L)$, locally on the base. An action on degeneration data $D$ is a Rosati compatible action on $B_D$ and an $O$-module structure on $Y$ with $c(a y) = \mathrm{act}(a)(c(y))$, such that $\tau$ is balanced: $\tau(a y, y') = \tau(y, a^* y')$ up to the adjunction. A uniformization $U$ of $G$ by $D$ and $A$ is *$O$-linear* for actions on $D$, $A$ and $G$ if the actions agree on the generic fibre, $q_e \circ \mathrm{act}(a) = \mathrm{act}(a) \circ q_e$, and $\mathrm{act}(a)$ acts on $T_Y$ through $a^*$ on characters.

Lean: `ReciprocityTheory.ChartRestriction.G.Out.RingAct` (also `ReciprocityTheory.ChartRestriction.G.Out.PolAV.OAct`, `ReciprocityTheory.ChartRestriction.G.Out.DegPre.OAct`, `ReciprocityTheory.ChartRestriction.G.Out.UnifPre.OLinear`).

So for an $O$-linear $U$ each $\mathrm{act}(a)$ on $G$ is linear over $(\mathrm{act}(a), a^*)$.

**Definition 9.6.5 (Factor).** Let $D, D'$ be degeneration data over $R$. A *factor* of $D'$ with model $D$ consists of a ring $O$ with involution, an action of $O$ on $D'$, elements $e, f \in O$ with $e^2 = e$, homomorphisms $\mathrm{inc} : B_D \to B_{D'}$ and $\mathrm{pr} : B_{D'} \to B_D$, and additive maps $\xi : Y \to Y'$ and $\xi_p : Y' \to Y$, such that:

1. $\mathrm{pr} \circ \mathrm{inc} = 1$, $\mathrm{inc} \circ \mathrm{pr} = \mathrm{act}(e)$, $\xi_p \circ \xi = 1$, $\xi \circ \xi_p = e$, and $c'(\xi(y)) = \mathrm{inc}(c(y))$;
2. the map $y \mapsto e^* f \xi(y)$ is injective, and each $e^* z$ with $z \in Y'$ is of this form;
3. there is a generating isomorphism $w : \Lambda(L_D) \cong (\mathrm{inc} \times \mathrm{act}(f)\,\mathrm{inc})^* \Lambda(L_{D'})$ with $\tau_D(a, b) = w \cdot \tau_{D'}(\xi(a), f\xi(b))$.

The factor is *algebraic* if $e^* e = b \cdot e^* f e$ for some integer $b > 0$, $e^* f e = e^* f^* e$, and $g \, e^* f e = e$ for some $g \in O$.

Lean: `GlobalTheory.Mum.Factor` (also `GlobalTheory.Mum.Factor.Alg`).

**Theorem 9.6.6 (Image of an idempotent, comparison).** Let $D, D'$ be degeneration data over $R$ and $F$ an algebraic factor of $D'$ with model $D$, ring $O$ and elements $e, f$. Let $U'$ be a uniformization of a semi-abelian group $G'$ by $D'$ and $A'$, with Rosati compatible actions of $O$ on $A'$ and on $G'$ for which $U'$ is $O$-linear. Let $G$ be a semi-abelian group with homomorphisms $\mathrm{inc} : G \to G'$ and $\mathrm{pr} : G' \to G$ such that $\mathrm{pr} \circ \mathrm{inc} = 1$ and $\mathrm{inc} \circ \mathrm{pr} = \mathrm{act}(e)$. Let $U_0$ be a uniformization of a semi-abelian group $G_0$ by $D$ and some $A_0$. Then there are an isomorphism of groups $\varepsilon : G \to G_0$ and homomorphisms $u : G' \to G_0$, $u' : G_0 \to G'$ such that $\varepsilon = u \circ \mathrm{inc}$, $u' \circ u = \mathrm{act}(e^* f e)$, and $(u, u')$ is adjoint for $(L_{U'}, L_{U_0})$.

Lean: `GlobalTheory.MumIsoAdj.iso_of_factor_adj` (also `GlobalTheory.T.idempotent_image_iso_uniformised_factor_with_adjoint_pair`, a wrapper).

*Proof.* Put $s = e^* f e$. Since $F$ is algebraic, $s^* = s$ and there is $g \in O$ with $g s = e$. A lemma on idempotent factors gives an adjoint pair from $D'$ to $D$, made of $\mathrm{pr}$, $\mathrm{act}(e^* f) \circ \mathrm{inc}$, $\xi_p$ and $e^* f \xi$. The theorem on adjoint pairs gives $u : G' \to G_0$ and $u' : G_0 \to G'$, linear over these maps, with $(u, u')$ adjoint.

We use the uniqueness of linear homomorphisms: an endomorphism of a uniformized semi-abelian group is determined by the maps over which it is linear. From $s^* = s$ and $g s = e$ we get $s g^* = e^*$ and $e g^* s = e$, using $e^2 = e$.

1. Both $u' \circ u$ and $\mathrm{act}(s)$ are linear over $\mathrm{act}(e^* f) \circ \mathrm{inc} \circ \mathrm{pr} = \mathrm{act}(s)$ on $B_{D'}$ and over multiplication by $s = s^*$ on $Y'$. So $u' \circ u = \mathrm{act}(s)$.
2. The endomorphism $u \circ \mathrm{act}(e g) \circ u'$ of $G_0$ is linear over $\mathrm{pr} \circ \mathrm{act}(e g s) \circ \mathrm{inc} = \mathrm{pr} \circ \mathrm{act}(e) \circ \mathrm{inc} = 1$ on $B_D$, and over the identity of $Y$: the lattice map is $y \mapsto \xi_p\big((g^* s)\,\xi(y)\big)$, and since $\xi \circ \xi_p = e$ and $e g^* s = e$, we get $\xi\big(\xi_p((g^* s)\,\xi(y))\big) = \xi(y)$, so the map is the identity. So it is the identity of $G_0$.

Let $\varepsilon = u \circ \mathrm{inc}$ and $\varepsilon' = \mathrm{pr} \circ \mathrm{act}(g) \circ u'$. Then
$$\varepsilon' \circ \varepsilon = \mathrm{pr} \circ \mathrm{act}(g s) \circ \mathrm{inc} = \mathrm{pr} \circ \mathrm{inc} \circ \mathrm{pr} \circ \mathrm{inc} = 1,$$
and $\varepsilon \circ \varepsilon' = u \circ \mathrm{act}(e)\,\mathrm{act}(g) \circ u' = 1$ by step 2. So $\varepsilon$ is an isomorphism of groups. $\square$

**Theorem 9.6.7 (Image of an idempotent is uniformized).** Let $D, D', F, U', G, \mathrm{inc}, \mathrm{pr}$ be as in the comparison theorem. Then there are a polarized abelian scheme $A$ over $K$ and a uniformization $U$ of $G$ by $D$ and $A$ such that
$$\Lambda(L_U) \cong (\mathrm{inc} \times \mathrm{act}(f)\,\mathrm{inc})^* \Lambda(L_{U'})$$
on $G \times_R G$.

Lean: `GlobalTheory.MumDesc.image_unif` (also `GlobalTheory.T.idempotent_image_uniformised_by_factor_data`, a wrapper).

*Proof.* A lemma on complete normal bases gives a semi-abelian group $G_0$ with a uniformization $U_0$ by $D$ and some $A_0$. The comparison theorem gives $\varepsilon : G \cong G_0$ and an adjoint pair $(u, u')$ with $\varepsilon = u \circ \mathrm{inc}$ and $u' \circ u = \mathrm{act}(e^* f e)$. A lemma on transport along group isomorphisms gives a uniformization $U$ of $G$ by $D$ and $A_0$ with $L_U \cong \varepsilon^* L_{U_0}$. Since $U'$ is $O$-linear, $(\mathrm{act}(e), \mathrm{act}(e^*))$ is adjoint for $(L_{U'}, L_{U'})$. Also $\mathrm{inc}$ is a homomorphism with $\mathrm{act}(e) \circ \mathrm{inc} = \mathrm{inc} \circ \mathrm{pr} \circ \mathrm{inc} = \mathrm{inc}$, and $u' \circ u = \mathrm{act}(e^*) \circ \mathrm{act}(f) \circ \mathrm{act}(e)$. A lemma on retracts of Mumford bundles, applied to $\mathrm{inc}$, $u$, $u'$, $\mathrm{act}(e)$, $\mathrm{act}(e^*)$ and $\mathrm{act}(f)$, gives the isomorphism of bundles. Take $A = A_0$. $\square$

**Remark 9.6.8 (Formalization).** The comparison theorem assumes that $G$ is semi-abelian, but its proof does not use this hypothesis, and it uses only the second and third clauses of algebraicity; the clause $e^* e = b \cdot e^* f e$ is discarded ([IdempotentImageIsoUniformisedFactorOfAdjointPair.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IdempotentImageIsoUniformisedFactorOfAdjointPair.lean#L32)). The uniqueness lemma for linear endomorphisms is proved twice, with the same name `linHom_unique` in two namespaces ([IdempotentImageIsoUniformisedFactorOfAdjointPair.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IdempotentImageIsoUniformisedFactorOfAdjointPair.lean#L22), [UniformisedGroupsAdjointHomPairClosedForm.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UniformisedGroupsAdjointHomPairClosedForm.lean#L31)). The theorem `adj_groups` restates `exists_linHom` with explicit arguments and is proved by it ([UniformisedGroupsAdjointHomPairClosedForm.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UniformisedGroupsAdjointHomPairClosedForm.lean#L78)). The lemmas on formal endomorphisms, algebraization of endomorphisms, products, idempotent factors, existence of uniformizations, transport and retracts have no entries in this chapter; we describe only what their call sites use. The predicate of an admissible base and the expansion property of a uniformization are not unfolded here, and the balance condition on periods is given only in words.
