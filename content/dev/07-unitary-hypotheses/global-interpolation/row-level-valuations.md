---
id: row-level-valuations
title: Column valuations at bundle points from true columns
kind: theorem
decl: GlobalTheory.Fc.Cv.row_level_valuations
module: Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.LevelPrimeColumnValuationsBundlePointsOverColumn
covers: 2425
status: drafted
drafted_by: writer@claude
---
This theorem turns a pointwise fact about true column choices into a row statement on family classes. The row statement is the one that the field `aP10` of [the record HypsAlt](/step/hyps-alt-def/) asks for: a sharp column bound and a twisted column bound at the data of the family. The pointwise fact is [sharp column bounds for true columns, folded form](/entry/closing-true-cols/). The result goes to the relay [column valuations at bundle points, the statement form](/entry/level-prime-column-valuations-bundle-points-over-columns/) and from there to [six rows at a member](/entry/six-rows-at-member-alt/).

## Statement

For a datum $D$ of type `D7` and an object $O$ over it, let $R(D, O)$ be the statement: for every word $u$ of $D$, `Conclusion5Sharp D u` holds and `TwistedColumnBoundAtT O.X O.ex.tw u` holds. [Sharp column bounds for the datum of a true column choice](/entry/row-true/) says what these two predicates mean.

**Theorem.** Let $Q$ be a slot with `OverCols Q`. Let `Bd` be any bundle type and `Lk : LkT Bd` any link. Then `LevelPrimeColumnValuationsAtBundlePoints Q Lk` holds.

The words in the statement:

- A slot `V4.Slot` is a predicate on constructed points (a context $K$, stages, a frame, twist data and a core). `OverCols Q` says that each point in $Q$ is in `HasCols`. A point is in `HasCols` when it comes from a column datum `w : ColW B f T` and later stages $Z$, with a column view `ColView`: the jet condition `ColIn.JetsIn w.I`, a row integrality `RowInt`, the equation that the twisted forms of the object are `w.tw Z`, and a tied tuple.
- `LevelPrimeColumnValuationsAtBundlePoints Q Lk` is `Row Q Lk fun 𝒜 _ => LevelPrimeColumnValuationsClosed 𝒜`. `Row Q Lk H` says: there is a bundle property $E$ that holds eventually at all points in $Q$ and all bundles linked by `Lk` (`RowE`), and $H(\mathcal A, \sigma)$ holds for each class $\mathcal A$ and each selection $\sigma$ for $E$.
- `LevelPrimeColumnValuationsClosed 𝒜` is `EvC R 𝒜`, by definition. It says: [Closed](/step/closed-def/) on the class `W3 𝒜`, there is $x_0$ such that $R(F.D(x,i), \mathrm{obj}(F,x,i))$ holds for all $x \ge x_0$ with $x > x_1$ and all $i$.

## Proof

The proof reduces the row statement to the pointwise fact in four steps.

1. `Row0.row` reduces the claim to `Row0 Q (EvC R)`. This is the row statement for the trivial bundle type and the trivial link. So `Bd` and `Lk` play no role.
2. `validForConstructedPointClasses_eventuallyWorkingClass` reduces `Row0 Q (EvC R)` to this: eventually in the parameters, $R(\beta.D, \beta.O)$ holds at each constructed point $\beta$ in $Q$. Its proof takes $E = R$ and proves `Closed` with $\varepsilon_1 = 1$, the zero threshold record and $x_0 = 0$.
3. `EvP.of_all` reduces this to the same claim for all parameters.
4. `property_at_constructedPoints_of_trueColumnsView` reduces the claim at a point in `HasCols` to a claim at a column datum $w$, later stages $Z$, an object $O$ and a choice `nch` with a column view, with `BaseSigns B` and `RealTied (w.D Z)`. `OverCols Q` puts each point of $Q$ in `HasCols`.

At the column datum, the column view rewrites the twisted forms of $O$ to `w.tw Z`. Then [the folded sharp bound](/entry/closing-true-cols/) applies to `w.I`, `w.ok`, the jet condition, `BaseSigns B`, `w.l`, $Z$, `w.l0` and the division datum `O.X`. The rest is bookkeeping.

## In the Lean code

The theorem is in [LevelPrimeColumnValuationsBundlePointsOverColumn.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/LevelPrimeColumnValuationsBundlePointsOverColumn.lean#L11). The lemmas it calls:

- `Row0.row`, `EvP.of_all` and `validForConstructedPointClasses_eventuallyWorkingClass`, in [ValidForConstructedPointClassesEventuallyWorking.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/ValidForConstructedPointClassesEventuallyWorking.lean#L388).
- `GlobalTheory.T.property_at_constructedPoints_of_trueColumnsView`, a relay of `view_at_built`. We have read its statement, not the details of its proof.
- `GlobalTheory.LvT.Built.TrueCols.closing_true_cols`.

Some hypotheses are not used. The hypothesis `RealTied (w.D Z)` is dropped (it is the `_` in `intro B f T w Z O nch hv hs _ u`, line 17). Of the column view, only the jet condition and the equation for the twisted forms are used, not `rowInt` or `tup`. The "eventually" and "closed" parts of the row statement are not used either: the property holds at every point, and the thresholds are all zero.
