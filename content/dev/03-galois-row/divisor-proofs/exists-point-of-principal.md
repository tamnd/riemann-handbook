---
id: exists-point-of-principal
title: A Siegel family classifies principal objects over noetherian local rings
kind: theorem
decl: GlobalTheory.SiegelFamLocal.exists_point_of_principal
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.SiegelFamilyClassifiesNoetherianLocal
covers: 407
status: drafted
drafted_by: writer@claude
---
This theorem proves that a Siegel family classifies each principal Siegel object over a noetherian local ring $R$. It passes to the completion $\hat R$, where [the complete case](/entry/siegel-family-classifies-complete-noetherian-local/) applies, and descends along the faithfully flat map $R \to \hat R$. [Its statement form](/entry/siegel-family-classifies-noetherian-local/) repeats it for [the noetherian classification](/entry/classify-noetherian/).

## Statement

Use $B_n = \mathbb{Z}[\zeta_n, 1/n]$, Siegel objects, the pullback relation $c \cong f^*u$ and Siegel families $(X, s, u)$ as in [the affine entry](/entry/exists-classify-affine/).

**Theorem.** Let $g \geq 1$ and $n \geq 3$ odd, and let $(X, s, u)$ be a Siegel family of genus $g$ and level $n$. Let $R$ be a noetherian local ring, $\beta \colon B_n \to R$, and $c$ a principal Siegel object over $\operatorname{Spec} R$. Then there is $f \colon \operatorname{Spec} R \to X$ with $sf = \operatorname{Spec} \beta$ and $c \cong f^*u$.

## Proof

Let $\mathfrak{m}$ be the maximal ideal of $R$ and $\hat R$ the $\mathfrak{m}$-adic completion.

1. $\hat R$ is noetherian (`AdicNoeth.isNoetherianRing_adicCompletion`) and flat over $R$ (Mathlib, `AdicCompletion.flat_of_isNoetherian`). The map $R \to \hat R$ is a local map of local rings, so $\hat R$ is faithfully flat over $R$. This is Theorem 8.14 of Matsumura, *Commutative Ring Theory*.
2. By `siegelFamily_classified_of_faithfullyFlat`, it is enough to classify each object $c'$ over $\hat R$ with $c' \cong c \otimes_R \hat R$. We have not opened the proof of this descent lemma.
3. Such a $c'$ is principal, since $c$ is (`SiegLevCalc.sRel_principal` with `sRel_one_one_iff`).
4. $\hat R$ is a complete noetherian local ring, so [the complete case](/entry/siegel-family-classifies-complete-noetherian-local/) classifies $c'$.

## In the Lean code

The theorem is in [SiegelFamilyClassifiesNoetherianLocal.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SiegelFamilyClassifiesNoetherianLocal.lean#L16). The lemmas it calls:

- `GlobalTheory.AdicNoeth.isNoetherianRing_adicCompletion`;
- `AdicCompletion.flat_of_isNoetherian` and `Module.FaithfullyFlat.of_flat_of_isLocalHom`, from Mathlib;
- `GlobalTheory.T.siegelFamily_classified_of_faithfullyFlat`, a statement form; it holds for any faithfully flat $R \to R'$, not only for the completion;
- `GlobalTheory.SiegLevCalc.sRel_principal` and `GlobalTheory.SiegLev.sRel_one_one_iff`;
- `GlobalTheory.T.siegelFamily_classifies_complete_noetherian_local`.

The completeness of $\hat R$ for its own maximal ideal, and the fact that $\hat R$ is local, come from instances (`inferInstance`); we have not looked up which ones.
