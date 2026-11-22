---
id: host-of-field
title: A good host for each admitted host datum
kind: theorem
decl: UpperTheory.Top.hostOfField
module: Development.AutomorphicArithmetic.CharacterBoxes.HostOfField
covers: 556
status: drafted
drafted_by: writer@claude
---
This theorem extends a host datum $H_0$ to a host $H$ with `HostGood`. It is a specialization, and the real content is in [the good host from the two prime inputs](/entry/host-of-field-of/). Its only user is [hosts for one character](/entry/supply-of-adm/), which describes the inputs `ShortNorm` and `SmallOne`.

## Statement

**Theorem.** Let $0 < \varepsilon < \tfrac1{52}$ and $C_0 \ge 1$. There are constants $C_{T2}$, $C_8 \ge C_0$, $c_6, C_b > 0$ and $x_0$ with this property. Take a scale $s$ with $s.\varepsilon = \varepsilon$, $s.x \ge x_0$, ranks $R$ with `RankVal s R`, a host datum $H_0$ with modulus $Q_S$ and primes $q, d$, an integer $0 < M \le C_0$ and $Y \in \mathbb{R}$. Assume $s.J, o(R) \le C_0$, $Q_S \le C_0 \, R.n$, $Q_S \mid \mathrm{lcm}(2^{R.e+2}, M)$, `PairWin s Y`, `PairGood M ε Y s.x q d`, `FieldRows` and `admitted R H0`. Then a host $H$ extends $H_0$ with constant $C_{T2}$, and a prime $q_0$ exists, with `HostGood s C8 4 c6 Cb H q0` and `Shares` for $H.TT$ with error $s.x^{-1+\varepsilon}$.

## Proof

The term is `hostOfFieldOf shortNorm smallOne`.

## In the Lean code

The theorem is in [HostOfField.lean](lean:Development/AutomorphicArithmetic/CharacterBoxes/HostOfField.lean#L8), `hostOfFieldOf` in [hostOfFieldOf.lean](lean:Development/AutomorphicArithmetic/ShortNorms/hostOfFieldOf.lean#L159).

- The constant $C_5$ of `HostGood` is fixed to $4$.
- The hypothesis `admitted R H0` is always true, as [hosts for one character](/entry/supply-of-adm/) says. We have not unfolded `FieldRows`.
