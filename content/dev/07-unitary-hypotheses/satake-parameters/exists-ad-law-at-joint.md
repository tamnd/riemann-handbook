---
id: exists-ad-law-at-joint
title: A joint carries an adelic datum with its laws
kind: theorem
decl: GlobalTheory.TwV.exists_adLawAt_joint
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.ExistsAdelicDatumWithLawsAtJoint
covers: 720
status: drafted
drafted_by: writer@claude
---
This theorem gives an adelic datum and characters that satisfy the law `AdLawAt` for the adelic data of a joint. It is a pass-through: it applies [`adelicChainDatum_characterLaws_jointKernel`](/entry/adelic-chain-datum-character-laws-joint-kernel/), the restated form of [`adLawAt_xiAd`](/entry/ad-law-at-xi-ad/), to five fields of the joint. It is used in the restated form [`exists_adelicDatum_with_laws_at_joint`](/entry/exists-adelic-datum-with-laws-at-joint/), in part 4 of [`joint_at_nonempty`](/entry/joint-at-nonempty/).

## Statement

Let $t$ be a tied kernel entry, $(u, \mu, w, h_g)$ a site with residue characteristic $p$ prime, `std` a standard choice at $w$ and $J$ a joint (`Joint t H X`). The joint holds chain charts $J.\mathrm{St}$, adelic data $A = J.A$ over them, a homomorphism $d_U = J.\mathrm{dtU}$ from the norm-one finite ideles to the group `D.Dt`, an element $a = J.a$ of $\mathcal{O}_E$, and the two conditions `AdPins A dtU` (`J.pins`) and `AdTie A dtU a` (`J.tie`).

**Theorem.** There are an adelic datum $\Xi$ over $J.\mathrm{St}$ and a family $\mu_T$ such that `AdLawAt A dtU a Ξ μ_T` holds.

## Proof

Take $\Xi = $ `xiAd A a` and $\mu_T = $ `muOf t u μ dtU`. [`adelicChainDatum_characterLaws_jointKernel`](/entry/adelic-chain-datum-character-laws-joint-kernel/), applied to $A$, $d_U$, $a$, `J.pins` and `J.tie`, gives the law. Nothing else is used.

## In the Lean code

The theorem is at [ExistsAdelicDatumWithLawsAtJoint.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/ExistsAdelicDatumWithLawsAtJoint.lean#L11). The proof is one line:

```
exact ⟨_, _, adelicChainDatum_characterLaws_jointKernel J.A J.dtU J.a J.pins J.tie⟩
```

The hypotheses `std` and the primality of $p$ are introduced and not used. Only five fields of $J$ enter the proof.
