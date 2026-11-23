---
title: Exact triples from short exact sequences of lattices
decls:
  - GlobalTheory.BKExact.isExactTriple_of_isSESLat_gen
  - GlobalTheory.BKExact.isExactTriple_of_isSESLat
  - GlobalTheory.T.isExactTriple_breuilKisin_of_shortExactLattices
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Exact triples from short exact sequences of lattices

A short exact sequence of Galois lattices $0 \to T_0 \to T_1 \to T_2 \to 0$ gives, through identifications with $\varphi$-modules, a sequence of maps of $\varphi$-modules $P_0 \to P_1 \to P_2$. This section proves that this sequence is exact in the sense that the lifting argument needs: the first map is injective on lattices, the sequence is exact at $P_1$ on lattices, and the second map has a cokernel of finite length. The proof works over the Witt vectors $W_{\mathcal{O}}$, where the sequence splits, and comes back to $\mathfrak{S}_{\mathcal{O}}$ with determinants. The result is used in Step 2 of [the lifting along surjections of good lattices](/entry/lift-f-of-is-good/).

We keep the notation of [the integral connection](/entry/int-conn-taylor-main/): a prime $\ell$, integers $a, e \ge 1$, a system of roots $\varpi$, and a complete field $L$ over $\mathbb{Q}_\ell$ with unit ball $\mathcal{O}$, free and finite over $\mathbb{Z}_\ell$, with tame descent data for $(L, \ell, e, a)$. The ring $\mathfrak{S}_{\mathcal{O}} = \mathcal{O}[[X]]$ sits in $L[[X]]$, and $\mathrm{frob}$ is $X \mapsto X^\ell$. Let $W(\mathbb{F}_{\ell^a})$ be the ring of Witt vectors of the field with $\ell^a$ elements and let $t : W(\mathbb{F}_{\ell^a}) \to \mathcal{O}$ be a map of $\mathbb{Z}_\ell$-algebras. The identifications of this section are taken with respect to $t$, as in the definition of [an identification](/entry/int-conn-taylor-main/).

**Definition 7.20.1 (Map of $\varphi$-modules).** Let $P$ and $Q$ be $\varphi$-modules of ranks $\iota$ and $\kappa$, with matrices $Y^P_\tau$ and $Y^Q_\tau$. A *map* $F : P \to Q$ is a family of $\kappa \times \iota$ matrices $F_\tau$ with entries in $\mathfrak{S}_{\mathcal{O}}$, for $\tau \in \mathbb{Z}/a$, such that
$$F_\tau\, Y^P_\tau = Y^Q_\tau\, \mathrm{frob}(F_{\tau - 1}) \quad \text{for all } \tau.$$
It acts on vectors by $(F v)_\tau = F_\tau v_\tau$. Its *image* is $F(M_P) \subseteq M_Q$, and its *cokernel* is the $\mathfrak{S}_{\mathcal{O}}$-module $M_Q / F(M_P)$.

The relation says that $F \circ \varphi_P = \varphi_Q \circ F$ on vectors. No descent datum enters here.

**Definition 7.20.2 (Exact triple).** Let $F : P_0 \to P_1$ and $G : P_1 \to P_2$ be maps of $\varphi$-modules. The pair $(F, G)$ is an *exact triple* if:

1. for $v \in M_{P_0}$, $F v = 0$ implies $v = 0$;
2. for $v \in M_{P_1}$, $G v = 0$ if and only if $v \in F(M_{P_0})$;
3. the cokernel $M_{P_2} / G(M_{P_1})$ has finite length as an $\mathfrak{S}_{\mathcal{O}}$-module.

Condition 3 replaces the surjectivity of $G$: on the lattices, $G$ is onto up to a module of finite length. For example, multiplication by $\ell$ is a map from a rank one $\varphi$-module to itself, and its cokernel $\mathfrak{S}_{\mathcal{O}} / \ell \mathfrak{S}_{\mathcal{O}}$ has infinite length. A cokernel of finite length is killed by a power of the maximal ideal of $\mathfrak{S}_{\mathcal{O}}$.

Let $G$ be a topological group. A *lattice* $T$ of $G$ is an $\mathcal{O}$-lattice in a continuous representation $V$ of $G$ over $L$. A *map of lattices* $f : T \to T'$ is a continuous $L$-linear map $f : V \to V'$ that commutes with $G$ and satisfies $f(T) \subseteq T'$.

