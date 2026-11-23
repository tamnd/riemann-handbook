---
title: Row lattices and ties
decls:
  - Formalism.L2.SG.Pf.latSurj
  - Formalism.L2.SG.LoopsTies.tiesAt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Row lattices and ties

This section proves two facts about lattices in a Hermitian space with a flag. The first fact is that every lattice of a given type, which we call a *row lattice*, comes from an element of an adelic stabilizer, up to the stabilizer of the flag. So the row lattices are parametrized by cosets in the adelic group. The second fact collects three integrality relations, called *ties*, between the Gram matrices of pairs of flags. Both facts are inputs of the step [nonempty hypotheses](/step/nonempty-hyps/). For lattices and genera see [Hermitian lattices](/learn/groups/#hermitian-lattices-and-the-mass-formula), and for the forms see [Hermitian forms](/learn/algebra/#hermitian-and-skew-hermitian-forms) and [[Hermitian form|8NJ7XY6F1S]].

### The setting

As in the earlier sections, $K$ is a CM field with real subfield $K^+$, and $\mathcal{O}_K$ is the ring of integers of $K$. Let $V$ be a finite dimensional $K$-vector space with a nondegenerate Hermitian form $h$, linear in the second variable. A *lattice* in $V$ is a finitely generated $\mathcal{O}_K$-submodule that spans $V$ over $K$. The dual of a lattice $\Lambda$ is $\Lambda^\vee = \{ y \in V : h(w, y) \in \mathcal{O}_K \text{ for all } w \in \Lambda \}$, and $\Lambda$ is *unimodular* if $\Lambda^\vee = \Lambda$. The *genus* of $L$ is the set of lattices locally isometric to $L$ at every prime.

We fix the data of a Hermitian setting, as in the last section. There is a unimodular base lattice $L_0 \subseteq V$, the group $G_f$ of finite adelic points of the unitary group of $h$, and the closure $\widehat{L}_0$ of $L_0$ in $V \otimes \mathbb{A}_f$. There are vectors $e_1, \dots, e_r, f_1, \dots, f_r$ with $h(e_a, e_b) = h(f_a, f_b) = 0$ and $h(e_a, f_b) = \delta_{ab}$. For each index $u$ of a finite family there is a vector $z_u$ orthogonal to all $e_a$ and $f_a$ with $h(z_u, z_u) = -T_u$, where $T_u$ is a prime number. There is also an element $x_u \in G_f$ that fixes all $e_a$ and $f_a$ and stabilizes $\widehat{L}_0$. Let $\mathfrak{d}$ be the different of $K^+$ over $\mathbb{Q}$, extended to a fractional ideal of $K$. Let $g = g_0 g_1$ be the product of the two distinct primes $g_0, g_1$ of the data.

### Flags and row lattices

**Definition 6.10.1 (Flag).** A *flag* of rank $r$ and norm $T \in K$ is a tuple $F = (e_1, \dots, e_r, z)$ of vectors of $V$ such that $e_1, \dots, e_r$ are linearly independent, $h(e_a, e_b) = 0$ and $h(e_a, z) = 0$ for all $a, b$, and $h(z, z) = -T$. Its subspaces are $X_j = \operatorname{span}_K(e_1, \dots, e_j)$ for $0 \leq j \leq r$, with $X_j = X_r$ for $j > r$, and $X = X_r$. For each index $u$, the flag $F_u$ is $(e_1, \dots, e_r, z_u)$, of norm $T_u$.

**Definition 6.10.2 (Stabilizer of a flag).** The stabilizer $\operatorname{Stab}(F)$ of a flag $F$ is the set of $K$-linear isometries $\gamma$ of $(V, h)$ with $\gamma(X_j) = X_j$ for all $j$ and $\gamma(z) = z$.

For a lattice $\Lambda$ and a flag $F$, let $\Lambda_X = \Lambda \cap X$ and $\Lambda^{\flat} = (\Lambda \cap X^\perp) + X$, where $X$ is seen as an $\mathcal{O}_K$-module. Let
$$X_S = \sum_{a = 1}^{r} \mathfrak{d}^{-(r + 1 - a)} e_a .$$
For a prime $\mathfrak{P}$ of $\mathcal{O}_K$, a subscript $\mathfrak{P}$ denotes the localization at $\mathfrak{P}$.

**Definition 6.10.3 (Row lattice).** Let $F = (e_1, \dots, e_r, z)$ be a flag. An $\mathcal{O}_K$-submodule $\Lambda \subseteq V$ is a *row lattice* for $F$ if these six conditions hold.

1. $\Lambda$ is in the genus of $L_0$.
2. $\Lambda$ is a lattice and is unimodular.
3. $z \in \Lambda$.
4. For each prime $\mathfrak{P}$ there are $c_1, \dots, c_r \in K \setminus \{0\}$, with $c_a = 1$ for all $a$ when $g \in \mathfrak{P}$, such that $(\Lambda_X)_{\mathfrak{P}} = \big(\sum_a \mathcal{O}_K c_a e_a\big)_{\mathfrak{P}}$.
5. If $c \in K$ and $c z \in \Lambda^{\flat}$, then $c \in \mathcal{O}_K$.
6. $\Lambda_X = X_S$.

**Definition 6.10.4 (Lattice of an adelic element).** Let $H_f(u) \subseteq G_f$ be the subgroup of elements that fix every $e_a$, every $f_a$ and $z_u$. For $x \in H_f(u)$ let
$$\Lambda(x) = \{ y \in V : (x x_u)^{-1} y \in \widehat{L}_0 \}.$$
Two $\mathcal{O}_K$-submodules $\Lambda, \Lambda'$ are *equivalent* for $F_u$ if $\gamma(\Lambda) = \Lambda'$ for some $\gamma \in \operatorname{Stab}(F_u)$.

### Surjectivity of the lattice map

The proof of surjectivity uses an orbit theorem for a vector of nonzero norm. A vector $z$ is *primitive* in a lattice $M$ if $c z \in M$ with $c \in K$ implies $c \in \mathcal{O}_K$. Let $s_1, \dots, s_m$ be vectors of $V$ and $\Sigma = \operatorname{span}_K(s_1, \dots, s_m)$. A lattice $M$ is *split* along $s$ if every $w \in M$ has some $w_1 \in M \cap \Sigma$ with $h(s_a, w - w_1) = 0$ for all $a$.

**Theorem 6.10.5 (Orbit theorem).** Let $L$ be the standard lattice of the setting. Let $s_1, \dots, s_m, z \in V$ with $h(s_a, z) = 0$ for all $a$. Let $M$ be a unimodular lattice. Assume that $M \cap \Sigma = L \cap \Sigma$, that $L$ and $M$ are split along $s$, that $z \in L \cap M$, and that $z$ is primitive in $L$ and in $M$. Then there is $x \in G_f$ that fixes every $s_a$ and $z$, with $\{ y \in V : x^{-1} y \in \widehat{L} \} = M$.

Lean: `Formalism.L2.SG.Pf.LatDictZ.anisotropic_vector_orbit`

*Proof.* The theorem is deduced from a local statement on primitive planes and an adelic gluing statement. We did not open them, so we give no argument here. $\square$

**Theorem 6.10.6 (Surjectivity of the lattice map).** Fix an index $u$. For every row lattice $\Lambda$ for $F_u$ there are $x \in H_f(u)$ and an $\mathcal{O}_K$-submodule $\Lambda'$ with $\Lambda' = \Lambda(x)$, such that $\Lambda'$ and $\Lambda$ are equivalent for $F_u$.

Lean: `Formalism.L2.SG.Pf.latSurj`

*Proof.* Let $\mathfrak{a}_a = \mathfrak{d}^{-(r + 1 - a)}$. The first step is a splitting of row lattices. There are vectors $f'_1, \dots, f'_r$ with $h(f'_a, f'_b) = 0$ and $h(e_a, f'_b) = \delta_{ab}$, and a submodule $L$ whose elements are orthogonal to all $e_a$ and $f'_a$, with $z_u \in L$, such that
$$\Lambda = \sum_a \mathfrak{a}_a e_a + L + \sum_a \mathfrak{a}_a^{-1} f'_a .$$
The setting gives the same form for the base lattice, $L_0 = \sum_a \mathfrak{a}_a e_a + L_W + \sum_a \mathfrak{a}_a^{-1} f_a$, with $L_W$ orthogonal to all $e_a$ and $f_a$.

Second, there is an isometry $\delta$ of $V$ with $\delta(e_a) = e_a$, $\delta(f_a) = f'_a$ and $\delta(z_u) = z_u$, which lies in $\operatorname{Stab}(F_u)$. Let $\Lambda_2 = \delta^{-1}(\Lambda)$. Then
$$\Lambda_2 = \sum_a \mathfrak{a}_a e_a + \delta^{-1}(L) + \sum_a \mathfrak{a}_a^{-1} f_a ,$$
and $\delta^{-1}(L)$ is orthogonal to all $e_a$ and $f_a$. Let $p$ be the orthogonal projection onto the complement of $\operatorname{span}(e_a, f_a)$. For $y \in \Lambda_2$ we get $p(y) \in \Lambda_2$ and $y - p(y) \in L_0$. Hence a vector $y$ with $p(y) = 0$ lies in $\Lambda_2$ if and only if it lies in $L_0$.

Third, we check the hypotheses of the orbit theorem with $s = (e_1, \dots, e_r, f_1, \dots, f_r)$, $z = z_u$ and $M = \Lambda_2$. The lattice $\Lambda_2$ is unimodular because $\Lambda$ is unimodular and $\delta$ is an isometry. It contains $z_u$ because $\delta(z_u) = z_u$. The vector $z_u$ is primitive in $\Lambda$ by condition 5, since $z_u$ is orthogonal to $X$ and so $c z_u \in \Lambda$ gives $c z_u \in \Lambda^{\flat}$. It is primitive in $\Lambda_2$ because $c z_u \in \Lambda_2$ if and only if $c z_u \in \Lambda$. It is primitive in $L_0$ by the same condition for $L_0$, which the setting gives. The agreement on $\Sigma$ and the two splittings follow from the second step.

The orbit theorem gives $x \in G_f$ that fixes all $e_a$, $f_a$ and $z_u$, so $x \in H_f(u)$, with $\{ y : x^{-1} y \in \widehat{L}_0 \} = \Lambda_2$. Since $x_u$ stabilizes $\widehat{L}_0$, $(x x_u)^{-1} y = x_u^{-1} x^{-1} y \in \widehat{L}_0$ if and only if $x^{-1} y \in \widehat{L}_0$. So $\Lambda(x) = \Lambda_2$, and $\delta(\Lambda_2) = \Lambda$ with $\delta \in \operatorname{Stab}(F_u)$. $\square$

### The ties of a pair of words

The second theorem is about a family of lattices and flags indexed by *terms*. For each pair $(u, u')$ of indices the data give a finite set of terms $t$, a weight of each term, and a predicate that marks a term as relevant. A construction assigns to each term $t$ a lattice $\Lambda_t$ and two flags $F_t = (e_1, \dots, e_r, z)$ of norm $T_u$ and $F'_t = (e'_1, \dots, e'_r, z')$ of norm $T_{u'}$. Among other conditions, $\Lambda_t$ satisfies conditions 2 to 5 of a row lattice for $F_t$, and $z' \in \Lambda_t$.

**Definition 6.10.7 (Gram matrix and its sizes).** Write $(v_1, \dots, v_{r+1}) = (e_1, \dots, e_r, z)$ and $(v'_1, \dots, v'_{r+1}) = (e'_1, \dots, e'_r, z')$. The Gram matrix of the term $t$ is the $(r+1) \times (r+1)$ matrix $Z_t$ with $(Z_t)_{ab} = h(v'_b, v_a)$. For a square matrix $Z$ over $K$ and $l \geq 0$, $D_l(Z)$ is the determinant of the upper left $l \times l$ block, and $D_l(Z) = 0$ when $l$ is larger than the size. The data fix a finite set $\mathcal{T}$ of embeddings $\tau \colon K \to \mathbb{C}$. Let $d_K = |\operatorname{disc} K|^{1/[K : \mathbb{Q}]}$ be the root discriminant. Then
$$|D_l(Z)|^{\natural}_\tau = d_K^{-2 e(r, l)}\, |\tau(D_l(Z))|$$
for an exponent $e(r, l)$ that we did not unfold, and, for real numbers $T, T'$,
$$G(Z)_\tau = \big(|D_{r+1}(Z)|^{\natural}_\tau\big)^2 - T T' \big(|D_r(Z)|^{\natural}_\tau\big)^2 .$$
For $1 \leq a \leq r + 1$ let $\rho_a = d_K^{-(r + 1 - a)}$. Two matrices $Z, Z'$ are *equivalent* if $Z' = A Z B$ with $A$ lower triangular and $B$ upper triangular, both with entries in $\mathcal{O}_K$ and with ones on the diagonal.

**Theorem 6.10.8 (Ties).** Assume the setting comes with a full family that satisfies a finiteness condition, an isomorphism condition and a decay condition. Let $u, u'$ be indices, and let $\Lambda_t$, $F_t$, $F'_t$ and $Z_t$ be as above, with $G = G(\cdot)$ taken with $T = T_u$ and $T' = T_{u'}$. Then these three properties hold.

1. (Norm relation.) For every relevant term $t$ of nonzero weight, $1 \leq \prod_{\tau \in \mathcal{T}} G(Z_t)_\tau$, and $1 \leq \prod_{\tau} \big(|D_l(Z_t)|^{\natural}_\tau\big)^2$ for every $l \leq r + 1$ with $D_l(Z_t) \neq 0$.
2. (Determinant factorization.) For every term $t$ of nonzero weight,
$$\frac{N(\Lambda_t, F_t, F'_t)}{\mathcal{N}(g)^{r+1}} = g^{-mf} \prod_{\tau \in \mathcal{T}} G(Z_t)_\tau ,$$
where $m, f$ are integers of the data, $N(\Lambda_t, F_t, F'_t)$ is the determinant of a lattice built from $\Lambda_t$ and the two flags, and $\mathcal{N}(g)$ is a normalizing factor attached to $g$.
3. (Entries in a lattice.) For all $a, b \in \{1, \dots, r + 1\}$ there is an additive subgroup $\Lambda_{ab} \subseteq \mathbb{C}^{\mathcal{T}}$ such that $\prod_\tau |x_\tau| \geq 1$ for every nonzero $x \in \Lambda_{ab}$, and such that $\big(\rho_a \rho_b\, \tau(Z_{ab})\big)_{\tau \in \mathcal{T}} \in \Lambda_{ab}$ for every relevant term $t$ of nonzero weight and every matrix $Z$ equivalent to $Z_t$.

Lean: `Formalism.L2.SG.LoopsTies.tiesAt`

*Proof.* The three properties are proved separately. We did not open these proofs, so we give no argument here. $\square$

**Remark 6.10.9 (Formalization).** Row lattices are `IsRowLat` ([FlagEEqHyperbolic.lean](lean:Formalism/SharpRestriction/CuspSpanNormBounds/FlagEEqHyperbolic.lean#L99)), and the surjectivity statement is `LatSurj` ([FullExists.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/FullExists.lean#L245)). In the statement, $\Lambda(x)$ is only a set of vectors, so the theorem also asserts that it is the carrier of a submodule. The theorem ([LatDictFinal.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/LatDictFinal.lean#L14)) applies `lattice_surjective_of_orbit` to the orbit theorem. The three steps above follow its proof (LatDict.lean, line 1112). The splitting `IsSplitRow_holds` and the isometry `dltE` were read by their statements only. The orbit theorem is `ZOrbit`, which is stated for every coordinate datum of a Hermitian space, with its standard lattice; we state it in the setting. It is proved by `zOrbit_of_open` from `primitive_plane_local` and `adelic_gluing`, which we did not open. Conditions 4 and 6 together force $\mathfrak{d}$ to be prime to every $\mathfrak{P}$ that contains $g$: at such a prime, condition 4 gives $(\Lambda_X)_{\mathfrak{P}} = \sum_a \mathcal{O}_{K, \mathfrak{P}} e_a$. If the data allowed a common prime, no row lattice would exist and the theorem would be vacuous; we did not check where the data exclude this. The ties theorem ([LoopRowSB.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/LoopRowSB.lean#L41)) is the conjunction of `normTieC_holds`, `gram_determinant_relation` and `entryLatC_holds`, which we did not open. The lattice of a term is the structure field `abelian₂`, a name also used for unrelated objects in other files. We did not unfold the exponent $e(r, l)$, the determinant $N$, the factor $\mathcal{N}(g)$, the weights, the relevance predicate, or the construction `atOfW` and its hypotheses.

## Notes and references

The trace identity of the fourth section feeds the [weighted count over definite unitary groups](/entry/weighted-count-definite-unitary/) and the [trace identity](/entry/cnt-trace-definite-forms-identity/) of Volume 9. There a weighted sum over marked pairs is moved to a sum over definite pairs by the bijection of the first section, and the identity of the fourth section turns that sum into traces on definite unitary groups. Both results are used in the proof of [the Hodge property of the geometric part](/entry/ks-hodge-of-geo/), which enters the step [GeoOne](/step/geo-one-def/) of [the Galois row](/proof/galois-row/).

The fifth to seventh sections give the induction step for the mass of unimodular Hermitian lattices, which feeds the step [theta local matching](/step/theta-local-matching/). The eighth section gives the [level splitting](/entry/level-s-all-split/) used in the volume computations. The ninth section serves the [real object at infinity](/entry/real-obj-in-infinity-x-jsz/) and the [estimate at infinity](/entry/in-infinity-xat/). The tenth section is an input of the step [nonempty hypotheses](/step/nonempty-hyps/).

- M. Harris and R. Taylor, *The Geometry and Cohomology of Some Simple Shimura Varieties*, Annals of Mathematics Studies 151, Princeton University Press, 2001, Chapter V. The count of points on the Shimura varieties used here, and its comparison with the trace formula.
- R. Kottwitz, "Points on some Shimura varieties over finite fields", *J. Amer. Math. Soc.* 5 (1992), §19. The terms of the point count for unitary groups, indexed by rational classes.
- V. Platonov and A. Rapinchuk, *Algebraic Groups and Number Theory*, Academic Press, 1994, Chapter 5, §5.1, Theorem 5.1. The finiteness of class numbers, of which the finiteness theorem of the third section is a form. Chapter 8 treats class numbers and genera of algebraic groups.
- C. L. Siegel, "Über die analytische Theorie der quadratischen Formen", *Ann. of Math.* 36 (1935). The mass formula for quadratic forms, the model of the mass and the singular series of the seventh section.
- W. T. Gan, J. Hanke and J.-K. Yu, "On an exact mass formula of Shimura", *Duke Math. J.* 107 (2001). Exact mass formulas for unitary groups, in terms of local densities.
- G. B. Folland, *A Course in Abstract Harmonic Analysis*, CRC Press, 1995, Chapter 2, §2.4 and §2.6. The modular function and quotient measures on homogeneous spaces, used in the ninth section.
- A. W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples*, Princeton University Press, 1986, Chapter IX. Discrete series and the Schur orthogonality relations, used in the energy bound of the ninth section.
