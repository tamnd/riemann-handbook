---
id: local-bessel-uniqueness-holds
title: The spectral setting, under the name of local Bessel uniqueness
kind: theorem
decl: GlobalTheory.T.local_bessel_uniqueness_holds
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.LocalBesselUniquenessHolds
covers: 1860
status: drafted
drafted_by: writer@claude
---
This theorem is a copy of [`exists_spectralData_gap_alt`](/entry/exists-spectral-data-gap-alt/) under a second name. It gives, for each datum with large gaps and local ties, a Hida setting with a full datum, transports and an integrable archimedean coefficient. Its only user is [`exists_sPack_integrable_alt`](/entry/exists-s-pack-integrable-alt/), which puts the result into an S-pack. Below this theorem are 1,860 declarations, one more than below the copy.

## Statement

The statement is the statement of [`exists_spectralData_gap_alt`](/entry/exists-spectral-data-gap-alt/), word for word. Assume `SiegelWeilUnitaryConvergent` and `RowsFinDim`. Let $D$ be a datum with `GapHyp D` and `LocTied D`, and let $F$ give a form for each word. Then there are a Hida setting $X$ for $D$, an adelic bridge isomorphism, an additive character $\psi$ of $\mathbb{A}_F$, a full datum $Y$ over $X$ with `FinX Y`, and a transport for each word, with eleven properties. The entry of the copy lists them.

## Proof

The proof is `exact exists_spectralData_gap_alt`, inside a `first | … | …` tactic that tries three forms of the same call. There is no other content.

## In the Lean code

The theorem is in [LocalBesselUniquenessHolds.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/LocalBesselUniquenessHolds.lean#L9).

The name is misleading. The statement is an existence statement, and no uniqueness appears in it. A uniqueness statement does enter the proof of the copy: `wuDecayOfGap_holds'` is proved from `besselMapUniqGap`, which says that two Bessel maps of a discrete series with large gaps are linearly dependent on smooth vectors. The name may refer to that step. The statement here does not mention Bessel maps.
