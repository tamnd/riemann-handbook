---
id: jacquet-shalika-rigidity-holds
title: Two families of cuspidal representations with the same Satake parameters are the same family
kind: theorem
decl: GlobalTheory.JSW.jacquetShalikaRigidity_holds
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.JacquetShalikaRigidityHolds
covers: 2259
status: drafted
drafted_by: writer@claude
---
This theorem proves the rigidity statement `JacquetShalikaRigidity`. Take two finite families, each member a [[cuspidal representation|9AZ164C298]] of a general linear group over a totally complex field. If they have the same total Satake parameters at almost all primes, then the two families agree up to order. [The slope theorem](/entry/slope-all-of/) uses it, through `jacquetShalika_of`, to get a Gelfand-Kazhdan duality. The analytic work is in [the vanishing lemma](/entry/vanish/).

## Statement

Let $E$ be a totally complex number field. Let $\iota$ and $\kappa$ be finite types, and let $\pi_i$ be a cuspidal representation of $\mathrm{GL}_{m_i}$ over $E$ and $\pi'_j$ one of $\mathrm{GL}_{m'_j}$, with all $m_i, m'_j \geq 1$. Here a cuspidal representation `CG E a` is an isomorphism class of irreducible spaces of cusp forms. Suppose that for cofinitely many primes $w$ of $E$ there are Satake parameters $B_i$ of $\pi_i$ and $B'_j$ of $\pi'_j$ at $w$ with
$$\sum_i B_i = \sum_j B'_j$$
as multisets.

**Theorem.** There is a bijection $s \colon \iota \to \kappa$ with $m'_{s(i)} = m_i$ and $\pi'_{s(i)} = \pi_i$ for all $i$.

This is the classification theorem of H. Jacquet and J. Shalika (On Euler products and the classification of automorphic forms II, Amer. J. Math. 103, 1981), for isobaric sums.

## Proof

1. The lemma `exists_isUnitary_twist_absPow` writes each $\pi_i$ as $\pi_{0,i} \otimes |\cdot|^{t_i}$ with $t_i \in \mathbb{R}$ and $\pi_{0,i}$ unitary, that is, with a unitary central character. The same holds for each $\pi'_j$.
2. Let $T$ be the finite set of primes where the hypothesis fails. By `unrOutside_of_twist`, each $\pi_{0,i}$ and $\pi'_{0,j}$ has Satake parameters outside $T$.
3. Let $M$ and $M'$ be the multisets of the pairs $(\pi_{0,i}, t_i)$ and $(\pi'_{0,j}, t'_j)$. Let $S$ be the set of pairs in $M + M'$, and $c(p)$ the multiplicity of $p$ in $M$ minus its multiplicity in $M'$.
4. Take the $(r+1)$st power sums of the equality of parameters. The lemma `sum_map_pow_twist` moves the twist out of the power sum as the factor $Nw^{-(r+1)t}$. So
$$\sum_{p \in S} c(p)\, Nw^{-(r+1)t_p} \sum_{\alpha \in \mathrm{sat}(\sigma_p, w)} \alpha^{r+1} = 0$$
for all $w \notin T$ and $r \geq 0$.
5. `vanish` gives $c = 0$. So $M = M'$, and then the multisets of the $\pi_i$ and of the $\pi'_j$ agree. `exists_equiv_of_map_eq` turns this into the bijection $s$.

## In the Lean code

The theorem is at [line 250 of JacquetShalikaRigidityHolds.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/JacquetShalikaRigidityHolds.lean#L250). The statement is in [StrongMultiplicityOne.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/GaloisCohomology₂/StrongMultiplicityOne.lean#L189), and `IsUnitary` is at [line 89](lean:Development/AbelianVarietyTheory/PublishedTheorems/GaloisCohomology₂/StrongMultiplicityOne.lean#L89) of that file. The decomposition into a unitary part and a twist is in [ExistsIsUnitaryTwistAbsPow.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsIsUnitaryTwistAbsPow.lean#L114).

The function `sat` in [UnrOutside.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/UnrOutside.lean#L16) chooses a Satake parameter, and it returns the empty multiset when there is none. So the identity in step 4 needs `UnrOutside`, which says that a parameter exists outside $T$. The same file has an `example` (line 27) that only states $x = x$ by `rfl`.
