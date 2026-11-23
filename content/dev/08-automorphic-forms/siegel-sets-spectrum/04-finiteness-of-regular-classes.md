---
title: Finiteness of regular classes
decls:
  - GlobalTheory.CompanionTheory.CFin.classes_finite
  - GlobalTheory.CompanionTheory.CFin.regClassFin
  - GlobalTheory.T.siegel_implies_regular_class_finite
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Finiteness of regular classes

The geometric side of the trace formula is a sum over conjugacy classes of rational elements. For a compactly supported test function $f$, only finitely many classes can contribute: a class contributes only if some conjugate of one of its elements lies in the support of $f$. This section proves this finiteness for the regular semisimple classes of a unitary group over a CM field, as a consequence of reduction theory. The result is used in the [direct computation of the elliptic side](/entry/elliptic-side-direct/) of the trace formula for unitary groups. For a compact quotient the same finiteness is the first step of [the trace formula for a compact quotient](/learn/trace-formula/#the-trace-formula-for-a-compact-quotient); here the quotient is not compact, and a Siegel set replaces the compact fundamental domain.

We keep the notation of the previous sections: $E/F$ is a CM extension, $J$ a nondegenerate Hermitian matrix, and $G(\mathbb{A})$ the adelic unitary group, with rational points $G(F)$.

**Definition 3.4.1 (Regular semisimple, rational conjugacy).** An element $\gamma \in G(F)$ is regular semisimple if the characteristic polynomial of $\gamma$, as an $n \times n$ matrix over $E$, is separable. Two elements $\gamma, \delta \in G(F)$ are conjugate if $\delta = \eta^{-1} \gamma \eta$ for some $\eta \in G(F)$. The conjugacy class of $\gamma$ is denoted $\mathfrak{o}_\gamma$.

A separable characteristic polynomial means $n$ distinct eigenvalues in an algebraic closure. The centralizer of such an element is then a maximal torus.

**Definition 3.4.2 (The Siegel package).** We say that the Siegel package holds if, for every CM extension $E/F$, every nondegenerate Hermitian $J$ and every Witt frame $(X, Y)$ of $J$, there are a compact subgroup $K$, a compact $\Omega \subseteq P^1$ and $c > 0$ with the following properties: $G(\mathbb{A}) = PK$; $K$ is in good position; $G(\mathbb{A}) = G(F)\, \mathfrak{S}(\Omega, c, K)$; the conjugates $a^{-1} p a$ with $p \in \Omega$ and $a$ in the cone lie in a fixed compact set; heights on the Siegel set satisfy $\operatorname{ht}(g) \le C \operatorname{ht}(\gamma g)^A$ for rational $\gamma$; and smooth cusp forms of moderate growth are rapidly decreasing on the Siegel set.

This is the package of the [chapter on finiteness](/entry/siegel-core/). The [section on Siegel domains](/entry/cov-main/) proves its covering clause.

We use the following facts, taken as given. Fix a Witt frame $(X, Y)$ of rank $r$, a complement frame $Z$ of the anisotropic part, and the basis $(X, Z, Y)$ of $E^n$; write matrices in this basis.

- (Stabilized flags.) Let $\Omega$, $c$, $K$ be as in the Siegel package and $C$ compact. There is $t_0$ such that: if $g = pak$ is in the Siegel set with torus coordinates $t$, and $\delta \in G(F)$ satisfies $g^{-1} \delta g \in C$, then $\delta$ maps $x_l$ into $\langle x_1, \dots, x_j \rangle$ for all $l \le j$, for every index $j$ with $t_j > t_0$ and $t_0\, t_{j+1} < t_j$. We call such indices deep (we use the threshold $\max(t_0, 1)$).
- (Weight ratios.) The deep indices cut the basis $(X, Z, Y)$ into blocks. There is $R$ such that, for $t$ in the cone, the weights of the torus on two basis vectors of the same block differ by a factor at most $R$.
- (Bounded denominators.) If the finite parts of a set of rational matrices lie in a compact set, then their entries in the basis $(X, Z, Y)$ have a common denominator $d$.
- (Regular elements in a parabolic.) A regular semisimple rational element that stabilizes the flags up to the deep indices is conjugate in $G(F)$ to the element whose matrix is its block diagonal part: the entries in the diagonal blocks are kept and the others are set to $0$.
- (Northcott.) For given $d$ and $B$ there are only finitely many matrices over $E$ whose entries $e$ satisfy: $de$ is an algebraic integer and $|\tau(e)| \le B$ for every complex embedding $\tau$.

**Theorem 3.4.3 (Finitely many regular classes meet a compact set).** Assume the Siegel package. Let $E/F$ be a CM extension, $J$ Hermitian and nondegenerate, and $C \subseteq G(\mathbb{A})$ compact. Then the set of regular semisimple conjugacy classes $\mathfrak{o}$ in $G(F)$ such that
$$x^{-1} \delta x \in C \quad \text{for some } x \in G(\mathbb{A}) \text{ and some } \delta \in \mathfrak{o}$$
is finite.

Lean: `GlobalTheory.CompanionTheory.CFin.classes_finite`.

*Proof.* Choose a Witt frame $(X, Y)$ and a complement frame, and take $K$, $\Omega$, $c$ from the Siegel package. Let $C_1 = \{k y k^{-1} : k \in K, y \in C\}$, a compact set. Take $t_0$, $R$ from the facts on stabilized flags and weight ratios.

Let $\mathfrak{o}$ be a class as in the theorem, with $\delta \in \mathfrak{o}$ and $x^{-1}\delta x \in C$. By the covering, $x = \eta\, p a k$ with $\eta \in G(F)$ and $pak$ in the Siegel set. Put $\delta_1 = \eta^{-1} \delta \eta$. It lies in $\mathfrak{o}$, and $(pak)^{-1} \delta_1 (pak) \in C$. By the fact on stabilized flags, $\delta_1$ stabilizes the flag up to every deep index. It is regular semisimple, because it is conjugate to an element of $\mathfrak{o}$. So it is conjugate in $G(F)$ to the element $\delta'$ whose matrix is the block diagonal part of the matrix of $\delta_1$. Every entry of $\delta'$ is $0$ or an entry of $\delta_1$ in a diagonal block.

Now bound these entries. Write $y = (pak)^{-1}\delta_1 (pak) \in C$. The finite part of $\delta_1$ is the finite part of $p\,(k y k^{-1})\, p^{-1}$, since $a$ is archimedean. So it lies in the compact set $\mathcal{C}$ of finite parts of $\{p z p^{-1} : p \in \Omega, z \in C_1\}$. By bounded denominators, the entries of $\delta_1$, and so those of $\delta'$, have a common denominator $d$ that depends only on $\mathcal{C}$. At the archimedean places, $\delta_1 = pa (k y k^{-1}) a^{-1} p^{-1}$. In the blocks that are kept, the conjugation by $a$ multiplies an entry by a ratio of torus weights on the same block, and these ratios are at most $R$. The entries of $p$ and of $k y k^{-1}$ are bounded on the compact sets $\Omega$ and $C_1$. So $|\tau(e)| \le B$ for every entry $e$ of $\delta'$ and every complex embedding $\tau$, with $B$ depending only on $\Omega$, $C_1$ and $R$.

By Northcott's finiteness, $\delta'$ lies in a finite set of matrices that depends only on $C$. Each class $\mathfrak{o}$ contains such a $\delta'$, so there are finitely many classes. $\square$

**Theorem 3.4.4 (Regular classes in the support of a test function).** Assume the Siegel package. Let $E/F$ be a CM extension and $V$ a Hermitian space over $E$, with adelic unitary group $G(\mathbb{A})$. Let $f$ be a continuous function on $G(\mathbb{A})$ with compact support. Then the set of regular semisimple conjugacy classes $\mathfrak{o}$ of $G(F)$ for which
$$f(x^{-1} \delta x) \neq 0 \quad \text{for some } x \in G(\mathbb{A}) \text{ and some } \delta \in \mathfrak{o}$$
is finite.

Lean: `GlobalTheory.CompanionTheory.CFin.regClassFin` (also `GlobalTheory.T.siegel_implies_regular_class_finite`, a second name).

*Proof.* The Gram matrix of $V$ is Hermitian and nondegenerate over the CM extension. If $f(x^{-1}\delta x) \neq 0$ then $x^{-1}\delta x$ lies in the support of $f$, which is compact. Apply the [theorem above](/entry/classes-finite/) with $C$ the support of $f$. $\square$

So in the geometric side
$$\sum_{\mathfrak{o}} \int_{G(F)\backslash G(\mathbb{A})} \sum_{\delta \in \mathfrak{o}} f(x^{-1}\delta x)\, dx,$$
restricted to regular semisimple classes, only finitely many terms are nonzero.

**Remark 3.4.5 (Formalization).** The proof uses only four clauses of the Siegel package: $K$, $\Omega$, $c$ and the covering. The Iwasawa decomposition, good position, the compact conjugates, the height bound and the decay of cusp forms are discarded with `-` in [SiegelImpliesRegularClassFinite.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/SiegelImpliesRegularClassFinite.lean#L364). The facts listed before the first theorem are the statements `GlobalTheory.T.siegel_compact_translate_bound`, `deep_cone_weight_ratio_bound`, `compact_finite_rational_denominator`, `bounded_integral_matrices_finite`, `exists_witt_complement_frame` and `rational_points_eq_embedding`. The conjugation to block diagonal form and the archimedean bound are lemmas of the same file (`exists_conj_levi`, `arch_bound`); they rest on `GlobalTheory.T.regular_semisimple_flag_stabilizer` and on frame criteria of the form `GlobalTheory.T.*`, and are only summarized above. The test function in the second theorem is a member of the space `CcGA V`, from which the proof uses only continuity and compact support.
