---
id: maximal-compact-pseudo-coefficient-data-prime
title: Pseudo-coefficient data on the maximal compact subgroup, from 24 lemmas
kind: theorem
decl: GlobalTheory.PsCo.Pc1.maximalCompact_pseudoCoefficientData'
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.MaximalCompactPseudoCoefficientData
covers: 783
status: drafted
drafted_by: writer@claude
---
This theorem proves `StKData`, the statement of [`maximalCompact_pseudoCoefficientData`](/entry/maximal-compact-pseudo-coefficient-data/). Its proof only passes 24 lemmas to [`stKData_of`](/entry/st-kdata-of/), which has the argument.

## Statement

The statement is `StKData`, as given in [`maximalCompact_pseudoCoefficientData`](/entry/maximal-compact-pseudo-coefficient-data/). For $r$ odd and a [[discrete series|9AB7HYGPEK]] $D$ of $U(p,q)$ with parameter $\lambda$ and gaps at least $100\, r^4$, there is a class polynomial $P_M$ on $K$ with $P_M(t_\theta) = \overline{\Theta_\lambda(t_\theta)}\, d(\theta)$, whose average $\int_K P_M(k)\, \pi(k)\, dk$ has trace $1$ on $D$ and $0$ on every other irreducible unitary $\pi$.

## Proof

The proof is the term `stKData_of` applied to 24 lemmas, one for each hypothesis of `stKData_of`. By the clause of `StKData` where `stKData_of` uses them, numbered as in [`maximalCompact_pseudoCoefficientData`](/entry/maximal-compact-pseudo-coefficient-data/):

- The gap condition: `gapConditions_of_largeGaps`.
- The polynomial $P_M$ and clause 1: `maxCompactPolynomial_blockTimesConjDetPower`, `modeMatrixDet_eq_adjointDet`, `coefPoly`, `trPoly`, `adjointDetTrace_classFunction`.
- Values on the torus, clause 2: `harishChandraWeight_integral_dominant`, `polyCoefIrrep_hasDerivedAction`, `adjointDet_onCompactTorus`, `torusId_full`.
- Trace 1 on $D$, clause 3: `compactDiscreteSeries_ownType`, `norm_irreducibleCharacter_unitaryMaxCompact_eq_one`.
- Trace 0 elsewhere, clause 4, by recognition of $D$: `unitaryRep_upq_matrixFunction`, `tracePairing_nonzero_intertwiner`, `rangeFD_closed`, `casimirScalar_stableSumSpace`, `supertrace_carriedBy_diracKernel`, `StrIdx_proof2`, `intertwiner_preserves_highestWeight`, `fockCoordinates_span_finiteDimensional`, `casimirValue_highestWeightCoordinates`, `highestWeightKernel_lowestType`, `eq_discreteSeries_of_lowestKType_casimir`, `HcPort.casimirActsByScalar_indefUnitary`.

We have not opened the proofs of these lemmas.

## In the Lean code

The theorem is in [MaximalCompactPseudoCoefficientData.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/MaximalCompactPseudoCoefficientData.lean#L32). Twenty-three lemmas are in the namespace `PcEF`; the last is in `HcPort`. The [`localPC_holds`](/entry/local-pc-holds/) entry says 23 lemmas. The count is 24. Some names do not match what the lemma proves: `casimirScalar_stableSumSpace` proves `BuildY`, and `polyCoefIrrep_hasDerivedAction` proves `ToKType`.
