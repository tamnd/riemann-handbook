---
title: The prismatic Dieudonné functor
decls:
  - GlobalTheory.PDivLat.hasDatum_of_conn_dual_conn
  - GlobalTheory.T.pDivisibleGroup_datum_of_connected_dual_connected
  - GlobalTheory.PDivLat.prismaticDieudonneHodgeAt_of_hasDatum
  - GlobalTheory.T.prismaticDieudonneHodge_of_hodgeTateDatum
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The prismatic Dieudonné functor

This section builds a contravariant functor $M$ from $p$-divisible groups over $O$ to free $A_{\inf}$-modules, with a Frobenius, a reduction modulo $\xi$ and a Hodge filtration on the reduction. It proves two results. The first reduces the existence of Hodge-Tate data to groups $G$ such that $G$ and $G^\vee$ are connected; for those groups, the last two sections give the data. The second builds the functor from the data. Together they prove the theorem on prismatic Dieudonné modules ([Theorem 2.11 of Volume 12](/entry/prismatic-dieudonne-hodge/)), which is a literature input of the proof ([step](/step/cm-abelian-inputs-from-literature/)).

We keep the notation of the last section. For a $p$-divisible group $G$ over $O$, let $T_p G$ be its Tate module, $G^\vee$ its dual, $\omega_G$ its module of invariant differentials and $\mathrm{Lie}(G) = \mathrm{Hom}_O(\omega_G, O)$. Let $\mathrm{HT} : T_p G \to \omega_{G^\vee}$ be the Hodge-Tate map and $\mathrm{dlog} : T_p G^\vee \to \omega_G$ the map of the last two sections. Let $\langle t, \chi \rangle \in \mathbb{Z}_p$ be the pairing of $t \in T_p G$ and $\chi \in T_p G^\vee$, read through the generator of $T_p \mu_{p^\infty}$ given by $\varepsilon$. We use the maps $\mathbb{Z}_p \to A_{\inf}$ and $\mathbb{Z}_p \to O$ without a name. Let $\mathbb{Q}_p/\mathbb{Z}_p$ be the dual of $\mu_{p^\infty}$.

**Definition 5.6.1 (Hodge-Tate datum).** Let $h \geq 0$. A *Hodge-Tate datum* of height $h$ for $\varepsilon$ consists of square matrices $F$, $G$, $\Psi$ and $\Psi'$ of size $h$ over $A_{\inf}$ such that
$$\begin{aligned}
G F &= \mu \cdot 1_h, & F &= \Psi\, \varphi^{-1}(F), & \Psi \Psi' &= \xi \cdot 1_h,
\end{aligned}$$
together with an action of $\mathbb{Z}_p$ by matrices that commutes with $F$. Put $\alpha = \theta(F)$ and $\beta = \theta(G)$ as maps of $O^h$, and let $\mathrm{Fil} = \ker \beta$. Let $\bar\beta : O^h / \mathrm{Fil} \to O^h$ be the map induced by $\beta$.

The action of $\mathbb{Z}_p$ carries no information here: a ring map from $\mathbb{Z}_p$ to a $p$-adically separated ring is the scalar map, so $F$ commutes with it. The matrices $F = 1$, $G = \mu \cdot 1$, $\Psi = 1$, $\Psi' = \xi \cdot 1$ give a datum for each $h$. For $h = 1$, the matrices $F = \mu$, $G = 1$, $\Psi = \xi$, $\Psi' = 1$ give a datum, since $\xi\, \varphi^{-1}(\mu) = \xi \nu = \mu$.

**Definition 5.6.2 (Datum of a $p$-divisible group).** Let $G$ be a $p$-divisible group over $O$ of height $h$. We say that $G$ *has a datum* if there are a Hodge-Tate datum of height $h$, an isomorphism $e : T_p G \to \mathbb{Z}_p^h$, and $O$-isomorphisms $\omega_{G^\vee} \to \mathrm{Fil}$ and $O^h / \mathrm{Fil} \to \mathrm{Lie}(G)$, such that:

1. $\alpha(e(t)) = \mathrm{HT}(t)$ in $\mathrm{Fil}$ for all $t \in T_p G$, with $e(t)$ read in $O^h$;
2. $\sum_i \bar\beta(y)_i\, \langle e^{-1}(\delta_i), \chi \rangle = x(\mathrm{dlog}\, \chi)$ for all $x \in \mathrm{Lie}(G)$ and $\chi \in T_p G^\vee$, where $y \in O^h / \mathrm{Fil}$ is the class that corresponds to $x$ and $\delta_i$ is the $i$-th unit vector.

