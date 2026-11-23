---
id: phi-zero-hermitian-curvature
title: The top vector as a twisted unipotent integral
kind: theorem
decl: Formalism.FourierDecayAlt.P.phi_zero_hermitian_curvature
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.PBTAsm
covers: 475
status: drafted
drafted_by: writer@claude
---
This theorem proves `PhiZero`. At one real place, the vector `p.V F` at each local point of level $r + 1$ is a twisted unipotent integral `PhiTop` of one smooth function $\Phi_0$ with compact support. It has no hypothesis. The proof is an assembly: it gives three proved facts to `phi_zero_of_parts`. The Lean code uses it for the density constant `density_constant` and in several other proofs below the trunk node [HypsAlt is nonempty](/step/nonempty-hyps/). The name has the words "hermitian curvature" only from the folder. The statement has no curvature in it.

## Statement

Fix the data $p$ at one real place, with parameters $k$, $r$ and finite-dimensional spaces $W_p$, $W_q$. Let $F$ be a coefficient that satisfies `CptCoef`. For a permutation $\sigma$ and $d \in \mathbb{C}^{r+1}$, `PhiTop` integrates $\psi_H(\eta)\,\Phi_0(Z(\sigma, d, \eta))$ over a space of variables $\eta$, with a character $\psi_H$. We have not unfolded $\psi_H$ or $Z$.

**Theorem.** There is $\Phi_0$ on $(r+1) \times (r+1)$ complex matrices, with values in $\operatorname{Hom}(W_q, W_p)$, such that:

1. $\Phi_0$ is smooth and has compact support;
2. $\det Z \ne 0$ on the support of $\Phi_0$;
3. for each local point $a$ of level $r + 1$, and each $(\sigma, d)$ whose matrix `hMat` is the point matrix of $a$, the vector `p.V F a` equals `PhiTop` of $\Phi_0$ at $(\sigma, d)$.

## Proof

Let $g(M) = |\det M|^2 - T\,|\det M'|^2$, with $M'$ the upper left $r \times r$ block and $T$ a constant of $p$. Put $\phi_0(Z) = I(s(Z))$ where $g(Z) > 0$, and $\phi_0(Z) = 0$ otherwise. Here $I$ is a fibre integral of `B.rho` applied to $F$, against measures that are Haar on two sets `N0set`. We have not unfolded `B.rho`. The map $s$ is a section: it is smooth on $\{g > 0\}$, and $s(Z)$ is a point over $Z$ with a frame condition. The three facts are:

1. `pbi_sectionExists_proof`: a section $s$ exists.
2. `fibre_integral_smooth`: $\phi_0$ is smooth for each section.
3. `fibre_integral_cells`: there are Haar measures and a constant $c$ such that `p.V F a` is `PhiTop` of $c\,\phi_0$, for each section.

Then $\Phi_0 = c\,\phi_0$. The support conditions come from `phi_zero_support`. It uses `CptCoef` to show that $\phi_0$ has compact support inside the invertible matrices.

## In the Lean code

The theorem is at [PBTAsm.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/PBTAsm.lean#L10). `phi_zero_of_parts`, `phi0` and the three statements are in [SupportPhiZeroSubset.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/SupportPhiZeroSubset.lean#L218). `PhiZero` is in [RealInputsClosedAdmissibleSettings.lean](lean:Formalism/HermitianCurvature/RealInputsClosedAdmissibleSettings.lean#L245), and `PhiTop` in [StatementU.lean](lean:Formalism/HermitianCurvature/StatementU.lean#L670). The three facts are proved in [ExistsMeasurableSection.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/ExistsMeasurableSection.lean#L462), [AutomorphicInSphericalLevel.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/AutomorphicInSphericalLevel.lean#L362) and [FibreIntegralCells.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/FibreIntegralCells.lean#L61).
