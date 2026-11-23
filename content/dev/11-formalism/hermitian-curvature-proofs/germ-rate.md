---
id: germ-rate
title: The germ expansion with a rate
kind: theorem
decl: Formalism.FourierDecayAlt.P.germ_rate
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.ChangeOfVariablesXy
covers: 772
status: drafted
drafted_by: writer@claude
---
This theorem compares an orbital integral at a point near a block matrix with a finite sum of orbital integrals at long Weyl points. The error is of size $O(|t|)$. It has no hypothesis. The Lean code uses it to get the weaker germ expansion `Germ` and the germ inputs of the definite side. So its parent is the trunk node [HypsAlt is nonempty](/step/nonempty-hyps/). The proof is a stationary phase argument, split into thirteen proved steps.

## Statement

Fix $\beta \ne 0$ and let $\psi(w) = \exp(i\,\mathrm{Re}(\beta w))$. Each integral below uses $(|\beta|/2\pi)$ times Lebesgue measure in each complex coordinate. Let $n = m + 2$, let $w$ be the antidiagonal permutation matrix, and let $\Phi$ be a function on $n \times n$ complex matrices with values in a Banach space. Put
$$\Omega(z) = \int_U \psi\Big(\sum_i u_{i,i+1}\Big)\,\Phi(z\,w\,u)\,du,$$
with $U$ the upper unipotent group. Let $\Omega_B(t, c)$ be the integral of $\Phi(\ell\,\mathrm{diag}(t\,w', c)\,u')$ against the same type of character. Here $\ell$ is unipotent with free entries only in the last row, $w'$ is the antidiagonal matrix of size $n - 1$, and $u'$ is upper unipotent.

**Theorem.** There are $C_1, C_2 \in \mathbb{N}$ with the following property. For each $m$, each $\beta \ne 0$ and each compact $K_c \subset \mathbb{C} \setminus \{0\}$, there is a constant $C$ such that
$$\Big\| |t|^{(m+1)^2}\,\Omega_B(t, c) - \frac{1}{m+2}\sum_{z^{m+2} = (-1)^{m+3} c\,t^{m+1}} |z|^{(m+1)^2}\,\psi\Big(\frac{(m+2)z}{t}\Big)\,\Omega(z) \Big\| \le C\,K\,|t|$$
for all $t \ne 0$ with $c\,t^{m+1} \in K_c$. The condition on $\Phi$ is this. For some $A \ge C_1 (m+2)^2$ and $k \ge C_2 (m+2)^2$, $\Phi$ is $C^k$ at each $Z$ with $\det Z \in \det(w) K_c$, and its first $k$ derivatives there are bounded by $K \min(1, \|Z\|^{-A})$.

## Proof

For large $|t|$ a separate step (`GermLargeT`) gives the bound. For small $|t|$ the proof splits $\Phi$ with a cutoff. A tail step bounds the part far out. On the rest, a change of variables to coordinates $(x, y)$ turns $\Omega_B$ into an oscillatory integral. The roots $z$ of $z^{m+2} = (-1)^{m+3} c\,t^{m+1}$ give its critical points. A partition of unity puts a cutoff near each root and one cutoff away from all of them. Nonstationary phase bounds the far part by $O(|t|)$. Stationary phase at each root gives the term $|z|^{(m+1)^2}\psi((m+2)z/t)$ times a limit amplitude. Two more steps identify that limit with $\Omega(z)$. The rest is algebra on the error terms. We have not unfolded the thirteen step statements beyond these roles.

## In the Lean code

The theorem is at [ChangeOfVariablesXy.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/ChangeOfVariablesXy.lean#L34). It applies `germ_rate_of_estimates` ([StationaryPhaseEstimates.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/StationaryPhaseEstimates.lean#L687)) to thirteen proved facts. The statement `GermRate` is in [StatementG.lean](lean:Formalism/HermitianCurvature/StatementG.lean#L100). The phase in the sum is the constant 1. `Germ` (line 92) allows an unknown unit phase and only asks that the error goes to 0. The next declaration, `germExpansion_true`, gets `Germ` from this theorem. Two of the thirteen inputs, `critical_cutoff_spec` and `stationary_leading_constant`, are not used by `germ_rate_of_estimates`. The first one enters the proof through the stationary and nonstationary steps.
