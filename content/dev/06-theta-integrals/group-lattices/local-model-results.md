---
id: local-model-results
title: The record of local model results, from Loc
kind: theorem
decl: Formalism.L2.G.local_model_results
module: Formalism.LocalToGlobal.GroupLattices.AdmissibleFamilyNoKernel
covers: 977
status: drafted
drafted_by: writer@claude
---
This theorem builds the record `Loc6` of seventeen local facts from the record `Loc`. One field comes from `Loc`. The other sixteen are proved lemmas, put in place by name. [LinkG from local data](/entry/link-of-local-closed/) uses the record twice: for the second theorem (`second_theorem_absolute_constant`) and, with `local_flatness_results`, for the first theorem (`loc8All_of`).

## Statement

`Loc` is the record with one field: `SecondTheoremReduced D` for each datum $D$ of type `D7`. `SecondTheoremReduced D` says: for all constants $C_\Lambda, C_k, C_{rk}, C_{\deg}$, the conditions `admitted` and two existence statements of constants imply `ConclusionE D`, the conclusion of [Statement E](/entry/stmt-e/).

**Theorem.** `Loc` implies `Loc6`.

The fields of `Loc6`, grouped:

- `p14R`: `SecondTheoremReduced D` for all $D$.
- `p39B`: `SecondPartClosed D` for all $D$. Under the conditions `AdmB D` there is $C_0 > 0$ such that for $C_\Lambda, C_k \ge C_0$ some positive $C_{rk}, C_{\deg}$ give `Conclusion2 D`.
- Three counting identities, for all $D$. Let $s(\lambda)$ be the number `stCount` of index sets `IsSt` for a dominant $\lambda \in \mathbb{Z}^n$.
  - (`rationalPlanesClauseThree`) The number of index sets for a sequence $\mu_0, \dots, \mu_N$ with dominant last term $\lambda$ is $\prod_{i<j} \frac{\lambda_i - \lambda_j + j - i}{j - i}$. This has the form of Weyl's dimension formula for $\mathrm{GL}_n$ (Fulton and Harris, *Representation Theory*, Lecture 6).
  - (`rationalPlanesClauseFour`) $s(\nu) = \sum_\mu s(\mu)$ for $\nu \in \mathbb{Z}^{m+1}$, over the $\mu \in \mathbb{Z}^m$ with $\nu_{i+1} \le \mu_i \le \nu_i$. This is a branching count by interlacing.
  - (`rationalPlanesClauseFive`) $s(\nu)\binom{b+m}{m} = \sum_\mu s(\mu)$, over the $\mu$ such that $\mu/\nu$ is a horizontal strip of size $b$, and the same with the strip below $\nu$. This is a Pieri count.
- Seven statements on Fock models and lattices (`DualHeightInclusion`, `BePerfect`, `LPOneEvery`, `FlatTop`, `DualHeightBasis`, `HLSpans`, `TestSide`) and the identity `WittIdent`, which do not mention $D$.
- Four conditions on each $D$: `FilteredProjectionCriterion`, `adm22`, `FewBadOrbits` and `LevelPrimesProviso`.

We have not unfolded the last twelve.

## Proof

The field `p14R` is `h.p14R`. Each other field is one named lemma:

- `p39B` is `SelectionLemmas.Pf.secondPartClosed`;
- the three counts are `weyl_dimension_formula_index_sets`, `branching_rule_count_form` and `pieri_rule_count_form`, through Gelfand-Tsetlin counts;
- the Fock model fields are the seven lemmas `Model.dualInclusionLattices` to `Model.testSide`, in the files of `FockModels`, and `wittIdentity_holds`;
- the last four are `joint_types_corollary_sentences`, `coarse_units_lemma`, `Model.fewBadOrbits` and `Model.products_sections_integral`.

## In the Lean code

The theorem is at [AdmissibleFamilyNoKernel.lean line 43](lean:Formalism/LocalToGlobal/GroupLattices/AdmissibleFamilyNoKernel.lean#L43). `Loc6` is at [PlaneCountTheoremWithConstants.lean line 1059](lean:Formalism/SharpRestriction/GrowthBounds/PlaneCountTheoremWithConstants.lean#L1059), and the three counts at [ValuationLowestDegreeRename.lean line 84](lean:Formalism/SharpRestriction/GrowthBounds/ValuationLowestDegreeRename.lean#L84).

- Only one field uses the hypothesis. `Loc` is supplied by [`loc_proved`](/entry/loc-proved/), from [Statement E](/entry/stmt-e/) through `criterion_restricted_of_closed`. That lemma ignores the two existence statements in `SecondTheoremReduced`.
- The field names do not describe the statements. "Rational planes clause three, four, five" are a dimension formula, a branching count and a Pieri count. The proof names say this.
- The three counts take an argument $D$ (written `_D`) and do not use it.
