---
id: subsingleton-ht-one-generic-fibre-of-sh-etale-cover
title: Vanishing of the first cohomology of the generic fibre of a strictly henselian line, a renaming
kind: theorem
decl: GlobalTheory.T.subsingleton_ht_one_genericFibre_of_sh_etale_cover
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.TateTwistCohomologyGenericFibreHenselLineSubsingStatement
covers: 917
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the vanishing of $H^1$ on the generic fibre](/entry/tate-twist-cohomology-generic-fibre-hensel-line-subsingleton/), which has the real content. It says that $H^1$ with coefficients $\mathbb{Z}/q(i)$ vanishes on the generic fibre of a strictly henselian local ring over the affine line. Two results use it, and both lead to the [local steps](/entry/steps-holds/) of the Galois row. Below this theorem are 917 declarations.

## Statement

Let $T$ be a local domain in which each monic polynomial of positive degree has a root (`AIC T`), with fraction field $K$. Let $q \geq 1$ be invertible in $T$.

**Theorem.** Let $A$ be a strictly henselian local ring (`SH A`) that is a $T[x]$-algebra, such that each $a \in A$ is in the image of a $T[x]$-algebra map $E \to A$ from an étale $T[x]$-algebra $E$. Then for each $i \in \mathbb{Z}$, $H^1(\operatorname{Spec}(K \otimes_T A), \mathbb{Z}/q(i)) = 0$.

## Proof

The proof is the term `GlobalTheory.LocAcycDegOne.tateTwistCohomology_genericFibre_henselLine_subsingleton`, with the same statement. There is no other step.

## In the Lean code

The theorem is in [TateTwistCohomologyGenericFibreHenselLineSubsingStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/TateTwistCohomologyGenericFibreHenselLineSubsingStatement.lean#L6), a file of seven lines. The name moves the result to the namespace `GlobalTheory.T`. Its two users call this name:

- `GlobalTheory.EtC.LineLocal.eqv_local` in EtaleCohomologyEquivStrictHenselianLinePoint.lean;
- `UpperTheory.Cb.C3.local_eqv` in EtaleCohomologyIndEtaleBaseChange.lean.

Both prove that pullback from $\operatorname{Spec} A$ to $\operatorname{Spec}(K \otimes_T A)$ is bijective on cohomology with coefficients $\mathbb{Z}/q(i)$ (the property `Eqv`). We read only their statements and the line that calls this theorem.
