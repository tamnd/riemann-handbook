---
id: supply-of-adm
title: Hosts for one character from the window bound and admissible ranks
kind: theorem
decl: UpperTheory.Top.supplyOfAdm
module: Development.AutomorphicArithmetic.CharacterBoxes.HostOfField
covers: 1448
status: drafted
drafted_by: writer@claude
---
This theorem builds, for one primitive character $\psi$, good hosts on windows of scale $\tfrac32$, from the window bound `VWinAt ψ 401` and an input on ranks. Its only user is [`supplyChi`](/entry/supply-chi/), which supplies the input on ranks. Through it, the hosts go to `zeroFreeAll_of_topG` in [ZeroFreeAll from Green, VWin and HypsAlt](/step/zero-free-all-of-green-v-win/).

## Statement

Let $\psi$ be a primitive [[Dirichlet character|JR4QSEFXWF]]. A scale $s$ has a size $s.x$ and a parameter $s.\varepsilon$. Ranks $R$ give a frame $\varphi$ with an order and an integer $o$.

Assume:

1. `VWinAt ψ 401`, as in [the step VWin](/step/vwin-def/);
2. (`hAdm`) for each $\varepsilon \in (0, \tfrac1{52})$ there is $x_0$ such that for each scale $s$ with $s.\varepsilon = \varepsilon$ and $s.x \ge x_0$, each frame $\varphi$ with $s.x^{2+8\varepsilon} \le \mathrm{ord}(\varphi) \le 2 s.x^{2+8\varepsilon}$ and $o(\varphi) = o(\mathrm{Level.cyc}\,\psi)$, and each host datum $H_0$ on $\varphi$ with `KerChi ψ H0`, there are ranks $R$ on $\varphi$ with `RankVal s R` and `admitted R H0`.

`KerChi ψ H0` says that the conductor of $\psi$ divides $Q_S$ and that the map `art` of $H_0$ is $1$ at $a$ exactly when $a \equiv \pm 1 \pmod{2^{e+2}}$, $\psi(a) = 1$ and two Jacobi symbols are $1$. `RankVal s R` fixes the sizes of the ranks in terms of $s.x$.

**Theorem.** Then `HostExW (3/2) P` holds, with $P(s, R, H)$ the conjunction of `EAtH (Level.cyc ψ) H T s.x s.ε 4` and `VVle E t √(s.b)`.

`HostExW λ P` says: for each $\varepsilon \in (0, \tfrac1{52})$ there are constants, a threshold $x_0$ and a set of scales with a window $[Y, Y^\lambda]$ above each bound, such that each such scale with $s.x \ge x_0$ has ranks $R$, a host $H$ and a prime $q_0$ with `RankVal s R`, `HostGood` (a list of 14 conditions) and $P$. `EAtH` holds the explicit formula conditions, among them $\|c_\chi\| \le 4 \log x$ for $c_\chi$ = `logDerivativeAtOne χ`. `VVle E t B` is the bound on lengths `shaLen` of [the step VWin](/step/vwin-def/).

## Proof

The term is `supplyOfAdmOf hostOfField`, and `hostOfField` is `hostOfFieldOf shortNorm smallOne`. For fixed $\varepsilon$:

1. `fieldChi ψ` gives frames $\varphi$ of order $c \cdot 2^e$ and host data $H_0$ with `KerChi`.
2. `winPairs` uses `VWinAt ψ 401` to give windows of scale $\tfrac32$ in which each $x$ has a `WinDatum`: primes $(q, d)$, an exponent $e$ and the bound `VVle` with $\lfloor x^{400} \rfloor$.
3. `hAdm` gives the ranks $R$. `hostOfField` gives the host $H$ with `HostGood`.
4. `boundedTw` gives the bounds of `EAtH`. Since $R.t \le x^{400}$ by `eventually_rank_le_rpow_of_lt_one_div_fiftytwo`, monotonicity of `VVle` gives the bound with $t = R.t$.

The rest is bookkeeping.

## In the Lean code

The theorem is in [HostOfField.lean](lean:Development/AutomorphicArithmetic/CharacterBoxes/HostOfField.lean#L17), with `hostOfField` at [line 8](lean:Development/AutomorphicArithmetic/CharacterBoxes/HostOfField.lean#L8). `supplyOfAdmOf` is in [supplyOfAdmOf.lean](lean:Development/AutomorphicArithmetic/ShortNorms/supplyOfAdmOf.lean#L13), `hostOfFieldOf` in [hostOfFieldOf.lean](lean:Development/AutomorphicArithmetic/ShortNorms/hostOfFieldOf.lean#L159), and `shortNorm`, `smallOne` in [Primes.lean](lean:Development/AutomorphicArithmetic/ShortNorms/Primes.lean#L5).

`SmallOne` says: there is $A \ge 1$ such that for each $M \ge 2$ there is a prime $p \equiv 1 \pmod M$ with $p \le M^A$. Linnik's theorem on the least prime in a progression (Linnik, Mat. Sb. 1944) implies it. `ShortNorm` is a lower bound for the number of primes of the form $4p = A^2 + dB^2$ in short intervals. We have not opened the proofs of the two statements.

The hypothesis `admitted R H0` is always true by `admissible_ranks_of_CMDatum` ([AdmChi.lean](lean:Development/AutomorphicArithmetic/CoprimeRanks/AdmChi.lean#L11)). The constant $C_5$ of `HostGood` is fixed to $4$. `WinDatum` uses the exponent $400$, while `VWinAt` uses $401$.
