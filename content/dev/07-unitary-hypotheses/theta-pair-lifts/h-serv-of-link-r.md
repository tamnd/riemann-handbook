---
id: h-serv-of-link-r
title: The service row from Artin reciprocity, restated
kind: theorem
decl: GlobalTheory.T.hServ_of_linkR
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.RowHServOfLinkStatement
covers: 10829
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`row_hServ_of_link_alt`](/entry/row-h-serv-of-link-alt/). It has the same statement, and its proof applies that theorem. Its user is [`allRows_of_open0_alt`](/entry/all-rows-of-open0-alt/), which gets the field `hServ` of the record `AllRowsAlt` from it. The real content is two levels lower, in [`servH_row_linkR_alt`](/entry/serv-h-row-link-r-alt/), which dominates 10,819 of the 10,829 declarations below this theorem.

## Statement

Assume `GlobalArtinReciprocity`. Let $h_L$ witness [RecTExists](/step/rect-exists-def/), let $p$ be parameters for $h_L$, and let $L_k$ be a linkage of bundles. Assume that for each context $K$, point $\beta$, real $c$ and bundle $b$ at $\beta$, if $L_k$ links $b$ then `ReciprocityLinkage p` links the reciprocity record $b.R$ of $b$. Then the service row `SlotServiceCondition (IsGoodE p.s) Lk` holds.

The hypothesis, the service row and `ReciprocityLinkage` are described in the entry [`row_hServ_of_link_alt`](/entry/row-h-serv-of-link-alt/).

## Proof

The proof is `row_hServ_of_link_alt`. Nothing else is used.

## In the Lean code

The theorem is at [RowHServOfLinkStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowHServOfLinkStatement.lean#L14). Its proof is the tactic

```
first | exact @row_hServ_of_link_alt | exact row_hServ_of_link_alt | (intros; apply row_hServ_of_link_alt <;> assumption)
```

(namespaces shortened), under `set_option maxHeartbeats 1000000`. The first branch already closes the goal, because the two statements are the same. So this theorem is a renaming. The file name says "statement": the file only fixes the statement in the namespace `GlobalTheory.T` and points to the proof in [RowHServOfLink.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowHServOfLink.lean#L17). The same pattern is used one level lower: `reciprocity_kernel_of_artin` is a renaming of `servH_row_linkR_alt`.
