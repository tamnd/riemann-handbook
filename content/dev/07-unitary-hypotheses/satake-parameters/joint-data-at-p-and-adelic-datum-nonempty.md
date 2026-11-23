---
id: joint-data-at-p-and-adelic-datum-nonempty
title: Each joint has a site, restated
kind: theorem
decl: GlobalTheory.T.jointData_at_p_and_adelicDatum_nonempty
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.JointDataAtPAndAdelicDatumNonemptyStatement
covers: 750
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`joint_at_nonempty`](/entry/joint-at-nonempty/). It has the same statement, and its proof applies that theorem. Its user is [`site_cmpLite_siteAdm`](/entry/site-cmp-lite-site-adm/), which calls it in its step 3 to get a joint site and then gives that site to [`admissible_at_each_site`](/entry/admissible-at-each-site/). The content is in `joint_at_nonempty`, which dominates 749 of the 750 declarations below this theorem.

## Statement

Assume `CurveEx`. Let $D$ be a datum of type `D7` with its size data, ties, instances, division data and extra data `ex`, and let $t$ be a tied kernel entry of `ex`. Let $(u, \mu, w, h_g)$ be a site whose residue characteristic $p$ is prime, $L_v$ a level structure, $I$ a comparison input, $H$ a hypothesis on $I$, $X$ a label of $I$, `std` a standard choice at $w$ and $J$ a joint (`Joint t H X`). Then the type `J.At std` of joint sites over $J$ is nonempty. `CurveEx` and joint sites are described in [`joint_at_nonempty`](/entry/joint-at-nonempty/) and [`admissible_at_each_site`](/entry/admissible-at-each-site/).

## Proof

Apply `joint_at_nonempty`. Nothing else is used.

## In the Lean code

The theorem is at [JointDataAtPAndAdelicDatumNonemptyStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/JointDataAtPAndAdelicDatumNonemptyStatement.lean#L8). Its proof is the tactic

```
first | exact @joint_at_nonempty | exact joint_at_nonempty | (intros; apply joint_at_nonempty <;> assumption)
```

(namespaces shortened), under `set_option maxHeartbeats 1000000`. The statement is word for word that of `joint_at_nonempty`, so the theorem is a renaming. The name speaks of "joint data at $p$" and "adelic datum": a joint site holds data at $p$ (an embedding into $\mathbb{C}_p$ and a curve datum) and an adelic datum with its laws.
