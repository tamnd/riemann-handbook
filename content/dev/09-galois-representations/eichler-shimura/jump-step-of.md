---
id: jump-step-of
title: Hodge degrees are Hodge-Tate jumps, given three inputs
kind: theorem
decl: UpperTheory.Gal.G3.jumpStep_of
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.PAdicWittLattices.TraceSplitHolds
covers: 324
status: drafted
drafted_by: writer@claude
---
This theorem proves `JumpStep` from three hypotheses: the Hodge-Tate frames for good models, the crystalline step, and the existence of the representation. [jumpStep_holds](/entry/jump-step-holds/) supplies all three and so proves `JumpStep` with no hypothesis. This theorem collects the other twelve facts that the proof needs, all proved here or in nearby files.

## Statement

**Theorem.** Assume `HTSpecGood` (a Hodge-Tate comparison with period matrices for good smooth models, see [htSpecGood](/entry/ht-spec-good/)), `CrysStep` (a continuous piece $\rho$ of a nice tower is crystalline at each place $w$ above $\ell$ where the tower has a cover that is onto, see [the crystalline step](/entry/crys-step-holds/)) and `RepEx` (each nice tower has a continuous semisimple piece). Then `JumpStep` holds: at such a place $w$, for each embedding $\tau$ above $w$, each degree $b$ that occurs at $\iota\tau$ in the Hodge cohomology of the tower, with the eigenvalues of the piece, is a Hodge-Tate jump of $\rho$ at $\tau$.

The objects and the full statement are in [jumpStep_holds](/entry/jump-step-holds/).

## Proof

The proof is one term:

```
G8.jumpStep_of (G8.jumpCore_of hS h1 ... h13) hC
```

`G8.jumpStep_of` reduces `JumpStep` to `JumpCore`, which also assumes that $\rho$ is crystalline at $w$; the hypothesis `CrysStep` gives this. `G8.jumpCore_of` proves `JumpCore` from `HTSpecGood` and thirteen more facts. The steps of that proof are in [jumpStep_holds](/entry/jump-step-holds/). The thirteen facts and their sources:

- `MatEx`, from `RepEx` by `matEx_of`: the Galois action on the piece has a matrix form. This is the only use of `RepEx`.
- `LowNice`, `LowHodge` and `LowPiece`: the tower on the generic fibre of the good model is nice, each Hodge occurrence on the tower is one on it, and its piece embeds into the piece of the given tower. They are `jLowNice`, `lowHodge_holds` and `lowPiece_holds`.
- `LocalMat`, `CoverLow`, `BridgeInt`, `BCTower` and `LocE`: the local inputs of `occ_low`. They are `jLocalMat`, `coverLow_of_cov`, `jBridgeInt`, `jBCTower` and `locE_of`.
- `OccMove`, `JumpsEx`, `ConjBridge` and `JumpOfHT2`: they move the occurrence to $\rho$, give the multiset of jumps of a crystalline $\rho$, conjugate the local bridge, and turn an occurrence into a jump. The first two are proved in the namespace `G8`, the last two are `jConjBridge` and `jJumpOfHT2`.

We have not unfolded the statements of these thirteen facts beyond their use in `G8.jumpCore_of`.

## In the Lean code

The theorem is in [TraceSplitHolds.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/PAdicWittLattices/TraceSplitHolds.lean#L78). `G8.jumpStep_of` and `JumpCore` are in [JumpStepOf.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/GoodCoverEigenspaces/JumpStepOf.lean#L113), and `G8.jumpCore_of` in [JumpOf.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/GoodCoverEigenspaces/JumpOf.lean#L34).

`jLocalMat` takes `seamHopEx_holds` and `locTower_holds` from the same file. These prove the same statements as `Seam.hopEx_holds` and `Seam.locTower_holds`, as [jumpStep_holds](/entry/jump-step-holds/) notes. The three hypotheses are only passed along; the theorem has no mathematics of its own.
