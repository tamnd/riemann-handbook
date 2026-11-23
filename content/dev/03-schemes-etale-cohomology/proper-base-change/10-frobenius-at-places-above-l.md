---
title: Frobenius at places above ℓ
decls:
  - UpperTheory.Ru.crystallineComparison.phiStep
  - UpperTheory.Ru.crystallineComparison.phiStep_of
  - UpperTheory.Ru.crystallineComparison.geoLoc
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Frobenius at places above ℓ

The [Galois row](/proof/galois-row/) attaches Galois representations to Hecke eigensystems in the cohomology of towers of varieties, and it needs to know their local behaviour at all places. At a place $w$ that does not divide $\ell$, the Frobenius is controlled by the Eichler-Shimura relation in étale cohomology. At a place above $\ell$ there is no Frobenius element that acts on the representation, and the statement must be made through $p$-adic Hodge theory: the representation is crystalline, and the Frobenius of its Weil-Deligne representation is controlled by the Hecke polynomial. In this section we prove this statement from [the Frobenius relation](/entry/fin-all/) and the crystalline comparison theorem. It is the crystalline field of [Steps holds](/entry/steps-holds/), and it gives the crystalline clause of [the Galois row step](/step/geo-one-holds/).

### Towers and pieces

Let $E$ be a number field with algebraic closure $\Omega$, and let $G_E = \operatorname{Gal}(\Omega/E)$. Let $\ell$ be a prime, let $\overline{\mathbb{Q}}_\ell$ be an algebraic closure of $\mathbb{Q}_\ell$, and let $\epsilon : \overline{\mathbb{Q}}_\ell \to \mathbb{C}$ be a field isomorphism.

**Definition 3.10.1 (Tower).** A *tower* over $E$ is a scheme $Z$ over $E$ with a set $\Gamma$ of *Hecke correspondences* $Z \xleftarrow{s_g} Y_g \xrightarrow{t_g} Z$, $g \in \Gamma$. The tower is *nice* if $Z$ is smooth and projective over $E$ and each $s_g$ is finite étale.

Let $H^*(Z_\Omega) = \bigoplus_n H^n(Z_\Omega, \mathbb{Q}_\ell)$. For $g \in \Gamma$, the *Hecke operator* $T_g$ is the endomorphism $s_{g*} t_g^*$ of $H^*(Z_\Omega)$: it is characterized by the condition that for a finite Galois cover $c : W \to Z_\Omega$ on which $s_g$ splits by sections $\sigma_1, \dots, \sigma_k : W \to Y_{g,\Omega}$, we have $c^* T_g x = \sum_{i} (t_g \sigma_i)^* x$. The group $G_E$ acts on $H^*(Z_\Omega)$ by transport of structure, and on $L \otimes_{\mathbb{Q}_\ell} H^*(Z_\Omega)$ for each field $L \supseteq \mathbb{Q}_\ell$ by base change.

**Definition 3.10.2 (Generalized eigenspaces).** Let $L \supseteq \mathbb{Q}_\ell$ be a field, let $\iota : J \to \Gamma$ be a family of correspondences and let $\theta : J \to L$. Then
$$V(L, \iota, \theta) = \bigcap_{j \in J} \bigcup_{N \geq 1} \ker\bigl( (T_{\iota(j)} \otimes 1 - \theta(j))^N \bigr) \subseteq L \otimes_{\mathbb{Q}_\ell} H^*(Z_\Omega)$$
is the joint generalized eigenspace of the $T_{\iota(j)}$ with the eigenvalues $\theta(j)$.

**Definition 3.10.3 (θ-piece).** Let $\theta : \Gamma \to L$ be a map, a *system of Hecke eigenvalues*. The $\theta$-*piece* is the joint eigenspace
$$\Pi_\theta = \bigcap_{g \in \Gamma} \ker\bigl(T_g \otimes 1 - \theta(g)\bigr) \subseteq L \otimes_{\mathbb{Q}_\ell} H^*(Z_\Omega).$$
A representation $\rho_0 : G_E \to \mathrm{GL}_d(L)$ is a *matrix of the action* on $\Pi_\theta$ if there is a basis $b_1, \dots, b_d$ of $\Pi_\theta$ with $\sigma(b_j) = \sum_i \rho_0(\sigma)_{ij} b_i$ for all $\sigma \in G_E$ and all $j$.

An eigenvector is a generalized eigenvector, so $\Pi_\theta \subseteq V(L, \mathrm{id}_\Gamma, \theta)$. On $\Pi_\theta$ each $T_g$ is the scalar $\theta(g)$, and the proofs below use this.

