---
title: Uniqueness of Whittaker functionals
decls:
  - GroundTheory.Automorphic.Whittaker.rank_whittaker_le_one_of_contragredient
  - GroundTheory.Automorphic.ContragredientTranspose.nonempty_equiv_contragredient
  - GroundTheory.Automorphic.ContragredientTranspose.rank_whittaker_le_one
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Uniqueness of Whittaker functionals

This section proves that an irreducible admissible representation of $\mathrm{GL}_n(F)$ has at most one Whittaker functional up to a scalar. The proof has two parts. The first part uses the criterion of [Corollary 4.1.8](/entry/bi-equivariant-sigma-invariant-gl/) and proves the bound when the contragredient is also generic. The second part proves that the contragredient is the twist of $\pi$ by the transpose inverse, so that the contragredient is generic when $\pi$ is. The result is used in the step [EveryCharacter from the Galois row](/step/every-character/). For the background, see [generic representations and local factors](/learn/representations/#generic-representations-and-local-factors) and [local multiplicity one](/learn/periods/#local-multiplicity-one).

We keep the notation of the previous section: $F$, $G = \mathrm{GL}_n(F)$, $N$, $\psi_N$, $\sigma$ and $\theta$.

### Whittaker functionals

**Definition 4.2.1 (Admissible representation).** A representation $(\pi, V)$ of $G$ on a complex vector space is *smooth* if every vector is fixed by an open subgroup. It is *admissible* if it is smooth and, for every compact open subgroup $K$, the space $V^K$ of $K$-fixed vectors has finite dimension.

**Definition 4.2.2 (Contragredient).** Let $(\pi, V)$ be smooth. The *contragredient* $\tilde{\pi}$ is the action $\tilde{\pi}(g)\xi = \xi \circ \pi(g^{-1})$ on the space $\tilde{V}$ of smooth vectors of the algebraic dual of $V$.

**Definition 4.2.3 (Whittaker functional).** Let $(\pi, V)$ be a representation of $G$ and $\chi$ a character of $N$. A linear form $\ell$ on $V$ is $(N, \chi)$-*equivariant* if $\ell(\pi(u)v) = \chi(u)\ell(v)$ for $u \in N$ and $v \in V$. Write $\mathrm{Wh}_\chi(\pi)$ for the space of these forms. A *Whittaker functional* is an element of $\mathrm{Wh}_{\psi_N}(\pi)$.

### The Gelfand-Kazhdan argument

**Theorem 4.2.4 (Uniqueness, given a generic contragredient).** Let $(\pi, V)$ be an irreducible admissible representation of $G$. Assume that $\mathrm{Wh}_{\psi_N^{-1}}(\tilde\pi) \neq 0$. Then $\dim \mathrm{Wh}_{\psi_N}(\pi) \leq 1$.

Lean: `GroundTheory.Automorphic.Whittaker.rank_whittaker_le_one_of_contragredient`.

*Proof.* Fix a Haar measure $\mu$ on $G$. It is invariant under inversion, and $\mu$ is invariant under $\sigma$: the image of $\mu$ under the automorphism $\theta$ is $c\mu$ for some $c > 0$, and $\theta^2 = 1$ gives $c^2 = 1$; then $\sigma = \mathrm{inv} \circ \theta$. For $f \in C_c^\infty(G)$ let $\pi(f) = \int_G f(g)\pi(g)\,d\mu(g)$. Fix a nonzero $\tilde\ell \in \mathrm{Wh}_{\psi_N^{-1}}(\tilde\pi)$.

For $\ell \in \mathrm{Wh}_{\psi_N}(\pi)$ define $A_\ell \colon C_c^\infty(G) \to \tilde V$ by $A_\ell(f) = \ell \circ \pi(f)$. The image is smooth because $f$ is fixed by an open subgroup on the right. If $\ell \neq 0$, then $A_\ell$ is onto, since $\tilde\pi$ is irreducible and the image is a nonzero invariant subspace. The distribution $D_\ell(f) = \tilde\ell(A_\ell(f))$ satisfies $D_\ell(f(u_1^{-1} \cdot u_2)) = \psi_N(u_1)\psi_N(u_2)^{-1}D_\ell(f)$. By [Corollary 4.1.8](/entry/bi-equivariant-sigma-invariant-gl/), $D_\ell(f \circ \sigma) = D_\ell(f)$.

Let $\mathcal{K}(\tilde\ell)$ be the space of $k \in C_c^\infty(G)$ with $\tilde\ell(\xi \circ \pi(k)) = 0$ for all $\xi \in \tilde V$. It depends only on $\tilde\ell$. We claim that $\ker A_\ell = \{ f : f \circ \sigma \in \mathcal{K}(\tilde\ell)\}$. First, $A_\ell$ intertwines right translation on $C_c^\infty(G)$ with $\tilde\pi$, and its image is irreducible. So $\ker A_\ell$ is a maximal proper subspace among the subspaces stable under right translation: every such proper subspace $L \supseteq \ker A_\ell$ equals $\ker A_\ell$. Second, the set $L = \{ f : f \circ \sigma \in \mathcal{K}(\tilde\ell)\}$ is stable under right translation, because $\sigma$ turns right translation by $g$ into left translation by $\sigma(g)^{-1}$, and $\mathcal{K}(\tilde\ell)$ is stable under left translation. Third, $\ker A_\ell \subseteq L$: write $\xi = A_\ell(k)$, which is possible as $A_\ell$ is onto; then $\tilde\ell(\xi \circ \pi(f\circ\sigma))$ is a value of $D_\ell$ on a convolution of $k$ and $f$, and the $\sigma$-invariance of $D_\ell$ moves it to a value that vanishes when $A_\ell(f) = 0$. Fourth, $L$ is proper, since a normalized indicator function $k_0$ with $\xi_0 \circ \pi(k_0) = \xi_0$ and $\tilde\ell(\xi_0) \neq 0$ gives an element outside $L$. So two nonzero $\ell_1, \ell_2$ have $\ker A_{\ell_1} = \ker A_{\ell_2}$.

Hence $A_{\ell_2} = T \circ A_{\ell_1}$ for a unique linear map $T \colon \tilde V \to \tilde V$. Both maps intertwine right translation with $\tilde\pi$, so $T$ commutes with $\tilde\pi$. The representation $\tilde\pi$ is admissible and irreducible, so by Schur's lemma $T = c$ for a scalar $c$. Evaluate at a normalized indicator function $f = \mu(K)^{-1}\mathbf{1}_K$, where $K$ is a compact open subgroup that fixes a given $v$: then $\pi(f)v = v$, so $\ell_2(v) = c\,\ell_1(v)$. $\square$

### The contragredient

**Theorem 4.2.5 (Contragredient and transpose).** Let $(\pi, V)$ be an irreducible admissible representation of $G$. Let $\iota(g) = {}^t g^{-1}$. Then $\tilde\pi \cong \pi \circ \iota$.

Lean: `GroundTheory.Automorphic.ContragredientTranspose.nonempty_equiv_contragredient`.

*Proof.* For an admissible representation $\rho$ and $f \in C_c^\infty(G)$, the operator $\rho(f)$ has finite rank, and $\Theta_\rho(f) = \operatorname{tr}\rho(f)$ is the *distribution character* of $\rho$. Two irreducible admissible representations with the same distribution character are isomorphic. So it is enough to compare characters. We have $\Theta_{\tilde\pi}(f) = \Theta_\pi(f^\vee)$ with $f^\vee(g) = f(g^{-1})$. Also $\Theta_{\pi\circ\iota}(f) = \Theta_\pi(f \circ \iota^{-1})$, since $\iota$ preserves the Haar measure. And $f \circ \iota^{-1}$ is the transpose of $f^\vee$. So we need $\Theta_\pi(f^\vee \circ {}^t) = \Theta_\pi(f^\vee)$. The character $\Theta_\pi$ is invariant under conjugation. By the theorem of Gelfand and Kazhdan, every distribution on $\mathrm{GL}_n(F)$ invariant under conjugation is invariant under the transpose (Gelfand-Kazhdan, *Lie Groups and Their Representations*, 1975; Bernstein-Zelevinsky, Russian Math. Surveys 31 (1976), §7). $\square$

**Theorem 4.2.6 (Uniqueness of Whittaker functionals).** Let $(\pi, V)$ be an irreducible admissible representation of $G$. Then $\dim \mathrm{Wh}_{\psi_N}(\pi) \leq 1$.

Lean: `GroundTheory.Automorphic.ContragredientTranspose.rank_whittaker_le_one`.

*Proof.* If $\mathrm{Wh}_{\psi_N}(\pi) = 0$ there is nothing to prove. Otherwise let $\ell \neq 0$ be a Whittaker functional. By [Theorem 4.2.5](/entry/nonempty-equiv-contragredient/) there is an isomorphism $E \colon \tilde V \to V$ with $E\,\tilde\pi(g) = \pi(\iota g)\,E$. Let $w_0$ be the antidiagonal permutation matrix. Then $\iota(g) = w_0\,\theta(g)\,w_0$ and $w_0^2 = 1$. Put $\ell'(\xi) = \ell(\pi(w_0)E\xi)$. For $u \in N$,
$$\ell'(\tilde\pi(u)\xi) = \ell(\pi(w_0 \iota(u)) E \xi) = \ell(\pi(\theta(u))\pi(w_0)E\xi) = \psi_N(\theta u)\,\ell'(\xi) = \psi_N(u)^{-1}\ell'(\xi).$$
So $\ell' \in \mathrm{Wh}_{\psi_N^{-1}}(\tilde\pi)$, and $\ell' \neq 0$ since $E$ and $\pi(w_0)$ are bijective. Now apply [Theorem 4.2.4](/entry/rank-whittaker-le-one-of-contragredient/). $\square$

In the classical form, this is the theorem of Gelfand and Kazhdan and of Shalika: an irreducible smooth representation of $\mathrm{GL}_n(F)$ has at most one Whittaker functional up to scalars. Here it is stated for admissible representations, which is no loss, since irreducible smooth representations of $\mathrm{GL}_n(F)$ are admissible.

**Remark 4.2.7 (Formalization).** The first theorem is in [WhittakerLocal.lean](lean:GroundTheory/AutomorphicForms/WhittakerLocal.lean#L91). It passes its data to `rank_le_one_of_ne_bot` in [WhittakerCriterion.lean](lean:GroundTheory/AutomorphicForms/WhittakerCriterion.lean#L796), an abstract criterion for any group with an anti-automorphism that preserves the Haar measure; that criterion calls `rank_equivariantFunctionals_le_one`, which uses `ker_coeffL_eq_comap` (line 616) and `exists_smul_eq` (line 661). We read the statements and the outline of these two lemmas; the lemma `coeffL_surjective` and the Schur lemma `algebraMap_intertwiningMap_bijective_of_isSmooth` were not unfolded. The product bound `rank_whittaker_mul_rank_whittaker_contragredient_le_one` at [line 76](lean:GroundTheory/AutomorphicForms/WhittakerLocal.lean#L76) is proved but not used. The main theorem sits in the namespace `ContragredientTranspose`, not with the other Whittaker results. The transpose invariance is `distribution_transpose_invariant` in `GelfandKazhdan.lean`, line 729, and the character criterion is `nonempty_equiv_of_distChar_eq` in `Character.lean`, line 341; both are proved in the development, not assumed.
