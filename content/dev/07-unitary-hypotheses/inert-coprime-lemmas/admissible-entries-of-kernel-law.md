---
id: admissible-entries-of-kernel-law
title: The admissible entries at a place, from the first kernel law and the ties at every level
kind: theorem
decl: Formalism.L2.KerInert.AdmLoc2.admissible_entries_of_kernel_law
module: Formalism.LocalToGlobal.InertKernelTheory.InertCoprimeLemmas.AdmissibleEntriesOfKernelLaw
covers: 576
status: drafted
drafted_by: writer@claude
---
This theorem is the reduction behind [`admissible_entries_small_chain`](/entry/admissible-entries-small-chain/), its only user. It assumes the first kernel law and proves `AdmAtEnt2`. Its own work is small: it changes the form of one hypothesis, the ties between levels, and then calls [`admissible_place_of_kernel_law`](/entry/admissible-place-of-kernel-law/).

## Statement

We use the names of the parent entry. Let $m$ be the length of the chain of levels, and let $Y$ be the pending datum of the system $X$ at the place $w$.

**Theorem.** If `TranslatesOfInertKernelAtPlace` holds, then `AdmAtEnt2` holds.

The two statements `AdmAtEnt2` and `AdmAt2` have the same data and the same first four hypotheses (`CurveIn`, the theta series hypotheses below the maximal level, `XiIn` and `LawInLt`), and the same conclusion: $Y$ is `admitted`. They differ only in the ties. `AdmAtEnt2` asks for maps $\iota$, $R_d$, $S_r$ with `TiesAt` at every level $j < m$. `AdmAt2` asks for `TiesAt` only at the levels $j$ with $j + 1 < m$. At the last level $m - 1$, when $m > 0$, it asks for a choice of representatives $l_p$ with `TiesC` and `HeckeC`.

## Proof

1. `admissible_stabilizer_of_law` turns `LawInLt` into `MinkowskiCounting` for $Y$, the invariance of the kernels under the stabilizers.
2. For $j + 1 < m$, the ties are the hypothesis itself.
3. Let $m > 0$. `coupled_section_exists` gives $l_p$: a section of the classes at level $m - 1$, with values in the representatives of $Y$.
4. `coupled_compatibility_at_place` turns $l_p$ and `TiesAt` at level $m - 1$ into `TiesC`.
5. `hecke_coupled_entry` turns $l_p$, step 1 and the stabilizer part `TieStabAt` of `TiesAt` at level $m - 1$ into `HeckeC`. `HeckeC` says that two sums over the classes, weighted by the inverse sizes of the stabilizers, agree. The first sums kernel values over the edges from each representative. The second takes the kernel at the image of $F$ under the operator `X.Tm`.
6. [`admissible_place_of_kernel_law`](/entry/admissible-place-of-kernel-law/) gives `admitted`.

## In the Lean code

The theorem is at [AdmissibleEntriesOfKernelLaw.lean](lean:Formalism/LocalToGlobal/InertKernelTheory/InertCoprimeLemmas/AdmissibleEntriesOfKernelLaw.lean#L91). `AdmAtEnt2` and `AdmAt2` are in [ThetaSeriesDataHypothesesBelowMaximalLevel.lean](lean:Formalism/LocalToGlobal/InertKernelTheory/ThetaSeriesDataHypothesesBelowMaximalLevel.lean#L71). The three lemmas of steps 3 to 5 are in SecondKernelCoupled.lean (lines 104, 138 and 151), and `TiesC`, `HeckeC` are in [SecondKernelCoupledLastLift.lean](lean:Formalism/LocalToGlobal/InertKernelTheory/SecondKernelCoupledLastLift.lean#L38).

- The first kernel law is not used here. It is passed on to `admissible_place_of_kernel_law`.
- `admissible_stabilizer_of_law` is called twice on the same data: here and inside [`admissible_general_of_kernel_law`](/entry/admissible-general-of-kernel-law/).
- We have not opened the proofs of the three lemmas of steps 3 to 5.
