---
id: exists-adelic-datum-with-laws-at-joint
title: A joint carries an adelic datum with its laws, restated
kind: theorem
decl: GlobalTheory.T.exists_adelicDatum_with_laws_at_joint
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.ExistsAdelicDatumWithLawsAtJointStatement
covers: 721
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`exists_adLawAt_joint`](/entry/exists-ad-law-at-joint/). It has the same statement, and its proof applies that theorem. Its user is [`joint_at_nonempty`](/entry/joint-at-nonempty/), which takes from it the adelic datum, the characters and the law of a joint site. The content is in [`adLawAt_xiAd`](/entry/ad-law-at-xi-ad/), which dominates 710 of the 721 declarations below this theorem.

## Statement

Let $t$ be a tied kernel entry, $(u, \mu, w, h_g)$ a site with residue characteristic $p$ prime, `std` a standard choice at $w$ and $J$ a joint (`Joint t H X`), as in [`joint_at_nonempty`](/entry/joint-at-nonempty/). Then there are an adelic datum $\Xi$ over the chain charts of $J$ and a family $\mu_T$ of functions on the finite ideles $(E \otimes_F \mathbb{A}_{F,f})^\times$ such that `AdLawAt J.A J.dtU J.a Ξ μ_T` holds. The law `AdLawAt` is described in [`adLawAt_xiAd`](/entry/ad-law-at-xi-ad/).

## Proof

Apply `exists_adLawAt_joint`. Nothing else is used.

## In the Lean code

The theorem is at [ExistsAdelicDatumWithLawsAtJointStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/ExistsAdelicDatumWithLawsAtJointStatement.lean#L9). Its proof is the tactic

```
first | exact @exists_adLawAt_joint | exact exists_adLawAt_joint | (intros; apply exists_adLawAt_joint <;> assumption)
```

(namespaces shortened), under `set_option maxHeartbeats 1000000`. The statement is word for word that of `exists_adLawAt_joint`, so the theorem is a renaming. As there, the standard choice `std` and the prime $p$ do not occur in the conclusion.
