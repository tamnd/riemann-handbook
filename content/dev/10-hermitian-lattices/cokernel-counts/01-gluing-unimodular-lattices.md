---
title: Gluing unimodular lattices
decls:
  - Formalism.L2.SG.Pf.Cnt.alpha_discriminant_holds
  - Formalism.L2.SG.Pf.Cnt.gluing_product_holds
  - Formalism.L2.SG.Pf.Cnt.gluing_mass_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Gluing unimodular lattices

Let $V$ be a Hermitian space over a CM field and $U \subseteq V$ a subspace with $V = U \oplus U^\perp$. A unimodular lattice $\Lambda$ in $V$ meets $U$ in a lattice $M$ and $U^\perp$ in a lattice $T$, and $\Lambda$ is glued from $M$ and $T$ along their discriminant modules. This section counts the unimodular lattices with a given intersection $M$, first at each prime and then globally. The main result is a mass formula: the sum of $1/|\mathrm{Stab}(\Lambda)|$ over the classes of such $\Lambda$ is a mass constant times an explicit product of local factors. It is one of the inputs of the step [HypsAlt is nonempty](/step/nonempty-hyps/), where the counts of lattices by their cokernels are turned into explicit constants.

**Definition 8.1.1 (CM field unramified over its real subfield).** Let $K$ be a number field with an involution $x \mapsto \bar{x}$ and let $F$ be its fixed field. We say that $K$ is *CM and unramified* if $K$ is totally complex, the involution is complex conjugation under every embedding $K \to \mathbb{C}$, and for every maximal ideal $P$ of $\mathcal{O}_K$ there is $\theta \in \mathcal{O}_K$ with $\theta - \bar{\theta} \notin P$. The last condition says that $K/F$ is unramified at every finite prime.

