---
id: thin-h
title: The thin bound for the characters of a host
kind: theorem
decl: QH.thinH
module: Development.AutomorphicArithmetic.MeanSquareBounds.GaussSumFunctionEq
covers: 373
status: drafted
drafted_by: writer@claude
---
This theorem proves `ThinH`: a bound $|g_\chi(y)| \le y\, e^{-c x^{\varepsilon/8}}$ for large $y$ and each primitive character $\chi$ of a host. It is an adapter. It puts the host data into the form of [`thin`](/entry/thin/), which has the analytic content, and checks the hypothesis on real zeros. Its only user is [`hostOfFieldOf`](/entry/host-of-field-of/), where it gives the condition `ThinOK` of `HostGood`.

## Statement

For a [[Dirichlet character|JR4QSEFXWF]] $\chi \ne 1$, $g_\chi$ is as in [`pairEx`](/entry/pair-ex/). A host $H$ has primes $q$, $d$, a modulus $Q_S$ and conductor $N_H = Q_S\, q\, d$. A character $\chi$ is a character of $H$ (`IsCharE`) if it is the primitive character that induces one of the characters of $(\mathbb{Z}/N_H)^\times$ that $H$ defines. `RealBox H` says: if $\chi$ is a real character of $H$ and $q$ or $d$ divides its conductor, then $L(\beta, \chi) \ne 0$ for real $\beta > 1 - \tfrac1{400}$.

**Theorem.** There is $c > 0$ such that for all $B$ and $\varepsilon \in (0, \tfrac1{52})$ there is $x_0$ with this property. Let $x \ge x_0$ and let $H$ be a host with odd part of $Q_S$ at most $B$, $\log N_H \le 2 x^{\varepsilon/5} \log^2 x$ and `RealBox H`. Then $|g_\chi(y)| \le y\, e^{-c\, x^{\varepsilon/8}}$ for each character $\chi$ of $H$ and each $y \ge e^{x^{\varepsilon/3}}/3$.

## Proof

Take $c = 1$. `small_zeros` gives $c_0 > 0$ such that no nontrivial character of level at most $8\lfloor B \rfloor$ has a real zero in $(1 - c_0, 1)$. Apply [`thin`](/entry/thin/) with $A = 2$ and $\min(c_0, \tfrac1{400})$. The level $N$ of $\chi$ divides $N_H$ (`level_dvd`), which gives the bound on $\log N$. For a real $\chi \ne 1$, the zero-free interval comes from `RealBox H` if $q$ or $d$ divides $N$. If not, `real_cond` gives $N \mid 8 Q_S' q d$, with $Q_S'$ the odd part of $Q_S$, so $N \le 8\lfloor B \rfloor$ and `small_zeros` applies.

## In the Lean code

The theorem is in [GaussSumFunctionEq.lean](lean:Development/AutomorphicArithmetic/MeanSquareBounds/GaussSumFunctionEq.lean#L55). `ThinH` and `RealBox` are in [PairGood.lean](lean:Development/AutomorphicArithmetic/CharacterBoxes/PairGood.lean#L32). It calls `thin`, `small_zeros`, `real_cond` and the private `gauss_sum_function_eq`, `level_dvd` and `isReal_of_sq`.

The module name and `gauss_sum_function_eq` are misleading: no Gauss sum appears. That lemma only says that `An.gChi`, with weight $\max(y/n - 1, 0)$, equals `G0`, with weight $y/n - 1$, since $n \le y$ in the sum. `small_zeros` is an induction on the level bound with `noExc_level`, which we have not opened.
