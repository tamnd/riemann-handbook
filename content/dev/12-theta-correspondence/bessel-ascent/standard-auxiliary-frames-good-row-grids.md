---
id: standard-auxiliary-frames-good-row-grids
title: Standard frames are good, given fixed depth vectors (named form)
kind: theorem
decl: GlobalTheory.T.standardAuxiliaryFrames_good_row_grids
module: Development.AbelianVarietyTheory.Proofs.TwistedOperators.StandardAuxiliaryFramesGoodRowGridsStatement
covers: 1304
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It gives the theorem [`std_good`](/entry/std-good/), which has the real content, a second name in the namespace `GlobalTheory.T`. Its one user is [`towerEx_of_depFixed`](/entry/tower-ex-of-dep-fixed/), which uses it for the goodness half of the conclusion `TowerEx`.

## Statement

Assume `DepFixed`: for every grid datum, every depth vector of a row pair or a core pair is fixed by the Weil action of the level groups of both spaces of the pair. Then for every grid datum $(D, L, G, W, M)$ that meets the standing conditions of `All`, every choice $v$ of volume data on the core spaces, and every system of frames $F$ that is standard (`Std F`), the frames are good with the line lattices of $F$:

$$F.\mathrm{Good}\bigl(v, W, \mathrm{lineLat}(F)\bigr).$$

The entry [`std_good`](/entry/std-good/) says what standard frames, the line lattices and goodness are.

## Proof

The proof is the term `GlobalTheory.AscFin.GoodStd.std_good`. Nothing else happens.

## In the Lean code

The theorem is in [StandardAuxiliaryFramesGoodRowGridsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/StandardAuxiliaryFramesGoodRowGridsStatement.lean#L12). The proof is the tactic `first | exact @GlobalTheory.AscFin.GoodStd.std_good | ...`, and the first branch closes the goal. The statement is word for word that of `std_good`. The words "row grids" in the name do not name a defined object.