**Definition 7.20.3 (Short exact sequence of lattices).** Maps of lattices $f : T_0 \to T_1$ and $g : T_1 \to T_2$ form a *short exact sequence* if $f$ is injective, $g$ is surjective, $g(T_1) = T_2$, $\ker g = \operatorname{im} f$ on $V_1$, and $f^{-1}(T_1) = T_0$.

The last condition says that $f(T_0)$ is saturated in $T_1$. So the sequence $0 \to T_0 \to T_1 \to T_2 \to 0$ of $\mathcal{O}$-modules is exact.

A map $F : P \to Q$ gives a $W_{\mathcal{O}}$-linear map $F_W : W_{\mathcal{O}}^\iota \to W_{\mathcal{O}}^\kappa$. Its matrix is $\iota(F)$, where $\iota$ is the ring map from families $(f_\tau)_{\tau \in \mathbb{Z}/a}$ of elements of $\mathfrak{S}_{\mathcal{O}}$ to $W_{\mathcal{O}}$ through which the identifications are defined ($X \mapsto [\varpi^\flat]$ and the embeddings $t_\tau$). The map $\iota$ is injective.

**Definition 7.20.4 (Compatible maps).** Let $j$ and $j'$ be identifications of $P$ with $T$ and of $Q$ with $T'$. A map of lattices $f : T \to T'$ and a map of $\varphi$-modules $F : P \to Q$ are *compatible* if
$$j' \circ F_W = (1 \otimes f) \circ j \quad \text{on } W_{\mathcal{O}}^\iota.$$

We use three results on maps of $\varphi$-modules. We take them as given.

The first is a splitting over $W_{\mathcal{O}}$. Let $f, g$ be a short exact sequence of lattices, $F$ compatible with $f$ and $G$ with $g$, for identifications $j_0, j_1, j_2$. Then $\iota(G)$ has a right inverse over $W_{\mathcal{O}}$ and $\iota(F)$ has a left inverse over $W_{\mathcal{O}}$; and if $G_W(v) = 0$ for some $v \in W_{\mathcal{O}}^\kappa$, then $v = F_W(w)$ for some $w$. The reason is that $W_{\mathcal{O}} \otimes T_0 \to W_{\mathcal{O}} \otimes T_1 \to W_{\mathcal{O}} \otimes T_2$ is split exact, since the sequence of free $\mathcal{O}$-modules splits, and the $j_i$ carry it to $F_W$ and $G_W$.

The second concerns unit coefficients. Let $y_s$, for $s$ in a finite set, be families of elements of $\mathfrak{S}_{\mathcal{O}}$, and let $c_s \in W_{\mathcal{O}}$ with $\sum_s c_s\, \iota(y_s) = 1$. Then for each $\tau$ there are $s$ and $k$ such that the coefficient of $X^k$ in $y_s(\tau)$ has norm $1$.

The third turns inverses up to a scalar into statements on cokernels. Let $F : P \to Q$ be a map of $\varphi$-modules.

1. Assume that for each $\tau$ there are a matrix $Y$ over $\mathfrak{S}_{\mathcal{O}}$ and a series $g \in L[[X]]$ with a coefficient of norm $1$ such that $F_\tau Y = g \cdot 1$. Then the cokernel of $F$ has finite length.
2. Assume that for each $\tau$ there are $Y$ and $g$ as in part 1 with $Y F_\tau = g \cdot 1$. Then the image of $F$ is saturated: if $v \in M_Q$ and $f \in \mathfrak{S}_{\mathcal{O}}$, $f \ne 0$, satisfy $f v \in F(M_P)$, then $v \in F(M_P)$.

The next lemma moves an inverse from $W_{\mathcal{O}}$ to $\mathfrak{S}_{\mathcal{O}}$ at the cost of a scalar.

**Lemma 7.20.5 (Right inverses up to a scalar).** Let $m$ and $n$ be finite sets, let $A$ be an $m \times n$ matrix whose entries are families of elements of $\mathfrak{S}_{\mathcal{O}}$, and let $Z$ be an $n \times m$ matrix over $W_{\mathcal{O}}$ with $\iota(A)\, Z = 1$. Then for each $\tau$ there are an $n \times m$ matrix $Y$ over $\mathfrak{S}_{\mathcal{O}}$ and $g \in \mathfrak{S}_{\mathcal{O}}$ with a coefficient of norm $1$ such that $A_\tau\, Y = g \cdot 1$, where $A_\tau$ is the matrix of the $\tau$-components.