So the datum is a matrix form of the Hodge-Tate sequence: $\alpha$ realizes $\mathrm{HT}$ on $\omega_{G^\vee}$, and $\bar\beta$ realizes $\mathrm{dlog}$ through the pairing. A $p$-divisible group is *constant* if each Hopf algebra $A_n$ is isomorphic to $O^{p^{nh}}$ as an $O$-algebra. A group $G$ is a *direct sum* of $G_1$ and $G_2$ if there are maps $i_k : G_k \to G$ and $q_k : G \to G_k$ with $q_k i_k = 1$, $q_2 i_1 = 0$, $q_1 i_2 = 0$ and $i_1 q_1 + i_2 q_2 = 1$.

**Theorem 5.6.3 (Reduction to biconnected groups).** Let $p$, $C$, $v$ and $O$ be as in the first section and let $\varepsilon \in O^\flat$ be a primitive system. Assume that every $p$-divisible group $G$ over $O$ such that $G$ and $G^\vee$ are connected has a datum. Then every $p$-divisible group over $O$ has a datum.

Lean: `GlobalTheory.PDivLat.hasDatum_of_conn_dual_conn` (also `GlobalTheory.T.pDivisibleGroup_datum_of_connected_dual_connected`, a wrapper).

*Proof.* The ring $O$ is a valuation ring. We use the following theorems, which are proved in other files of the formalization and which we take as given here.

- Every $G$ is a direct sum of a connected group and a constant group.
- A constant group has a datum.
- If $G_1$ and $G_2$ have data, then so does each direct sum of $G_1$ and $G_2$.
- If $G$ has a datum, then so does $G^\vee$.
- Having a datum is invariant under isomorphism.

First we show: a retract of a connected group is connected. Let $f : H \to G$ and $r : G \to H$ with $r f = 1$, and let $G$ be connected. The map of Hopf algebras $A_n(G) \to A_n(H)$ induced by $f$ is surjective, since the map induced by $r$ is a section of it. The ring $A_n(H)$ is not zero, since it has a counit to $O$ and $O$ is not zero. A nonzero quotient of a local ring is local. So $H$ is connected.

Now let $G$ be any group. Write $G$ as a direct sum of a connected $G_1$ and a constant $G_2$. Write $G_1^\vee$ as a direct sum of a connected $H_1$ and a constant $H_2$, with maps $i_1$ and $q_1$. Dualize: $q_1^\vee$ and $i_1^\vee$, composed with the isomorphism $G_1 \cong G_1^{\vee\vee}$, make $H_1^\vee$ a retract of $G_1$. So $H_1^\vee$ is connected. Since $H_1$ and $H_1^\vee$ are connected, $H_1$ has a datum by hypothesis. The constant group $H_2$ has a datum, so $G_1^\vee$ has a datum. So $G_1^{\vee\vee}$ has a datum, and so has $G_1$. The constant group $G_2$ has a datum, so $G$ has a datum. $\square$

Next we define the functor. Let $\varphi^n$ be the $n$-th power of the Frobenius of $A_{\inf}$.

**Definition 5.6.4 (Hodge-Tate lattice).** Let $G$ be a $p$-divisible group over $O$. Let $M(G)$ be the set of $\mathbb{Z}_p$-linear maps $y : T_p G \to A_{\inf}$ such that for each $n \geq 0$ there is $x \in \mathrm{Lie}(G^\vee)$ with
$$\theta(\varphi^n(y(t))) = x(\mathrm{HT}(t)) \quad \text{for all } t \in T_p G.$$
It is an $A_{\inf}$-submodule of $\mathrm{Hom}_{\mathbb{Z}_p}(T_p G, A_{\inf})$. For $f : G \to H$, the map $M(f) : M(H) \to M(G)$ is $y \mapsto y \circ T_p f$.

**Definition 5.6.5 (Prismatic Dieudonné-Hodge data).** Let $\varepsilon \in O^\flat$. *Prismatic Dieudonné-Hodge data* at $\varepsilon$ consist of a functor $M$ from the opposite category of $p$-divisible groups over $O$ to $A_{\inf}$-modules, a functor $D$ of the same kind to $O$-modules, and for each $G$ a $\varphi$-semilinear map $\varphi_G$ of $M(G)$, a $\theta$-semilinear map $r_G : M(G) \to D(G)$ and $O$-linear maps $\iota_G : \omega_G \to D(G)$ and $\pi_G : D(G) \to \mathrm{Lie}(G^\vee)$, such that:

