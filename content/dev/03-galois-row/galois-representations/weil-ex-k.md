---
id: weil-ex-k
title: Weil representations exist for good unitary dual pairs
kind: theorem
decl: PositivityTheory.ThKW.S.weilEx_k
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.ThetaParseval.ThetaKernels.WpSTop
covers: 395
status: drafted
drafted_by: writer@claude
---
This theorem is a second name. It packages [the existence of the Weil representation](/entry/exists-is-weil-k/) as the statement `WeilEx_k`, so that [the tools theorem](/proof/determinants/) can use it. All the content is in [the existence entry](/entry/exists-is-weil-k/).

## Statement

**Theorem.** Let $E/F$ be number fields with an involution $\sigma$ and base data $B$ that satisfy `GoodK`. Let $X$ be a hermitian space of signature $(r, s)$ and $W$ a skew-hermitian space of signature $(r', s')$. Let $M$ be a good tensor model for $(X, W)$. Let $\chi_X, \chi_W$ be Hecke characters. Assume that on an idele $a$ of $F$, $\chi_X(a)$ is $1$ when $a$ is in $F^\times$ times the norms from $E$, and $(-1)^n$ when it is not (this is `ResEtaPow`). Assume the same for $\chi_W$ with $(-1)^d$. Then a Weil representation $\omega$ for $M$, $\psi$, $\chi_X$ and $\chi_W$ exists.

## Proof

The proof term is `exists_isWeil_k`. The statement `WeilEx_k` has the same text as the type of that theorem, so no step is needed.

## In the Lean code

- The theorem is in [WpSTop.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/WpSTop.lean#L45). The statement `WeilEx_k` is in [ThkTowStmt.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/ThkTowStmt.lean#L18).
- It has one use, in [TPGHolds.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/TPGHolds.lean#L52). There `pairEx_of_k` joins it with `modelEx_k` to fill the field `pairEx` of `Tools_k`.
- It is a copy of `weilEx` in [WeilEx.lean](lean:Development/WeilBound/ThetaLifts/Reductions/WeilPairs/WeilPairExistence/WeilEx.lean#L49) ([its entry](/entry/s-weil-ex/)). The only change is `GoodK` in place of `IsGood`.
