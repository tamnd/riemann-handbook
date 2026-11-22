---
id: unitary-automorphic-counting-of-compact-dual-volume-ratio
title: The counting theorem from the volume ratio, a second name
kind: theorem
decl: GlobalTheory.T.unitaryAutomorphicCounting_of_compactDualVolumeRatio
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.UnitaryAutomorphicCountingOfCompactDualVolumeRatStatement
covers: 1621
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the counting theorem from the volume step](/entry/counting-theorem-of-volume-step/). That entry has the content. Its user is [`count_typed_of_volumeStep`](/entry/count-typed-of-volume-step/), which turns the counting theorem into the points lemma for the counting row of [the unitary hypotheses node](/proof/unitary-hypotheses/).

## Statement

**Theorem.** `VolumeStep` implies `CountingTheorem`.

`VolumeStep` is a recursion for the volume of a unitary group: it compares the volume of a group of size $n$ with the volume of a group of size $n-1$, each divided by a factor $v_n^f$. Here $v_n$ is a product of sphere volumes times $2^{n(n-1)/2}$, which has the form of a volume of the compact group $U(n)$. `CountingTheorem` says that the dimension of a space of automorphic forms with given discrete series at the real places is close to a main term. Both are stated in full in [the counting theorem from the volume step](/entry/counting-theorem-of-volume-step/).

## Proof

The proof applies `GlobalTheory.CountFinal.countingTheorem_of_volumeStep`, which has the same statement. Nothing else happens.

## In the Lean code

The theorem is in [UnitaryAutomorphicCountingOfCompactDualVolumeRatStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/UnitaryAutomorphicCountingOfCompactDualVolumeRatStatement.lean#L18). The proof is a `first | exact ... | ...` combinator with three tries. Each try applies the same lemma. The file has `set_option maxHeartbeats 1000000`, which a one-line proof does not need.

The file is named as a statement file, but it imports the proof module (line 2) and only renames the theorem there. The other twelve imports are already reached through that import. The words "compact dual volume ratio" in the name refer to the factors $v_n^f$ in `VolumeStep`. The statement itself does not mention a compact dual.