1. $M$ is additive;
2. $M(G)$ is free of finite rank over $A_{\inf}$, and its rank is the height of $G$;
3. for each $m \in M(G)$ there is $n$ with $\varphi_G(n) = \varphi(\xi)\, m$, and $\varphi_G$ is natural in $G$;
4. $r_G$ is surjective, its kernel is $\xi M(G)$, and $r_G$ is natural in $G$;
5. $\iota_G$ is injective, $\pi_G$ is surjective, the image of $\iota_G$ is the kernel of $\pi_G$, and $\iota_G$ and $\pi_G$ are natural in $G$;
6. there is an isomorphism $M(\mathbb{Q}_p/\mathbb{Z}_p) \to A_{\inf}$ that takes $\varphi_G$ to $\varphi$;
7. there is an isomorphism $M(\mu_{p^\infty}) \to A_{\inf}$ that takes $\varphi_G$ to $\varphi(\xi)\, \varphi$;
8. each $A_{\inf}$-linear map $g : M(\mu_{p^\infty}) \to M(\mathbb{Q}_p/\mathbb{Z}_p)$ that commutes with the Frobenius maps is $M(f)$ for a unique $f : \mathbb{Q}_p/\mathbb{Z}_p \to \mu_{p^\infty}$.

In part 5, naturality of $\iota_G$ is with respect to the map of differentials of $f$, and naturality of $\pi_G$ is with respect to the map of Lie algebras of $f^\vee$.

**Theorem 5.6.6 (The prismatic Dieudonné functor).** Let $p$, $C$, $v$ and $O$ be as in the first section and let $\varepsilon \in O^\flat$ be a primitive system. Assume that every $p$-divisible group over $O$ has a datum. Then there are prismatic Dieudonné-Hodge data at $\varepsilon$.

Lean: `GlobalTheory.PDivLat.prismaticDieudonneHodgeAt_of_hasDatum` (also `GlobalTheory.T.prismaticDieudonneHodge_of_hodgeTateDatum`, a wrapper).

*Proof.* The functor is the Hodge-Tate lattice $M$. Since $\varepsilon$ is a primitive system, the component $\zeta_1$ is a primitive $p$-th root of unity. We take as given that then $A_{\inf}$ is a domain, $\theta$ is surjective, and $\ker \theta = \xi A_{\inf}$, and that $\mu \neq 0$. So $\theta(\xi) = 0$. The other results we take as given are named in the steps.

