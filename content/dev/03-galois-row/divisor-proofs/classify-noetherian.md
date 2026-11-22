---
id: classify-noetherian
title: A Siegel family classifies principal objects over noetherian rings
kind: theorem
decl: GlobalTheory.SiegelNoeth.classify_noetherian
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.SiegelFamilyClassifiesNoetherian
covers: 446
status: drafted
drafted_by: writer@claude
---
This theorem proves that a Siegel family classifies each principal Siegel object over $\operatorname{Spec} R$ for a noetherian ring $R$. It reduces the question to the local rings $R_\mathfrak{p}$, where [the noetherian local case](/entry/siegel-family-classifies-noetherian-local/) applies, and then spreads the result to an open neighbourhood. [Its statement form](/entry/siegel-family-classifies-noetherian/) repeats it for [the classification over affine schemes](/entry/exists-classify-affine/).

## Statement

Use $B_n = \mathbb{Z}[\zeta_n, 1/n]$, Siegel objects, the pullback relation $c \cong f^*u$ and Siegel families $(X, s, u)$ as in [the affine entry](/entry/exists-classify-affine/).

**Theorem.** Let $g \geq 1$ and $n \geq 3$ odd, and let $(X, s, u)$ be a Siegel family of genus $g$ and level $n$. Let $R$ be a noetherian ring, $\beta \colon B_n \to R$, and $c$ a principal Siegel object over $\operatorname{Spec} R$. Then there is $f \colon \operatorname{Spec} R \to X$ with $sf = \operatorname{Spec} \beta$ and $c \cong f^*u$.

## Proof

Call an object over a scheme $T$ *classified* if it is $f^*u$ for some $f \colon T \to X$ over $B_n$.

1. By `siegelFamily_classified_of_local`, it is enough to find, for each point $\mathfrak{p}$ of $\operatorname{Spec} R$, an open immersion $V \to \operatorname{Spec} R$ whose image contains $\mathfrak{p}$, and a pullback of $c$ to $V$ that is classified. We have not opened the proof of this gluing lemma.
2. Fix $\mathfrak{p}$. Each pullback $c'$ of $c$ to $R_\mathfrak{p}$ is principal (`siegPre_pull_ringChange`). Since $R_\mathfrak{p}$ is noetherian and local, [the local case](/entry/siegel-family-classifies-noetherian-local/) classifies $c'$.
3. `siegelClassified_at_prime_spreads_basicOpen` then gives $r \notin \mathfrak{p}$ such that each pullback of $c$ to $R[1/r]$ is classified. We have not opened its proof.
4. Take $V = \operatorname{Spec} R[1/r]$. It is an open immersion with image the basic open set $D(r)$, which contains $\mathfrak{p}$. A pullback of $c$ to $V$ exists by `siegPre_pull_ringChange`, and step 3 classifies it.

The rest is bookkeeping with $\operatorname{Spec}$ of composite ring maps.

## In the Lean code

The theorem is in [SiegelFamilyClassifiesNoetherian.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SiegelFamilyClassifiesNoetherian.lean#L24). The lemmas it calls:

- `GlobalTheory.T.siegelFamily_classified_of_local`, a statement form: a principal object is classified if it is classified on an open cover;
- `GlobalTheory.T.siegelFamily_classifies_noetherian_local`;
- `GlobalTheory.T.siegelClassified_at_prime_spreads_basicOpen`, a statement form;
- `GlobalTheory.SiegelRingChange.siegPre_pull_ringChange` in [SiegelPrePullbackPrincipalRingChange.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/SiegelPrePullbackPrincipalRingChange.lean#L52): pullbacks of Siegel objects exist and pullbacks of principal objects are principal;
- the Mathlib facts `IsOpenImmersion.of_isLocalization` and `PrimeSpectrum.localization_away_comap_range`.

The file also proves two small lemmas, `spMap_comp_eq` and `spMap_id_eq`, on $\operatorname{Spec}$ of a composite and of the identity. Similar lemmas appear again as `spMap_comp_` and `spMap_id_` in the file of [the complete case](/entry/classified-of-complete/).