*Proof.* Take determinants in $\iota(A) Z = 1$. The Cauchy-Binet formula, in the form that sums over all maps $\phi : m \to n$, gives
$$1 = \sum_{\phi : m \to n} \Big(\prod_{\beta \in m} Z_{\phi(\beta)\beta}\Big)\, \iota\big(\det A_{\cdot, \phi}\big),$$
where $A_{\cdot, \phi}$ is the $m \times m$ matrix with columns $\phi(\beta)$ of $A$, and where we use that $\iota$ is a ring map, so it commutes with determinants. By the result on unit coefficients, for the given $\tau$ there is $\phi$ such that $g = \det (A_\tau)_{\cdot, \phi}$ has a coefficient of norm $1$. Let $S_\phi$ be the $n \times m$ matrix with $(S_\phi)_{k\beta} = 1$ if $\phi(\beta) = k$ and $0$ otherwise. Then $A_\tau S_\phi = (A_\tau)_{\cdot, \phi}$. Put $Y = S_\phi \operatorname{adj}\big((A_\tau)_{\cdot,\phi}\big)$. Then $Y$ has entries in $\mathfrak{S}_{\mathcal{O}}$ and
$$A_\tau Y = (A_\tau)_{\cdot, \phi}\, \operatorname{adj}\big((A_\tau)_{\cdot,\phi}\big) = g \cdot 1. \qquad \square$$

Applied to the transpose, the lemma also turns a left inverse $Y_W\, \iota(A) = 1$ into $Y A_\tau = g \cdot 1$.

**Theorem 7.20.6 (Exact triples from short exact sequences of lattices).** Let $\ell$, $a$, $e$, $\varpi$, $L$, $\mathcal{O}$ and $t$ be as above, and let $G$ be a topological group. Let $P_0, P_1, P_2$ be $\varphi$-modules of ranks $\iota, \kappa, \mu$, let $T_0, T_1, T_2$ be lattices of $G$, and let $j_i$ be an identification of $P_i$ with $T_i$ with respect to $t$. Let $f : T_0 \to T_1$ and $g : T_1 \to T_2$ form a short exact sequence of lattices, and let $F : P_0 \to P_1$ and $H : P_1 \to P_2$ be maps of $\varphi$-modules, with $F$ compatible with $f$ and $H$ compatible with $g$. Then $(F, H)$ is an exact triple.

Lean: `GlobalTheory.BKExact.isExactTriple_of_isSESLat_gen`.

*Proof.* By the splitting over $W_{\mathcal{O}}$, there are $Z$ with $\iota(H) Z = 1$ and $Y_W$ with $Y_W\, \iota(F) = 1$. By the lemma, applied to $H$ and to the transpose of $F$, for each $\tau$ there are matrices $Y^H_\tau$, $Y^F_\tau$ over $\mathfrak{S}_{\mathcal{O}}$ and elements $c^H_\tau, c^F_\tau \in \mathfrak{S}_{\mathcal{O}}$ with a coefficient of norm $1$ such that
$$H_\tau\, Y^H_\tau = c^H_\tau \cdot 1, \qquad Y^F_\tau\, F_\tau = c^F_\tau \cdot 1.$$
A series with a coefficient of norm $1$ is not $0$.

*Condition 1.* Let $v \in M_{P_0}$ with $F v = 0$. Then $c^F_\tau v_\tau = Y^F_\tau F_\tau v_\tau = 0$. Since $L[[X]]$ is a domain and $c^F_\tau \ne 0$, $v_\tau = 0$ for all $\tau$.

