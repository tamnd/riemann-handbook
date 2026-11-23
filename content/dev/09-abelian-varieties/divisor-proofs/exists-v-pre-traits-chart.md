---
id: exists-v-pre-traits-chart
title: A raw Siegel Fourier system from a theta setup, with traits and a member
kind: theorem
decl: GlobalTheory.Poinc.Sep.exists_vPre_traits_chart
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsFourierTermSystemTraitsChartThetaModel
covers: 499
status: drafted
drafted_by: writer@claude
---
This theorem builds a raw Fourier system on a theta setup of level $l^{2j}$ over the compactification. One index carries the given monomial family, and the other indices are all the traits of $X$ that are regular at the chosen point. It is the proof of [the theta model statement](/entry/exists-fourier-term-system-traits-chart-theta-model/), which [the normalization step](/entry/exists-chart-member-traits-r/) uses. It is the Siegel form of [the unitary construction](/entry/exists-v-pre-traits-on-chart/). Below it are 499 declarations.

## Statement

The statement is that of [the theta model statement](/entry/exists-fourier-term-system-traits-chart-theta-model/). Let $N_1 = l^{2j}$ and let $A = \mathcal{O}_{M, z_1}$. `IsChartMemberP` is `IsChartMember` of [the normalization step](/entry/exists-chart-member-traits-r/) with `IsThetaTerms₀` in place of `IsThetaTerms`: the clause that one term at $\mu = 0$ equals $1$ is dropped. `Exact` says that each class sum modulo $N_1$ of the terms is the image of an element of $A$. `ClassSums` says that the class sums of deeper levels come from elements of the integral closure of $A$ in a finite Galois extension, on which the Galois group acts through linear maps of the lattice. [The unitary entry](/entry/exists-v-pre-traits-on-chart/) says this in more detail.

## Proof

1. `exists_thetaSetup_primePowerLevel_regular_chart` gives $j \geq j_0$, a theta setup $X_1$ with $r N = N_1$, a point $z_1$, a complete normal noetherian local domain $V_1$ with a finite injective $\rho \colon V \to V_1$, a local map $\mathrm{ev} \colon A \to V_1$ that is regular (`RegAt`) and agrees with $\xi$, and degeneration data $D_0$ over $V_1$ that refine $Q$.
2. `stalk_isNoetherian_normal_fractionRing` shows that $A$ is a domain. `exists_eighthPowerMatrixAction_thetaCompactification` gives an action of $8 \times 8$ integral matrices (`IsAct`). The theta divisor gives a label $x_0$ through $z_1$.
3. `UnifOver` for $\xi$, at $(V_1, \rho, D_0)$, gives a semi-abelian scheme over $V_1$. Then `exists_uniformised_member_of_refined_uniformisation` gives a uniformized member $\mathfrak{m}_0$ (`UMem`) over $V_1$ with `SharpRef`. As $\rho$ is finite and injective, it is local.
4. For each trait $T$ with a local regular map $A \to T$ over the point of $X$, `nonempty_uMem_trait` (same file) gives a member over $T$ with $t = \varpi$ and $\delta = \beta$. It uses `siegelModuliTrait_periods_monomial_posDef`, which also gives the rank bound once $\zeta_n$ is a unit.
5. The index set is `Option Tr`. The index `none` carries $(V_1, X_Q, \rho \circ t, \delta)$, and `some T` carries $(T, X_T, \varpi, \beta)$. `exists_member_terms_integral_unit_shift` gives the coefficients $u$, with a unit for each $\mu$ and $u(0, c)$ a unit when $c$ is the label $x_0$. The labels are the set `HH` of $X_1$ at $z_1$.
6. `HasTraitsR` takes the index `some T` with the identity map. `IsChartMemberP` takes $D = D(\mathfrak{m}_0)$, and `memberTerms_isThetaTerms_torsionFrames` gives the theta terms. Only `none` can have $m \neq 1$.
7. The members make $\Phi$ geometric (`IsGeo`). Then `thetaSystem_classSums_values_of_functions` gives `Exact`, and `uniformisedMembers_classSums_deeper_levels` gives `ClassSums`.

## In the Lean code

The theorem is in [ExistsFourierTermSystemTraitsChartThetaModel.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsFourierTermSystemTraitsChartThetaModel.lean#L39), and `nonempty_uMem_trait` at [L22](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsFourierTermSystemTraitsChartThetaModel.lean#L22). `UMem`, `IsAct` and `IsGeo` are in [IsActIffIsDiagEnd.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsActIffIsDiagEnd.lean#L67). `IsThetaTerms₀`, `RegAt`, `Exact` and `ClassSums` are in [IsChartMemberP.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsChartMemberP.lean#L102).

`Tr` is a sigma type over all traits, so $Y$ lives in `Type 1`. The isomorphisms $e$ and $h$ of the member are identities. Unlike the unitary case, no square roots are adjoined. We have not unfolded `Setup`, `UMem.Terms`, `IsCoef` or `Refines`, so "theta setup" and "uniformized member" follow the names.
