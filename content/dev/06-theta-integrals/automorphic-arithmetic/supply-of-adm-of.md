---
id: supply-of-adm-of
title: Hosts for one character, given a host builder
kind: theorem
decl: UpperTheory.T3.supplyOfAdmOf
module: Development.AutomorphicArithmetic.ShortNorms.supplyOfAdmOf
covers: 862
status: drafted
drafted_by: writer@claude
---
This theorem is [`supplyOfAdm`](/entry/supply-of-adm/) with one more hypothesis: a builder that completes host axioms to a good host. `supplyOfAdm` is `supplyOfAdmOf hostOfField`, and [`hostOfField`](/entry/host-of-field/) gets the builder from [`hostOfFieldOf`](/entry/host-of-field-of/).

## Statement

(B) says: for each $\varepsilon \in (0, \tfrac1{52})$ and $C_0 \ge 1$ there are constants $C_{T2}$, $C_8 \ge C_0$, $c_6, C_b > 0$ and $x_0$ as follows. Let $s$ be a scale with $s.\varepsilon = \varepsilon$ and $s.x \ge x_0$, let $R$ be ranks with `RankVal s R`, let $H_0$ be host axioms on the frame of $R$, with primes $q, d$ and modulus $Q_S$, and let $M \ge 1$ and $Y$ satisfy:

1. $s.J, o(R), M \le C_0$ and $Q_S \le C_0\, n(R)$;
2. $Q_S$ divides $\operatorname{lcm}(2^{e+2}, M)$, with $e$ the exponent of $R$;
3. $s.x^{1/s.J} \le Y \le s.x$;
4. `PairGood M ε Y s.x q d` holds ([`pairEx`](/entry/pair-ex/));
5. `FieldRows H0 ⌊Y^{ε/5}⌋` and `admitted R H0` hold.

Then there are a host $H$ over $H_0$ with constant $C_{T2}$ and a prime $q_0$ with `HostGood s C8 4 c6 Cb H q0`, and the set $TT$ of $H$ has `Shares` with error $s.x^{-1+\varepsilon}$.

**Theorem.** If (B) holds, then for each primitive [[Dirichlet character|JR4QSEFXWF]] $\psi$ with `VWinAt ψ 401` and the input `hAdm` on ranks, `HostExW (3/2) P` holds, as in the parent entry.

## Proof

The parent entry has the main steps. Let $N$ be the conductor of $\psi$.

1. [`QH.pairEx`](/entry/pair-ex/) gives `winPairs` its input `PairEx`. So each `WinDatum` holds a pair $(q, d)$ with `PairGood N ε Y x q d`.
2. (B) is used with $M = N$ and $C_0 = J + o(\mathrm{Level.cyc}\,\psi) + 8N$, with $J$ from `winPairs`.
3. Let $A^{\varepsilon/5} = 5 + 4N$. The threshold $x_1$ is above those of (B) and `hAdm`, and above $A^J$ and $c\, 2^{e_0}$, with $c$ and $e_0$ from `fieldChi`. Then $Y \ge A$, so $\lfloor Y^{\varepsilon/5} \rfloor \ge 4N$, as `fieldChi` needs.
4. $q \ne 3$, since $\log q > Y^{\varepsilon/5}/2 > \log 3$. And $e \ge e_0$, since $c\,2^e \ge x > c\,2^{e_0}$.
5. $Q_S \le 4N c\,2^e \le 8N x^{2+8\varepsilon} \le C_0\, n(R)$, by `RankVal`.
6. Since $Q_S \mid \operatorname{lcm}(2^{e+2}, N)$, each prime factor of $Q_S$ divides $2N$, as `boundedTw` needs.

## In the Lean code

The theorem is in [supplyOfAdmOf.lean](lean:Development/AutomorphicArithmetic/ShortNorms/supplyOfAdmOf.lean#L13). Hypothesis (B) is word for word the statement of `hostOfField`, and the conclusion is word for word the statement of `supplyOfAdm`. It also calls `pairHyp` and `isChiField`. The module is in the folder `ShortNorms`, but the proof uses no short norm statement except through (B).
