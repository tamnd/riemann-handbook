---
id: sep-st
title: Separation at the centre of a chart on the Siegel blowup
kind: theorem
decl: GlobalTheory.Poinc.Sep.sepSt
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ChartSeparationDataDefinedOverCentreField
covers: 797
status: drafted
drafted_by: writer@claude
---
This theorem proves $\mathrm{SepSt}$: if a geometric point at the centre of a monomial family on the normalized Siegel blowup is defined over a subfield $k_0$, then the family is defined over $k_0$ there. It is the proof of [the statement entry](/entry/chart-separation-data-defined-over-centre-field/), which [the smooth blowup with pre-charts](/entry/chart-st5-holds/) uses. Below it are 797 declarations.

## Statement

Let $g$, $n$, $\Lambda_n$, $\mathcal{A}$ over $X$, $\varphi$ and $i \colon X \to Z$ be as in [the parent theorem](/entry/chart-st5-holds/), with `IsThetaCompact` for $i$. Let $J$ be an ideal sheaf on $Z$ off $i(X)$ with `ValOn` for $\varphi$ and $d \geq 1$, $\pi \colon \overline{S} \to Z$ a normalized blowup of $J$, and $j \colon X \to \overline{S}$ with $\pi \circ j = i$. The input is:

- a local domain $V$ with degeneration data $Q$ whose lattice $X_Q$ has rank at most $g$ (`Data`: an abelian scheme $B$ with an ample line bundle, points $c(a)$ and trivializations $\tau(a, b)$), and $\xi \colon \operatorname{Spec} V \to \overline{S}$ with `UnifOver`: over each finite extension of $V$ that refines $Q$, the data uniformize a semi-abelian scheme whose generic fibre maps to $\mathcal{A}$ through $j$;
- nonzero $s_1, \dots, s_m$ in the maximal ideal, units $s_{m+1}, \dots, s_{m+N}$, and a basis $\varepsilon$ of the symmetric forms on $X_Q$, with $\varepsilon_1, \dots, \varepsilon_m$ in a cone of $\varphi$ and together positive definite, and $\tau(a, b) = \prod_i s_i^{n\varepsilon_i(a, b)} \tau_0(a, b)$ (`TauIn`);
- $\mathrm{ev} \colon V \to K$, $K$ algebraically closed, whose point of $\overline{S}$ is $\xi$ of the closed point, defined over an algebraically closed subfield $k_0$.

**Theorem.** Then (`SepAt`): (a) $\mathrm{ev}(s_k) = 0$ for $k \leq m$; (b) for each Siegel family $\mathcal{A}'$ and each map that pulls it back to $B$ with its line bundle, if the base point is defined over $k_0$, then so are the points $c(a)$; (c) if $Q$ comes from a ring $W_0$ that $\mathrm{ev}$ maps into $k_0$ (`FromBase`), then each $\mathrm{ev}(s_i)$ lies in $k_0$.

## Proof

1. `monoTau_inl` drops the units and makes $Q$ monomial in $t_k = s_k$ with forms $\delta_k = n\varepsilon_k$, $k \leq m$.
2. Let $l$ be the least prime factor of $n$. `torsion_theta_values_abelianPart_defined_over` and `eighthPower_thetaCoefficient_eq_const_mul_monomial` give bounds $j_1, j_2$.
3. [The Fourier system with a chart member](/entry/exists-fourier-term-system-regular-traits-given-chart/) gives $j \geq \max(j_1, j_2, 1)$, a Fourier system $\Phi$ of level $l^{2j}$ and a member $y$ with a finite injective $\rho \colon V \to V_y$.
4. `exists_stalk_elements_approx_leadingTerm_quotients` extends $\mathrm{ev}$ to $\mathrm{ev}_1 \colon V_y \to K$ and proves `Elements`.
5. `poincareApprox_values_at_point_of_elements` proves `Values`. This is the only use of `NoSelfInt`.
6. Part (a) is the first clause of `Values`. Part (b) is the bound $j_1$ applied to the theta terms and the ratio clause of `Values`.
7. Part (c), for $s_{m+k}$: the bound $j_2$ gives $\mathrm{ev}_1(u(\mu, c)) = r \prod_{k'} \mathrm{ev}(s_{m+k'})^{q_W(n\varepsilon_{m+k'})(\mu)}$ with $r \in k_0$. `exists_ext_functional` gives a linear form $\lambda$, a positive multiple of the $(m+k)$-th coordinate, that kills each $\delta_{y,k}$. The last clause of `Values` gives two unit products of coefficients with ratio in $k_0$ and exponents that differ by $M\lambda$. So $\mathrm{ev}(s_{m+k})^{Mnc_0} \in k_0$ (`mem_of_ratio`), and $\mathrm{ev}(s_{m+k}) \in k_0$ as $k_0$ is algebraically closed.

## In the Lean code

The theorem is in [ChartSeparationDataDefinedOverCentreField.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ChartSeparationDataDefinedOverCentreField.lean#L143). The helpers are in the namespace `Assembly` of the same file. `SepSt`, `SepAt`, `FromBase`, `TauIn` and `UnifOver` are in [FromBase.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/FromBase.lean#L58), and `Elements` and `Values` in [IsChartMember.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsChartMember.lean#L66).

Unlike [the unitary proof](/entry/sep-b-of-norm-bl/), the member has no square roots, and the level is a power of the least prime factor of $n$, not of $3$. We have not unfolded `IsMonomialTau`, `ThetaInt`, `Unif` or `Refines`.
