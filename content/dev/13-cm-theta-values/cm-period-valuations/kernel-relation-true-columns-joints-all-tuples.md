---
id: kernel-relation-true-columns-joints-all-tuples
title: Joints at every tuple over true columns, restated
kind: theorem
decl: GlobalTheory.T.kernel_relation_true_columns_joints_all_tuples
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.KernelRelationTrueColumnsJointsAllTuplesStatement
covers: 428
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`oneTie_jointsAt_all`](/entry/one-tie-joints-at-all/). It has the same statement, and its proof applies that theorem. Its user is [`jointsAt_all_std`](/entry/joints-at-all-std/), which gets the hypotheses from a column part. The content is in [`joints_all_true`](/entry/joints-all-true/), two levels down.

## Statement

The statement is that of [`oneTie_jointsAt_all`](/entry/one-tie-joints-at-all/). In short: let $I$ be a true-columns datum with laws $l$, $l_0$ and a later stage $Z$, let $D = I.\mathrm{rec7}(l, Z)$, and let $t$ be a tied kernel entry of extra data `ex` over $D$. Under the standard conditions on $I$, `ex`, $t$, the columns $C$ and the group data $g$, and the tie `LatTied hT Gi Gl`, there is a tied kernel entry $t'$ of `ex` with `JointsAt t' μ` for every tuple $\mu$, and $e_0(u, \mu_0) = e_{\mu_0}(u, 0)$ for every word $u$.

## Proof

Apply `oneTie_jointsAt_all`. Nothing else is used.

## In the Lean code

The theorem is at [KernelRelationTrueColumnsJointsAllTuplesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/KernelRelationTrueColumnsJointsAllTuplesStatement.lean#L14). The proof is the tactic

```
first | exact @GlobalTheory.Pdv.oneTie_jointsAt_all | exact GlobalTheory.Pdv.oneTie_jointsAt_all | (intros; apply GlobalTheory.Pdv.oneTie_jointsAt_all <;> assumption)
```

The two statements are the same text. The name speaks of a "kernel relation", but no relation between kernels appears in the statement: the conclusion is the existence of joints and an identity of twisted forms. Two hypotheses are never used (see [`oneTie_jointsAt_all`](/entry/one-tie-joints-at-all/)).
