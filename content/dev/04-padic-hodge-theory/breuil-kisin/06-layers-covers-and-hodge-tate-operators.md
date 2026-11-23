---
title: Layers, covers and Hodge-Tate operators
decls:
  - GlobalTheory.CovClose.exists_gal_inv
  - GlobalTheory.CovClose.lay_pos
  - GlobalTheory.T.isSemistable_latticeInMatrixAlgebraLayer
  - GlobalTheory.T.layer_DdR_bounds_alt
  - GlobalTheory.T.deRham_crystalline_of_lattice_reads
  - GlobalTheory.T.exists_galois_elem_cyclotomic_period_not_root_of_unity
  - GlobalTheory.T.isHodgeTate_iff_diagonal_adapted_basis
  - GlobalTheory.T.exists_hodge_basis_at_embedding
  - GlobalTheory.T.hodgeTateOperator_pow_eq_sum
  - GlobalTheory.T.trace_pow_eq_along_latticeTowerCover
  - GlobalTheory.T.multiset_eq_of_power_sums_zpow_eq
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Layers, covers and Hodge-Tate operators

This section sets up the objects of [the theorem on covers](/entry/closed-of-cover/), which is proved in the next section and ends the chapter. A homomorphism $r : G_K \to \mathrm{GL}_a(\Omega)$ is compared with lattices through a *reading*: an equivariant map from a lattice to the matrix algebra $M_a(\Omega)$ whose image contains $1$. A *cover* of $r$ is a lattice read by $r$ together with a tower of lattices whose layers are built from members of a given set of representations. We then attach to one element $g \in G_K$ a *Hodge-Tate operator*: a matrix on $C^a$ that acts on the graded pieces of the de Rham filtration, with eigenvalues $z^h$, where $h$ runs over the Hodge-Tate jumps and $z \in C$ is not a root of unity. The lemmas of the section say that the traces of the powers of these operators pass from the layers of a cover to the lattice that it covers, and that the traces determine the jumps. We keep the notation of the previous sections. For $x \in M_d(A_{\mathrm{inf}})$ we write $\theta(x) \in M_d(C)$ for $\theta$ applied to the entries of $\iota(x)$, and $|\cdot|$ is the absolute value of $C$, with $|\ell| = \ell^{-1}$.

**Definition 3.6.1 (Reading).** Let $\Gamma$ be a group and let $\rho : \Gamma \to \mathrm{GL}_d(\mathbb{Z}_\ell)$ and $r : \Gamma \to \mathrm{GL}_a(\Omega)$ be homomorphisms. We say that $r$ *reads* $\rho$ through $b_1, \dots, b_d \in M_a(\Omega)$ and $e \in \mathbb{Z}_\ell^d$ if
$$r(g) \, b_j = \sum_{i=1}^d \rho(g)_{ij} \, b_i \quad \text{for all } g \in \Gamma \text{ and all } j, \qquad \sum_{i=1}^d e_i b_i = 1.$$

The first condition says that $v \mapsto \sum_i v_i b_i$ maps $\mathbb{Z}_\ell^d$ to $M_a(\Omega)$ and turns $\rho$ into left multiplication by $r$. The second condition lets us recover $r$ from $\rho$: $r(g) = r(g) \sum_j e_j b_j = \sum_i (\rho(g) e)_i \, b_i$.

**Definition 3.6.2 (Realization).** Let $L_0$ be a finite extension of $\mathbb{Q}_\ell$ in $\Omega$ and let $\rho_1 : G_K \to \mathrm{GL}_a(\Omega)$ be a homomorphism. A *realization* of $\rho_1$ over a finite extension $L \supseteq L_0$ in $\Omega$ is a homomorphism $r' : G_K \to \mathrm{GL}_a(L)$ that equals $\rho_1$ in $\mathrm{GL}_a(\Omega)$, together with the representation $R$ of $G_K$ on $L^a$ given by $R(g) v = r'(g) v$.

