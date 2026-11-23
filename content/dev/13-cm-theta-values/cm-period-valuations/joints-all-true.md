---
id: joints-all-true
title: Joints at every tuple for a kernel entry with standard reads
kind: theorem
decl: GlobalTheory.TwU.AllTuples.joints_all_true
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.TrueColumnJointsHoldAllTuples
covers: 424
status: drafted
drafted_by: writer@claude
---
This theorem proves that a tied kernel entry over a true-columns datum has a joint at every good site of every tuple, and that the twisted forms at step zero agree at the reference tuple. Its user is the restatement [`trueColumn_joints_hold_all_tuples`](/entry/true-column-joints-hold-all-tuples/), and through it [`oneTie_jointsAt_all`](/entry/one-tie-joints-at-all/) and [`jointsAt_all_std`](/entry/joints-at-all-std/).

## Statement

Let $I$, $l$, $l_0$, $Z$, $D = I.\mathrm{rec7}(l, Z)$, the data $L, h_T, G_i, G_l, K, Y, c_X$, `ex`, the tied kernel entry $t$, the columns $C$ with `full`, and the group data $g$ be as in [`oneTie_jointsAt_all`](/entry/one-tie-joints-at-all/). There is no tuple datum here.

**Theorem.** Assume `I.Ok`, `TC.Pins`, `I.IsTw`, `JetsIn I`, $\mathrm{ex.tw} = I.\mathrm{tw}(l, l_0, Z)$, $\mathrm{ex.errX}.\pi_T = X.\pi_T$, `I.StdKer l Z t`, `I.StdC l Z C`, `I.StdDt` for `full`, $g.\mathrm{herm} = \mathrm{full.to0}$, $g.\mathrm{forms}(u) = (C.\mathrm{forms}\,u).\mathrm{to0}$, the condition on the values of $\chi_D$, and `LatTied hT Gi Gl`. Assume also:

- `StdRd I l Z t`: each read $t.\mathrm{rd}(u, a)$ is a standard read, that is, its sizes $N$ are those of the representatives of the classes of $I$, and below level $m$ its values $\Xi$ are the images under `embLL` of the values `xiAt` of $I$;
- for each word $u$, tuple $a$, step $i$ and class $c$, the pin of $t.\mathrm{rd}(u, a)$ at $(i, c)$ holds if and only if $i + 1 \le m$ or the representative of $c$ lies over a row (`OverRow`).

Then `JointsAt t a` for every tuple $a$, and $e_0(u, \mu_0) = e_{\mu_0}(u, 0)$ for every word $u$.

## Proof

1. **Joints.** Fix a tuple $a$. `trueColumn_exists_chainCharts_kernelData_forms` (a second name for `jIn_nonempty_true`) gives for each word $u$ an element of `JIn t u a`. This is a structure of 23 fields with no site in it: group data, hermitian columns, chain charts at each step, adelic data with pins and a tie, an element of $\mathcal{O}_E$, and conditions that tie step zero of the charts to step zero of the forms. The proof chooses good charts at every stage (`trueColumnChoice_goodCharts_every_stage`) and compatible kernel data (`trueColumn_kernelData_compatible_stepCharts`).
2. `jointsAtSplitUnramifiedPlaces_of_chainCharts` (a second name for `jointsAt_of_jIn`) turns these and `LatTied` into `JointsAt t a`. At each site $w$ with residue characteristic outside $Q_p(a)$, it builds comparison site data from the charts (`exists_comparisonSiteData_over_chainCharts`), the hypothesis on the comparison (`comparison_data_statements_at_site`) and a label (`exists_labIn_c0_cls_eq_levelZeroClass`), and assembles a joint.
3. **Forms.** Rewrite with $\mathrm{ex.tw} = I.\mathrm{tw}(l, l_0, Z)$ and apply `tw_e0_mu0_eq_eMu0_zero` (a second name for `stepZeroFormIdentification_refTuple_eq_id`). Its proof uses the law $l_0$ at $(u, \mu_0)$, the fact that the step zero twist at the reference tuple is the identity, and the injectivity of an embedding.

## In the Lean code

The theorem is at [TrueColumnJointsHoldAllTuples.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/TrueColumnJointsHoldAllTuples.lean#L14). The three lemmas it calls are second names; the proofs are `jointsAt_of_jIn` in [JointsAtSplitUnramifiedPlacesOfChainCharts.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/JointsAtSplitUnramifiedPlacesOfChainCharts.lean#L26), `jIn_nonempty_true` in [TrueColumnExistsChainChartsKernelDataForms.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/TrueColumnExistsChainChartsKernelDataForms.lean#L23) and `stepZeroFormIdentification_refTuple_eq_id` in [StepZeroFormIdentificationRefTupleEqId.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/StepZeroFormIdentificationRefTupleEqId.lean#L13). `JIn` is in [JointCmpEmbeddingYAlt.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/JointCmpEmbeddingYAlt.lean#L54).

All hypotheses are used. The second conclusion does not depend on $t$, $C$ or $g$: it uses only the equality of twists. `stepZeroFormIdentification_refTuple_eq_id` takes `I.Ok` and `TC.Pins` but does not use them (line 14). We have not opened the lemmas that `jIn_nonempty_true` and `jointsAt_of_jIn` call.
