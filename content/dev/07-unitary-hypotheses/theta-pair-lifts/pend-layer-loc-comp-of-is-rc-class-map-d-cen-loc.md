---
id: pend-layer-loc-comp-of-is-rc-class-map-d-cen-loc
title: The first two tie conditions at every layer point
kind: theorem
decl: GlobalTheory.HeightCounting.Up.PendLayer.locComp_of_isRc_classMapD_cenLoc
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.PendingLayerConditionAtMember
covers: 549
status: drafted
drafted_by: writer@claude
---
This theorem proves the first two of the four tie conditions `Tie4` at every layer point. It collects facts at each layer point and passes them to [the two tie conditions for one datum](/entry/tie-chi-of-lab-all-green-chi-cen/), which has the content. Its user is the second name [`tieChi_at_mem_of_depth_zero_inputs`](/entry/tie-chi-at-mem-of-depth-zero-inputs/). The result goes on to [the closed link bound, given a cut](/entry/final-of-alt/), in branch 1 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). Below this theorem are 549 declarations.

## Statement

Let $h_L$ be an element of `RecTExists`. A property $p$ holds *at every layer point* (`MemberAtLayerPoint hL p`) if, eventually in the sense of `EvLgG`, for each context $K$, base $B$, frame $f$ and twist datum $T$ with `KPx B f`, and for each column $w$, index $Z$ and further data (a set of places, a base level, rows $t$, a norm choice and its extension $c$) such that the default extension is nonempty, `RXs t` is nonempty and `ColPin w` holds, $p$ holds. The datum of the point is $D = w.D\,Z$. We have not unfolded `EvLgG` or these data.

**Theorem.** Assume `HtCard`, the record `PublishedInputsThirdLayerAlt` of fourteen named inputs, and `DepthZeroSupport`. Then for each $h_L$, at every layer point the datum $D$ satisfies `tieChi`, and $D$ has a pending datum $P$ with `admDZ P` and `EigSpan P`.

## Proof

1. Four facts hold at every layer point, and `atMem_and'` joins them.
   - `cenLoc_zlStable_cenInt_at_members`: `CenLoc` for the family $M$ of the point, `ZLStable` and `CenInt`.
   - `jumpsCard_at_members_of_htCard`, from `HtCard`: `JumpsCard`.
   - `isTied_of_layer_member_alt`, from the published inputs: linked data $X$ (a character choice datum $X.P$ of $D$, and a real datum that agrees with it) with $X.P$ *pinned* at the point: $X.P$ has the character frame, norm choice, tuple, representations and family $M$ of the point, and satisfies `LabAll`, `GreenLab` and `ChiTOk`.
   - `sizes_host_at_record`, moved to layer points by `atMem_mono_of_colPin`: seven size and host facts.
2. At each point, `atMem_mono` applies [`tieChi_of_labAll_green_chi_cen`](/entry/tie-chi-of-lab-all-green-chi-cen/) to $X.P$ and these facts. The pin gives $X.P.M = M$, which turns `CenLoc D M` into `CenLoc D X.P.M`.

The rest is bookkeeping.

## In the Lean code

The theorem is in [PendingLayerConditionAtMember.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PendingLayerConditionAtMember.lean#L46). `MemberAtLayerPoint` is in [ThetaDataExists.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ThetaDataExists.lean#L25). The three `atMem` lemmas are in [AtMemAnd.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AtMemAnd.lean#L20), and `isTied_of_layer_member_alt` is in [TiedConditionOfLayer.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TiedConditionOfLayer.lean#L33). Of the seven facts of `sizes_host_at_record`, the proof uses only `RootsLL`.

The name `locComp_of_isRc_classMapD_cenLoc` does not match the statement. Nothing called `isRc` or `classMapD` appears, and `CenLoc` is only an intermediate fact. The same short name is used for three other theorems with other statements, in the namespaces `TypePrimesFinished`, `PinClose` and `TieChiPin`.
