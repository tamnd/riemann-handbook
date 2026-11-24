---
title: The singular case in measure form
decls:
  - GlobalTheory.CompanionTheory.WeilSiegel.HypStep.hyp_step
  - GlobalTheory.T.zero_block_coefficient_rank_increase
  - GlobalTheory.CompanionTheory.WeilSiegel.Free.swFree_singular
  - GlobalTheory.CompanionTheory.WeilSiegel.Free.swFree_block
  - GlobalTheory.T.siegelWeil_free_of_block_nonempty_frames
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The singular case in measure form

This section proves the Siegel-Weil formula in a measure form for a singular Hermitian matrix $T$ in the convergent range $2n < M$. The theta side is a measure on adelic frames, made from the rational frames of $T$ and a fundamental domain of the unitary group. The formula says that this measure is an Euler product of the local fibre measures of the section [Gram fibres and the hyperbolic stage](/entry/local-stages/), with constant 1. The proof is an induction on $n$. The case $T = 0$ adds a hyperbolic plane and uses the two theorems of that section. The case $T \ne 0$ splits off an anisotropic line. The result for block matrices is the input to [the theorem on frames](/entry/siegel-frame/) in the section on the convergent range.

We keep the setting of the previous section: $E/F$ is a CM extension, $J$ is a nondegenerate Hermitian $M \times M$ matrix, and $b$ is a basis of $E/F$. Let $\mathbb{A}$ be the [[adele ring|NYJFYZ0B4M]] of $F$, $\mathbb{A}_\infty = F \otimes_{\mathbb{Q}} \mathbb{R}$ its archimedean part, and $U_J$ the unitary group of $h_J$. For a finite set $S$ of finite places we write $X_v$ for the component of an adelic tuple $X$ at $v$ and $X_\infty$ for its archimedean part.

**Definition 4.2.1 (Standard measures).** A measure $\lambda_\infty$ on $\mathbb{A}_\infty$ is standard if it is an additive Haar measure and some fundamental domain of $\mathcal{O}_F$ in $\mathbb{A}_\infty$ has measure 1. A standard system is a standard $\lambda_\infty$ together with standard measures $\lambda_v$ at all finite places.

**Definition 4.2.2 (Theta measure).** Let $\mu$ be a Haar measure on $U_J(\mathbb{A})$ and let $\mathcal{F}$ be a measurable [[fundamental domain|WEGEXJBX26]] for the left action of $U_J(F)$. For a set $S$ of rational $n$-tuples, the theta measure is the measure on adelic $n$-tuples
$$\Theta_S = \mu(\mathcal{F})^{-1} \sum_{X \in S} (h \mapsto h^{-1} X)_* \bigl(\mu|_{\mathcal{F}}\bigr).$$

