---
id: kernel-identity
title: The reproducing kernel as a sum of products of theta series
kind: theorem
decl: GlobalTheory.SW.kernel_identity
module: Development.AbelianVarietyTheory.Proofs.SiegelThetaTransformation.KernelIdentity
covers: 784
status: drafted
drafted_by: writer@claude
---
This theorem is the analytic core of [`theta_span`](/entry/theta-span/). It writes a sum over the group $\Delta$ of translates of the reproducing kernel as a finite sum of products of theta series. The proof is the doubling method: the product of two theta series is a theta series on a doubled space, and the [Siegel-Weil formula](/entry/siegel-weil-definite-hermitian-of-four-mul-lt/) replaces it by an Eisenstein series, which unfolds into the sum over $\Delta$.

## Statement

Take the data of [`theta_span`](/entry/theta-span/): a hermitian space `X` of signature $(p_0, q_0)$ with domain $\mathcal{D}$, an even $n$ with $4r < n$, $M > 0$, and a theta system $(\Delta, \mathcal{L}, \Phi, \mu)$. Then there is a constant $\kappa \neq 0$ with the following property. Let $P_1, \dots, P_m$ be row-highest harmonic polynomials of type $(c, c')$ that form an invariant family (`InvFam`). Let $L_1, L_2 \in \mathcal{L}$ and $x_1, x_2 \in \mathcal{D}$. Then the series over $\gamma \in \Delta$
$$\sum_{\gamma \in \Delta} \kappa \cdot \mathrm{cs}_\Lambda\big\langle \Phi(L_1, \Lambda), \Phi(\gamma L_2, \Lambda)\big\rangle \cdot \overline{\mu(\gamma, L_2)} \cdot \mathrm{kern}_P(x_1, \gamma x_2)$$
converges to
$$\mathrm{cs}_\Lambda \sum_{j=1}^m \theta_{P_j}\big(\Phi(L_1, \Lambda)\big)(x_1)\, \overline{\theta_{P_j}\big(\Phi(L_2, \Lambda)\big)(x_2)}.$$
Here $\mathrm{cs}_\Lambda$ is `classSum`, the sum over the classes $\Lambda$ of the genus, weighted by $1/\#\mathrm{Stab}(\Lambda)$. The kernel $\mathrm{kern}_P$ is a derivative in the auxiliary variables of a Gaussian kernel `kZero`. The constant $\kappa$ does not depend on the forms or on $P$.

## Proof

Fix $L_1, L_2$, $x_1, x_2$, and work before the derivatives, with auxiliary variables $z, w$.

1. `doubledHermitianTestFunction_zero_and_norm` gives $\kappa \neq 0$ with $\mathrm{dbl}(\varphi_1, \varphi_2)(0) = \kappa \langle \varphi_1, \varphi_2 \rangle$ for Schwartz-Bruhat $\varphi_1, \varphi_2$.
2. Doubling (`doubledHermitianTestFunction_spec`): the product $\theta(\varphi_1)(x_1)\,\overline{\theta(\varphi_2)(x_2)}$ is `kZero` times the theta series of $\mathrm{dbl}(\varphi_1, \varphi_2)$ at a doubled point.
3. Unfolding (`KernSum.hasSum_eis`): the Eisenstein series of $\mathrm{dbl}$ at the doubled point is a sum over Lagrangians. By `maximalIsotropic_doubled_graph_or_isotropic`, a Lagrangian is the graph of a unique unitary $\gamma$, or it contains the image of a nonzero isotropic vector $\xi$. Graphs of $\gamma \in \Delta$ give the terms of the left side. Graphs of $\gamma \notin \Delta$ give $0$ by the orthogonality axiom. The other Lagrangians give $0$ by the cusp axiom.
4. The difference of the two sides is `kZero` times `swd`, the class sum of theta series minus Eisenstein series. By `isHeat_swd_of_adm` it solves a heat equation. [Siegel-Weil](/entry/siegel-weil-definite-hermitian-of-four-mul-lt/), applied in degree $r$, says that `swd` vanishes at $z = z' = 0$.
5. `invariant_polyDeriv_kills_doubled_heat_solution` shows that the derivatives $P_j(\partial)$, summed over $j$, kill this difference. This uses that the family is invariant.
6. The derivatives pass through the sums by analyticity (`thetaSeries_testFunction_holomorphic_weight` and two private lemmas). This gives the identity.

## In the Lean code

The theorem is in [KernelIdentity.lean](lean:Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation/KernelIdentity.lean#L181), and the unfolding `KernSum.hasSum_eis` is at [L50](lean:Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation/KernelIdentity.lean#L50). The Siegel-Weil formula is used only at $z = z' = 0$; the heat equation and the invariance of $P$ carry it to the derivatives. The functions `wG` and `dbl` are defined by choice, with $0$ as the value when no choice exists. I have not unfolded `kZero` or the doubled points `dblZ` and `dblz`.
