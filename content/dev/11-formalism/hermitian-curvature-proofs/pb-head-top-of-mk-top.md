---
id: pb-head-top-of-mk-top
title: The head formula from the top truncation statement
kind: theorem
decl: Formalism.FourierDecayAlt.P.pb_headTop_of_mkTop
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.PbHeadTopOfMkTop
covers: 534
status: drafted
drafted_by: writer@claude
---
This theorem is a relay. It proves the head formula `HeadTop` from the hypothesis `MkTop`. The proof only passes `MkTop` and proved facts to two other theorems. The theorem `head_top` applies it to a proof of `MkTop`, and this gives `HeadTop` outright. That is how it is below the trunk node [HypsAlt is nonempty](/step/nonempty-hyps/).

## Statement

`MkTop` is stated in [the built bounds from the top truncation statement](/entry/pb-built-bounds2-cpt-of-mk-top/). `HeadTop` is stated in [the built bounds from the head formula](/entry/built-bounds-compact-of-head-top/). It says that the top density `topDens` equals the coefficient `RR` at level $r + 1$, with the last point $(1, \zeta)$ added to $h$ and $h'$.

**Theorem.** If `MkTop` holds, then `HeadTop` holds.

## Proof

There are two steps.

1. `pb_exhPic_of_mkTop` proves the exhaustion picture `ExhPic`. It gives `MkTop` and eighteen proved facts to `CutEX.exhPic_of_leaves`. That theorem only applies the proved implication `exceptional_assumption_holds` to its arguments. So the work for this step is in `exceptional_assumption_holds`, whose proof we have not unfolded.
2. `pb_headTop_of` takes `ExhPic` and the proved fact `top_unipotent_integral`, and calls `head_top_of_radial_exhaustion` with the proved fact `head_weight_at`.

## In the Lean code

The theorem is at [PbHeadTopOfMkTop.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/PbHeadTopOfMkTop.lean#L26), and the first step is at line 20. `exhPic_of_leaves` and the implication `Asm` are in [CutEX2.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutEX2.lean#L189). `exceptional_assumption_holds` is a theorem in [CutEXAsm.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutEXAsm.lean#L119), although its name says "assumption". `head_top` is in [RadialExhaustion.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/RadialExhaustion.lean#L6).
