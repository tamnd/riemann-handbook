---
id: pic-generic-fibre-quotient-strict-henselisation-no-torsion-alt
title: No q-torsion in the Picard group of the generic fibre of a quotient of a strict henselisation, a renaming
kind: theorem
decl: GlobalTheory.T.pic_generic_fibre_quotient_strictHenselisation_no_torsion_alt
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.PicGenericFibreQuotientStrictHenselisationNoTorsStatement
covers: 776
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the theorem without `_alt`](/entry/pic-generic-fibre-quotient-strict-henselisation-no-torsion/), which has the real content. It says that the Picard group of the generic fibre of a quotient of a strict henselisation of $T[x]$ has no $q$-torsion. Its only user is [picL](/entry/pic-l/). Below this theorem are 776 declarations.

## Statement

Let $T$ be a local domain in which each monic polynomial of positive degree has a root, with fraction field $K$, and let $q \geq 1$ be invertible in $T$. Let $O$ be a henselian local $T[x]$-algebra with separably closed residue field. Suppose that $O$ is the union of a directed family of $T[x]$-subalgebras $S_i$, each isomorphic to the localization at a prime of an étale $T[x]$-algebra.

**Theorem.** Let $\pi \colon O \to A$ be a surjection of $T[x]$-algebras. If $c \in \operatorname{Pic}(K \otimes_T A)$ and $c^q = 1$, then $c = 1$.

## Proof

The proof is the term `GlobalTheory.pic_generic_fibre_quotient_strictHenselisation_no_torsion`, with the same statement. There is no other step.

## In the Lean code

The theorem is in [PicGenericFibreQuotientStrictHenselisationNoTorsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/PicGenericFibreQuotientStrictHenselisationNoTorsStatement.lean#L7), a file of eight lines. The name moves the result from the root namespace `GlobalTheory` to `GlobalTheory.T` and adds the suffix `_alt`. The file imports `Mathlib` twice (lines 1 and 3).