*Condition 2, first direction.* Let $v \in M_{P_1}$ with $H v = 0$. Put $f = \prod_\tau c^F_\tau$, a nonzero element of $\mathfrak{S}_{\mathcal{O}}$. By part 2 of the third result, applied with the left inverses $Y^F_\tau$, it is enough to show that $f v \in F(M_{P_0})$. Let $\iota(v) \in W_{\mathcal{O}}^\kappa$ be the image of $v$. By compatibility, $H_W(\iota(v)) = \iota(H v) = 0$, so by the exactness over $W_{\mathcal{O}}$ there is $w$ with $\iota(F)\, w = \iota(v)$. Then
$$\iota(F Y^F)\, \iota(v) = \iota(F)\, \iota(Y^F)\, \iota(F)\, w = \iota(F)\, \iota(c^F) w = \iota(c^F)\, \iota(v),$$
and since $\iota$ is injective, $F_\tau Y^F_\tau v_\tau = c^F_\tau v_\tau$ for every $\tau$. Put
$$u_\tau = \Big(\prod_{\sigma \ne \tau} c^F_\sigma\Big)\, Y^F_\tau v_\tau.$$
Then $u \in M_{P_0}$, since all factors have entries in $\mathfrak{S}_{\mathcal{O}}$, and $F_\tau u_\tau = \big(\prod_{\sigma} c^F_\sigma\big) v_\tau = f v_\tau$. So $f v = F u$.

*Condition 2, second direction.* We show $H_\tau F_\tau = 0$ for all $\tau$; then $H F w = 0$ for all $w$. Since $g \circ f = 0$ on $V_0$, the map $(1 \otimes g)(1 \otimes f)$ is $0$ on $W_{\mathcal{O}} \otimes T_0$. By compatibility,
$$j_2\big(H_W F_W v\big) = (1 \otimes g)(1 \otimes f)\, j_0(v) = 0,$$
so $H_W F_W = 0$ since $j_2$ is injective. Applied to the basis vectors, this gives $\iota(H F) = 0$. Since $\iota$ is injective, $H_\tau F_\tau = 0$ for every $\tau$.

*Condition 3.* This is part 1 of the third result, applied to $H$ with the right inverses $Y^H_\tau$. $\square$

The case used in the proof is the Galois group of $\mathbb{Q}_\ell$, with the map $t$ that comes from Fontaine's map $\theta$. Let $L$ be a finite extension of $\mathbb{Q}_\ell$ that contains the unramified extension of degree $a$. Then $\theta$ induces a map of $\mathbb{Z}_\ell$-algebras $\theta_W : W(\mathbb{F}_{\ell^a}) \to \mathcal{O}$.

**Corollary 7.20.7.** Let $\ell$ be a prime, $a, e \ge 1$, $\varpi$ a system of roots, and $L$ a finite extension of $\mathbb{Q}_\ell$ that contains the unramified extension of degree $a$, with tame descent data for $(L, \ell, e, a)$. Let $P_0, P_1, P_2$ be $\varphi$-modules over $\mathcal{O}$, $T_0, T_1, T_2$ lattices of $G_{\mathbb{Q}_\ell}$, and $j_i$ an identification of $P_i$ with $T_i$ with respect to $\theta_W$. Let $f : T_0 \to T_1$ and $g : T_1 \to T_2$ form a short exact sequence of lattices, and let $F : P_0 \to P_1$ and $G : P_1 \to P_2$ be maps of $\varphi$-modules compatible with $f$ and $g$. Then $(F, G)$ is an exact triple.

Lean: `GlobalTheory.BKExact.isExactTriple_of_isSESLat` (also `GlobalTheory.T.isExactTriple_breuilKisin_of_shortExactLattices`, a second name).

*Proof.* This is the theorem applied to $G_{\mathbb{Q}_\ell}$ with $t = \theta_W$. $\square$

**Remark 7.20.8 (Formalization).** The three results that we take as given are `phiModuleHom_shortExact_split_wittTilt_alt` with `tame_setting_group_action_compat` (the splitting and the exactness over $W_{\mathcal{O}}$), `exists_unit_coeff_wittTilt_relation`, and `finiteLength_coker_of_surjective_mod_uniformizer`. We read their statements, not their proofs, so the reason given for the splitting is a classical sketch, and we give none for the other two. Two names do not match their statements. `tame_setting_group_action_compat` states the exactness of $F_W, H_W$ at the middle term; it says nothing about a group action. `finiteLength_coker_of_surjective_mod_uniformizer` assumes inverses up to a scalar with a unit coefficient, not a surjectivity modulo a uniformizer. The lemma on right inverses is `exists_right`, with `det_mul_eq_sum_fun'`, `selCols` and `exists_right_of_minor` ([IsExactTripleBreuilKisinOfShortExactLattices.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/IsExactTripleBreuilKisinOfShortExactLattices.lean#L48)). A map of $\varphi$-modules carries no descent condition, and the theorem holds for any topological group. The second name is a wrapper that sets `maxHeartbeats` to 1000000 and closes the goal with `first | exact @…`.
