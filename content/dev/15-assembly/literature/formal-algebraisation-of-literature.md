---
id: formal-algebraisation-of-literature
title: Grothendieck's formal existence theorem, as a literature input
kind: theorem
decl: UpperTheory.LiteratureTheorems.formal_algebraisation_of_literature
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.EveryCharacterOfLiteratureOfVWin
covers: 939
status: drafted
drafted_by: writer@claude
---
This theorem gives the statement `FormalAlgebraisation`. It takes a proof $O$ of [OpenLiteratureStatements](/step/open-literature-statements-def/) and does not use it. The proof is one term, [`formalAlgebraisation`](/entry/formal-thickening-formal-algebraisation/), and that entry has the real content. The result fills the field `q18` of the bundle [PublishedHodgeBundleTheorems](/step/published-results-arithmetic/). Below this theorem are 939 declarations.

## Statement

Let $R$ be a Noetherian ring, complete for the $I$-adic topology. Write $R_e = R/I^{e+1}$. `FormalAlgebraisation` is the conjunction of two parts.

1. `Morphisms`. Let $X$ be proper over $R$, and let $Z$ be separated, locally of finite type and quasi-compact over $R$. Let $Y_e = X \times_R R_e$, with compatible maps. Then each compatible family of $R$-maps $f_e \colon Y_e \to Z$ comes from a unique $g \colon X \to Z$.
2. `Schemes`. Let $Y_e$ be proper over $R_e$ with $Y_e = Y_{e+1} \times_{R_{e+1}} R_e$. Let $N_e$ be compatible line bundles, with $N_0$ relatively ample. Then there are $X$ proper over $R$ and a relatively ample line bundle $M$ with $Y_e = X \times_R R_e$ and $N_e \cong M|_{Y_e}$.

These are Grothendieck's existence theorems, EGA III$_1$, Théorème 5.4.1 for morphisms and Théorème 5.4.5 for schemes (Publ. Math. IHÉS 11, 1961). We have not unfolded `RelAmple` or `LB`.

## Proof

Apply `PositivityTheory.FormalThickening.formalAlgebraisation`. The argument $O$ is not used.

## In the Lean code

The theorem is at [EveryCharacterOfLiteratureOfVWin.lean line 381](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L381). The statement is in [FormalAlgebraisation.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/FormalAlgebraisation.lean#L17). The proof below is in [Development.lean](lean:Development/WeilBound/CoreStatements/TemperedRepresentationTheory/FormalAlgebraisation/Development.lean#L16). It joins `formal_algebraisation_schemes`, `formal_morphism_existence` and `formal_morphism_uniqueness`. Their inputs are `grothendieck_existence_closed` and `grothendieck_existence_closed_proj`, which we have not unfolded.

Odd point. The name says "of literature", but the code proves the statement and ignores $O$.
