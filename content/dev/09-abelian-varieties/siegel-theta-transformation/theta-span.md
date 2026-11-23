---
id: theta-span
title: Bounded forms are finite sums of hermitian theta series
kind: theorem
decl: GlobalTheory.SW.SpanMain.theta_span
module: Development.AbelianVarietyTheory.Proofs.SiegelThetaTransformation.HermitianThetaSeriesSpanBoundedForms
covers: 975
status: drafted
drafted_by: writer@claude
---
This theorem proves that, for a theta system, each bounded holomorphic form of the right weight is a finite linear combination of theta series. It is the proof of [`hermitianTheta_series_span_bounded_forms`](/entry/hermitian-theta-series-span-bounded-forms/), and through it of [`level_theta_span`](/entry/level-theta-span/). The method is a reproducing kernel: the form is an integral of itself against a kernel, and the [kernel identity](/entry/kernel-identity/) writes the kernel as a sum of products of theta series.

## Statement

The data are a CM field $E$, a [[Hermitian form|48P4A1CX85]] `X : Data E r` of signature $(p_0, q_0)$ with domain $\mathcal{D}$ (`X.dom`, a set of frames), an even $n$ with $4r < n$, and $M > 0$. A theta system (`IsSystem`) is a group $\Delta$ of unitary matrices, a $\Delta$-stable set $\mathcal{L}$ of full lattices in $E^r$, test functions $\Phi(L, \Lambda)$ indexed by $L \in \mathcal{L}$ and by lattices $\Lambda$ in the genus `Vset`, and a multiplier $\mu$ with $|\mu| = 1$. Its axioms say:

- $\Delta$ moves $\Phi(L, \Lambda)$ to $\mu\,\Phi(\gamma L, \Lambda)$, and unitary $\gamma \notin \Delta$ give orthogonal functions;
- the Gram matrix $\langle \Phi(L, \Lambda), \Phi(L', \Lambda)\rangle$ has constant diagonal $a$, and its off-diagonal part is small (row sums at most $\theta a$ with $\theta < 1$);
- a cusp condition, and the admissibility of the doubled family.

A form (`IsForm`) is a function $F(L, x)$ on $\mathcal{L} \times \mathcal{D}$ that is holomorphic in $x$, equivariant under the Borel subgroup with weight `wtOf c c' n`, satisfies $F(\gamma L, \gamma x) = \mu(\gamma, L)^{-1} F(L, x)$, and is bounded in the norm `pnorm`. The conclusion `InSpan` is: there are finitely many $\Lambda_i$, row-highest harmonic polynomials $P_i$ of type $(c, c')$ and $a_i \in \mathbb{C}$ with
$$F(L, x) = \sum_i a_i\, \theta_{P_i}\big(\Phi(L, \Lambda_i)\big)(x)$$
for all $L \in \mathcal{L}$ and $x \in \mathcal{D}$. Here $\theta_P(\varphi)$ is the derivative $P(\partial)$ of a Siegel theta series of $\varphi$.

## Proof

1. Choose an invariant family $P_1, \dots, P_m$ of row-highest polynomials, not all zero (`exists_invFam_rowHighest`).
2. Let $C(L, L')$ be the class sum over $\Lambda$ of $\langle \Phi(L, \Lambda), \Phi(L', \Lambda)\rangle$. By `lattice_operator_coefficients`, $C$ is $a$ on the diagonal, its off-diagonal row sums are at most $\theta a$, and it is $\Delta$-equivariant.
3. Since $\theta < 1$, the operator $F' \mapsto \sum_{L'} C(\cdot, L') F'$ is invertible by a Neumann series. `Neumann.main` gives a form $F'$ with $F(L, x) = \sum_{L'} C(L, L') F'(L', x)$.
4. On a thin slab of $\mathcal{D}$, the kernel $\mathrm{kern}_P$ reproduces bounded forms: $\int_{\text{slab}} \mathrm{kern}_P(x, y) F'(L', y)\,dy = \rho\, F'(L', x)$ with $\rho > 0$ (`thin_slab`, `kern_integrableOn_slab`, `kern_reproducing`). `bound_on` bounds $F'$ on the slab.
5. Thus $\rho F(L, x) = \sum_{L'} \int C(L, L')\,\mathrm{kern}_P(x, y) F'(L', y)\,dy$. Unfold the sum over $L'$ into a sum over $\Delta$ and a fundamental domain (`unfold_frames`). The [kernel identity](/entry/kernel-identity/) turns the sum over $\Delta$ into a finite sum of products $\theta_{P_j}(\Phi(L, \Lambda))(x)\,\overline{\theta_{P_j}(\Phi(L', \Lambda))(y)}$. The classes $\Lambda$ are finite in number (`finite_cls_and_stab`).
6. So $\rho F(L, x)$ is a finite combination of the $\theta_{P_j}(\Phi(L, \Lambda))(x)$. Divide by $\rho$.

## In the Lean code

The theorem is in [HermitianThetaSeriesSpanBoundedForms.lean](lean:Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation/HermitianThetaSeriesSpanBoundedForms.lean#L168). The local helpers `unfold_span` ([L22](lean:Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation/HermitianThetaSeriesSpanBoundedForms.lean#L22)), `bound_on` (L87) and `unfold_frames` (L130) are in the same file. `IsSystem`, `IsForm` and `InSpan` are in [IsSystem.lean](lean:Development/AbelianVarietyTheory/Definitions/SpanningFamilies/IsSystem.lean#L113). I have not unfolded `pnorm` or the proofs of the slab lemmas.
