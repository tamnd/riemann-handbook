---
id: pair-ex
title: Good pairs of primes exist at each large height
kind: theorem
decl: QH.pairEx
module: Development.AutomorphicArithmetic.MeanSquareBounds.pairEx
covers: 769
status: drafted
drafted_by: writer@claude
---
This theorem proves `PairEx`: at each large height $Y$ there are primes $(q, d)$ such that the twists of the characters modulo $M$ by the Jacobi symbols of $q$ and $d$ have zero-free boxes and small explicit formula sums. Its only user is [`supplyOfAdmOf`](/entry/supply-of-adm-of/), through `winPairs`.

## Statement

For a primitive [[Dirichlet character|JR4QSEFXWF]] $\chi \ne 1$ and $y \ge 1$ let

$$g_\chi(y) = \sum_{n \le y} \Lambda(n)\chi(n)\Bigl(\frac{y}{n} - 1\Bigr) + y\,\frac{L'}{L}(1, \chi),$$

with $\Lambda$ the [[von Mangoldt function|087EMZTHWN]]. Let $\mathrm{tw}_{ij}(\xi)(a) = \xi(a) (\tfrac{a}{q})^i (\tfrac{a}{d})^j$ for $i, j \in \{0, 1\}$, $z = Y^{\varepsilon/5}$, $z' = Y^{\varepsilon/5} \log^2 Y$ and $h_j = 8M e^{z + j z'}$. `PairGood M ε Y X q d` says:

1. (`WinPair`) $q \equiv 3 \pmod 8$ and $d \equiv 7 \pmod{16}$ are primes, $z/2 < \log q \le z$, $z'/2 < \log d \le z'$, $q \mid d + 1$, and $p \mid d + 1$ for each odd prime $p \le z$;
2. $\gcd(M, qd) = 1$;
3. for each $\xi$ modulo $M$, each $(i, j) \ne (0, 0)$ and each primitive $\chi$ that agrees with $\mathrm{tw}_{ij}(\xi)$ on integers prime to $2Mqd$: $|g_\chi(y)| \le y^{1/2 + \varepsilon/2}$ and $|\tfrac{L'}{L}(1, \chi)| \le 4 \log y$ for $Y \le y \le X$;
4. for each real primitive $\rho$ of conductor dividing $8M$ and each such $\chi$ for $\mathrm{tw}_{ij}(\rho)$: $L(s, \chi) \ne 0$ for $\operatorname{Re} s > 1 - \tfrac1{400}$, $|\operatorname{Im} s| \le h_j$.

**Theorem.** For each $M \ge 1$, $\varepsilon \in (0, \tfrac1{52})$ and $A \ge 1$ there is $Y_1$ such that for each $Y \ge Y_1$ there are $q, d$ with `PairGood M ε Y Y^A q d`.

## Proof

Apply [`pair_exists`](/entry/pair-exists/) with $\tau = \varepsilon/2$, $K = A$, $N_0 = 8M$, $X = Y^A$ and $z'$ as above. It gives $(q, d)$ with `Rows`, $q > 8M$, `GoodQ` and `GoodD`.

1. `Rows` gives `WinPair`. Since $d > q > 8M$, neither prime divides $M$.
2. `pairEx_box` lifts $\xi$ to modulus $8M$ and uses `ind_drop` to change the modulus of agreement. So `Box` holds for each $\chi$ of clauses 3 and 4, with height $h_j$. This gives clause 4 and the bound on $g_\chi$ (`pairEx_g` identifies the two forms of $g_\chi$).
3. The bound $|\tfrac{L'}{L}(1, \chi)| \le 4 \log Y$ comes from `kappa4`, since $Y^{\varepsilon/6} \le \log h_j \le 3 Y^{\varepsilon/5} \log^2 Y$.

## In the Lean code

The theorem is in [pairEx.lean](lean:Development/AutomorphicArithmetic/MeanSquareBounds/pairEx.lean#L112). `PairEx` and `PairGood` are in [PairGood.lean](lean:Development/AutomorphicArithmetic/CharacterBoxes/PairGood.lean#L18), `WinPair` in [ExistsPageN.lean](lean:Development/AutomorphicArithmetic/CharacterBoxes/ExistsPageN.lean#L27).

`Box` also holds a bound $C \log Y$ for $\tfrac{L'}{L}(1, \chi)$, with $C$ from `pair_exists`. The proof drops it and uses `kappa4` for the constant $4$.
