---
id: local-nongeneric-bound-record-family
title: The local non-generic bound under all its names
kind: theorem
decl: GlobalTheory.local_nongeneric_bound_record_family
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.LocalNongenericBoundRecordFamily
covers: 461
status: drafted
drafted_by: writer@claude
---
This theorem states one local bound under the five names that the global records use. It is a pass-through. The content is in [`ngAt`](/entry/ng-at/), through its statement form [`hermitianDoubleCoset_amplitude_bound_local`](/entry/hermitian-double-coset-amplitude-bound-local/). Three theorems use the result: `closed_steps_equal_words`, `rowNGP_of_leaves` and `rowGen1P_of_siegelWeil_of_points`. All three lie below the step [HypsAlt is nonempty from the closed bound](/step/nonempty-hyps/).

## Statement

**Theorem.** Let $C \geq 39$. Then:

1. for all $k, r$ with $4r + 7 \leq k$, the bound $\mathrm{NonGenericLocalBound}(k, r, C)$ holds;
2. for each datum $D$ of type `D7`, the propositions `Conclusion1 D C`, `NonGenericLocalBoundOfLargeRank D C` and `adm5 D C` hold;
3. for each family `Fm` of type `FamP eps`, the propositions `FamilyNonGenericLocalBound Fm C` and `admF5 Fm C` hold.

$\mathrm{NonGenericLocalBound}(k, r, C)$ says: for every local model $M$ with `M.OK`, every Hermitian space $H$ of dimension $k + 2r + 1$ and every frame pair $P$ with `P.RelG (theta M)`, the bound `NGAt k P C` holds. [The entry for `ngAt`](/entry/ng-at/) states `NGAt`.

## Proof

Item 1 is `hermitianDoubleCoset_amplitude_bound_local` with its arguments in a new order. `Conclusion1 D C` is item 1 at the $(k, r)$ of $D$. The other names unfold to `Conclusion1`, for $D$ or for each member of the family.

## In the Lean code

The theorem is in [LocalNongenericBoundRecordFamily.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/LocalNongenericBoundRecordFamily.lean#L10). The only lemma it calls is `GlobalTheory.T.hermitianDoubleCoset_amplitude_bound_local`.

The second item states `Conclusion1 D C` three times: `NonGenericLocalBoundOfLargeRank` is defined as `Conclusion1`, and `adm5` is `stNG`, whose text in [CongruenceAtSplitFrobeniusHolds.lean](lean:Formalism/SharpRestriction/CuspSpanNormBounds/CongruenceAtSplitFrobeniusHolds.lean#L715) repeats `Conclusion1`. So `h3` is `h2` with no change.
