---
id: shares-at-all
title: The share conditions of the family at every run index, by cases on the index
kind: theorem
decl: GlobalTheory.InputsAtRecord.sharesAt_all
module: Development.AbelianVarietyTheory.Proofs.HeightProofs.ExistsIndexBoundHypothesesWithNetAllValuedPoints
covers: 775
status: drafted
drafted_by: writer@claude
---
This theorem gives step 4 of [`inputsNet_recPlus`](/entry/inputs-net-rec-plus/): a new count $\delta$, new forms $\theta'_1, \dots, \theta'_\delta$, and five share conditions on the family. It is a case split on the index $j$. The content is in two lemmas, one for $j < m$ and one for $j = m$. Branch 2 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/) is above it.

## Statement

Use the record $T$, the algebra of forms $X_j$, `ParOK`, `PageOK` and the scalars $S$ of [the entry for `inputsNet_recPlus`](/entry/inputs-net-rec-plus/). Let $G$ be a family (`GlobalFamilyData`) for $X_j$ and weights $\kappa, w_L, w_F$.

**Theorem.** Let $1 \le j \le m$. Assume `ParOK T EX p j`, `PageOK`, `HypC`, the lattice condition `LatAt`, `GenOK` for $G$, and `EtaOK` when $j < m$. Let $\mathcal{S}$ be a set of cusp forms of weight $w_F$ that spans them over $K$. Then `SharesAt` holds: there are $\delta$ and $\theta'_1, \dots, \theta'_\delta \in \mathcal{S}$ such that, after we put $\delta$ and $\theta'$ into $G$, and for each choice of the other refilled fields,

1. `InBasis` holds at each prime $\lambda$: certain vectors made from $G$ are a basis of a vector space over a completion at $\lambda$;
2. `ShareRd`: $\binom{T_n - 1}{\dim Y} \delta \le \operatorname{rk} M_\kappa$;
3. `ShareRhoR` and `ShareRhoP`, two more bounds in terms of $\operatorname{rk} M_\kappa$;
4. `InContainMR` holds at each $\lambda$.

We have not unfolded `ShareRhoR`, `ShareRhoP`, `InContainMR` or the vectors of `InBasis`.

## Proof

If $j < m$, apply `cuspFormBasisShares_indefinite_liftIndex`. If $j = m$, apply `cuspFormBasisShares_definite_liftIndex`. The rest is bookkeeping.

## In the Lean code

The theorem is in [ExistsIndexBoundHypothesesWithNetAllValuedPoints.lean](lean:Development/AbelianVarietyTheory/Proofs/HeightProofs/ExistsIndexBoundHypothesesWithNetAllValuedPoints.lean#L66). `SharesAt` and `GenOK` are in [GrowthConstantBoundGcR.lean](lean:Development/AbelianVarietyTheory/Definitions/HeightFunctions/GrowthConstantBoundGcR.lean#L79). We have not read the proofs of the two lemmas.

- For $j = m$, the proof passes only one of the five parts of `GenOK`, the condition `NoCommonZero` on the forms of $G$. `EtaOK` is not used there, since its premise $j < m$ is false.
- `SharesAt` quantifies over the other fields of the refilled family. So the five conditions do not depend on those fields.
