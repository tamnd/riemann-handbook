---
id: adelic-chain-datum-character-laws-joint-kernel
title: The adelic chain datum satisfies its laws, restated
kind: theorem
decl: GlobalTheory.T.adelicChainDatum_characterLaws_jointKernel
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.AdelicChainDatumCharacterLawsJointKernelStatement
covers: 719
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`adLawAt_xiAd`](/entry/ad-law-at-xi-ad/). It has the same statement, and its proof applies that theorem. Its user is [`exists_adLawAt_joint`](/entry/exists-ad-law-at-joint/), which applies it to the adelic data of a joint. The content is in `adLawAt_xiAd`, which dominates 710 of the 719 declarations below this theorem.

## Statement

Let $t$ be a tied kernel entry, $(u, \mu)$ a word and a tuple, $\mathrm{St}$ chain charts, $A$ adelic data over $\mathrm{St}$, $d_U$ a homomorphism from the norm-one finite ideles to `D.Dt`, and $a \in \mathcal{O}_E$. If `AdPins A dtU` and `AdTie A dtU a` hold, then

$$\texttt{AdLawAt}\ A\ d_U\ a\ (\texttt{xiAd}\ A\ a)\ (\texttt{muOf}\ t\ u\ \mu\ d_U).$$

The datum `xiAd`, the characters `muOf` and the law `AdLawAt` are described in [`adLawAt_xiAd`](/entry/ad-law-at-xi-ad/). The Lean statement wraps the quantifiers and the two hypotheses in `UnderTie`.

## Proof

Apply `adLawAt_xiAd`. Nothing else is used.

## In the Lean code

The theorem is at [AdelicChainDatumCharacterLawsJointKernelStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/AdelicChainDatumCharacterLawsJointKernelStatement.lean#L6). Its proof is the tactic

```
first | exact @adLawAt_xiAd | exact adLawAt_xiAd | (intros; apply adLawAt_xiAd <;> assumption)
```

(namespaces shortened), under `set_option maxHeartbeats 1000000`. The statement is word for word that of `adLawAt_xiAd`, so the theorem is a renaming. `UnderTie` is in [UnderTie.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/UnderTie.lean#L106).
