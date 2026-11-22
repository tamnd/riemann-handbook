---
id: host-of-field-of
title: A good host from host axioms, given short norms and small primes
kind: theorem
decl: UpperTheory.T3.hostOfFieldOf
module: Development.AutomorphicArithmetic.ShortNorms.hostOfFieldOf
covers: 552
status: drafted
drafted_by: writer@claude
---
This theorem completes host axioms $H_0$ on a frame to a host $H$ that meets all conditions of `HostGood`. [`hostOfField`](/entry/host-of-field/) proves its two hypotheses on primes and so gives the builder that [`supplyOfAdmOf`](/entry/supply-of-adm-of/) needs. Through [`supplyOfAdm`](/entry/supply-of-adm/), the hosts go to the step [ZeroFreeAll from Green, VWin and HypsAlt](/step/zero-free-all-of-green-v-win/).

## Statement

`SmallOne` says: there is $A \ge 1$ such that for each $M \ge 2$ there is a prime $p \equiv 1 \pmod M$ with $p \le M^A$. `ShortNorm` is a lower bound for the number of primes of the form $4p = A^2 + dB^2$ in an interval $[X, X(1+h)]$, for $d \equiv 3 \pmod 4$ prime. Both are as in [`supplyOfAdm`](/entry/supply-of-adm/).

**Theorem.** Assume `ShortNorm` and `SmallOne`. Then statement (B) of [`supplyOfAdmOf`](/entry/supply-of-adm-of/) holds. So host axioms that meet the hypotheses of (B) extend to a host $H$ with a prime $q_0$, `HostGood s C8 4 c6 Cb H q0` and `Shares`.

## Proof

The proof chooses the extra data of $H$ and checks `HostGood` in groups. Let $N = Q_S\, q\, d$, the conductor of $H_0$.

1. **Level primes.** `levelData` gives two primes $g_0 \ne g_1$ of size about $(k\, b)^8$ that are norms $\pi \bar\pi$ with $\pi \equiv 1 \pmod N$, two primes $p, p' \equiv 1 \pmod{15N}$ and a prime $q_0 \equiv 1 \pmod N$, all at most $N^{C_8}$. `split_of_one_mod` and `ncard_placesOver` give how they split in the field $E$ of the host.
2. **The second set.** `hof_thick`, from `thickFrame2`, gives a set $T_2$ with `NoRel`, of size between $x^{-\varepsilon} n(R)$ and $n_0/(4 L_w)$.
3. **The host.** `hof_exists_host` applies `admitted R H0` to these choices and gets a host $D$ over $H_0$.
4. **The pair.** `qdBig` and `pairRows` give that $q$ and $d$ exceed $4tr + 1$, the bounds `QDq` with constant $4$, `Boxq`, and $\log N \le 2 x^{\varepsilon/5} \log^2 x$.
5. **Bad set and shares.** `topsChoiceH` gives the set $TT$ with `BadOK` and `Shares`. $H$ is $D$ with this $TT$.
6. **Analytic conditions.** `hof_box`, from `realBox`, gives `BoxW` and `RealBox`. Then [`QH.thinH`](/entry/thin-h/), with $B = C_0$, gives `ThinOK` through `thinScales_iff_hostBound`. From `QDq`, $|\mathrm{dlogH}(H)| \le 4 \log x \le x^{\varepsilon}$.

## In the Lean code

The theorem is in [hostOfFieldOf.lean](lean:Development/AutomorphicArithmetic/ShortNorms/hostOfFieldOf.lean#L159). It also calls `normOne_iff_host`.

In `hof_exists_host` the ideal `ccK` of the choices is the unit ideal $\top$. So `ccK_split`, which is about prime ideals that contain $\top$, holds vacuously. The set `TT` is first empty and is replaced in step 5. The constant $C_5 = 4$ comes from `pairRows`. We have not unfolded `HostVal`, `BadOK` or `PairRow`.
