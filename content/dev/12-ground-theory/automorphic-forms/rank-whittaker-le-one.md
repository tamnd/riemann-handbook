---
id: rank-whittaker-le-one
title: Uniqueness of Whittaker functionals for GL(n) over a p-adic field
kind: theorem
decl: GroundTheory.Automorphic.ContragredientTranspose.rank_whittaker_le_one
module: GroundTheory.AutomorphicForms.ContragredientTranspose
covers: 306
status: drafted
drafted_by: writer@claude
---
This theorem proves that an irreducible admissible representation of $\mathrm{GL}_n$ over a non-archimedean local field has at most one Whittaker functional, up to a scalar. Two theorems named `whitLeOne_of_dict`, in two files WhitLeOneOfDict.lean, use it; we have not opened them. Through them it lies below [EveryCharacter](/step/every-character/).

## Statement

Let $F$ be a non-archimedean local field and $\psi_0 \colon F \to \mathbb{C}^\times$ a continuous nontrivial additive character. Let $N \subset \mathrm{GL}_n(F)$ be the group of upper triangular unipotent matrices and $\psi_N(u) = \psi_0(u_{12} + u_{23} + \dots + u_{n-1,n})$. Let $\pi$ be a representation of $\mathrm{GL}_n(F)$ on a complex vector space $V$. Suppose that $\pi$ is irreducible, and admissible: each vector has an open stabilizer, and the vectors fixed by each compact open subgroup form a space of finite dimension.

**Theorem.** The space of linear forms $\ell$ on $V$ with $\ell(\pi(u)v) = \psi_N(u)\,\ell(v)$ for all $u \in N$ and $v \in V$ has dimension at most $1$.

This is the uniqueness of the Whittaker model (Gelfand and Kazhdan, "Representations of the group GL(n, K) where K is a local field", in *Lie Groups and Their Representations*, 1975; Shalika, Ann. of Math. 100, 1974). See [generic representations](/learn/representations/#generic-representations-and-local-factors).

## Proof

The proof follows Gelfand and Kazhdan. It has three parts.

1. **The contragredient is a twist.** Let $\theta^{\mathsf T}(g) = (g^{\mathsf T})^{-1}$. Then $\tilde\pi \cong \pi \circ \theta^{\mathsf T}$ (`nonempty_equiv_contragredient`, same file). The distribution character of $\tilde\pi$ is that of $\pi$ composed with $g \mapsto g^{-1}$. The distribution character of $\pi \circ \theta^{\mathsf T}$ is that of $\pi$ composed with $\theta^{\mathsf T}$, because Haar measure is $\theta^{\mathsf T}$-invariant. A conjugation-invariant distribution on $\mathrm{GL}_n(F)$ is invariant under transpose (`distribution_transpose_invariant`), so the two characters agree. Irreducible admissible representations with the same character are equivalent (`nonempty_equiv_of_distChar_eq`).
2. **A functional on the contragredient.** If the space is $0$, there is nothing to prove. Otherwise take $\ell \neq 0$ in it. Let $w_0$ be the antidiagonal permutation matrix and $\theta(g) = \sigma(g)^{-1}$, where $\sigma(g)_{ij} = g_{n+1-j,\,n+1-i}$ is the transpose about the antidiagonal. Then $\theta^{\mathsf T}(g) = w_0\, \theta(g)\, w_0$ (`thetaT_eq_longestWeyl`). For $u \in N$, $\theta(u) \in N$ and $\psi_N(\theta(u)) = \psi_N(u)^{-1}$. So, with $E \colon \tilde\pi \cong \pi \circ \theta^{\mathsf T}$, the form $\ell'(x) = \ell(\pi(w_0) E x)$ is a nonzero functional on $\tilde\pi$ with character $\psi_N^{-1}$.
3. **The Gelfand-Kazhdan criterion.** Every distribution on $\mathrm{GL}_n(F)$ that transforms by $\psi_N$ on the left and $\psi_N^{-1}$ on the right under $N$ is invariant under $\sigma$ (`distribution_sigma_invariant`). With part 2, `rank_whittaker_le_one_of_contragredient` gives the bound.

## In the Lean code

The theorem is in [ContragredientTranspose.lean](lean:GroundTheory/AutomorphicForms/ContragredientTranspose.lean#L77). The lemmas it calls:

- `nonempty_equiv_contragredient` and `thetaT_eq_longestWeyl`, in the same file.
- `rank_whittaker_le_one_of_contragredient`, in [WhittakerLocal.lean](lean:GroundTheory/AutomorphicForms/WhittakerLocal.lean#L91). It applies the abstract criterion `rank_le_one_of_ne_bot` of [WhittakerCriterion.lean](lean:GroundTheory/AutomorphicForms/WhittakerCriterion.lean#L796), with the $\sigma$-invariance of Haar measure (`map_sigma_eq`) and `distribution_sigma_invariant`.
- `distribution_transpose_invariant`, in [GelfandKazhdan.lean](lean:GroundTheory/AutomorphicForms/ContragredientTranspose/GelfandKazhdan.lean#L729), and `nonempty_equiv_of_distChar_eq`, in [Character.lean](lean:GroundTheory/AutomorphicForms/ContragredientTranspose/Character.lean#L341).

We have not opened the proofs of the two distribution lemmas, which hold the analysis. The forms $\ell$ are in the full algebraic dual of $V$, and irreducibility is algebraic, as in the smooth theory. The Lean contragredient acts on the smooth vectors of the algebraic dual. WhittakerLocal.lean also proves the product bound `rank_whittaker_mul_rank_whittaker_contragredient_le_one`, but this theorem does not use it.
