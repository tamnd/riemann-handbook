---
id: aprime-inf-holds
title: The archimedean disintegration constant in closed form
kind: theorem
decl: Formalism.L2.SG.Closed.AprimeInf_holds
module: Formalism.LocalToGlobal.SiegelLatticeTheory.ClosedVolumeStatements.RealBracketHolds
covers: 990
status: drafted
drafted_by: writer@claude
---
This theorem proves `AprimeInf`: a constant $a'$ that disintegrates the Haar measure of $G_\infty$ along the orbit of a frame has an explicit value. It is the third input of [`RealBracket_holds`](/entry/real-bracket-holds/). The proof is one line. It applies [`aprime_infinite_real`](/entry/aprime-infinite-real/) to the compactness statement `hinfCompact_holds` and to the instance `GaugeVolUD`. The content is below `aprime_infinite_real`.

## Statement

**The gauge constant.** For signs $\varepsilon \in \{\pm 1\}^n$ let $J_\varepsilon$ be the diagonal matrix of the signs, $U(J_\varepsilon) = \{g : g^* J_\varepsilon g = J_\varepsilon\}$, and $\mu$ the Haar measure of Mathlib on it. Let $B_\rho$ be the ball of radius $\rho$ in its Lie algebra, with the Euclidean norm of the real and imaginary parts of the entries. The gauge constant is
$$\mathrm{g}(\varepsilon) = \lim_{\rho \to 0^+} \frac{\mu(\exp B_\rho)}{\operatorname{vol}(B_\rho)},$$
and `GaugeDens` $\varepsilon$ says that this limit exists and is positive. So $\mu / \mathrm{g}(\varepsilon)$ is the Haar measure with density $1$ at the identity in exponential coordinates. For a setting $X$, $g_U = \prod_{v \mid \infty} \mathrm{g}(\varepsilon_v)$.

**The instance.** `GaugeVolUD` says: for each $k$, `GaugeDens` holds for the compact group $U(k)$ (all signs $+$), and $\mu / \mathrm{g}$ gives $U(k)$ the total mass $V_k = \prod_{i=1}^{k} (2\pi)^i / (i-1)!$.

**Theorem.** Assume `GaugeVolUD`. Let $X$ be a setting with $d$ infinite places, $u, u'$ words, and $\psi$ a character, with `HypX`, `MeasCompatψ` and `IsStdChar ψ`, and with `GaugeDens` $\varepsilon_v$ at each infinite place $v$. Let $a' > 0$ satisfy the disintegration clause `AinfClause` at infinity for the frame of $u'$ (stated in [`RealBracket_holds`](/entry/real-bracket-holds/)). Then
$$a' = \frac{g_U\, V_k^{\,d}\, T_{u'}^{-kd}}{\mu_H(u')(\mathrm{all})},$$
where $\mu_H(u')$ is the measure `X.muH u'` on the stabilizer at infinity of the frame of $u'$.

## Proof

`aprime_infinite_real` proves `AprimeInf` from two inputs:

1. `HinfCompact`: for each setting and each word $u$, the stabilizer in $G(F_\infty)$ of the frame of $u$ is compact. It is `MassDataX.hinfCompact_holds`, proved from `hinfCompact_of` and four lemmas; we have not unfolded them.
2. `GaugeVolUD`, from the instance.

## In the Lean code

The theorem is in [RealBracketHolds.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedVolumeStatements/RealBracketHolds.lean#L12). `AprimeInf` is in [NcRealPf.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/NcRealPf.lean#L109), `GaugeDens` and the gauge constant in [SGauge.lean](lean:Formalism/SharpRestriction/CuspSpanNormBounds/SGauge.lean#L22), and `GaugeVolUD` in [BlockGrp.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ArchimedeanOrbitMeasures/BlockGrp.lean#L207).

`GaugeVolUD` is an instance argument here, not an open hypothesis. It is proved as `GV.gaugeVolU` in [JacConstGVol.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/JacConstGVol.lean#L489) and declared as the instance `factGaugeVol` in [FactsGV.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/WeightedGaugeFactors/FactsGV.lean#L6). Its first half, `GaugeDens` for $U(k)$, is also a case of `gauge_density_exists`, which proves `GaugeDens` for all signs.

The hypothesis "`GaugeDens` $\varepsilon_v$ at each $v$" of `AprimeInf` is always true by `gauge_density_exists`. [`RealBracket_holds`](/entry/real-bracket-holds/) supplies it that way. The data $u$, $\mathcal F_N$, $\mathcal F_N'$ enter `AprimeInf` only through `HypX`; the conclusion does not mention them.
