---
id: first-theorem-threshold-functions
title: The base-level projection bound, with thresholds as functions
kind: theorem
decl: Formalism.MainNotions.G.first_theorem_threshold_functions
module: Formalism.SharpRestriction.GrowthBounds.PlaneCountTheoremWithConstants
covers: 315
status: drafted
drafted_by: writer@claude
---
This theorem restates [the uniform base-level projection bound](/entry/first-theorem-uniform-thresholds/) with the thresholds as functions of $C_0$. The proof is the axiom of choice and nothing more. The result is used below the trunk step [EveryCharacter from theta integrals and local matching](/step/theta-local-matching/). Below it are 315 declarations.

## Statement

`Conclusion2` $(C_0, C_H, C)$ is the base-level projection bound of [`theorem_I_closed_form_holds`](/entry/theorem-i-closed-form-holds/): a function $\kappa \ge 0$ with mean at most $C|T|N_1/Y$ and the property `LPprime`. It does not depend on the datum $D$.

**Theorem.** Assume `ExtremalProjectorTools` and `Loc8All`. Then there are $T_0 > 0$ and functions $T_2, C \colon \mathbb{R} \to \mathbb{R}$ such that for each $C_0 \ge T_0$ we have $T_2(C_0) > 0$, $C(C_0) > 0$, and `Conclusion2` $(C_0, C_H, C(C_0))$ for all $C_H \ge T_2(C_0)$ and all data $D$. [`first_theorem_admitted_closed`](/entry/first-theorem-admitted-closed/) describes the two hypotheses.

## Proof

`first_theorem_uniform_thresholds` gives $T_0$ and, for each $C_0 \ge T_0$, numbers $T_2$ and $C$. The tactic `choose!` makes $T_2$ and $C$ into functions of $C_0$.

## In the Lean code

The theorem is in [PlaneCountTheoremWithConstants.lean](lean:Formalism/SharpRestriction/GrowthBounds/PlaneCountTheoremWithConstants.lean#L1282). It has three users:

- `linkG_top` (line 1790 of the same file), through `first_theorem_closed_form` (line 1761).
- `link_of_local_closed` in [AdmissibleFamilyNoKernel.lean](lean:Formalism/LocalToGlobal/GroupLattices/AdmissibleFamilyNoKernel.lean#L272), also through `first_theorem_closed_form`.
- `GlobalTheory.EX.RangeOne.rangeOne_abs` in [TensorOfPairLift.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/TensorOfPairLift.lean#L637), with the two records filled.

The proof uses `classical` and `choose!`, so $T_2$ and $C$ are not computable. `first_theorem_closed_form` needs them as functions, because it bounds $\max(2T_2(c), 2C(c))$ over a list of constants $c$ of a family.
