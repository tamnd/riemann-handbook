---
id: gs-pairing-input
title: Nondegeneracy of the pairing of H^1 with compactly supported H^2 for prime-power roots of unity
kind: theorem
decl: GroundTheory.ProfCoh.gsPairingInput
module: GroundTheory.ProfiniteCohomology.RestrictedRamification.BaseMain
covers: 334
status: drafted
drafted_by: writer@claude
---
This theorem proves that the cup product pairing between $H^1(G_S, \mathbb{Z}/n)$ and $H^2_c(G_S, \mu_n)$ has zero kernels on both sides, for $n$ a power of a prime $\ell$ and for every number field. The proof uses class field theory for characters of $G_S$ and Kummer theory for $H^2_c$. It is the input of `exists_compactDualityHypotheses_gs_of_pairing`, and so of [the duality axioms for one prime power](/entry/exists-compact-duality-hypotheses-gs/).

## Statement

Let $\ell$ be a prime and $n = \ell^k \geq 1$.

**Theorem** (`GsPairingInput n ℓ`). Let $L$ be a number field in $\overline{\mathbb{Q}}$ and $S$ a finite set of finite places of $L$ that contains the primes above $\ell$. Suppose that $\mu_n \subset L$, that $n$ is odd or $L$ is totally complex, and that $H^3(G_S, \mu_n) = 0$. Let $t \colon H^3_c(G_S, \mu_n) \to \mathbb{Z}/n$ be the trace `gsCompactInv` (as in [the previous entry](/entry/exists-compact-duality-hypotheses-gs/)), and consider

$$H^1(G_S, \mathbb{Z}/n) \times H^2_c(G_S, \mu_n) \to \mathbb{Z}/n, \qquad (x, y) \mapsto t(y \cup x).$$

Then $x = 0$ if $t(y \cup x) = 0$ for all $y$, and $y = 0$ if $t(y \cup x) = 0$ for all $x$.

Here $G_S$ and $H^\bullet_c$ are as in [the Poitou-Tate package](/entry/gs-tate-poitou-tate-hypotheses/), with compact support at the finite places of $S$ only.

## Proof

Let $C_S$ be the quotient of the idele group of $L$ by the subgroup `sIdeleSubgroup S`, which we have not unfolded. Class field theory enters as `charEquiv`: an isomorphism between continuous characters $G_S \to \mathbb{Z}/n$ and characters $C_S \to \mathbb{Z}/n$. It uses the hypothesis "odd or totally complex". A datum $d$ of type `GsUnitsDatum` has a class $[d] \in C_S$ (`gsUnitsClass`) and, by Kummer theory, a class $\delta(d) \in H^2_c(G_S, \mu_n)$. The key formula is `gsCompactInv_gsCupClass`: for a character $\chi$ with class $x$,

$$t(\delta(d) \cup x) = \chi'([d]),$$

where $\chi'$ is the character of $C_S$ that corresponds to $\chi$.

1. **Left kernel** (`gsCompactInv_ker_left`). Let $x \neq 0$. Its character $\chi'$ is nontrivial, so $\chi'(a) \neq 0$ for some $a \in C_S$. By `exists_coprime_gsUnitsClass_eq`, $m a = [d]$ for some $d$ and some $m$ prime to $\ell$. Then $t(\delta(d) \cup x) = m\,\chi'(a) \neq 0$ in $\mathbb{Z}/\ell^k$.
2. **Right kernel** (`gsCompactInv_ker_right`). The case $k = 0$ is trivial. Otherwise each $y$ is $\delta(d)$ for some $d$ (`surjective_gsKummerCompactδ`, `gsUnitsData_surjective`). If $y$ pairs to zero with all $x$, then every character of $C_S$ into $\mathbb{Z}/n$ kills $[d]$, so $[d] = n b$ (`exists_nsmul_eq_of_forall_zmod`). Writing $m b = [d']$ with $m$ prime to $\ell$ gives $m y = 0$. Since also $\ell^k y = 0$, $y = 0$.

## In the Lean code

The theorem is in [BaseMain.lean](lean:GroundTheory/ProfiniteCohomology/RestrictedRamification/BaseMain.lean#L56). Its proof is one line that calls the two kernel lemmas in [BasePairing.lean](lean:GroundTheory/ProfiniteCohomology/RestrictedRamification/BasePairing.lean#L106). `GsPairingInput` and `GsPairingNondegenerate` are in [BijectiveGsLocalInvRootsOfPlaces.lean](lean:GroundTheory/ProfiniteCohomology/RestrictedRamification/BijectiveGsLocalInvRootsOfPlaces.lean#L47). `charEquiv` is in [ClassFieldGSFull.lean](lean:GroundTheory/ProfiniteCohomology/RestrictedRamification/ClassFieldGSFull.lean#L77).

The hypothesis $\mu_n \subset L$ is in `GsPairingInput`, but the proof never uses it: the binder is `_`. So the theorem holds without it. The exponent $k$ is not in the statement `GsPairingInput n ℓ`; it enters only through the hypothesis $n = \ell^k$.
