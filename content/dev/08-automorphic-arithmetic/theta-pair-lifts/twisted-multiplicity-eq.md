---
id: twisted-multiplicity-eq
title: Equal cuspidal multiplicities from the conditions on a real datum
kind: theorem
decl: GlobalTheory.MultEqFinal.twisted_multiplicity_eq
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.TwistedMultiplicityOne
covers: 3684
status: drafted
drafted_by: writer@claude
---
This theorem only passes hypotheses along. It turns conditions on a real datum into the record `Given` and applies [the content entry](/entry/unitary-theory-of-harish-chandra-langlands-alt/). Its only user is [its renaming](/entry/twisted-multiplicity-one/), below [the last node of the trunk](/step/nonempty-hyps/).

## Statement

**Theorem.** Assume the ten published-result statements `HarishChandraAnalyticity`, `DiscreteSeriesClassification`, `CuspRapidDecay`, `HarishChandraFinite`, `CuspTraceClass`, `DixmierMalliavinFactorisation`, `FlathFactorisation`, `ZelevinskyPolynomialRing`, `GeometricLemma` and `GreenCuspidal`. Let $D$ be a datum (`D7`), $R$ a real datum of type `RealDat3 D A3 Ks` and $F$ a face of type `Face3 D A3`. Suppose:

1. the family $A_3$ satisfies `Ok3 s` for some $s \in \mathbb{N}$;
2. $R$ satisfies the weak characterisation at $F$, and `R.toRealDat.ExAt` holds;
3. the host hypothesis `HostHyp D` holds;
4. there are size data $L$ with a parameter choice;
5. `D.host.ccK = ⊤`;
6. the guard `QGuard` and the condition `GoodTypes` hold for the underlying real datum.

Then `MultEq` holds for the underlying real datum `R.toRealDat`. The content entry unfolds `MultEq`.

## Proof

`given_of_top` builds `Given R.toRealDat F.lv2`, a record of six fields. The core field comes from `core_of_weak`, applied to hypothesis 2. The parameter choice is hypothesis 4. The absolute irreducibility of the characters comes from the field `ok2.irr` of hypothesis 1. The fields `types` and `guard` are hypotheses 6. The gap condition $100 r^4 \le \lambda_n(\tau) - \lambda_{n+1}(\tau)$ is the field `gapR` of hypothesis 3. Then the content entry gives `MultEq`.

## In the Lean code

The theorem is at [TwistedMultiplicityOne.lean line 15](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedMultiplicityOne.lean#L15). It calls:

- `GlobalTheory.GivenOfTop.given_of_top`, at [ScalarHypothesesOfTopRows.lean line 18](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/ScalarHypothesesOfTopRows.lean#L18);
- `UpperTheory.Lit.I5.unitary_theory_of_harishChandra_langlands_alt`.

Odd points:

- Hypothesis 5, `D.host.ccK = ⊤`, is not used. `given_of_top` takes it as `hc` and does not use it.
- The parameter $s$ of hypothesis 1 is free. Only the field `ok2.irr` is used.
- Harish-Chandra analyticity and Flath factorisation are passed on and not used.
- The name says "twisted", but no twist appears in the statement.
