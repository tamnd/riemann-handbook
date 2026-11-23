---
id: constructed-point-reference-chain-word-forms-map
title: The forms map at a bundle point over true columns
kind: theorem
decl: GlobalTheory.Fc.PeriodEntriesOverColumns.constructedPoint_referenceChainWord_formsMap
module: Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.ReferenceChainEvaluationBundlePointsOverColumnsA
covers: 457
status: drafted
drafted_by: writer@claude
---
This lemma proves `Conclusion6` at the datum of one constructed point that comes from true columns. It is the pointwise fact that [the forms map row from true columns](/entry/reference-chain-evaluation-bundle-points-over-columns/) turns into a row statement. Its proof only moves from the point to the column datum under it; the work is done by [the forms map at every true column member](/entry/forms-map-at-every-true-column-member/), through its second name [`aux_of_ok_of_pins`](/entry/aux-of-ok-of-pins/).

## Statement

**Lemma.** Let $Q$ be a slot with `OverCols Q`. Let $K$ be a context and $\beta$ a bundle point over $K$ (a structure `BPt K`: stages $X$, a frame $f$, twist data $T$, a core, a layer, and a list of conditions on them) with $\beta$ in $Q$. Then `Conclusion6 β.D u` holds for every word $u$ of the datum $\beta.D$.

[The forms map from a symmetric comparison](/entry/forms-map-of-symmetric-comparison-lower-map-finite-char/) says what `Conclusion6` means.

## Proof

`OverCols Q` puts $\beta$ in the slot `HasCols`. A point of `HasCols` comes from a column datum `w : ColW B f T` and later stages $Z$, and its datum is `w.D Z`, which is `TC.rec7 w.I w.l Z`. The lemma `property_at_constructedPoints_of_trueColumnsView` makes this precise: to prove a property $R(\beta.D, \beta.O)$ at all points of `HasCols`, it is enough to prove $R(w.D Z, O)$ for each column datum $w$, each $Z$, each object $O$ and each choice `nch`, under three hypotheses: a column view `ColView`, `BaseSigns B` and `RealTied (w.D Z)`.

The proof takes $R(D, O) = \forall u,$ `Conclusion6 D u`, and at a column datum applies `aux_of_ok_of_pins` to `w.I`, `w.ok`, `w.pins`, `w.l` and $Z$. The three hypotheses are not used.

## In the Lean code

The lemma is in [ReferenceChainEvaluationBundlePointsOverColumnsA.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/ReferenceChainEvaluationBundlePointsOverColumnsA.lean#L12). It calls:

- `GlobalTheory.T.property_at_constructedPoints_of_trueColumnsView`, in [PropertyAtConstructedPointsOfTrueColumnsViewStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/PropertyAtConstructedPointsOfTrueColumnsViewStatement.lean#L8), a relay of `view_at_built`. We have read its statement, not its proof.
- `GlobalTheory.T.aux_of_ok_of_pins`.

The column view, `BaseSigns` and `RealTied` are all dropped (the wildcards in `fun _ _ _ w Z _ _ _ _ _`, line 15).

The name speaks of a "reference chain word". The statement is about every word $u$, not a reference word.