**Definition 3.10.4 (Piece).** Let $\theta : \Gamma \to \overline{\mathbb{Q}}_\ell$. A representation $\rho : G_E \to \mathrm{GL}_d(\overline{\mathbb{Q}}_\ell)$ is a *piece* of $H$ for $\theta$ if there are a matrix $\rho_0$ of the action on $\Pi_\theta$ and a function $c$ on $\{1, \dots, d\}$ such that each $\rho_0(\sigma)$ is block triangular for $c$ and $\rho(\sigma)$ is its block diagonal part.

### The congruence at a place above ℓ

Let $w$ be a finite place of $E$ above $\ell$, with valuation ring $\mathcal{O}_w \subset E$, residue degree $f_w$ and norm $Nw = \ell^{f_w}$. For $\vartheta_0, \dots, \vartheta_n \in \overline{\mathbb{Q}}_\ell$, the *Hecke polynomial* is
$$P_w(X) = \sum_{j=0}^{n} (-1)^j (Nw)^{\binom{j}{2}} \vartheta_j X^{n-j}.$$

**Definition 3.10.5 (Congruence at $w$).** The tower $H$ with $\theta$ satisfies the *congruence at $w$* for $\vartheta_0, \dots, \vartheta_n$ if the following data exist:

1. a projective smooth scheme $\mathcal{Y}$ over $\mathcal{O}_w$, with a map $\pi : Z \to \mathcal{Y}$ over $E$, and a finite group $\Delta$ acting on $Z$, such that $Z \to \mathcal{Y}_E$ is finite, étale, surjective and Galois with group $\Delta$, and each element of $\Delta$ is a Hecke correspondence $g$ with $\theta(g) = 1$;
2. a uniformizer $\varpi$ of $\mathcal{O}_w$ and correspondences $T_0, \dots, T_n$ on $\mathcal{Y}$ over $\mathcal{O}_w$ that satisfy the point identity of [Theorem 3.8.4](/entry/w-zero/) with $q = Nw$;
3. Hecke correspondences $\gamma_j$ and integers $m_j > 0$ such that $T_j$ lies under $\gamma_j$ with multiplicity $m_j$, and $\theta(\gamma_j) = m_j \vartheta_j$.

The same definition makes sense over the ring of integers $\mathcal{O}_K$ of a finite extension $K$ of $\mathbb{Q}_\ell$ with residue field of size $\ell^f$: we replace $\mathcal{O}_w$ by $\mathcal{O}_K$ and $Nw$ by $\ell^f$. We then speak of the *congruence over $\mathcal{O}_K$*.

### The theorem

**Theorem 3.10.6 (Frobenius at places above $\ell$).** Let $H$ be a nice tower over $E$, let $\theta$ be a system of Hecke eigenvalues and let $\rho : G_E \to \mathrm{GL}_d(\overline{\mathbb{Q}}_\ell)$ be continuous and a piece of $H$ for $\theta$. Let $w \mid \ell$, and assume the congruence at $w$ for $\vartheta_0, \dots, \vartheta_n$. Assume $\vartheta_0 \neq 0$ and
$$\epsilon(P_w)(X) = \epsilon(\vartheta_0) \prod_{r \in R} (X - r)$$
for a multiset $R$ of complex numbers. Then for every place of $\Omega$ above $w$, with decomposition group $D_w$, the restriction of $\rho$ to $D_w$ is crystalline, and there are an element $g$ of the Weil group at $w$ of degree $-1$ and an integer $m \geq 0$ such that the characteristic polynomial of $g$ on the Weil-Deligne representation of $\rho|_{D_w}$ divides $\prod_{r \in R} (X - r)^m$.

Lean: `UpperTheory.Ru.crystallineComparison.phiStep`.

The Weil-Deligne representation of a crystalline representation is defined by Fontaine's functor $D_{\mathrm{cris}}$, and its Frobenius is the linear Frobenius $\varphi^f$ (J.-M. Fontaine, *Représentations ℓ-adiques potentiellement semi-stables*, Astérisque 223, 1994; see the [Background](/learn/galois-representations/#crystalline-de-rham-and-potentially-semistable-representations)). An element of degree $-1$ is a geometric Frobenius. So the theorem says that the eigenvalues of the crystalline Frobenius on $\rho|_{D_w}$ are roots of the Hecke polynomial.

