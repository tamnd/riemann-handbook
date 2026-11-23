---
id: forms-map-at-every-true-column-member
title: The forms map at every true column member
kind: theorem
decl: GlobalTheory.Mem.Col2.TC.formsMap_at_every_trueColumnMember
module: Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.FormsMapAtEveryTrueColumnMember
covers: 455
status: drafted
drafted_by: writer@claude
---
This theorem proves `Conclusion6` at every word of the datum that a true column input builds. It checks the three hypotheses of [the forms map from a symmetric comparison](/entry/forms-map-of-symmetric-comparison-lower-map-finite-char/) for true columns, and then applies that theorem. It is used under its second name [`aux_of_ok_of_pins`](/entry/aux-of-ok-of-pins/), and the result goes up through [the forms map at a bundle point](/entry/constructed-point-reference-chain-word-forms-map/) to the field `aPt0` of [HypsAlt](/step/hyps-alt-def/).

## Statement

Let $B$ be a base, $X$ a `PreX` over it, and $I$ a true column input (`TC B X`, which is `ColIn B X`) with `I.Ok` and the pins `TC.Pins B X`. Let $l$ be the laws `I.Laws` and $Z$ later stages over the columns `I.cols l`. Let $D$ be the datum `I.rec7 l Z`.

**Theorem.** `Conclusion6 D u` holds for every word $u$ of $D$.

`Conclusion6 D u` says: the class map of the member forms at $u$ is injective, its maps of stabilizers are bijective, and the period map on forms is rational, integral and bounded by an explicit constant. [The forms map from a symmetric comparison](/entry/forms-map-of-symmetric-comparison-lower-map-finite-char/) gives the five clauses in full.

## Proof

Fix $u$.

1. **Symmetric tied forms.** [`colsTiedSym_std`](/entry/cols-tied-sym-std/) gives a symmetric tied column system $C$ for $D$ whose forms are standard at every word (`I.StdC l Z C`). Let $T_f$ be its forms at $u$, a `FormsTiedSym D u Ch chOf`. The lemma also gives a level condition, which this proof drops.
2. **The lower map tie.** `LowerTie.lowerMap_tie` turns the standard property of $T_f$ into `LowerMapTieS T_f`. This says how the lower map of the period data acts on the coordinates of $T_f$: under a unit determinant condition, it is given by the branching tensor `brTen D u` applied to the coordinate polynomial.
3. **The branching norms.** `beOnTie_true` proves `BeOnTie D u`: for each $\tau$, the number $\beta(\tau)$ (`beOn`) of the member forms equals the operator norm of the branching map `brOne` from the weight $\lambda_\tau$ to the weight $\sigma_\tau$.
4. **Roots of unity.** `trueCols_exists_primitiveRoots` shows that the coefficient field `D.what₂.LL` contains a primitive $g_i$th root and a primitive $(g_i - 1)$th root of unity, for $i = 0, 1$, where $g_0, g_1$ are the two primes `D.host.g`.
5. **A finite character.** `chi_last_step_finite_order_symTie` uses step 4 to show that the level character $\chi$ of $T_f$ at the top step $m$ has finite order, with $n = \prod_i g_i (g_i - 1)$, and takes values in the image of `D.what₂.LL`.

Steps 2, 3 and 5 are the three hypotheses of [the forms map from a symmetric comparison](/entry/forms-map-of-symmetric-comparison-lower-map-finite-char/), which gives `Conclusion6 D u`.

## In the Lean code

The theorem is in [FormsMapAtEveryTrueColumnMember.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/FormsMapAtEveryTrueColumnMember.lean#L15). The lemmas it calls:

- `GlobalTheory.Mem.Col2.TC.colsTiedSym_std`, in [ExistsStandardColumnComparisonsTrueColumns.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsStandardColumnComparisonsTrueColumns.lean#L20).
- `GlobalTheory.Mem.Col2.LowerTie.lowerMap_tie`, in [LowerMapTie.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/LowerMapTie.lean#L14).
- `GlobalTheory.Mem.Col2.TC.beOnTie_true`, in [BranchingNormIdentityTrueColumnsMembers.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/BranchingNormIdentityTrueColumnsMembers.lean#L62).
- `GlobalTheory.trueCols_exists_primitiveRoots`, in [ExistsPrimitiveRootsCoeffFieldTrueColumns.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/ExistsPrimitiveRootsCoeffFieldTrueColumns.lean#L10).
- `GlobalTheory.chi_last_step_finite_order_symTie`, in [ChiLastStepFiniteOrderSymTie.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/ChiLastStepFiniteOrderSymTie.lean#L13).
- `GlobalTheory.RedPt0.formsMap_of_symmetricComparison_lowerMap_finiteChar`.

We have read the statements of the first five lemmas, not their proofs. `beOnTie_true` ignores both `I.Ok` and the pins (its proof is `fun I _ _ l Z u => ...`), and `trueCols_exists_primitiveRoots` does not take the pins. `colsTiedSym_std` (size 417) has a second user, so it is not among the 455 declarations that this theorem dominates.