Throughout this section $K/F$ is CM and unramified, $V$ is a finite-dimensional $K$-vector space and $h \colon V \times V \to K$ is a Hermitian form: $h$ is conjugate-linear in the first variable, linear in the second, and $h(y, x) = \overline{h(x, y)}$ ([Hermitian forms](/learn/algebra/#hermitian-and-skew-hermitian-forms)). For a maximal ideal $\mathfrak{p}$ of $\mathcal{O}_F$ we write $L_\mathfrak{p}$ for the localization of an $\mathcal{O}_K$-module $L$ at $\mathcal{O}_F \setminus \mathfrak{p}$, $N\mathfrak{p}$ for the norm of $\mathfrak{p}$ and $v_\mathfrak{p}$ for the $\mathfrak{p}$-adic valuation on $\mathcal{O}_F$.

**Definition 8.1.2 (Lattices, duals, discriminant modules).** Let $X \subseteq V$ be a subspace. A *lattice in $X$* is a finitely generated $\mathcal{O}_K$-submodule $L \subseteq X$ that spans $X$ over $K$. It is *integral* if $h(L, L) \subseteq \mathcal{O}_K$. Its dual in $X$ is $L^\#_X = X \cap \{ y \in V : h(L, y) \subseteq \mathcal{O}_K \}$. A lattice $\Lambda$ in $V$ is *unimodular* if $\Lambda^\#_V = \Lambda$. For an integral lattice $L$ in $X$, the *discriminant module* at $\mathfrak{p}$ is the finite $\mathcal{O}_K$-module
$$\Delta_\mathfrak{p}(X, L) = (L^\#_X)_\mathfrak{p} / L_\mathfrak{p}.$$
We write $a_\mathfrak{p}(X, L)$ for the number of $\mathcal{O}_K$-linear endomorphisms $P$ of $\Delta_\mathfrak{p}(X, L)$ that preserve the form modulo $\mathcal{O}_{K,\mathfrak{p}}$: if $P$ sends the classes of $x, y$ to the classes of $x', y'$, then $h(x', y') - h(x, y) \in \mathcal{O}_{K,\mathfrak{p}}$.

The discriminant module is the obstruction to unimodularity: $L$ is unimodular at $\mathfrak{p}$ if and only if $\Delta_\mathfrak{p}(X, L) = 0$. When $V = U \oplus U^\perp$ and $\Lambda$ is unimodular, the two projections identify $\Delta_\mathfrak{p}(U, \Lambda \cap U)$ with $\Delta_\mathfrak{p}(U^\perp, \Lambda \cap U^\perp)$, up to a sign of the form. This is the classical picture of gluing (Nikulin, §1.5, for $\mathbb{Z}$-lattices).

**Definition 8.1.3 (Jordan basis).** Let $L$ be a lattice in $X$ and $\mathfrak{p}$ a maximal ideal of $\mathcal{O}_F$. A *Jordan basis* of $L$ at $\mathfrak{p}$ is a family $b = (b_1, \dots, b_m)$ in $X$ with $\mathcal{O}_{K,\mathfrak{p}}$-span equal to $L_\mathfrak{p}$, with $h(b_i, b_j) = 0$ for $i \neq j$, and with $a_i = h(b_i, b_i)$ a nonzero element of $\mathcal{O}_F$. For such $a = (a_i)$ put
$$c_\mathfrak{p}(a) = \#\{ i : v_\mathfrak{p}(a_i) \neq 0 \}, \qquad v_\mathfrak{p}(a) = \sum_i v_\mathfrak{p}(a_i).$$
Let $c_\mathfrak{p}(X, L)$ and $v_\mathfrak{p}(X, L)$ be the least values of $c_\mathfrak{p}(a)$ and $v_\mathfrak{p}(a)$ over all Jordan bases. Put $n(M) = \prod_\mathfrak{p} N\mathfrak{p}^{v_\mathfrak{p}(U, M)}$.

Since $K/F$ is unramified, a Hermitian lattice over $\mathcal{O}_{K,\mathfrak{p}}$ has an orthogonal basis. This is the content of the first lemma.

**Lemma 8.1.4 (Jordan bases).** (a) Let $X \subseteq V$ be a subspace on which $h$ is nondegenerate and let $L$ be an integral lattice in $X$. Then $L$ has a Jordan basis at every maximal ideal $\mathfrak{p}$ of $\mathcal{O}_F$. (b) If $L$ is a lattice in $V$ and $(b, a)$ is a Jordan basis of $L$ at $\mathfrak{p}$, then the $\mathfrak{p}$-valuation of the discriminant ideal of $L$ is $v_\mathfrak{p}(a)$.

Lean: `Formalism.L2.SG.Pf.Cnt.jordan_splitting_exists`.

**Lemma 8.1.5 (Jordan invariants).** Let $L$ and $L'$ be lattices in subspaces $X \subseteq V$ and $X' \subseteq V'$ of two Hermitian spaces, with Jordan bases $(b, a)$ and $(b', a')$ at $\mathfrak{p}$. If $\Delta_\mathfrak{p}(X, L) \cong \Delta_\mathfrak{p}(X', L')$ as $\mathcal{O}_K$-modules, then $\sum_i \min(v_\mathfrak{p}(a_i), j) = \sum_i \min(v_\mathfrak{p}(a'_i), j)$ for every $j \geq 0$.

Lean: `Formalism.L2.SG.Pf.Cnt.jordan_invariants_holds`.

The numbers $\sum_i \min(v_\mathfrak{p}(a_i), j)$ for $j \geq 0$ determine the multiset of the nonzero valuations $v_\mathfrak{p}(a_i)$, and the elementary divisors of the discriminant module are these valuations. So the lemma says that the discriminant module determines the nonzero part of the Jordan type.

**Lemma 8.1.6 (Jordan isometry).** Let $h$ be totally positive definite, let $L, L'$ be lattices in $V$ with Jordan bases $(b, a)$ and $(b', a')$ at $\mathfrak{p}$, and assume $v_\mathfrak{p}(a_i) = v_\mathfrak{p}(a'_i)$ for all $i$. Then some isometry $g$ of $(V, h)$ satisfies $g(L_\mathfrak{p}) = L'_\mathfrak{p}$.

Lean: `Formalism.L2.SG.Pf.Cnt.jordan_isometry_holds`.

