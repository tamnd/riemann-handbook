---
title: The Hodge metric is good
decls:
  - GlobalTheory.HodgeInvGood.inv_hodgeGram_goodBound
  - GlobalTheory.T.inv_hodgeMetricGram_mumfordGoodGrowth_boundaryChart
  - GlobalTheory.LieBaseGood.lieGram_isGood
  - GlobalTheory.T.hodgeMetric_lieGram_isGood_mumford
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Hodge metric is good

This section proves that the Hodge metric on a Lie base is good in the sense of Mumford: near each boundary point, in a chart where the boundary is a union of coordinate hyperplanes, the metric, the inverse of its determinant, its connection and its curvature grow at most like powers of $\log$ of the distance to the boundary, measured against the Poincaré metric. The input is the [local form of the Hodge metric](/entry/exists-hodge-period-chart/) of the last section. The result is one of the facts that [the good base](/entry/exists-good-base/) supplies to the main theorem.

**Definition 7.6.1 (Good bounds).** Let $S \subseteq \{0, \dots, n-1\}$, $c \in \mathbb{R}$ and $N \in \mathbb{N}$. Let $G$ be a smooth map from an open subset of $\mathbb{C}^n$ to $M_m(\mathbb{C})$, and let $\nabla_a$ and $\Theta_{ab}$ be the matrices of the Chern connection and the curvature of $G$ in the coordinate directions. Put $L(v) = \sum_{a \in S} |\log|v_a||$ and $w_a(v) = |v_a|\,|\log|v_a||$ for $a \in S$, $w_a(v) = 1$ for $a \notin S$. We say that $G$ satisfies the *good bounds* $(S, c, N)$ at $v$ if, for all indices:

1. $|G(v)_{ij}| \leq c\, L(v)^N$;
2. $|\det G(v)|^{-1} \leq c\, L(v)^N$;
3. $|(\nabla_a)_{ij}(v)|\, w_a(v) \leq c$;
4. $|(\Theta_{ab})_{ij}(v)|\, w_a(v)\, w_b(v) \leq c$;
5. $|(\partial_a \nabla_b - \partial_b \nabla_a)_{ij}(v)|\, w_a(v)\, w_b(v) \leq c$.

The weights $w_a$ come from the Poincaré metric $|dz|^2 / (|z| \log|z|)^2$ on the punctured disc. Conditions 3 to 5 say that the connection and curvature forms have bounded norm for the Poincaré metric, and conditions 1 and 2 say that the metric and its inverse have at most logarithmic growth.

**Definition 7.6.2 (Good metric).** Let $h$ be a Hermitian metric on a framed family $\mathcal{E}$ over an open set $O$ of a variety $X$ of dimension $n$. The metric is *good* if for each $y \in X(\mathbb{C})$ not in $O(\mathbb{C})$ there are a holomorphic chart $\phi$ at $y$ and a set $S$ of coordinates such that:

1. $\phi(y)_a = 0$ for $a \in S$;
2. a point $z$ of the chart is outside $O(\mathbb{C})$ if and only if $\phi(z)_a = 0$ for some $a \in S$;
3. there are a frame $A \in S(y)$, $c \in \mathbb{R}$ and $N \in \mathbb{N}$ such that, for $z \in O(\mathbb{C})$ near $y$ and every $\tau$, the Gram family $h_A(\phi^{-1}(\cdot))_\tau$ satisfies the good bounds $(S, c, N)$ at $\phi(z)$.

