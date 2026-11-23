---
id: inp-all
title: The inputs of the CM theta norm bound hold for every datum
kind: theorem
decl: GlobalTheory.NormSum.inp_all
module: Development.AbelianVarietyTheory.Proofs.FoundationProofs.CmThetaNormBoundHypothesesSatisfied
covers: 757
status: drafted
drafted_by: writer@claude
---
This theorem fills a structure of 22 fields, each by one theorem applied to the datum. It has no mathematics of its own. It serves the step [nonempty hypotheses](/step/nonempty-hyps/): the evaluation grid of item 4 of that step (`evaluation_grid_of_join`) depends on it, through the lemmas that build the number fields of the theta evaluations.

## Statement

**Theorem.** For every datum $D$ of type `D7`, the structure `Inp D` holds.

`Inp D` collects the facts on CM theta functions that the norm bound needs. By their names, the fields are of four kinds:

1. Group theory and characters: the genus one type `g1`, the permutation of types `perm`, a unitary intertwiner `uni`, and a Gauss sum constant `mu`.
2. Galois action on CM points: the conjugate curve `curve`, rationality of theta translates `gal` and `galEx`, a two-torsion CM point `t0Ex`, and the fields `use1`, `alg`, `conj`, `nrm`, `bar` on algebraic Taylor coefficients, conjugates, norms and complex conjugation.
3. Signs: `odd3`, `odd4`, `rep`, and the equivariance `eqv` of odd vectors.
4. Integrality of the elliptic curve model: `model`, `transl`, `two`, `jets` and `split`, from the file `GL3Theta`.

We have not unfolded these fields.

## Proof

Each field is the theorem `T.<name> D` of the same subject. The pair `g1`, `perm` comes from one theorem, `T.inducedType_thetaGenusOne_permutes`. The field `eqv` is `OddRank.exact_equivariance`.

## In the Lean code

The theorem is in [CmThetaNormBoundHypothesesSatisfied.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/CmThetaNormBoundHypothesesSatisfied.lean#L29). `Inp` is in [NormSumPairRankZeroOfCurveCoordNorm.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/NormSumPairRankZeroOfCurveCoordNorm.lean#L175). The real content is in the 21 theorems that fill the fields. [The cube relation](/entry/cube-add-int-be-biadd/) is below some of them: `CMEndo.endo_all` uses it, and the files of the fields `jets`, `two` and `split` import the file of `endo_all`.