We prove the theorem in two steps. The first step is local: over a finite extension $K$ of $\mathbb{Q}_\ell$, the $\theta$-piece embeds in a crystalline representation on which the Hecke polynomial kills the crystalline Frobenius. The second step passes from $\rho_0$ to its block diagonal part $\rho$.

### A local crystalline model

Let $K$ be a finite extension of $\mathbb{Q}_\ell$ in $\overline{\mathbb{Q}}_\ell$, with $G_K = \operatorname{Gal}(\overline{\mathbb{Q}}_\ell/K)$. For a representation $V$ of $G_K$ on a finite-dimensional $\mathbb{Q}_\ell$-vector space, let $D_{\mathrm{cris}}(V) = (V \otimes_{\mathbb{Q}_\ell} B_{\mathrm{cris}})^{G_K}$.

**Definition 3.10.7 (Local crystalline model).** Let $G$ be a group with a homomorphism $e : G \to G_K$, let $f, q, n \geq 0$ be integers, let $\vartheta_0, \dots, \vartheta_n \in \overline{\mathbb{Q}}_\ell$ and let $r_0 : G \to \mathrm{GL}_a(\overline{\mathbb{Q}}_\ell)$. A *local crystalline model* of $r_0$ for $(f, q, n, \vartheta)$ is a crystalline representation $V$ of $G_K$ on a finite-dimensional $\mathbb{Q}_\ell$-vector space, endomorphisms $T_0, T_1, \dots$ of $V$, and an injective $\overline{\mathbb{Q}}_\ell$-linear map $b : \overline{\mathbb{Q}}_\ell^a \to \overline{\mathbb{Q}}_\ell \otimes V$, such that:

1. $\sum_{j=0}^{n} (-1)^j q^{\binom{j}{2}} (T_j \otimes \varphi^{f(n-j)}) x = 0$ for each $x \in D_{\mathrm{cris}}(V)$;
2. $b(r_0(g) x) = e(g) \, b(x)$ for all $g \in G$ and $x$;
3. $T_j b(x) = \vartheta_j b(x)$ for all $j \leq n$ and $x$.

So $r_0$ is a subrepresentation of $\overline{\mathbb{Q}}_\ell \otimes V$, on which $T_j$ acts by $\vartheta_j$, and the relation 1 is the Hecke polynomial evaluated at the crystalline Frobenius, before we replace $T_j$ by $\vartheta_j$.

We use two theorems as inputs. The first is [Theorem 3.9.2](/entry/fin-all/), the Frobenius relation, for finite extensions $K$ with residue field of size $\ell^f$. The second is the crystalline comparison theorem of G. Faltings (*Crystalline cohomology and p-adic Galois representations*, 1989), which we take as given in this form: for each finite extension $K$ of $\mathbb{Q}_\ell$ and each smooth projective scheme $\mathcal{M}$ over $\mathcal{O}_K$, each $H^j(\mathcal{M}_{\overline{K}}, \mathbb{Q}_\ell)$ is a crystalline representation of $G_K$.

**Proposition 3.10.8 (Local crystalline model).** Assume the conclusion of [Theorem 3.9.2](/entry/fin-all/) and the crystalline comparison theorem. Let $K$ be a finite extension of $\mathbb{Q}_\ell$ such that $\mathcal{O}_K$ is a discrete valuation ring with residue field of size $\ell^f$, $f > 0$. Let $H$ be a nice tower over $K$ and let $\theta : \Gamma \to \overline{\mathbb{Q}}_\ell$. Assume the congruence over $\mathcal{O}_K$ for $\vartheta_0, \dots, \vartheta_n$. Let $\rho_1 : G_K \to \mathrm{GL}_a(\overline{\mathbb{Q}}_\ell)$ be a matrix of the action on $\Pi_\theta$, with $\Omega = \overline{\mathbb{Q}}_\ell$. Then $\rho_1$ has a local crystalline model for $(f, \ell^f, n, \vartheta)$, with $G = G_K$ and $e$ the identity.

Lean: `UpperTheory.Ru.crystallineComparison.geoLoc`.

*Proof.* Let $\pi : Z \to \mathcal{Y}$, $\Delta$, $T_j$, $\gamma_j$ and $m_j$ be the data of the congruence, and write $H^*(\mathcal{Y}) = \bigoplus_i H^i(\mathcal{Y}_{\overline{\mathbb{Q}}_\ell}, \mathbb{Q}_\ell)$. We use three facts from the chapter on [Galois representations](/entry/geo-side-of/), which we take as given here.

