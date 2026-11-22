---
id: exists-bot-dat-of-placed-p-framed
title: One central pin for all placed framed Bessel data, in statement form
kind: theorem
decl: GlobalTheory.T.exists_botDat_of_placedP_framed
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.OneCentralPinStatement
covers: 1056
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`exists_botDat_pin_of_placed_of_framed`](/entry/exists-bot-dat-pin-of-placed-of-framed/). Its only user is [`famAllQ_of_allTrue_alt`](/entry/fam-all-q-of-all-true-alt/), which takes from it, in step 1 of its proof, the central element $z$ and the bottom data pinned at $z$. That theorem is part of the multiplicity condition in branch 3 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). The real content is in `exists_botDat_pin_of_placed_of_framed`.

## Statement

The statement is word for word the statement of [`exists_botDat_pin_of_placed_of_framed`](/entry/exists-bot-dat-pin-of-placed-of-framed/). In short: let $W$ be a real package over a datum $D$ with the package hypotheses, and let $1 \le r_S$. Then there is a central element $z$ of the adelic group of the space $Y_0$, with trivial archimedean component, such that each placed and framed Bessel datum $\mathcal B$ for a family character $f$ carries a bottom datum $d$ with base point $f.g.b_0$ and `d.Pin z`.

## Proof

The proof applies `exists_botDat_pin_of_placed_of_framed`. Nothing else happens.

## In the Lean code

The theorem is at [OneCentralPinStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OneCentralPinStatement.lean#L23). The proof is the tactic `first | exact @GlobalTheory.MiTop.exists_botDat_pin_of_placed_of_framed | ...`, so the theorem only passes its hypotheses along. The theorem name says `placedP`; the hypothesis is `PlacedConditions`.
