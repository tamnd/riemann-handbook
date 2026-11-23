---
id: antisymmetry
title: The sign change of the height defect
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.PB.Top.antisymmetry
module: Development.AutomorphicSpectrum.Proofs.MetricProofs.Antisymmetry
covers: 623
status: drafted
drafted_by: writer@claude
---
This theorem proves $\mathrm{Antisymmetry}$: the limit height polynomial of a realization, minus its volume times the height polynomial of the flag variety, changes sign under each block simple swap. It compares the realization with the flag variety itself, through the swap relation of [the adjacent swap relation](/entry/adjacent-swap-height-polynomial-relation/). The result goes up through [the statement form](/entry/antisymmetry-prime/) to [the swap relation from seven statements](/entry/good-tower-antisymmetry-of/).

## Statement

Fix a finite nonempty set $\Psi$ and $N \geq 2$, and let $R = \mathbb{R}[X_p : p \in \Psi \times \{0, \dots, N-1\}]$. For a weight $\lambda$ put $\mathrm{gap}_\lambda(\tau, i) = \lambda_{\tau,i} - \lambda_{\tau,i+1}$, and $\mathrm{gap}_\lambda(\tau, N-1) = \lambda_{\tau,N-1}$. For $Q \in R$ let $Q^{\mathrm{wt}}(\lambda) = Q(\mathrm{gap}_\lambda)$ (the map `toWt`).

Let $S$ be an analytic system of dimension $d + 1$ with potentials $\theta_p$, and $\mathrm{Re}$ a realization of $S$ with Hermitian lines $\bar L_{p,t}$ for $t > 0$ and degree $\deg$. For an intersection system $I$, the limit height polynomial is

$$\mathrm{PB} = \sum_{w} \lim_{t \to 0^+} \frac{I(\bar L_{w_1,t}, \dots, \bar L_{w_{d+2},t})}{\deg}\, X_{w_1} \cdots X_{w_{d+2}},$$

the sum over all $w \colon \{1, \dots, d+2\} \to \Psi \times \{0, \dots, N-1\}$. The degree polynomial $\deg_S$ has the mixed integrals of the $\theta_p$ as coefficients. Let $h$ be the polynomial built in the same way from the lines of the flag variety (`hFlPoly`), and $\mathrm{vol}(S) = \deg_S^{\mathrm{wt}}(\rho) / \deg_{\mathrm{Fl}}(\rho)$ with $\rho_{\tau,i} = -i$.

A flag system for $j$ (`FlagSys`) asks: $j \leq N$, $d + 1 = |\Psi|\binom{N}{2}$, $S$ is uniformised (near each point the potentials come from a period map to the flag variety, which is an immersion at one point), and each adjacent pair $(\tau, a)$, $b = a + 1$ with $b < j$ or $j \leq a$, has a square system with the coefficients $\xi_{\tau,a}$.

**Theorem.** Assume `Inputs`. Let $I$ be a full intersection system, and let $\mathrm{Re}$ have a flag system for $j$. Then $\delta = \mathrm{PB}^{\mathrm{wt}} - \mathrm{vol}(S)\, h$ is homogeneous of degree $|\Psi|\binom{N}{2} + 1$, and $\delta(\lambda \circ s) = -\delta(\lambda)$ for each swap $s$ of $(\tau, a)$ and $(\tau, a+1)$ as above.

## Proof

1. `flag_variety_analytic_system_exists` gives a reference system $S_0$ with a realization $\mathrm{Re}_0$ on the flag variety, of degree $1$, with constant lines and a flag system for $N$. Then $d = d_0$.
2. `flLines_polys` and `realisation_potential_degree_compatibility` give $\mathrm{PB}(\mathrm{Re}_0)^{\mathrm{wt}} = h$ and $\deg_{S_0}^{\mathrm{wt}} = \deg_{\mathrm{Fl}}$.
3. `proportional'` gives $\deg_S^{\mathrm{wt}} = \mathrm{vol}(S) \deg_{\mathrm{Fl}}$. Since `toWt` is injective (`weight_transform_injective_linear`), $\deg_S = \mathrm{vol}(S) \deg_{S_0}$.
4. Both polynomials are homogeneous of degree $|\Psi|\binom{N}{2} + 1$ (`formPoly_isHomogeneous_and_eval` and `weighted_polynomial_homogeneous_coeff_bound`), so $\delta$ is too.
5. Apply the [adjacent swap relation](/entry/adjacent-swap-height-polynomial-relation/) to $\mathrm{Re}$ and to $\mathrm{Re}_0$. Each gives $\mathrm{PB}^{\mathrm{wt}}(\lambda) + \mathrm{PB}^{\mathrm{wt}}(\lambda \circ s)$ as a linear expression in the degree polynomial. By step 3 and the linearity of `tsgPoly` and `linePoly`, the sum for $\mathrm{Re}$ is $\mathrm{vol}(S)$ times the sum for $\mathrm{Re}_0$, which is $h(\lambda) + h(\lambda \circ s)$. So $\delta(\lambda) + \delta(\lambda \circ s) = 0$.

`mem_antisymSpace_of_pointwise` turns steps 4 and 5 into membership in the space of antisymmetric polynomials `antisymSpace`.

## In the Lean code

The theorem is in [Antisymmetry.lean](lean:Development/AutomorphicSpectrum/Proofs/MetricProofs/Antisymmetry.lean#L19). The statement is in [AgreementIffGuarded.lean](lean:Development/AutomorphicSpectrum/Statements/MetricStatements/AgreementIffGuarded.lean#L82), and `antisymSpace` in [Statements.lean](lean:GroundTheory/HeightsAndTheta/Heights/Antisymmetric/Statements.lean#L37).

The reference system has a flag system for $N$, so its square systems exist for every adjacent pair; the proof uses the one for the pair of each swap. We have not unfolded the analytic system, the mixed integral `mInt` or the flag lines `xLine` and `yLineFl`.
