---
id: real-bracket-holds
title: The archimedean bracket from the reference covolume
kind: theorem
decl: Formalism.L2.SG.Closed.RealBracket_holds
module: Formalism.LocalToGlobal.SiegelLatticeTheory.ClosedVolumeStatements.RealBracketHolds
covers: 1653
status: drafted
drafted_by: writer@claude
---
This theorem proves `RealBracket`, an identity between volumes at the infinite places of a totally real field $F$. It has one hypothesis, `CovolRef`. The theorem [`ncTieC_of_closed`](/entry/nc-tie-c-of-closed/) uses it to replace the hypothesis `RealBracket` of [`ncTie0All_of`](/entry/nc-tie0-all-of/). The proof only puts four results together. The work is in the files that it calls.

## Statement

Let $X$ be a setting with a CM extension $E/F$, let $d$ be the number of infinite places of $F$, and let $r$, $k$ be the ranks `D.R.rS` and `D.R.k`. For words $u, u'$ there are measures $\mu_H(u)$ and $\mu_N(u)$ on groups at infinity, and positive reals $T_u$, $T_{u'}$. Put $e = -(8r^3 + 6r^2 + 6kr^2 + r)/3$.

**Theorem.** Assume `CovolRef`: for all $X$, $u$, $u'$ and fundamental domains $\mathcal F_N, \mathcal F_N'$ with `HypX`, the product of the reference volumes of $\mathcal F_N$ and $\mathcal F_N'$ is $\lvert d_F \rvert^{e}$. Assume also the two instances `GaugeVolUD` and `RhsWLim`. Then `RealBracket` holds. That is, under `HypX`, `MeasCompatψ` and `IsStdChar ψ`, for every $a' > 0$ that satisfies the disintegration clause `AinfClause` at infinity,
$$c_X(u,u')\, \mu_H(u)(\mathrm{all})\, \mu_N(u)(\mathcal F_N)\, \mu_N(u')(\mathcal F_N') = a'\, 2^{kd} \Big(\frac{\pi^k}{(k-1)!}\Big)^{d} T_u^{-kd}\, \lvert d_F \rvert^{e}.$$
Here $c_X(u,u')$ is `DisintegrationConstant X u u' 1`.

The clause `AinfClause` says that $\int f\, d\mu_{G_\infty} = a' \int\int f(s(y) h')\, d\mu_{H_\infty}\, d\nu(y)$ for every measurable $f$ and every section $s$ of the orbit map of the frame of $u'$. Here $\nu$ is the fibre measure over the Gram matrix of that frame.

## Proof

The proof is `realBracket_of_jac` applied to four inputs:

1. `JacGauge_holds`, a disintegration statement with an explicit Jacobian constant. It is a renaming of `Formalism.L2.SG.Pf.jacGauge`, which uses the instance `RhsWLim`.
2. The hypothesis `CovolRef`.
3. `AprimeInf_holds`. It says that $a' = g_U \cdot V_k^{d} \cdot T_{u'}^{-kd} / \mu_H(u')(\mathrm{all})$, where $g_U$ is a gauge constant and $V_k = \prod_{i<k} (2\pi)^{i+1}/i!$. It comes from `aprime_infinite_real` with `hinfCompact_holds` and the instance `GaugeVolUD`.
4. `gauge_density_exists`: the gauge density statement `GaugeDens` for every sign vector.

In [NcRealXPS.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/NcRealXPS.lean#L265), `realBracket_of_jac` first turns `JacGauge` and `CovolRef` into `PlaceSplit`. This writes each measure as a product over the infinite places. It also gives a local disintegration constant at each place. Then `realBracket_of` in [NcRealPf.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/NcRealPf.lean#L159) multiplies the local constants, uses `ProdExact_holds` and `AprimeInf`, and finishes with algebra. The key step is $V_k = V_{k-1}\,(2\pi)^k/(k-1)!$.

We have not unfolded `JacGauge`, `GaugeDens` or the proofs of `aprime_infinite_real` and `ProdExact_holds`.

## In the Lean code

The theorem is in [RealBracketHolds.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedVolumeStatements/RealBracketHolds.lean#L20). `RealBracket` and `eDF` are in [NcReal.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/NcReal.lean#L35), and `CovolRef` is at [NcRealXPS.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/NcRealXPS.lean#L169).

`DisintegrationConstant` is defined by choice: it is a constant $C > 0$ with the disintegration property, and $0$ if no such constant exists. In `CovolRef`, both volumes use the reference measure `refNX X u` of the word $u$, also for $\mathcal F_N'$. The proof of `placeSplit_of` uses `refNX X u` for $u'$ too, so this is consistent.
