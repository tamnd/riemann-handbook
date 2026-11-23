---
id: main-theorem-published-results-final-alt-alt
title: The period identity on the row of linked bundles, renamed
kind: theorem
decl: GlobalTheory.T.main_theorem_published_results_final_alt_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.MainTheoremPublishedResultsFinal
covers: 10466
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [the period identity on the row of linked bundles](/entry/fam-mi-star-row-alt-alt/), which has the content. Its only user is [`miStarRowClosing_alt_alt`](/entry/mi-star-row-closing-alt-alt/). That caller gets the row of bundle point conditions from `point_lines_of_cusp_rapid_decay` and passes all other hypotheses on. The result goes to the multiplicity condition of branch 3 of the [unitary hypotheses node](/proof/unitary-hypotheses/).

## Statement

**Theorem.** Assume the thirteen literature hypotheses, the diagonal row hypothesis, $h_L$ : [RecTExists](/step/rect-exists-def/), parameters $p$ for $h_L$, that `RXs` is nonempty at each weighted point, and the row of `BundlePointConditions`. Then the row of the period identity `MIstar2` holds at the linked bundles.

Each word is defined in the [entry of the row theorem](/entry/fam-mi-star-row-alt-alt/). The two statements are the same.

## Proof

The proof is the term `GlobalTheory.Fam.miStar_row_alt_alt`. There is nothing else.

## In the Lean code

The theorem is in [MainTheoremPublishedResultsFinal.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MainTheoremPublishedResultsFinal.lean#L43), in the same file as the theorem it renames (line 24). The proof is `first | exact @miStar_row_alt_alt | ...`. The two types are the same text, word for word.

The name does not describe the statement. It is not a main theorem: it is one row statement deep inside branch 3. "Final" does not mark an end: the result goes up through `miStarRowClosing_alt_alt` and at least three more theorems before it reaches branch 3.

There is a version without "alt", `GlobalTheory.T.main_theorem_published_results_final` in [MainTheoremPublishedResultsFinalStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/MainTheoremPublishedResultsFinalStatement.lean#L34). It uses `LocalLanglandsGL`, `Bl.Prm`, `Bl.IsLinked` and `PtRows` in place of `RecTExists`, `Parameters`, `BundleLinkage` and `BundlePointConditions`.
