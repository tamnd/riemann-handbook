---
id: formal-thickening-formal-algebraisation
title: Grothendieck existence for morphisms and schemes, assembled
kind: theorem
decl: PositivityTheory.FormalThickening.formalAlgebraisation
module: Development.WeilBound.CoreStatements.TemperedRepresentationTheory.FormalAlgebraisation.Development
covers: 938
status: drafted
drafted_by: writer@claude
---
This theorem proves `FormalAlgebraisation`, the two Grothendieck existence statements over a complete Noetherian ring. [The literature entry](/entry/formal-algebraisation-of-literature/) states it in full and calls this theorem. This entry describes how the proof joins four lemmas. The lemmas rest on closed-subscheme forms of the existence theorem.

## Statement

The statement is `Morphisms ∧ Schemes`, as in [the literature entry](/entry/formal-algebraisation-of-literature/). We use its names: $R$ complete for $I$, $R_e = R/I^{e+1}$, $X$ proper, $Z$ separated, locally of finite type and quasi-compact, and a compatible family $f_e : Y_e \to Z$.

## Proof

The part `Schemes` is `formal_algebraisation_schemes` applied to `grothendieck_existence_closed_proj`. That input is `GEClosedProj`. Let $P$ be projective space $\mathbb{P}^N_R$. A compatible system of closed subschemes $C_e$ of the thickenings $P \times_R R_e$ comes from one closed subscheme $C' \subset P$.

The part `Morphisms` has two halves.

- Existence. `formal_morphism_existence` takes [grothendieck_existence_closed](/entry/grothendieck-existence-closed/) (`GEClosed`) and `iso_of_thickenings` (`IsoOfThick`), and gives $g : X \to Z$ that restricts to each $f_e$. `GEClosed` is the closed-subscheme statement for a separated, locally finite type and quasi-compact $P$, when $C_0$ is proper (`IsProper` of $C_0$ over the base of the first thickening). Then $C'$ is proper over $R$. `IsoOfThick` says: a proper map $p : C \to X$, with $X$ proper over $R$, that is an isomorphism over every $R_e$ is an isomorphism. These inputs fit the usual argument: algebraize the graphs of the $f_e$ inside $X \times_R Z$, then show that the projection to $X$ is an isomorphism. We did not open `exists_hom_of_thickenings`, so we have not checked that it argues this way.
- Uniqueness. If $g'$ also restricts to each $f_e$, then $g'$ and $g$ agree on every $Y_e$. `formal_morphism_uniqueness` then gives $g' = g$.

The theorem itself only passes the inputs to these lemmas. The content is in the lemmas and in [ge-closed](/entry/ge-closed/), which proves `GEClosed`.

## In the Lean code

The theorem is in [Development.lean](lean:Development/WeilBound/CoreStatements/TemperedRepresentationTheory/FormalAlgebraisation/Development.lean#L17). `GEClosed`, `GEClosedProj` and `IsoOfThick` are in [GEClosedProj.lean](lean:Development/WeilBound/CoreStatements/TemperedRepresentationTheory/FormalAlgebraisation/GEClosedProj.lean#L13). The statement is in [FormalAlgebraisation.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/FormalAlgebraisation.lean#L43).

`formal_morphism_existence` is a wrapper that calls `MorphismAlgebraisation.exists_hom_of_thickenings`. `formal_morphism_uniqueness` uses `FormalUniq.eq_of_comp_thickenings_eq`, and `formal_algebraisation_schemes` is `FormalAlg.schemes_of_closedProj`. The three inputs are proved by `GE.geClosed`, `GE.geClosedProj` and `IsoThick.isoOfThick`. We did not open these proofs.
