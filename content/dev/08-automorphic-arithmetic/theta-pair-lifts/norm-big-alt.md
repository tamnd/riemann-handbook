---
id: norm-big-alt
title: The norm of a large bottom pair is a fixed multiple of an L-value product
kind: theorem
decl: GlobalTheory.NormBigProof.normBig_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.NormBigOfNonvanishing
covers: 384
status: drafted
drafted_by: writer@claude
---
This theorem proves `NormBig`: the norm of the large member of a bottom pair at $t$ is a product of L-values at $t$ times a nonzero constant that does not depend on $t$. Its renaming [`normBig_of_lNe`](/entry/norm-big-of-l-ne/) goes to [the joined estimates of the square top term](/entry/square-top-term-joined-estimates/), where `NormBig` is an input for `BotNe`.

## Statement

**Theorem.** Assume [`ThetaLocalInputs`](/step/theta-local-inputs-def/), the record `Inp D` for every datum $D$, and `LNe`. Then `NormBig` holds.

`LNe` and `NormBig` have the form `GBig Q` of [the tower entry](/entry/tower-alt-bis/), which also states `LNe`. `Inp D` is a record of 22 facts about $D$ that we have not unfolded.

For $Q$ in `NormBig`, put $e_0 = \lfloor (b - b')/2 \rfloor$ and $h_0 = \lfloor (b + b')/2 \rfloor$, where $b$ and $b'$ are the ranks `botBig` and `botSmall` of the bottom stage $(i, j)$. A *bottom pair* at $t$ is a pair $(P, P')$ of the structure `Pair` with $P$ of rank $(b, b + b')$ and $P'$ of rank $(b', b + b')$, with fixed characters, standard data and block level for the ideal `modT G t` (`IsBottom`). The norm of $P$ is

$$\|P\| = \sum_{h} \frac{1}{|\Gamma_h|} \sum_{T} |P(h, T)|^2,$$

a weighted sum over the classes $h$ of $\mathrm{GA}_d$ modulo the level group $J$ of $P$, of squares of coordinates. Then `NormBig` says: for all $\delta, t_0, i, j$ there is $A \neq 0$ such that for every $t$, every bottom pair $(P, P')$ at $t$ and every L-function $\Lambda$ of the character $\nu_H(t, i, j)$,

$$\|P\| = A \prod_{s = 1 - e_0}^{h_0} \Lambda(s).$$

## Proof

The thresholds are the maxima of those of `LNe` and two lemmas.

1. Suppose that a bottom pair $(P_0, P_0')$ exists at some point $t_0$. Let $\Lambda_0$ be the L-function of $\nu_H(t_0, i, j)$ from `LNe`. Since $h_0 \le$ `halfRank` (`squareBottomHalfRankSum_le_halfRank`), `LNe` gives $\prod_{s} \Lambda_0(s) \neq 0$.
2. `big_theta_lift_ne_zero_of_petersson_norm` gives $\|P_0\| \neq 0$. Put $A = \|P_0\| / \prod_s \Lambda_0(s)$.
3. `theta_lift_petersson_norm_ratio_formula` gives $\|P\| \prod_s \Lambda_0(s) = \|P_0\| \prod_s \Lambda(s)$ for each bottom pair $(P, P')$ at $t$. Divide.
4. If no bottom pair exists at any point, take $A = 1$. The statement is then vacuous.

Both lemmas rest on [the norm formula for one bottom pair](/entry/petersson-norm-bottom-theta-lift-eq/), which has the real content.

## In the Lean code

The theorem is at [NormBigOfNonvanishing.lean line 14](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/NormBigOfNonvanishing.lean#L14). `NormBig` and `LNe` are in [NormSmall.lean](lean:Development/AbelianVarietyTheory/Statements/PlaceShiftStatements/NormSmall.lean#L114), and `Pair.norm` in [NormSumPairRankZeroOfCurveCoordNorm.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/NormSumPairRankZeroOfCurveCoordNorm.lean#L161).

Odd points:

- The ratio lemma, `big_theta_petersson_norm_ratio_eq` in [ThetaLiftPeterssonNormEqRallisIntegral.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/ThetaLiftPeterssonNormEqRallisIntegral.lean#L115), takes `LNe` but does not use it, and its thresholds are 0.
- `normBig_of_lNe` at line 48 is a `first | exact` wrapper of this theorem.
- [NormBigOfNonvanishing.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/NormBigOfNonvanishing.lean#L18) has `normBig`, with the same conclusion and the hypothesis `Hypotheses₂` in place of `ThetaLocalInputs`.
