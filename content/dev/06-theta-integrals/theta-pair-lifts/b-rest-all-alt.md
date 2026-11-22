---
id: b-rest-all-alt
title: The remaining division bounds on the working class
kind: theorem
decl: Formalism.L2.DIV.RestAll.bRest_all_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.BrestFinalAll
covers: 338
status: drafted
drafted_by: writer@claude
---
This theorem proves four of the ten facts in the closed bound `DivisionKernelConstantBounds`, on the working class $\mathcal{D}(\mathcal{A})$ of [the shape theorem](/entry/shape-closed-link-n-of-green/). Its only user is [the same bounds at the constant 2](/entry/link-brest-alt/), which passes the result to the shape theorem for step 6 (`LinkDIVt`) of its proof.

## Statement

Use the notation of [the shape theorem](/entry/shape-closed-link-n-of-green/): a family $F$ has data $D(x,i)$ and size data $L(x,i)$, $\mathcal{D}(\mathcal{A})$ is the class `D3 3 𝒜`, and `Closed` is the predicate of [the definition Closed](/step/closed-def/).

**Theorem.** Let $\mathcal{A}$ be a family class and $C_{\mathrm{abs}}$ a real number. Assume:

1. a twist selection on $\mathcal{A}$ with five companion choices, the last a bundle `selB` of indefinite realisations;
2. at each selected point: the realisation has bounded rows (`hRB`), the base-level choice satisfies `DivRows3G` and `DcPtG`, and all realisations are primitive (`hPA`);
3. the closed row condition `rRows` on $\mathcal{D}(\mathcal{A})$;
4. the closed condition `tie`: eventually each $D(x,i)$ is `RealTied` and carries a symmetric tied column datum whose forms satisfy `ChiFin0`.

Then `Closed` holds on $\mathcal{D}(\mathcal{A})$ for this statement: if `TuSize F` and `DGamSize F`, then

- (`hh`) `ComplementTwoFamily F` and `DIVinN F` imply the frame number bound `FrameNumberBoundFamily F Csz CH`;
- (`bu`) eventually each $D(x,i)$ is `BuRational`: the pairing `Bu` of two images equals the image of `Bk` under the embedding `embLL`, so it takes values in the field `LL`;
- (`rr`) eventually each $D(x,i)$ is `RRFull`: the lattice of `RR` is finitely generated and spans its space over `LL`;
- (`la`) eventually $0 \le L(x,i).\mathrm{La}$.

We have not unfolded `FrameNumberBound`, `DivRows3G`, `DcPtG` or `rRows`.

## Proof

1. `closed_funSharp_thr_alt` uses `hRB`, `hPA`, `DivRows3G` and `rRows`. It gives a function $C_{F0}$ such that $F$ is large for the threshold `thrHH`, and such that `DIVinN F` implies, eventually, $\mu_{\max}(\mathrm{RR}) + \operatorname{mean}_e \log \kappa_R(e) \le x^{C_{F0}} b$.
2. For `hh`, fix a family. From `tie` and `TuSize`, `lvlF_of_ties` gives `LvlF`. Then `muRank_of_lvl` gives `MuRank`, and `linkMu_of_full` gives `LinkMu` through `nuFullF_of_lvl`. `closed_linkG_of_tuSize_dGamSize` gives `LinkG`, by [the concrete LinkG theorem](/entry/link-g-concrete5/). Then `hh_of_lvl` combines these with the bound of step 1 and a bound on $\mu_{\max}$ from `TuSize`.
3. `buRat_rrFull_closed_alt` gives `bu` and `rr`. It uses `rRows`, `hPA`, the column choice, `DivRows3G` and `DcPtG`, through `buRational_of` and `rrFull_of`.
4. `la_of` gives `la` with no hypothesis.

The rest is bookkeeping.

## In the Lean code

The theorem is at [BrestFinalAll.lean line 25](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BrestFinalAll.lean#L25). The main lemmas are in [HefunFunTop.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/HefunFunTop.lean#L117), [BurrbPlug.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BurrbPlug.lean#L23), [LinkgLinkGCl.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkgLinkGCl.lean#L20) and [LvlWire.lean](lean:Formalism/LocalToGlobal/Divisibility/DivisibilityRemainder/NoColumnCase/LvlWire.lean#L51).

The constant $C_{\mathrm{abs}}$ is never used. The structure `RemainingDivisionBounds Fm Cabs CH` ([IndefiniteRealisationChoice.lean line 158](lean:Formalism/LocalToGlobal/IndefiniteRealisationChoice.lean#L158)) does not read `Cabs` in any field. The field `la` holds for every family by `la_of` ([RecBridgeWire.lean line 16](lean:Formalism/LocalToGlobal/Divisibility/RecBridgeWire.lean#L16)), so it carries no content from the hypotheses.
