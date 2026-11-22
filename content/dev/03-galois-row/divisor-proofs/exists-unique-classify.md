---
id: exists-unique-classify
title: A Siegel family classifies principal Siegel objects over every scheme
kind: theorem
decl: GlobalTheory.SiegFamAll.existsUnique_classify
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.SiegelFamilyExistsUniqueClassifyScheme
covers: 557
status: drafted
drafted_by: writer@claude
---
This theorem proves that the base $X$ of a Siegel family is a fine moduli scheme for principal Siegel objects of odd level $n \geq 3$. A Siegel family only asks for classifying maps over reduced schemes and for uniqueness over local rings; this theorem removes both limits. [The moduli with an action of an order](/entry/act-sieg-exists-rep/) uses it, through [its statement form](/entry/siegel-family-exists-unique-classify-scheme/), to get the map $f \colon S \to X$ in its universal property.

## Statement

Let $B_n = \mathbb{Z}[\zeta_n, 1/n] \subset \mathbb{C}$ and use the Siegel objects of genus $g$ and level $n$ over $B_n$, and the principal ones, from [the Siegel representability entry](/entry/sd-rep-of-coprime/). A *Siegel family* $F$ (`SFam`) is a scheme $X$, smooth of relative dimension $g(g+1)/2$ and quasi-projective over $B_n$, with a principal Siegel object $u$ over $X$, such that:

- each principal object over a reduced scheme $S$, whose points over the generic point of $\operatorname{Spec} B_n$ are dense, is a pullback of $u$ along some map $S \to X$ over $B_n$;
- over $\operatorname{Spec}$ of a local ring, two such maps for the same object are equal.

Here "$c$ is a pullback of $u$ along $f$" (`SiegPB`) means: a cartesian map of abelian schemes over $f$, an isomorphism of the line bundles, and equality of the level structures.

**Theorem.** Let $g \geq 1$, $n \geq 3$ odd, and $F$ a Siegel family. For each scheme $S$ over $B_n$ and each principal Siegel object $c$ over $S$, there is a unique $f \colon S \to X$ over $B_n$ such that $c$ is a pullback of $u$ along $f$.

## Proof

1. *Affine case* ([`exists_classify_affine`](/entry/exists-classify-affine/)). Let $S = \operatorname{Spec} R$. `principalSiegel_descends_finiteType_subring` gives a subring $R_0 \subseteq R$, finitely generated over $\mathbb{Z}$, and a principal object $c_0$ over $R_0$ whose pullback is $c$. $R_0$ is noetherian, so [the noetherian classification](/entry/siegel-family-classifies-noetherian/) gives $f_0 \colon \operatorname{Spec} R_0 \to X$. Then $f = f_0 \circ (\operatorname{Spec} R \to \operatorname{Spec} R_0)$.
2. *Existence.* Each point of $S$ lies in an affine open $V$ of the standard cover. The restriction of $c$ to $V$ is principal (`siegPre_pull_ringChange`), and step 1 classifies it. `siegelFamily_classified_of_local` glues these maps into one $f$.
3. *Uniqueness.* `siegelFamily_classifyingMap_unique`: two maps over $B_n$ along which $c$ is a pullback of $u$ are equal.

## In the Lean code

The theorem is in [SiegelFamilyExistsUniqueClassifyScheme.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SiegelFamilyExistsUniqueClassifyScheme.lean#L28). `SFam` is in [IsSeparatedOfIsQProjOver.lean](lean:Development/AbelianVarietyTheory/Definitions/ModuliSpaces/IsSeparatedOfIsQProjOver.lean#L18), and `SiegPB` in [Clauses.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/Clauses.lean#L50). The lemmas of steps 1 to 3 are statement forms whose proofs we have not opened; they are `SiegFG.siegPre_descends_fg`, `SiegelNoeth.classify_noetherian`, `SiegZar.classified_of_local` and `SiegUniq.eq_of_siegPB`. Almost all of the subtree is below `exists_classify_affine` (547 of 557 declarations), and most of that below the noetherian case.

The uniqueness lemma does not use that $c$ is principal. The existence step needs no hypothesis on $S$: the reduction to a finitely generated ring removes the need for noetherian or reduced bases.
