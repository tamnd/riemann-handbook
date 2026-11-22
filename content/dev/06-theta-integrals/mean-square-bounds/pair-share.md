---
id: pair-share
title: Most pairs of primes are good
kind: theorem
decl: QH.pair_share
module: Development.AutomorphicArithmetic.MeanSquareBounds.PairShare
covers: 721
status: drafted
drafted_by: writer@claude
---
Most primes $q$ of a first set are good, and for each good $q$ most primes $d$ of a second set are good. This pass-through joins `stage1` and `stage2`, which come from [`stage`](/entry/stage/), for [`pair_exists`](/entry/pair-exists/).

## Statement

Let $z = Y^{\varepsilon/5}$. $P_1$ is the set of primes $q \equiv 3 \pmod 8$ in $(e^{z/2}, e^{z}]$. $P_2(q)$ is the set of primes $d \equiv 7 \pmod{16}$ in $(e^{z'/2}, e^{z'}]$ such that $q$ and each prime $p \in [3, z]$ divide $d + 1$. `GoodQ` says: for each $\xi$ modulo $N_0$, the primitive characters of $\xi \cdot (\tfrac{\cdot}{q})$ satisfy `Box` with height $N_0 e^{z}$. `GoodD` says the same for $\xi \cdot (\tfrac{\cdot}{q})^a (\tfrac{\cdot}{d})$, $a \in \{0, 1\}$, with height $N_0 e^{z + z'}$.

**Theorem.** There is $C > 0$ such that for all $\varepsilon \in (0, \tfrac1{52})$, $\tau > 0$, $K, N_0 \ge 1$ and $\eta > 0$ there is $Y_0$ as follows. Let $Y \ge Y_0$, $X \le Y^K$ and $1 \le z'/(z \log^2 Y) \le K^2$. Then $P_1 \ne \emptyset$. At least $(1 - \eta)|P_1|$ primes $q \in P_1$ have `GoodQ`, $P_2(q) \ne \emptyset$, and `GoodD` for at least $(1 - \eta)|P_2(q)|$ primes $d \in P_2(q)$.

## Proof

`stage1` and `stage2` bound by $\eta |P_1|$ and $\eta |P_2(q)|$ each subset with no good element. `share_of_bad` applies this to the bad set. Take $C = \max(C_1, C_2)$. `boxAll_mono` lets $C$ grow and $Y^K$ shrink to $X$.

## In the Lean code

The theorem is in [PairShare.lean](lean:Development/AutomorphicArithmetic/MeanSquareBounds/PairShare.lean#L26). `stage1` ([Stage1Succ.lean](lean:Development/AutomorphicArithmetic/MeanSquareBounds/Stage1Succ.lean#L36)) applies `stage` with $m_0 = 8$, $a_0 = 3$, $U = e^{z}$. `stage2` ([CharOf.lean](lean:Development/AutomorphicArithmetic/MeanSquareBounds/CharOf.lean#L61)) uses $6\varepsilon/5$ for $\varepsilon$. We have read only the first lines of their proofs.
