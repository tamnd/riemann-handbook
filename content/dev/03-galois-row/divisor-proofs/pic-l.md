---
id: pic-l
title: No q-torsion in the Picard group of the generic fibre of a strictly henselian line
kind: theorem
decl: GlobalTheory.LocAcycDegOne.picL
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.TateTwistCohomologyGenericFibreHenselLineSubsing
covers: 777
status: drafted
drafted_by: writer@claude
---
This theorem proves that $\operatorname{Pic}(K \otimes_T A)$ has no $q$-torsion, for the rings $T$ and $A$ of [the vanishing of $H^1$](/entry/tate-twist-cohomology-generic-fibre-hensel-line-subsingleton/). That theorem uses it as the Picard input of the Kummer sequence. The proof only changes the hypotheses on $A$ into those of [the statement for a quotient](/entry/pic-generic-fibre-quotient-strict-henselisation-no-torsion-alt/), which has the content. Below this theorem are 777 declarations.

## Statement

Let $T$, $K$, $q$ and $A$ be as in [the parent entry](/entry/tate-twist-cohomology-generic-fibre-hensel-line-subsingleton/).

**Theorem.** If $c \in \operatorname{Pic}(K \otimes_T A)$ and $c^q = 1$, then $c = 1$.

## Proof

1. `surj_of_strictHenselisation_polynomial_alt` gives a ring $O$ and a surjection $\pi \colon O \to A$ of $T[x]$-algebras. Here $O$ is henselian local with separably closed residue field, and it is the union of a directed family of subalgebras $S_i$, each isomorphic to the localization of an étale $T[x]$-algebra at a prime.
2. `pic_generic_fibre_quotient_strictHenselisation_no_torsion_alt` takes $O$, $\pi$ and these facts, and gives the conclusion.

There is no other step.

## In the Lean code

The theorem is in [TateTwistCohomologyGenericFibreHenselLineSubsing.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/TateTwistCohomologyGenericFibreHenselLineSubsing.lean#L19). The proof has two lines. The lemmas:

- `GlobalTheory.T.surj_of_strictHenselisation_polynomial_alt`, in SurjOfStrictHenselisationPolynomialStatement.lean; we have read only its statement;
- `GlobalTheory.T.pic_generic_fibre_quotient_strictHenselisation_no_torsion_alt`, in [PicGenericFibreQuotientStrictHenselisationNoTorsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/PicGenericFibreQuotientStrictHenselisationNoTorsStatement.lean#L7).

The sister lemma `unitsL` (line 14) has the same form, for units. The hypothesis that $A$ is strictly henselian, and the hypothesis on images of étale algebras, are used only in step 1.
