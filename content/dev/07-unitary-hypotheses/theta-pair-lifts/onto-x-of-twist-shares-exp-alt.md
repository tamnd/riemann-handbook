---
id: onto-x-of-twist-shares-exp-alt
title: The surjectivity statement from the twist, share, bad places and exponent estimates
kind: theorem
decl: GlobalTheory.BigOn.ontoX_of_twist_shares_exp_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.OntoXOfTwistSharesExp
covers: 491
status: drafted
drafted_by: writer@claude
---
This theorem is the last step of [the surjectivity statement from twelve published inputs](/entry/onto-x-of-hypotheses-alt-alt/), step 7 there. It takes four estimates, proves the others again with no input, and calls the lemma that gives `SurjectiveOntoX`. That result goes to branch 2 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). Below this theorem are 491 declarations.

## Statement

**Theorem.** Assume `ExportedStatement`, `TwistStatement'`, `ShareStatement`, `BadPlacesStatement` and `ExponentStatement`. Then `SurjectiveOntoX` holds.

The four last statements say that, for each closed family hypothesis, there is $c_0$ such that for each constant $c \ge c_0$ that is bad in the sense of `OnPage.ConstBad`, eventually at points $p$, each recorded object $O$ at $p$ has the twist bound, the share bound, the bad share bound and, for all $C$, the exponent bound. `SurjectiveOntoX` is stated in [the parent entry](/entry/onto-x-of-hypotheses-alt-alt/). We have not unfolded the bounds on $O$.

## Proof

The first hypothesis, `ExportedStatement`, is not used. The proof is one call of `onto_x_of_all_estimates`, which needs nine statements. Four are the hypotheses. The other five are proved with no input:

1. the page statement, by `page_estimate_statement'`;
2. the geometric statement, by `geoSt_of_pageSt'` from the page statement;
3. the two runs statement and the rationality statement, by `runs_estimate_statement'` and `rational_estimate_statement'`;
4. the rank at twisted places, by `rank_at_twisted_places_of_max_geo` from the maximality statement (`maximum_estimate_statement'`), the geometric statement and the comparison off the own prime (`bigOn_comparison_at_twisted_places`).

## In the Lean code

The theorem is in [OntoXOfTwistSharesExp.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OntoXOfTwistSharesExp.lean#L21). `onto_x_of_all_estimates` is in [OntoPathStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OntoPathStatement.lean#L13); it is a second name for `OntoPath.onto_path_alt`, which we have not opened.

The first argument is bound by `intro _`, so it is never used. Its type is a hypothesis that does no work.

Each lemma of the proof is a second name. Five of them are second names of lemmas that the parent also calls: `pageSt_alt`, [`geoSt_of_pageSt_alt`](/entry/geo-st-of-page-st-alt/), `rankLocSt_of_max_geo_runs`, `maxSt_alt` and [`compareOffOwn_atRuns_alt`](/entry/compare-off-own-at-runs-alt/). So the page, geometric and rank statements are proved twice, once in the parent and once here. The other two stand for `bigOn_runsSt` and `bigOn_ratSt`, which the parent does not call. This is why the comparison off the own prime has two users. A parallel copy, `GlobalTheory.BigOn.ontoX_of_twist_shares_exp`, is in [OntoXOfTwistSharesExp.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/OntoXOfTwistSharesExp.lean#L21).
