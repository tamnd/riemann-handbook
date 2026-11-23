---
id: theorem-of-local-lemmas
title: Local lifting theorem C with constant 25, with the Wach vector bound as a hypothesis
kind: theorem
decl: Formalism.MainNotions.RamifiedCoefficientChains.Asm.theorem_of_local_lemmas
module: Formalism.SharpRestriction.LevelLetterCocycles.FrobeniusLiftLemmasOfAdmitted
covers: 670
status: drafted
drafted_by: writer@claude
---
This theorem is the general form of [theorem C with constant 25 from five local hypotheses](/entry/theorem-of-literature-hypotheses/). It takes the first of the three parts of that proof, the bound from cocycles to Wach vectors, as a hypothesis. Its only user is that parent entry, which supplies the hypothesis by `local_lemmas_of_literature`. The parent entry describes the conclusion and the proof.

## Statement

Let $D$ be a datum with Wach data $HW$, Fontaine data $F$ and comparison data $C_m$, and let $C_R, C_A, C_B, C_K$ be reals. Assume:

1. (`h12`) if the 19 conditions `admitted D HW F Cm CR CA CB CK` hold, then `cocyclesToWachVectorsBoundAtGoodExtensions D HW F` holds;
2. (`adm23`) the Hodge-Tate jumps of the middle term of a short exact sequence of crystalline lattices are the jumps of the two ends;
3. (`LetterConditionGlobal`) the letter condition on each Wach module.

**Theorem.** Then `Stmt D HW F Cm 25 CR CA CB CK` holds: the 19 admitted conditions imply `ConclusionL` with constant 25.

The bound in hypothesis 1 is `CocyclesToWachVectorsBound`, asked at each prime $\ell$ and each good triple $(K, 1, L)$. We have not unfolded it.

## Proof

The proof assumes `admitted` and builds the three parts that `stmt_of_lemmas` asks for. Part 1 is hypothesis 1 applied to `admitted`. Part 2 is `lattice_bound_three_six_of` at each good triple, from `frobenius_lift_lemmas_of_admitted` and `steps6_of`. These use `h2_bound_of_admitted`, `dual_lemma_of_admitted`, `lemmaDN0_L` and `lemmaGs_rec`. Only `lemmaGs_rec` uses hypotheses 2 and 3. Part 3 is `rhoLift_of_Adm`. The rest is in `stmt_of_lemmas`.

## In the Lean code

The theorem is at [FrobeniusLiftLemmasOfAdmitted.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/FrobeniusLiftLemmasOfAdmitted.lean#L272). `lemmaGs_rec` is at [line 231](lean:Formalism/SharpRestriction/LevelLetterCocycles/FrobeniusLiftLemmasOfAdmitted.lean#L231) and `rhoLift_of_Adm` at [line 135](lean:Formalism/SharpRestriction/LevelLetterCocycles/FrobeniusLiftLemmasOfAdmitted.lean#L135). `stmt_of_lemmas` is at [LatticeBoundsOfThreeParts.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/LatticeBoundsOfThreeParts.lean#L592).

- The theorem and its parent differ only in hypothesis 1. The parent replaces it with three literature hypotheses.
- `lemmaDN0_L` takes the eleventh admitted condition directly, as the projection `hA.2.2.2.2.2.2.2.2.2.2.1`.