A realization over $L$ exists if and only if all entries of $\rho_1$ lie in $L$. For an embedding $\tau : K \to L$ we have the [multiplicities](/entry/sst-periods/) $m_\tau(R, n)$, and we view $\tau$ as an embedding of $K$ into $\Omega$ through $L \subset \Omega$.

**Definition 3.6.3 (Layer and cover).** Let $\Gamma$ be a group, $L_0$ a finite extension of $\mathbb{Q}_\ell$ in $\Omega$, and $\mathcal{C}$ a set of homomorphisms $\Gamma \to \mathrm{GL}_a(\Omega)$. Let $\rho' : \Gamma \to \mathrm{GL}_{d'}(\mathbb{Z}_\ell)$ be a homomorphism. A *layer* for $\rho'$ with members in $\mathcal{C}$ consists of an integer $m \geq 0$, members $\rho_1, \dots, \rho_m \in \mathcal{C}$, finite extensions $L_1, \dots, L_m \supseteq L_0$ in $\Omega$ such that $\rho_k$ has entries in $L_k$, matrices $b_{s,k} \in M_a(L_k)$ for $1 \leq s \leq d'$, a vector $e' \in \mathbb{Z}_\ell^{d'}$ and constants $c_1, \dots, c_m \in \Omega$, such that:

1. the vectors $b_s = (b_{s,1}, \dots, b_{s,m})$ form a basis of $\prod_k M_a(L_k)$ over $\mathbb{Q}_\ell$;
2. for each $k$, $\rho_k$ reads $\rho'$ through $b_{1,k}, \dots, b_{d',k}$ and $e'$.