1. The map $\pi^* \otimes 1 : \overline{\mathbb{Q}}_\ell \otimes H^*(\mathcal{Y}) \to \overline{\mathbb{Q}}_\ell \otimes H^*(Z_{\overline{\mathbb{Q}}_\ell})$ is injective, commutes with $G_K$, and its image contains $\Pi_\theta$. The reason is that $Z \to \mathcal{Y}_K$ is Galois with group $\Delta$ and $\theta = 1$ on $\Delta$.
2. Each $H^i(\mathcal{Y}_{\overline{\mathbb{Q}}_\ell}, \mathbb{Q}_\ell)$ is finite-dimensional, since $\mathcal{Y}$ is smooth and projective.
3. For each $j \leq n$ there is an action $A_j$ of $T_j$ on $H^*(\mathcal{Y})$ in the sense of the [previous section](/entry/fin-all/), with $T_{\gamma_j} \circ \pi^* = m_j \, \pi^* \circ A_j$. This uses that $s_{\gamma_j}$ is finite étale and that $T_j$ lies under $\gamma_j$ with multiplicity $m_j$.

*Coordinates.* Let $y_1, \dots, y_a$ be the basis of $\Pi_\theta$ for $\rho_1$. By fact 1, $y_k = \pi^*(z_k)$ for some $z_k$. Since $H^i(\mathcal{Y}_{\overline{\mathbb{Q}}_\ell}) = 0$ for $i < 0$, there is $N$ such that all $z_k$ lie in degrees $0$ to $N - 1$. We choose a basis of each $H^i$, $i < N$, of size $d_i$, and we put $V = \bigoplus_{i < N} \mathbb{Q}_\ell^{d_i}$. Let $u : V \to H^*(\mathcal{Y})$ be the coordinate map onto $\bigoplus_{i<N} H^i$. Then $\pi^* u \otimes 1$ is injective and its image contains the $y_k$. So there is a unique linear $b$ with $(\pi^* u)(b(x)) = \sum_k x_k y_k$, and $b$ is injective because the $y_k$ are linearly independent.

*The Galois action.* Let $G_K$ act on $V$ by the coordinates of its action on each $H^i$. Then $\sigma \circ \pi^* u = \pi^* u \circ \sigma$, and $\sigma(y_j) = \sum_k \rho_1(\sigma)_{kj} y_k$. Both sides of $b(\rho_1(\sigma)x) = \sigma b(x)$ have the same image under the injective map $\pi^* u$, so property 2 holds.

*The Hecke action.* Let $T'_j$ be the endomorphism of $V$ given by the coordinates of $A_j$ on each $H^i$, for $j \leq n$, and put $T'_j = 0$ for $j > n$. By fact 3, $(\pi^* u)(T'_j b(x)) = m_j^{-1} T_{\gamma_j} \sum_k x_k y_k$. Each $y_k$ lies in $\Pi_\theta$, so $T_{\gamma_j} y_k = \theta(\gamma_j) y_k = m_j \vartheta_j y_k$. So $(\pi^* u)(T'_j b(x)) = \vartheta_j (\pi^* u)(b(x))$, and property 3 follows from injectivity, since $m_j \neq 0$.

*Crystalline and the relation.* By the crystalline comparison theorem, each $H^i(\mathcal{Y}_{\overline{\mathbb{Q}}_\ell}, \mathbb{Q}_\ell)$ is crystalline, and so is its copy $\mathbb{Q}_\ell^{d_i}$. We take as given, from the [previous section](/entry/fin-all/), that the conclusion of [Theorem 3.9.2](/entry/fin-all/), applied to $\mathcal{Y}$ and the actions $A_j$, gives relation 1 on each copy $\mathbb{Q}_\ell^{d_i}$. A finite direct sum of crystalline representations is crystalline, and $D_{\mathrm{cris}}$ of a direct sum is the direct sum of the $D_{\mathrm{cris}}$. So $V$ is crystalline and relation 1 holds on $V$. $\square$

### From the local model to the Frobenius

For a place of $\Omega$ above $w$ with decomposition group $D_w$, let $K_w$ be the completion of $E$ at $w$ and $e : D_w \to G_{K_w}$ the isomorphism given by the choice of an embedding $\Omega \to \overline{\mathbb{Q}}_\ell$ over the place.

