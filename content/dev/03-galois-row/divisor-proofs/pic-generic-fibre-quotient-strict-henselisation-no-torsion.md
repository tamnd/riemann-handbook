---
id: pic-generic-fibre-quotient-strict-henselisation-no-torsion
title: No q-torsion in the Picard group of the generic fibre of a quotient of a strict henselisation
kind: theorem
decl: GlobalTheory.pic_generic_fibre_quotient_strictHenselisation_no_torsion
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.PicGenericFibreQuotientStrictHenselisationNoTors
covers: 775
status: drafted
drafted_by: writer@claude
---
This theorem passes from a strict henselisation $O$ of $T[x]$ to a quotient $A$ of $O$, for the statement that the Picard group of the generic fibre over $T$ has no $q$-torsion. It splits into two cases. If $A = O$, the statement is [pic_localization_strictHenselisation_no_torsion](/entry/pic-localization-strict-henselisation-no-torsion/), which has the main content. If $A$ is a proper quotient, the generic fibre has dimension 0 and its Picard group is trivial. Its second name is [the `_alt` version](/entry/pic-generic-fibre-quotient-strict-henselisation-no-torsion-alt/). Below this theorem are 775 declarations; 764 of them are below the first case.

## Statement

The hypotheses on $T$, $K$, $q$ and $O$, and the statement, are those of [the `_alt` entry](/entry/pic-generic-fibre-quotient-strict-henselisation-no-torsion-alt/): for a surjection $\pi \colon O \to A$ of $T[x]$-algebras, $\operatorname{Pic}(K \otimes_T A)$ has no $q$-torsion. Write $A_K = K \otimes_T A$. It is the localization of $A$ at the image of $T \setminus \{0\}$ (`Localization.tensorRightAlgEquiv`).

## Proof

$T$ is integrally closed, as each monic polynomial over $T$ has a root in $T$ (`isIntegrallyClosed_of_forall_monic_root`). $O$ is a domain (`indEtale_isDomain_isIntegrallyClosed`).

*Case 1: $\pi$ is injective.* Then $\pi$ is an isomorphism, so $A_K \cong K \otimes_T O$, the localization of $O$ at $T \setminus \{0\}$. `pic_localization_strictHenselisation_no_torsion` gives the result for this ring, and `pic_transfer` moves it along the isomorphism.

*Case 2: $\ker \pi \neq 0$.* We prove that each prime $Q$ of $A_K$ is maximal. Then $\operatorname{Pic} A_K = 1$ by `pic0` (from `pic_eq_one_of_forall_prime_maximal`). Let $Q \subseteq Q'$ with $Q'$ maximal, and let $p \subseteq p'$ be their inverse images in $O$. Then $p \supseteq \ker \pi$, so $p \neq 0$, and $p' \cap T = 0$, as $T \setminus \{0\}$ becomes invertible in $A_K$. `primes_eq` gives $p = p'$ in two steps:

1. `poly`: in $T[x]$, if $P \subseteq P'$ are primes, $P \neq 0$ and $P' \cap T = 0$, then $P = P'$. The reason: both stay prime in $K[x]$, the localization at $T \setminus \{0\}$, and there the nonzero prime $P K[x]$ is maximal.
2. `incomp`, from `ind_etale_prime_comparison`: in a directed union of localizations of étale $T[x]$-algebras, primes $p \subseteq p'$ with the same contraction to $T[x]$ are equal. To apply step 1 to the contractions, the contraction of $p$ must be nonzero. It is, since otherwise `incomp` applied to $0 \subseteq p$ gives $p = 0$.

As $\pi$ is surjective and localization keeps primes apart, $p = p'$ gives $Q = Q'$. The rest is bookkeeping.

## In the Lean code

The theorem is in [PicGenericFibreQuotientStrictHenselisationNoTors.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/PicGenericFibreQuotientStrictHenselisationNoTors.lean#L78). The lemmas of the same file, in the namespace `GlobalTheory.QPic`: `pic0` (line 11), `incomp` (line 13), `poly` (line 15), `pic_transfer` (line 51) and `primes_eq` (line 60). From other files:

- `GlobalTheory.pic_localization_strictHenselisation_no_torsion`, in [PicLocalizationStrictHenselisationNoTorsion.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/PicLocalizationStrictHenselisationNoTorsion.lean#L12);
- `GlobalTheory.T.pic_eq_one_of_forall_prime_maximal` and `GlobalTheory.T.ind_etale_prime_comparison`, whose statements only we have read;
- `GlobalTheory.LocIndEtale.isIntegrallyClosed_of_forall_monic_root` and `GlobalTheory.indEtale_isDomain_isIntegrallyClosed`, not opened.

In case 2 the hypotheses on $q$ and on the residue field are not used: the Picard group is trivial, not only free of $q$-torsion.
