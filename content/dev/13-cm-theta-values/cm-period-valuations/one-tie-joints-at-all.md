---
id: one-tie-joints-at-all
title: Joints at every tuple after a change to standard reads
kind: theorem
decl: GlobalTheory.Pdv.oneTie_jointsAt_all
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.KernelRelationTrueColumnsJointsAllTuples
covers: 427
status: drafted
drafted_by: writer@claude
---
This theorem proves that some tied kernel entry has joints at every tuple. It replaces the given entry by one whose reads are the standard reads, and then applies [`trueColumn_joints_hold_all_tuples`](/entry/true-column-joints-hold-all-tuples/). Its user is the restatement [`kernel_relation_true_columns_joints_all_tuples`](/entry/kernel-relation-true-columns-joints-all-tuples/), and through it [`jointsAt_all_std`](/entry/joints-at-all-std/). The content is in [`joints_all_true`](/entry/joints-all-true/).

## Statement

Let $I$ be a true-columns datum (`TC B X`) over a base $B$, with laws $l$, $l_0$ and a later stage $Z$, and let $D = I.\mathrm{rec7}(l, Z)$. Let $L, h_T, G_i, G_l, K, Y, c_X$ and `ex` be size data, ties, instances, constants, division data and extra data over $D$, and let $t$ be a tied kernel entry of `ex`. Let $C$ be symmetric tied columns of $D$ (`ColsTiedSym`) with a fullness datum `full`, let $g$ be group compatibility data for `ex.cmp`, and let `tp` be a tied tuple datum for a choice `nch`.

**Theorem.** Assume:

- on $I$: `I.Ok`, `TC.Pins`, `I.IsTw`, `JetsIn I`, and $\mathrm{tp}.\xi = I.\xi$;
- on `ex`: $\mathrm{ex.tw} = I.\mathrm{tw}(l, l_0, Z)$ and $\mathrm{ex.errX}.\pi_T = X.\pi_T$;
- on $t$: `I.StdKer l Z t`;
- on $C$, `full` and $g$: `I.StdC l Z C`, `I.StdLvC l Z u (C.forms u)` for every word $u$, `I.StdDt` for the determinant of `full`, $g.\mathrm{herm} = \mathrm{full.to0}$ and $g.\mathrm{forms}(u) = (C.\mathrm{forms}\,u).\mathrm{to0}$;
- each value $\chi_D(z)$ is the image under `embLL` of an element of `LL`;
- `LatTied hT Gi Gl`.

Then there is a tied kernel entry $t'$ of `ex` with `JointsAt t' μ` for every tuple $\mu$, and $e_0(u, \mu_0) = e_{\mu_0}(u, 0)$ for every word $u$. We have not unfolded the conditions on $I$, $C$ and $g$.

## Proof

1. `stdKer_stdRd_mark` gives a tied kernel entry $t'$: it is $t$ with its reads replaced by the standard reads `I.kerRd l Z`. It satisfies `StdKer`, `StdRd` (each read of $t'$ is a standard read, `RdStd`), `TopPinned`, and a description of the pins of its reads: the pin at step $i$ and class $c$ holds when $i + 1 \le m$ or the class lies over a row (`OverRow`).
2. [`trueColumn_joints_hold_all_tuples`](/entry/true-column-joints-hold-all-tuples/), applied to $t'$, gives the joints of $t'$ and the identity of forms.

## In the Lean code

The theorem is at [KernelRelationTrueColumnsJointsAllTuples.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/KernelRelationTrueColumnsJointsAllTuples.lean#L15). It calls `GlobalTheory.Pdv.stdKer_stdRd_mark` in [StdKerStdRdMark.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/StdKerStdRdMark.lean#L17) and `GlobalTheory.T.trueColumn_joints_hold_all_tuples`. `StdRd` is in [ColNorm.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/ColNorm.lean#L28).

Two hypotheses are never used: $\mathrm{tp}.\xi = I.\xi$ (`_htp`) and the condition `StdLvC` (`_hLv`), line 16. So the data `nch` and `tp` play no part. The conclusion is existential: it does not say that $t$ itself has joints. The fact `TopPinned` from step 1 is dropped.
