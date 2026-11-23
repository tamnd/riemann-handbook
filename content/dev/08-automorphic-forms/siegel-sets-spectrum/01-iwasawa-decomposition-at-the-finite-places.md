---
title: Iwasawa decomposition at the finite places
decls:
  - GlobalTheory.T.unitary_adelic_iwasawa_compact
  - GlobalTheory.CompanionTheory.KFin.exists_compact_iwasawa_good
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Iwasawa decomposition at the finite places

The first sections of this chapter build Siegel sets for a unitary group over a CM field and prove that their rational translates cover the adelic group. This is the reduction theory of Borel and Harish-Chandra, here done by hand for unitary groups; see [arithmetic subgroups and Siegel sets](/learn/trace-formula/#arithmetic-subgroups-and-siegel-sets). A Siegel set is a product $\Omega A_c K$ of a compact piece of a minimal parabolic subgroup, a cone in a split torus and a compact subgroup. This section fixes the notation and constructs the compact subgroup at the finite places: a compact open subgroup $K_f$ such that every finite adelic point is a parabolic element times an element of $K_f$, and such that the parabolic elements of $K_f$ split into a Levi part and a unipotent part inside $K_f$. The result is used in the step [EveryCharacter](/step/every-character/).

**Definition 3.1.1 (CM extension and Hermitian matrix).** Let $F$ be a totally real number field and $E/F$ a totally imaginary quadratic extension, with nontrivial automorphism $\sigma$ over $F$; we write $\bar z = \sigma(z)$. For a matrix $X$ over $E$ (or over an $E$-algebra) let $X^* = \bar X^{T}$. A matrix $J \in M_n(E)$ is Hermitian and nondegenerate if $J^* = J$ and $\det J \neq 0$. It defines the Hermitian form $h(z, w) = z^* J w$ on $E^n$.

The [Hermitian forms](/learn/algebra/#hermitian-and-skew-hermitian-forms) of this kind are the forms that define unitary groups over $F$.

**Definition 3.1.2 (Adelic unitary group).** Let $\mathbb{A}$ be the adele ring of $F$ and $\mathbb{A}_E = \mathbb{A} \otimes_F E$. The adelic unitary group of $J$ is
$$G(\mathbb{A}) = \{ g \in \mathrm{GL}_n(\mathbb{A}_E) : g^* J g = J \},$$
with its locally compact topology. It contains the rational points $G(F) = G(\mathbb{A}) \cap \mathrm{GL}_n(E)$. Write $G(\mathbb{A}) = G_\infty \times G(\mathbb{A}_f)$ for the splitting into the archimedean part and the finite part. We call $g$ a finite point if its archimedean part is $1$, and an archimedean point if its finite part is $1$.

**Definition 3.1.3 (Witt frame).** Let $r \ge 0$. A Witt frame of rank $r$ for $J$ is a pair of matrices $X, Y \in M_{n \times r}(E)$ such that
$$X^* J X = 0, \qquad Y^* J Y = 0, \qquad X^* J Y = 1_r,$$
and such that $h$ is anisotropic on the complement $V_0 = \{ z : X^* J z = 0 \text{ and } Y^* J z = 0 \}$: if $z \in V_0$ and $h(z, z) = 0$ then $z = 0$.

The columns $x_1, \dots, x_r$ of $X$ span a maximal isotropic subspace, the columns $y_1, \dots, y_r$ of $Y$ span a dual isotropic subspace, and $E^n = \langle X \rangle \oplus \langle Y \rangle \oplus V_0$. So $r$ is the Witt index of $h$, and the frame is the unitary analogue of a hyperbolic basis.

**Definition 3.1.4 (Minimal parabolic, Levi and unipotent parts).** Fix a Witt frame $(X, Y)$ of rank $r$. Put:

- $P$, the set of $p \in G(\mathbb{A})$ with $pX = XB$ for an upper triangular $B \in M_r(\mathbb{A}_E)$. This is the stabilizer of the isotropic flag $\langle x_1 \rangle \subset \langle x_1, x_2 \rangle \subset \cdots$.
- $P^1$, the set of $p \in P$ for which each diagonal entry $B_{ii}$ is a unit of $\mathbb{A}_E$ with adelic absolute value $1$.
- $M$, the set of $m \in G(\mathbb{A})$ with $mX = X \operatorname{diag}(d)$ and $mY = Y \operatorname{diag}(d')$ for some $d, d' \in \mathbb{A}_E^r$.
- $N$, the set of $u \in G(\mathbb{A})$ with $uX = XB$ for an upper triangular $B$ with $B_{ii} = 1$, and with $(u - 1)z \in \langle X \rangle_{\mathbb{A}_E}$ for every $z \in E^n$ with $X^* J z = 0$.

Then $P$ is the adelic points of a minimal parabolic subgroup, $M$ is its Levi subgroup (a product of $r$ copies of $\mathrm{Res}_{E/F}\mathbb{G}_m$ and the anisotropic group $U(V_0)$), and $N$ is its unipotent radical. The group $P^1$ is the part of $P$ on which every character $|B_{ii}|$ is trivial. It is the analogue of the group $P(\mathbb{A})^1$ of [arithmetic subgroups and Siegel sets](/learn/trace-formula/#arithmetic-subgroups-and-siegel-sets).

**Definition 3.1.5 (Good position).** A subgroup $K \subseteq G(\mathbb{A})$ is in good position for the frame $(X, Y)$ if every $p \in P \cap K$ can be written $p = mu$ with $m \in M \cap K$ and $u \in N \cap K$.

For a maximal compact subgroup in good position relative to a minimal parabolic, this is the classical fact that $P \cap K = (M \cap K)(N \cap K)$.

**Theorem 3.1.6 (Iwasawa decomposition at the finite places).** Let $E/F$ be a CM extension, $J \in M_n(E)$ Hermitian and nondegenerate, and $(X, Y)$ a Witt frame of rank $r$ for $J$. Then there is a compact subgroup $K_f$ of $G(\mathbb{A})$ such that:

1. every element of $K_f$ is a finite point;
2. every finite point $g$ can be written $g = pk$ with $p \in P$, $p$ a finite point, and $k \in K_f$;
3. $K_f$ is in good position for $(X, Y)$.

Lean: `GlobalTheory.CompanionTheory.KFin.exists_compact_iwasawa_good` (also `GlobalTheory.T.unitary_adelic_iwasawa_compact`, a second name).

The proof uses lattices. We take the following local and global facts as given; they are the standard theory of [lattices in Hermitian spaces](/learn/hermitian-lattices/#lattices-in-quadratic-and-hermitian-spaces).

- At each finite place $v$ of $F$ there is a maximal even lattice $\Lambda_v \subset E_v^n$ that is adapted to the frame $(X, Y)$.
- There is a global lattice $L_0$ whose completion $L_{0,v}$ is maximal even and adapted for almost all $v$.
- The stabilizer in $G(F_v)$ of a maximal even lattice is compact.
- The stabilizer of a maximal even adapted lattice acts transitively on the isotropic flags of the frame. So every $g_v \in G(F_v)$ is $p_v k_v$, with $p_v$ upper triangular on $X$ and $k_v$ in the stabilizer.
- An element of $P$ is the product of a Levi part $m \in M$ and an element of $N$, where $m$ is given by the diagonal blocks of $p$ in the frame. If $p_v$ stabilizes an adapted maximal even lattice $\Lambda_v$, then so does the Levi part $m_v$, since $\Lambda_v$ has a basis adapted to the frame.

*Proof.* At each finite place $v$ choose $\Lambda_v$ maximal even and adapted. If $L_{0,v}$ is maximal even and adapted, choose $\Lambda_v = L_{0,v}$. Then $\Lambda_v = L_{0,v}$ for almost all $v$. Let $K_f$ be the group of finite points $g$ with $g_v \Lambda_v = \Lambda_v$ for every $v$.

Compactness. Let $S$ be the finite set of $v$ with $\Lambda_v \neq L_{0,v}$. The group $G(\mathbb{A}_f)$ is the restricted product of the $G(F_v)$ with respect to the stabilizers of $L_{0,v}$. In it, $K_f$ is the product of the stabilizers of $\Lambda_v$ for $v \in S$ and of $L_{0,v}$ for $v \notin S$. Each factor is compact, so the product is compact by Tychonoff, and it is compact in the restricted product topology.

Decomposition. Let $g$ be a finite point. Since $g_v$ stabilizes $L_{0,v}$ for almost all $v$, the set $S_g$ of places where $g_v$ does not stabilize $\Lambda_v$ is finite. At $v \in S_g$ write $g_v = p_v k_v$ by flag transitivity. Let $p$ be the finite point with component $p_v$ at $v \in S_g$ and $1$ elsewhere. Then $p \in P$, because each component is upper triangular on $X$. The element $k = p^{-1} g$ has component $k_v$ at $v \in S_g$ and $g_v$ elsewhere, so it stabilizes every $\Lambda_v$, and $k \in K_f$.

Good position. Let $p \in P \cap K_f$ and let $m$ be its Levi part, so that $u = m^{-1} p \in N$. The archimedean part of $p$ is $1$. The Levi part is computed blockwise from the matrix of $p$, so the archimedean part of $m$ is also $1$, and $m$ is a finite point. At each $v$, $p_v$ stabilizes $\Lambda_v$, so $m_v$ stabilizes $\Lambda_v$. Hence $m \in K_f$, and $u = m^{-1}p \in K_f$. $\square$

The theorem gives the finite half of an Iwasawa decomposition $G(\mathbb{A}) = P K$. At the archimedean places $G_\infty$ is a product of compact unitary groups and of noncompact groups $U(p, q)$, and the archimedean decomposition is a separate input. In the [section on Siegel domains](/entry/red-cov-step/) both are used.

**Remark 3.1.7 (Formalization).** The conclusion covers finite points only: the Lean statement asks that $K_f$ lie in the finite points and gives $g = pk$ only for finite $g$. The full decomposition of $G(\mathbb{A})$ is a separate statement, `GlobalTheory.T.unitary_adelic_iwasawa`, with no good position clause. The local lattice facts listed above are statements of the form `GlobalTheory.T.*` (for example `lattice_max_even_almost_all`, `lattice_stabilizer_compact`, `max_even_lattice_flag_transitive_local`, `max_even_lattice_adapted_basis`); see [UnitaryAdelicIwasawaCompact.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/UnitaryAdelicIwasawaCompact.lean#L58).
