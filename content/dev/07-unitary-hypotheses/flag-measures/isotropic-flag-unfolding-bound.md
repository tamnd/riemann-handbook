---
id: isotropic-flag-unfolding-bound
title: The unfolding bound for a flag type, a second name
kind: theorem
decl: GlobalTheory.T.isotropicFlag_unfolding_bound
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.IsotropicFlagUnfoldingBoundStatement
covers: 856
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`unfoldBound`](/entry/unfold-bound/). That entry has the content. Its user is [the flag measure bound](/entry/flag-measure-bound/), which divides it by the volume ratio from the volume step.

## Statement

**Theorem.** `UnfoldBound` holds.

`UnfoldBound` compares two unitary groups over the same CM field: $G$ of signature $(p,q)$ and $G_0$ of signature $(p-s, q-s)$, with $s = \sum_i j_i$. It bounds the covolume in $G(F)\backslash G(\mathbb{A})$ of the set of points of flag type $(j, \tau)$, $\tau \in B$, by the gauge volume of $G_0$, the volumes of the groups $\mathrm{GL}_{j_i}$ over $E$, an explicit constant and $\int_B \mathrm{dens}(\tau)\, d\tau$. It is stated in full in [`unfoldBound`](/entry/unfold-bound/). The flag types and the density are defined in [the flag measure bound](/entry/flag-measure-bound/).

## Proof

The proof applies `GlobalTheory.FlagUnfold.unfoldBound`, which has the same statement. Nothing else happens.

## In the Lean code

The theorem is in [IsotropicFlagUnfoldingBoundStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/IsotropicFlagUnfoldingBoundStatement.lean#L6). The statement `UnfoldBound` is in [SameKindIsometric.lean](lean:Development/AbelianVarietyTheory/Statements/CuspFrameWeights/SameKindIsometric.lean#L84). The proof is a `first | exact ... | ...` combinator with three tries, and each try applies the same lemma. The file sets `maxHeartbeats 1000000`, which a one-line proof does not need. The theorem has no hypothesis of its own: `UnfoldBound` is proved outright, with no use of `VolumeStep`.
