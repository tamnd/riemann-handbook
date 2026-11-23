---
id: jacquet-rallis-unit-match-all-ranks
title: The Jacquet-Rallis fundamental lemma for unit functions (statement file)
kind: theorem
decl: GlobalTheory.T.jacquetRallisUnitMatch_all_ranks
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.JacquetRallisUnitMatchAllRanksStatement
covers: 1358
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the Jacquet-Rallis fundamental lemma for unit functions in all ranks](/entry/unit-match-all/). The real content is in [unit matching from the quadratic Weil representation](/entry/unit-match-of-weil-field/), which does the induction on the rank. Its place in the spine is below [EveryCharacter](/step/every-character/). Below it are 1,358 declarations of the proof.

## Statement

For every $r \geq 0$, $\mathrm{UnitMatch}(r)$ holds.

Let $E/F$ be an unramified quadratic extension of $p$-adic fields. $\mathrm{UnitMatch}(r)$ compares orbital integrals of the unit function $\mathbf{1}_{\mathfrak{gl}_{r+1}(\mathcal{O}_F)}$ under $\mathrm{GL}_r(F)$, weighted at each point $Y$ of the orbit by a sign $\omega(Y)$ built from $\eta_{E/F}$, with orbital integrals of the unit function on Hermitian $(r+1) \times (r+1)$ matrices under $U_r$. At each regular element the two are equal, and the first is $0$ when the invariants have no Hermitian element. This is the Lie algebra form of the fundamental lemma of Jacquet and Rallis (Clay Math. Proc. 13, 2011), proved by Yun (Duke Math. J. 156, 2011) and by Beuzart-Plessis (Duke Math. J. 170, 2021). The objects are defined in full in [the entry with the proof](/entry/unit-match-of-weil-field/).

## Proof

The proof is `unitMatch_all`. Its type is the statement, so Lean accepts it at once. There is nothing more.

## In the Lean code

The theorem is at [JacquetRallisUnitMatchAllRanksStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/JacquetRallisUnitMatchAllRanksStatement.lean#L6). The proof is the tactic `first | exact @GlobalTheory.JR.unitMatch_all | ...`. The first branch closes the goal, since the two types are the same.

The theorem has two direct uses, neither of which is an entry of this handbook. Both apply `unitLemma_lieAlgebra_unitaryGroup_of_jacquetRallis` to it and take the first part: `unitLemma_identity_unconditional` in [UnitLemmaUnramifiedProductUnitaryGroups.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UnitLemmaUnramifiedProductUnitaryGroups.lean#L10), and `match_principal_congruence_inert` in [CongruenceSubgroupIndicatorWeight.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CongruenceSubgroupIndicatorWeight.lean#L41). We have not unfolded `unitLemma_lieAlgebra_unitaryGroup_of_jacquetRallis`.
