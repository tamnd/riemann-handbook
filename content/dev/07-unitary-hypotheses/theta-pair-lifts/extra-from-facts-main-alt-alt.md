---
id: extra-from-facts-main-alt-alt
title: The commuting endomorphism and the congruence length bound from the norm choice facts
kind: theorem
decl: GlobalTheory.ExtraFromFacts.main_alt_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ImportsExtraAlt
covers: 3711
status: drafted
drafted_by: writer@claude
---
This theorem gives constants $C \ge 0$ and $C_T$ for which the two facts `ExtraAlt D C CT` hold at each datum $D$ that satisfies the norm choice facts and the four ties. Its copy [`exists_const_tieChi_bound_of_facts`](/entry/exists-const-tie-chi-bound-of-facts/) is the first step of [the bound LinkN for one family](/entry/link-n-of-tw-good-galois-preconditions/), where it gives the hypothesis `FactsFAlt` of each cut family. This is in branch 1 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). Below this theorem are 3,711 declarations.

## Statement

Let `Hypotheses₂` be the record of seven named inputs of `GlobalTheory.NLink` (Fontaine's $B_{\mathrm{cris}}$, global Artin reciprocity, local Bloch-Kato, local Tate duality, the local Euler characteristic, local finiteness and an integral result of Bhatt-Scholze). `NormChoiceFacts D n` and `Tie4 D` are as in [`NormFromFacts.main_alt_alt`](/entry/norm-from-facts-main-alt-alt/).

`ExtraAlt D C CT` is the conjunction of two statements.

1. `CommutingEndomorphismCondition D`: at each local index $i$ with `TwLoc D i` and $\ell_i$ outside the set `gset D`, there is an endomorphism $\alpha$ of the Hecke module $M_i$ that commutes with the Hecke algebra, acts on each eigenvector of a good eigensystem by the integer $N$ (`restRowsFiniteGroupCard`), and acts by $0$ on each eigenvector of a system in $Z_i$ that is not good.
2. `PairedCharacterConditionAlt D C CT`: the bound on the congruence length $\eta_i$ by $\sum_\pi m(\pi) R(\pi)$, stated in full in [the entry with its proof](/entry/closing-local-inputs-main-alt-alt/).

**Theorem.** Assume `Hypotheses₂`. Then there are $C \in \mathbb R$ and $C_T \in \mathbb N$ with $C \ge 0$ such that for each datum $D$ and norm choice $n$, if `NormChoiceFacts D n` and `Tie4 D` hold, then `ExtraAlt D C CT`.

## Proof

1. [`exists_bound_tieChi_of_prints`](/entry/exists-bound-tie-chi-of-prints/) gives $C_T$ with the bound `PairedCharacterConditionAlt D (8 C_T) C_T`. Set $C = 8 C_T$, so $C \ge 0$. This is the second fact.
2. `no_cut_passes_of_artin_reciprocity` turns `GlobalArtinReciprocity` into `NoCutStatement`, a conjunction of sixteen step statements. Its second part `StepCentral`, applied to its first part `CentralIdemCoeff`, gives `CentralElt D`: at each $i$ there is a central element of a group algebra over $O_i$ whose image is $N$ times a product, over all pairs $(k, v)$, of elements `atPlace (eSer …)`.
3. `commutingEndomorphismCondition_of_serLoc` gives the first fact from `EigSpan`, `CentralElt D`, `SerLoc`, and five fields of `NormChoiceFacts`: `provisionFortyOne`, `tieLab`, `tie0`, `adm1` and `adm5`.

The second fact covers most of the subtree: 3,258 of the 3,711 declarations are below step 1.

## In the Lean code

The theorem is at [ImportsExtraAlt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ImportsExtraAlt.lean#L18), and `ExtraAlt` at [BoundAtTwoThreeFamilyFon.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BoundAtTwoThreeFamilyFon.lean#L22). The lemmas it calls:

- `exists_bound_tieChi_of_prints`, a copy of [`NormFromFacts.main_alt_alt`](/entry/norm-from-facts-main-alt-alt/).
- `no_cut_passes_of_artin_reciprocity` and `commutingEndomorphismCondition_of_serLoc`, whose proofs we have not opened.

Odd points:

- `ExtraAlt` is `Extra` of [BoundAtTwoAndThreeForFamily.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/BoundAtTwoAndThreeForFamily.lean#L51) with `aux₃` replaced by `PairedCharacterConditionAlt`, which drops the hypothesis `SetSQ`.
- `StepCentral` takes a pending datum `Pend D` as an argument and does not name it in its conclusion `CentralElt D`.
- The module name `ImportsExtraAlt` describes the imports, not the theorem. The parts `tieChi` and `TieInePoly` of `Tie4` are used only in step 1.
