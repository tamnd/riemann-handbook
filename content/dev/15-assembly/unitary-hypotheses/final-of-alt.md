---
id: final-of-alt
title: The closed link bound, given a cut and the Galois preconditions
kind: theorem
decl: UpperTheory.GalC.final_of_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.LinkNFam
covers: 14859
status: drafted
drafted_by: writer@claude
---
This theorem is the main part of [the closed link bound](/entry/final-alt-alt/), which is step 4 of branch 1 in [the unitary hypotheses chapter](/proof/unitary-hypotheses/). It turns a hypothesis on the Galois data at each layer point into a row statement linked at the parameters of the chapter. Then it passes the result, with the [closed bound](/step/closed-def/), to [the linked form of the link bound](/entry/linked-at-link-n-of-bound-at-two-three/). The analytic content is lower, in [the link bound for one family](/entry/link-n-of-tw-good-galois-preconditions/).

## Statement

A family $F$ gives, for each real $x$ and each index $i \in I_x$, a datum $D_{x,i}$ with size data $L_{x,i}$. We have not unfolded the family type `FamP`. The *link bound* `LinkN F` says: there are $C$ and $x_0$ such that for $x \ge x_0$, for each $i \in I_x$ with `ShaFinOdd` and for each lift $j$ of $D_{x,i}$, if the series $\sum_l v_l$ of `vvTerm` converges, then
$$\eta_j(L_{x,i}) \le d_j \Bigl(C \bigl(f m b \Lambda^2 + (\log X)^2 N_c\bigr) + \sum_l v_l\Bigr).$$
Here $\eta_j$ is `etaSum`, $d_j$ is `dZ0 j`, $f$ and $m$ are numbers of $D_{x,i}$, and $b$, $\Lambda$, $X$ and $N_c$ are the fields `sc.b`, `sc.L`, `sc.x` and `Nc` of $L_{x,i}$. We have not unfolded these numbers. A *closed bound* `Closed 𝒞 P` says: there is $\varepsilon_1 > 0$ such that for each $\varepsilon \in (0, \varepsilon_1]$ there is a threshold $K$ with $P(F)$ for every family $F$ in the class $\mathcal{C}$ that is large for $K$.

Let $p$ be the parameters `parametersOfExtension (extensionWithList hL cDep) SExt.none (geoCl anyGeometry)`. By definition this is `parametersOfDependence hL cDep`. A condition is *linked at* $p$ (`LinkedAt`) when it holds on the slot rows of $p$ after one extra large base condition. [The linked form](/entry/linked-at-link-n-of-bound-at-two-three/) gives the details.

**Theorem.** Assume `Hypotheses₂`, the cut hypothesis `CutGivesAlt`, the published inputs `PublishedInputsThirdLayerAlt`, `GeometricGaloisRepCompatibility`, `DepthZeroSupport`, an element $h_L$ of `RecTExists`, a real $c$, and:

1. at every layer point, the datum $D$ and its norm choice satisfy `GaloisPreconditions`;
2. the closed bound for `BoundAtTwoThreeFamilyFonAlt` is linked at $p$.

Then the closed bound for `LinkN` is linked at $p$.

## Proof

1. The slots of $p$ satisfy `WitMv`. This comes from `slot_mv_extension_with_list_geo_cl`, which gives `PositionMv`, and `witnesses_pass_along_set_division`, which turns `PositionMv` into `WitMv`.
2. At every layer point the datum satisfies the four tie conditions `Tie4`. This is `tieChi_at_members_of_depthZero`, from the field `ht` of the compatibility record, the published inputs and `DepthZeroSupport`.
3. `AtMem.and_z` joins hypothesis 1 and step 2. The second part of `atMem_at_wit_alt`, with step 1, moves a property of $(D, \text{norm choice})$ that holds at every layer point to a row linked at $p$. Its other input says that an element of `extensionWithList` gives one of `extensionWithLaw`; this is the first projection.
4. `linkedAt_linkN_of_boundAtTwoThree` takes this row and hypothesis 2, and gives the conclusion.

The rest is bookkeeping.

## In the Lean code

The theorem is in [LinkNFam.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkNFam.lean#L75). The lemmas it calls:

- `slot_mv_extension_with_list_geo_cl` in [SlotMvPin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SlotMvPin.lean#L20);
- `witnesses_pass_along_set_division`, in the module `WitnessesPassAlongSetDivisionStatement`, with `WitMv` in [PositionMv.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/PositionMv.lean#L23);
- `tieChi_at_members_of_depthZero` in [LocalTypeDeterminedAtAllPrimes.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LocalTypeDeterminedAtAllPrimes.lean#L36), itself a relay of `locComp_of_isRc_classMapD_cenLoc`;
- `atMem_at_wit_alt` in [OverNEOfNEb.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OverNEOfNEb.lean#L25) and `AtMem.and_z` in [AtMemberImp.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AtMemberImp.lean#L21);
- `linkedAt_linkN_of_boundAtTwoThree`, in the same file.

`Hypotheses₂` and `CutGivesAlt` only pass through to the next lemma. Hypothesis 2 also passes through unchanged. It is redundant: `boundAtTwoThree_linked_of_recT` in [At23OfAll.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/At23OfAll.lean#L24) proves it from `Hypotheses₂`.
