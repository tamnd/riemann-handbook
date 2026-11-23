---
id: admissible-place-of-kernel-law
title: The admissible conditions at a place, from the first kernel law and the coupled last level
kind: theorem
decl: Formalism.L2.KerInert.AdmLoc2.admissible_place_of_kernel_law
module: Formalism.LocalToGlobal.InertKernelTheory.InertCoprimeLemmas.AdmissibleEntriesOfKernelLaw
covers: 473
status: drafted
drafted_by: writer@claude
---
This theorem specializes [`admissible_general_of_kernel_law`](/entry/admissible-general-of-kernel-law/) to the system `sysAt` of a chain of levels at a place $w$. That general lemma takes two of the 13 conditions of `admitted` as hypotheses. This theorem proves them from two instance lemmas and passes everything else along. Its only user is [`admissible_entries_of_kernel_law`](/entry/admissible-entries-of-kernel-law/).

## Statement

**Theorem.** If `TranslatesOfInertKernelAtPlace` holds, then `AdmAt2` holds.

`AdmAt2` is described in the [user entry](/entry/admissible-entries-of-kernel-law/). Under `CurveIn`, the theta series hypotheses below the maximal level, `XiIn`, `LawInLt`, `TiesAt` at the levels $j$ with $j + 1 < m$, and (if $m > 0$) a choice $l_p$ with `TiesC` and `HeckeC` at level $m - 1$, the pending datum $Y$ of `sysAt` is `admitted`.

## Proof

1. The number of levels of `sysAt` equals $m$, by `KA.fl_m`.
2. `admissible_third_instance` gives `adm3b` for `sysAt`: for $j < m$, the map `X.Kz j` sends each $F$ in `X.FQ j` into `X.FQ (j + 1)`.
3. If $m > 0$, `admissible_fourth_instance` turns the ties and $l_p$ into `ArchimedeanSignatureMatching`. If $m = 0$, that condition is vacuous: it quantifies over $j$ with $j + 1 < 0$ or $j + 1 = 0$, and there is no such $j$.
4. [`admissible_general_of_kernel_law`](/entry/admissible-general-of-kernel-law/) gives `admitted`.

## In the Lean code

The theorem is at [AdmissibleEntriesOfKernelLaw.lean](lean:Formalism/LocalToGlobal/InertKernelTheory/InertCoprimeLemmas/AdmissibleEntriesOfKernelLaw.lean#L79). `admissible_third_instance` is in SecondKernelInstances.lean (line 128) and `admissible_fourth_instance` in SecondKernelCoupled.lean (line 90). We have not opened their proofs.

- `ArchimedeanSignatureMatching` ([FormalGroupSystem.lean](lean:Formalism/SharpRestriction/GrowthBounds/FormalGroupSystem.lean#L587)) has no archimedean place and no signature. It says that `X.Kz j F` is a weighted sum of kernel values.
- The first kernel law is only passed on.