Now let $\Gamma$ be a topological group and $r : \Gamma \to \mathrm{GL}_a(\Omega)$ a homomorphism. A *cover* of $r$ over $L_0$ with members in $\mathcal{C}$ consists of a continuous homomorphism $\rho : \Gamma \to \mathrm{GL}_d(\mathbb{Z}_\ell)$, elements $b_1, \dots, b_d$ and $e$ through which $r$ reads $\rho$, a [tower](/entry/limit-frame-exists/) $(\rho'_n, \Pi_n, f_n)$ of $\rho$ with every $\rho'_n$ continuous, and for each $n$ a layer for $\rho'_n$ with members in $\mathcal{C}$, with data $m^{(n)}$, $b^{(n)}_{s,k}$, $e^{(n)}$ and $c^{(n)}_k$, such that for all $n$ and $s$:
$$\Pi_n e^{(n)} \equiv e \pmod{\ell^n}, \qquad \Big| \mathrm{tr} \Big( \sum_{i=1}^d \Pi_n(i, s) \, b_i \Big) - \sum_{k} c^{(n)}_k \, \mathrm{tr} \big( b^{(n)}_{s,k} \big) \Big| \leq \ell^{-n}.$$

By 1 and 2, the map $v \mapsto (\sum_s v_s b_{s,k})_k$ is an isomorphism from $\mathbb{Q}_\ell^{d'}$ onto $\prod_k M_a(L_k)$ that turns $\rho'$ into left multiplication by $\rho_k$ on the $k$-th factor. The columns of $M_a(L_k)$ are $a$ copies of $L_k^a$. So $\mathbb{Q}_\ell^{d'}$ with $\rho'$ is a sum of copies of realizations of members of $\mathcal{C}$, with scalars restricted to $\mathbb{Q}_\ell$. A cover approximates $\rho$ modulo $\ell^n$ by the layer $\rho'_n$, compatibly with the vectors $e$ and up to $\ell^{-n}$ in the traces.

**Lemma 3.6.4 (The first layer is not empty).** Let $a \geq 1$ and let $r : \Gamma \to \mathrm{GL}_a(\Omega)$ have a cover over $L_0$ with members in $\mathcal{C}$. Then the layer of $\rho'_1$ has $m \geq 1$ members.

Lean: `GlobalTheory.CovClose.lay_pos`.

*Proof.* Assume $m = 0$. Then $\prod_k M_a(L_k)$ is the zero space, and a basis of the zero space is empty, so $d'_1 = 0$. By 1 of the definition of a tower there is $S$ with $\Pi_1 S \equiv 1 \pmod{\ell}$ in $M_d(\mathbb{Z}_\ell)$. Since $d'_1 = 0$, the product $\Pi_1 S$ is $0$. If $d \geq 1$, the diagonal entry gives $\ell \mid 1$ in $\mathbb{Z}_\ell$, which is false. So $d = 0$, and $\sum_i e_i b_i$ is the empty sum $0$. This contradicts $\sum_i e_i b_i = 1$ in $M_a(\Omega)$, since $a \geq 1$. $\square$

**Lemma 3.6.5 (Layers).** Let $\rho'$ have a layer with members in a set $\mathcal{C}$ of homomorphisms $G_K \to \mathrm{GL}_a(\Omega)$, and let $V' = \mathbb{Q}_\ell^{d'}$ with $\rho'$. If every realization over every finite extension $L \supseteq L_0$ of every member of $\mathcal{C}$ is semistable, then $V'$ is semistable. The same holds with crystalline in place of semistable.

Lean: `GlobalTheory.T.isSemistable_latticeInMatrixAlgebraLayer`.

**Lemma 3.6.6 (Jumps of a layer).** Let $L_0$ contain $\tau(K)$ for every embedding $\tau : K \to \Omega$. Let $J$ assign to each such $\tau$ a finite multiset $J(\tau)$ of integers, and let $N \geq 0$ with $|h| \leq N$ for all $h \in J(\tau)$ and all $\tau$. Assume that every realization $R$ over $L \supseteq L_0$ of every member of $\mathcal{C}$ is semistable with $m_\tau(R, n)$ equal to the multiplicity of $n$ in $J(\tau)$ for all $\tau : K \to L$ and $n \in \mathbb{Z}$. Then for every $\rho'$ with a layer with members in $\mathcal{C}$, the representation $V' = \mathbb{Q}_\ell^{d'}$ satisfies $D_{\mathrm{dR}}(V') \subseteq \mathrm{Fil}^{-N}(V')$ and $D_{\mathrm{dR}}(V') \cap \mathrm{Fil}^{N+1}(V') = 0$.

Lean: `GlobalTheory.T.layer_DdR_bounds_alt`.

**Lemma 3.6.7 (Reading de Rham and crystalline).** Let $r : G_K \to \mathrm{GL}_a(\Omega)$ read $\rho : G_K \to \mathrm{GL}_d(\mathbb{Z}_\ell)$ through some $b$ and $e$, and let $R$ be a realization of $r$ over $L \supseteq L_0$. If $\mathbb{Q}_\ell^d$ with $\rho$ is de Rham, then $R$ is de Rham. If it is crystalline, then $R$ is crystalline.

Lean: `GlobalTheory.T.deRham_crystalline_of_lattice_reads`.

**Lemma 3.6.8 (Inverting an embedding).** Let $\tau : K \to \Omega$ be an embedding over $\mathbb{Q}_\ell$. There is $\sigma \in G$ with $\sigma(\tau(x)) = x$ for all $x \in K$.

Lean: `GlobalTheory.CovClose.exists_gal_inv`.

*Proof.* Since $\Omega$ is a normal algebraic extension of $\mathbb{Q}_\ell$ that contains $K$, the embedding $\tau$ extends to a $\mathbb{Q}_\ell$-algebra map $\varphi : \Omega \to \Omega$. An endomorphism of an algebraic extension over the base field is bijective, so $\varphi \in G$. Put $\sigma = \varphi^{-1}$. Then $\sigma(\tau(x)) = \sigma(\varphi(x)) = x$ for $x \in K$. $\square$

The jumps are detected by one element of $G_K$. Since $E$ generates $\ker \theta$ and $G_K$ preserves $\ker \theta$, each $g \in G_K$ satisfies $g(E) = Ew$ for some $w \in A_{\mathrm{inf}}$, and then $g$ multiplies $E^j$ by $w^j$, so it acts on $\mathrm{Fil}^j B_{\mathrm{dR}}^+ / \mathrm{Fil}^{j+1} B_{\mathrm{dR}}^+$ through the factor $\theta(w)^j$ times its action on $C$.

**Lemma 3.6.9 (A Galois element of infinite order on $E$).** There are $g \in G_K$, $w \in A_{\mathrm{inf}}$ and $z \in C$ with $g(E) = Ew$ and $z \, \theta(w) = 1$, such that $z^i \neq 1$ for every $i \geq 1$.

Lean: `GlobalTheory.T.exists_galois_elem_cyclotomic_period_not_root_of_unity`.

**Definition 3.6.10 (Hodge-Tate operator).** Let $\xi \in A_{\mathrm{inf}}$, let $\rho : G_K \to M_a(\Omega)$ be a map and $z \in C$. A matrix $u \in M_a(C)$ is a *Hodge-Tate operator* of $\rho$ for $\xi$ with parameter $z$ if the following holds for every finite extension $K'$ of $\mathbb{Q}_\ell$, all integers $p, q \geq 0$ and all $x \in B_{\mathrm{dR}}^a$ and $y \in (B_{\mathrm{dR}}^+)^a$: if $\rho(g) \, g(x) = x$ for all $g \in G_K \cap G_{K'}$ and $\xi^q x = \xi^p y$, then $u \, \theta(y) = z^{p-q} \, \theta(y)$.

When $\xi$ generates $\ker \theta$, the vector $x = \xi^{p-q} y$ is an invariant vector of filtration degree $p - q$, and $\theta(y)$ is its image in the graded piece of degree $p - q$. So $u$ acts on the images of invariant vectors of degree $j$ by $z^j$. With $g$ and $z$ as in the last lemma, $z^{-j}$ is the factor by which $g$ moves the graded piece of degree $j$.

**Lemma 3.6.11 (Hodge-Tate operators and Hodge bases).** Assume that $B_{\mathrm{dR}}^{G_{K''}} = K''$ for every finite extension $K''$ of $\mathbb{Q}_\ell$. Let $\xi$ generate $\ker \theta$, let $\rho : G_K \to M_a(\Omega)$ be a map with a [Hodge basis](/entry/sst-periods/) $(V_H, p, q, Q)$ over $K' \supseteq K$, and let $z \in C$ and $u \in M_a(C)$. Then $u \, \theta(V_H) = \theta(V_H) \, \mathrm{diag}(z^{p_1 - q}, \dots, z^{p_a - q})$ if and only if $u$ is a Hodge-Tate operator of $\rho$ for $\xi$ with parameter $z$.

Lean: `GlobalTheory.T.isHodgeTate_iff_diagonal_adapted_basis`.

**Lemma 3.6.12 (Hodge basis at an embedding).** Let $\xi$ generate $\ker \theta$, let $L$ be a finite extension of $\mathbb{Q}_\ell$ in $\Omega$ and $r' : G_K \to \mathrm{GL}_a(L)$ a homomorphism such that the representation $R$ of $G_K$ on $L^a$ given by $r'$ is de Rham, let $\tau : K \to L$ be an embedding and let $\sigma \in G$ with $\sigma(\tau(x)) = x$ for all $x \in K$. There are a finite extension $K' \supseteq K$ and a Hodge basis $(V_H, p, q, Q)$ of $\sigma \circ r'$ for $\xi$ over $K'$ such that $\#\{i : p_i - q = n\} = m_\tau(R, n)$ for every $n \in \mathbb{Z}$.

Lean: `GlobalTheory.T.exists_hodge_basis_at_embedding`.

**Lemma 3.6.13 (Powers of the operator).** Let $r : G_K \to \mathrm{GL}_a(\Omega)$ read $\rho : G_K \to \mathrm{GL}_d(\mathbb{Z}_\ell)$ through $b$ and $e$. Let $\xi \in A_{\mathrm{inf}}$, $\sigma \in G$, $z \in C$, let $(V_H, p, q, Q)$ be a Hodge basis of $\rho$ for $\xi$ over $K$, and let $U \in M_d(C)$ with $U \theta(V_H) = \theta(V_H) \, \mathrm{diag}(z^{p_i - q})$. If $u \in M_a(C)$ is a Hodge-Tate operator of $\sigma \circ r$ for $\xi$ with parameter $z$, then for every $n \geq 0$
$$u^n = \sum_{i=1}^d (U^n e)_i \, \sigma(b_i).$$

Lean: `GlobalTheory.T.hodgeTateOperator_pow_eq_sum`.

So the eigenvalues of $u$, which are $z^h$ for the jumps $h$ of $r$, are controlled by the lattice $\rho$ through $U$.

**Lemma 3.6.14 (Traces along a cover).** Let $\Gamma$ be a topological group, $a \geq 1$, and let $r : \Gamma \to \mathrm{GL}_a(\Omega)$ have a cover over $L_0$ with members in $\mathcal{C}$, with the notation of the definition. Let $\sigma \in G$, $U \in M_d(C)$, $U'_m \in M_{d'_m}(C)$ for $m \geq 0$, $B \in \mathbb{R}$ and $S : \mathbb{N} \to C$ with $S(0) = a$. Assume that all entries of $U$ and of every $U'_m$ have absolute value at most $B$, that for every $n$ there is $m \geq n$ such that all entries of $U \Pi_m - \Pi_m U'_m$ have absolute value at most $B \ell^{-n}$, and that
$$\mathrm{tr} \Big( \sum_{i} (U'^{\,n}_m e^{(m)})_i \, \sigma(b^{(m)}_{i,k}) \Big) = S(n) \quad \text{for all } m, k, n.$$
Then $\mathrm{tr} \big( \sum_i (U^n e)_i \, \sigma(b_i) \big) = S(n)$ for every $n \geq 0$.

Lean: `GlobalTheory.T.trace_pow_eq_along_latticeTowerCover`.

**Lemma 3.6.15 (Power sums).** Let $k$ be a field of characteristic $0$ and $z \in k$ nonzero and not a root of unity. Let $J, J'$ be finite multisets of integers with $\sum_{h \in J} z^{hn} = \sum_{h \in J'} z^{hn}$ for all $n \geq 0$. Then $J = J'$.

Lean: `GlobalTheory.T.multiset_eq_of_power_sums_zpow_eq`.

The reason is that $h \mapsto z^h$ is injective, and in characteristic $0$ the power sums for $n \geq 0$ determine a finite multiset of elements of $k$.

**Remark 3.6.16 (Formalization).** The definitions are `Reads`, `Layer`, `Cover`, `IsHT`, `Hodge` and `IsZ` in [TrivIsCr.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/TrivIsCr.lean#L113), and the tower is `BKLim.Tower` of the last section. A realization is a pair `r'`, `R` with `R g v = (r' g).val *ᵥ v`; the realization of a member $\rho_k$ over $L_k$ is built by `GlobalTheory.CovClose.modelOf` and `GlobalTheory.CovClose.repOf`. Except for the first two lemmas, which are proved in [ClosedOfCover.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ClosedOfCover.lean#L38), we have not opened the lemmas of this section beyond their statements; the reason given after the lemma on power sums is ours. The constants $c_k$ of a layer and the trace condition of a cover can enter the proof of the theorem on covers only through the lemma on traces along a cover. The lemma on powers of the operator has no hypothesis on $\xi$ and no hypothesis $B_{\mathrm{dR}}^{G_{K''}} = K''$.
