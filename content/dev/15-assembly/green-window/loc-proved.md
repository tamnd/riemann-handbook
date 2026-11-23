---
id: loc-proved
title: The local input Loc
kind: theorem
decl: Formalism.L2.G.loc_proved
module: Formalism.LocalToGlobal.GroupLattices.AdmissibleFamilyNoKernel
covers: 2162
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement `Loc`, the local input of [`linkG_concrete_noKer`](/entry/link-g-concrete-no-ker/). [`linkG_concrete5`](/entry/link-g-concrete5/) puts it in that slot. The proof is a short conversion. The real content is in [`stmtE`](/entry/stmt-e/), which dominates 2,159 of the 2,162 declarations below this theorem.

## Statement

`Loc` is a structure with one field, `p14R`: for each datum $D$ (the type `D7`), `SecondTheoremReduced D` holds. That statement says: for all constants $C_{La}, C_k, C_{rk}, C_{deg}$, if `admitted D CLa Ck Crk Cdeg` holds, and if two further conditions hold (positive constants with `SourceCleaning.aux₃`, and positive constants with `PlaneGramData.aux₃` for all large $C_H$), then `ConclusionE D` holds.

Here `admitted` is a conjunction of 37 named conditions on $D$. `ConclusionE D` says: there is $C_0 > 0$ such that `aux₃ D C` holds for each $C \ge C_0$. `aux₃ D C` is a long statement about a prime $p \ge 13$, discrete valuation rings in an unramified quadratic setting, orbit and weight hypotheses, and numerical inequalities, with the conclusion `LPprime`. We have not unfolded `LPprime`.

**Theorem.** `Loc` holds.

## Proof

Let $D$ be a datum. `stmtE D` gives `ClosedFormOfAdmitted D`: for all constants, `admitted` implies `ConclusionE D`. The lemma `criterion_restricted_of_closed` turns this into `SecondTheoremReduced D`: it ignores the two further conditions and applies `stmtE D` to the constants and to the proof of `admitted`. So `SecondTheoremReduced` is weaker than what `stmtE` proves.

## In the Lean code

The theorem is in [AdmissibleFamilyNoKernel.lean](lean:Formalism/LocalToGlobal/GroupLattices/AdmissibleFamilyNoKernel.lean#L284), and `Loc` at line 36 of the same file. `SecondTheoremReduced` and `criterion_restricted_of_closed` are in [PlaneCountTheoremWithConstants.lean](lean:Formalism/SharpRestriction/GrowthBounds/PlaneCountTheoremWithConstants.lean#L1020). `stmtE` is in [AevalValuation.lean](lean:Formalism/SharpRestriction/GrowthBounds/AevalValuation.lean#L13). `admitted`, `ConclusionE`, `ClosedFormOfAdmitted` and `aux₃` are in the namespace `tableLineDegreeFive`, in [TableLineDegreeFive.lean](lean:Formalism/SharpRestriction/GrowthBounds/TableLineDegreeFive.lean#L30).

Two odd points:

- `aux₃` takes the datum as `_D` and never uses it. So `ConclusionE D` is the same statement for every $D$, and $D$ enters `SecondTheoremReduced D` only through its hypotheses.
- The two further conditions in `SecondTheoremReduced` are never used.

In this file, `Loc` is used only through the field `p14R`, in `local_model_results`. The lemmas `extremal_projector_tools_of_loc` and `local_flatness_results` take `Loc` and do not use it.
