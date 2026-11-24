---
title: Isotropic lines and local averages
decls:
  - GlobalTheory.CompanionTheory.WeilSiegel.Free.EstZero.estimate_zero
  - GlobalTheory.T.global_volume_rank_one_normalised
  - GlobalTheory.CompanionTheory.SW.OneZero.one_vector_zero
  - GlobalTheory.T.siegelWeilFree_zero_rank_one_of_three_le
  - GlobalTheory.CompanionTheory.WhitFree.AvgInf.avgInf_tendsto
  - GlobalTheory.T.archimedean_siegel_weil_measure
  - GlobalTheory.CompanionTheory.AvgFree.exhaust_density
  - GlobalTheory.CompanionTheory.AvgFree.avgFree_tendsto
  - GlobalTheory.T.local_siegel_weil_unramified_measure
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Isotropic lines and local averages

This section proves two kinds of results. The first is the free Siegel-Weil property for a single isotropic vector, $\mathrm{SWFree}(J, 0_1)$ for $M \ge 3$. It is the base of the induction in [the singular case](/entry/sw-free-singular/), and together with the [unfolding along an isotropic vector](/entry/unfold-frames/) it gives every isotropic frame. The second kind identifies the Gram fibre measures $m_\infty$ and $m_v$ of [the section on Gram fibres](/entry/local-stages/) as limits of averages over small neighbourhoods of a Gram matrix. These limits are how the coefficient side of the [Eisenstein series](/learn/automorphic-forms/#eisenstein-series) meets the fibre measures.

The proof of $\mathrm{SWFree}(J, 0_1)$ follows Siegel's Hauptsatz. Invariance and local finiteness force the theta measure of the isotropic vectors to be an Euler product of the local fibre measures up to a constant $c$. A lattice point count then shows $c = 1$, since the main term grows faster than the error.

### The isotropic count

Fix a CM extension $E/F$ and a nondegenerate Hermitian $J$ of size $M$. For each finite place $v$ let $L_v$ be a lattice in $E_v^M$, equal to $\mathcal{O}_{E_v}^M$ for almost all $v$. We write $\operatorname{proj}_\infty X$ for the archimedean component of an adelic vector.

**Theorem 4.12.1 (Isotropic count with error).** Let $3 \le M$, and let $m_\infty$ and $m_v$ be free Gram fibre families. There are a continuous $\varphi > 0$ on $E_\infty^M$ with $\int \varphi \, dm_\infty(0) < \infty$ and a constant $C$ such that for every integer $a > 0$
$$\Bigl| I(a) - \int \varphi \, dm_\infty(0) \prod_v m_v(0)(a^{-1} L_v) \Bigr| \le C a^{[F:\mathbb{Q}] M},$$
where $I(a)$ is the theta integral, over the nonzero isotropic vectors, of $\varphi(\operatorname{proj}_\infty X)$ times the indicator of $\{X : a X_v \in L_v \text{ for all } v\}$.

Lean: `GlobalTheory.CompanionTheory.WeilSiegel.Free.EstZero.estimate_zero` (also `GlobalTheory.T.global_volume_rank_one_normalised`, a second name).

*Proof.* Take $\varphi$ to be a Gaussian $\varphi(x) = \exp(-\pi \, {}^t\bar{x} P x)$, built from a positive definite $P$ and the Gram matrix $B$ of the trace form. Unfolding the theta integral gives a sum of $\varphi$ over the isotropic points of the lattice $a^{-1} L$. Split the isotropic vectors by the fibre map: the count of lattice points of $a^{-1}L$ on the isotropic cone, weighted by $\varphi$, is a Riemann sum for the fibre measure $m_\infty(0)$ times the density of the cone in $a^{-1}L$. The density is the product of the local volumes $m_v(0)(a^{-1}L_v)$. The difference between the sum and the integral is bounded by the number of lattice points in a shell of width $O(1)$, which is $O(a^{[F:\mathbb{Q}] M})$ because $\varphi$ decays and the lattice $a^{-1}L$ has $a^{2[F:\mathbb{Q}]M}$ points per unit volume on a space of real dimension $2[F:\mathbb{Q}]M$, while the cone has real codimension $[F:\mathbb{Q}]$. $\square$

The main term grows like $a^{[F:\mathbb{Q}](2M-2)}$, since the cone has real dimension $[F:\mathbb{Q}](2M-1)$ and the fibre measure scales by $a^{-[F:\mathbb{Q}](2M-2)}$ under $x \mapsto a^{-1}x$. For $M \ge 3$ this beats $a^{[F:\mathbb{Q}]M}$.

**Theorem 4.12.2 (Free Siegel-Weil for one isotropic vector).** Let $E/F$ be CM and $J$ nondegenerate of size $M \ge 3$ with a nonzero rational isotropic vector. Then $\mathrm{SWFree}(J, 0_1)$ holds.

Lean: `GlobalTheory.CompanionTheory.SW.OneZero.one_vector_zero` (also `GlobalTheory.T.siegelWeilFree_zero_rank_one_of_three_le`, a second name).

*Proof.* Fix free Gram fibre families. The theta measure $\Theta$ of the nonzero isotropic vectors is locally finite and invariant under $U_J(\mathbb{A})$ (`theta_measure_locally_finite_invariant`). The local fibre measures $m_\infty(0)$ and $m_v(0)$ are also invariant, and on the isotropic cone an invariant locally finite measure is determined by its values on product sets up to a scalar (`global_volume_rank_one_product`, `finite_volume_rank_one_product`). A test set with positive finite volume (`exists_test_set`) and the renormalised infinite product (`infinite_product_renormalization`) give a constant $c$ with
$$\Theta = c \cdot m_\infty(0) \otimes \prod_v m_v(0),$$
that is, $\Theta$ is an Euler product with constant $c$.

Apply this to the test function of the isotropic count. The left side is $I(a)$ and the right side is $c$ times the main term. The main term equals $w \kappa a^{[F:\mathbb{Q}](2M-2)}$ with $w = \int \varphi \, dm_\infty(0) > 0$ and $\kappa > 0$ the product of the $m_v(0)(L_v)$ (`finite_volume_rank_one_euler`). So
$$|c - 1| \, w \kappa \, a^{[F:\mathbb{Q}](2M-2)} \le |C| \, a^{[F:\mathbb{Q}] M}$$
for every integer $a > 0$. Since $2M - 2 > M$, dividing and letting $a$ grow gives $c = 1$. In the Lean proof this is a contradiction: if $c \ne 1$ the inequality $|c - 1| w \kappa a \le |C|$ fails for large $a$. $\square$

### Archimedean averages

The fibre measure $m_\infty(c)$ is a measure on the tuples $X$ with $\operatorname{gr}(X) = c$. It can be recovered by thickening the fibre. For a function $\rho$ on Hermitian $n \times n$ matrices let $\operatorname{gramTest}(c, \rho)(X) = \rho(\operatorname{gr}(X) - c)$.

**Theorem 4.12.3 (Archimedean average).** Let $0 < n$ with $2n < M$, let $m_\infty$ be a free Gram fibre family at the archimedean places, and let $\varphi$ be an archimedean [Schwartz function](/learn/analysis/#the-fourier-transform). Then $\varphi$ is measurable and $m_\infty(c)$-integrable for every Hermitian $c$. Let $\rho_k \ge 0$ be continuous with compact support and positive integral, with supports shrinking to $0$. Then $\varphi \cdot \operatorname{gramTest}(c, \rho_k)$ is integrable for each $k$, and
$$\frac{\int \varphi(X) \, \rho_k\bigl(\operatorname{gr}(X) - c\bigr) \, dX}{\int \rho_k} \longrightarrow \int \varphi \, dm_\infty(c).$$

Lean: `GlobalTheory.CompanionTheory.WhitFree.AvgInf.avgInf_tendsto` (also `GlobalTheory.T.archimedean_siegel_weil_measure`, a second name).

*Proof.* Pass to complex coordinates at each archimedean place. On the open set of linearly independent tuples the Gram map is a submersion when $2n < M$, so Lebesgue measure disintegrates along it with the fibre measures $m_\infty(c)$ as conditional measures; this is the defining property of a free fibre family. The fibre measures move continuously in $c$, by a shear that carries one fibre to a nearby one and preserves Lebesgue measure. So $c \mapsto \int \varphi \, dm_\infty(c)$ is continuous, and the averages against $\rho_k$ converge to its value at $c$. The set of linearly dependent tuples has measure zero for Lebesgue measure and for each fibre. Integrability uses the growth of box volumes, $m_\infty(c)$ of a box of side $R$ is $O(R^{2[F:\mathbb{Q}](nM - n^2)})$, against the decay of $\varphi$, and the compactness of the good set of linearly independent tuples in a box (`good_set_compact_linearly_independent`). $\square$

### Finite averages

At a finite place $v$ the analogue uses compact open sets. For a compact open $A$ of $n$-tuples in $E_v^M$ and a set $Y$ of Hermitian matrices, write $\operatorname{gramIn}(Y) = \{X : \operatorname{gr}(X) \in Y\}$ and $\operatorname{gramNear}(c, U) = \operatorname{gramIn}(c + U)$.

**Theorem 4.12.4 (Exhaustion with density).** Let $v$ be finite, $0 < n$ and $2n < M$, and let $A$ be compact open. There are compact open sets $T_1 \subseteq T_2 \subseteq \dots \subseteq A$ of linearly independent tuples, whose union is the set of linearly independent tuples in $A$, and numbers $\varepsilon_j \to 0$, such that
$$\operatorname{vol}\bigl((A \setminus T_j) \cap \operatorname{gramIn}(Y)\bigr) \le \varepsilon_j \operatorname{vol}(Y)$$
for every measurable $Y$.

Lean: `GlobalTheory.CompanionTheory.AvgFree.exhaust_density`.

*Proof.* Let $T_j$ be the tuples in $A$ whose minors of size $n$ do not all lie in $\varpi^j \mathcal{O}$. These are compact open, increasing and exhaust the independent tuples. The complement $A \setminus T_j$ is covered by scaled copies of a fixed set of nearly dependent tuples. For each copy, the volume of the part with Gram matrix in $Y$ is at most a constant times $\operatorname{vol}(Y)$, by the scaling of the Gram map (`scale_density`). The volume of the nearly dependent tuples with Gram matrix in $Y$ tends to $0$ relative to $\operatorname{vol}(Y)$, by a density bound that uses $2n < M$ (`bad_density`). $\square$

**Theorem 4.12.5 (Finite average).** Let $v$ be finite, $0 < n$ and $2n < M$, let $m_v$ be a free Gram fibre family at $v$, let $A$ be compact open, and let $U_k$ be compact open neighbourhoods of $0$ shrinking to $0$. Then
$$\frac{\operatorname{vol}\bigl(A \cap \operatorname{gramNear}(c, U_k)\bigr)}{\operatorname{vol}(U_k)} \longrightarrow m_v(c)(A).$$

Lean: `GlobalTheory.CompanionTheory.AvgFree.avgFree_tendsto` (also `GlobalTheory.T.local_siegel_weil_unramified_measure`, a second name).

*Proof.* On each $T_j$ the Gram map is locally a projection in suitable coordinates, since the tuples are independent. So for $k$ large the set $T_j \cap \operatorname{gramNear}(c, U_k)$ is a union of translates of $U_k$ times pieces of the fibre, and its volume divided by $\operatorname{vol}(U_k)$ equals $m_v(c)(T_j)$ exactly (`local_fibre_measure_unramified_volume`). The rest, $A \setminus T_j$, contributes at most $\varepsilon_j$ by exhaustion with density, applied to $Y = c + U_k$. Letting $k$ and then $j$ go to infinity gives the limit, since $m_v(c)(T_j) \to m_v(c)(A)$ by monotone convergence and the dependent tuples have $m_v(c)$-measure zero. $\square$

The archimedean and finite averages say that the fibre measures are the measures used in the coefficient formulas. They are used in [Whittaker integrals and fibre measures](/entry/whit-eq-integral/) and in the finite place computation of [Section 4.14.3](/entry/loc-fin-x/).

**Remark 4.12.6 (Formalization).** The names in `GlobalTheory.T` are stated with `first | exact` ([GlobalVolumeRankOneNormalisedStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/GlobalVolumeRankOneNormalisedStatement.lean#L8), [SiegelWeilFreeZeroRankOneOfThreeLeStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/SiegelWeilFreeZeroRankOneOfThreeLeStatement.lean#L8), [ArchimedeanSiegelWeilMeasureStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/ArchimedeanSiegelWeilMeasureStatement.lean#L13), [LocalSiegelWeilUnramifiedMeasureStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/LocalSiegelWeilUnramifiedMeasureStatement.lean#L13)). Three file names do not match their content. `GlobalVolumeRankOneNormalised` is the error estimate, not a normalisation ([GlobalVolumeRankOneNormalised.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/GlobalVolumeRankOneNormalised.lean#L183)). `ArchimedeanSiegelWeilMeasure` is the limit of averages ([ArchimedeanSiegelWeilMeasure.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/ArchimedeanSiegelWeilMeasure.lean#L153)). `LocalSiegelWeilUnramifiedMeasure` has no unramified hypothesis, and the finite average holds at every finite place ([LocalSiegelWeilUnramifiedMeasure.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/LocalSiegelWeilUnramifiedMeasure.lean#L297), [L393](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/LocalSiegelWeilUnramifiedMeasure.lean#L393)). The proof of $c = 1$ in [SiegelWeilFreeZeroRankOneOfThreeLe.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/SiegelWeilFreeZeroRankOneOfThreeLe.lean#L26) is by contradiction with a linear bound in $a$, after dividing both growth rates. The lemmas named in the proofs are second names that we follow by name and statement; the sketches above give the classical argument they encode.
