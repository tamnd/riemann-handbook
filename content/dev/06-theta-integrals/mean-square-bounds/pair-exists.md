---
id: pair-exists
title: One good pair of primes from a positive share of good pairs
kind: theorem
decl: QH.pair_exists
module: Development.AutomorphicArithmetic.MeanSquareBounds.PairExists
covers: 727
status: drafted
drafted_by: writer@claude
---
This theorem picks one pair of primes $(q, d)$ for which all twisted characters satisfy `Box`. It is a pass-through to [`pair_share`](/entry/pair-share/), whose content is in [`stage`](/entry/stage/). Its only user is [`pairEx`](/entry/pair-ex/).

## Statement

Let $z = Y^{\varepsilon/5}$. `Rows z z' q d` says: $q \equiv 3 \pmod 8$ and $d \equiv 7 \pmod{16}$ are primes, $z/2 < \log q \le z$, $z'/2 < \log d \le z'$, $q < d$, and $p \mid d + 1$ for each odd prime $p$ with $p \le z$ or $p = q$. `GoodQ` and `GoodD` are as in [`pair_share`](/entry/pair-share/).

**Theorem.** There is $C > 0$ such that for all $\varepsilon \in (0, \tfrac1{52})$, $\tau > 0$, $K \ge 1$ and $N_0 \ge 1$ there is $Y_0$ with this property. For $Y \ge Y_0$, $X \le Y^K$ and $Y^{\varepsilon/5} \log^2 Y \le z' \le K^2\, Y^{\varepsilon/5} \log^2 Y$, there are $q, d$ with `Rows z z' q d`, $q > N_0$, `GoodQ N0 C τ Y X z q` and `GoodD N0 C τ Y X z z' q d`.

## Proof

`pair_share` with $\eta = \tfrac12$ gives a nonempty set $G_1$ of good $q$. Take $q \in G_1$, and in the same way $d$ in the good set $G_2$ for $q$. Then `rows_of_mem` gives `Rows`, since $2z \le z'$ for $Y \ge e^2$. For large $Y$, $z \ge 2N_0$, so $q \ge \log q + 1 > z/2 \ge N_0$.

## In the Lean code

The theorem is in [PairExists.lean](lean:Development/AutomorphicArithmetic/MeanSquareBounds/PairExists.lean#L9). `Rows`, `GoodQ` and `GoodD` are in [PrimeSetTwoBounds.lean](lean:Development/AutomorphicArithmetic/MeanSquareBounds/PrimeSetTwoBounds.lean#L48).
