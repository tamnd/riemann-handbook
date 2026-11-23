---
id: exists-good-grid-frames-of-depth-fixed
title: Good frames for the theta tower, given fixed depth vectors (named form)
kind: theorem
decl: GlobalTheory.T.existsGoodGridFrames_of_depthFixed
module: Development.AbelianVarietyTheory.Proofs.TwistedOperators.ExistsGoodGridFramesOfDepthFixedStatement
covers: 1356
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It gives the theorem [`towerEx_of_depFixed`](/entry/tower-ex-of-dep-fixed/) a second name in the namespace `GlobalTheory.T`. Its one user is the ascent [`ascent_of_depFixed`](/proof/bessel-seesaw/), which uses it as the frame input of the tower of periods. The chapter [Bessel periods, seesaw and separation of functionals](/proof/bessel-seesaw/) calls this input "the frames" in its Step 6.

## Statement

$$\mathrm{DepFixed} \implies \mathrm{TowerEx}.$$

`DepFixed` says that, for every grid datum, every depth vector of a row pair or a core pair is fixed by the Weil action of the level groups of both spaces of the pair. `TowerEx` says that, for every grid datum and every choice $v$ of volume data on the core spaces, there are frames $F$ (Witt decompositions and line vectors along the tower) whose ends fit the bottom and top periods, and a family of lattices $\Gamma_L$ for which $F$ is good. The entry [`towerEx_of_depFixed`](/entry/tower-ex-of-dep-fixed/) states both in full.

## Proof

The proof is the term `GlobalTheory.AscFin.towerEx_of_depFixed`. Nothing else happens.

## In the Lean code

The theorem is in [ExistsGoodGridFramesOfDepthFixedStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExistsGoodGridFramesOfDepthFixedStatement.lean#L12). The proof is the tactic `first | exact @GlobalTheory.AscFin.towerEx_of_depFixed | ...`, and the first branch closes the goal. The two statements are the same up to the namespace. The real content is in [`std_good`](/entry/std-good/), two levels below.