So $\int \varphi \, d\Theta_S = \mu(\mathcal{F})^{-1} \int_{\mathcal{F}} \sum_{X \in S} \varphi(h^{-1} X) \, d\mu(h)$ for $\varphi \ge 0$. With $S = \operatorname{Fr}_J(T)$ this is the average over $U_J(F) \backslash U_J(\mathbb{A})$ of the theta series of $\varphi$ attached to the frames of $T$, see [theta kernels](/learn/theta/#theta-kernels).

**Definition 4.2.3 (Euler product measure).** Let $I$ be a measure on adelic $n$-tuples, $c \ge 0$, $m_\infty$ a measure on archimedean tuples and $m_v$ a measure on tuples over $F_v \otimes_F E$ for each finite $v$. For a finite set $S$ of places and functions $\varphi_\infty \ge 0$ and $\varphi_v \ge 0$, let $\varphi_S$ be the function that is 0 unless $X_v \in L_v$ for all $v \notin S$, and is $\varphi_\infty(X_\infty) \prod_{v \in S} \varphi_v(X_v)$ otherwise. We say that $I$ is the Euler product of $(m_\infty, m_v)$ with constant $c$ if three conditions hold.

1. $m_v(L_v) < \infty$ for all $v$.
2. $\sum_v |m_v(L_v) - 1| < \infty$.
3. There is a finite set $S_0$ such that for all finite $S \supseteq S_0$ and all measurable $\varphi_\infty, \varphi_v \ge 0$,
$$\begin{aligned} \int \varphi_S \, dI &= c \int \varphi_\infty \, dm_\infty \prod_{v \in S} \int \varphi_v \, dm_v \\ &\quad \times \prod_{v \notin S} m_v(L_v). \end{aligned}$$

Conditions 1 and 2 make the infinite product converge. Condition 3 says that $I$ is the restricted product of the local measures on functions that are standard outside $S$.

**Definition 4.2.4 (Siegel-Weil property).** Let $T$ be an $n \times n$ Hermitian matrix over $E$. We say that the free Siegel-Weil property holds for $(J, T)$ if the following holds for every basis $b$, every standard system $(\lambda_\infty, \lambda_v)$, every Haar measure $\mu$ on $U_J(\mathbb{A})$ with a fundamental domain $\mathcal{F}$, and all free Gram fibre families $m_\infty$ and $m_v$ for the coordinate measures: the theta measure $\Theta_{\operatorname{Fr}_J(T)}$ is the Euler product of $(m_\infty(T), m_v(T))$ with constant 1. The nondegenerate Siegel-Weil property is the same statement with nondegenerate fibre families and with the set of all rational tuples $X$ with $\operatorname{gr}(X) = T$ in place of the frames.

The constant 1 is the Tamagawa number of $U_J$ seen through the standard measures. For $\det T \ne 0$ each tuple with Gram matrix $T$ is a frame, so the two sets agree in that case.

**Theorem 4.2.5 (Hyperbolic step).** Let $E/F$ be CM, let $J$ be Hermitian and nondegenerate of size $M$, and let $1 \le n$ with $2n < M$. Assume that $\operatorname{Fr}_J(0_n)$ is not empty and that the free Siegel-Weil property holds for $(J, 0_n)$. Then the free Siegel-Weil property holds for $(J^+, 0_{n+1})$, where $J^+$ is the hyperbolic extension of $J$.

Lean: `GlobalTheory.CompanionTheory.WeilSiegel.HypStep.hyp_step` (also `GlobalTheory.T.zero_block_coefficient_rank_increase`, a second name).

*Proof.* Fix the data of the property for $J^+$: a basis $b$, a standard system, a Haar measure $\mu$ on $U_{J^+}(\mathbb{A})$ with a fundamental domain, and free fibre families $m_\infty$, $m_v$ in rank $n+1$. The matrix $J^+$ is again nondegenerate. We need the corresponding data for $J$: the unitary group $U_J$ has a Haar measure $\mu_1$ with a fundamental domain $\mathcal{F}_1$ of finite volume, and free fibre families $m'_\infty$, $m'_v$ in rank $n$ and $m_{1,\infty}$, $m_{1,v}$ in rank 1 for $J^+$ exist. The hypothesis for $(J, 0_n)$ applies to these data and gives an Euler product with constant 1 for the frames of $0_n$ in $E^M$. The rank one case of the property for $J^+$ holds because $M + 2 \ge 3$ ([the rank one case](/entry/siegel-weil-free-zero-rank-one-of-three-le/)).

Now we prove the three conditions for $\Theta_{\operatorname{Fr}_{J^+}(0_{n+1})}$. Conditions 1 and 2 are [the theorem on masses at the isotropic stage](/entry/mass-isotropic/), applied to $m_v$, $m_{1,v}$ and $m'_v$. For condition 3, an Euler product measure with constant 1 exists on the adelic tuples, and the volume of the rank one stage is computed by the rank one theorem. For almost all $v$ the lattice stabiliser in $U_{J^+}(F_v)$ has the standard volume. Let $S$ contain $S_0$ for the rank $n$ and rank one statements and the finitely many exceptional places. For $v \notin S$ and $g$ in the lattice stabiliser, the stage integral of the indicator of $L_v$ is $m'_v(0)(L_v)$, by [the theorem on local stages](/entry/local-stages/). Unfolding the theta series along the first vector of a frame (the [hyperbolic plane unfolding](/entry/hyperbolic-plane-unfolding-integral/)) writes $\int \varphi_S \, d\Theta$ as a rank one theta integral of a stage integral. We apply the rank one property and then the rank $n$ property inside. The partial products over finite sets of places outside $S$ increase to the infinite product. The monotone convergence theorem for a supremum over places then gives the formula of condition 3 with constant 1. $\square$

The hypothesis that $\operatorname{Fr}_J(0_n)$ is not empty is not used in this proof.

Next we treat a general singular matrix. Two facts on Hermitian forms are used. First, if $T$ is singular and not zero, then $T$ takes a nonzero value $t$ on some vector, and $T$ is congruent to $t \oplus T'$ with $T'$ singular of size $n - 1$. Second, if $T = 0$ and $X$ is a frame of $0_{n+2}$ in $E^M$, then $x_1$ is a nonzero isotropic vector, so $h_J$ splits off a hyperbolic plane containing $x_1$: $J$ is congruent to $J_1^+$ with $J_1$ of size $M - 2$, and the remaining vectors give a frame of $0_{n+1}$ in $E^{M-2}$.

**Theorem 4.2.6 (The singular case).** Let $E/F$ be CM and let $J$ be Hermitian and nondegenerate of size $M$. Let $T$ be an $n \times n$ Hermitian matrix with $\det T = 0$ and $2n < M$. If $\operatorname{Fr}_J(T)$ is not empty, then the free Siegel-Weil property holds for $(J, T)$.

Lean: `GlobalTheory.CompanionTheory.WeilSiegel.Free.swFree_singular`.

*Proof.* We use induction on $n$, for all $M$ and $J$ at once. For $n = 0$ the matrix $T$ is empty and $\det T = 1$, so there is nothing to prove.

Let $T$ have size $n + 1$ and suppose $T = 0$. If $n + 1 = 1$, the claim is the rank one case, which holds since $M > 2$ gives $M \ge 3$. If $n + 1 = n' + 2$, take a frame $X$ of $0$. Split $h_J$ at the isotropic vector $x_1$ as above: $J$ is congruent to $J_1^+$ with $J_1$ of size $M_1 = M - 2$, and $\operatorname{Fr}_{J_1}(0_{n'+1})$ is not empty. Since $2(n'+1) < M_1$, the induction hypothesis gives the property for $(J_1, 0_{n'+1})$. [The hyperbolic step](/entry/hyp-step/) gives it for $(J_1^+, 0_{n'+2})$. The property depends only on the congruence class of $J$, so it holds for $(J, 0)$.

Suppose $T \ne 0$. Then $T$ takes a value $t \ne 0$, and $T$ is congruent to $t \oplus T'$ with $T'$ singular of size $n$. A frame of $T$ gives a vector $x$ with $h_J(x, x) = t$. Since $t \ne 0$, the line of $x$ is anisotropic and $h_J$ is congruent to $t \oplus J'$ with $J'$ of size $M - 1$. The other vectors of the frame, projected to the orthogonal complement of $x$, give a frame of $T'$ for $J'$. Since $2n < M - 1$, the induction hypothesis gives the property for $(J', T')$. Extending a frame by the scalar block $t$ gives it for $(t \oplus J', t \oplus T')$. The property is invariant under a congruence of the form and under a congruence of the matrix, so it holds for $(J, T)$. $\square$

A matrix in block form is the shape that the next sections meet.

**Definition 4.2.7 (Block matrix).** Let $t < n$. An $n \times n$ matrix $T$ is in block form of rank $t$ if $T_{ij} = 0$ whenever $i \ge t$ or $j \ge t$ (indices from 0), and the leading $t \times t$ minor of $T$ is not zero.

**Corollary 4.2.8 (Block case).** Let $E/F$ and $J$ be as above. Let $T$ be Hermitian of size $n$ and in block form of rank $t$ for some $t < n$, with $2n < M$. If $\operatorname{Fr}_J(T)$ is not empty, then the free Siegel-Weil property holds for $(J, T)$.

Lean: `GlobalTheory.CompanionTheory.WeilSiegel.Free.swFree_block` (also `GlobalTheory.T.siegelWeil_free_of_block_nonempty_frames`, a second name).

*Proof.* Row $t$ of $T$ is zero since $t < n$, so $\det T = 0$. Apply [the singular case](/entry/sw-free-singular/). $\square$

**Remark 4.2.9 (Formalization).** The hyperbolic step never uses its hypothesis that the frames of $0_n$ exist ([ZeroBlockCoefficientRankIncrease.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeil/ArchimedeanSiegelWeil/PlaceIntegrals/ZeroBlockCoefficientRankIncrease.lean#L78)). The block case discards the nonvanishing of the leading minor and uses only the zero row ([SiegelWeilFreeOfBlockNonemptyFrames.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeil/ArchimedeanSiegelWeil/PlaceIntegrals/SiegelWeilFreeOfBlockNonemptyFrames.lean#L531)), so it holds for every singular $T$. The second names are stated with `first | exact`. Despite its name, the rank increase statement is about the theta measure of isotropic frames, not about a Fourier coefficient. The places $v$ in the Euler product run over the finite places only, and the archimedean place enters through $m_\infty$.
