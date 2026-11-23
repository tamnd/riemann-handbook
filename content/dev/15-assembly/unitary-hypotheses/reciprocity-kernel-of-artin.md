---
id: reciprocity-kernel-of-artin
title: The service row for the reciprocity kernel, restated
kind: theorem
decl: GlobalTheory.T.reciprocity_kernel_of_artin
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ServHRowLinkRStatement
covers: 10820
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`servH_row_linkR_alt`](/entry/serv-h-row-link-r-alt/). It has the same statement, and its proof applies that theorem. Its user is [`row_hServ_of_link_alt`](/entry/row-h-serv-of-link-alt/), which turns it into the service row of the record `AllRowsAlt` in [the unitary hypotheses node](/proof/unitary-hypotheses/). The real content is two levels lower, in [`servH_row_of_artin`](/entry/serv-h-row-of-artin/).

## Statement

Assume `GlobalArtinReciprocity`. Let $h_L$ witness [RecTExists](/step/rect-exists-def/) and let $p$ be parameters for $h_L$. Then the [row](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/ValidForConstructedPointClassesEventuallyWorking.lean#L268) `Row (IsGoodE p.s) (ReciprocityLinkage p) (ServH ker)` holds, where `ker` sends a reciprocity record $R$ to its kernel entry `R.T.ker`. The notions are described in the entry [`servH_row_linkR_alt`](/entry/serv-h-row-link-r-alt/).

## Proof

The proof is `servH_row_linkR_alt`. Nothing else is used.

## In the Lean code

The theorem is at [ServHRowLinkRStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ServHRowLinkRStatement.lean#L14). Its proof is the tactic

```
first | exact @servH_row_linkR_alt | exact servH_row_linkR_alt | (intros; apply servH_row_linkR_alt <;> assumption)
```

(namespaces shortened). The first branch closes the goal, because the two statements are the same. So this theorem is a renaming.

The name can mislead. The "kernel" is the entry `R.T.ker` of a reciprocity record, not the kernel of the Artin map. Artin reciprocity is only a hypothesis here, and this proof does not use it.
