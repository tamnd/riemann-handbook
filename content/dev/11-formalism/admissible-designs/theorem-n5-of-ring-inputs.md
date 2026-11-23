---
id: theorem-n5-of-ring-inputs
title: The congruence length bound from the Selmer tuple on each ring datum
kind: theorem
decl: Formalism.MainNotions.N.K.Final.theorem_n5_of_ring_inputs
module: Formalism.AdmissibleDesigns.StatementOneBChangedOfOpen
covers: 575
status: drafted
drafted_by: writer@claude
---
This theorem proves the bound `GlobalLatticeIndexTheorem` on $v_{cc}(\pi)$ from one main hypothesis: the tuple `SelmerInequalityThree` holds for the normalized family $r^{\mathrm{N}}$ on each ring datum. [`theorem_n5_of_open_b`](/entry/theorem-n5-of-open-b/) supplies that hypothesis. This theorem replaces $r$ by $r^{\mathrm{N}}$, builds one ring datum with [`normalized_ring_data`](/entry/normalized-ring-data/), and then applies `selmer_inequality_three`. It is assembly. It does no new estimate.

## Statement

The notation is that of [the congruence length bound from the local inputs](/entry/theorem-n5-from-inputs/). The family $r^{\mathrm{N}}$ (`Norm.rN`) is $r$ away from $\pi$ and $\rho_\pi \oplus \chi_1 \oplus \dots \oplus \chi_t$ at $\pi$.

**Theorem.** Assume `admG1`, `admG2`, `admG3`, `TameGeneratorConditions`, `admG6`, `FamilyContinuous`, `SemisimpleDecomposition`, `adm51` and `SelfGood`. Assume that `OnRing` holds for `SelmerInequalityThree`: if `LengthBoundAtPlaces`, `LiftExponentAtPlaces` and `admTB` hold for $r^{\mathrm{N}}$ and $\pi \in Z$, then for each $g_0, e_B, e_1, s$ and each ring datum `Dd` with `RingDef`, continuity, `Dd.Top` and a rank-one first block, the tuple holds. Then `LengthBoundAtPlaces`, `LiftExponentAtPlaces` and `admTB` for $r$ imply `GlobalLatticeIndexTheorem`.

## Proof

1. **Move to $r^{\mathrm{N}}$.** `row_normalized`, `lift_normalized` and `row_bound_normalized_lattice` move the three premises from $r$ to $r^{\mathrm{N}}$, with the help of `SemisimpleDecomposition`.
2. **Reduce to a display.** `theorem_of_display_and_g2` gives the bound from `SelmerLengthInequality`, under five conditions. The proof uses only $\pi \in Z$. `SelmerLengthInequality` names $\rho$ and not $r$, so it is enough to prove it for $r^{\mathrm{N}}$.
3. **Choose the design.** `design_normalized_of_admitted` turns `adm51` and $\pi \in Z$ into an element $g_0$ with cyclotomic character $1 + \ell^{s_0}u_0$, and matrices $e_B, e_1, s$ with `IdemHyp` and `DistinctEigenvalueCornerPerturbation`. We did not unfold its proof.
4. **Build the ring datum.** `normalized_ring_data` gives `Dd` with `RingDef`, the instances, `Dd.Top` and `RealDisplayAllK`. Its inputs are `NormAt` for $r^{\mathrm{N}}$, `admG1` moved to $r^{\mathrm{N}}$, and the third part of `admG3` (the residual image of $\rho_\pi$ spans all matrices).
5. **Conclude.** `selmer_inequality_three` takes `RealDisplayAllK`, `PrimHyp`, the cyclotomic equation, `admG6`, the lift bound, `SelfGood` and the tuple from the hypothesis. It gives `SelmerLengthInequality`.

## In the Lean code

The theorem is in [StatementOneBChangedOfOpen.lean](lean:Formalism/AdmissibleDesigns/StatementOneBChangedOfOpen.lean#L271), with `OnRing` at line 139. `theorem_of_display_and_g2` is in [KernelLengthHigherColumns.lean](lean:Formalism/AdmissibleDesigns/KernelLengthHigherColumns.lean#L185) and `selmer_inequality_three` in [TheoremFromNormalizedOpenThree.lean](lean:Formalism/AdmissibleDesigns/TheoremFromNormalizedOpenThree.lean#L129).

The proof ignores four of the five conditions of the display (line 282). It discards with `-` the fact that $g_0$ lies in an inertia group above $\ell$ (line 285) and the equation $v_{cc}(\pi) = \operatorname{length}(\mathcal{O}/cc_\pi)$ from `normalized_ring_data` (line 286). The first two parts of `admG3` are not used.
