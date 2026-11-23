---
id: admissible-general-of-kernel-law
title: The thirteen admissible conditions for a general system, from the first kernel law
kind: theorem
decl: Formalism.L2.KerInert.AdmLoc2.admissible_general_of_kernel_law
module: Formalism.LocalToGlobal.InertKernelTheory.InertCoprimeLemmas.AdmissibleEntriesOfKernelLaw
covers: 435
status: drafted
drafted_by: writer@claude
---
This theorem assembles the 13 conditions of `admitted` for the pending datum of a general system $X$ at an inert prime $p \ge 5$. It is an assembly. Each condition comes from one lemma or one hypothesis, and two conditions are hypotheses that it passes straight through. Its only user is [`admissible_place_of_kernel_law`](/entry/admissible-place-of-kernel-law/), which proves those two for the system at a place.

## Statement

Let $Y$ be the pending datum `pendG` of a system $X$ over $p$, built from the theta data $F$ = `FrecG ...`.

**Theorem.** If `TranslatesOfInertKernelAtPlace` holds, then `AdmGen2` holds.

`AdmGen2` says: assume `CurveIn` ($p \ge 5$, $p$ inert, a good model over the Witt vectors, and the conditions on $c$, $\delta$, $\chi$ and $\lambda$), the theta series hypotheses below the maximal level, `XiIn`, `LawInLt`, `adm3b` for $X$ and `ArchimedeanSignatureMatching` for $Y$. Then $Y$ is `admitted`.

## Proof

The conditions, in the order of `admitted`:

1. `adm1` (a Dwork lemma at every prime) is `positivity_condition_holds`. It does not depend on $X$.
2. `adm2`, `adm2b` and `adm3` come from the first kernel law, applied to the hypotheses of `CurveIn` and of the theta series data. This is the only use of that law.
3. `adm2c` (`BeProp` for the series `beLT`) is `admissible_second_inert`.
4. `adm3b` and `ArchimedeanSignatureMatching` are hypotheses.
5. `adm5` comes from `invariance_iff_additive_maps_exist` and the hypothesis `XiIn`.
6. `MinkowskiCounting` comes from `LawInLt` by `admissible_stabilizer_of_law`. That lemma extends the theta series by $0$ outside the levels $j < m$ and the lattice tuples. Then it applies `kapLaw_of_stabLaw` and `ker_law`.
7. `adm6` is `up_down_adjoint`. It holds for every pending datum.
8. `adm7` is [`pending_tuple_admissible`](/entry/pending-tuple-admissible/).
9. `adm8` is `admissible_all_levels`. It holds for every system.
10. `adm11` is `admissible_eleventh_inert`.

## In the Lean code

The theorem is at [AdmissibleEntriesOfKernelLaw.lean](lean:Formalism/LocalToGlobal/InertKernelTheory/InertCoprimeLemmas/AdmissibleEntriesOfKernelLaw.lean#L62). `AdmGen2` is in [ThetaSeriesDataHypothesesBelowMaximalLevel.lean](lean:Formalism/LocalToGlobal/InertKernelTheory/ThetaSeriesDataHypothesesBelowMaximalLevel.lean#L57). The first kernel law is in [TranslatesOfInertKernelAtPlace.lean](lean:Formalism/LocalToGlobal/InertKernelTheory/TranslatesOfInertKernelAtPlace.lean#L20). The conditions are in [FormalGroupSystem.lean](lean:Formalism/SharpRestriction/GrowthBounds/FormalGroupSystem.lean#L546).

- Two of the 13 conditions are assumed. So `AdmGen2` alone proves nothing about them.
- `positivity_condition_holds` proves `adm1`, a Dwork lemma. The name speaks of positivity. Three theorems in the library have this name (in MultisetValuation/PositivityConditionHolds.lean, RootWeights/PositivityConditionHolds.lean and CountingStatementReduction.lean).
- `MinkowskiCounting` is the invariance of the kernels under the level groups. It has no count.
- `pendG` is an abbreviation for `pendT X ... (FrecG ...)` ([StatementAdmAt.lean](lean:Formalism/LocalToGlobal/InertKernelTheory/StatementAdmAt.lean#L21)), the datum of the first kernel law.
- We have not opened the proofs of the lemmas in items 1, 3, 5, 7, 8, 9 and 10.