**Proposition 3.10.9 (Reduction to the local model).** Assume the following local statement. For every number field $E$, every nice tower $H$ over $E$, every $\theta : \Gamma \to \overline{\mathbb{Q}}_\ell$, every matrix $\rho_0$ of the action on $\Pi_\theta$, every $w \mid \ell$ with the congruence at $w$ for $\vartheta_0, \dots, \vartheta_n$, and every place of $\Omega$ above $w$, the restriction $\rho_0|_{D_w}$ has a local crystalline model for $(f_w, Nw, n, \vartheta)$ over $K_w$, with the map $e$. Then the conclusion of the theorem holds.

Lean: `UpperTheory.Ru.crystallineComparison.phiStep_of`.

*Proof.* Let $\rho$ be a piece, with $\rho_0$ and $c$ as in the definition. Fix a place above $w$. The local statement gives a local crystalline model of $\rho_0|_{D_w}$. The restriction $\rho|_{D_w}$ is continuous, and it is the block diagonal part of $\rho_0|_{D_w}$ for the same $c$. We use two facts of $p$-adic Hodge theory.

1. *Descent to a finite extension.* There are a finite extension $L'$ of $\mathbb{Q}_\ell$, a crystalline representation $r'$ of $D_w$ over $L'$ that is a model of $\rho|_{D_w}$, and $\vartheta'_j \in L'$ with image $\vartheta_j$ in $\overline{\mathbb{Q}}_\ell$, such that $P'(\Phi)$ is nilpotent on $D_{\mathrm{cris}}(r')$. Here $P' = \sum_j (-1)^j (Nw)^{\binom{j}{2}} \vartheta'_j X^{n-j}$ and $\Phi = \varphi^{f_w}$. The reason is that $\rho|_{D_w}$ is a direct sum of subquotients of $\rho_0|_{D_w}$, that subquotients of crystalline representations are crystalline, that $D_{\mathrm{cris}}$ is exact on them, and that a continuous representation of a compact group over $\overline{\mathbb{Q}}_\ell$ is defined over a finite extension.
2. *From nilpotence to the Frobenius.* If $r'$ is such a crystalline model and $P'(\Phi)$ is nilpotent on $D_{\mathrm{cris}}(r')$, and if the image of $P'$ in $\mathbb{C}[X]$ is $u \prod_{r \in R}(X - r)$ with $u \neq 0$, then $\rho|_{D_w}$ is crystalline and a geometric Frobenius $g$ satisfies the divisibility of the theorem. The reason is that the Weil-Deligne representation of a crystalline representation has monodromy $N = 0$, and that a geometric Frobenius acts on it by $\Phi$.

We apply fact 2 with $u = \epsilon(\vartheta_0) \neq 0$. The image of $P'$ in $\mathbb{C}[X]$ is $\epsilon(P_w)$, since $\vartheta'_j \mapsto \vartheta_j$, and $\epsilon(P_w) = \epsilon(\vartheta_0) \prod_{r \in R}(X - r)$ by hypothesis. $\square$

*Proof of the theorem.* This is the proposition on the reduction to the local model, applied to the local statement. The local statement is [Theorem 1.6.1](/entry/geo-side-of/) of the chapter on Galois representations, which we apply to [Theorem 3.9.2](/entry/fin-all/) and the crystalline comparison theorem. Its proof passes to $K_w$: the congruence at $w$ gives the congruence over $\mathcal{O}_{K_w}$ for the tower base-changed to $K_w$, with $f = f_w$; the matrix $\rho_0|_{D_w}$ becomes, through $e$, a matrix $\rho_1$ of the action on the $\theta$-piece of this tower; and the proposition on the local crystalline model gives the model of $\rho_1$, hence of $\rho_0|_{D_w}$. $\square$

**Remark 3.10.10 (Formalization).** The statements also quantify over a choice of the period rings at $\ell$ and a bridge between the global and local Galois groups; $B_{\mathrm{cris}}$ stands for the period ring of this choice. The Hecke operator $T_g$ is the operator of the correspondence if one exists, and $0$ otherwise. The proof of the theorem is the line `phiStep_of (geoSide_of finAll smoothModel_crystalline)` ([SmoothModelCrystalline.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/SmoothModelCrystalline.lean#L13)). The generalized eigenspace $V(L, \iota, \theta)$ is `GlobalTheory.GalV.V`; pieces use the eigenspace `piece`. The facts used in the proofs are `pieceIn_holds`, `etSide_sm_holds`, `heckeCl`, `crysCopy`, `annModel`, `annPi`, `congBC`, `locTower_holds`, `joinQ` and `nilToPhi`; we checked them from their statements, and the reasons given for them are ours. The definitions `IsCrysAt` and `wdAt` were not unfolded.
