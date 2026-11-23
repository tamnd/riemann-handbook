---
id: true-column-joints-hold-all-tuples
title: Joints at every tuple for standard reads, restated
kind: theorem
decl: GlobalTheory.T.trueColumn_joints_hold_all_tuples
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.TrueColumnJointsHoldAllTuplesStatement
covers: 425
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`joints_all_true`](/entry/joints-all-true/). It has the same statement, and its proof applies that theorem. Its user is [`oneTie_jointsAt_all`](/entry/one-tie-joints-at-all/), which first replaces the kernel entry by one with standard reads. The content is in `joints_all_true`.

## Statement

The statement is that of [`joints_all_true`](/entry/joints-all-true/). In short: let $I$ be a true-columns datum with laws $l$, $l_0$ and a later stage $Z$, and let $t$ be a tied kernel entry of extra data `ex` over $D = I.\mathrm{rec7}(l, Z)$ whose reads are standard (`StdRd`) and whose pins are as described there. Under the standard conditions on $I$, `ex`, the columns $C$ and the group data $g$, and the tie `LatTied hT Gi Gl`, the entry $t$ has `JointsAt t a` for every tuple $a$, and $e_0(u, \mu_0) = e_{\mu_0}(u, 0)$ for every word $u$.

## Proof

Apply `joints_all_true`. Nothing else is used.

## In the Lean code

The theorem is at [TrueColumnJointsHoldAllTuplesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/TrueColumnJointsHoldAllTuplesStatement.lean#L10). The proof is the tactic

```
first | exact @GlobalTheory.TwU.AllTuples.joints_all_true | exact GlobalTheory.TwU.AllTuples.joints_all_true | (intros; apply GlobalTheory.TwU.AllTuples.joints_all_true <;> assumption)
```

The two statements are the same text. In contrast to [`oneTie_jointsAt_all`](/entry/one-tie-joints-at-all/), the conclusion is about the given entry $t$, not about some other entry.
