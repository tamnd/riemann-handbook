---
id: sep-b-of-norm-bl
title: Separation on the normalized blowup of an integral compactification
kind: theorem
decl: GlobalTheory.USep.sepB_of_normBl
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.SeparationNormalizedBlowupUnitaryCompactificatio
covers: 533
status: drafted
drafted_by: writer@claude
---
This theorem proves `SepB` for a normalized blowup of an integral compactification along a boundary ideal. It is the proof of [the separation statement](/entry/separation-normalized-blowup-unitary-compactification/), which step 6 of [the normalized blowup with separation](/entry/u-poin-st-x-sep/) cites. The chain leads to [the toroidal compactification theorem](/entry/toroidal-for-fan-ks/) and [the literature step](/step/every-character-of-literature/). Below this theorem are 533 declarations.

## Statement

Take $E$, $H$, a datum of signature $(p, q)$ with $p + q \geq 1$, $\varphi$ with `IsPolFan` and `NoSelfInt`, the moduli scheme $X$ and the field $F$, as in [the parent entry](/entry/u-poin-st-x-sep/). Let $Z_o$ be an integral compactification (`UCompact`) over a Dedekind domain $o$ with fraction field $F$, with generic fibre $Z_F$ and open immersion $i \colon X_F \to Z_F$. Let $d \geq 1$, and let $J$ be an ideal sheaf on $Z_o$ whose support misses $i(X_F)$ and whose valuations are those of $d\varphi$ (`UValOn`).

**Theorem.** Let $\pi \colon S \to Z_F$ be a proper normalized blowup of $J\mathcal{O}_{Z_F}$ (`IsNormBl`). Let $j \colon X_F \to S$ be an open immersion with $\pi \circ j = i$ and $\pi^{-1}(i(X_F)) = j(X_F)$. Then $j$ satisfies `SepB`.

`SepB` is stated in [the parent entry](/entry/u-poin-st-x-sep/). For each input $(V, s, \varepsilon, \mathrm{ev} \colon V \to K, k_0)$ it asks for `SepAtB`: (a) $\mathrm{ev}(s_1), \dots, \mathrm{ev}(s_m)$ are $0$; (b) the abelian part of the degeneration data descends to $k_0$ (`DescAt`); (c) if the data come from a base ring that maps into $k_0$ (`FromBase`), then $\mathrm{ev}(s_{m+1}), \dots, \mathrm{ev}(s_{m+N})$ lie in $k_0$.

## Proof

1. `abelianPart_descends_of_thetaTerms_ratios`, for the genus of the family and $n = 3$, gives a bound $j_0$.
2. [The Fourier system with a member](/entry/exists-unitary-fourier-system-traits-family/), with $n = 3$, gives $j \geq j_0$, a system $\Phi$ of level $N_1 = 9^j$ on a finite normal cover of $Z_o$, and a member $y$ with theta terms and $t_k^2 = \rho(s_{h(k)})$ for a finite injective $\rho \colon V \to V_y$.
3. `exists_approximating_elements_normalCover_unitary` extends $\mathrm{ev}$ to $\mathrm{ev}_1 \colon V_y \to K$ with $\mathrm{ev}_1 \circ \rho = \mathrm{ev}$, and proves `Elements` with degree $2d$. It uses $J$, $d$, `UValOn` and the blowup.
4. `exists_hasSupports` and `exists_supportingTuple_smoothCone_cmField` give a support degree $d_0$. Then `poincareApprox_values_at_point_of_elements` proves `Values`: $\mathrm{ev}_1(t_k) = 0$; ratios $u(\mu, c)/u(\mu, c')$ lie in $k_0$; and for each linear form $\lambda$ that kills every $\delta_k$, two unit coefficients have exponents that differ by $M\lambda$ and a ratio in $k_0$. This is the only step that uses `NoSelfInt`.
5. Part (a): $\mathrm{ev}(s_{h(k)}) = \mathrm{ev}_1(t_k)^2 = 0$.
6. Part (b): step 1 gives `DescAt` over $V_y$ from the theta terms and the ratios of step 4. `descendsAbelianPart_of_isPullDeg` moves it back to $V$ along $\rho$.
7. Part (c): fix $i$. `periodsInCoordinates_fromBase_pullDeg` moves `FromBase` to $V_y$. Then `thetaTerm_coefficient_sq_eq_monomial_subfield` gives $\mathrm{ev}_1(u)^2 = r \prod_k \mathrm{ev}(s_{m+k})^{M'\varepsilon_{m+k}(\mu, \mu)}$ with $r \in k_0$. A Smith normal form (`exists_extend_smul`) gives $n \neq 0$ and a linear form $\lambda$ on all bilinear forms that is $n$ times the $(m+i)$-th coordinate on balanced forms. It kills the $\delta_k$. Step 4 for $\lambda$ gives $\mathrm{ev}(s_{m+i})^{M' M n} \in k_0$. As $k_0$ is algebraically closed, $\mathrm{ev}(s_{m+i}) \in k_0$ (`mem_of_zpow_mem`).

## In the Lean code

The theorem is in [SeparationNormalizedBlowupUnitaryCompactificatio.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SeparationNormalizedBlowupUnitaryCompactificatio.lean#L97). The helpers `mem_of_zpow_mem`, `exists_extend_smul` and `zpow_sum_units` are in the same file. `SepB` and `SepAtB` are in [FromBaseAlt.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/FromBaseAlt.lean#L35). `Elements` and `Values` are in [IsChartMember.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsChartMember.lean#L66).

Three hypotheses are never used: properness of $\pi$, the open immersion property of $j$, and $\pi^{-1}(i(X_F)) = j(X_F)$. The construction of $d_0$ repeats `exists_hasSupports_cm` in [ExistsUnitaryApproxPoincareSeries.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsUnitaryApproxPoincareSeries.lean#L88). The module name is cut short: it ends in "Compactificatio". We have not unfolded `DegPre`, `IsPullDeg`, `Dominant` or `HasSupports`.