1. *Frobenius.* We take as given that there are $\varphi$-semilinear maps $\varphi_G$ of $M(G)$ with $(\varphi_G y)(t) = \varphi(y(t))$, such that $\varphi(\xi) M(G)$ lies in the image of $\varphi_G$. Naturality holds since both sides send $y$ to $\varphi \circ y \circ T_p f$. This gives part 3.
2. *Separation.* We take as given, for $G$ with a datum: if $x \in \mathrm{Lie}(G^\vee)$ and $x(\mathrm{HT}(t)) = 0$ for all $t$, then $x = 0$; and each $x \in \mathrm{Lie}(G^\vee)$ has the form $x(\mathrm{HT}(t)) = \theta(y(t))$ for some $y \in M(G)$. By the case $n = 0$ of the definition, each $y \in M(G)$ gives an $x$ with $x(\mathrm{HT}(t)) = \theta(y(t))$, and it is unique by separation. Call it $q_G(y)$. Separation also shows that $q_G$ is additive and $\theta$-semilinear.
3. *Additivity.* For $f, g : G \to H$ we have $T_p(f + g) = T_p f + T_p g$, so $M(f + g) = M(f) + M(g)$. This gives part 1.
4. *Reduction.* For a functor to $A_{\inf}$-modules, base change along $\theta$ gives a functor $D$ to $O$-modules and natural $\theta$-semilinear maps $r_G : M(G) \to D(G)$. Since $\theta$ is surjective with kernel $\xi A_{\inf}$, each $r_G$ is surjective with kernel $\xi M(G)$. This gives part 4.
5. *The map $\pi_G$.* The map $q_G$ vanishes on $\xi M(G)$, since $\theta(\xi) = 0$. So it factors as $q_G = \pi_G \circ r_G$ for an $O$-linear $\pi_G$. Each $x$ is $q_G(y)$ for some $y$ by step 2, so $\pi_G$ is surjective.
6. *The map $\iota_G$.* We take as given: for $G$ with a datum and $r_G$, $\pi_G$ as above, there is an injective $\iota_G : \omega_G \to D(G)$ whose image is the kernel of $\pi_G$, with $\iota_G(\mathrm{dlog}\, \chi) = r_G(y)$ whenever $y(t) = \mu\, \langle t, \chi \rangle$ for all $t$. We take as given that $\iota_G$ is natural. Naturality of $\pi_G$ follows from separation and from the compatibility of $\mathrm{HT}$ with $T_p f$. This gives part 5.
7. *Rank.* We take as given that $M(G)$ is free of finite rank equal to the height when $G$ has a datum. This gives part 2.
8. *The two basic groups.* We take as given an isomorphism $e : M(\mathbb{Q}_p/\mathbb{Z}_p) \to A_{\inf}$ with $e(y) = y(t_0)$ for the generator $t_0$ of the Tate module. Then $e(\varphi_G y) = \varphi(y(t_0)) = \varphi(e(y))$, which is part 6. We take as given an isomorphism $e : M(\mu_{p^\infty}) \to A_{\inf}$ with $\mu\, e(y) = y(t_\varepsilon)$, where $t_\varepsilon$ is the point of $T_p \mu_{p^\infty}$ given by $\varepsilon$. Then
$$\begin{aligned}
\mu\, e(\varphi_G m) = \varphi(m(t_\varepsilon)) = \varphi(\mu\, e(m)) = \mu\, \varphi(\xi)\, \varphi(e(m)),
\end{aligned}$$
since $\varphi(\mu) = \mu\, \varphi(\xi)$. Since $A_{\inf}$ is a domain and $\mu \neq 0$, we get $e(\varphi_G m) = \varphi(\xi)\, \varphi(e(m))$, which is part 7.
9. *Maps from $\mu_{p^\infty}$.* We take as given: if $g : M(\mu_{p^\infty}) \to M(\mathbb{Q}_p/\mathbb{Z}_p)$ is linear and $(g m')(t) = \varphi((g m)(t))$ whenever $m'(t) = \varphi(m(t))$ for all $t$, then $g = M(f)$ for a unique $f$. If $g$ commutes with the Frobenius maps and $m'(t) = \varphi(m(t))$, then $m' = \varphi_G(m)$ by step 1, so $g(m') = \varphi_G(g(m))$, which has the required values. This gives part 8. $\square$

The functor uses only the Tate module, the Hodge-Tate map and the Frobenius of $A_{\inf}$; the data enter through the results taken as given, as a source of bases. The proof of the theorem on prismatic Dieudonné modules combines the frame of the last sections, the period matrices, the lift to $A_{\inf}$, and a construction of data from the lifted matrices for biconnected groups, then applies the two theorems of this section.

**Remark 5.6.7 (Formalization).** The first theorem is in [PDivisibleGroupDatumOfConnectedDualConnected.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/PDivisibleGroupDatumOfConnectedDualConnected.lean#L25), with the retract lemma `isConn_of_retract` at line 13. The second is in [PrismaticDieudonneHodgeOfHodgeTateDatum.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/PrismaticDieudonneHodgeOfHodgeTateDatum.lean#L25); its inputs are eight `GlobalTheory.T` statements, of which we read the statements only, and two general lemmas on base change along $\theta$. A datum is `Datum` in XiMulNu.lean (line 54) and having one is `HasDatum` in [GhostFrobenius.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/GhostFrobenius.lean#L79), where the ring of the action is fixed to $\mathbb{Z}_p$; the lattice is `latt` in the same file. The data are `PrismaticDieudonneHodgeAt` in InjectiveOfSmulMemRange.lean (line 23). Part 3 asks only that the image of $\varphi_G$ contains $\varphi(\xi) M(G)$, and part 8 is full faithfulness for the single pair $(\mathbb{Q}_p/\mathbb{Z}_p, \mu_{p^\infty})$. A second, different definition with the same name is in HodgeAtOfPrismaticDieudonneAt.lean (line 62); it also asks that $\varphi_G$ is injective. The theorem on prismatic Dieudonné modules (InjectiveOfSmulMemRange.lean, line 62) assumes only that $\varepsilon^{1/p}$ gives a primitive $p$-th root of unity, and its proof in PrismaticDieudonneHodge.lean derives a primitive system from that. The retract lemma assumes $O$ nonzero.
