---
id: square-top-term-joined-estimates
title: Twelve estimates on Hecke L-values and bottom pairs
kind: theorem
decl: GlobalTheory.SqTop.square_top_term_joined_estimates
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.SquareTopTermJoinedEstimates
covers: 2312
status: drafted
drafted_by: writer@claude
---
This theorem proves twelve statements about Hecke L-values, toric values and "bottom pairs" for all large data. It is restated as [`square_leading_term_bound`](/entry/square-leading-term-bound/), and [the bound on the maximal slope at fitted points](/entry/fitted-function-at-zero-close-alt/) uses all twelve conclusions in its leaf estimates. Below it are 2,312 declarations of the proof.

## Statement

Assume `HoweDualityReal`, [`ThetaLocalInputs`](/step/theta-local-inputs-def/), `HeckeFunctionalEquationAbs` (the functional equation $\Lambda(s) = \varepsilon N^{1/2-s} \Lambda'(1-s)$, $|\varepsilon| = 1$, of the [previous entries](/entry/fourier-coefficient-fit-of-join-alt/)), `ToricDenominator`, `Transport`, `ZetaDenominators`, `Refl`, [`ThetaIntegralsAgree`](/step/theta-integrals-agree-def/) and [`LocalMatching`](/step/local-matching-def/).

Each conclusion has the form `GBig Q`: there is $C_{F,0}$ such that for each $\varepsilon$ and each $C_F \ge C_{F,0}$ there are $C_0$ and $x_0$ with this property. For each $C \ge C_0$, each datum $D$ with size data $L$ such that $\varepsilon(L) = \varepsilon$, $x(L) \ge x_0$ and `Rec L` holds, each datum $L_c$ of type `LevCh` with base point $\mu_0$, and each grid $G$ at the constants $(1, C_F, b)$, the statement $Q(G, \mu_0, C, x, b)$ holds. `Rec L` asks, among other rows, that $F$ is the maximal real subfield of the CM field $E$ of $D$.

In the statements $Q$, "$\Lambda$ is an L-function of $\chi$" (`IsHeckeL χ Λ`) means: $\Lambda$ is entire and equals the Euler product of the Hecke character $\chi$ for $\operatorname{Re} s > 1$. Let $b_{TH} = C f b (\log b + \log x)$. The twelve statements, by group:

- **Field.** `FieldDat`: $E$ is CM and abelian over $\mathbb{Q}$, with field data and an integral lattice.
- **L-values.** `LNe`: the L-functions of certain characters $\nu_H(t, i, j)$ have no zero at the integers $s$ with $1 - e_0 \le s \le h$, where $h$ is `halfRank`, and those of a family of twists have no zero at the integers $s \ge 1$.
- **Toric values.** `TorEx`: each such value $\Lambda(s)$ is a nonzero toric value whose period normalization $\beta$ is algebraic. `DenEx`: each has a denominator function $n$ with finite support on the primes. `DenSum`: $\sum_{l \in S} n(l) \log l \le b_{TH}$. `ThbSt`: the toric values have height at most $b_{TH}$.
- **Bottom pairs.** `BotSmall`, `BotEx`, `BotNe` and `TriEx`: bottom pairs exist, they are small, they have a nonzero coordinate, and bottom triangles with constant coefficients exist.
- **Ratios.** `OneSqSt` bounds the valuations of a square ratio at each place. `Tower` writes a quotient of products of L-values as an away unit times a product of step ratios.

## Proof

1. `completedHeckeL_bounded_in_vertical_strips` (no hypothesis), `fieldDat` and the functional equation give `LNe` and an upper bound for L-values.
2. `Transport` gives `TorEx` and a bound `BetaArch`. `ZetaDenominators` gives `DenEx` and `DenSum`. `ToricDenominator` gives `ThbSt` and a lower bound `RhoLow`.
3. `botSmall_holds` proves `BotSmall` with no hypothesis. `cmThetaNormBoundHypotheses_satisfied` (no hypothesis) gives `BotEx`.
4. The theta inputs, `ThetaIntegralsAgree` and `LocalMatching` give `BotConst`, `Tower` and, with `HoweDualityReal`, `TriEx`. Then `bottomTheta_nonvanishing` gives `BotNe`.
5. `square_ratio_valuation_without_norm_formula` combines eleven of these facts with `Refl` and gives `OneSqSt`.

## In the Lean code

The theorem is in [SquareTopTermJoinedEstimates.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/SquareTopTermJoinedEstimates.lean#L13). The statements and `GBig` are in [NormSmall.lean](lean:Development/AbelianVarietyTheory/Statements/PlaceShiftStatements/NormSmall.lean#L34). Each hypothesis is used. `HoweDualityReal` is used only for `TriEx`.

The input `Refl` is assumed, not proved. It says $\Lambda(s)\Lambda_0(1-s) = \epsilon\,\Lambda(1-s)\Lambda_0(s)$ for $1 - e_0 \le s \le 0$, with $\epsilon$ an away unit. It looks like a consequence of the functional equation, but the proof does not derive it from `HeckeFunctionalEquationAbs`.

`BotSmall` contains the condition that the set of twisted places at $\mu_0$ is empty. It is proved by `botSmall_holds` with no hypothesis. We have not unfolded that proof.
