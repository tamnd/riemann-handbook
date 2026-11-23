---
id: aprime-inf-of-hinf-compact
title: The archimedean orbit constant, from compact stabilizers and the gauge volumes
kind: theorem
decl: PI.AprimeInfAsm.aprimeInf_of_hinfCompact
module: Formalism.PeriodIntegrals.OrbitalBoundsConclusion.AprimeInf
covers: 986
status: drafted
drafted_by: writer@claude
---
This theorem proves `AprimeInf`, the value of the constant $a'$ in the disintegration of the Haar measure of the real unitary group along the orbit of a frame. It has two hypotheses: the stabilizers at infinity are compact, and the gauge volumes of the compact unitary groups are known. The theorem [`aprime_infinite_real`](/entry/aprime-infinite-real/) has the same statement and only calls this one. Its caller, [`AprimeInf_holds`](/entry/aprime-inf-holds/), supplies both hypotheses, and the result goes to [`RealBracket_holds`](/entry/real-bracket-holds/). The proof only assembles proved lemmas around [`aprimeInf_of_grp`](/entry/aprime-inf-of-grp/).

## Statement

Let $X$ be a setting (`HidaSetting`) with a CM extension $E/F$, a Hermitian matrix $J$ of size $n$, and the group $G_\infty$ of $J$ over $F \otimes \mathbb R$. Let $d$ be the number of infinite places of $F$ and $k$ the integer `D.R.k`. For a word $u$, let $H_\infty(u) \subset G_\infty$ be the stabilizer of the frame of $u$, a tuple of $2r+1$ vectors.

- `HinfCompact`: for every $X$ and $u$, the group $H_\infty(u)$ is compact.
- `GaugeVolUD`: for every $k$, the compact group $U(k)$ satisfies `GaugeDens` (the ratio $\mu_G(\exp B_\rho)/\operatorname{vol}(B_\rho)$ has a positive limit $g_U$ as $\rho \to 0^+$), and the measure $\mu_G/g_U$ gives $U(k)$ the total mass $V_k = \prod_{i<k} (2\pi)^{i+1}/i!$.

**Theorem.** Under these two hypotheses, `AprimeInf` holds. That is, let $u, u'$ be words and $\psi$ a character of $\mathbb A_F$ with `HypX`, `MeasCompatψ` and `IsStdChar ψ`, and suppose `GaugeDens` holds at each infinite place. Let $a' > 0$ satisfy `AinfClause`: self-dual measures on tuples and on Hermitian matrices at infinity exist, and for every such choice and every fibre family over the Gram map,
$$\int_{G_\infty} f \, d\mu_G = a' \int_y \int_{H_\infty(u')} f(s(y)h)\, d\mu_H(h)\, d\mathrm{fib}(y)$$
for all measurable $f \geq 0$ and all sections $s$ of the orbit map. Then
$$a' = g_U \, V_k^{\,d} \, T_{u'}^{-kd} \big/ \mu_H(u')\bigl(H_\infty(u')\bigr),$$
where $g_U$ is the product of the gauge constants over the infinite places and $T_{u'}$ is the integer `Tw u'`. We have not unfolded `HypX`, `MeasCompatψ` or `IsStdChar`.

## Proof

The proof is one line:

```
aprimeInf_of_grp hC (grpStd_full expProdU_holds hV) nuBridge placeJacAll_holds
```

`grpStd_full` turns `GaugeVolUD` and `ExpProdU` into `GrpStd`, the limit of Haar volumes of small tubes. `ExpProdU` is proved by `expProdU_holds`. `NuBridge` and `PlaceJacAll` are proved by `nuBridge` and `placeJacAll_holds`. The rest is in [`aprimeInf_of_grp`](/entry/aprime-inf-of-grp/).

## In the Lean code

The theorem is in [AprimeInf.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/AprimeInf.lean#L10). `AprimeInf` is in [NcRealPf.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/NcRealPf.lean#L109), `AinfClause` in [NcReal.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/NcReal.lean#L15), `HinfCompact` in [StrongApproxN.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/MassComputations/StrongApproxN.lean#L32) and `GaugeVolUD` in [BlockGrp.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ArchimedeanOrbitMeasures/BlockGrp.lean#L207).

`aprime_infinite_real`, at line 13 of the same file, is a second name with the same statement. Both hypotheses are proved in the code: `HinfCompact` by `hinfCompact_holds`, and `GaugeVolUD` by `gaugeVolU`, through the instance `factGaugeVol`. The caller takes `GaugeVolUD` as a `Fact` instance.

[Assembly.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ArchimedeanOrbitMeasures/Assembly.lean#L51) has a parallel route, `aprimeInf_of_open`, which takes `CayValId` as a hypothesis instead of the proved `cayValId_holds`.