**Definition 8.1.7 (Local densities).** Let $L$ be a lattice in $V$, $n = \dim_K V$. Let $A_k(L)$ be the number of $\mathcal{O}_K$-linear endomorphisms of $L/\mathfrak{p}^k L$ that preserve $h$ modulo $\mathfrak{p}^k$. The *local density* of $L$ at $\mathfrak{p}$ is $\alpha_\mathfrak{p}(L) = \lim_k A_k(L)/N\mathfrak{p}^{k n^2}$. Let $\eta_\mathfrak{p} = -1$ if $\mathfrak{p}$ is inert in $K$ and $\eta_\mathfrak{p} = 1$ otherwise, and put
$$\alpha^{\mathrm{std}}_\mathfrak{p}(m) = \prod_{j=1}^{m} \bigl(1 - \eta_\mathfrak{p}^{j} N\mathfrak{p}^{-j}\bigr).$$

This is the local density of [Volume 1](/learn/groups/#hermitian-lattices-and-the-mass-formula) for $S = T$, written with endomorphisms of $L$. For a unimodular lattice of rank $m$ the density is $\alpha^{\mathrm{std}}_\mathfrak{p}(m)$, the order of $\mathrm{U}_m$ over the residue field divided by $N\mathfrak{p}^{m^2}$.

**Theorem 8.1.8 (Density and discriminant).** Let $h$ be totally positive definite, let $L$ be an integral lattice in $V$ and let $(b, a)$ be a Jordan basis of $L$ at $\mathfrak{p}$. Then
$$\alpha_\mathfrak{p}(L) = a_\mathfrak{p}(V, L) \cdot \alpha^{\mathrm{std}}_\mathfrak{p}\bigl(n - c_\mathfrak{p}(a)\bigr).$$

Lean: `Formalism.L2.SG.Pf.Cnt.alpha_discriminant_holds`.

*Proof.* Take $k \geq 2 v_\mathfrak{p}(a) + 1$. Two facts hold for such $k$. First, $a_\mathfrak{p}(V, L)$ equals the size of an explicit set of matrices built from the diagonal entries $a_i$ modulo $\mathfrak{p}^k$; this is a model computation for the diagonal form $\mathrm{diag}(a_1, \dots, a_n)$. Second, from this model, $A_k(L)$ is the product of $a_\mathfrak{p}(V, L)$ and the size of a kernel set that depends only on $a$ and $k$: an endomorphism of $L/\mathfrak{p}^k L$ that preserves $h$ is given by its action on the discriminant module and an element of this kernel. Divide by $N\mathfrak{p}^{k n^2}$ and let $k \to \infty$. The kernel count tends to the density of the unimodular part, which has rank $n - c_\mathfrak{p}(a)$, and that density is $\alpha^{\mathrm{std}}_\mathfrak{p}(n - c_\mathfrak{p}(a))$. $\square$

**Definition 8.1.9 (Gluing set and local fibre counts).** Let $h$ be nondegenerate and let $U \subseteq V$ be a subspace with $V = U \oplus U^\perp$. Let $M$ be a lattice in $U$ and $T$ a lattice in $U^\perp$. The *gluing set* $\mathcal{G}(U, M)$ is the set of unimodular lattices $\Lambda$ in $V$ with $\Lambda \cap U = M$. The *local fibre count* $f_\mathfrak{p}(M, T)$ is the number of $\mathcal{O}_{K,\mathfrak{p}}$-lattices $\Lambda$ that are localizations of lattices in $V$, are self-dual at $\mathfrak{p}$, and satisfy $\Lambda \cap U = M_\mathfrak{p}$ and $\Lambda \cap U^\perp = T_\mathfrak{p}$. Let $\mathrm{U}(V, U)$ be the group of isometries of $V$ that fix $U$ pointwise, and $\mathrm{Stab}_U(\Lambda)$ its subgroup of elements $g$ with $g \Lambda = \Lambda$. Two lattices $T, T'$ in $U^\perp$ are in the same *$U$-genus* if for every $\mathfrak{p}$ some $g \in \mathrm{U}(V, U)$ maps $T_\mathfrak{p}$ to $T'_\mathfrak{p}$.

**Lemma 8.1.10 (Local gluing).** Let $h$ be nondegenerate, $V = U \oplus U^\perp$, $M$ a lattice in $U$ and $T$ a lattice in $U^\perp$. If $f_\mathfrak{p}(M, T) \neq 0$, then $\Delta_\mathfrak{p}(U, M) \cong \Delta_\mathfrak{p}(U^\perp, T)$ and $f_\mathfrak{p}(M, T) = a_\mathfrak{p}(U^\perp, T)$. For every $g \in \mathrm{U}(V, U)$, $f_\mathfrak{p}(M, gT) = f_\mathfrak{p}(M, T)$.

Lean: `Formalism.L2.SG.Pf.Cnt.local_gluing_holds`.

The local self-dual lattices with the given intersections are the graphs of the anti-isometries between the two discriminant modules. Once one such graph exists, the others are its compositions with the form-preserving endomorphisms of $\Delta_\mathfrak{p}(U^\perp, T)$, and so there are $a_\mathfrak{p}(U^\perp, T)$ of them.

**Theorem 8.1.11 (Gluing product).** Let $h$ be nondegenerate, $V = U \oplus U^\perp$ with $h$ positive definite on $U^\perp$, $M$ a lattice in $U$ and $\Lambda_0 \in \mathcal{G}(U, M)$. Let $T$ be a lattice in $U^\perp$. Then:

1. $f_\mathfrak{p}(M, T) \neq 0$ for every $\mathfrak{p}$ if and only if $T$ is in the $U$-genus of $\Lambda_0 \cap U^\perp$;
2. the number of $\Lambda \in \mathcal{G}(U, M)$ with $\Lambda \cap U^\perp = T$ is $\prod_\mathfrak{p} f_\mathfrak{p}(M, T)$.

Lean: `Formalism.L2.SG.Pf.Cnt.gluing_product_holds`.

*Proof.* A lattice in $V$ is determined by its localizations, and every family of localizations that agrees with one lattice at almost all primes comes from a lattice. So the lattices $\Lambda$ of part 2 correspond to the families $(\Lambda_\mathfrak{p})$ of local lattices counted by the $f_\mathfrak{p}(M, T)$; at almost all primes $M$ and $T$ are unimodular and $f_\mathfrak{p} = 1$. This gives part 2. For part 1, if $T$ is in the $U$-genus of $T_0 = \Lambda_0 \cap U^\perp$, then $f_\mathfrak{p}(M, T) = f_\mathfrak{p}(M, T_0) \geq 1$ by the invariance in the Lemma (Local gluing). Conversely, if all $f_\mathfrak{p}(M, T)$ are nonzero, then $\Delta_\mathfrak{p}(U^\perp, T) \cong \Delta_\mathfrak{p}(U, M) \cong \Delta_\mathfrak{p}(U^\perp, T_0)$ by the same lemma. By the Lemma (Jordan invariants) $T$ and $T_0$ have the same nonzero Jordan valuations at $\mathfrak{p}$, and the zero valuations fill the rest. The Lemma (Jordan isometry), applied to $h$ on $U^\perp$ and extended by the identity on $U$, gives an element of $\mathrm{U}(V, U)$ that maps $(T_0)_\mathfrak{p}$ to $T_\mathfrak{p}$. $\square$

**Definition 8.1.12 (Mass constant).** Let $m \geq 1$ and $c \in \mathbb{R}$. For a lattice $L$ of rank $m$ with discriminant valuations $v_\mathfrak{p}(L)$ put
$$\lambda(L) = \prod_\mathfrak{p} \frac{\alpha^{\mathrm{std}}_\mathfrak{p}(m) \, N\mathfrak{p}^{m v_\mathfrak{p}(L)}}{\alpha_\mathfrak{p}(L)}.$$
We say that *$c$ is a mass constant for $(K, F, m)$* if for every totally positive definite Hermitian space $W$ of dimension $m$ and every integral lattice $L$ in $W$, the mass of the genus of $L$ equals $c \, \lambda(L)$.

This is the form of the Siegel mass formula in [Volume 1](/learn/groups/#hermitian-lattices-and-the-mass-formula), with all the archimedean and global factors gathered into $c$. A mass constant need not exist for a given $c$; the next theorem takes one as a hypothesis.

**Theorem 8.1.13 (Gluing mass formula).** Let $h$ be nondegenerate, $V = U \oplus U^\perp$ with $h$ positive definite on $U^\perp$, and $m = \dim U^\perp$. Let $M$ be an integral lattice in $U$ with $\mathcal{G}(U, M)$ nonempty, and let $c$ be a mass constant for $(K, F, m)$. Then there is a finite set $S \subseteq \mathcal{G}(U, M)$ that meets each $\mathrm{U}(V, U)$-orbit in $\mathcal{G}(U, M)$ exactly once, each $\mathrm{Stab}_U(\Lambda)$ for $\Lambda \in S$ is finite, and
$$\sum_{\Lambda \in S} \frac{1}{|\mathrm{Stab}_U(\Lambda)|} = c \, n(M)^m \prod_\mathfrak{p} \frac{\alpha^{\mathrm{std}}_\mathfrak{p}(m)}{\alpha^{\mathrm{std}}_\mathfrak{p}\bigl(m - c_\mathfrak{p}(U, M)\bigr)}.$$

Lean: `Formalism.L2.SG.Pf.Cnt.gluing_mass_holds`.

*Proof.* Let $T_0 = \Lambda_0 \cap U^\perp$ for some $\Lambda_0 \in \mathcal{G}(U, M)$. Group the $\Lambda \in \mathcal{G}(U, M)$ by $T = \Lambda \cap U^\perp$. By the [Theorem (Gluing product)](/entry/gluing-product-holds/), the lattices $T$ that occur are those in the $U$-genus of $T_0$, and each occurs for $\prod_\mathfrak{p} f_\mathfrak{p}(M, T) = \prod_\mathfrak{p} a_\mathfrak{p}(U^\perp, T)$ lattices $\Lambda$. The group $\mathrm{U}(V, U)$ is the isometry group of $U^\perp$, and the stabilizer of $T$ acts on these $\Lambda$ with stabilizers $\mathrm{Stab}_U(\Lambda)$. Counting orbits with weights gives
$$\sum_{\Lambda \in S} \frac{1}{|\mathrm{Stab}_U(\Lambda)|} = \sum_{[T]} \frac{\prod_\mathfrak{p} a_\mathfrak{p}(U^\perp, T)}{|\mathrm{Stab}(T)|},$$
the sum over the classes in the genus of $T_0$. The numerator is constant on the genus, so the right side is $\prod_\mathfrak{p} a_\mathfrak{p}(U^\perp, T_0)$ times the mass of $T_0$, and the mass is $c \, \lambda(T_0)$. By the [Theorem (Density and discriminant)](/entry/alpha-discriminant-holds/) applied to $T_0$ with a Jordan basis $a$, the factor $a_\mathfrak{p}$ cancels against $\alpha_\mathfrak{p}(T_0)$ in $\lambda(T_0)$, which leaves $\alpha^{\mathrm{std}}_\mathfrak{p}(m) N\mathfrak{p}^{m v_\mathfrak{p}(T_0)} / \alpha^{\mathrm{std}}_\mathfrak{p}(m - c_\mathfrak{p}(a))$. The discriminant modules of $T_0$ and $M$ are isomorphic, so by the Lemma (Jordan invariants) and the Lemma (Jordan bases) the numbers $v_\mathfrak{p}$ and $c_\mathfrak{p}$ for $T_0$ agree with those for $M$. The product of the factors $N\mathfrak{p}^{m v_\mathfrak{p}}$ is $n(M)^m$. $\square$

**Remark 8.1.14 (Formalization).** The mass formula is proved from the gluing product, the density formula, the local gluing lemma and the two Jordan lemmas, through an intermediate statement on the mass of the $U$-genus of $T$ ([NondegenerateOnOrthCompl.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/NondegenerateOnOrthCompl.lean#L16)). The proof of the density formula passes through two inputs, the model count of the discriminant automorphisms and the factorization of $A_k(L)$ for $k \geq 2 v_\mathfrak{p}(a) + 1$; we read their statements but not their proofs. In the gluing mass formula the mass constant $c$ is a hypothesis, so the theorem is only as strong as the mass formula that supplies $c$. The infinite products are `tprod` over all maximal ideals, which is $1$ by convention when the product does not converge; the factors are $1$ at almost all primes, so this does not arise.