This is the definition of D. Mumford, "Hirzebruch's proportionality theorem in the non-compact case", Invent. Math. 42 (1977), 239 to 272, for a boundary with normal crossings, written in one frame. The [Background](/learn/abelian-varieties/#mumfords-proportionality-theorem) explains why it is the right condition: the Chern forms of a good metric are integrable and represent the Chern classes of the canonical extension.

**Theorem 7.6.3 (Good bounds for the inverse Hodge Gram matrix).** Let $(r, \tau_0, B_i)$ be a [period chart](/entry/exists-period-chart-of-lat-fam/) on the polydisc in $\mathbb{C}^n$ with boundary coordinates $i < a$, and let $G$ be its Hodge Gram matrix. Then there are $0 < \rho \leq 1/2$, $c$ and $N$ such that at each point $v$ of $\Delta^*_{a,n}$ with $|v_i| < \rho$ for all $i$:

1. $G(v)$ is positive definite;
2. $G^{-1}$ is of class $C^2$ near $v$;
3. $G^{-1}$ satisfies the good bounds $(\{0, \dots, a-1\}, c, N)$ at $v$.

Lean: `GlobalTheory.HodgeInvGood.inv_hodgeGram_goodBound` (also `GlobalTheory.T.inv_hodgeMetricGram_mumfordGoodGrowth_boundaryChart`, a second name).

*Proof.* Write $\ell_i = \ell(v_i) = -\log|v_i| / 2\pi$, so that $G = \operatorname{Im} \tau_0 + \sum_{i < a} \ell_i B_i$. This is a real symmetric matrix, and $\partial \bar\partial G = 0$, since $\operatorname{Im} \tau_0$ is the imaginary part of a holomorphic function and each $\ell_i$ is harmonic. Let $L = \sum_{i < a} |\log|v_i||$.

1. *Chart bounds.* There are $\rho \leq 1/2$, $c_0 > 0$ and $C$ such that, on the punctured polydisc of radius $\rho$,
$$c_0 \cdot 1 \leq G(v) \leq C\Bigl(1 + \sum_i \ell_i\Bigr) \cdot 1$$
as quadratic forms, $G(v)$ is positive definite, and the operator norm of the connection $\nabla_\xi$ of $G$ is at most $C$ times the Poincaré length of $\xi$. The upper bound holds since $\tau_0$ is bounded near $0$. The lower bound uses the block form of the period chart: on the $r \times r$ block, $\sum_i \ell_i B_i$ is large and positive definite when the $v_i$ are small; on the complementary block, $\operatorname{Im} \tau_0$ is positive definite; and a Schur complement estimate controls the off-diagonal blocks. The connection is $\nabla = G^{-1} \partial G$, and $\partial G$ is $\partial \operatorname{Im} \tau_0$ plus the terms $B_i\, \partial \ell_i$ with $|\partial_i \ell_i| = 1/(4\pi |v_i|)$. A uniform bound on $\ell_i\, G^{-1} B_i$ then bounds $\nabla$ by the Poincaré metric.
2. *Entries and determinant.* On the punctured polydisc of radius $1/2$, $\sum_i |\log|v_i|| = 2\pi \sum_i \ell_i$, and this sum is at least $\log 2$ when $a > 0$. From $G \geq c_0$, the entries of $G^{-1}$ are at most $1/c_0 \leq c_0^{-1} (\log 2)^{-g} L^g$. From $G \leq C(1 + L/2\pi)$, $|\det G^{-1}|^{-1} = |\det G| \leq g!\, (C(1 + L/2\pi))^g$, which is at most a constant times $L^g$. This gives conditions 1 and 2 with $N = g$. If $a = 0$, the same bounds hold with $N = 0$.
3. *Connection and curvature.* Since $G$ is symmetric, the connection of $G^{-1}$ is $-\nabla_\xi^{\mathsf{T}}$. Since $G$ is real symmetric and $\partial\bar\partial G = 0$, the curvature of $G^{-1}$ is $-\bigl((\nabla_\eta^{\mathsf{T}})^* \nabla_\xi\bigr)^{\mathsf{T}}$, and $\partial_\xi \nabla_\eta - \partial_\eta \nabla_\xi$ for $G^{-1}$ is $-[\nabla_\eta, \nabla_\xi]^{\mathsf{T}}$. So all three are bounded by the bound on $\nabla$ of step 1 and its square. The Poincaré length of the coordinate vector $e_k$, times the weight $w_k(v)$, is at most $5$. This gives conditions 3 to 5, with $c$ a multiple of $\max(C, C^2)$. $\square$

**Theorem 7.6.4 (The Hodge metric is good).** Let $X, j, f, \mathcal{E}, A_0$ be a Lie base, with open part $O$ and Hodge metric $h$. Then $h$ is a good metric on $\mathcal{E}$ over $O$.

Lean: `GlobalTheory.LieBaseGood.lieGram_isGood` (also `GlobalTheory.T.hodgeMetric_lieGram_isGood_mumford`, a second name).

*Proof.* Let $y \in X(\mathbb{C})$ be outside $O(\mathbb{C})$. The [period chart on a Lie base](/entry/exists-hodge-period-chart/) gives a chart $\phi$ at $y$ onto the polydisc, with boundary $\{z_i = 0 \text{ for some } i < a\}$, a period chart with Hodge Gram matrix $G$, a frame $A$ and holomorphic matrices $Q_\tau$ with independent rows at $0$, $\sum_\tau m_\tau = g$, such that $h_A = Q_\tau\, G^{-1}\, Q_\tau^*$ on $O$, with orthogonal cross terms. Take $S = \{0, \dots, a-1\}$. Conditions 1 and 2 of a good metric hold by the form of the chart.

The [good bounds for the inverse Hodge Gram matrix](/entry/inv-hodge-gram-good-bound/) give $\rho$, $c_0$, $N_0$ with good bounds for $G^{-1}$ on the punctured polydisc of radius $\rho$. Let $W$ be the intersection of the image of the chart, of $O$ and of this punctured polydisc. It is open.

It remains to move the bounds from $G^{-1}$ to $Q_\tau\, G^{-1}\, Q_\tau^*$. Since the rows of the matrices $Q_\tau$ together form an invertible $g \times g$ matrix $Q$ near $0$, the family $Q\, G^{-1}\, Q^*$ is $G^{-1}$ in a holomorphic frame, and the cross terms vanish. So it is block diagonal with the blocks $h_{A,\tau}$. Under a holomorphic change of frame with invertible values on a ball, the good bounds hold again, with new constants $c'$, $N'$, on a smaller ball: the entries and the determinant change by bounded factors; the connection changes by $Q^{-1} \partial Q$, which is bounded; and the curvature changes by conjugation. For a block diagonal metric, the connection and the curvature are block diagonal, so each block satisfies the bounds. Finally the bounds depend only on the germ of the Gram family at the point, so they hold for $h_A(\phi^{-1}(\cdot))_\tau$ at all points of $O$ near $y$. $\square$

**Remark 7.6.5.** Mumford proves that the invariant metric on an automorphic bundle of a locally symmetric variety is good, by a reduction to the nilpotent orbit form (Mumford, Invent. Math. 42 (1977), 239 to 272). The proof here uses only the period chart of abelian varieties with $\mathcal{O}_E$-action, which is the case of unitary Shimura varieties.

**Remark 7.6.6 (Formalization).** The good bounds are the structure `GoodBound` and the good metric is `IsGood` in [InterPolyProdSum.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/InterPolyProdSum.lean#L95). The connection `conn`, the curvature `curv` and the derivative `mdel` were not unfolded; we read them by their names and by the lemmas about them. The coordinates are indexed from $0$, and the boundary set is the image of $\{0, \dots, a-1\}$ in $\{0, \dots, n-1\}$. The chart bounds of step 1 are `hodgeChartBounds_of_schur_lemW` in [HodgeChartBoundsOfSchurLemW.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HodgeChartBoundsOfSchurLemW.lean#L41). It takes the Schur complement estimate and the uniform bound on $t_i (Y + \sum_l t_l B_l)^{-1} B_i$ as hypotheses, and the proof of the theorem supplies them as the lemmas `schur_complement_block_quadratic_lower_bound` and `exists_uniform_bound_smul_inv_add_sum_mul_mulVec`. The formula for the connection of the inverse is `conn_inv` in [InvHodgeMetricGramMumfordGoodGrowthBoundaryChart.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/InvHodgeMetricGramMumfordGoodGrowthBoundaryChart.lean#L27). The formulas for the curvature and for $\partial_\xi \nabla_\eta - \partial_\eta \nabla_\xi$, the bound $5$ and the bound $\log 2$ are the lemmas `chernCurvature_inverse_realSymmetric_gram`, `holomorphicDeriv_chernConnection_inverseSymmetricGram`, `poincareNorm_coordinateVector_mul_length_le_five` and `puncturedPolydisc_sum_negLog_eq_and_ge_logTwo`, whose proofs we did not open. The exponent is `if a = 0 then 0 else g` (line 83). The frame change and the move to an equal germ are `mumfordGoodGrowthBound_frameChange_orthogonalSummands` and `mumfordGoodGrowthBound_congr_germ_gram`. Both are second names, proved by `first | exact @…` from `FrameGood.frame_summands_goodBound` and `GoodMetric.goodBound_congr_nhds`. The frame change asks for orthogonality only at the points of the open set $W$.
