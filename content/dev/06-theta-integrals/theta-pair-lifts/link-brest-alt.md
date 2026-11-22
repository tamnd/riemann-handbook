---
id: link-brest-alt
title: The remaining division bounds at the constant 2
kind: theorem
decl: GlobalTheory.Top.link_brest_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.LinkBrest
covers: 340
status: drafted
drafted_by: writer@claude
---
This theorem is [the remaining division bounds](/entry/b-rest-all-alt/) with the constant $C_{\mathrm{abs}} = 2$. Its only user is [the shape theorem](/entry/shape-closed-link-n-of-green/). There `toRows_alt` turns its result into the bound `DivisionKernelConstantBounds` at the same constant, for step 6 (`LinkDIVt`).

## Statement

Use the notation of [the shape theorem](/entry/shape-closed-link-n-of-green/): $\mathcal{A}$ is a family class and $\mathcal{D}(\mathcal{A})$ is its working class `D3 3 𝒜`.

**Theorem.** Take the same hypotheses as [the remaining division bounds](/entry/b-rest-all-alt/): a twist selection on $\mathcal{A}$ with its five companion choices, three conditions on the selected data, and two closed conditions on $\mathcal{D}(\mathcal{A})$ (`rRows` and `tie`). Then the closed statement on $\mathcal{D}(\mathcal{A})$ holds that `TuSize F` and `DGamSize F` imply `RemainingDivisionBounds F 2 CH`.

## Proof

The proof is one line. It applies `bRest_all_alt` with `Cabs := 2` and the other arguments unchanged.

## In the Lean code

The theorem is at [LinkBrest.lean line 18](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkBrest.lean#L18). It calls only `bRest_all_alt`.

- It adds nothing.
- No field of the conclusion reads the constant. The structure `RemainingDivisionBounds Fm Cabs CH` ([IndefiniteRealisationChoice.lean line 158](lean:Formalism/LocalToGlobal/IndefiniteRealisationChoice.lean#L158)) takes `Cabs` as a parameter, but its four fields do not mention it. The constant only fixes the type of what the caller builds next. In [TopShape.lean line 36](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopShape.lean#L36) the result is `bRest`, and `RemainingDivisionBounds.toRows_alt` ([IndefiniteRealisationChoice.lean line 100](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/IndefiniteRealisationChoice.lean#L100)) copies the four fields into `DivisionKernelConstantBounds Fm Rt 2 CH`. There the field `pkg` reads the constant.
