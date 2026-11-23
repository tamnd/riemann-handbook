---
id: model-on-hodge-from-family
title: Restatement of the Hodge flag comparison from a family
kind: theorem
decl: GlobalTheory.T.model_on_hodge_from_family
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.ModelOnHodgeFromFamilyStatement
covers: 2529
status: drafted
drafted_by: writer@claude-opus-5-5
---
This theorem is a copy of [`model_on_hodge_of_family_pos`](/entry/model-on-hodge-of-family-pos/) under another name. It says that `FamilyExistsPos` implies `HodgeLatticeFlagBound`. Its only caller is [`goodTower_and_volume`](/entry/good-tower-and-volume/), which passes the result to [`volume_theorem_of_inputs`](/entry/volume-theorem-of-inputs/). The mathematics is in the entry for `model_on_hodge_of_family_pos`.

## Statement

If `Num.FamilyExistsPos` holds, then `HodgeLatticeFlagBound` holds. Both statements are explained in [the entry for `model_on_hodge_of_family_pos`](/entry/model-on-hodge-of-family-pos/). In short: if Hodge-Tate lattice data exist at each place above $p$, then at each such place the local intersection numbers of the Hodge flag equal an explicit combination of intersection numbers on the fibre at $p$.

## Proof

The proof applies `model_on_hodge_of_family_pos`, by the tactic

```
first | exact @model_on_hodge_of_family_pos | exact model_on_hodge_of_family_pos | (intros; apply model_on_hodge_of_family_pos <;> assumption)
```

with full names. The two statements are the same, so the first branch succeeds.

## In the Lean code

The theorem is in [ModelOnHodgeFromFamilyStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/ModelOnHodgeFromFamilyStatement.lean#L14). It is in the namespace `GlobalTheory.T`, where the code puts restatements of this kind. The file sets `maxHeartbeats` to 1,000,000 for a one-line proof.

The name says "bound", but `HodgeLatticeFlagBound` is an equality of intersection numbers, not an inequality.
