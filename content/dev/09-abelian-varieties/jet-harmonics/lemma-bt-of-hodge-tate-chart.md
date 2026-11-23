---
id: lemma-bt-of-hodge-tate-chart
title: The minor bound LemmaBT from the Hodge-Tate chart bound
kind: theorem
decl: GlobalTheory.PowGerm.lemmaBT_of_hodgeTate_chart
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.DepthBelowOneOfHodgeTateChartForm
covers: 471
status: drafted
drafted_by: writer@claude
---
This theorem passes hypotheses along. It proves `LemmaBT` from the chart bound `HTFSt p` for all primes $p$, by one call to [`lemmaBT_of_characters`](/entry/lemma-bt-of-characters/), which has the real content. Its second name is [`T.depthBelowOne_of_hodgeTate_chart_form`](/entry/depth-below-one-of-hodge-tate-chart-form/), which [`least_value_le`](/entry/least-value-le/) calls.

## Statement

**Theorem.** If `HTFSt p` holds for every prime $p$, then `LemmaBT` holds.

The [parent entry](/entry/depth-below-one-of-hodge-tate-chart-form/) states both. In short, `HTFSt p` says that $c\,O^d$ lies in the $O$-span of the differentials $\mathrm{dl}(u_k)$ of finitely many characters $u_k$ of a formal group, for each $c$ with $v(c)^{p-1} \le v(p)$. `LemmaBT` bounds the valuation of a product of minors.

## Proof

`lemmaBT_of_characters` takes five inputs. The proof supplies them:

1. three of the five parts of `firstFiveLaws`: the bundles `Laws`, `Laws2` and `Laws4`;
2. the first part of `twistBaseChange_and_valuation_statements`, that is, `TwistBaseChangeStatement`;
3. `T.exists_characters_boundedMinors_of_hodgeTateChartBound h`, which turns the hypothesis into the existence of character values with bounded leading minors.

There is no other step.

## In the Lean code

The theorem is in [DepthBelowOneOfHodgeTateChartForm.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/DepthBelowOneOfHodgeTateChartForm.lean#L24). The proof is a term of two lines.

The hypothesis is proved elsewhere in the code: `hodgeTate_inclusion_chart` in [HodgeTateInclusionChartCharacters.lean](lean:Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/HodgeTateInclusionChartCharacters.lean#L49) proves `HTFSt p` for every prime $p$. So the hypothesis is not an open input of the proof. The other parts of `firstFiveLaws` and `twistBaseChange_and_valuation_statements` are not used.
